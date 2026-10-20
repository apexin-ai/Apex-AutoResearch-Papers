"""L1 Head Ablation + Action Probe R² (50 demos version): measure how ablating L1
instruction-attending heads affects action-relevant information at different readout layers.
Includes 10,000-resample paired bootstrap CI and p-values.
"""

import argparse
import gc
import glob
import json
import os
import time

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path
from PIL import Image

NUM_IMAGE_TOKENS = 256
INST_START = 1 + NUM_IMAGE_TOKENS  # BOS(1) + image(256) = 257

INSTRUCTION_HEADS_24 = [0,1,2,4,7,8,10,11,12,14,15,16,17,18,19,20,22,23,25,26,27,29,30,31]

SEED = 42
BATCH_SIZE = 256
LR = 1e-3
EPOCHS = 50
PATIENCE = 5
HIDDEN_DIM = 256
INPUT_DIM = 4096
N_BOOTSTRAP = 10000


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--model_path", default="/root/autodl-tmp/vla-ssd/checkpoints/openvla-7b")
    p.add_argument("--data_dir", default="/root/autodl-tmp/vla-ssd/data/libero/libero_goal/")
    p.add_argument("--output", default="/root/autodl-tmp/vla-ssd/results/l1_head_ablation/action_probe_50demos.json")
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--demos_per_task", type=int, default=50)
    p.add_argument("--readout_layers", type=int, nargs="+", default=[1, 8, 13])
    p.add_argument("--condition", type=str, default=None)
    p.add_argument("--dry_run", action="store_true")
    return p.parse_args()


def task_desc_from_filename(fname):
    stem = Path(fname).stem.replace("_demo", "")
    return stem.replace("_", " ")


def install_ablation_hook(model, heads_to_ablate):
    import transformers.models.llama.modeling_llama as llama_mod
    from transformers.models.llama.modeling_llama import repeat_kv

    layer1_attn = model.language_model.model.layers[1].self_attn
    layer1_attn._ablate_heads = heads_to_ablate

    original_fn = llama_mod.eager_attention_forward

    def ablated_eager_attention_forward(module, query, key, value, attention_mask,
                                        scaling, dropout=0.0, **kwargs):
        key_states = repeat_kv(key, module.num_key_value_groups)
        value_states = repeat_kv(value, module.num_key_value_groups)

        attn_weights = torch.matmul(query, key_states.transpose(2, 3)) * scaling
        if attention_mask is not None:
            causal_mask = attention_mask[:, :, :, :key_states.shape[-2]]
            attn_weights = attn_weights + causal_mask

        attn_weights = nn.functional.softmax(attn_weights, dim=-1, dtype=torch.float32).to(query.dtype)
        attn_weights = nn.functional.dropout(attn_weights, p=dropout, training=module.training)

        if hasattr(module, '_ablate_heads') and module._ablate_heads is not None:
            seq_len = attn_weights.shape[-1]
            if INST_START < seq_len:
                attn_weights[:, module._ablate_heads, :, INST_START:] = 0.0
                row_sums = attn_weights.sum(dim=-1, keepdim=True).clamp(min=1e-9)
                attn_weights = attn_weights / row_sums

        attn_output = torch.matmul(attn_weights, value_states)
        attn_output = attn_output.transpose(1, 2).contiguous()
        return attn_output, attn_weights

    llama_mod.eager_attention_forward = ablated_eager_attention_forward
    return original_fn


def remove_ablation_hook(model, original_fn):
    import transformers.models.llama.modeling_llama as llama_mod
    llama_mod.eager_attention_forward = original_fn
    layer1_attn = model.language_model.model.layers[1].self_attn
    layer1_attn._ablate_heads = None


def load_model(model_path, device):
    from transformers import AutoModelForVision2Seq, AutoProcessor

    processor = AutoProcessor.from_pretrained(
        model_path, trust_remote_code=True, local_files_only=True
    )
    model = AutoModelForVision2Seq.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        trust_remote_code=True,
        low_cpu_mem_usage=True,
        attn_implementation="eager",
        local_files_only=True,
    )
    model = model.to(device).eval()
    print(f"Model loaded on {device}")
    return model, processor


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


@torch.no_grad()
def extract_features_for_task(model, processor, images, instruction, readout_layers, device):
    hooks = []
    hook_outputs = {}

    def make_hook(layer_idx):
        def hook_fn(module, input, output):
            if isinstance(output, tuple):
                hidden = output[0]
            else:
                hidden = output
            hook_outputs[layer_idx] = hidden[:, -1, :].detach().cpu().float()
        return hook_fn

    for l in readout_layers:
        h = model.language_model.model.layers[l].register_forward_hook(make_hook(l))
        hooks.append(h)

    features = {l: [] for l in readout_layers}
    prompt = f"In: What action should the robot take to {instruction}?\nOut:"

    try:
        for img_idx, image in enumerate(images):
            inputs = processor(text=[prompt], images=[image], return_tensors="pt")
            inputs = {k: v.to(device) for k, v in inputs.items()}

            with torch.amp.autocast("cuda", dtype=torch.float16):
                model(**inputs)

            for l in readout_layers:
                features[l].append(hook_outputs[l].squeeze(0).numpy())

            del inputs
            hook_outputs.clear()

            if (img_idx + 1) % 50 == 0:
                print(f"    {img_idx + 1}/{len(images)} frames")
    finally:
        for h in hooks:
            h.remove()

    for l in readout_layers:
        features[l] = np.array(features[l])

    return features


def build_train_val(task_features, task_actions, task_names, readout_layers):
    """80/20 per-task split, build (x_t, a_{t+1}) pairs for each layer."""
    result = {}
    for l in readout_layers:
        X_tr_list, y_tr_list = [], []
        X_val_list, y_val_list, val_tasks = [], [], []

        for task_idx, task in enumerate(task_names):
            feats = task_features[task][l]
            acts = task_actions[task]
            n_demos = len(feats)
            n_train = int(n_demos * 0.8)

            for i in range(n_demos):
                feat = feats[i]
                act = acts[i]
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

        result[l] = (
            torch.cat(X_tr_list), torch.cat(y_tr_list),
            torch.cat(X_val_list), torch.cat(y_val_list), val_tasks
        )
    return result


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
            idx = perm[start:start + BATCH_SIZE]
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

    per_dim_r2 = []
    for d in range(7):
        ss_res = np.sum((y_true[:, d] - pred_np[:, d]) ** 2)
        ss_tot = np.sum((y_true[:, d] - y_true[:, d].mean()) ** 2)
        per_dim_r2.append(float(1 - ss_res / ss_tot) if ss_tot > 0 else 0.0)

    ss_res = np.sum((y_true - pred_np) ** 2)
    ss_tot = np.sum((y_true - y_true.mean(axis=0)) ** 2)
    overall_r2 = float(1 - ss_res / ss_tot)

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
        "mean_R2": round(mean_r2, 4),
        "overall_R2": round(overall_r2, 4),
        "per_dim_R2": [round(x, 4) for x in per_dim_r2],
        "per_task_R2": {k: round(v, 4) for k, v in per_task_r2.items()},
        "epochs_trained": epochs_trained,
        "n_train": len(X_tr),
        "n_val": len(X_val),
    }


def bootstrap_paired_ci(all_results, n_bootstrap=N_BOOTSTRAP, seed=SEED):
    """Paired bootstrap CI (resampling tasks) for R2 differences.

    For each layer, compares baseline vs ablate_all24 and baseline vs ablate_all32.
    Returns 95% CI and two-sided p-value for the mean R2 difference.
    """
    rng = np.random.RandomState(seed)
    bootstrap_results = {}

    if "baseline" not in all_results:
        return bootstrap_results

    baseline_tasks = all_results["baseline"]

    for ablation_name in ["ablate_all24", "ablate_all32"]:
        if ablation_name not in all_results:
            continue

        ablation_tasks = all_results[ablation_name]
        comparison_key = f"baseline_vs_{ablation_name}"
        bootstrap_results[comparison_key] = {}

        for layer_key in baseline_tasks:
            bl_per_task = baseline_tasks[layer_key]["per_task_R2"]
            ab_per_task = ablation_tasks[layer_key]["per_task_R2"]

            tasks = sorted(bl_per_task.keys())
            bl_vals = np.array([bl_per_task[t] for t in tasks])
            ab_vals = np.array([ab_per_task[t] for t in tasks])
            diffs = ab_vals - bl_vals  # positive = ablation higher

            n_tasks = len(tasks)
            observed_mean_diff = float(np.mean(diffs))

            boot_diffs = np.zeros(n_bootstrap)
            for b in range(n_bootstrap):
                idx = rng.randint(0, n_tasks, size=n_tasks)
                boot_diffs[b] = np.mean(diffs[idx])

            ci_lo = float(np.percentile(boot_diffs, 2.5))
            ci_hi = float(np.percentile(boot_diffs, 97.5))

            # two-sided p-value: proportion of bootstrap samples on the other side of zero
            if observed_mean_diff >= 0:
                p_val = float(np.mean(boot_diffs <= 0)) * 2
            else:
                p_val = float(np.mean(boot_diffs >= 0)) * 2
            p_val = min(p_val, 1.0)

            boot_bl_means = np.zeros(n_bootstrap)
            boot_ab_means = np.zeros(n_bootstrap)
            for b in range(n_bootstrap):
                idx = rng.randint(0, n_tasks, size=n_tasks)
                boot_bl_means[b] = np.mean(bl_vals[idx])
                boot_ab_means[b] = np.mean(ab_vals[idx])

            bootstrap_results[comparison_key][layer_key] = {
                "observed_diff": round(observed_mean_diff, 4),
                "CI_95": [round(ci_lo, 4), round(ci_hi, 4)],
                "p_value": round(p_val, 4),
                "baseline_mean_R2": round(float(np.mean(bl_vals)), 4),
                "baseline_CI_95": [round(float(np.percentile(boot_bl_means, 2.5)), 4),
                                   round(float(np.percentile(boot_bl_means, 97.5)), 4)],
                "ablation_mean_R2": round(float(np.mean(ab_vals)), 4),
                "ablation_CI_95": [round(float(np.percentile(boot_ab_means, 2.5)), 4),
                                   round(float(np.percentile(boot_ab_means, 97.5)), 4)],
                "n_tasks": n_tasks,
                "per_task_diffs": {t: round(float(diffs[i]), 4) for i, t in enumerate(tasks)},
            }

    return bootstrap_results


def main():
    args = parse_args()
    device = torch.device(f"cuda:{args.gpu}")
    readout_layers = args.readout_layers

    print("=== L1 Head Ablation: Action Probe R² (50 demos) ===")
    print(f"Model: {args.model_path}")
    print(f"Data: {args.data_dir}")
    print(f"Readout layers: {readout_layers}")
    print(f"Demos per task: {args.demos_per_task}")
    print(f"Output: {args.output}")

    hdf5_files = sorted(glob.glob(os.path.join(args.data_dir, "*.hdf5")))
    n_tasks = len(hdf5_files)
    task_names = [task_desc_from_filename(f) for f in hdf5_files]
    print(f"Tasks: {n_tasks}")
    for i, name in enumerate(task_names):
        print(f"  [{i}] {name}")

    conditions = {
        "baseline": None,
        "ablate_all24": INSTRUCTION_HEADS_24,
        "ablate_all32": list(range(32)),
    }

    if args.condition:
        if args.condition not in conditions:
            raise ValueError(f"Unknown condition: {args.condition}. Available: {list(conditions.keys())}")
        conditions = {args.condition: conditions[args.condition]}

    model, processor = load_model(args.model_path, device)

    import transformers.models.llama.modeling_llama as llama_mod
    original_eager_fn = llama_mod.eager_attention_forward

    all_results = {}

    for cond_name, heads in conditions.items():
        print(f"\n{'='*60}")
        print(f"Condition: {cond_name} (heads={heads})")
        print(f"{'='*60}")
        t0 = time.time()

        if heads is not None:
            install_ablation_hook(model, heads)
        else:
            remove_ablation_hook(model, original_eager_fn)

        task_features = {}
        task_actions = {}

        for task_idx, (hdf5_path, task_name) in enumerate(zip(hdf5_files, task_names)):
            print(f"\n  Task {task_idx}: {task_name}")
            f = h5py.File(hdf5_path, "r")
            data = f["data"]
            demo_keys = sorted(data.keys(), key=lambda x: int(x.split("_")[1]))
            demo_keys = demo_keys[:args.demos_per_task]

            all_images = []
            demo_boundaries = []
            demo_actions = []

            for dk in demo_keys:
                imgs_np = data[dk]["obs"]["agentview_rgb"][:]
                acts_np = np.asarray(data[dk]["actions"], dtype=np.float32)

                if args.dry_run:
                    imgs_np = imgs_np[:5]
                    acts_np = acts_np[:5]

                pil_images = [Image.fromarray(img) for img in imgs_np]
                all_images.extend(pil_images)
                demo_boundaries.append(len(pil_images))
                demo_actions.append(acts_np)

            f.close()

            total_frames = len(all_images)
            print(f"    {len(demo_keys)} demos, {total_frames} frames")

            feats = extract_features_for_task(
                model, processor, all_images, task_name, readout_layers, device
            )

            per_demo_feats = {l: [] for l in readout_layers}
            offset = 0
            for boundary in demo_boundaries:
                for l in readout_layers:
                    per_demo_feats[l].append(feats[l][offset:offset + boundary])
                offset += boundary

            task_features[task_name] = per_demo_feats
            task_actions[task_name] = demo_actions

            del all_images, feats
            gc.collect()
            torch.cuda.empty_cache()

        print(f"\n  Training probes...")
        layer_data = build_train_val(task_features, task_actions, task_names, readout_layers)

        cond_results = {}
        for l in readout_layers:
            X_tr, y_tr, X_val, y_val, val_tasks = layer_data[l]
            print(f"    L{l}: train={len(X_tr)}, val={len(X_val)}")
            metrics = train_and_eval(X_tr, y_tr, X_val, y_val, val_tasks, device)
            cond_results[f"L{l}"] = metrics
            print(f"    L{l}: mean_R2={metrics['mean_R2']}, overall_R2={metrics['overall_R2']}, "
                  f"epochs={metrics['epochs_trained']}")

        elapsed = time.time() - t0
        print(f"  Condition {cond_name} done in {elapsed/60:.1f} min")
        all_results[cond_name] = cond_results

        remove_ablation_hook(model, original_eager_fn)
        del task_features, task_actions, layer_data
        gc.collect()
        torch.cuda.empty_cache()

    # Bootstrap CI
    print(f"\n{'='*60}")
    print("Running paired bootstrap CI (10,000 resamples)...")
    print(f"{'='*60}")
    bootstrap = bootstrap_paired_ci(all_results)

    for comp_key, layers in bootstrap.items():
        print(f"\n  {comp_key}:")
        for lk, stats in layers.items():
            print(f"    {lk}: diff={stats['observed_diff']}, "
                  f"CI=[{stats['CI_95'][0]}, {stats['CI_95'][1]}], "
                  f"p={stats['p_value']}")

    r2_summary = {}
    for cond in all_results:
        r2_summary[cond] = {}
        for lk in all_results[cond]:
            r2_summary[cond][lk] = all_results[cond][lk]["mean_R2"]

    output = {
        "action_probe_R2": r2_summary,
        "bootstrap_paired_CI": bootstrap,
        "detailed_results": all_results,
        "metadata": {
            "probe": "MLP(4096,256,7)",
            "optimizer": f"Adam lr={LR}",
            "epochs": EPOCHS,
            "patience": PATIENCE,
            "batch_size": BATCH_SIZE,
            "seed": SEED,
            "target": "next_action a_{t+1} from feature at time t",
            "normalization": "z-score (train mean/std)",
            "split": "80/20 per-task by demo index",
            "readout_layers": readout_layers,
            "demos_per_task": args.demos_per_task,
            "n_tasks": n_tasks,
            "n_bootstrap": N_BOOTSTRAP,
            "checkpoint": args.model_path,
            "instruction_heads_24": INSTRUCTION_HEADS_24,
        }
    }

    os.makedirs(os.path.dirname(args.output), exist_ok=True)
    with open(args.output, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*60}")
    print("SUMMARY: Action Probe R² by condition and layer")
    print(f"{'='*60}")
    print(json.dumps(r2_summary, indent=2))
    print(f"\nResults saved to {args.output}")


if __name__ == "__main__":
    main()
