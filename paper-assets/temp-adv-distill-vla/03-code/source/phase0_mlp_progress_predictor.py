#!/usr/bin/env python3
"""
phase0_mlp_progress_predictor.py — Gate 1 Fallback (b): MLP progress predictor.

If Gate 1(a) raw cos_sim Spearman rho fails, train a 3-layer MLP per layer to
predict normalized timestep t/T from frozen VLA features. Gate passes if any
layer achieves test R² > 0.8.

Supports two modes:
  1. --features_dir: load pre-extracted .pt feature files (from phase0_feature_validation.py)
  2. Otherwise: load the VLA model and extract features from scratch

Deps: torch, transformers, scipy, matplotlib, h5py, numpy, Pillow, sklearn
"""

import argparse
import glob
import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.metrics import r2_score, mean_absolute_error
from torch.utils.data import DataLoader, TensorDataset


def parse_args():
    p = argparse.ArgumentParser(
        description="Gate 1 Fallback (b): MLP progress predictor on frozen VLA features"
    )
    p.add_argument("--model_path", type=str,
                   default="/root/temp-adv-distill-vla/models/openvla-7b-finetuned-libero-spatial")
    p.add_argument("--data_path", type=str,
                   default="/root/temp-adv-distill-vla/data/libero")
    p.add_argument("--features_dir", type=str, default=None,
                   help="Directory with pre-extracted feature .pt files. "
                        "If not provided, features are extracted from the model.")
    p.add_argument("--output_dir", type=str,
                   default="/root/temp-adv-distill-vla/artifacts")
    p.add_argument("--num_trajectories", type=int, default=50)
    p.add_argument("--epochs", type=int, default=100)
    p.add_argument("--lr", type=float, default=1e-3)
    p.add_argument("--device", type=str, default="cuda:1")
    p.add_argument("--layers", type=str, default="15,22,31",
                   help="Comma-separated layer indices (used when extracting features)")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--patience", type=int, default=10,
                   help="Early stopping patience (epochs)")
    p.add_argument("--batch_size", type=int, default=256)
    p.add_argument("--r2_threshold", type=float, default=0.8,
                   help="R² threshold for Gate 1(b) pass")
    return p.parse_args()


# ---------------------------------------------------------------------------
# MLP architecture
# ---------------------------------------------------------------------------

class ProgressMLP(nn.Module):
    """3-layer MLP: φ(s_t) -> predicted t/T."""

    def __init__(self, input_dim=4096):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, 512),
            nn.ReLU(),
            nn.Linear(512, 128),
            nn.ReLU(),
            nn.Linear(128, 1),
            nn.Sigmoid(),
        )

    def forward(self, x):
        return self.net(x).squeeze(-1)


# ---------------------------------------------------------------------------
# Feature extraction (reused from phase0_feature_validation.py logic)
# ---------------------------------------------------------------------------

def load_model(model_path, device):
    """Load OpenVLA model frozen in eval mode."""
    from transformers import AutoModelForVision2Seq, AutoProcessor

    print(f"[load_model] Loading processor from {model_path}")
    processor = AutoProcessor.from_pretrained(model_path, trust_remote_code=True)

    print(f"[load_model] Loading model from {model_path}")
    model = AutoModelForVision2Seq.from_pretrained(
        model_path,
        torch_dtype=torch.bfloat16,
        low_cpu_mem_usage=True,
        trust_remote_code=True,
    ).to(device)
    model.eval()
    for param in model.parameters():
        param.requires_grad = False

    print(f"[load_model] Model loaded on {device}")
    return model, processor


def resolve_llm_layers(model):
    """Locate the LLM decoder layer list."""
    if hasattr(model, "language_model"):
        lm = model.language_model
        if hasattr(lm, "model") and hasattr(lm.model, "layers"):
            return lm.model.layers
        if hasattr(lm, "layers"):
            return lm.layers
    if hasattr(model, "model") and hasattr(model.model, "layers"):
        return model.model.layers
    for name, child in model.named_modules():
        if name.endswith(".layers") and hasattr(child, "__len__"):
            return child
    raise RuntimeError(f"Cannot locate LLM decoder layers in {type(model).__name__}")


def register_hooks(model, layer_indices):
    """Register forward hooks on target LLM layers."""
    layers = resolve_llm_layers(model)
    num_layers = len(layers)
    print(f"[hooks] LLM backbone: {num_layers} decoder layers")

    resolved = []
    for idx in layer_indices:
        actual = idx if idx >= 0 else num_layers + idx
        assert 0 <= actual < num_layers, f"Layer {idx} -> {actual} out of range [0, {num_layers})"
        resolved.append(actual)

    feature_dict = {}
    handles = []

    def make_hook(name):
        def hook_fn(module, input, output):
            if isinstance(output, tuple):
                hidden = output[0]
            else:
                hidden = output
            feature_dict[name] = hidden.detach()
        return hook_fn

    for actual in resolved:
        name = f"layer_{actual}"
        h = layers[actual].register_forward_hook(make_hook(name))
        handles.append(h)
        print(f"  Registered hook on layer {actual} -> '{name}'")

    return handles, feature_dict, resolved


def load_libero_trajectories(data_path, num_trajectories):
    """Load LIBERO HDF5 trajectories."""
    import h5py
    from PIL import Image

    patterns = ["**/*.hdf5", "**/*.h5", "*.hdf5", "*.h5"]
    hdf5_files = []
    for pat in patterns:
        hdf5_files = sorted(glob.glob(os.path.join(data_path, pat), recursive=True))
        if hdf5_files:
            break
    if not hdf5_files:
        raise FileNotFoundError(f"No HDF5 files found in {data_path}")

    print(f"[data] Found {len(hdf5_files)} HDF5 file(s) in {data_path}")
    trajectories = []

    for fpath in hdf5_files:
        if len(trajectories) >= num_trajectories:
            break
        try:
            with h5py.File(fpath, "r") as f:
                data_grp = f["data"] if "data" in f else f

                task = _extract_task_description(f, data_grp, fpath)

                demo_keys = sorted(
                    [k for k in data_grp.keys() if k.startswith("demo")],
                    key=lambda x: int(x.split("_")[-1])
                )
                for dk in demo_keys:
                    if len(trajectories) >= num_trajectories:
                        break
                    demo = data_grp[dk]
                    obs = demo["obs"] if "obs" in demo else demo

                    img_key = _find_image_key(obs)
                    if img_key is None:
                        continue

                    images = obs[img_key][:]
                    if images.shape[0] < 5:
                        continue

                    trajectories.append({
                        "images": images,
                        "task": task,
                        "source": f"{Path(fpath).name}:{dk}",
                    })
        except Exception as e:
            print(f"  Warning: failed to read {fpath}: {e}")
            continue

    print(f"[data] Loaded {len(trajectories)} trajectories")
    return trajectories


def _extract_task_description(f, data_grp, fpath):
    for attr_src in [f.attrs, data_grp.attrs]:
        for key in ["problem_info", "task", "language_instruction",
                     "task_description", "instruction"]:
            if key in attr_src:
                val = attr_src[key]
                if isinstance(val, bytes):
                    val = val.decode("utf-8")
                if isinstance(val, str) and val.strip():
                    return val.strip()
    stem = Path(fpath).stem
    parts = stem.split("_")
    if len(parts) > 2 and parts[0] == "LIBERO":
        return " ".join(parts[2:]).replace("demo", "").strip()
    return " ".join(parts).replace("_", " ").strip()


def _find_image_key(obs_group):
    candidates = [
        "agentview_rgb", "agentview_image", "image", "rgb",
        "pixels", "eye_in_hand_rgb", "front_rgb",
    ]
    for c in candidates:
        if c in obs_group:
            return c
    for k in obs_group.keys():
        try:
            ds = obs_group[k]
            if hasattr(ds, "shape") and len(ds.shape) == 4 and ds.shape[-1] == 3:
                return k
        except Exception:
            pass
    return None


def extract_features(model, processor, trajectories, layer_features, device):
    """Extract per-timestep features for all trajectories.

    Returns list of dicts, each {layer_name: Tensor(T, hidden_dim)}.
    """
    from PIL import Image as PILImage

    features_per_traj = []
    for i, traj in enumerate(trajectories):
        images = traj["images"]
        task = traj["task"]
        T = len(images)
        prompt = f"In: What action should the robot take to {task}?\nOut:"

        print(f"  [{i+1}/{len(trajectories)}] {traj['source']} ({T} steps)")

        all_features = {k: [] for k in layer_features}

        for t in range(T):
            img = PILImage.fromarray(images[t])
            layer_features.clear()

            inputs = processor(prompt, img).to(device, dtype=torch.bfloat16)
            with torch.no_grad():
                try:
                    _ = model(**inputs)
                except Exception:
                    _ = model(
                        input_ids=inputs.get("input_ids"),
                        attention_mask=inputs.get("attention_mask"),
                        pixel_values=inputs.get("pixel_values"),
                    )

            for k, v in layer_features.items():
                pooled = v.mean(dim=1).squeeze(0).float().cpu()
                all_features[k].append(pooled)

        features_per_traj.append({k: torch.stack(v) for k, v in all_features.items()})

    return features_per_traj


# ---------------------------------------------------------------------------
# Data preparation — split by trajectory, not by timestep
# ---------------------------------------------------------------------------

def prepare_data(features_per_traj, layer_names, seed=42):
    """Build train/test splits per layer.

    Data is split by trajectory (80/20), not by timestep, to avoid data
    leakage from temporally correlated frames within the same trajectory.

    Returns dict {layer_name: (X_train, y_train, X_test, y_test, traj_indices_test)}
    """
    rng = np.random.RandomState(seed)
    n_traj = len(features_per_traj)
    indices = rng.permutation(n_traj)
    n_train = int(0.8 * n_traj)
    train_idx = set(indices[:n_train].tolist())
    test_idx = set(indices[n_train:].tolist())

    print(f"[data split] {len(train_idx)} train / {len(test_idx)} test trajectories "
          f"(by trajectory, not timestep)")

    result = {}
    for layer_name in layer_names:
        train_X, train_y = [], []
        test_X, test_y = [], []
        test_traj_ids = []

        for i, traj_feats in enumerate(features_per_traj):
            feats = traj_feats[layer_name]  # (T, D)
            T = feats.shape[0]
            targets = torch.arange(T, dtype=torch.float32) / max(T - 1, 1)  # t/T in [0, 1]

            if i in train_idx:
                train_X.append(feats)
                train_y.append(targets)
            else:
                test_X.append(feats)
                test_y.append(targets)
                test_traj_ids.extend([i] * T)

        result[layer_name] = (
            torch.cat(train_X), torch.cat(train_y),
            torch.cat(test_X), torch.cat(test_y),
            test_traj_ids,
        )

    first_layer = layer_names[0]
    print(f"  Train samples: {result[first_layer][0].shape[0]}, "
          f"Test samples: {result[first_layer][2].shape[0]}")

    return result


# ---------------------------------------------------------------------------
# Training
# ---------------------------------------------------------------------------

def train_mlp(X_train, y_train, X_test, y_test, *,
              input_dim, epochs, lr, patience, batch_size, device):
    """Train a ProgressMLP with early stopping.

    Returns (model, train_losses, best_epoch).
    """
    model = ProgressMLP(input_dim=input_dim).to(device)
    optimizer = optim.AdamW(model.parameters(), lr=lr)
    criterion = nn.MSELoss()

    train_ds = TensorDataset(X_train.to(device), y_train.to(device))
    train_loader = DataLoader(train_ds, batch_size=batch_size, shuffle=True)

    X_val = X_test.to(device)
    y_val = y_test.to(device)

    best_val_loss = float("inf")
    best_state = None
    best_epoch = 0
    epochs_no_improve = 0
    train_losses = []

    for epoch in range(1, epochs + 1):
        model.train()
        epoch_loss = 0.0
        n_batches = 0
        for xb, yb in train_loader:
            pred = model(xb)
            loss = criterion(pred, yb)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            epoch_loss += loss.item()
            n_batches += 1

        avg_train_loss = epoch_loss / n_batches
        train_losses.append(avg_train_loss)

        model.eval()
        with torch.no_grad():
            val_pred = model(X_val)
            val_loss = criterion(val_pred, y_val).item()

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            best_epoch = epoch
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        if epoch % 10 == 0 or epoch == 1:
            print(f"    Epoch {epoch:3d}: train_loss={avg_train_loss:.6f}  "
                  f"val_loss={val_loss:.6f}  best_epoch={best_epoch}")

        if epochs_no_improve >= patience:
            print(f"    Early stopping at epoch {epoch} (patience={patience}, best={best_epoch})")
            break

    model.load_state_dict(best_state)
    model.to(device)
    return model, train_losses, best_epoch


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------

def evaluate_mlp(model, X_test, y_test, device):
    """Compute R² and MAE on test set."""
    model.eval()
    with torch.no_grad():
        preds = model(X_test.to(device)).cpu().numpy()
    targets = y_test.numpy()

    r2 = r2_score(targets, preds)
    mae = mean_absolute_error(targets, preds)
    return r2, mae, preds, targets


# ---------------------------------------------------------------------------
# Visualization
# ---------------------------------------------------------------------------

def plot_predictions(preds, targets, layer_name, r2, mae, output_dir):
    """Scatter plot: predicted t/T vs actual t/T."""
    fig, ax = plt.subplots(1, 1, figsize=(6, 6))
    ax.scatter(targets, preds, alpha=0.15, s=8, c="steelblue", edgecolors="none")
    ax.plot([0, 1], [0, 1], "r--", alpha=0.7, label="perfect prediction")
    ax.set_xlabel("Actual t/T")
    ax.set_ylabel("Predicted t/T")
    ax.set_title(f"{layer_name}: MLP Progress Predictor\nR²={r2:.4f}, MAE={mae:.4f}")
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)
    ax.set_aspect("equal")
    ax.legend()
    ax.grid(True, alpha=0.3)

    path = os.path.join(output_dir, f"gate1b_mlp_{layer_name}.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Saved {path}")


def plot_training_curves(all_losses, layer_names, output_dir):
    """Training loss curves for all layers."""
    fig, ax = plt.subplots(1, 1, figsize=(8, 5))
    for layer_name in layer_names:
        ax.plot(all_losses[layer_name], label=layer_name)
    ax.set_xlabel("Epoch")
    ax.set_ylabel("Train MSE Loss")
    ax.set_title("MLP Progress Predictor Training Curves")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.set_yscale("log")

    path = os.path.join(output_dir, "gate1b_training_curves.png")
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"[plot] Saved {path}")


# ---------------------------------------------------------------------------
# Feature loading from pre-extracted files
# ---------------------------------------------------------------------------

def load_features_from_dir(features_dir, layer_names):
    """Load pre-extracted features from .pt files.

    Expected format: each .pt file is a dict {layer_name: Tensor(T, D)} for one trajectory.
    File naming: features_traj_000.pt, features_traj_001.pt, ...
    """
    pt_files = sorted(glob.glob(os.path.join(features_dir, "features_traj_*.pt")))
    if not pt_files:
        pt_files = sorted(glob.glob(os.path.join(features_dir, "*.pt")))
    if not pt_files:
        raise FileNotFoundError(f"No .pt feature files found in {features_dir}")

    print(f"[features] Loading {len(pt_files)} feature files from {features_dir}")
    features_per_traj = []
    for fp in pt_files:
        data = torch.load(fp, map_location="cpu", weights_only=True)
        if not isinstance(data, dict):
            print(f"  Warning: skipping {fp} (not a dict)")
            continue
        available = set(data.keys())
        needed = set(layer_names)
        if not needed.issubset(available):
            print(f"  Warning: {fp} has keys {available}, need {needed}. "
                  f"Missing: {needed - available}")
            continue
        features_per_traj.append({k: data[k] for k in layer_names})

    if not features_per_traj:
        raise ValueError(f"No valid feature files loaded from {features_dir}")

    print(f"[features] Loaded {len(features_per_traj)} trajectories")
    sample = features_per_traj[0][layer_names[0]]
    print(f"  Feature shape per timestep: {sample.shape[1]} (hidden_dim), "
          f"sample traj length: {sample.shape[0]}")
    return features_per_traj


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)

    torch.manual_seed(args.seed)
    np.random.seed(args.seed)

    layer_indices = [int(x.strip()) for x in args.layers.split(",")]
    layer_names = [f"layer_{i}" for i in layer_indices]

    print("=" * 60)
    print("Gate 1 Fallback (b): MLP Progress Predictor")
    print("=" * 60)
    print(f"  Layers:      {layer_names}")
    print(f"  Epochs:      {args.epochs}")
    print(f"  LR:          {args.lr}")
    print(f"  Patience:    {args.patience}")
    print(f"  Device:      {args.device}")
    print(f"  Seed:        {args.seed}")
    print(f"  R² threshold: {args.r2_threshold}")

    # --- Step 1: Get features ---
    if args.features_dir:
        print(f"\n[Mode] Loading pre-extracted features from {args.features_dir}")
        features_per_traj = load_features_from_dir(args.features_dir, layer_names)
    else:
        print(f"\n[Mode] Extracting features from model (no --features_dir provided)")
        model, processor = load_model(args.model_path, args.device)
        handles, layer_features, resolved_indices = register_hooks(model, layer_indices)
        layer_names = [f"layer_{i}" for i in resolved_indices]

        trajectories = load_libero_trajectories(args.data_path, args.num_trajectories)
        if not trajectories:
            print("ERROR: No valid trajectories loaded.")
            sys.exit(1)

        print(f"\nExtracting features ({len(trajectories)} trajectories) ...")
        features_per_traj = extract_features(
            model, processor, trajectories, layer_features, args.device
        )

        for h in handles:
            h.remove()

        # Save extracted features for future reuse
        feat_save_dir = os.path.join(args.output_dir, "extracted_features")
        os.makedirs(feat_save_dir, exist_ok=True)
        for i, feats in enumerate(features_per_traj):
            save_path = os.path.join(feat_save_dir, f"features_traj_{i:03d}.pt")
            torch.save(feats, save_path)
        print(f"[save] Saved {len(features_per_traj)} feature files to {feat_save_dir}")

        # Free model memory
        del model, processor
        torch.cuda.empty_cache()

    if not features_per_traj:
        print("ERROR: No features available.")
        sys.exit(1)

    # Infer hidden_dim from data
    hidden_dim = features_per_traj[0][layer_names[0]].shape[1]
    print(f"\n  Hidden dim: {hidden_dim}")
    print(f"  Trajectories: {len(features_per_traj)}")

    # --- Step 2: Prepare data (split by trajectory) ---
    data = prepare_data(features_per_traj, layer_names, seed=args.seed)

    # --- Step 3: Train & evaluate per layer ---
    results = {}
    all_losses = {}

    for layer_name in layer_names:
        print(f"\n{'─' * 60}")
        print(f"Training MLP for {layer_name}")
        print(f"{'─' * 60}")

        X_train, y_train, X_test, y_test, _ = data[layer_name]

        mlp, train_losses, best_epoch = train_mlp(
            X_train, y_train, X_test, y_test,
            input_dim=hidden_dim,
            epochs=args.epochs,
            lr=args.lr,
            patience=args.patience,
            batch_size=args.batch_size,
            device=args.device,
        )
        all_losses[layer_name] = train_losses

        r2, mae, preds, targets = evaluate_mlp(mlp, X_test, y_test, args.device)
        results[layer_name] = {"r2": r2, "mae": mae, "best_epoch": best_epoch}

        print(f"  >> {layer_name}: R²={r2:.4f}, MAE={mae:.4f}, best_epoch={best_epoch}")

        plot_predictions(preds, targets, layer_name, r2, mae, args.output_dir)

        # Save MLP checkpoint
        ckpt_path = os.path.join(args.output_dir, f"gate1b_mlp_{layer_name}.pt")
        torch.save(mlp.state_dict(), ckpt_path)

    # --- Step 4: Training curves ---
    plot_training_curves(all_losses, layer_names, args.output_dir)

    # --- Step 5: Gate 1(b) decision ---
    print("\n" + "=" * 60)
    print("GATE 1(b) RESULTS: MLP Progress Predictor")
    print("=" * 60)

    gate_passed = False
    gate_layer = None

    for layer_name in layer_names:
        r = results[layer_name]
        status = "PASS" if r["r2"] > args.r2_threshold else "FAIL"
        print(f"  {layer_name}: R²={r['r2']:.4f}, MAE={r['mae']:.4f} -> {status}")
        if r["r2"] > args.r2_threshold and not gate_passed:
            gate_passed = True
            gate_layer = layer_name

    print("-" * 60)
    if gate_passed:
        print(f"GATE 1(b) PASSED ({gate_layer}, R²={results[gate_layer]['r2']:.4f})")
    else:
        print("GATE 1(b) FAILED — proceed to fallback (c): VIP features")
    print("=" * 60)

    # Save results JSON
    summary = {
        "gate": "1b",
        "passed": gate_passed,
        "r2_threshold": args.r2_threshold,
        "best_layer": gate_layer,
        "per_layer": results,
        "num_trajectories": len(features_per_traj),
        "seed": args.seed,
    }
    json_path = os.path.join(args.output_dir, "gate1b_results.json")
    with open(json_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nResults saved to {json_path}")


if __name__ == "__main__":
    main()
