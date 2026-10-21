"""Demo Count Sensitivity: compare RSA + probe profiles from 25 vs 50 demos.

Subsamples 25 demos (seed=42) from each task's 50 demos, reruns:
  - RSA: Method B (cosine rep dist, euclidean action dist, N_SAMPLE=20, within-task Spearman)
  - Probe: MLP (->256->7), epochs=50, patience=5, lr=1e-3, batch=256, seed=42

Only trained_image_mean condition (33 layers).
"""
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---

import argparse
import json
import os
import time
import glob
from itertools import combinations
from pathlib import Path

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
import torch
import torch.nn as nn
from scipy.spatial.distance import pdist
from scipy.stats import spearmanr

FEATURE_DIR = f"{PROJECT_ROOT}/features/trained_libero_goal/"
DATA_DIR = f"{PROJECT_ROOT}/data/libero/libero_goal/"
OUT_PATH = f"{PROJECT_ROOT}/results/ablations/demo_sensitivity_25.json"

N_LAYERS = 33
INPUT_DIM = 4096
HIDDEN_DIM = 256
ACTION_DIM = 7
BATCH_SIZE = 256
LR = 1e-3
EPOCHS = 50
PATIENCE = 5
N_SAMPLE = 20
SUBSAMPLE_SEED = 42
N_DEMOS_SUBSET = 25


class MLPProbe(nn.Module):
    def __init__(self):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(INPUT_DIM, HIDDEN_DIM),
            nn.ReLU(),
            nn.Linear(HIDDEN_DIM, ACTION_DIM),
        )

    def forward(self, x):
        return self.net(x)


def discover_tasks():
    return sorted([Path(p).stem for p in glob.glob(os.path.join(FEATURE_DIR, "*.h5"))])


def subsample_indices(n_total, n_subset, seed):
    rng = np.random.RandomState(seed)
    return sorted(rng.choice(n_total, n_subset, replace=False).tolist())


def subsample_to_length(arr, target_len):
    T = arr.shape[0]
    if T <= target_len:
        return arr
    idx = np.linspace(0, T - 1, target_len, dtype=int)
    return arr[idx]


def load_actions(task):
    path = os.path.join(DATA_DIR, f"{task}_demo.hdf5")
    if not os.path.exists(path):
        return {}
    result = {}
    with h5py.File(path, "r") as f:
        for key in f["data"].keys():
            if key.startswith("demo_"):
                did = int(key.split("_")[1])
                result[did] = f[f"data/{key}/actions"][:].astype(np.float32)
    return result


# ===== RSA =====

def compute_rsa_for_layer(layer, tasks, demo_indices_map, actions_cache):
    """Compute RSA for one layer using specified demo indices per task."""
    task_rhos = []

    for task in tasks:
        if task not in actions_cache:
            actions_cache[task] = load_actions(task)
        actions = actions_cache[task]

        feat_path = os.path.join(FEATURE_DIR, f"{task}.h5")
        if not os.path.exists(feat_path):
            continue

        demo_ids = demo_indices_map[task]
        with h5py.File(feat_path, "r") as f:
            available = sorted(
                set(int(k.split("_")[1]) for k in f.keys() if k.startswith("demo_"))
                & set(actions.keys())
            )
            use_ids = [d for d in demo_ids if d in available]

            if len(use_ids) < 2:
                continue

            demo_reps = []
            demo_acts = []
            for did in use_ids:
                feat = np.asarray(f[f"demo_{did}"]["image_mean"][:, layer, :], dtype=np.float32)
                act = actions[did]
                T = min(feat.shape[0], act.shape[0])
                if T < 2:
                    continue
                feat_sub = subsample_to_length(feat[:T], N_SAMPLE)
                act_sub = subsample_to_length(act[:T], N_SAMPLE)
                demo_reps.append(feat_sub.mean(axis=0))
                demo_acts.append(act_sub.mean(axis=0))

            if len(demo_reps) < 2:
                continue

            rep_mat = np.array(demo_reps)
            act_mat = np.array(demo_acts)

            rep_dists = pdist(rep_mat, metric="cosine")
            act_dists = pdist(act_mat, metric="euclidean")

            if rep_dists.std() < 1e-12 or act_dists.std() < 1e-12:
                continue

            rho, _ = spearmanr(rep_dists, act_dists)
            if not np.isnan(rho):
                task_rhos.append(rho)

    if task_rhos:
        return float(np.mean(task_rhos))
    return None


# ===== Probe =====

def load_probe_data_for_layer(layer, demo_indices_map):
    """Load features and actions for probe training using specified demo indices."""
    task_data = {}
    for h5_path in sorted(glob.glob(os.path.join(FEATURE_DIR, "*.h5"))):
        task = Path(h5_path).stem
        action_path = os.path.join(DATA_DIR, f"{task}_demo.hdf5")
        if not os.path.exists(action_path):
            continue

        use_ids = demo_indices_map[task]
        demos = []
        with h5py.File(h5_path, "r") as ff, h5py.File(action_path, "r") as fa:
            for did in use_ids:
                feat_key = f"demo_{did}"
                act_key = f"data/demo_{did}/actions"
                if feat_key not in ff or act_key not in fa:
                    continue
                feat = np.asarray(ff[feat_key]["image_mean"][:, layer, :], dtype=np.float32)
                act = np.asarray(fa[act_key], dtype=np.float32)
                demos.append((feat, act))
        if demos:
            task_data[task] = demos
    return task_data


def build_train_val(task_data):
    X_tr, y_tr = [], []
    X_val, y_val, val_tasks = [], [], []

    for task in sorted(task_data.keys()):
        demos = task_data[task]
        n_train = int(len(demos) * 0.8)

        for i, (feat, act) in enumerate(demos):
            T = min(feat.shape[0], act.shape[0])
            if T < 2:
                continue
            x = torch.from_numpy(feat[:T - 1])
            y = torch.from_numpy(act[1:T])

            if i < n_train:
                X_tr.append(x)
                y_tr.append(y)
            else:
                X_val.append(x)
                y_val.append(y)
                val_tasks.extend([task] * (T - 1))

    if not X_tr or not X_val:
        return None, None, None, None, None
    return (torch.cat(X_tr), torch.cat(y_tr),
            torch.cat(X_val), torch.cat(y_val), val_tasks)


def train_probe(X_tr, y_tr, X_val, y_val, val_tasks, seed, device):
    torch.manual_seed(seed)
    np.random.seed(seed)

    mu = X_tr.mean(dim=0)
    std = X_tr.std(dim=0).clamp(min=1e-8)
    X_tr_n = ((X_tr - mu) / std).to(device)
    y_tr_d = y_tr.to(device)
    X_val_n = ((X_val - mu) / std).to(device)
    y_val_d = y_val.to(device)

    model = MLPProbe().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)
    loss_fn = nn.MSELoss()

    best_val_loss = float("inf")
    patience_count = 0
    best_pred = None
    n_tr = X_tr_n.shape[0]

    for epoch in range(EPOCHS):
        model.train()
        perm = torch.randperm(n_tr, device=device)
        for start in range(0, n_tr, BATCH_SIZE):
            idx = perm[start:start + BATCH_SIZE]
            pred = model(X_tr_n[idx])
            loss = loss_fn(pred, y_tr_d[idx])
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_pred = model(X_val_n)
            val_loss = loss_fn(val_pred, y_val_d).item()

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            patience_count = 0
            best_pred = val_pred.cpu()
        else:
            patience_count += 1
            if patience_count >= PATIENCE:
                break

    y_val_np = y_val.numpy()
    pred_np = best_pred.numpy()
    tasks_arr = np.array(val_tasks)
    unique_tasks = sorted(set(val_tasks))

    r2_list = []
    for task in unique_tasks:
        mask = tasks_arr == task
        y_t = y_val_np[mask]
        p_t = pred_np[mask]
        ss_res = np.sum((y_t - p_t) ** 2)
        ss_tot = np.sum((y_t - y_t.mean(axis=0)) ** 2)
        r2 = 1.0 - ss_res / max(ss_tot, 1e-8)
        r2_list.append(float(r2))

    return float(np.mean(r2_list))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--gpu", type=int, default=0)
    parser.add_argument("--dry-run", action="store_true",
                        help="Only run layer 0 to verify logic")
    args = parser.parse_args()

    device = f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu"
    layers = [0] if args.dry_run else list(range(N_LAYERS))

    print(f"Demo Sensitivity | device={device} | layers={len(layers)} | "
          f"25 vs 50 demos | seed={SUBSAMPLE_SEED}")
    print("=" * 60)

    t_start = time.time()
    tasks = discover_tasks()
    print(f"Found {len(tasks)} tasks")

    # Build demo index maps
    all_demo_ids = list(range(50))
    subset_indices = subsample_indices(50, N_DEMOS_SUBSET, SUBSAMPLE_SEED)
    print(f"Subset indices (first 10): {subset_indices[:10]}")

    full_map = {task: all_demo_ids for task in tasks}
    subset_map = {task: subset_indices for task in tasks}

    actions_cache = {}

    rsa_50 = []
    rsa_25 = []
    probe_50 = []
    probe_25 = []

    for li, layer in enumerate(layers):
        t_layer = time.time()

        # RSA
        rsa_full = compute_rsa_for_layer(layer, tasks, full_map, actions_cache)
        rsa_sub = compute_rsa_for_layer(layer, tasks, subset_map, actions_cache)
        rsa_50.append(rsa_full)
        rsa_25.append(rsa_sub)

        # Probe - full
        task_data_full = load_probe_data_for_layer(layer, full_map)
        data_full = build_train_val(task_data_full)
        if data_full[0] is not None:
            r2_full = train_probe(*data_full, seed=42, device=device)
        else:
            r2_full = None
        probe_50.append(r2_full)

        # Probe - subset
        task_data_sub = load_probe_data_for_layer(layer, subset_map)
        data_sub = build_train_val(task_data_sub)
        if data_sub[0] is not None:
            r2_sub = train_probe(*data_sub, seed=42, device=device)
        else:
            r2_sub = None
        probe_25.append(r2_sub)

        dt = time.time() - t_layer
        print(f"Layer {layer:2d} | RSA 50={rsa_full:.4f} 25={rsa_sub:.4f} | "
              f"Probe 50={r2_full:.4f} 25={r2_sub:.4f} | {dt:.1f}s")

    # Comparison
    rsa_50_valid = [v for v in rsa_50 if v is not None]
    rsa_25_valid = [v for v in rsa_25 if v is not None]
    probe_50_valid = [v for v in probe_50 if v is not None]
    probe_25_valid = [v for v in probe_25 if v is not None]

    # Profile correlations (only where both are valid)
    rsa_paired = [(a, b) for a, b in zip(rsa_50, rsa_25) if a is not None and b is not None]
    probe_paired = [(a, b) for a, b in zip(probe_50, probe_25) if a is not None and b is not None]

    rsa_profile_corr = float(spearmanr(
        [p[0] for p in rsa_paired], [p[1] for p in rsa_paired]
    )[0]) if len(rsa_paired) >= 3 else None

    probe_profile_corr = float(spearmanr(
        [p[0] for p in probe_paired], [p[1] for p in probe_paired]
    )[0]) if len(probe_paired) >= 3 else None

    # Peak detection
    def find_peak(values, metric_name):
        valid = [(i, v) for i, v in enumerate(values) if v is not None]
        if not valid:
            return {"layer": None, metric_name: None}
        best_i, best_v = max(valid, key=lambda x: x[1])
        return {"layer": best_i, metric_name: round(best_v, 4)}

    result = {
        "method": "Demo count sensitivity (25 vs 50 demos)",
        "condition": "trained_image_mean",
        "subsample_seed": SUBSAMPLE_SEED,
        "n_demos_full": 50,
        "n_demos_subset": N_DEMOS_SUBSET,
        "n_tasks": len(tasks),
        "rsa_50demos": [round(v, 4) if v is not None else None for v in rsa_50],
        "rsa_25demos": [round(v, 4) if v is not None else None for v in rsa_25],
        "probe_50demos": [round(v, 4) if v is not None else None for v in probe_50],
        "probe_25demos": [round(v, 4) if v is not None else None for v in probe_25],
        "comparison": {
            "rsa_profile_correlation": round(rsa_profile_corr, 4) if rsa_profile_corr is not None else None,
            "probe_profile_correlation": round(probe_profile_corr, 4) if probe_profile_corr is not None else None,
            "rsa_peak_50": find_peak(rsa_50, "rsa"),
            "rsa_peak_25": find_peak(rsa_25, "rsa"),
            "probe_peak_50": find_peak(probe_50, "r2"),
            "probe_peak_25": find_peak(probe_25, "r2"),
        },
        "elapsed_seconds": round(time.time() - t_start, 1),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2)

    print(f"\n{'='*60}")
    print(f"RSA profile correlation (50 vs 25): {rsa_profile_corr}")
    print(f"Probe profile correlation (50 vs 25): {probe_profile_corr}")
    print(f"RSA peak 50: {find_peak(rsa_50, 'rsa')}")
    print(f"RSA peak 25: {find_peak(rsa_25, 'rsa')}")
    print(f"Probe peak 50: {find_peak(probe_50, 'r2')}")
    print(f"Probe peak 25: {find_peak(probe_25, 'r2')}")
    print(f"\nDone in {(time.time()-t_start)/60:.1f} min. Saved to {OUT_PATH}")


if __name__ == "__main__":
    main()
