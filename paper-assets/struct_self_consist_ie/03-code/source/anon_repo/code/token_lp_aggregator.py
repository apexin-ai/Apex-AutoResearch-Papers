"""Token-level LP Learned Aggregator experiment.

Compares mean-pool baseline vs learned aggregators (Attention, 1D-CNN)
for predicting sample quality from token-level log-probabilities.

Usage:
    python token_lp_aggregator.py --data_path output/exp_029b_scierc_10epoch/samples.jsonl \
        --dataset scierc --output_dir output/token_lp_aggregator
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

import numpy as np
import torch
import torch.nn as nn
from scipy.stats import spearmanr
from sklearn.model_selection import KFold

sys.path.insert(0, str(Path(__file__).resolve().parent))
from evaluation import per_instance_f1


def load_data(data_path, subtask="ner", max_seq_len=512):
    instances = []
    with open(data_path) as f:
        for line in f:
            rec = json.loads(line)
            gold = rec["gold"]
            if not gold.get("entities", []):
                continue

            sample_token_lps = []
            sample_mean_lps = []
            sample_f1s = []

            for s in rec["samples"]:
                token_lps = s.get("token_logprobs")
                if token_lps is None:
                    continue
                arr = np.array(token_lps, dtype=np.float32)
                if len(arr) > max_seq_len:
                    arr = arr[:max_seq_len]
                sample_token_lps.append(arr)
                sample_mean_lps.append(s["mean_logprob"])
                sample_f1s.append(per_instance_f1(s, gold, subtask))

            if len(sample_token_lps) < 2:
                continue

            instances.append({
                "instance_id": rec.get("id", ""),
                "sample_token_lps": sample_token_lps,
                "sample_mean_lps": sample_mean_lps,
                "sample_f1s": sample_f1s,
            })
    return instances


def prepare_tensors(instances, max_seq_len=512):
    all_token_lps = []
    all_lengths = []
    all_mean_lps = []
    all_f1s = []
    all_instance_ids = []

    for idx, inst in enumerate(instances):
        for tlp, mlp, f1 in zip(inst["sample_token_lps"],
                                 inst["sample_mean_lps"],
                                 inst["sample_f1s"]):
            padded = np.zeros(max_seq_len, dtype=np.float32)
            length = min(len(tlp), max_seq_len)
            padded[:length] = tlp[:length]
            all_token_lps.append(padded)
            all_lengths.append(length)
            all_mean_lps.append(mlp)
            all_f1s.append(f1)
            all_instance_ids.append(idx)

    return (
        torch.tensor(np.array(all_token_lps)),
        torch.tensor(all_lengths, dtype=torch.long),
        torch.tensor(all_mean_lps, dtype=torch.float32),
        torch.tensor(all_f1s, dtype=torch.float32),
        np.array(all_instance_ids),
    )


class AttentionAggregator(nn.Module):
    def __init__(self, hidden_dim=32):
        super().__init__()
        self.attn_proj = nn.Linear(1, hidden_dim)
        self.attn_score = nn.Linear(hidden_dim, 1)
        self.predictor = nn.Linear(1, 1)

    def forward(self, token_lps, lengths):
        x = token_lps.unsqueeze(-1)
        mask = torch.arange(x.size(1), device=x.device).unsqueeze(0) < lengths.unsqueeze(1)
        h = torch.tanh(self.attn_proj(x))
        scores = self.attn_score(h).squeeze(-1)
        scores = scores.masked_fill(~mask, -1e9)
        weights = torch.softmax(scores, dim=1)
        pooled = (weights.unsqueeze(-1) * x).sum(dim=1)
        return self.predictor(pooled).squeeze(-1)


class CNNAggregator(nn.Module):
    def __init__(self, channels=16, kernel_size=5):
        super().__init__()
        self.conv1 = nn.Conv1d(1, channels, kernel_size, padding=kernel_size // 2)
        self.conv2 = nn.Conv1d(channels, 1, kernel_size, padding=kernel_size // 2)
        self.predictor = nn.Linear(1, 1)

    def forward(self, token_lps, lengths):
        x = token_lps.unsqueeze(1)
        mask = torch.arange(x.size(2), device=x.device).unsqueeze(0) < lengths.unsqueeze(1)
        h = torch.relu(self.conv1(x))
        h = self.conv2(h).squeeze(1)
        h = h.masked_fill(~mask, 0.0)
        pooled = h.sum(dim=1, keepdim=True) / lengths.unsqueeze(1).float()
        return self.predictor(pooled).squeeze(-1)


def train_model(model, train_lps, train_lengths, train_f1s,
                epochs=100, lr=1e-3, batch_size=256):
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
    criterion = nn.MSELoss()
    n = len(train_f1s)

    for epoch in range(epochs):
        model.train()
        perm = torch.randperm(n)
        epoch_loss = 0.0
        n_batches = 0
        for i in range(0, n, batch_size):
            idx = perm[i:i + batch_size]
            pred = model(train_lps[idx], train_lengths[idx])
            loss = criterion(pred, train_f1s[idx])
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1
    return epoch_loss / max(n_batches, 1)


def evaluate_fold(model, test_lps, test_lengths, test_f1s,
                  test_mean_lps, test_instance_ids):
    model.eval()
    with torch.no_grad():
        pred_scores = model(test_lps, test_lengths).numpy()

    actual_f1s = test_f1s.numpy()
    mean_lps_np = test_mean_lps.numpy()

    rho_model, _ = spearmanr(pred_scores, actual_f1s)
    rho_mean, _ = spearmanr(mean_lps_np, actual_f1s)
    if np.isnan(rho_model): rho_model = 0.0
    if np.isnan(rho_mean): rho_mean = 0.0

    unique_instances = np.unique(test_instance_ids)
    model_sel, mean_sel, oracle_sel = [], [], []

    for inst_idx in unique_instances:
        mask = test_instance_ids == inst_idx
        inst_f1s = actual_f1s[mask]
        model_sel.append(inst_f1s[np.argmax(pred_scores[mask])])
        mean_sel.append(inst_f1s[np.argmax(mean_lps_np[mask])])
        oracle_sel.append(inst_f1s[np.argmax(inst_f1s)])

    return {
        "rho_model": rho_model, "rho_mean": rho_mean,
        "selection_f1_model": np.mean(model_sel),
        "selection_f1_mean": np.mean(mean_sel),
        "selection_f1_oracle": np.mean(oracle_sel),
    }


def run_cv(instances, model_class, model_name, n_folds=5, seeds=(42, 123, 456),
           max_seq_len=512, epochs=100, lr=1e-3, log_file=None):
    token_lps, lengths, mean_lps, f1s, instance_ids = prepare_tensors(instances, max_seq_len)
    n_instances = len(instances)
    all_results = []

    for seed in seeds:
        torch.manual_seed(seed)
        np.random.seed(seed)
        kf = KFold(n_splits=n_folds, shuffle=True, random_state=seed)

        for fold_idx, (train_inst, test_inst) in enumerate(kf.split(np.arange(n_instances))):
            train_set, test_set = set(train_inst), set(test_inst)
            train_mask = np.array([iid in train_set for iid in instance_ids])
            test_mask = np.array([iid in test_set for iid in instance_ids])

            model = model_class()
            final_loss = train_model(model, token_lps[train_mask], lengths[train_mask],
                                     f1s[train_mask], epochs=epochs, lr=lr)
            result = evaluate_fold(model, token_lps[test_mask], lengths[test_mask],
                                   f1s[test_mask], mean_lps[test_mask], instance_ids[test_mask])

            msg = (f"[{model_name}] seed={seed} fold={fold_idx} "
                   f"loss={final_loss:.4f} "
                   f"rho_model={result['rho_model']:.4f} "
                   f"rho_mean={result['rho_mean']:.4f} "
                   f"sel_f1_model={result['selection_f1_model']:.4f} "
                   f"sel_f1_mean={result['selection_f1_mean']:.4f} "
                   f"sel_f1_oracle={result['selection_f1_oracle']:.4f}")
            print(msg)
            if log_file:
                log_file.write(msg + "\n")
                log_file.flush()
            all_results.append(result)

    return all_results


def compute_mean_lp_baseline(instances, n_folds=5, seeds=(42, 123, 456), max_seq_len=512):
    token_lps, lengths, mean_lps, f1s, instance_ids = prepare_tensors(instances, max_seq_len)
    n_instances = len(instances)
    all_results = []

    for seed in seeds:
        np.random.seed(seed)
        kf = KFold(n_splits=n_folds, shuffle=True, random_state=seed)
        for fold_idx, (_, test_inst) in enumerate(kf.split(np.arange(n_instances))):
            test_set = set(test_inst)
            test_mask = np.array([iid in test_set for iid in instance_ids])
            test_f1 = f1s[test_mask].numpy()
            test_mean = mean_lps[test_mask].numpy()
            test_iids = instance_ids[test_mask]

            rho, _ = spearmanr(test_mean, test_f1)
            if np.isnan(rho): rho = 0.0

            mean_sel, oracle_sel = [], []
            for inst_idx in np.unique(test_iids):
                m = test_iids == inst_idx
                mean_sel.append(test_f1[m][np.argmax(test_mean[m])])
                oracle_sel.append(test_f1[m][np.argmax(test_f1[m])])

            all_results.append({"rho": rho, "selection_f1": np.mean(mean_sel),
                                "selection_f1_oracle": np.mean(oracle_sel)})
    return all_results


def compute_random_baseline(instances, n_folds=5, seeds=(42, 123, 456), max_seq_len=512):
    _, _, _, f1s, instance_ids = prepare_tensors(instances, max_seq_len)
    n_instances = len(instances)
    all_results = []

    for seed in seeds:
        np.random.seed(seed)
        kf = KFold(n_splits=n_folds, shuffle=True, random_state=seed)
        for _, (_, test_inst) in enumerate(kf.split(np.arange(n_instances))):
            test_set = set(test_inst)
            test_mask = np.array([iid in test_set for iid in instance_ids])
            test_f1 = f1s[test_mask].numpy()
            test_iids = instance_ids[test_mask]

            random_f1s = []
            for inst_idx in np.unique(test_iids):
                m = test_iids == inst_idx
                random_f1s.append(np.mean(test_f1[m]))
            all_results.append({"selection_f1": np.mean(random_f1s)})
    return all_results


def summarize_results(name, results, key_rho, key_sel, key_oracle=None):
    sels = [r[key_sel] for r in results]
    summary = {"name": name, "selection_f1_mean": float(np.mean(sels)),
               "selection_f1_std": float(np.std(sels))}
    if key_rho:
        rhos = [r[key_rho] for r in results]
        summary["spearman_rho_mean"] = float(np.mean(rhos))
        summary["spearman_rho_std"] = float(np.std(rhos))
    if key_oracle:
        oracles = [r[key_oracle] for r in results]
        summary["oracle_f1_mean"] = float(np.mean(oracles))
        summary["oracle_f1_std"] = float(np.std(oracles))
    return summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", required=True)
    parser.add_argument("--dataset", default="scierc")
    parser.add_argument("--output_dir", default="output/token_lp_aggregator")
    parser.add_argument("--subtask", default="ner")
    parser.add_argument("--max_seq_len", type=int, default=512)
    parser.add_argument("--epochs", type=int, default=150)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--n_folds", type=int, default=5)
    parser.add_argument("--max_instances", type=int, default=0)
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    log_path = os.path.join(args.output_dir, f"training_log_{args.dataset}.txt")
    log_file = open(log_path, "w")

    t0 = time.time()
    instances = load_data(args.data_path, subtask=args.subtask, max_seq_len=args.max_seq_len)

    if args.max_instances > 0 and len(instances) > args.max_instances:
        np.random.seed(42)
        indices = np.random.choice(len(instances), args.max_instances, replace=False)
        instances = [instances[i] for i in sorted(indices)]

    n_samples_total = sum(len(inst["sample_f1s"]) for inst in instances)
    log_file.write(f"Loaded {len(instances)} instances, {n_samples_total} samples\n")
    print(f"Loaded {len(instances)} instances, {n_samples_total} samples")

    seeds = (42, 123, 456)

    print("\n=== Mean LP Baseline ===")
    log_file.write("\n=== Mean LP Baseline ===\n")
    mean_results = compute_mean_lp_baseline(instances, n_folds=args.n_folds, seeds=seeds, max_seq_len=args.max_seq_len)
    for r in mean_results:
        log_file.write(f"  rho={r['rho']:.4f} sel_f1={r['selection_f1']:.4f} oracle={r['selection_f1_oracle']:.4f}\n")
    mean_summary = summarize_results("Mean LP", mean_results, "rho", "selection_f1", "selection_f1_oracle")
    print(f"  Spearman rho: {mean_summary['spearman_rho_mean']:.4f} +/- {mean_summary['spearman_rho_std']:.4f}")
    print(f"  Selection F1: {mean_summary['selection_f1_mean']:.4f} +/- {mean_summary['selection_f1_std']:.4f}")

    random_results = compute_random_baseline(instances, n_folds=args.n_folds, seeds=seeds, max_seq_len=args.max_seq_len)
    random_summary = summarize_results("Random", random_results, None, "selection_f1")

    print("\n=== Attention Aggregator ===")
    log_file.write("\n=== Attention Aggregator ===\n")
    attn_results = run_cv(instances, AttentionAggregator, "Attention",
                          n_folds=args.n_folds, seeds=seeds, max_seq_len=args.max_seq_len,
                          epochs=args.epochs, lr=args.lr, log_file=log_file)
    attn_summary = summarize_results("Attention", attn_results, "rho_model", "selection_f1_model", "selection_f1_oracle")
    print(f"  Spearman rho: {attn_summary['spearman_rho_mean']:.4f} +/- {attn_summary['spearman_rho_std']:.4f}")
    print(f"  Selection F1: {attn_summary['selection_f1_mean']:.4f} +/- {attn_summary['selection_f1_std']:.4f}")

    print("\n=== 1D-CNN Aggregator ===")
    log_file.write("\n=== 1D-CNN Aggregator ===\n")
    cnn_results = run_cv(instances, CNNAggregator, "1D-CNN",
                         n_folds=args.n_folds, seeds=seeds, max_seq_len=args.max_seq_len,
                         epochs=args.epochs, lr=args.lr, log_file=log_file)
    cnn_summary = summarize_results("1D-CNN", cnn_results, "rho_model", "selection_f1_model", "selection_f1_oracle")
    print(f"  Spearman rho: {cnn_summary['spearman_rho_mean']:.4f} +/- {cnn_summary['spearman_rho_std']:.4f}")
    print(f"  Selection F1: {cnn_summary['selection_f1_mean']:.4f} +/- {cnn_summary['selection_f1_std']:.4f}")

    oracle_f1 = mean_summary["oracle_f1_mean"]
    random_f1 = random_summary["selection_f1_mean"]

    def gap_closure(sel_f1):
        if oracle_f1 - random_f1 < 1e-9: return 0.0
        return 100.0 * (sel_f1 - random_f1) / (oracle_f1 - random_f1)

    gc_mean = gap_closure(mean_summary["selection_f1_mean"])
    gc_attn = gap_closure(attn_summary["selection_f1_mean"])
    gc_cnn = gap_closure(cnn_summary["selection_f1_mean"])

    final = {
        "dataset": args.dataset, "data_path": args.data_path,
        "n_instances": len(instances), "n_samples": n_samples_total,
        "n_folds": args.n_folds, "seeds": list(seeds),
        "epochs": args.epochs, "max_seq_len": args.max_seq_len,
        "results": {
            "random": {"selection_f1": random_summary["selection_f1_mean"],
                       "selection_f1_std": random_summary["selection_f1_std"], "gap_closure": 0.0},
            "mean_lp": {"spearman_rho": mean_summary["spearman_rho_mean"],
                        "spearman_rho_std": mean_summary["spearman_rho_std"],
                        "selection_f1": mean_summary["selection_f1_mean"],
                        "selection_f1_std": mean_summary["selection_f1_std"], "gap_closure": gc_mean},
            "attention": {"spearman_rho": attn_summary["spearman_rho_mean"],
                          "spearman_rho_std": attn_summary["spearman_rho_std"],
                          "selection_f1": attn_summary["selection_f1_mean"],
                          "selection_f1_std": attn_summary["selection_f1_std"], "gap_closure": gc_attn},
            "cnn": {"spearman_rho": cnn_summary["spearman_rho_mean"],
                    "spearman_rho_std": cnn_summary["spearman_rho_std"],
                    "selection_f1": cnn_summary["selection_f1_mean"],
                    "selection_f1_std": cnn_summary["selection_f1_std"], "gap_closure": gc_cnn},
            "oracle": {"selection_f1": oracle_f1, "gap_closure": 100.0},
        },
        "elapsed_seconds": time.time() - t0,
    }

    results_path = os.path.join(args.output_dir, f"results_{args.dataset}.json")
    with open(results_path, "w") as f:
        json.dump(final, f, indent=2)

    print("\n" + "=" * 75)
    print(f"{'Aggregator':<20} {'Spearman rho':>14} {'Selection F1':>16} {'Gap Closure':>14}")
    print("-" * 75)
    print(f"{'Random':<20} {'n/a':>14} {random_summary['selection_f1_mean']:>11.4f}+/-{random_summary['selection_f1_std']:.4f} {'0.0%':>14}")
    print(f"{'Mean LP':<20} {mean_summary['spearman_rho_mean']:>9.4f}+/-{mean_summary['spearman_rho_std']:.4f} {mean_summary['selection_f1_mean']:>11.4f}+/-{mean_summary['selection_f1_std']:.4f} {gc_mean:>12.1f}%")
    print(f"{'Attention':<20} {attn_summary['spearman_rho_mean']:>9.4f}+/-{attn_summary['spearman_rho_std']:.4f} {attn_summary['selection_f1_mean']:>11.4f}+/-{attn_summary['selection_f1_std']:.4f} {gc_attn:>12.1f}%")
    print(f"{'1D-CNN':<20} {cnn_summary['spearman_rho_mean']:>9.4f}+/-{cnn_summary['spearman_rho_std']:.4f} {cnn_summary['selection_f1_mean']:>11.4f}+/-{cnn_summary['selection_f1_std']:.4f} {gc_cnn:>12.1f}%")
    print(f"{'Oracle':<20} {'n/a':>14} {oracle_f1:>11.4f}       {'100.0%':>14}")
    print("=" * 75)

    log_file.write(f"\nTotal time: {time.time() - t0:.1f}s\n")
    log_file.close()
    print(f"\nResults saved to {results_path}")
    print(f"Log saved to {log_path}")


if __name__ == "__main__":
    main()
