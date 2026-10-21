#!/usr/bin/env python3
"""Train linear and MLP probes on Few-NERD hidden states to predict sample quality.

Evaluates with 5-fold CV x 3 seeds. Computes Spearman rho, Selection F1,
and Gap Closure % relative to greedy/oracle baselines.

Input: hidden_states.pt, labels.pt, logprobs.pt, subsampled_instances.jsonl
Output: results_goldfiltered.json
"""

import json
import os
import warnings

import numpy as np
import torch
import torch.nn as nn
from scipy.stats import spearmanr
from sklearn.linear_model import Ridge
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler

warnings.filterwarnings("ignore")

DATA_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/hidden_state_probe_fewnerd"
SAMPLES_PATH = os.path.join(DATA_DIR, "subsampled_instances.jsonl")

CV_FOLDS = 5
SEEDS = [42, 123, 456]

MLP_HIDDEN = [256, 64]
MLP_EPOCHS = 100
MLP_LR = 1e-3
MLP_DROPOUT = 0.1
MLP_BATCH = 256


def entity_set(ext):
    return {(e["start"], e["end"], e["type"]) for e in ext.get("entities", [])}


def compute_ner_f1(pred, gold):
    pred_set = entity_set(pred)
    gold_set = entity_set(gold)
    tp = len(pred_set & gold_set)
    if tp == 0:
        return 0.0
    p = tp / (tp + len(pred_set - gold_set))
    r = tp / (tp + len(gold_set - pred_set))
    return 2 * p * r / (p + r)


def load_instance_data():
    with open(SAMPLES_PATH) as f:
        instances = [json.loads(line) for line in f if line.strip()]

    n_samples = len(instances[0]["samples"])
    instance_data = []
    nonempty_indices = []
    for orig_idx, inst in enumerate(instances):
        gold = inst["gold"]
        if len(gold.get("entities", [])) == 0:
            continue
        sample_f1s = [compute_ner_f1(s, gold) for s in inst["samples"]]
        greedy = inst.get("greedy", inst["samples"][0])
        greedy_f1 = compute_ner_f1(greedy, gold)
        oracle_f1 = max(sample_f1s)
        lp_scores = []
        for s in inst["samples"]:
            lp = s.get("mean_logprob")
            if lp is None:
                lp = s.get("cumulative_logprob", -999) / max(s.get("n_tokens", 1), 1)
            lp_scores.append(lp)
        instance_data.append({
            "sample_f1s": sample_f1s,
            "greedy_f1": greedy_f1,
            "oracle_f1": oracle_f1,
            "lp_scores": lp_scores,
        })
        nonempty_indices.append(orig_idx)
    return instance_data, n_samples, nonempty_indices


class MLPProbe(nn.Module):
    def __init__(self, input_dim, hidden_dims, dropout=0.1):
        super().__init__()
        layers = []
        prev = input_dim
        for h in hidden_dims:
            layers.extend([nn.Linear(prev, h), nn.ReLU(), nn.Dropout(dropout)])
            prev = h
        layers.append(nn.Linear(prev, 1))
        self.net = nn.Sequential(*layers)

    def forward(self, x):
        return self.net(x).squeeze(-1)


def train_mlp(X_train, y_train, X_val, y_val, seed):
    torch.manual_seed(seed)
    device = "cpu"
    model = MLPProbe(X_train.shape[1], MLP_HIDDEN, MLP_DROPOUT).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=MLP_LR, weight_decay=1e-4)

    X_tr = torch.tensor(X_train, dtype=torch.float32, device=device)
    y_tr = torch.tensor(y_train, dtype=torch.float32, device=device)
    X_v = torch.tensor(X_val, dtype=torch.float32, device=device)

    best_val_loss = float("inf")
    patience_counter = 0
    best_state = None

    for epoch in range(MLP_EPOCHS):
        model.train()
        perm = torch.randperm(len(X_tr))
        total_loss = 0.0
        n_batches = 0
        for start in range(0, len(X_tr), MLP_BATCH):
            idx = perm[start:start + MLP_BATCH]
            pred = model(X_tr[idx])
            loss = nn.functional.mse_loss(pred, y_tr[idx])
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
            n_batches += 1

        model.eval()
        with torch.no_grad():
            val_pred = model(X_v)
            val_loss = nn.functional.mse_loss(val_pred, torch.tensor(y_val, dtype=torch.float32, device=device)).item()

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= 15:
                break

    if best_state is not None:
        model.load_state_dict(best_state)
    model.eval()
    with torch.no_grad():
        preds = model(X_v).cpu().numpy()
    return preds


def compute_selection_f1(instance_data, n_samples, score_matrix):
    sel_f1s = []
    greedy_f1s = []
    oracle_f1s = []
    random_f1s = []

    for i, idata in enumerate(instance_data):
        scores = score_matrix[i]
        chosen = int(np.argmax(scores))
        sel_f1s.append(idata["sample_f1s"][chosen])
        greedy_f1s.append(idata["greedy_f1"])
        oracle_f1s.append(idata["oracle_f1"])
        random_f1s.append(np.mean(idata["sample_f1s"]))

    return (
        np.mean(sel_f1s),
        np.mean(greedy_f1s),
        np.mean(oracle_f1s),
        np.mean(random_f1s),
    )


def run_cv(hidden_states, labels, instance_data, n_samples, method="linear"):
    n_instances = len(instance_data)
    all_rhos = []
    all_sel_f1s = []
    all_greedy_f1s = []
    all_oracle_f1s = []

    for seed in SEEDS:
        kf = KFold(n_splits=CV_FOLDS, shuffle=True, random_state=seed)
        inst_indices = np.arange(n_instances)

        fold_score_matrix = np.zeros((n_instances, n_samples))

        for fold, (train_inst, val_inst) in enumerate(kf.split(inst_indices)):
            train_rows = []
            val_rows = []
            for idx in train_inst:
                for s in range(n_samples):
                    train_rows.append(idx * n_samples + s)
            for idx in val_inst:
                for s in range(n_samples):
                    val_rows.append(idx * n_samples + s)

            X_train = hidden_states[train_rows]
            y_train = labels[train_rows]
            X_val = hidden_states[val_rows]
            y_val = labels[val_rows]

            if method == "linear":
                scaler = StandardScaler()
                X_train_s = scaler.fit_transform(X_train)
                X_val_s = scaler.transform(X_val)
                reg = Ridge(alpha=1.0)
                reg.fit(X_train_s, y_train)
                preds = reg.predict(X_val_s)
            elif method == "mlp":
                scaler = StandardScaler()
                X_train_s = scaler.fit_transform(X_train)
                X_val_s = scaler.transform(X_val)
                preds = train_mlp(X_train_s, y_train, X_val_s, y_val, seed * 100 + fold)
            else:
                raise ValueError(f"Unknown method: {method}")

            for k, idx in enumerate(val_inst):
                for s in range(n_samples):
                    fold_score_matrix[idx, s] = preds[k * n_samples + s]

        rho_val, _ = spearmanr(
            fold_score_matrix.flatten(),
            np.array([f1 for idata in instance_data for f1 in idata["sample_f1s"]])
        )
        sel_f1, greedy_f1, oracle_f1, _ = compute_selection_f1(
            instance_data, n_samples, fold_score_matrix
        )

        all_rhos.append(rho_val)
        all_sel_f1s.append(sel_f1)
        all_greedy_f1s.append(greedy_f1)
        all_oracle_f1s.append(oracle_f1)

    greedy_mean = np.mean(all_greedy_f1s)
    oracle_mean = np.mean(all_oracle_f1s)
    sel_mean = np.mean(all_sel_f1s)
    gap = oracle_mean - greedy_mean
    gap_closure = ((sel_mean - greedy_mean) / gap * 100) if gap > 0 else 0.0

    return {
        "rho_mean": float(np.mean(all_rhos)),
        "rho_std": float(np.std(all_rhos, ddof=1)),
        "rho_per_seed": [float(r) for r in all_rhos],
        "sel_f1_mean": float(sel_mean),
        "sel_f1_std": float(np.std(all_sel_f1s, ddof=1)),
        "sel_f1_per_seed": [float(f) for f in all_sel_f1s],
        "greedy_f1_mean": float(greedy_mean),
        "oracle_f1_mean": float(oracle_mean),
        "gap_closure": float(gap_closure),
    }


def compute_lp_baseline(instance_data, n_samples):
    score_matrix = np.array([idata["lp_scores"] for idata in instance_data])
    flat_scores = score_matrix.flatten()
    flat_f1s = np.array([f1 for idata in instance_data for f1 in idata["sample_f1s"]])
    rho, _ = spearmanr(flat_scores, flat_f1s)

    sel_f1, greedy_f1, oracle_f1, random_f1 = compute_selection_f1(
        instance_data, n_samples, score_matrix
    )
    gap = oracle_f1 - greedy_f1
    gap_closure = ((sel_f1 - greedy_f1) / gap * 100) if gap > 0 else 0.0

    return {
        "rho": float(rho),
        "sel_f1": float(sel_f1),
        "greedy_f1": float(greedy_f1),
        "oracle_f1": float(oracle_f1),
        "random_f1": float(random_f1),
        "gap_closure": float(gap_closure),
    }


def main():
    print("Loading hidden states and labels...")
    hidden_states = torch.load(os.path.join(DATA_DIR, "hidden_states.pt"), weights_only=True).numpy()
    labels = torch.load(os.path.join(DATA_DIR, "labels.pt"), weights_only=True).numpy()
    logprobs = torch.load(os.path.join(DATA_DIR, "logprobs.pt"), weights_only=True).numpy()

    print(f"  hidden_states: {hidden_states.shape}")
    print(f"  labels: {labels.shape}")

    print("Loading instance data for selection F1...")
    instance_data, n_samples, nonempty_indices = load_instance_data()
    n_instances = len(instance_data)
    print(f"  {n_instances} instances with non-empty gold, {n_samples} samples each")

    rows = []
    for idx in nonempty_indices:
        for s in range(n_samples):
            rows.append(idx * n_samples + s)
    rows = np.array(rows)
    hs_filtered = hidden_states[rows]
    labels_filtered = labels[rows]

    print("\nComputing LP baseline...")
    lp_baseline = compute_lp_baseline(instance_data, n_samples)
    print(f"  LP: rho={lp_baseline['rho']:.4f}, sel_f1={lp_baseline['sel_f1']:.4f}, "
          f"gap_closure={lp_baseline['gap_closure']:.1f}%")

    print("\nTraining Linear Probe (Ridge, 5-fold CV x 3 seeds)...")
    linear_results = run_cv(hs_filtered, labels_filtered, instance_data, n_samples, method="linear")
    print(f"  Linear: rho={linear_results['rho_mean']:.4f}+/-{linear_results['rho_std']:.4f}, "
          f"sel_f1={linear_results['sel_f1_mean']:.4f}, gap_closure={linear_results['gap_closure']:.1f}%")

    print("\nTraining MLP Probe (5-fold CV x 3 seeds)...")
    mlp_results = run_cv(hs_filtered, labels_filtered, instance_data, n_samples, method="mlp")
    print(f"  MLP: rho={mlp_results['rho_mean']:.4f}+/-{mlp_results['rho_std']:.4f}, "
          f"sel_f1={mlp_results['sel_f1_mean']:.4f}, gap_closure={mlp_results['gap_closure']:.1f}%")

    results = {
        "dataset": "Few-NERD",
        "n_instances": n_instances,
        "n_samples": n_samples,
        "hidden_dim": int(hidden_states.shape[1]),
        "cv_folds": CV_FOLDS,
        "seeds": SEEDS,
        "gold_filtered": True,
        "probes": {
            "linear": linear_results,
            "mlp": mlp_results,
        },
        "baselines": {
            "lp": lp_baseline,
        },
    }

    output_path = os.path.join(DATA_DIR, "results_goldfiltered.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {output_path}")

    print("\n" + "=" * 75)
    print(f"{'Method':<20} {'Dim':>5} {'Spearman rho':>14} {'Selection F1':>14} {'Gap Closure':>13}")
    print("-" * 75)
    print(f"{'LP (mean pool)':<20} {'1':>5} {lp_baseline['rho']:>14.4f} {lp_baseline['sel_f1']:>14.4f} {lp_baseline['gap_closure']:>12.1f}%")
    print(f"{'Hidden Linear':<20} {'4096':>5} {linear_results['rho_mean']:>10.4f}+/-{linear_results['rho_std']:.4f} {linear_results['sel_f1_mean']:>14.4f} {linear_results['gap_closure']:>12.1f}%")
    print(f"{'Hidden MLP':<20} {'4096':>5} {mlp_results['rho_mean']:>10.4f}+/-{mlp_results['rho_std']:.4f} {mlp_results['sel_f1_mean']:>14.4f} {mlp_results['gap_closure']:>12.1f}%")
    print(f"{'Oracle':<20} {'--':>5} {'--':>14} {lp_baseline['oracle_f1']:>14.4f} {'100.0':>12}%")
    print("=" * 75)


if __name__ == "__main__":
    main()
