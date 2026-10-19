# C1 causal ablation: Train BCE predictor with KL-derived oracle masks as targets.
# Isolates whether KL distillation advantage comes from gradient coupling or target quality.
# If result ~ KL PPL (11.79): target quality is the main factor.
# If result ~ BCE PPL (22.51): gradient coupling is the main factor.
#
# Architecture: same predictor (GELU, d_b=128) trained with BCE loss against binary masks
# produced by a frozen KL predictor, plus Lagrangian sparsity constraint (same as KL training).
#
# Usage:
#   python train_bce_kl_targets.py --kl_checkpoint checkpoints/mvp_kl_norm_v2_s42/predictor_kl_normalized.pt \
#       --output_dir checkpoints/c1_ablation_bce_kl_targets_s42 --gpu 0

import argparse
import importlib.util
import math
import os
import sys
import time

import torch
import torch.nn.functional as F
import wandb
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_utils import get_calibration_loader, get_eval_dataset
from predictor import PredictorWrapper, SparsityPredictor


def _best_attn_impl():
    if importlib.util.find_spec("flash_attn"):
        return "flash_attention_2"
    return "sdpa"


def cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps):
    def lr_lambda(step):
        if step < warmup_steps:
            return step / max(warmup_steps, 1)
        progress = (step - warmup_steps) / max(total_steps - warmup_steps, 1)
        return 0.5 * (1.0 + math.cos(math.pi * progress))
    return torch.optim.lr_scheduler.LambdaLR(optimizer, lr_lambda)


def parse_args():
    p = argparse.ArgumentParser(description="C1 ablation: BCE with KL-derived oracle targets")
    p.add_argument("--model_name_or_path", type=str,
                   default="/root/autodl-tmp/models/llama-3.1-8b")
    p.add_argument("--kl_checkpoint", type=str, required=True,
                   help="Path to trained KL predictor checkpoint (oracle source)")
    p.add_argument("--num_steps", type=int, default=1000)
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--seq_len", type=int, default=2048)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--sparsity_target", type=float, default=0.5)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--output_dir", type=str, required=True)
    p.add_argument("--wandb_project", type=str, default="distill_sparse_swiglu")
    p.add_argument("--wandb_run_name", type=str, default=None)
    p.add_argument("--warmup_steps", type=int, default=100)
    p.add_argument("--log_every", type=int, default=100)
    p.add_argument("--lambda_max", type=float, default=1000.0)
    p.add_argument("--bottleneck_dim", type=int, default=128)
    p.add_argument("--gradient_accumulation_steps", type=int, default=1)
    p.add_argument("--skip_eval", action="store_true")
    p.add_argument("--max_eval_samples", type=int, default=200)
    return p.parse_args()


def train_bce_kl_targets(wrapper, kl_predictors, dataloader, args, device):
    """BCE training with frozen KL predictor targets + Lagrangian sparsity constraint."""
    params = list(wrapper.predictors.parameters())
    optimizer = torch.optim.AdamW(params, lr=args.lr, weight_decay=0.01)
    scheduler = cosine_schedule_with_warmup(optimizer, args.warmup_steps, args.num_steps)

    wrapper.predictors.train()
    data_iter = iter(dataloader)
    ga = args.gradient_accumulation_steps
    num_layers = len(wrapper.predictors)

    lambda_sparse = 1.0
    target_sparsity = args.sparsity_target
    margin = 0.02

    print(f"BCE+KL-targets Lagrangian: lambda={lambda_sparse}, target={target_sparsity}, "
          f"margin={margin}, cap={args.lambda_max}")

    t0 = time.time()

    for opt_step in range(1, args.num_steps + 1):
        accum_loss = 0.0
        accum_bce = 0.0
        accum_constraint = 0.0
        accum_agreement = 0.0
        last_sparsity = 0.0

        for _ in range(ga):
            try:
                batch = next(data_iter)
            except StopIteration:
                data_iter = iter(dataloader)
                batch = next(data_iter)

            input_ids = batch["input_ids"].to(device)

            wrapper.forward_dense(input_ids, capture_intermediates=True)
            layer_inputs = wrapper.get_layer_inputs()

            total_bce = torch.tensor(0.0, device=device)
            all_masks = {}
            batch_agreement = 0.0
            active_layers = 0

            for layer_idx in range(num_layers):
                if layer_idx not in layer_inputs:
                    continue
                inp = layer_inputs[layer_idx]

                with torch.no_grad():
                    kl_logits = kl_predictors[layer_idx](inp)
                    oracle_target = (kl_logits > 0).float()

                new_logits = wrapper.predictors[layer_idx](inp)
                total_bce = total_bce + F.binary_cross_entropy_with_logits(
                    new_logits, oracle_target)

                # STE mask for sparsity tracking
                soft_mask = torch.sigmoid(new_logits)
                hard_mask = (new_logits > 0).float()
                all_masks[layer_idx] = hard_mask - soft_mask.detach() + soft_mask

                batch_agreement += (hard_mask == oracle_target).float().mean().item()
                active_layers += 1

            total_bce = total_bce / max(active_layers, 1)

            if all_masks:
                actual_sparsity = 1.0 - torch.stack(
                    [m.mean() for m in all_masks.values()]).mean()
                sparsity_error = torch.abs(actual_sparsity - target_sparsity)
                constraint_loss = lambda_sparse * torch.clamp(
                    sparsity_error - margin, min=0.0) ** 2
            else:
                constraint_loss = torch.tensor(0.0, device=device)

            loss = (total_bce + constraint_loss) / ga
            loss.backward()

            accum_loss += loss.item()
            accum_bce += total_bce.item() / ga
            accum_constraint += constraint_loss.item() / ga
            if active_layers > 0:
                accum_agreement += (batch_agreement / active_layers) / ga

        torch.nn.utils.clip_grad_norm_(params, 1.0)
        optimizer.step()
        scheduler.step()
        optimizer.zero_grad()

        with torch.no_grad():
            if all_masks:
                avg_sparsity = 1.0 - torch.stack(
                    [m.mean() for m in all_masks.values()]).mean().item()
            else:
                avg_sparsity = 0.0
        last_sparsity = avg_sparsity

        old_lambda = lambda_sparse
        if avg_sparsity < target_sparsity - margin:
            lambda_sparse *= 2.0
        elif avg_sparsity > target_sparsity + margin:
            lambda_sparse *= 0.5
        lambda_sparse = max(0.01, min(lambda_sparse, args.lambda_max))

        log_dict = {
            "loss": accum_loss, "bce_loss": accum_bce,
            "constraint_loss": accum_constraint, "sparsity": last_sparsity,
            "oracle_agreement": accum_agreement,
            "lr": scheduler.get_last_lr()[0], "lambda_sparse": lambda_sparse,
        }
        wandb.log(log_dict, step=opt_step)

        if opt_step % args.log_every == 0 or opt_step <= 5:
            elapsed = time.time() - t0
            print(
                f"[Step {opt_step}/{args.num_steps}] loss={accum_loss:.4f} "
                f"bce={accum_bce:.4f} constraint={accum_constraint:.4f} "
                f"sparsity={last_sparsity:.3f} agreement={accum_agreement:.3f} "
                f"lambda={lambda_sparse:.2f} "
                f"lr={scheduler.get_last_lr()[0]:.2e} "
                f"elapsed={elapsed:.1f}s ({elapsed/opt_step:.2f}s/step)"
            )

    total_time = time.time() - t0
    print(f"\nBCE+KL-targets training complete: {args.num_steps} steps in "
          f"{total_time:.1f}s ({total_time/args.num_steps:.2f}s/step)")


@torch.no_grad()
def evaluate_ppl(wrapper, tokenizer, device, args):
    """Evaluate WikiText-2 perplexity with the trained predictor's hard masks."""
    print("\nLoading WikiText-2 for evaluation ...")
    examples = get_eval_dataset("wikitext2", tokenizer, args.seq_len,
                                max_samples=args.max_eval_samples)
    print(f"  {len(examples)} sequences")

    wrapper.predictors.eval()
    wrapper.gumbel_mask.hard = True
    wrapper.sparse_mode = True

    total_loss = 0.0
    total_tokens = 0
    for ex in examples:
        ids = ex["input_ids"].unsqueeze(0).to(device)
        labels = ex["labels"].unsqueeze(0).to(device)
        logits = wrapper.model(input_ids=ids).logits
        loss = F.cross_entropy(
            logits.view(-1, logits.size(-1)), labels.view(-1), reduction="sum")
        total_loss += loss.item()
        total_tokens += labels.numel()

    ppl = torch.exp(torch.tensor(total_loss / total_tokens)).item()

    # Sparsity stats from one sample
    wrapper._layer_masks.clear()
    sample_ids = examples[0]["input_ids"].unsqueeze(0).to(device)
    wrapper.forward(sample_ids)
    masks = wrapper.get_masks()
    if masks:
        avg_sparsity = 1.0 - torch.stack(
            [m.float().mean() for m in masks.values()]).mean().item()
    else:
        avg_sparsity = 0.0

    return ppl, avg_sparsity


def main():
    args = parse_args()
    device = torch.device(f"cuda:{args.gpu}")

    torch.manual_seed(args.seed)

    os.makedirs(args.output_dir, exist_ok=True)

    run_name = args.wandb_run_name or f"c1_bce_kl_targets_s{args.seed}"
    wandb.init(project=args.wandb_project, name=run_name,
               config=vars(args), tags=["c1_ablation"])

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

    wrapper = PredictorWrapper(model, bottleneck_size=args.bottleneck_dim)
    wrapper.predictors.to(device=device, dtype=torch.bfloat16)

    # Frozen KL predictor (oracle source)
    print(f"Loading KL oracle predictor from {args.kl_checkpoint} ...")
    kl_ckpt = torch.load(args.kl_checkpoint, map_location=device, weights_only=True)

    num_layers = model.config.num_hidden_layers
    hidden_size = model.config.hidden_size
    intermediate_size = model.config.intermediate_size

    kl_predictors = torch.nn.ModuleList([
        SparsityPredictor(hidden_size, intermediate_size, args.bottleneck_dim)
        for _ in range(num_layers)
    ])
    kl_predictors.load_state_dict(kl_ckpt["predictors"])
    kl_predictors.to(device=device, dtype=torch.bfloat16)
    kl_predictors.eval()
    for p in kl_predictors.parameters():
        p.requires_grad = False

    kl_params = sum(p.numel() for p in kl_predictors.parameters())
    print(f"KL oracle predictor loaded ({kl_params:,} params, frozen)")

    print(f"Loading calibration data (wikitext-103, seed={args.seed}) ...")
    dataloader = get_calibration_loader(
        tokenizer, args.batch_size, args.seq_len, args.seed)

    train_bce_kl_targets(wrapper, kl_predictors, dataloader, args, device)

    ckpt_path = os.path.join(args.output_dir, "predictor_bce_kl_targets.pt")
    torch.save({
        "predictors": wrapper.predictors.state_dict(),
        "args": vars(args),
    }, ckpt_path)
    print(f"Saved checkpoint -> {ckpt_path}")

    if not args.skip_eval:
        # Free KL predictor memory before eval
        del kl_predictors
        torch.cuda.empty_cache()

        ppl, sparsity = evaluate_ppl(wrapper, tokenizer, device, args)
        print(f"\n=== WikiText-2 Evaluation ===")
        print(f"  Perplexity: {ppl:.2f}")
        print(f"  Actual sparsity: {sparsity:.3f}")
        print(f"\n=== Reference ===")
        print(f"  KL predictor PPL: 11.79")
        print(f"  BCE predictor PPL: 22.51")
        wandb.log({"eval/wt2_ppl": ppl, "eval/sparsity": sparsity})

    wandb.finish()
    print("\nDone.")


if __name__ == "__main__":
    main()
