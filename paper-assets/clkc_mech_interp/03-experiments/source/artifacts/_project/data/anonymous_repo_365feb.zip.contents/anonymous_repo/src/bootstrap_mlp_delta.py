"""Bootstrap MLP vs Linear probe delta for statistical validation."""

import argparse
import json
import time
import warnings
import numpy as np
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import balanced_accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

warnings.filterwarnings("ignore")


class MLPProbe(nn.Module):
    def __init__(self, input_dim, hidden_dim=256, dropout=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim), nn.ReLU(), nn.Dropout(dropout),
            nn.Linear(hidden_dim, 1),
        )
    def forward(self, x):
        return self.net(x).squeeze(-1)


def train_mlp_once(X_train, y_train, X_test, y_test, seed=42, epochs=50, lr=1e-3, bs=64):
    torch.manual_seed(seed)
    X_tr, X_val, y_tr, y_val = train_test_split(
        X_train, y_train, test_size=0.15, stratify=y_train, random_state=seed)
    X_tr_t = torch.tensor(X_tr, dtype=torch.float32)
    y_tr_t = torch.tensor(y_tr, dtype=torch.float32)
    X_val_t = torch.tensor(X_val, dtype=torch.float32)
    y_val_t = torch.tensor(y_val, dtype=torch.float32)
    X_test_t = torch.tensor(X_test, dtype=torch.float32)

    n_pos = y_tr_t.sum().item()
    n_neg = len(y_tr_t) - n_pos
    pos_weight = torch.tensor([n_neg / max(n_pos, 1)])

    model = MLPProbe(X_tr_t.shape[1])
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)
    loader = DataLoader(TensorDataset(X_tr_t, y_tr_t), batch_size=bs, shuffle=True)
    best_val_loss = float("inf")
    patience_counter = 0
    best_state = None

    for _ in range(epochs):
        model.train()
        for xb, yb in loader:
            optimizer.zero_grad()
            criterion(model(xb), yb).backward()
            optimizer.step()
        model.eval()
        with torch.no_grad():
            vl = criterion(model(X_val_t), y_val_t).item()
        if vl < best_val_loss:
            best_val_loss = vl
            best_state = {k: v.clone() for k, v in model.state_dict().items()}
            patience_counter = 0
        else:
            patience_counter += 1
            if patience_counter >= 10:
                break

    if best_state:
        model.load_state_dict(best_state)
    model.eval()
    with torch.no_grad():
        preds = (model(X_test_t) > 0).numpy().astype(int)
    return balanced_accuracy_score(y_test, preds)


def load_split(path, layer):
    d = torch.load(path, map_location="cpu", weights_only=True)
    act = d["activations"][:, layer, :]
    if act.dtype == torch.bfloat16:
        act = act.float()
    act = act.numpy()
    labels = d["labels"].numpy()
    n_train = d["split_sizes"]["train"]
    return act[:n_train], labels[:n_train], act[n_train:], labels[n_train:]


def run_bootstrap(train_path, test_path, layer, n_bootstrap=1000, seed=42):
    train_all, train_labels, _, _ = load_split(train_path, layer)
    _, _, test_data, test_labels = load_split(test_path, layer)
    print(f"  Train: {train_all.shape}, Test: {test_data.shape}")

    rng = np.random.RandomState(seed)
    deltas, linear_accs, mlp_accs = [], [], []

    for i in range(n_bootstrap):
        idx = rng.choice(len(train_all), size=len(train_all), replace=True)
        X_boot = train_all[idx]
        y_boot = train_labels[idx]
        if len(np.unique(y_boot)) < 2:
            continue

        scaler = StandardScaler()
        X_boot_s = scaler.fit_transform(X_boot)
        test_s = scaler.transform(test_data)

        lr = LogisticRegression(max_iter=2000, class_weight="balanced", solver="lbfgs")
        lr.fit(X_boot_s, y_boot)
        l_acc = balanced_accuracy_score(test_labels, lr.predict(test_s))
        m_acc = train_mlp_once(X_boot_s, y_boot, test_s, test_labels, seed=seed+i)

        deltas.append(m_acc - l_acc)
        linear_accs.append(l_acc)
        mlp_accs.append(m_acc)

        if (i + 1) % 100 == 0:
            print(f"  [{i+1}/{n_bootstrap}] delta={np.mean(deltas):.4f}", flush=True)

    deltas = np.array(deltas)
    return {
        "mean_delta": round(float(np.mean(deltas)), 6),
        "ci_lower": round(float(np.percentile(deltas, 2.5)), 6),
        "ci_upper": round(float(np.percentile(deltas, 97.5)), 6),
        "excludes_zero": bool(np.percentile(deltas, 2.5) > 0 or np.percentile(deltas, 97.5) < 0),
        "mean_linear_acc": round(float(np.mean(linear_accs)), 6),
        "mean_mlp_acc": round(float(np.mean(mlp_accs)), 6),
        "n_valid_boots": len(deltas),
        "layer": layer,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--conditions", type=str, required=True,
                        help='JSON: [{"name": "...", "train_path": "...", "test_path": "...", "layer": N}]')
    parser.add_argument("--n_bootstrap", type=int, default=1000)
    parser.add_argument("--output", type=str, default="results/mlp_bootstrap_results.json")
    args = parser.parse_args()

    conditions = json.loads(args.conditions)
    all_results = {}

    for cfg in conditions:
        name = cfg["name"]
        print(f"\n{'='*60}")
        print(f"  {name} (layer {cfg['layer']})")
        print(f"{'='*60}")
        all_results[name] = run_bootstrap(
            cfg["train_path"], cfg["test_path"], cfg["layer"],
            n_bootstrap=args.n_bootstrap,
        )

    from pathlib import Path
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved to {args.output}")

    for name, r in all_results.items():
        tag = "***SIG***" if r["excludes_zero"] else "   n.s.  "
        print(f"  {tag} {name}: delta={r['mean_delta']:+.4f} [{r['ci_lower']:+.4f}, {r['ci_upper']:+.4f}]")


if __name__ == "__main__":
    main()
