import os
os.environ["CUDA_VISIBLE_DEVICES"] = "4"

"""StructFuse contrastive training entry point.

Trains a bi-encoder (Qwen2.5-Coder-3B) with InfoNCE loss, data-flow-weighted
positives, and configurable hard-negative mining.  Supports single/multi-GPU
via HuggingFace Accelerate, LoRA, gradient checkpointing, and W&B logging.
"""

from __future__ import annotations

import argparse
import json
import math
import os
import random
from pathlib import Path
from typing import Any, Dict, List

import numpy as np
import torch
from torch.utils.data import DataLoader, Dataset
from transformers import AutoTokenizer, get_cosine_schedule_with_warmup

from accelerate import Accelerator
from accelerate.utils import set_seed

from contrastive_model import StructFuseEncoder
from hard_negative_mining import build_miner, mine_batch


# ── Dataset ──────────────────────────────────────────────────────────

class ContrastiveDataset(Dataset):
    """
    Each sample: {query, positive, negatives[], pos_weight, features[]}.

    The raw data file is JSONL with fields:
        query_id, query_tokens, pos_id, pos_tokens, pos_dataflow_distance,
        neg_candidates (list of file ids), features (dict per candidate).

    Negatives are mined dynamically per epoch via `refresh_negatives()`.
    """

    def __init__(
        self,
        data_path: str,
        tokenizer: AutoTokenizer,
        max_seq_length: int,
        num_negatives: int,
        pos_weight_alpha: float,
        use_fusion_head: bool,
    ):
        self.tokenizer = tokenizer
        self.max_seq_length = max_seq_length
        self.num_negatives = num_negatives
        self.alpha = pos_weight_alpha
        self.use_fusion_head = use_fusion_head

        self.samples: List[Dict[str, Any]] = []
        with open(data_path) as f:
            for line in f:
                if line.strip():
                    self.samples.append(json.loads(line))

        # mined negatives, refreshed each epoch
        self._negatives: Dict[int, List[Dict[str, Any]]] = {}

    def refresh_negatives(self, mined: Dict[str, List[tuple]]):
        """Update negatives after an epoch-level mining pass."""
        self._negatives = {}
        for idx, sample in enumerate(self.samples):
            qid = sample["query_id"]
            negs = mined.get(qid, [])
            self._negatives[idx] = negs

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        s = self.samples[idx]

        query_enc = self.tokenizer(
            s["query_tokens"], truncation=True, max_length=self.max_seq_length,
            padding=False, return_tensors=None,
        )
        pos_enc = self.tokenizer(
            s["pos_tokens"], truncation=True, max_length=self.max_seq_length,
            padding=False, return_tensors=None,
        )

        # positive weight from data-flow distance
        dist = s.get("pos_dataflow_distance", 1.0)
        pos_weight = math.exp(-self.alpha * dist)

        # negatives
        neg_pool = self._negatives.get(idx, [])
        if len(neg_pool) < self.num_negatives:
            # fallback: use candidates from the sample itself
            fallback = s.get("neg_candidates", [])
            random.shuffle(fallback)
            while len(neg_pool) < self.num_negatives and fallback:
                cid = fallback.pop()
                neg_pool.append({"id": cid, "tokens": s.get("candidate_tokens", {}).get(cid, "")})

        neg_encs = []
        for ni in range(self.num_negatives):
            if ni < len(neg_pool):
                neg_item = neg_pool[ni]
                tokens = neg_item.get("tokens", neg_item.get("id", ""))
            else:
                tokens = ""
            neg_encs.append(self.tokenizer(
                tokens, truncation=True, max_length=self.max_seq_length,
                padding=False, return_tensors=None,
            ))

        # features for fusion head
        features = None
        if self.use_fusion_head:
            features = self._extract_features(s, neg_pool)

        return {
            "query_ids": query_enc["input_ids"],
            "query_mask": query_enc["attention_mask"],
            "pos_ids": pos_enc["input_ids"],
            "pos_mask": pos_enc["attention_mask"],
            "neg_ids": [ne["input_ids"] for ne in neg_encs],
            "neg_mask": [ne["attention_mask"] for ne in neg_encs],
            "pos_weight": pos_weight,
            "features": features,
        }

    def _extract_features(self, sample, neg_pool) -> List[List[float]]:
        """Build (1+K, NUM_FEATURES) feature matrix for pos + negatives."""
        feat_keys = ["dataflow_distance", "bm25_score", "co_change_freq",
                      "inter_procedural_flag", "path_count"]
        all_feats = []
        # positive features
        pos_feat = [float(sample.get(f"pos_{k}", 0.0)) for k in feat_keys]
        all_feats.append(pos_feat)
        # negative features
        for ni in range(self.num_negatives):
            if ni < len(neg_pool):
                neg_item = neg_pool[ni]
                nf = [float(neg_item.get(k, 0.0)) for k in feat_keys]
            else:
                nf = [0.0] * len(feat_keys)
            all_feats.append(nf)
        return all_feats


def collate_fn(batch: List[Dict]) -> Dict[str, torch.Tensor]:
    """Pad variable-length sequences and stack into tensors."""

    def _pad_1d(seqs, pad_value=0):
        max_len = max(len(s) for s in seqs)
        padded = [s + [pad_value] * (max_len - len(s)) for s in seqs]
        return torch.tensor(padded, dtype=torch.long)

    def _pad_2d(batch_seqs, pad_value=0):
        """batch_seqs: list of list-of-seqs (B x K x varying L)."""
        max_len = max(len(s) for seqs in batch_seqs for s in seqs)
        result = []
        for seqs in batch_seqs:
            padded = [s + [pad_value] * (max_len - len(s)) for s in seqs]
            result.append(padded)
        return torch.tensor(result, dtype=torch.long)

    query_ids = _pad_1d([b["query_ids"] for b in batch])
    query_mask = _pad_1d([b["query_mask"] for b in batch])
    pos_ids = _pad_1d([b["pos_ids"] for b in batch])
    pos_mask = _pad_1d([b["pos_mask"] for b in batch])
    neg_ids = _pad_2d([b["neg_ids"] for b in batch])
    neg_mask = _pad_2d([b["neg_mask"] for b in batch])
    pos_weights = torch.tensor([b["pos_weight"] for b in batch], dtype=torch.float32)

    out = {
        "query_ids": query_ids,
        "query_mask": query_mask,
        "pos_ids": pos_ids,
        "pos_mask": pos_mask,
        "neg_ids": neg_ids,
        "neg_mask": neg_mask,
        "pos_weights": pos_weights,
    }

    if batch[0]["features"] is not None:
        out["features"] = torch.tensor(
            [b["features"] for b in batch], dtype=torch.float32
        )

    return out


# ── Evaluation ───────────────────────────────────────────────────────

@torch.no_grad()
def evaluate(model: StructFuseEncoder, val_loader: DataLoader, accelerator: Accelerator) -> Dict[str, float]:
    """Compute recall@1/5/10 and average loss on the validation set."""
    model.eval()
    total_loss = 0.0
    total_correct = {1: 0, 5: 0, 10: 0}
    total_samples = 0

    for batch in val_loader:
        kwargs = {
            "query_ids": batch["query_ids"],
            "query_mask": batch["query_mask"],
            "pos_ids": batch["pos_ids"],
            "pos_mask": batch["pos_mask"],
            "neg_ids": batch["neg_ids"],
            "neg_mask": batch["neg_mask"],
            "pos_weights": batch["pos_weights"],
            "features": batch.get("features"),
        }
        loss, logits = model(**kwargs)

        total_loss += loss.item() * logits.size(0)
        total_samples += logits.size(0)

        for k in [1, 5, 10]:
            if logits.size(1) >= k:
                topk = logits.topk(min(k, logits.size(1)), dim=1).indices
                total_correct[k] += (topk == 0).any(dim=1).sum().item()
            else:
                total_correct[k] += (logits.argmax(dim=1) == 0).sum().item()

    # Aggregate across all processes for multi-GPU correctness
    stats = torch.tensor(
        [total_loss, total_samples] + [total_correct[k] for k in [1, 5, 10]],
        device=accelerator.device, dtype=torch.float64,
    )
    stats = accelerator.reduce(stats, reduction="sum")
    total_loss = stats[0].item()
    total_samples = stats[1].item()
    for i, k in enumerate([1, 5, 10]):
        total_correct[k] = stats[2 + i].item()

    model.train()
    metrics = {"val_loss": total_loss / max(total_samples, 1)}
    for k in [1, 5, 10]:
        metrics[f"recall@{k}"] = total_correct[k] / max(total_samples, 1)
    return metrics


# ── Training ─────────────────────────────────────────────────────────

def train(args):
    set_seed(args.seed)
    accelerator = Accelerator(log_with="wandb" if args.wandb_project else None)

    if args.wandb_project and accelerator.is_main_process:
        accelerator.init_trackers(
            project_name=args.wandb_project,
            config=vars(args),
            init_kwargs={"wandb": {"name": args.wandb_run_name}},
        )

    # tokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model_name, trust_remote_code=True)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    # model
    model = StructFuseEncoder(
        model_name=args.model_name,
        proj_dim=args.proj_dim,
        use_projection=True,
        use_lora=args.use_lora,
        lora_r=args.lora_r,
        lora_alpha=args.lora_r * 2,
        use_fusion_head=args.use_fusion_head,
    )
    if args.gradient_checkpointing:
        model.enable_gradient_checkpointing()

    # datasets
    train_ds = ContrastiveDataset(
        args.train_file, tokenizer, args.max_seq_length,
        args.num_negatives, args.pos_weight_alpha, args.use_fusion_head,
    )
    val_ds = ContrastiveDataset(
        args.val_file, tokenizer, args.max_seq_length,
        args.num_negatives, args.pos_weight_alpha, args.use_fusion_head,
    )

    train_loader = DataLoader(
        train_ds, batch_size=args.batch_size, shuffle=True,
        collate_fn=collate_fn, num_workers=4, pin_memory=True,
    )
    val_loader = DataLoader(
        val_ds, batch_size=args.batch_size, shuffle=False,
        collate_fn=collate_fn, num_workers=2, pin_memory=True,
    )

    # hard-negative miner
    dataflow_graph = _load_json_as_sets(args.dataflow_graph_file) if args.dataflow_graph_file else None
    embeddings = _load_embeddings(args.embeddings_file) if args.embeddings_file else None
    miner = build_miner(
        strategy=args.hard_negative_strategy,
        dataflow_graph=dataflow_graph,
        embeddings=embeddings,
    )

    # optimizer & scheduler
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate, weight_decay=0.01)
    total_steps = len(train_loader) * args.num_epochs
    warmup_steps = int(total_steps * args.warmup_ratio)
    scheduler = get_cosine_schedule_with_warmup(optimizer, warmup_steps, total_steps)

    # accelerate prepare
    model, optimizer, train_loader, val_loader, scheduler = accelerator.prepare(
        model, optimizer, train_loader, val_loader, scheduler
    )

    # ── training loop ────────────────────────────────────────────
    global_step = 0
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    for epoch in range(args.num_epochs):
        # epoch-level negative mining
        if accelerator.is_main_process:
            accelerator.print(f"[Epoch {epoch+1}] Mining hard negatives ({args.hard_negative_strategy})...")
            queries = [s["query_id"] for s in train_ds.samples]
            pos_map = {s["query_id"]: [s["pos_id"]] for s in train_ds.samples}
            all_cands = list({s["query_id"] for s in train_ds.samples}
                            | {s["pos_id"] for s in train_ds.samples})
            mined = mine_batch(miner, queries, pos_map, all_cands, args.num_negatives)
            train_ds.refresh_negatives(mined)

        accelerator.wait_for_everyone()
        model.train()

        for batch in train_loader:
            kwargs = {
                "query_ids": batch["query_ids"],
                "query_mask": batch["query_mask"],
                "pos_ids": batch["pos_ids"],
                "pos_mask": batch["pos_mask"],
                "neg_ids": batch["neg_ids"],
                "neg_mask": batch["neg_mask"],
                "pos_weights": batch["pos_weights"],
                "features": batch.get("features"),
            }
            loss, logits = model(**kwargs)

            accelerator.backward(loss)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()
            scheduler.step()
            optimizer.zero_grad()

            global_step += 1

            if accelerator.is_main_process and global_step % 50 == 0:
                lr = scheduler.get_last_lr()[0]
                accelerator.print(f"  step {global_step}  loss={loss.item():.4f}  lr={lr:.2e}")
                if args.wandb_project:
                    accelerator.log({"train_loss": loss.item(), "learning_rate": lr}, step=global_step)

            if global_step % args.eval_steps == 0:
                metrics = evaluate(
                    accelerator.unwrap_model(model), val_loader, accelerator
                )
                if accelerator.is_main_process:
                    accelerator.print(f"  [eval@{global_step}] {metrics}")
                    if args.wandb_project:
                        accelerator.log(metrics, step=global_step)

            if global_step % args.save_steps == 0 and accelerator.is_main_process:
                ckpt_dir = output_dir / f"checkpoint-{global_step}"
                _save_checkpoint(accelerator.unwrap_model(model), tokenizer, ckpt_dir, args)

    # ── final save ───────────────────────────────────────────────
    if accelerator.is_main_process:
        final_metrics = evaluate(accelerator.unwrap_model(model), val_loader, accelerator)
        accelerator.print(f"[Final eval] {final_metrics}")
        if args.wandb_project:
            accelerator.log(final_metrics, step=global_step)
        _save_checkpoint(accelerator.unwrap_model(model), tokenizer, output_dir / "final", args)
        accelerator.print(f"Training complete. Model saved to {output_dir / 'final'}")

    if args.wandb_project:
        accelerator.end_training()


# ── helpers ──────────────────────────────────────────────────────────

def _save_checkpoint(model, tokenizer, path, args):
    path = Path(path)
    path.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), path / "model.pt")
    tokenizer.save_pretrained(path)
    with open(path / "training_config.json", "w") as f:
        json.dump(vars(args), f, indent=2)


def _load_json_as_sets(path: str) -> Dict[str, set]:
    with open(path) as f:
        raw = json.load(f)
    return {k: set(v) for k, v in raw.items()}


def _load_embeddings(path: str) -> Dict[str, np.ndarray]:
    data = np.load(path, allow_pickle=True)
    return {str(k): data[k] for k in data.files}


# ── CLI ──────────────────────────────────────────────────────────────

def parse_args():
    p = argparse.ArgumentParser(description="StructFuse contrastive training")
    p.add_argument("--model-name", default="Qwen/Qwen2.5-Coder-3B")
    p.add_argument("--train-file", required=True)
    p.add_argument("--val-file", required=True)
    p.add_argument("--output-dir", required=True)
    p.add_argument("--batch-size", type=int, default=8)
    p.add_argument("--learning-rate", type=float, default=2e-5)
    p.add_argument("--num-epochs", type=int, default=3)
    p.add_argument("--warmup-ratio", type=float, default=0.1)
    p.add_argument("--num-negatives", type=int, default=7)
    p.add_argument("--hard-negative-strategy", choices=["random", "embedding_distance", "dataflow_aware"], default="dataflow_aware")
    p.add_argument("--hard-negative-ratio", type=float, default=0.5)
    p.add_argument("--temperature", type=float, default=0.07)
    p.add_argument("--pos-weight-alpha", type=float, default=1.0)
    p.add_argument("--use-fusion-head", action="store_true")
    p.add_argument("--use-lora", action="store_true")
    p.add_argument("--lora-r", type=int, default=16)
    p.add_argument("--proj-dim", type=int, default=256)
    p.add_argument("--gradient-checkpointing", action="store_true")
    p.add_argument("--eval-steps", type=int, default=500)
    p.add_argument("--save-steps", type=int, default=1000)
    p.add_argument("--max-seq-length", type=int, default=2048)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--wandb-project", default="structfuse")
    p.add_argument("--wandb-run-name", default=None)
    p.add_argument("--dataflow-graph-file", default=None, help="JSON file: {file_id: [reachable_ids]}")
    p.add_argument("--embeddings-file", default=None, help=".npz file with pre-computed embeddings")
    return p.parse_args()


if __name__ == "__main__":
    train(parse_args())
