# Two-phase BCE+Compensation training for SwiGLU sparsity predictors.
#
# Phase 1 (BCE warmup): train predictor only with BCESparsityLoss + SparsityRegularizer.
#   CompensationHead is frozen; no compensation loss.
# Phase 2 (joint): train predictor + CompensationHead.
#   Total loss = BCE + comp_loss_weight * CompensationMSE + reg_weight * SparsityReg.
#
# Input:  frozen Llama model + calibration data (wikitext-103 or c4)
# Output: predictor_bce_comp.pt containing predictor + comp_head weights
#
# Usage:
#   python train_bce_comp.py --num_steps 1000 --gpu 0
#   python train_bce_comp.py --comp_warmup_steps 300 --predictor_lr 5e-4 --comp_lr 1e-3 --gpu 0

import argparse
import importlib.util
import math
import os
import sys

import torch
import wandb
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_utils import get_calibration_loader, get_random_loader
from losses import BCESparsityLoss, CompensationLoss, SparsityRegularizer
from predictor import CompensationNetwork, PredictorWrapper


def parse_args():
    p = argparse.ArgumentParser(
        description="Two-phase BCE+Compensation training for SwiGLU sparsity predictors"
    )
    p.add_argument("--model_name_or_path", type=str,
                    default="/root/autodl-tmp/models/llama-3.1-8b")
    p.add_argument("--num_steps", type=int, default=1000)
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--seq_len", type=int, default=2048)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--output_dir", type=str,
                    default="/root/distill_sparse_swiglu/checkpoints")
    p.add_argument("--dataset", type=str, default="wikitext-103",
                    choices=["wikitext-103", "c4"])
    p.add_argument("--use_random_data", action="store_true",
                    help="Use random tokens instead of real data (for dry-run)")
    p.add_argument("--gradient_accumulation_steps", type=int, default=1)
    p.add_argument("--log_every", type=int, default=10)
    # LR schedule
    p.add_argument("--predictor_lr", type=float, default=1e-3)
    p.add_argument("--comp_lr", type=float, default=1e-3)
    p.add_argument("--warmup_steps", type=int, default=100,
                    help="LR cosine warmup steps")
    # Sparsity
    p.add_argument("--sparsity_target", type=float, default=0.5)
    p.add_argument("--sparsity_reg_weight", type=float, default=0.1)
    p.add_argument("--tau_start", type=float, default=1.0)
    p.add_argument("--tau_end", type=float, default=0.1)
    # Compensation
    p.add_argument("--comp_warmup_steps", type=int, default=200,
                    help="BCE-only warmup steps before enabling CompensationHead")
    p.add_argument("--comp_loss_weight", type=float, default=1.0,
                    help="Weight for compensation MSE loss in Phase 2")
    p.add_argument("--comp_bottleneck", type=int, default=256,
                    help="CompensationHead bottleneck dimension")
    # W&B
    p.add_argument("--wandb_project", type=str, default="distill_sparse_swiglu")
    p.add_argument("--wandb_run_name", type=str, default=None)
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


def train(wrapper, comp_net, dataloader, args, device):
    """Two-phase training loop.

    Phase 1 (step 1..comp_warmup_steps): BCE + SparsityReg, predictor only.
    Phase 2 (step comp_warmup_steps+1..num_steps): BCE + CompMSE + SparsityReg,
        predictor + CompensationHead jointly.
    """
    bce_fn = BCESparsityLoss(sparsity_target=args.sparsity_target)
    comp_loss_fn = CompensationLoss()
    reg_fn = SparsityRegularizer(args.sparsity_target, args.sparsity_reg_weight)

    # Freeze comp_net during Phase 1; optimizer holds both param groups but
    # AdamW skips params with grad=None (requires_grad=False).
    comp_net.requires_grad_(False)

    optimizer = torch.optim.AdamW([
        {"params": list(wrapper.predictors.parameters()), "lr": args.predictor_lr},
        {"params": list(comp_net.parameters()), "lr": args.comp_lr},
    ], weight_decay=0.01)
    scheduler = cosine_schedule_with_warmup(optimizer, args.warmup_steps, args.num_steps)

    wrapper.predictors.train()
    comp_net.train()

    data_iter = iter(dataloader)
    ga = args.gradient_accumulation_steps
    num_layers = len(wrapper.predictors)
    phase2_started = False

    for opt_step in range(1, args.num_steps + 1):
        if opt_step == args.comp_warmup_steps + 1 and not phase2_started:
            comp_net.requires_grad_(True)
            phase2_started = True
            print(f"[Phase 2] Step {opt_step}: CompensationHead training enabled")

        tau = args.tau_start + (args.tau_end - args.tau_start) * (opt_step / args.num_steps)
        wrapper.gumbel_mask.tau = tau

        in_warmup = opt_step <= args.comp_warmup_steps

        accum_loss = 0.0
        accum_bce = 0.0
        accum_comp = 0.0
        accum_reg = 0.0
        last_sparsity = 0.0

        for _ in range(ga):
            try:
                batch = next(data_iter)
            except StopIteration:
                data_iter = iter(dataloader)
                batch = next(data_iter)

            input_ids = batch["input_ids"].to(device)

            wrapper.forward_dense(input_ids, capture_intermediates=True)
            intermediates = wrapper.get_intermediates()
            layer_inputs = wrapper.get_layer_inputs()

            total_bce = torch.tensor(0.0, device=device)
            total_comp = torch.tensor(0.0, device=device)
            all_masks = {}
            active_layers = 0

            for layer_idx in range(num_layers):
                if layer_idx not in intermediates:
                    continue
                active_layers += 1

                dense_act = intermediates[layer_idx]
                inp = layer_inputs[layer_idx]

                pred_logits = wrapper.predictors[layer_idx](inp)
                total_bce = total_bce + bce_fn(pred_logits, dense_act)

                with torch.no_grad():
                    mask = (pred_logits > 0).to(dense_act.dtype)
                    all_masks[layer_idx] = mask

                if not in_warmup:
                    down_proj = wrapper.model.model.layers[layer_idx].mlp.down_proj
                    with torch.no_grad():
                        dense_out = down_proj(dense_act)
                        sparse_out = down_proj(dense_act * mask)
                    comp = comp_net.forward_layer(layer_idx, inp)
                    total_comp = total_comp + comp_loss_fn(comp, sparse_out, dense_out)

            total_bce = total_bce / max(active_layers, 1)
            reg = reg_fn(all_masks)

            if in_warmup:
                loss = (total_bce + reg) / ga
            else:
                total_comp = total_comp / max(active_layers, 1)
                loss = (total_bce + args.comp_loss_weight * total_comp + reg) / ga
                accum_comp += total_comp.item() / ga

            loss.backward()
            accum_loss += loss.item()
            accum_bce += total_bce.item() / ga
            accum_reg += reg.item() / ga

            last_sparsity = (
                1.0 - torch.stack([m.mean() for m in all_masks.values()]).mean().item()
                if all_masks else 0.0
            )

        torch.nn.utils.clip_grad_norm_(
            list(wrapper.predictors.parameters()) + list(comp_net.parameters()), 1.0
        )
        optimizer.step()
        scheduler.step()
        optimizer.zero_grad()

        phase_str = "warmup" if in_warmup else "joint"
        log_dict = {
            "loss": accum_loss, "bce_loss": accum_bce, "comp_loss": accum_comp,
            "reg_loss": accum_reg, "sparsity": last_sparsity,
            "lr_pred": optimizer.param_groups[0]["lr"],
            "lr_comp": optimizer.param_groups[1]["lr"],
            "phase": 1 if in_warmup else 2,
        }
        wandb.log(log_dict, step=opt_step)

        if opt_step % args.log_every == 0 or opt_step == 1:
            print(
                f"[Step {opt_step}/{args.num_steps}] phase={phase_str} "
                f"loss={accum_loss:.4f} bce={accum_bce:.4f} comp={accum_comp:.4f} "
                f"reg={accum_reg:.4f} sparsity={last_sparsity:.3f} "
                f"lr_pred={optimizer.param_groups[0]['lr']:.2e} "
                f"lr_comp={optimizer.param_groups[1]['lr']:.2e}"
            )


def main():
    args = parse_args()
    torch.manual_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}")
    os.makedirs(args.output_dir, exist_ok=True)

    run_name = (args.wandb_run_name
                or f"bce_comp_s{args.sparsity_target}_plr{args.predictor_lr}_clr{args.comp_lr}")
    wandb.init(project=args.wandb_project, name=run_name, config=vars(args))

    print(f"Loading model from {args.model_name_or_path} ...")
    tokenizer = AutoTokenizer.from_pretrained(args.model_name_or_path)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(
        args.model_name_or_path,
        dtype=torch.bfloat16,
        device_map={"": device},
        attn_implementation=_best_attn_impl(),
    )
    model.eval()

    print("Initializing predictor wrapper ...")
    wrapper = PredictorWrapper(model, bottleneck_size=128)
    wrapper.predictors.to(device=device, dtype=torch.bfloat16)

    num_layers = model.config.num_hidden_layers
    hidden_size = model.config.hidden_size
    comp_net = CompensationNetwork(num_layers, hidden_size, args.comp_bottleneck)
    comp_net.to(device=device, dtype=torch.bfloat16)

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
    comp_params = sum(p.numel() for p in comp_net.parameters())
    total_params = sum(p.numel() for p in model.parameters())
    print(f"Predictor params: {pred_params:,} ({pred_params * 2 / 1024**2:.1f} MB bf16)")
    print(f"Compensation params: {comp_params:,} ({comp_params * 2 / 1024**2:.1f} MB bf16)")
    print(f"Model params: {total_params:,}")
    print(f"Phase 1: BCE warmup for {args.comp_warmup_steps} steps")
    print(f"Phase 2: BCE+Comp joint for {args.num_steps - args.comp_warmup_steps} steps")

    train(wrapper, comp_net, dataloader, args, device)

    ckpt_path = os.path.join(args.output_dir, "predictor_bce_comp.pt")
    torch.save({
        "predictors": wrapper.predictors.state_dict(),
        "comp_network": comp_net.state_dict(),
        "args": vars(args),
    }, ckpt_path)
    print(f"Saved checkpoint -> {ckpt_path}")

    wandb.finish()


if __name__ == "__main__":
    main()
