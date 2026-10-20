"""Full-layer action probe R² scan: L0-L32 × trained/untrained × image_mean/last_preaction.
Matches unified_action_probe.py hyperparams (50ep/patience5/lr1e-3/hidden256/seed42).
Outputs per-layer R² curves + bootstrap CIs for peak comparisons.
"""
import os, json, time, glob
from pathlib import Path
from multiprocessing import Process, Manager

import h5py
import numpy as np
import torch
import torch.nn as nn

SEED = 42
BATCH_SIZE = 256
LR = 1e-3
EPOCHS = 50
PATIENCE = 5
HIDDEN_DIM = 256
N_LAYERS = 33
INPUT_DIM = 4096

DATA_DIR = "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/"
FEATURE_BASE = "/root/autodl-tmp/vla-ssd/features/"
UNIFIED_JSON = "/root/autodl-tmp/vla-ssd/results/functional_validation/unified_action_probe.json"
OUT_PATH = "/root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json"

CONDITIONS = {
    "trained": {"dir": "trained_libero_goal", "device": "cuda:0"},
    "untrained": {"dir": "untrained_libero_goal", "device": "cuda:1"},
}
AGG_KEYS = ["image_mean", "last_preaction"]


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


def load_features_and_actions(feat_dir, agg_key, layer):
    task_data = {}
    for h5_path in sorted(glob.glob(os.path.join(feat_dir, "*.h5"))):
        task = Path(h5_path).stem
        action_path = os.path.join(DATA_DIR, f"{task}_demo.hdf5")
        if not os.path.exists(action_path):
            continue

        demos = []
        with h5py.File(h5_path, "r") as ff, h5py.File(action_path, "r") as fa:
            keys = sorted(
                [k for k in ff.keys() if k.startswith("demo_")],
                key=lambda x: int(x.split("_")[-1]),
            )
            for k in keys:
                idx = int(k.split("_")[-1])
                feat = np.asarray(ff[k][agg_key][:, layer, :], dtype=np.float32)
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

    return (torch.cat(X_tr_list), torch.cat(y_tr_list),
            torch.cat(X_val_list), torch.cat(y_val_list), val_tasks)


def train_and_eval(X_tr, y_tr_raw, X_val, y_val_raw, val_tasks, device):
    torch.manual_seed(SEED)
    np.random.seed(SEED)

    y_mean = y_tr_raw.mean(dim=0)
    y_std = y_tr_raw.std(dim=0).clamp(min=1e-6)
    y_tr = (y_tr_raw - y_mean) / y_std
    y_val = (y_val_raw - y_mean) / y_std

    X_tr_d = X_tr.to(device)
    y_tr_d = y_tr.to(device)
    X_val_d = X_val.to(device)
    y_val_d = y_val.to(device)

    model = ActionMLPProbe(INPUT_DIM).to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)
    criterion = nn.MSELoss()

    n = len(X_tr_d)
    best_val_loss = float("inf")
    best_state = None
    wait = 0
    epochs_trained = 0

    for epoch in range(EPOCHS):
        model.train()
        perm = torch.randperm(n, device=device)
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

    return {
        "mean_R2": mean_r2,
        "overall_R2": overall_r2,
        "per_task_R2": per_task_r2,
        "gripper_acc": gripper_acc,
        "epochs_trained": epochs_trained,
    }


def run_condition(condition, cfg, result_dict):
    device = torch.device(cfg["device"])
    feat_dir = os.path.join(FEATURE_BASE, cfg["dir"])
    cond_results = {}

    for agg_key in AGG_KEYS:
        layer_results = {}
        for layer in range(N_LAYERS):
            t0 = time.time()
            task_data = load_features_and_actions(feat_dir, agg_key, layer)
            X_tr, y_tr, X_val, y_val, val_tasks = build_train_val(task_data)
            metrics = train_and_eval(X_tr, y_tr, X_val, y_val, val_tasks, device)
            elapsed = time.time() - t0
            layer_results[f"layer_{layer}"] = metrics
            print(f"  {condition}/{agg_key}/L{layer}: mean_R2={metrics['mean_R2']:.4f} "
                  f"({elapsed:.1f}s, ep={metrics['epochs_trained']})")
            del task_data, X_tr, y_tr, X_val, y_val
            torch.cuda.empty_cache()
        cond_results[agg_key] = layer_results

    result_dict[condition] = cond_results


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


def find_peak(layer_results):
    best_layer, best_r2 = -1, -999
    for lk, metrics in layer_results.items():
        if metrics["mean_R2"] > best_r2:
            best_r2 = metrics["mean_R2"]
            best_layer = int(lk.split("_")[1])
    return {"layer": best_layer, "mean_R2": best_r2}


def main():
    print("=" * 60)
    print("Full-layer action probe R² scan")
    print(f"33 layers × 2 conditions × 2 aggs = 132 probes")
    print("=" * 60)
    t_start = time.time()

    manager = Manager()
    result_dict = manager.dict()

    processes = []
    for condition, cfg in CONDITIONS.items():
        p = Process(target=run_condition, args=(condition, cfg, result_dict))
        p.start()
        processes.append(p)
        print(f"Started {condition} on {cfg['device']}")

    for p in processes:
        p.join()

    results = dict(result_dict)

    # --- summary ---
    summary = {}
    for cond in ["trained", "untrained"]:
        for agg in AGG_KEYS:
            peak = find_peak(results[cond][agg])
            summary[f"{cond}_{agg}_peak"] = peak
            print(f"Peak {cond}/{agg}: L{peak['layer']} mean_R2={peak['mean_R2']:.4f}")

    # --- load reference baselines ---
    with open(UNIFIED_JSON, "r") as f:
        unified = json.load(f)
    proj_per_task = unified["projector"]["per_task_R2"]
    dino_per_task = unified["dino_cls"]["per_task_R2"]

    # --- bootstrap comparisons ---
    print("\n=== Bootstrap Comparisons ===")
    bootstrap = {}

    # a) Projector vs trained image_mean peak
    tr_im_peak = summary["trained_image_mean_peak"]
    tr_im_peak_r2 = results["trained"]["image_mean"][f"layer_{tr_im_peak['layer']}"]["per_task_R2"]
    comp = bootstrap_pairwise(proj_per_task, tr_im_peak_r2)
    bootstrap["projector_vs_trained_imgmean_peak"] = comp
    print(f"  projector vs trained imgmean peak (L{tr_im_peak['layer']}): "
          f"delta={comp['delta']:.4f}, CI={comp['ci_95']}, p={comp['p_value']:.4f}")

    # b) Trained vs untrained best-vs-best (image_mean)
    tr_peak = summary["trained_image_mean_peak"]
    un_peak = summary["untrained_image_mean_peak"]
    tr_r2 = results["trained"]["image_mean"][f"layer_{tr_peak['layer']}"]["per_task_R2"]
    un_r2 = results["untrained"]["image_mean"][f"layer_{un_peak['layer']}"]["per_task_R2"]
    comp = bootstrap_pairwise(tr_r2, un_r2)
    bootstrap["trained_vs_untrained_imgmean_bestvsbest"] = comp
    print(f"  trained(L{tr_peak['layer']}) vs untrained(L{un_peak['layer']}) imgmean best-vs-best: "
          f"delta={comp['delta']:.4f}, CI={comp['ci_95']}, p={comp['p_value']:.4f}")

    # c) Trained vs untrained best-vs-best (last_preaction)
    tr_peak_lp = summary["trained_last_preaction_peak"]
    un_peak_lp = summary["untrained_last_preaction_peak"]
    tr_r2_lp = results["trained"]["last_preaction"][f"layer_{tr_peak_lp['layer']}"]["per_task_R2"]
    un_r2_lp = results["untrained"]["last_preaction"][f"layer_{un_peak_lp['layer']}"]["per_task_R2"]
    comp = bootstrap_pairwise(tr_r2_lp, un_r2_lp)
    bootstrap["trained_vs_untrained_lastpre_bestvsbest"] = comp
    print(f"  trained(L{tr_peak_lp['layer']}) vs untrained(L{un_peak_lp['layer']}) lastpre best-vs-best: "
          f"delta={comp['delta']:.4f}, CI={comp['ci_95']}, p={comp['p_value']:.4f}")

    # d) Same-layer comparison at trained peak (image_mean)
    trained_peak_layer = tr_peak["layer"]
    tr_sl = results["trained"]["image_mean"][f"layer_{trained_peak_layer}"]["per_task_R2"]
    un_sl = results["untrained"]["image_mean"][f"layer_{trained_peak_layer}"]["per_task_R2"]
    comp = bootstrap_pairwise(tr_sl, un_sl)
    bootstrap["trained_vs_untrained_imgmean_samelayer"] = comp
    print(f"  same-layer(L{trained_peak_layer}) imgmean: "
          f"delta={comp['delta']:.4f}, CI={comp['ci_95']}, p={comp['p_value']:.4f}")

    # e) Same-layer comparison at trained peak (last_preaction)
    trained_peak_layer_lp = tr_peak_lp["layer"]
    tr_sl_lp = results["trained"]["last_preaction"][f"layer_{trained_peak_layer_lp}"]["per_task_R2"]
    un_sl_lp = results["untrained"]["last_preaction"][f"layer_{trained_peak_layer_lp}"]["per_task_R2"]
    comp = bootstrap_pairwise(tr_sl_lp, un_sl_lp)
    bootstrap["trained_vs_untrained_lastpre_samelayer"] = comp
    print(f"  same-layer(L{trained_peak_layer_lp}) lastpre: "
          f"delta={comp['delta']:.4f}, CI={comp['ci_95']}, p={comp['p_value']:.4f}")

    # --- assemble output ---
    output = {
        "hyperparams": {
            "epochs": EPOCHS, "patience": PATIENCE, "lr": LR,
            "batch_size": BATCH_SIZE, "hidden": HIDDEN_DIM, "seed": SEED,
            "target": "next_action_a_{t+1}", "normalization": "z-score",
            "split": "80/20_per_task_by_demo_index",
            "model": "Linear(4096,256)->ReLU->Linear(256,7)",
        },
        "trained": results["trained"],
        "untrained": results["untrained"],
        "summary": summary,
        "bootstrap_comparisons": bootstrap,
        "reference_baselines": {
            "projector_mean_R2": unified["projector"]["mean_R2"],
            "projector_per_task_R2": proj_per_task,
            "dino_cls_mean_R2": unified["dino_cls"]["mean_R2"],
            "dino_cls_per_task_R2": dino_per_task,
        },
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    elapsed = time.time() - t_start
    print(f"\nDone in {elapsed/60:.1f} min. Saved to {OUT_PATH}")


if __name__ == "__main__":
    main()
