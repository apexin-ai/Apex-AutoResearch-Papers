# Per-layer KL training: each step masks only 1 random layer, others stay dense.
# Demonstrates end-to-end coupling value — training layers independently vs jointly.
# The confound (train single-layer, infer all-layer) is intentional:
# if per-layer PPL is much worse than end-to-end KL, it proves cross-layer coupling matters.
#
# Input:  frozen Llama model + calibration data (wikitext-103)
# Output: predictor_perlayer_kl.pt (same format as KL/BCE checkpoints for benchmark_eval.py)
#
# Usage:
#   python train_perlayer_kl.py --num_steps 10000 --sparsity_target 0.3 --seed 42 --gpu 0

import argparse
import importlib.util
import math
import os
import random
import sys
import time

import torch
import torch.nn.functional as F
import wandb
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_utils import get_calibration_loader, get_random_loader
from losses import KLDistillLoss
from predictor import PredictorWrapper


def parse_args():
    p = argparse.ArgumentParser(
        description="Per-layer KL training: each step masks 1 random layer"
    )
    p.add_argument("--model_name_or_path", type=str,
                    default="/root/autodl-tmp/models/llama-3.1-8b")
    p.add_argument("--num_steps", type=int, default=10000)
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--seq_len", type=int, default=2048)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--sparsity_target", type=float, default=0.3)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--output_dir", type=str,
                    default="/root/distill_sparse_swiglu/checkpoints")
    p.add_argument("--wandb_project", type=str, default="distill_sparse_swiglu")
    p.add_argument("--wandb_run_name", type=str, default=None)
    p.add_argument("--tau_start", type=float, default=1.0)
    p.add_argument("--tau_end", type=float, default=0.1)
    p.add_argument("--warmup_steps", type=int, default=100)
    p.add_argument("--log_every", type=int, default=100)
    p.add_argument("--use_random_data", action="store_true",
                    help="Use random tokens instead of real data (for dry-run)")
    p.add_argument("--dataset", type=str, default="wikitext-103",
                    choices=["wikitext-103", "c4"])
    p.add_argument("--gradient_accumulation_steps", type=int, default=1)
    p.add_argument("--bottleneck_dim", type=int, default=128,
                    help="Predictor bottleneck dimension (d_b)")
    p.add_argument("--lambda_max", type=float, default=5000.0,
                    help="Max value for adaptive Lagrangian multiplier")
    p.add_argument("--kl_temperature", type=float, default=1.0)
    p.add_argument("--save_every", type=int, default=2000,
                    help="Save checkpoint every N steps (0=disabled)")
    p.add_argument("--gradient_checkpointing", action="store_true")
    p.add_argument("--resume", action="store_true",
                    help="Resume from latest intermediate checkpoint in output_dir")
    return p.parse_args()


def _best_attn_impl():
    if importlib.util.find_spec("flash_attn"):
        return "flash_attention_2"
    return "sdpa"


def cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps):
    def lr_lambda(step):
        if step < warmup_steps:
            return step / max(1, warmup_steps)
        progress = (step - warmup_steps) / max(1, total_steps - warmup_steps)
        return 0.5 * (1.0 + math.cos(math.pi * progress))
    return torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)


def patch_perlayer_masking(wrapper):
    """Re-patch MLPs so only wrapper._active_layer applies mask; others stay dense.

    When _active_layer is None (eval mode), all layers apply masks simultaneously.
    """
    wrapper._active_layer = None

    for layer_idx, layer in enumerate(wrapper.model.model.layers):
        mlp = layer.mlp
        gate_proj = mlp.gate_proj
        up_proj = mlp.up_proj
        down_proj = mlp.down_proj
        act_fn = mlp.act_fn
        predictor = wrapper.predictors[layer_idx]

        def _make_patched(li, pred, gp, up, dp, afn):
            def patched_forward(x):
                gate = afn(gp(x))
                up_out = up(x)
                intermediate = gate * up_out

                should_mask = (
                    wrapper.sparse_mode and
                    (wrapper._active_layer is None or li == wrapper._active_layer)
                )
                if should_mask:
                    logits = pred(x)
                    mask = wrapper.gumbel_mask(logits)
                    wrapper._layer_masks[li] = mask
                    return dp(intermediate * mask)
                return dp(intermediate)
            return patched_forward

        mlp.forward = _make_patched(
            layer_idx, predictor, gate_proj, up_proj, down_proj, act_fn
        )


def train(wrapper, dataloader, args, device):
    """Per-layer KL training with per-layer Lagrangian sparsity constraint.

    Each step: sample random layer l, mask only that layer, compute KL on full model output,
    update only layer l's predictor. Lagrangian lambdas are independent per layer.
    """
    num_layers = wrapper.model.config.num_hidden_layers
    kl_fn = KLDistillLoss(temperature=args.kl_temperature)

    params = list(wrapper.predictors.parameters())
    optimizer = torch.optim.AdamW(params, lr=args.lr, weight_decay=0.01)
    scheduler = cosine_schedule_with_warmup(optimizer, args.warmup_steps, args.num_steps)

    wrapper.predictors.train()

    if args.gradient_checkpointing:
        wrapper.model.train()
        wrapper.model.gradient_checkpointing_enable(
            gradient_checkpointing_kwargs={"use_reentrant": False}
        )
        print("Gradient checkpointing enabled")

    # Per-layer Lagrangian multipliers
    lambdas = [1.0] * num_layers
    target_sparsity = args.sparsity_target
    margin = 0.02

    # Track per-layer stats
    layer_kl_sum = [0.0] * num_layers
    layer_sparsity_sum = [0.0] * num_layers
    layer_count = [0] * num_layers

    start_step = 0

    # Resume from checkpoint if requested
    if args.resume:
        import glob
        pattern = os.path.join(args.output_dir, "predictor_perlayer_kl_step_*.pt")
        ckpts = sorted(glob.glob(pattern), key=lambda p: int(p.split("_step_")[1].split(".pt")[0]))
        if ckpts:
            latest = ckpts[-1]
            ckpt = torch.load(latest, map_location=device)
            wrapper.predictors.load_state_dict(ckpt["predictors"])
            optimizer.load_state_dict(ckpt["optimizer"])
            scheduler.load_state_dict(ckpt["scheduler"])
            lambdas = ckpt["lambdas"]
            start_step = ckpt["step"]
            layer_kl_sum = ckpt.get("layer_kl_sum", [0.0] * num_layers)
            layer_sparsity_sum = ckpt.get("layer_sparsity_sum", [0.0] * num_layers)
            layer_count = ckpt.get("layer_count", [0] * num_layers)
            if "rng_state" in ckpt:
                random.setstate(ckpt["rng_state"])
                torch.set_rng_state(ckpt["torch_rng_state"])
                torch.cuda.set_rng_state(ckpt["cuda_rng_state"])
            print(f"Resumed from {latest} at step {start_step}")
        else:
            print("No checkpoint found for resume, starting from scratch")

    data_iter = iter(dataloader)
    ga = args.gradient_accumulation_steps
    t0 = time.time()

    print(f"Per-layer KL training: {args.num_steps} steps, {num_layers} layers, "
          f"target_sparsity={target_sparsity}, lambda_max={args.lambda_max}")

    for opt_step in range(start_step + 1, args.num_steps + 1):
        # Random layer selection
        l = random.randint(0, num_layers - 1)
        wrapper._active_layer = l

        # Global tau schedule
        tau = args.tau_start + (args.tau_end - args.tau_start) * (opt_step / args.num_steps)
        wrapper.gumbel_mask.tau = tau

        accum_loss = 0.0
        accum_kl = 0.0
        accum_constraint = 0.0
        last_sparsity = 0.0

        for _ in range(ga):
            try:
                batch = next(data_iter)
            except StopIteration:
                data_iter = iter(dataloader)
                batch = next(data_iter)

            input_ids = batch["input_ids"].to(device)

            # Dense forward (no masks anywhere)
            dense_logits = wrapper.forward_dense(input_ids).logits.detach()

            # Sparse forward (only layer l masked)
            sparse_logits = wrapper.forward_sparse(input_ids).logits

            kl_raw = kl_fn(dense_logits, sparse_logits)

            # Sparsity constraint for layer l
            mask = wrapper._layer_masks.get(l)
            if mask is not None:
                actual_sparsity = 1.0 - mask.mean()
                sparsity_error = (actual_sparsity - target_sparsity).abs()
                constraint_loss = lambdas[l] * torch.clamp(sparsity_error - margin, min=0.0) ** 2
                last_sparsity = actual_sparsity.item()
            else:
                constraint_loss = torch.tensor(0.0, device=device)

            loss = (kl_raw + constraint_loss) / ga
            loss.backward()

            accum_loss += loss.item()
            accum_kl += kl_raw.item() / ga
            accum_constraint += constraint_loss.item() / ga

        torch.nn.utils.clip_grad_norm_(params, 1.0)
        optimizer.step()
        scheduler.step()
        optimizer.zero_grad()

        # Per-layer Lagrangian update
        old_lambda = lambdas[l]
        if last_sparsity < target_sparsity - margin:
            lambdas[l] *= 2.0
        elif last_sparsity > target_sparsity + margin:
            lambdas[l] *= 0.5
        lambdas[l] = max(0.01, min(lambdas[l], args.lambda_max))

        # Track per-layer stats
        layer_kl_sum[l] += accum_kl
        layer_sparsity_sum[l] += last_sparsity
        layer_count[l] += 1

        log_dict = {
            "loss": accum_loss, "kl": accum_kl,
            "constraint_loss": accum_constraint, "sparsity": last_sparsity,
            "tau": tau, "lr": scheduler.get_last_lr()[0],
            "lambda": lambdas[l], "active_layer": l,
        }
        wandb.log(log_dict, step=opt_step)

        if opt_step % args.log_every == 0 or opt_step == 1:
            dt = time.time() - t0
            avg_kl = sum(layer_kl_sum) / max(1, sum(layer_count))
            print(
                f"[Step {opt_step}/{args.num_steps}] layer={l} kl={accum_kl:.4f} "
                f"sparsity={last_sparsity:.3f} lambda={lambdas[l]:.2f} "
                f"tau={tau:.3f} lr={scheduler.get_last_lr()[0]:.2e} "
                f"avg_kl={avg_kl:.4f} dt={dt:.1f}s"
            )
            if old_lambda != lambdas[l]:
                print(f"  [Lambda L{l}] {old_lambda:.2f} -> {lambdas[l]:.2f}")

        if args.save_every > 0 and (opt_step % args.save_every == 0 or opt_step == args.num_steps):
            ckpt_path = os.path.join(args.output_dir, f"predictor_perlayer_kl_step_{opt_step}.pt")
            os.makedirs(args.output_dir, exist_ok=True)
            torch.save({
                "predictors": wrapper.predictors.state_dict(),
                "optimizer": optimizer.state_dict(),
                "scheduler": scheduler.state_dict(),
                "lambdas": lambdas,
                "step": opt_step,
                "layer_kl_sum": layer_kl_sum,
                "layer_sparsity_sum": layer_sparsity_sum,
                "layer_count": layer_count,
                "rng_state": random.getstate(),
                "torch_rng_state": torch.get_rng_state(),
                "cuda_rng_state": torch.cuda.get_rng_state(),
                "args": vars(args),
            }, ckpt_path)
            print(f"Saved checkpoint -> {ckpt_path}")

    # Print per-layer summary
    print("\n--- Per-Layer Training Summary ---")
    for i in range(num_layers):
        if layer_count[i] > 0:
            avg_kl_i = layer_kl_sum[i] / layer_count[i]
            avg_sp_i = layer_sparsity_sum[i] / layer_count[i]
            print(f"  Layer {i:2d}: count={layer_count[i]:4d} avg_kl={avg_kl_i:.4f} "
                  f"avg_sparsity={avg_sp_i:.3f} final_lambda={lambdas[i]:.2f}")


def main():
    args = parse_args()
    torch.manual_seed(args.seed)
    random.seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}")
    os.makedirs(args.output_dir, exist_ok=True)

    run_name = args.wandb_run_name or f"perlayer_kl_s{args.sparsity_target}_seed{args.seed}"
    wandb.init(project=args.wandb_project, name=run_name, config=vars(args))

    print(f"Loading model from {args.model_name_or_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name_or_path,
        torch_dtype=torch.bfloat16,
        device_map={"": device},
        attn_implementation=_best_attn_impl(),
    )
    model.eval()

    print("Initializing predictor wrapper ...")
    wrapper = PredictorWrapper(model, bottleneck_size=args.bottleneck_dim)
    wrapper.predictors.to(device=device, dtype=torch.bfloat16)

    # Re-patch MLPs for per-layer masking
    patch_perlayer_masking(wrapper)
    print("Per-layer masking patched (only active_layer gets mask per step)")

    print("Setting up data loader ...")
    if args.use_random_data:
        vocab_size = tokenizer.vocab_size
        dataloader = get_random_loader(vocab_size, args.batch_size, args.seq_len, args.seed)
        print(f"Using random data (vocab_size={vocab_size})")
    else:
        dataloader = get_calibration_loader(
            tokenizer, args.batch_size, args.seq_len, args.seed, args.dataset
        )

    pred_params = sum(p.numel() for p in wrapper.predictors.parameters())
    print(f"Predictor params: {pred_params:,} ({pred_params * 2 / 1024**2:.1f} MB bf16)")

    train(wrapper, dataloader, args, device)

    # Save final checkpoint
    ckpt_path = os.path.join(args.output_dir, "predictor_perlayer_kl.pt")
    torch.save({"predictors": wrapper.predictors.state_dict(), "args": vars(args)}, ckpt_path)
    print(f"Saved final checkpoint -> {ckpt_path}")

    # Set active_layer=None for all-layer eval summary
    wrapper._active_layer = None
    wrapper.predictors.eval()
    print("\nEval mode: all layers masked simultaneously (inference config)")

    wandb.finish()


if __name__ == "__main__":
    main()
