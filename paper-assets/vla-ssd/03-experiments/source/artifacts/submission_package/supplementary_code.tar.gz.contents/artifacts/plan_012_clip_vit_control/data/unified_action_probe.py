"""Unified action probe: identical hyperparams across all vision encoders.

Models: SigLIP projector, DINOv2 cls_token, CLIP cls_token,
        VLA trained image_mean L19, VLA trained last_preaction L19.

Hyperparams (fixed): epochs=50, patience=5, lr=1e-3, batch=256, hidden=256, seed=42.
Target: predict next action a_{t+1} from feature at time t.
Split: 80/20 per-task (first 80% demos = train).
Target normalization: z-score using train mean/std.
"""
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---
import os, json, time, glob
from pathlib import Path

import h5py
import numpy as np
import torch
import torch.nn as nn
from sklearn.metrics import r2_score

SEED = 42
BATCH_SIZE = 256
LR = 1e-3
EPOCHS = 50
PATIENCE = 5
HIDDEN_DIM = 256
DEVICE = torch.device("cuda:0")

DATA_DIR = f"{PROJECT_ROOT}/data/libero/libero_goal/"
FEATURE_BASE = f"{PROJECT_ROOT}/features/"
OUT_PATH = f"{PROJECT_ROOT}/results/functional_validation/unified_action_probe.json"

FEATURE_CONFIGS = {
    "projector": {
        "dir": "siglip_only_libero_goal",
        "key_prefix": "demo",
        "feat_key": "last_preaction",
        "layer": None,
        "input_dim": 4096,
    },
    "dino_cls": {
        "dir": "dinov2_libero_goal",
        "key_prefix": "traj",
        "feat_key": "cls_token",
        "layer": None,
        "input_dim": 1024,
    },
    "clip_cls": {
        "dir": "clip_libero_goal",
        "key_prefix": "traj",
        "feat_key": "cls_token",
        "layer": None,
        "input_dim": 1024,
    },
    "vla_image_mean_L19": {
        "dir": "trained_libero_goal",
        "key_prefix": "demo",
        "feat_key": "image_mean",
        "layer": 19,
        "input_dim": 4096,
    },
    "vla_last_preaction_L19": {
        "dir": "trained_libero_goal",
        "key_prefix": "demo",
        "feat_key": "last_preaction",
        "layer": 19,
        "input_dim": 4096,
    },
}


class ActionMLPProbe(nn.Module):
    def __init__(self, in_dim, out_dim=7, hidden_dim=HIDDEN_DIM):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, out_dim),
        )

    def forward(self, x):
        return self.net(x)


def load_features_and_actions(cfg):
    feat_dir = os.path.join(FEATURE_BASE, cfg["dir"])
    prefix = cfg["key_prefix"]
    feat_key = cfg["feat_key"]
    layer = cfg["layer"]

    task_data = {}
    for h5_path in sorted(glob.glob(os.path.join(feat_dir, "*.h5"))):
        task = Path(h5_path).stem
        action_path = os.path.join(DATA_DIR, f"{task}_demo.hdf5")
        if not os.path.exists(action_path):
            print(f"  WARNING: no action file for {task}, skipping")
            continue

        demos = []
        with h5py.File(h5_path, "r") as ff, h5py.File(action_path, "r") as fa:
            keys = sorted(
                [k for k in ff.keys() if k.startswith(f"{prefix}_")],
                key=lambda x: int(x.split("_")[-1]),
            )
            for k in keys:
                idx = int(k.split("_")[-1])
                ds = ff[k][feat_key]
                if layer is not None and len(ds.shape) == 3:
                    feat = np.asarray(ds[:, layer, :], dtype=np.float32)
                else:
                    feat = np.asarray(ds[:], dtype=np.float32)
                act = np.asarray(fa[f"data/demo_{idx}/actions"], dtype=np.float32)
                demos.append((feat, act))
        task_data[task] = demos
    return task_data


def build_train_val(task_data):
    X_tr_list, y_tr_list = [], []
    X_val_list, y_val_list, val_tasks = [], [], []

    for task in sorted(task_data.keys()):
        demos = task_data[task]
        n_train = int(len(demos) * 0.8)

        for i, (feat, act) in enumerate(demos):
            T = min(feat.shape[0], act.shape[0])
            if T < 2:
                continue
            x = torch.from_numpy(feat[: T - 1])
            y = torch.from_numpy(act[1:T])

            if i < n_train:
                X_tr_list.append(x)
                y_tr_list.append(y)
            else:
                X_val_list.append(x)
                y_val_list.append(y)
                val_tasks.extend([task] * (T - 1))

    return torch.cat(X_tr_list), torch.cat(y_tr_list), torch.cat(X_val_list), torch.cat(y_val_list), val_tasks


def train_and_eval(X_tr, y_tr_raw, X_val, y_val_raw, val_tasks, in_dim, tag=""):
    torch.manual_seed(SEED)
    np.random.seed(SEED)

    y_mean = y_tr_raw.mean(dim=0)
    y_std = y_tr_raw.std(dim=0).clamp(min=1e-6)
    y_tr = (y_tr_raw - y_mean) / y_std
    y_val = (y_val_raw - y_mean) / y_std

    X_tr_d = X_tr.to(DEVICE)
    y_tr_d = y_tr.to(DEVICE)
    X_val_d = X_val.to(DEVICE)
    y_val_d = y_val.to(DEVICE)

    model = ActionMLPProbe(in_dim).to(DEVICE)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)
    criterion = nn.MSELoss()

    n = len(X_tr_d)
    best_val_loss = float("inf")
    best_state = None
    wait = 0
    epochs_trained = 0

    for epoch in range(EPOCHS):
        model.train()
        perm = torch.randperm(n, device=DEVICE)
        for start in range(0, n, BATCH_SIZE):
            idx = perm[start : start + BATCH_SIZE]
            pred = model(X_tr_d[idx])
            loss = criterion(pred, y_tr_d[idx])
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

        model.eval()
        with torch.no_grad():
            val_pred = model(X_val_d)
            val_loss = criterion(val_pred, y_val_d).item()

        epochs_trained = epoch + 1
        if val_loss < best_val_loss - 1e-6:
            best_val_loss = val_loss
            best_state = {k: v.cpu().clone() for k, v in model.state_dict().items()}
            wait = 0
        else:
            wait += 1
            if wait >= PATIENCE:
                break

    model.load_state_dict(best_state)
    model.eval()

    with torch.no_grad():
        pred_norm = model(X_val_d).cpu()
    pred = pred_norm * y_std + y_mean
    y_true = y_val_raw.numpy()
    pred_np = pred.numpy()

    ss_res = np.sum((y_true - pred_np) ** 2)
    ss_tot = np.sum((y_true - y_true.mean(axis=0)) ** 2)
    overall_r2 = float(1 - ss_res / ss_tot)

    dim_names = ["dx", "dy", "dz", "drx", "dry", "drz", "gripper"]
    per_dim_r2 = {}
    for j, name in enumerate(dim_names):
        ss_r = np.sum((y_true[:, j] - pred_np[:, j]) ** 2)
        ss_t = np.sum((y_true[:, j] - y_true[:, j].mean()) ** 2)
        per_dim_r2[name] = float(1 - ss_r / ss_t) if ss_t > 0 else 0.0

    gripper_acc = float(np.mean((pred_np[:, 6] >= 0) == (y_true[:, 6] >= 0)))

    tasks_arr = np.array(val_tasks)
    unique_tasks = sorted(set(val_tasks))
    per_task_r2 = {}
    for t in unique_tasks:
        mask = tasks_arr == t
        yt = y_true[mask]
        yp = pred_np[mask]
        ss_r = np.sum((yt - yp) ** 2)
        ss_t = np.sum((yt - yt.mean(axis=0)) ** 2)
        per_task_r2[t] = float(1 - ss_r / ss_t) if ss_t > 0 else 0.0

    mean_r2 = float(np.mean(list(per_task_r2.values())))

    print(f"  [{tag}] mean_R2={mean_r2:.4f}  overall_R2={overall_r2:.4f}  "
          f"gripper_acc={gripper_acc:.4f}  epochs={epochs_trained}")

    return {
        "mean_R2": mean_r2,
        "overall_R2": overall_r2,
        "per_task_R2": per_task_r2,
        "per_dim_R2": per_dim_r2,
        "gripper_acc": gripper_acc,
        "epochs_trained": epochs_trained,
        "val_loss": float(best_val_loss),
    }


def bootstrap_pairwise(r2_a, r2_b, n_boot=10000):
    np.random.seed(SEED)
    tasks = sorted(r2_a.keys())
    a = np.array([r2_a[t] for t in tasks])
    b = np.array([r2_b[t] for t in tasks])
    observed = float(a.mean() - b.mean())

    n = len(tasks)
    deltas = np.empty(n_boot)
    for i in range(n_boot):
        idx = np.random.randint(0, n, n)
        deltas[i] = a[idx].mean() - b[idx].mean()

    ci_lo = float(np.percentile(deltas, 2.5))
    ci_hi = float(np.percentile(deltas, 97.5))
    p_one = float(np.mean(deltas <= 0)) if observed > 0 else float(np.mean(deltas >= 0))
    p_value = float(min(p_one * 2, 1.0))

    return {"delta": observed, "ci_95": [ci_lo, ci_hi], "p_value": p_value}


def main():
    results = {}
    results["hyperparams"] = {
        "epochs": EPOCHS, "patience": PATIENCE, "lr": LR,
        "batch_size": BATCH_SIZE, "hidden": HIDDEN_DIM, "seed": SEED,
        "target": "next_action_a_{t+1}", "normalization": "z-score",
        "split": "80/20_per_task_by_demo_index",
    }

    for name, cfg in FEATURE_CONFIGS.items():
        print(f"\n=== {name} ===")
        t0 = time.time()
        task_data = load_features_and_actions(cfg)
        X_tr, y_tr, X_val, y_val, val_tasks = build_train_val(task_data)
        print(f"  Samples: {len(X_tr)} train / {len(X_val)} val, dim={X_tr.shape[1]}")
        metrics = train_and_eval(X_tr, y_tr, X_val, y_val, val_tasks, cfg["input_dim"], name)
        results[name] = metrics
        print(f"  Time: {time.time() - t0:.1f}s")
        del task_data, X_tr, y_tr, X_val, y_val
        torch.cuda.empty_cache()

    print("\n=== Bootstrap Pairwise Comparisons ===")
    pairs = [
        ("projector", "dino_cls"),
        ("projector", "clip_cls"),
        ("clip_cls", "dino_cls"),
        ("projector", "vla_image_mean_L19"),
        ("projector", "vla_last_preaction_L19"),
    ]
    bootstrap = {}
    for a, b in pairs:
        key = f"{a}_vs_{b}"
        ci = bootstrap_pairwise(results[a]["per_task_R2"], results[b]["per_task_R2"])
        bootstrap[key] = ci
        print(f"  {key}: delta={ci['delta']:.4f}, CI={ci['ci_95']}, p={ci['p_value']:.4f}")
    results["bootstrap_pairwise"] = bootstrap

    print("\n=== Summary ===")
    for name in FEATURE_CONFIGS:
        m = results[name]
        print(f"  {name:30s} mean_R2={m['mean_R2']:.4f}  overall_R2={m['overall_R2']:.4f}")

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {OUT_PATH}")


if __name__ == "__main__":
    main()
