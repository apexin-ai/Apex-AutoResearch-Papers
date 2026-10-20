#!/usr/bin/env python3
"""Architecture ablation for progress stagnation detection.

Architectures:
  gru_attn     — GRU(256,2) + learned attention pooling over hidden states
  gru_meanpool — GRU(256,2) + mean pooling over hidden states
  transformer  — 2-layer Transformer encoder (d=256, 4 heads) + mean pool
  mlp          — mean-pool input embeddings → MLP(1024→256→1), no temporal modeling

Input:  data/embeddings.pt (1024-dim Qwen3-Embedding, conf≥2 filtered via split_info)
Split:  checkpoints/split_info.json (instance-level train/val/test)
Hypers: lr=1e-3, batch=64, epochs=50, early_stop patience=10, seed=42
Output: data/architecture_ablation_results.json
"""

import argparse
import json
import random
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn.utils.rnn import pack_padded_sequence, pad_packed_sequence
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import accuracy_score, f1_score


# ---------------------------------------------------------------------------
# Dataset / collate
# ---------------------------------------------------------------------------

class WindowDataset(Dataset):
    def __init__(self, embeddings, labels):
        self.embeddings = embeddings
        self.labels = labels

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        return self.embeddings[idx], self.labels[idx]


def collate_fn(batch):
    embs, labs = zip(*batch)
    lengths = torch.tensor([e.shape[0] for e in embs], dtype=torch.long)
    max_len = lengths.max().item()
    dim = embs[0].shape[1]
    padded = torch.zeros(len(batch), max_len, dim)
    for i, e in enumerate(embs):
        padded[i, : e.shape[0]] = e
    labels = torch.tensor(labs, dtype=torch.float32)
    return padded, labels, lengths


# ---------------------------------------------------------------------------
# Model architectures
# ---------------------------------------------------------------------------

def _make_length_mask(seq_len: int, lengths: torch.Tensor, device: torch.device):
    """Returns bool mask (B, T) where True = padding position."""
    return torch.arange(seq_len, device=device).unsqueeze(0) >= lengths.unsqueeze(1)


class GRUAttentionProbe(nn.Module):
    """GRU + learned attention over all hidden states."""

    def __init__(self, embed_dim, hidden_size=256, num_layers=2, dropout=0.1):
        super().__init__()
        self.gru = nn.GRU(embed_dim, hidden_size, num_layers, batch_first=True,
                          dropout=dropout if num_layers > 1 else 0.0)
        self.attn_score = nn.Linear(hidden_size, 1)
        self.classifier = nn.Linear(hidden_size, 1)

    def forward(self, x, lengths):
        lengths_dev = lengths.to(x.device)
        packed = pack_padded_sequence(x, lengths.cpu(), batch_first=True, enforce_sorted=False)
        output, _ = self.gru(packed)
        output, _ = pad_packed_sequence(output, batch_first=True)  # (B, T, H)
        scores = self.attn_score(output).squeeze(-1)              # (B, T)
        pad_mask = _make_length_mask(output.size(1), lengths_dev, x.device)
        scores = scores.masked_fill(pad_mask, float("-inf"))
        weights = F.softmax(scores, dim=1)                        # (B, T)
        context = (output * weights.unsqueeze(-1)).sum(dim=1)      # (B, H)
        return self.classifier(context).squeeze(-1)


class GRUMeanPoolProbe(nn.Module):
    """GRU + mean pooling over hidden states (no attention)."""

    def __init__(self, embed_dim, hidden_size=256, num_layers=2, dropout=0.1):
        super().__init__()
        self.gru = nn.GRU(embed_dim, hidden_size, num_layers, batch_first=True,
                          dropout=dropout if num_layers > 1 else 0.0)
        self.classifier = nn.Linear(hidden_size, 1)

    def forward(self, x, lengths):
        lengths_dev = lengths.to(x.device).unsqueeze(1).float()
        packed = pack_padded_sequence(x, lengths.cpu(), batch_first=True, enforce_sorted=False)
        output, _ = self.gru(packed)
        output, _ = pad_packed_sequence(output, batch_first=True)
        valid = (~_make_length_mask(output.size(1), lengths.to(x.device), x.device)).unsqueeze(-1).float()
        pooled = (output * valid).sum(dim=1) / lengths_dev
        return self.classifier(pooled).squeeze(-1)


class TransformerProbe(nn.Module):
    """Transformer encoder (project 1024→d_model) + mean pool."""

    def __init__(self, embed_dim, d_model=256, nhead=4, num_layers=2, dropout=0.1):
        super().__init__()
        self.proj = nn.Linear(embed_dim, d_model)
        layer = nn.TransformerEncoderLayer(
            d_model, nhead, dim_feedforward=d_model * 4, dropout=dropout, batch_first=True,
        )
        self.encoder = nn.TransformerEncoder(layer, num_layers)
        self.classifier = nn.Linear(d_model, 1)

    def forward(self, x, lengths):
        x = self.proj(x)
        lengths_dev = lengths.to(x.device)
        pad_mask = _make_length_mask(x.size(1), lengths_dev, x.device)
        x = self.encoder(x, src_key_padding_mask=pad_mask)
        valid = (~pad_mask).unsqueeze(-1).float()
        pooled = (x * valid).sum(dim=1) / lengths_dev.unsqueeze(1).float()
        return self.classifier(pooled).squeeze(-1)


class MLPProbe(nn.Module):
    """Mean-pool input embeddings → MLP. No temporal modeling."""

    def __init__(self, embed_dim, hidden_size=256, dropout=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(embed_dim, hidden_size),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_size, 1),
        )

    def forward(self, x, lengths):
        lengths_dev = lengths.to(x.device).unsqueeze(1).float()
        valid = (~_make_length_mask(x.size(1), lengths.to(x.device), x.device)).unsqueeze(-1).float()
        pooled = (x * valid).sum(dim=1) / lengths_dev
        return self.net(pooled).squeeze(-1)


ARCH_MAP = {
    "gru_attn": GRUAttentionProbe,
    "gru_meanpool": GRUMeanPoolProbe,
    "transformer": TransformerProbe,
    "mlp": MLPProbe,
}


def build_model(arch, embed_dim, hidden_size=256, num_layers=2, dropout=0.1):
    if arch == "transformer":
        return TransformerProbe(embed_dim, d_model=hidden_size, nhead=4,
                                num_layers=num_layers, dropout=dropout)
    if arch == "mlp":
        return MLPProbe(embed_dim, hidden_size, dropout)
    return ARCH_MAP[arch](embed_dim, hidden_size, num_layers, dropout)


# ---------------------------------------------------------------------------
# Training utilities
# ---------------------------------------------------------------------------

def set_seed(seed):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed_all(seed)


def count_params(model):
    return sum(p.numel() for p in model.parameters())


def compute_metrics(labels, preds):
    return {
        "macro_f1": f1_score(labels, preds, average="macro", zero_division=0),
        "accuracy": accuracy_score(labels, preds),
        "f1_stag": f1_score(labels, preds, pos_label=0, zero_division=0),
        "f1_prog": f1_score(labels, preds, pos_label=1, zero_division=0),
    }


@torch.no_grad()
def evaluate(model, loader, device):
    model.eval()
    all_labels, all_preds = [], []
    for padded, labels, lengths in loader:
        logits = model(padded.to(device), lengths)
        preds = (torch.sigmoid(logits) >= 0.5).long().cpu()
        all_labels.extend(labels.long().tolist())
        all_preds.extend(preds.tolist())
    return compute_metrics(all_labels, all_preds)


def train_one_arch(arch, train_ds, val_ds, test_ds, embed_dim, pos_weight, device, args):
    set_seed(args.seed)
    model = build_model(arch, embed_dim, args.hidden_size, args.num_layers, args.dropout).to(device)
    n_params = count_params(model)

    print(f"\n{'=' * 60}")
    print(f"Architecture: {arch} | Params: {n_params:,}")
    print(f"{'=' * 60}")

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True, collate_fn=collate_fn)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, collate_fn=collate_fn)
    test_loader = DataLoader(test_ds, batch_size=args.batch_size, collate_fn=collate_fn)

    optimizer = torch.optim.AdamW(model.parameters(), lr=args.lr, weight_decay=args.weight_decay)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    best_f1, best_state, patience_ctr, best_epoch = 0.0, None, 0, 0
    t0 = time.time()

    for epoch in range(1, args.epochs + 1):
        model.train()
        total_loss, n = 0.0, 0
        for padded, labels, lengths in train_loader:
            padded, labels = padded.to(device), labels.to(device)
            logits = model(padded, lengths)
            loss = criterion(logits, labels)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item() * len(labels)
            n += len(labels)

        avg_loss = total_loss / n
        val_m = evaluate(model, val_loader, device)

        improved = val_m["macro_f1"] > best_f1
        if improved:
            best_f1 = val_m["macro_f1"]
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            patience_ctr = 0
            best_epoch = epoch
        else:
            patience_ctr += 1

        tag = " *" if improved else ""
        print(f"  Epoch {epoch:2d} | loss={avg_loss:.4f} | val_F1={val_m['macro_f1']:.4f}{tag}")

        if patience_ctr >= args.patience:
            print(f"  Early stopping at epoch {epoch}")
            break

    elapsed = time.time() - t0

    # Evaluate best model on test set
    model.load_state_dict(best_state)
    model.to(device)
    test_m = evaluate(model, test_loader, device)

    print(f"  Best val F1: {best_f1:.4f} (epoch {best_epoch})")
    print(f"  Test: macro_f1={test_m['macro_f1']:.4f}  acc={test_m['accuracy']:.4f}  "
          f"f1_stag={test_m['f1_stag']:.4f}  f1_prog={test_m['f1_prog']:.4f}")
    print(f"  Time: {elapsed:.1f}s")

    return {
        "arch": arch,
        "params": n_params,
        "best_epoch": best_epoch,
        "best_val_f1": round(best_f1, 4),
        "test_macro_f1": round(test_m["macro_f1"], 4),
        "test_accuracy": round(test_m["accuracy"], 4),
        "test_f1_stag": round(test_m["f1_stag"], 4),
        "test_f1_prog": round(test_m["f1_prog"], 4),
        "train_time_s": round(elapsed, 1),
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    p = argparse.ArgumentParser(description="Architecture ablation for progress probe")
    p.add_argument("--arch", default="all",
                   choices=["gru_attn", "gru_meanpool", "transformer", "mlp", "all"])
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--batch_size", type=int, default=64)
    p.add_argument("--epochs", type=int, default=50)
    p.add_argument("--hidden_size", type=int, default=256)
    p.add_argument("--num_layers", type=int, default=2)
    p.add_argument("--dropout", type=float, default=0.1)
    p.add_argument("--weight_decay", type=float, default=0.01)
    p.add_argument("--patience", type=int, default=10)
    p.add_argument("--min_confidence", type=int, default=2)
    args = p.parse_args()

    device = f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu"
    print(f"Device: {device}")

    base = Path(__file__).parent

    # --- Load data ---
    data = torch.load(base / "data" / "embeddings.pt", weights_only=False)
    embeddings = data["embeddings"]
    labels = data["labels"]
    instance_ids = data["instance_ids"]
    confidences = data.get("confidences", [1] * len(labels))
    embed_dim = data["embed_dim"]

    # --- Load or create split ---
    split_path = base / "checkpoints" / "split_info.json"
    if split_path.exists():
        with open(split_path) as f:
            split_info = json.load(f)
        keep = split_info.get("keep_indices")
        if keep is not None:
            embeddings = [embeddings[i] for i in keep]
            labels = [labels[i] for i in keep]
            instance_ids = [instance_ids[i] for i in keep]
        train_idx = split_info["train_indices"]
        val_idx = split_info["val_indices"]
        test_idx = split_info["test_indices"]
        print(f"Loaded split from {split_path}")
    else:
        if args.min_confidence > 0:
            keep = [i for i, c in enumerate(confidences) if c >= args.min_confidence]
            embeddings = [embeddings[i] for i in keep]
            labels = [labels[i] for i in keep]
            instance_ids = [instance_ids[i] for i in keep]
        unique = sorted(set(instance_ids))
        rng = random.Random(args.seed)
        rng.shuffle(unique)
        n = len(unique)
        n_train = int(n * 0.7)
        n_val = int(n * 0.15)
        train_set = set(unique[:n_train])
        val_set = set(unique[n_train: n_train + n_val])
        train_idx, val_idx, test_idx = [], [], []
        for i, iid in enumerate(instance_ids):
            if iid in train_set:
                train_idx.append(i)
            elif iid in val_set:
                val_idx.append(i)
            else:
                test_idx.append(i)
        print("Created new split (no split_info.json found)")

    def make_ds(indices):
        return WindowDataset([embeddings[i] for i in indices], [labels[i] for i in indices])

    train_ds = make_ds(train_idx)
    val_ds = make_ds(val_idx)
    test_ds = make_ds(test_idx)

    train_labels = [labels[i] for i in train_idx]
    n_pos = sum(train_labels)
    n_neg = len(train_labels) - n_pos
    pos_weight = torch.tensor([n_neg / max(n_pos, 1)]).to(device)

    total = len(train_idx) + len(val_idx) + len(test_idx)
    print(f"Data: {total} windows  (train={len(train_idx)}, val={len(val_idx)}, test={len(test_idx)})")
    print(f"Train pos/neg: {n_pos}/{n_neg}  pos_weight={pos_weight.item():.3f}")
    print(f"Embed dim: {embed_dim}")

    # --- Run ablation ---
    archs = ["gru_attn", "gru_meanpool", "transformer", "mlp"] if args.arch == "all" else [args.arch]

    results = []
    for arch in archs:
        r = train_one_arch(arch, train_ds, val_ds, test_ds, embed_dim, pos_weight, device, args)
        results.append(r)

    # --- Comparison table ---
    print(f"\n{'=' * 80}")
    print("ARCHITECTURE ABLATION RESULTS")
    print(f"{'=' * 80}")
    header = f"{'Arch':<16} {'Params':>8} {'macro_f1':>9} {'accuracy':>9} {'f1_stag':>9} {'f1_prog':>9} {'time':>7}"
    print(header)
    print("-" * len(header))
    for r in results:
        print(f"{r['arch']:<16} {r['params']:>8,} {r['test_macro_f1']:>9.4f} {r['test_accuracy']:>9.4f} "
              f"{r['test_f1_stag']:>9.4f} {r['test_f1_prog']:>9.4f} {r['train_time_s']:>6.1f}s")

    # --- Save results ---
    out_path = base / "data" / "architecture_ablation_results.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "experiment": "ablation-architecture",
        "results": results,
        "config": {k: v for k, v in vars(args).items()},
    }
    with open(out_path, "w") as f:
        json.dump(payload, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
