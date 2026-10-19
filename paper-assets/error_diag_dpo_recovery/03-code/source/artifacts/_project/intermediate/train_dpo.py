#!/usr/bin/env python3
"""DPO training with ETADN temporal discount weighting.

Two modes:
  single_gamma: all samples share one gamma (baseline / gamma sweep)
  etadn: per-sample gamma_e read from JSONL (ETADN method)

Key design: gamma(d) is NOT computed here. In etadn mode it comes directly
from the JSONL gamma_e field produced by build_dpo_pairs.py.

Input: JSONL from build_dpo_pairs.py
  Each line: {prompt, chosen, rejected, gamma_e, error_type, ...}
  prompt/chosen/rejected are lists of message dicts [{role, content}, ...]

Output: model checkpoints in --output_dir

Memory strategy: reference model logps are precomputed once before training,
so only the policy model stays on GPU during the training loop.

Dependencies: torch, transformers, wandb
"""
import argparse
import json
import logging
import os
import sys
from functools import partial
from pathlib import Path

import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    get_cosine_schedule_with_warmup,
)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from dmpo_loss import compute_phi_weights

logger = logging.getLogger("train_dpo")


# ---------------------------------------------------------------------------
# Dataset
# ---------------------------------------------------------------------------


class DPODataset(Dataset):
    """DPO dataset from JSONL with prompt/chosen/rejected message lists."""

    def __init__(self, data_path: str, tokenizer, max_length: int, mode: str, gamma: float):
        self.samples = []
        with open(data_path) as f:
            for line in f:
                if line.strip():
                    self.samples.append(json.loads(line))
        self.tokenizer = tokenizer
        self.max_length = max_length
        self.mode = mode
        self.gamma = gamma
        logger.info("Loaded %d DPO samples from %s", len(self.samples), data_path)

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        sample = self.samples[idx]
        prompt = sample["prompt"]
        chosen = sample["chosen"]
        rejected = sample["rejected"]

        # gamma source: JSONL gamma_e for etadn, CLI --gamma for single_gamma
        gamma = sample["gamma_e"] if self.mode == "etadn" else self.gamma

        # Tokenize prompt to measure prefix length
        prompt_ids = self.tokenizer.apply_chat_template(
            prompt, add_generation_prompt=True
        )
        # Tokenize full sequences (prompt + response)
        chosen_ids = self.tokenizer.apply_chat_template(prompt + chosen)
        rejected_ids = self.tokenizer.apply_chat_template(prompt + rejected)

        prompt_len = min(len(prompt_ids), self.max_length)
        chosen_ids = chosen_ids[: self.max_length]
        rejected_ids = rejected_ids[: self.max_length]

        return {
            "idx": idx,
            "chosen_ids": chosen_ids,
            "rejected_ids": rejected_ids,
            "prompt_len": prompt_len,
            "gamma": gamma,
        }


# ---------------------------------------------------------------------------
# Collation
# ---------------------------------------------------------------------------


def collate_dpo(batch: list[dict], pad_token_id: int) -> dict:
    """Pad chosen and rejected sequences separately."""
    max_c = max(len(b["chosen_ids"]) for b in batch)
    max_r = max(len(b["rejected_ids"]) for b in batch)

    indices, gammas, prompt_lens = [], [], []
    chosen_ids, chosen_mask, chosen_resp_lens = [], [], []
    rejected_ids, rejected_mask, rejected_resp_lens = [], [], []

    for b in batch:
        pl = b["prompt_len"]
        indices.append(b["idx"])
        prompt_lens.append(pl)
        gammas.append(b["gamma"])

        c = b["chosen_ids"]
        c_pad = max_c - len(c)
        chosen_ids.append(c + [pad_token_id] * c_pad)
        chosen_mask.append([1] * len(c) + [0] * c_pad)
        chosen_resp_lens.append(max(len(c) - pl, 0))

        r = b["rejected_ids"]
        r_pad = max_r - len(r)
        rejected_ids.append(r + [pad_token_id] * r_pad)
        rejected_mask.append([1] * len(r) + [0] * r_pad)
        rejected_resp_lens.append(max(len(r) - pl, 0))

    return {
        "indices": indices,
        "chosen_ids": torch.tensor(chosen_ids, dtype=torch.long),
        "chosen_mask": torch.tensor(chosen_mask, dtype=torch.long),
        "rejected_ids": torch.tensor(rejected_ids, dtype=torch.long),
        "rejected_mask": torch.tensor(rejected_mask, dtype=torch.long),
        "prompt_lens": prompt_lens,
        "chosen_resp_lens": chosen_resp_lens,
        "rejected_resp_lens": rejected_resp_lens,
        "gammas": gammas,
    }


# ---------------------------------------------------------------------------
# Per-token log probs
# ---------------------------------------------------------------------------


def get_per_token_logps(
    model: torch.nn.Module,
    input_ids: torch.Tensor,
    attention_mask: torch.Tensor,
) -> torch.Tensor:
    """Per-token log P(token_t | prefix[:t]).

    Returns (B, L) where position t holds log P(input_ids[t] | input_ids[:t]).
    Position 0 is always 0 (no conditioning context for the first token).
    """
    outputs = model(input_ids=input_ids, attention_mask=attention_mask)
    logits = outputs.logits[:, :-1, :]  # (B, L-1, V)
    labels = input_ids[:, 1:]  # (B, L-1)
    log_probs = F.log_softmax(logits, dim=-1)
    token_logps = torch.gather(log_probs, 2, labels.unsqueeze(-1)).squeeze(-1)
    # Left-pad one zero so result[t] aligns with input_ids[t]
    return F.pad(token_logps, (1, 0), value=0.0)


# ---------------------------------------------------------------------------
# Reference logps precomputation
# ---------------------------------------------------------------------------


@torch.no_grad()
def precompute_ref_logps(
    model: torch.nn.Module,
    dataset: DPODataset,
    tokenizer,
    device: torch.device,
    batch_size: int,
) -> tuple[dict[int, torch.Tensor], dict[int, torch.Tensor]]:
    """Precompute reference model logps for all samples (response tokens only).

    Returns two dicts mapping sample index -> (resp_len,) CPU tensor.
    After this call the model can be switched to training mode in-place.
    """
    model.eval()
    loader = DataLoader(
        dataset,
        batch_size=batch_size,
        shuffle=False,
        collate_fn=partial(collate_dpo, pad_token_id=tokenizer.pad_token_id),
    )

    ref_chosen: dict[int, torch.Tensor] = {}
    ref_rejected: dict[int, torch.Tensor] = {}

    for batch in loader:
        c_logps = get_per_token_logps(
            model, batch["chosen_ids"].to(device), batch["chosen_mask"].to(device)
        )
        r_logps = get_per_token_logps(
            model, batch["rejected_ids"].to(device), batch["rejected_mask"].to(device)
        )

        B = batch["chosen_ids"].shape[0]
        for i in range(B):
            idx = batch["indices"][i]
            pl = batch["prompt_lens"][i]
            c_rl = batch["chosen_resp_lens"][i]
            r_rl = batch["rejected_resp_lens"][i]
            ref_chosen[idx] = c_logps[i, pl : pl + c_rl].cpu()
            ref_rejected[idx] = r_logps[i, pl : pl + r_rl].cpu()

    logger.info("Precomputed ref logps for %d samples", len(ref_chosen))
    return ref_chosen, ref_rejected


# ---------------------------------------------------------------------------
# Batch loss
# ---------------------------------------------------------------------------


def compute_batch_loss(
    policy_model: torch.nn.Module,
    batch: dict,
    ref_chosen_all: dict[int, torch.Tensor],
    ref_rejected_all: dict[int, torch.Tensor],
    beta: float,
    device: torch.device,
) -> tuple[torch.Tensor, dict]:
    """Forward policy model and compute phi-weighted DPO loss."""
    # Policy forward
    pc_logps = get_per_token_logps(
        policy_model, batch["chosen_ids"].to(device), batch["chosen_mask"].to(device)
    )
    pr_logps = get_per_token_logps(
        policy_model, batch["rejected_ids"].to(device), batch["rejected_mask"].to(device)
    )

    B = batch["chosen_ids"].shape[0]
    losses = []
    chosen_rewards = []
    rejected_rewards = []

    for i in range(B):
        idx = batch["indices"][i]
        pl = batch["prompt_lens"][i]
        c_rl = batch["chosen_resp_lens"][i]
        r_rl = batch["rejected_resp_lens"][i]
        gamma = batch["gammas"][i]

        if c_rl <= 0 or r_rl <= 0:
            continue

        # phi discount weights from etadn_discount
        w_c = compute_phi_weights(c_rl, gamma).to(device)
        w_r = compute_phi_weights(r_rl, gamma).to(device)

        # Policy response logps
        pc = pc_logps[i, pl : pl + c_rl]
        pr = pr_logps[i, pl : pl + r_rl]

        # Precomputed ref response logps
        rc = ref_chosen_all[idx].to(device)
        rr = ref_rejected_all[idx].to(device)

        # Weighted log-ratios
        chosen_logratio = (pc * w_c).sum() - (rc * w_c).sum()
        rejected_logratio = (pr * w_r).sum() - (rr * w_r).sum()

        logit = beta * (chosen_logratio - rejected_logratio)
        losses.append(-F.logsigmoid(logit))

        chosen_rewards.append(chosen_logratio.detach())
        rejected_rewards.append(rejected_logratio.detach())

    if not losses:
        return torch.tensor(0.0, device=device, requires_grad=True), {}

    loss = torch.stack(losses).mean()
    cr = torch.stack(chosen_rewards)
    rr = torch.stack(rejected_rewards)
    metrics = {
        "loss": loss.item(),
        "chosen_reward": cr.mean().item(),
        "rejected_reward": rr.mean().item(),
        "reward_margin": (cr - rr).mean().item(),
        "reward_accuracy": (cr > rr).float().mean().item(),
    }
    return loss, metrics


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------


def train(args: argparse.Namespace):
    import wandb

    torch.manual_seed(args.seed)
    device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")

    wandb.init(
        project=args.wandb_project,
        name=args.wandb_run_name or f"{args.mode}_s{args.seed}",
        config=vars(args),
    )

    # Tokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token_id is None:
        tokenizer.pad_token_id = tokenizer.eos_token_id

    # Model
    logger.info("Loading model: %s", args.model_name)
    model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map={"": device},
    )

    # Dataset
    dataset = DPODataset(
        args.data_path, tokenizer, args.max_length, args.mode, args.gamma
    )

    # Precompute ref logps (model is the ref at initialization)
    logger.info("Precomputing reference logps...")
    ref_chosen, ref_rejected = precompute_ref_logps(
        model, dataset, tokenizer, device, args.batch_size
    )

    # Switch to training mode
    model.gradient_checkpointing_enable()
    model.train()

    loader = DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=True,
        collate_fn=partial(collate_dpo, pad_token_id=tokenizer.pad_token_id),
        drop_last=False,
    )

    optimizer = torch.optim.AdamW(
        model.parameters(), lr=args.learning_rate, weight_decay=0.01
    )
    total_steps = len(loader) * args.num_epochs
    warmup_steps = min(total_steps // 10, 100)
    scheduler = get_cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps)

    # Save training config
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    with open(out_dir / "training_config.json", "w") as f:
        json.dump(vars(args), f, indent=2)

    global_step = 0
    for epoch in range(args.num_epochs):
        epoch_loss = 0.0
        epoch_steps = 0

        for batch in loader:
            loss, metrics = compute_batch_loss(
                model, batch, ref_chosen, ref_rejected, args.beta, device
            )

            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()

            global_step += 1
            epoch_loss += loss.item()
            epoch_steps += 1

            wandb.log(
                {
                    "train/loss": loss.item(),
                    "train/lr": scheduler.get_last_lr()[0],
                    **{f"train/{k}": v for k, v in metrics.items() if k != "loss"},
                },
                step=global_step,
            )

            if global_step % 10 == 0:
                logger.info(
                    "Step %d | Loss %.4f | Margin %.4f | Acc %.2f",
                    global_step,
                    loss.item(),
                    metrics.get("reward_margin", 0),
                    metrics.get("reward_accuracy", 0),
                )

        avg_loss = epoch_loss / max(epoch_steps, 1)
        logger.info("Epoch %d/%d | Avg Loss %.4f", epoch + 1, args.num_epochs, avg_loss)
        wandb.log(
            {"train/epoch_loss": avg_loss, "train/epoch": epoch + 1}, step=global_step
        )

        ckpt_dir = out_dir / f"checkpoint-epoch{epoch + 1}"
        model.save_pretrained(ckpt_dir)
        tokenizer.save_pretrained(ckpt_dir)
        logger.info("Saved checkpoint: %s", ckpt_dir)

    final_dir = out_dir / "final"
    model.save_pretrained(final_dir)
    tokenizer.save_pretrained(final_dir)
    logger.info("Training complete. Final model: %s", final_dir)
    wandb.finish()


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="DPO training with ETADN temporal discount"
    )
    parser.add_argument("--data_path", type=str, required=True, help="DPO JSONL file")
    parser.add_argument(
        "--model_name",
        type=str,
        default="/root/autodl-tmp/.hf_cache/Qwen3-8B",
    )
    parser.add_argument("--output_dir", type=str, default="outputs/dpo")
    parser.add_argument(
        "--mode",
        type=str,
        choices=["single_gamma", "etadn"],
        required=True,
    )
    parser.add_argument(
        "--gamma", type=float, default=0.92, help="gamma for single_gamma mode"
    )
    parser.add_argument(
        "--gamma_min", type=float, default=0.85, help="gamma_min for etadn (logged only)"
    )
    parser.add_argument(
        "--gamma_max", type=float, default=0.97, help="gamma_max for etadn (logged only)"
    )
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--num_epochs", type=int, default=3)
    parser.add_argument("--batch_size", type=int, default=4)
    parser.add_argument("--learning_rate", type=float, default=5e-7)
    parser.add_argument("--max_length", type=int, default=2048)
    parser.add_argument("--wandb_project", type=str, default="etadn-dpo")
    parser.add_argument("--wandb_run_name", type=str, default=None)
    parser.add_argument("--beta", type=float, default=0.1, help="DPO temperature")
    parser.add_argument("--gpu", type=int, default=0)
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s %(message)s",
    )

    train(args)


if __name__ == "__main__":
    main()
