"""MLP probe for knowledge conflict detection.

1-hidden-layer MLP (256, ReLU, dropout=0.1) vs linear probe comparison.
"""

import argparse
import json
from pathlib import Path

import numpy as np
import torch
from torch import nn
from torch.utils.data import TensorDataset, DataLoader
from sklearn.metrics import balanced_accuracy_score, f1_score, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


class MLPProbe(nn.Module):
    def __init__(self, input_dim, hidden_dim=256, dropout=0.1):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, 1),
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)


def load_activations(path: str) -> dict:
    data = torch.load(path, map_location="cpu", weights_only=True)
    n_train = data["split_sizes"]["train"]
    acts = data["activations"]
    if acts.dtype == torch.bfloat16:
        acts = acts.float()
    return {
        "train_X": acts[:n_train],
        "train_y": data["labels"][:n_train],
        "test_X": acts[n_train:],
        "test_y": data["labels"][n_train:],
    }


def train_mlp(
    train_X: np.ndarray,
    train_y: np.ndarray,
    test_X: np.ndarray,
    test_y: np.ndarray,
    device: str = "cpu",
    epochs: int = 50,
    lr: float = 1e-3,
    batch_size: int = 64,
    seed: int = 42,
) -> dict:
    torch.manual_seed(seed)
    scaler = StandardScaler()
    train_X = scaler.fit_transform(train_X)
    test_X = scaler.transform(test_X)

    X_tr, X_val, y_tr, y_val = train_test_split(
        train_X, train_y, test_size=0.15, stratify=train_y, random_state=seed
    )

    X_tr_t = torch.tensor(X_tr, dtype=torch.float32)
    y_tr_t = torch.tensor(y_tr, dtype=torch.float32)
    X_val_t = torch.tensor(X_val, dtype=torch.float32).to(device)
    y_val_t = torch.tensor(y_val, dtype=torch.float32).to(device)
    X_test_t = torch.tensor(test_X, dtype=torch.float32).to(device)

    n_pos = y_tr_t.sum().item()
    n_neg = len(y_tr_t) - n_pos
    pos_weight = torch.tensor([n_neg / max(n_pos, 1)], device=device)

    input_dim = X_tr_t.shape[1]
    model = MLPProbe(input_dim).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr, weight_decay=1e-4)
    criterion = nn.BCEWithLogitsLoss(pos_weight=pos_weight)

    train_ds = TensorDataset(X_tr_t, y_tr_t)
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)

    best_val_loss = float("inf")
    patience_counter = 0
    best_state = None

    for epoch in range(epochs):
        model.train()
        for xb, yb in train_loader:
            xb, yb = xb.to(device), yb.to(device)
            optimizer.zero_grad()
            loss = criterion(model(xb), yb)
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_loss = criterion(model(X_val_t), y_val_t).item()

        if val_loss < best_val_loss:
            best_val_loss = val_loss
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
        preds = (model(X_test_t) > 0).cpu().numpy().astype(int)

    return {
        "accuracy": round(float(accuracy_score(test_y, preds)), 4),
        "balanced_accuracy": round(float(balanced_accuracy_score(test_y, preds)), 4),
        "f1": round(float(f1_score(test_y, preds)), 4),
    }


def run_direction(train_data, test_data, num_layers, direction_name, device="cpu"):
    train_y = train_data["train_y"].numpy()
    test_y = test_data["test_y"].numpy()
    results = []
    best_bal_acc, best_layer = 0.0, 0

    for layer in range(num_layers):
        train_X = train_data["train_X"][:, layer, :].numpy()
        test_X = test_data["test_X"][:, layer, :].numpy()
        metrics = train_mlp(train_X, train_y, test_X, test_y, device=device)
        metrics["layer"] = layer
        results.append(metrics)

        if metrics["balanced_accuracy"] > best_bal_acc:
            best_bal_acc = metrics["balanced_accuracy"]
            best_layer = layer

        print(f"    Layer {layer:2d}: acc={metrics['accuracy']:.4f}  "
              f"bal_acc={metrics['balanced_accuracy']:.4f}  f1={metrics['f1']:.4f}")

    print(f"  Best: layer {best_layer}, bal_acc={best_bal_acc:.4f}")
    return results


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--activation_dir", type=str, required=True)
    parser.add_argument("--output_dir", type=str, required=True)
    parser.add_argument("--device", type=str, default="cpu")
    args = parser.parse_args()

    en_path = Path(args.activation_dir) / "en_activations.pt"
    zh_path = Path(args.activation_dir) / "zh_activations.pt"
    has_en = en_path.exists()
    has_zh = zh_path.exists()

    if not has_en and not has_zh:
        raise FileNotFoundError(f"No activation files found in {args.activation_dir}")

    en_data = load_activations(str(en_path)) if has_en else None
    zh_data = load_activations(str(zh_path)) if has_zh else None

    num_layers = en_data["train_X"].shape[1] if has_en else zh_data["train_X"].shape[1]
    print(f"Number of layers: {num_layers}")

    all_results = {}
    if has_en:
        print("\n[EN→EN] Training MLP probes...")
        all_results["EN→EN"] = run_direction(en_data, en_data, num_layers, "EN→EN", args.device)
    if has_zh:
        print("\n[ZH→ZH] Training MLP probes...")
        all_results["ZH→ZH"] = run_direction(zh_data, zh_data, num_layers, "ZH→ZH", args.device)
    if has_en and has_zh:
        print("\n[EN→ZH] Training MLP probes...")
        all_results["EN→ZH"] = run_direction(en_data, zh_data, num_layers, "EN→ZH", args.device)
        print("\n[ZH→EN] Training MLP probes...")
        all_results["ZH→EN"] = run_direction(zh_data, en_data, num_layers, "ZH→EN", args.device)

    summary = {}
    for direction, results in all_results.items():
        best = max(results, key=lambda r: r["balanced_accuracy"])
        summary[direction] = {
            "best_layer": best["layer"],
            "best_balanced_accuracy": best["balanced_accuracy"],
            "best_f1": best["f1"],
        }

    output = {"per_layer": all_results, "summary": summary, "num_layers": num_layers}
    Path(args.output_dir).mkdir(parents=True, exist_ok=True)
    json_path = Path(args.output_dir) / "mlp_probe_results.json"
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nSaved results to {json_path}")


if __name__ == "__main__":
    main()
