"""Llama-2 base action probe R²: extract features + train 33-layer probes.

Phase 1: Extract hidden states from llama2base checkpoint (OpenVLA with Llama-2 base LLM weights)
Phase 2: Train MLP action probes per layer, image_mean readout
"""
import gc
import glob
import json
import os
import time
from pathlib import Path

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
import torch
import torch.nn as nn
from PIL import Image

NUM_IMAGE_TOKENS = 256
N_LAYERS = 33
INPUT_DIM = 4096

SEED = 42
BATCH_SIZE = 256
LR = 1e-3
EPOCHS = 50
PATIENCE = 5
HIDDEN_DIM = 256

MODEL_PATH = "/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b-llama2base"
DATA_DIR = "/root/autodl-tmp/vla-ssd/data/libero/libero_goal/"
FEATURE_DIR = "/root/autodl-tmp/vla-ssd/features/llama2base_libero_goal/"
OUT_PATH = "/root/autodl-tmp/vla-ssd/results/action_probe/llama2base_action_probe.json"
EXISTING_RESULTS = "/root/autodl-tmp/vla-ssd/results/functional_validation/fulllayer_action_probe.json"

GPU = int(os.environ.get("CUDA_VISIBLE_DEVICES", "1").split(",")[0])
EXTRACT_BATCH = 4
MAX_DEMOS = 50


def task_desc_from_filename(fname):
    stem = Path(fname).stem.replace("_demo", "")
    return stem.replace("_", " ")


# ─── Phase 1: Feature extraction ───


def extract_features():
    from transformers import AutoModelForVision2Seq, AutoProcessor

    device = torch.device(f"cuda:{GPU}")

    print("=" * 60)
    print("Phase 1: Feature Extraction (llama2base)")
    print(f"Model: {MODEL_PATH}")
    print(f"Device: {device}")
    print("=" * 60)

    os.makedirs(FEATURE_DIR, exist_ok=True)

    hdf5_files = sorted(glob.glob(os.path.join(DATA_DIR, "*.hdf5")))
    print(f"Tasks: {len(hdf5_files)}")

    all_done = True
    for hdf5_path in hdf5_files:
        task_id = Path(hdf5_path).stem.replace("_demo", "")
        out_path = os.path.join(FEATURE_DIR, f"{task_id}.h5")
        if not os.path.exists(out_path):
            all_done = False
            break

    if all_done:
        print("All feature files exist, skipping extraction.")
        return

    processor = AutoProcessor.from_pretrained(
        MODEL_PATH, trust_remote_code=True, local_files_only=True
    )
    model = AutoModelForVision2Seq.from_pretrained(
        MODEL_PATH,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
        local_files_only=True,
    )
    model = model.to(device).eval()
    n_params = sum(p.numel() for p in model.parameters()) / 1e9
    print(f"Model loaded: {n_params:.1f}B params on {device}")

    layer_indices = list(range(N_LAYERS))
    t_all = time.time()

    for i, hdf5_path in enumerate(hdf5_files):
        task_desc = task_desc_from_filename(hdf5_path)
        task_id = Path(hdf5_path).stem.replace("_demo", "")
        out_path = os.path.join(FEATURE_DIR, f"{task_id}.h5")

        if os.path.exists(out_path):
            print(f"[{i+1}/{len(hdf5_files)}] Skip {task_id} (exists)")
            continue

        print(f"\n[{i+1}/{len(hdf5_files)}] {task_desc}")
        t0 = time.time()

        prompt = f"In: What action should the robot take to {task_desc}?\nOut:"

        f = h5py.File(hdf5_path, "r")
        data = f["data"]
        demo_keys = sorted(data.keys(), key=lambda x: int(x.split("_")[1]))
        demo_keys = demo_keys[:MAX_DEMOS]

        out_f = h5py.File(out_path, "w")
        out_f.attrs["model_path"] = MODEL_PATH
        out_f.attrs["task"] = task_desc
        out_f.attrs["layers"] = np.array(layer_indices, dtype=np.int32)
        out_f.attrs["num_image_tokens"] = NUM_IMAGE_TOKENS

        total_frames = sum(data[dk]["obs"]["agentview_rgb"].shape[0] for dk in demo_keys)
        processed = 0

        for dk in demo_keys:
            images_ds = data[dk]["obs"]["agentview_rgb"]
            T = images_ds.shape[0]

            lp_list = []
            im_list = []

            for t0_idx in range(0, T, EXTRACT_BATCH):
                t1_idx = min(t0_idx + EXTRACT_BATCH, T)
                batch_imgs = [Image.fromarray(images_ds[t]) for t in range(t0_idx, t1_idx)]
                B = len(batch_imgs)

                inputs = processor(
                    text=[prompt] * B, images=batch_imgs, padding=True, return_tensors="pt"
                )
                inputs = {k: v.to(device) for k, v in inputs.items()}

                with torch.no_grad(), torch.amp.autocast("cuda", dtype=torch.bfloat16):
                    out = model(**inputs, output_hidden_states=True)
                hs_tuple = out.hidden_states

                lp_gpu = torch.stack([hs_tuple[li][:, -1, :] for li in layer_indices])
                im_gpu = torch.stack([
                    hs_tuple[li][:, 1:1+NUM_IMAGE_TOKENS, :].mean(dim=1)
                    for li in layer_indices
                ])
                lp_batch = lp_gpu.permute(1, 0, 2).cpu().half()
                im_batch = im_gpu.permute(1, 0, 2).cpu().half()
                del lp_gpu, im_gpu

                for b in range(B):
                    lp_list.append(lp_batch[b])
                    im_list.append(im_batch[b])

                del out, hs_tuple, inputs, lp_batch, im_batch
                processed += B

            lp_arr = torch.stack(lp_list).numpy()
            im_arr = torch.stack(im_list).numpy()
            g = out_f.create_group(dk)
            g.create_dataset("last_preaction", data=lp_arr, dtype="float16",
                             compression="gzip", compression_opts=4)
            g.create_dataset("image_mean", data=im_arr, dtype="float16",
                             compression="gzip", compression_opts=4)
            out_f.flush()
            del lp_list, im_list, lp_arr, im_arr

        f.close()
        out_f.close()

        sz = os.path.getsize(out_path) / 1024**3
        print(f"  {len(demo_keys)} demos, {total_frames} frames, {sz:.2f} GB, {time.time()-t0:.0f}s")

        gc.collect()
        torch.cuda.empty_cache()

    print(f"\nPhase 1 done in {(time.time()-t_all)/60:.1f} min")

    del model, processor
    gc.collect()
    torch.cuda.empty_cache()


# ─── Phase 2: Probe training ───


class ActionMLPProbe(nn.Module):
    def __init__(self, in_dim=INPUT_DIM, out_dim=7, hidden_dim=HIDDEN_DIM):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, out_dim),
        )

    def forward(self, x):
        return self.net(x)


def load_features_and_actions(feat_dir, layer):
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
                feat = np.asarray(ff[k]["image_mean"][:, layer, :], dtype=np.float32)
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
            x = torch.from_numpy(feat[:T-1])
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

    model = ActionMLPProbe().to(device)
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
            idx = perm[start:start+BATCH_SIZE]
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
        "n_train": len(X_tr),
        "n_val": len(X_val),
    }


def run_probes():
    device = torch.device(f"cuda:{GPU}")

    print("\n" + "=" * 60)
    print("Phase 2: Action Probe Training (llama2base, image_mean)")
    print(f"Features: {FEATURE_DIR}")
    print(f"Device: {device}")
    print("=" * 60)

    layer_results = {}
    t_all = time.time()

    for layer in range(N_LAYERS):
        t0 = time.time()
        task_data = load_features_and_actions(FEATURE_DIR, layer)
        X_tr, y_tr, X_val, y_val, val_tasks = build_train_val(task_data)
        metrics = train_and_eval(X_tr, y_tr, X_val, y_val, val_tasks, device)
        elapsed = time.time() - t0
        layer_results[f"layer_{layer}"] = metrics
        print(f"  L{layer}: mean_R2={metrics['mean_R2']:.4f}, "
              f"overall_R2={metrics['overall_R2']:.4f}, "
              f"ep={metrics['epochs_trained']}, {elapsed:.1f}s")
        del task_data, X_tr, y_tr, X_val, y_val
        torch.cuda.empty_cache()

    print(f"\nPhase 2 done in {(time.time()-t_all)/60:.1f} min")
    return layer_results


def find_peak(layer_results):
    best_layer, best_r2 = -1, -999
    for lk, metrics in layer_results.items():
        if metrics["mean_R2"] > best_r2:
            best_r2 = metrics["mean_R2"]
            best_layer = int(lk.split("_")[1])
    return {"layer": best_layer, "mean_R2": best_r2}


def main():
    t_start = time.time()

    # Phase 1
    extract_features()

    # Phase 2
    layer_results = run_probes()

    peak = find_peak(layer_results)
    print(f"\nPeak: L{peak['layer']} mean_R2={peak['mean_R2']:.4f}")

    # Load existing trained/untrained for comparison
    comparison = {}
    if os.path.exists(EXISTING_RESULTS):
        with open(EXISTING_RESULTS, "r") as f:
            existing = json.load(f)
        for cond in ["trained", "untrained"]:
            if cond in existing and "image_mean" in existing[cond]:
                cond_data = existing[cond]["image_mean"]
                comparison[cond] = {
                    lk: cond_data[lk]["mean_R2"]
                    for lk in cond_data
                }

    # Build output
    output = {
        "condition": "llama2base",
        "readout": "image_mean",
        "hyperparams": {
            "epochs": EPOCHS, "patience": PATIENCE, "lr": LR,
            "batch_size": BATCH_SIZE, "hidden": HIDDEN_DIM, "seed": SEED,
            "target": "next_action_a_{t+1}", "normalization": "z-score",
            "split": "80/20_per_task_by_demo_index",
            "model": "Linear(4096,256)->ReLU->Linear(256,7)",
        },
        "llama2base_image_mean": layer_results,
        "summary": {
            "llama2base_peak": peak,
        },
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    elapsed = time.time() - t_start

    # Print summary
    print("\n" + "=" * 60)
    print("=== Llama-2 Base Action Probe R² (image_mean) ===")
    print("=" * 60)

    key_layers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                  14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                  26, 27, 28, 29, 30, 31, 32]

    for l in key_layers:
        lk = f"layer_{l}"
        if lk in layer_results:
            r2 = layer_results[lk]["mean_R2"]
            tr_r2 = comparison.get("trained", {}).get(lk, None)
            un_r2 = comparison.get("untrained", {}).get(lk, None)
            line = f"L{l:2d}: llama2base={r2:.4f}"
            if tr_r2 is not None:
                line += f"  trained={tr_r2:.4f}"
            if un_r2 is not None:
                line += f"  untrained={un_r2:.4f}"
            print(line)

    print(f"\nPeak: L{peak['layer']} R²={peak['mean_R2']:.4f}")
    print(f"Total time: {elapsed/60:.1f} min")
    print(f"Results saved to {OUT_PATH}")


if __name__ == "__main__":
    main()
