"""
Scheduled Sampling variant of train.py for mitigating exposure bias
in multi-turn ThreadGate training.

Occasionally replaces teacher-forced ground truth with model's own
autoregressive continuation, then computes GAR loss on generated text.
"""
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


class MultiTurnSSDataset(Dataset):
    """Multi-turn dataset that also returns first_assistant_start for SS."""

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
        first_assistant_start = -1
        for turn in boundaries["turns"]:
            if turn["role"] == "assistant":
                labels[turn["content_start"]:turn["content_end"]] = input_ids[turn["content_start"]:turn["content_end"]]
                if first_assistant_start == -1:
                    first_assistant_start = turn["content_start"]

        return {
            "input_ids": input_ids,
            "labels": labels,
            "turn_features": turn_feats,
            "goal_positions": boundaries["goal_token_positions"],
            "assistant_last_positions": boundaries["assistant_last_token_positions"],
            "first_assistant_start": first_assistant_start,
        }


def collate_fn(batch):
    item = batch[0]
    return {
        "input_ids": item["input_ids"].unsqueeze(0),
        "labels": item["labels"].unsqueeze(0),
        "turn_features": item["turn_features"],
        "goal_positions": item["goal_positions"],
        "assistant_last_positions": item["assistant_last_positions"],
        "first_assistant_start": item["first_assistant_start"],
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


def get_ss_ratio(global_step, ss_warmup_steps, ss_max_ratio):
    """Linear ramp from 0 to ss_max_ratio over ss_warmup_steps."""
    if ss_warmup_steps <= 0:
        return ss_max_ratio
    return min(ss_max_ratio, ss_max_ratio * global_step / ss_warmup_steps)


def generate_continuation(model, tokenizer, prefix_ids, max_tokens, temperature, device):
    """
    Autoregressively generate a continuation from prefix_ids.

    Temporarily removes gate hooks (they interfere with KV cache),
    runs generation in eval + no_grad mode, then restores hooks.

    Returns:
        full_ids: (1, prefix_len + gen_len) tensor of the full sequence
        gen_len: number of newly generated tokens
    """
    # Remove gate hooks temporarily
    saved_hooks = []
    if hasattr(model, '_hooks') and model._hooks:
        saved_hooks = list(model._hooks)
        for h in saved_hooks:
            h.remove()
        model._hooks = []

    model.eval()
    with torch.no_grad():
        prefix = prefix_ids.unsqueeze(0).to(device)  # (1, prefix_len)
        generated = model.base_model.generate(
            input_ids=prefix,
            max_new_tokens=max_tokens,
            temperature=temperature,
            do_sample=True,
            top_p=0.9,
            pad_token_id=tokenizer.pad_token_id,
        )
    model.train()

    # Restore gate hooks
    if saved_hooks and model.gate_type != "none":
        model._hooks = []
        for i, layer in enumerate(model.base_model.base_model.model.model.layers):
            model._hooks.append(layer.register_forward_hook(model._make_hook(i)))

    gen_len = generated.shape[1] - prefix.shape[1]
    return generated, gen_len


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
    # Scheduled Sampling arguments
    parser.add_argument("--scheduled-sampling", action="store_true", help="Enable scheduled sampling")
    parser.add_argument("--ss-max-ratio", type=float, default=0.3, help="Maximum SS probability")
    parser.add_argument("--ss-warmup-steps", type=int, default=100, help="Steps to linearly ramp SS ratio from 0 to max")
    parser.add_argument("--ss-gen-max-tokens", type=int, default=128, help="Max tokens for autoregressive generation in SS")
    parser.add_argument("--ss-gen-temperature", type=float, default=0.7, help="Temperature for SS generation")
    args = parser.parse_args()

    set_seed(args.seed)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Device: {device}")
    if torch.cuda.is_available():
        print(f"GPU: {torch.cuda.get_device_name(0)}")
        print(f"VRAM: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")

    print(f"Gate type: {args.gate_type}")
    if args.scheduled_sampling:
        print(f"Scheduled Sampling: ENABLED (max_ratio={args.ss_max_ratio}, warmup={args.ss_warmup_steps}, "
              f"gen_max_tokens={args.ss_gen_max_tokens}, temperature={args.ss_gen_temperature})")
    else:
        print("Scheduled Sampling: DISABLED (standard teacher forcing)")
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
    dataset = MultiTurnSSDataset(args.data_dir, tokenizer, max_seq_len=args.max_seq_len)
    dataloader = DataLoader(dataset, batch_size=1, shuffle=True, collate_fn=collate_fn, num_workers=0)
    print(f"Dataset size: {len(dataset)}")

    gate_params = []
    lora_params = []
    for name, param in model.named_parameters():
        if param.requires_grad:
            if 'gates.' in name or 'turn_embedding.' in name:
                gate_params.append(param)
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

    # SS statistics
    ss_used_count = 0
    ss_total_count = 0
    ss_fallback_count = 0

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
            first_assistant_start = batch["first_assistant_start"]

            # ---- Decide whether to use scheduled sampling this step ----
            use_ss = False
            if args.scheduled_sampling and first_assistant_start > 0:
                ss_ratio = get_ss_ratio(global_step, args.ss_warmup_steps, args.ss_max_ratio)
                ss_total_count += 1
                if random.random() < ss_ratio:
                    use_ss = True

            if use_ss:
                # ---- SS path: generate continuation, then compute GAR on it ----
                prefix_ids = input_ids[0, :first_assistant_start]  # (prefix_len,)

                generated_ids, gen_len = generate_continuation(
                    model, tokenizer, prefix_ids,
                    max_tokens=args.ss_gen_max_tokens,
                    temperature=args.ss_gen_temperature,
                    device=device,
                )

                if gen_len < 2:
                    # Generation too short, fall back to teacher forcing
                    ss_fallback_count += 1
                    use_ss = False
                else:
                    ss_used_count += 1

                    # Truncate to max_seq_len
                    if generated_ids.shape[1] > args.max_seq_len:
                        generated_ids = generated_ids[:, :args.max_seq_len]

                    # Build turn features and boundaries for the generated sequence
                    gen_ids_1d = generated_ids.squeeze(0)
                    gen_boundaries = detect_turn_boundaries(gen_ids_1d, tokenizer)
                    gen_turn_feats = build_turn_features(gen_ids_1d, tokenizer)

                    # Build labels: mask everything except generated assistant content
                    gen_labels = torch.full_like(generated_ids, -100)
                    for turn in gen_boundaries["turns"]:
                        if turn["role"] == "assistant":
                            gen_labels[0, turn["content_start"]:turn["content_end"]] = \
                                generated_ids[0, turn["content_start"]:turn["content_end"]]

                    gen_turn_feats_device = {
                        k: v.to(device) if isinstance(v, torch.Tensor) else v
                        for k, v in gen_turn_feats.items()
                    }

                    # Forward pass on generated sequence (with gradients for GAR)
                    with measurer.measure():
                        outputs = model(
                            generated_ids.to(device),
                            labels=gen_labels.to(device),
                            turn_features=gen_turn_feats_device,
                            output_attentions=True,
                        )

                    l_ntp = outputs.loss

                    # GAR on generated text: may have only 1 assistant turn
                    gen_goal_pos = gen_boundaries["goal_token_positions"]
                    gen_assistant_pos = gen_boundaries["assistant_last_token_positions"]

                    if len(gen_assistant_pos) >= 1 and len(gen_goal_pos) > 0:
                        gar_per_turn = []
                        for pos in gen_assistant_pos:
                            gar_val = measurer.compute_gar_differentiable(gen_goal_pos, [pos])
                            gar_per_turn.append(gar_val)

                        if len(gar_per_turn) >= 2:
                            # Multiple turns: use standard GAR loss
                            l_gar = compute_gar_loss(
                                gar_per_turn, epsilon=args.gar_epsilon,
                                mode=args.gar_loss_mode, target=args.gar_target,
                            )
                        else:
                            # Single turn: use MSE target directly
                            gar_val = gar_per_turn[0]
                            l_gar = (gar_val - args.gar_target) ** 2
                    else:
                        l_gar = torch.tensor(0.0, device=device, requires_grad=True)

                    # Gate diversity on generated sequence
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

            if not use_ss:
                # ---- Standard teacher-forced path (identical to train.py) ----
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

            loss = l_ntp + args.lambda_gar * l_gar + args.lambda_gate_div * l_gate_div
            loss = loss / args.grad_accum
            loss.backward()

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

            epoch_loss += loss.item() * args.grad_accum
            epoch_ntp += l_ntp.item()
            epoch_gar += l_gar.item()
            epoch_div += l_gate_div.item()
            num_batches += 1

            if step % 50 == 0 or args.dry_run:
                mem_used = torch.cuda.max_memory_allocated() / 1e9 if torch.cuda.is_available() else 0
                gate_vals = model.get_gate_values()
                mean_gate = np.mean([g.mean().item() for g in gate_vals.values()]) if gate_vals else 0
                ss_tag = " [SS]" if use_ss else ""
                ss_stats_str = ""
                if args.scheduled_sampling:
                    current_ratio = get_ss_ratio(global_step, args.ss_warmup_steps, args.ss_max_ratio)
                    ss_stats_str = f" | SS_ratio={current_ratio:.3f} used={ss_used_count}/{ss_total_count}"
                print(
                    f"Epoch {epoch} Step {step}{ss_tag} | "
                    f"L_NTP={l_ntp.item():.4f} L_GAR={l_gar.item():.4f} L_DIV={l_gate_div.item():.4f} "
                    f"Loss={loss.item()*args.grad_accum:.4f} | "
                    f"Gate={mean_gate:.4f} | Mem={mem_used:.1f}GB{ss_stats_str}"
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
        if args.scheduled_sampling:
            print(f"  SS stats: used={ss_used_count} total={ss_total_count} fallback={ss_fallback_count}")

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

    if args.scheduled_sampling:
        print(f"SS final stats: used={ss_used_count} total={ss_total_count} fallback={ss_fallback_count}")
        if ss_total_count > 0:
            print(f"  Effective SS rate: {ss_used_count / ss_total_count:.3f}")

    log_gate_stats(model, global_step, detailed=True)

    os.makedirs(args.output_dir, exist_ok=True)
    model.base_model.save_pretrained(os.path.join(args.output_dir, "lora"))
    if model.gates is not None:
        gate_state = {"gates": model.gates.state_dict()}
        if hasattr(model, "turn_embedding"):
            gate_state["turn_embedding"] = model.turn_embedding.state_dict()
        torch.save(gate_state, os.path.join(args.output_dir, "gate_params.pt"))

    config_dict = {
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
        "scheduled_sampling": args.scheduled_sampling,
        "ss_max_ratio": args.ss_max_ratio,
        "ss_warmup_steps": args.ss_warmup_steps,
        "ss_gen_max_tokens": args.ss_gen_max_tokens,
        "ss_gen_temperature": args.ss_gen_temperature,
        "ss_used_count": ss_used_count,
        "ss_total_count": ss_total_count,
        "ss_fallback_count": ss_fallback_count,
    }
    with open(os.path.join(args.output_dir, "train_config.json"), "w") as f:
        json.dump(config_dict, f, indent=2)

    print(f"Final model saved to {args.output_dir}")
    print(f"Gate parameters received gradients during training: {gate_grad_observed}")


if __name__ == "__main__":
    main()
