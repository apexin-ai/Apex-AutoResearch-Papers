import argparse
import os
import sys
import json
import time
import random

import torch
import torch.nn.functional as F
import numpy as np
from torch.optim import AdamW
from torch.utils.data import DataLoader, Dataset
from transformers import AutoTokenizer, get_cosine_schedule_with_warmup
from peft import LoraConfig, get_peft_model
from datasets import load_from_disk

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from threadgate import ThreadGatedModel
from gar import GARMeasurer, compute_gar_loss
from turn_utils import detect_turn_boundaries, build_turn_features
from config import (
    MODEL_NAME, LORA_RANK, GAR_EPSILON, GAR_LAMBDA, LEARNING_RATE,
    BATCH_SIZE, GRADIENT_ACCUMULATION, MAX_SEQ_LEN, NUM_EPOCHS, SEED,
    INIT_BIAS, GAR_LOSS_MODE, GAR_TARGET, LAMBDA_GATE_DIV, MIN_GATE_STD,
)


def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


class MultiTurnDataset(Dataset):
    def __init__(self, data_path, tokenizer, max_seq_len=2048):
        self.ds = load_from_disk(data_path)
        self.tokenizer = tokenizer
        self.max_seq_len = max_seq_len

    def __len__(self):
        return len(self.ds)

    def __getitem__(self, idx):
        messages = self.ds[idx]["messages"]
        text = self.tokenizer.apply_chat_template(messages, tokenize=False)
        encoding = self.tokenizer(
            text, truncation=True, max_length=self.max_seq_len, return_tensors="pt"
        )
        input_ids = encoding.input_ids.squeeze(0)

        boundaries = detect_turn_boundaries(input_ids, self.tokenizer)
        turn_feats = build_turn_features(input_ids, self.tokenizer)

        labels = input_ids.clone()
        labels[:] = -100
        for turn in boundaries["turns"]:
            if turn["role"] == "assistant":
                labels[turn["content_start"]:turn["content_end"]] = input_ids[turn["content_start"]:turn["content_end"]]

        return {
            "input_ids": input_ids,
            "labels": labels,
            "turn_features": turn_feats,
            "goal_positions": boundaries["goal_token_positions"],
            "assistant_last_positions": boundaries["assistant_last_token_positions"],
        }


def collate_fn(batch):
    item = batch[0]
    return {
        "input_ids": item["input_ids"].unsqueeze(0),
        "labels": item["labels"].unsqueeze(0),
        "turn_features": item["turn_features"],
        "goal_positions": item["goal_positions"],
        "assistant_last_positions": item["assistant_last_positions"],
    }


def log_gate_stats(model, global_step, detailed=False):
    gate_values = model.get_gate_values()
    if not gate_values:
        return
    per_layer_gates = []
    for layer_idx in sorted(gate_values.keys()):
        g = gate_values[layer_idx].mean().item()
        per_layer_gates.append(g)
    gate_mean = sum(per_layer_gates) / len(per_layer_gates)
    gate_std = (sum((g - gate_mean)**2 for g in per_layer_gates) / len(per_layer_gates)) ** 0.5
    gate_min = min(per_layer_gates)
    gate_max = max(per_layer_gates)
    print(f"[GATE] step={global_step} mean={gate_mean:.4f} std={gate_std:.4f} min={gate_min:.4f} max={gate_max:.4f}")
    if detailed:
        layer_str = " ".join([f"L{i}:{g:.3f}" for i, g in enumerate(per_layer_gates)])
        print(f"[GATE-PROFILE] step={global_step} {layer_str}")


def pcgrad_project(g_ntp_flat, g_gar_flat):
    """PCGrad projection (Yu et al., NeurIPS 2020).

    If g_ntp and g_gar conflict (negative cosine similarity), project g_ntp
    onto the plane orthogonal to g_gar. Returns (combined gradient, cos_sim).
    """
    dot = torch.dot(g_ntp_flat, g_gar_flat)
    g_gar_norm_sq = torch.dot(g_gar_flat, g_gar_flat)
    cos_sim = dot / (g_ntp_flat.norm() * g_gar_flat.norm() + 1e-8)

    if cos_sim.item() < 0:
        # Project g_ntp onto plane orthogonal to g_gar
        g_ntp_proj = g_ntp_flat - (dot / (g_gar_norm_sq + 1e-8)) * g_gar_flat
        combined = g_ntp_proj + g_gar_flat
    else:
        combined = g_ntp_flat + g_gar_flat
    return combined, cos_sim.item()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default=MODEL_NAME)
    parser.add_argument("--gate-type", type=str, default="threadgate", choices=["threadgate", "uniform", "none"])
    parser.add_argument("--seed", type=int, default=SEED)
    parser.add_argument("--output-dir", type=str, required=True)
    parser.add_argument("--data-dir", type=str, default="data/ultrachat_8k")
    parser.add_argument("--lambda-gar", type=float, default=GAR_LAMBDA)
    parser.add_argument("--max-seq-len", type=int, default=MAX_SEQ_LEN)
    parser.add_argument("--epochs", type=int, default=NUM_EPOCHS)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--max-steps", type=int, default=None)
    parser.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    parser.add_argument("--lr", type=float, default=LEARNING_RATE)
    parser.add_argument("--grad-accum", type=int, default=GRADIENT_ACCUMULATION)
    parser.add_argument("--gar-loss-mode", type=str, default=GAR_LOSS_MODE, choices=["pairwise", "cumulative", "maximize", "hinge_target", "smooth_saturation", "mse_target"])
    parser.add_argument("--lambda-gate-div", type=float, default=LAMBDA_GATE_DIV)
    parser.add_argument("--min-gate-std", type=float, default=MIN_GATE_STD)
    parser.add_argument("--gar-epsilon", type=float, default=GAR_EPSILON)
    parser.add_argument("--init-bias", type=float, default=INIT_BIAS)
    parser.add_argument("--gar-target", type=float, default=GAR_TARGET)
    parser.add_argument("--gate-lr-multiplier", type=float, default=1.0)
    args = parser.parse_args()

    set_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")

    print(f"Gate type: {args.gate_type}")
    print(f"Method: PCGrad (Yu et al., NeurIPS 2020)")
    print(f"Loading model: {args.model}")

    model = ThreadGatedModel(
        args.model,
        gate_type=args.gate_type,
        init_bias=args.init_bias,
        device_map="auto",
    )

    lora_config = LoraConfig(
        r=LORA_RANK,
        lora_alpha=32,
        target_modules=["q_proj", "v_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    model.base_model = get_peft_model(model.base_model, lora_config)
    model.base_model.print_trainable_parameters()

    model.base_model.gradient_checkpointing_enable()

    original_model = model.base_model.base_model.model
    original_model.config._attn_implementation = "eager"
    original_model.config.attn_implementation = "eager"
    for layer in original_model.model.layers:
        layer.self_attn._attn_implementation = "eager"

    measurer = GARMeasurer(original_model, measure_only=False)

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    print(f"Loading data from {args.data_dir}")
    dataset = MultiTurnDataset(args.data_dir, tokenizer, max_seq_len=args.max_seq_len)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=True, collate_fn=collate_fn, num_workers=0)
    print(f"Dataset size: {len(dataset)}")

    gate_params = []
    gate_param_names = []
    lora_params = []
    for name, param in model.named_parameters():
        if param.requires_grad:
            if 'gates.' in name or 'turn_embedding.' in name:
                gate_params.append(param)
                gate_param_names.append(name)
            else:
                lora_params.append(param)

    print(f"LoRA params: {len(lora_params)}, Gate params: {len(gate_params)}")
    print(f"Gate LR multiplier: {args.gate_lr_multiplier} (gate lr = {args.lr * args.gate_lr_multiplier})")

    if gate_params:
        param_groups = [
            {"params": lora_params, "lr": args.lr},
            {"params": gate_params, "lr": args.lr * args.gate_lr_multiplier},
        ]
    else:
        param_groups = [{"params": lora_params, "lr": args.lr}]

    optimizer = AdamW(param_groups, weight_decay=0.01)

    total_steps = len(dataloader) * args.epochs // args.grad_accum
    if args.dry_run:
        total_steps = 5
    if args.max_steps is not None:
        total_steps = args.max_steps
    scheduler = get_cosine_schedule_with_warmup(
        optimizer,
        num_warmup_steps=max(1, total_steps // 10),
        num_training_steps=total_steps,
    )

    print(f"Total training steps: {total_steps}")
    print(f"Gradient accumulation: {args.grad_accum}")
    print(f"Lambda GAR: {args.lambda_gar}")
    print(f"Lambda Gate Div: {args.lambda_gate_div}")
    print(f"Min Gate Std: {args.min_gate_std}")
    print("=" * 60)

    total_params, trainable_params, ratio = model.count_parameters()
    print(f"Total params: {total_params:,}")
    print(f"Trainable params: {trainable_params:,} ({ratio*100:.2f}%)")
    print("=" * 60)

    model.train()
    start_time = time.time()
    global_step = 0
    gate_grad_observed = False
    optimizer.zero_grad()

    # PCGrad diagnostic accumulators (reset every 50 global steps)
    pcgrad_cos_sims = []        # per-layer cosine similarities per step
    pcgrad_mag_ratios_pre = []  # ||g_ntp|| / ||g_gar|| before projection
    pcgrad_mag_ratios_post = [] # ||g_ntp_proj|| / ||g_gar|| after projection
    pcgrad_conflict_fracs = []  # fraction of layers with cos < 0 per step
    pcgrad_conflict_steps = 0   # number of steps with at least one conflict

    for epoch in range(args.epochs):
        epoch_loss = 0.0
        epoch_ntp = 0.0
        epoch_gar = 0.0
        epoch_div = 0.0
        num_batches = 0

        for step, batch in enumerate(dataloader):
            if args.dry_run and global_step >= 5:
                break
            if args.max_steps is not None and global_step >= args.max_steps:
                break

            input_ids = batch["input_ids"].to(device)
            labels = batch["labels"].to(device)
            turn_features = {
                k: v.to(device) if isinstance(v, torch.Tensor) else v
                for k, v in batch["turn_features"].items()
            }

            with measurer.measure():
                outputs = model(
                    input_ids,
                    labels=labels,
                    turn_features=turn_features,
                    output_attentions=True,
                )

            l_ntp = outputs.loss

            goal_pos = batch["goal_positions"]
            assistant_pos = batch["assistant_last_positions"]

            if len(assistant_pos) >= 2 and len(goal_pos) > 0:
                gar_per_turn = []
                for pos in assistant_pos:
                    gar_val = measurer.compute_gar_differentiable(goal_pos, [pos])
                    gar_per_turn.append(gar_val)
                l_gar = compute_gar_loss(gar_per_turn, epsilon=args.gar_epsilon, mode=args.gar_loss_mode, target=args.gar_target)
            else:
                l_gar = torch.tensor(0.0, device=device, requires_grad=True)

            gate_values_grad = model.get_gate_values(with_grad=True)
            if gate_values_grad and args.lambda_gate_div > 0 and args.gate_type != "none":
                per_layer_means = []
                for layer_idx in sorted(gate_values_grad.keys()):
                    per_layer_means.append(gate_values_grad[layer_idx].mean())
                gate_means_tensor = torch.stack(per_layer_means)
                current_gate_std = gate_means_tensor.std()
                l_gate_div = F.relu(torch.tensor(args.min_gate_std, device=device) - current_gate_std)
            else:
                l_gate_div = torch.tensor(0.0, device=device)

            # --- PCGrad: separate backward passes for gate params ---
            if gate_params and args.gate_type != "none":
                # Combined loss for LoRA params (standard backward)
                loss_combined = l_ntp + args.lambda_gar * l_gar + args.lambda_gate_div * l_gate_div
                loss_combined_scaled = loss_combined / args.grad_accum

                # Step 1: Backward for NTP loss, retain graph for second pass
                optimizer.zero_grad()
                l_ntp_scaled = l_ntp / args.grad_accum
                l_ntp_scaled.backward(retain_graph=True)

                # Collect NTP gradients on gate params
                g_ntp_list = []
                for p in gate_params:
                    if p.grad is not None:
                        g_ntp_list.append(p.grad.detach().clone())
                    else:
                        g_ntp_list.append(torch.zeros_like(p))

                # Step 2: Zero gate grads, backward for GAR + gate_div loss
                for p in gate_params:
                    if p.grad is not None:
                        p.grad.zero_()

                l_gar_div_scaled = (args.lambda_gar * l_gar + args.lambda_gate_div * l_gate_div) / args.grad_accum
                l_gar_div_scaled.backward(retain_graph=True)

                # Collect GAR+div gradients on gate params
                g_gar_list = []
                for p in gate_params:
                    if p.grad is not None:
                        g_gar_list.append(p.grad.detach().clone())
                    else:
                        g_gar_list.append(torch.zeros_like(p))

                # Step 3: Zero all grads, do full combined backward for LoRA params
                optimizer.zero_grad()
                loss_combined_scaled.backward()

                # Step 4: PCGrad projection on gate params only
                step_cos_sims = []
                step_has_conflict = False
                step_mag_pre = []
                step_mag_post = []

                for i, p in enumerate(gate_params):
                    g_ntp_flat = g_ntp_list[i].flatten()
                    g_gar_flat = g_gar_list[i].flatten()

                    ntp_norm = g_ntp_flat.norm().item()
                    gar_norm = g_gar_flat.norm().item()

                    if ntp_norm < 1e-12 or gar_norm < 1e-12:
                        # Skip projection if either gradient is near-zero
                        step_cos_sims.append(0.0)
                        step_mag_pre.append(0.0)
                        step_mag_post.append(0.0)
                        continue

                    combined, cos = pcgrad_project(g_ntp_flat, g_gar_flat)
                    step_cos_sims.append(cos)
                    step_mag_pre.append(ntp_norm / (gar_norm + 1e-8))

                    if cos < 0:
                        step_has_conflict = True
                        # Compute post-projection magnitude ratio
                        g_ntp_proj = combined - g_gar_flat
                        step_mag_post.append(g_ntp_proj.norm().item() / (gar_norm + 1e-8))
                    else:
                        step_mag_post.append(ntp_norm / (gar_norm + 1e-8))

                    # Overwrite gate param gradient with PCGrad combined gradient
                    p.grad.copy_(combined.reshape(p.grad.shape))

                # Accumulate diagnostics
                if step_cos_sims:
                    pcgrad_cos_sims.append(np.mean(step_cos_sims))
                    n_conflict = sum(1 for c in step_cos_sims if c < 0)
                    pcgrad_conflict_fracs.append(n_conflict / len(step_cos_sims))
                    if step_has_conflict:
                        pcgrad_conflict_steps += 1
                    if step_mag_pre:
                        pcgrad_mag_ratios_pre.append(np.mean(step_mag_pre))
                    if step_mag_post:
                        pcgrad_mag_ratios_post.append(np.mean(step_mag_post))
            else:
                # No gate params or gate_type == "none": standard training
                loss = l_ntp + args.lambda_gar * l_gar + args.lambda_gate_div * l_gate_div
                loss = loss / args.grad_accum
                loss.backward()

            # Use combined loss for logging
            loss_val = (l_ntp + args.lambda_gar * l_gar + args.lambda_gate_div * l_gate_div).item()

            if (step + 1) % args.grad_accum == 0 or args.dry_run:
                torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
                if not gate_grad_observed and model.gates is not None:
                    gate_grad_observed = any(
                        p.grad is not None and p.grad.abs().sum() > 0
                        for p in model.gates.parameters()
                    )
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad()
                global_step += 1

                if global_step % 50 == 0:
                    log_gate_stats(model, global_step, detailed=(global_step % 100 == 0))

                    # PCGrad diagnostic logging
                    if pcgrad_cos_sims:
                        avg_cos = np.mean(pcgrad_cos_sims)
                        avg_conflict_frac = np.mean(pcgrad_conflict_fracs)
                        avg_mag_pre = np.mean(pcgrad_mag_ratios_pre) if pcgrad_mag_ratios_pre else 0.0
                        avg_mag_post = np.mean(pcgrad_mag_ratios_post) if pcgrad_mag_ratios_post else 0.0
                        print(
                            f"[PCGRAD] step={global_step} "
                            f"avg_cos={avg_cos:.4f} "
                            f"mag_ratio_pre={avg_mag_pre:.4f} "
                            f"mag_ratio_post={avg_mag_post:.4f} "
                            f"conflict_frac={avg_conflict_frac:.4f} "
                            f"conflict_steps={pcgrad_conflict_steps}/{len(pcgrad_cos_sims)}"
                        )
                    # Reset accumulators
                    pcgrad_cos_sims = []
                    pcgrad_mag_ratios_pre = []
                    pcgrad_mag_ratios_post = []
                    pcgrad_conflict_fracs = []
                    pcgrad_conflict_steps = 0

            epoch_loss += loss_val
            epoch_ntp += l_ntp.item()
            epoch_gar += l_gar.item()
            epoch_div += l_gate_div.item()
            num_batches += 1

            if step % 50 == 0 or args.dry_run:
                mem_used = torch.cuda.max_memory_allocated() / 1e9 if torch.cuda.is_available() else 0
                gate_vals = model.get_gate_values()
                mean_gate = np.mean([g.mean().item() for g in gate_vals.values()]) if gate_vals else 0
                print(
                    f"Epoch {epoch} Step {step} | "
                    f"L_NTP={l_ntp.item():.4f} L_GAR={l_gar.item():.4f} L_DIV={l_gate_div.item():.4f} "
                    f"Loss={loss_val:.4f} | "
                    f"Gate={mean_gate:.4f} | Mem={mem_used:.1f}GB"
                )
                if epoch == 0 and step == 0:
                    log_gate_stats(model, 0, detailed=True)

        if args.dry_run:
            break
        if args.max_steps is not None and global_step >= args.max_steps:
            break

        avg_loss = epoch_loss / max(num_batches, 1)
        avg_ntp = epoch_ntp / max(num_batches, 1)
        avg_gar = epoch_gar / max(num_batches, 1)
        avg_div = epoch_div / max(num_batches, 1)
        print(f"\nEpoch {epoch} done | Avg Loss={avg_loss:.4f} Avg NTP={avg_ntp:.4f} Avg GAR={avg_gar:.4f} Avg DIV={avg_div:.4f}")

        if not args.dry_run:
            ckpt_dir = os.path.join(args.output_dir, f"epoch_{epoch}")
            os.makedirs(ckpt_dir, exist_ok=True)
            model.base_model.save_pretrained(os.path.join(ckpt_dir, "lora"))
            if model.gates is not None:
                gate_state = {"gates": model.gates.state_dict()}
                if hasattr(model, "turn_embedding"):
                    gate_state["turn_embedding"] = model.turn_embedding.state_dict()
                torch.save(gate_state, os.path.join(ckpt_dir, "gate_params.pt"))
            print(f"Checkpoint saved to {ckpt_dir}")

    elapsed = time.time() - start_time
    print(f"\nTraining complete in {elapsed:.1f}s")

    log_gate_stats(model, global_step, detailed=True)

    os.makedirs(args.output_dir, exist_ok=True)
    model.base_model.save_pretrained(os.path.join(args.output_dir, "lora"))
    if model.gates is not None:
        gate_state = {"gates": model.gates.state_dict()}
        if hasattr(model, "turn_embedding"):
            gate_state["turn_embedding"] = model.turn_embedding.state_dict()
        torch.save(gate_state, os.path.join(args.output_dir, "gate_params.pt"))

    config_dict = {
        "method": "pcgrad",
        "gate_type": args.gate_type,
        "seed": args.seed,
        "epochs": args.epochs,
        "lr": args.lr,
        "lambda_gar": args.lambda_gar,
        "max_seq_len": args.max_seq_len,
        "grad_accum": args.grad_accum,
        "gate_lr_multiplier": args.gate_lr_multiplier,
        "init_bias": args.init_bias,
        "gar_loss_mode": args.gar_loss_mode,
        "gar_target": args.gar_target,
        "lambda_gate_div": args.lambda_gate_div,
        "min_gate_std": args.min_gate_std,
        "total_steps": global_step,
        "elapsed_seconds": elapsed,
    }
    with open(os.path.join(args.output_dir, "train_config.json"), "w") as f:
        json.dump(config_dict, f, indent=2)

    print(f"Final model saved to {args.output_dir}")
    print(f"Gate parameters received gradients during training: {gate_grad_observed}")


if __name__ == "__main__":
    main()
