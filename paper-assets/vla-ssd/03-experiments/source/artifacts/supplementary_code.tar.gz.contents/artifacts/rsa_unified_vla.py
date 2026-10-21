"""Unified RSA recalculation for all VLA conditions using Method B.

Method B (reference: rsa_clip.py):
  - rep_dist: cosine
  - act_dist: euclidean (L2)
  - N_SAMPLE: 20 (np.linspace subsample)
  - pairing: within-task itertools.combinations
  - aggregation: per-task Spearman -> mean + bootstrap CI
  - seed: 42
"""

import json
import os
import time
from pathlib import Path

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
from scipy.spatial.distance import pdist
from scipy.stats import spearmanr

FEAT_BASE = Path("/root/autodl-tmp/vla-ssd/features")
DATA_DIR = Path("/root/autodl-tmp/vla-ssd/data/libero/libero_goal")
OUT_PATH = Path("/root/autodl-tmp/vla-ssd/results/rsa/unified_rsa_results.json")

TASKS = [
    "open_the_middle_drawer_of_the_cabinet",
    "open_the_top_drawer_and_put_the_bowl_inside",
    "push_the_plate_to_the_front_of_the_stove",
    "put_the_bowl_on_the_plate",
    "put_the_bowl_on_the_stove",
    "put_the_bowl_on_top_of_the_cabinet",
    "put_the_cream_cheese_in_the_bowl",
    "put_the_wine_bottle_on_the_rack",
    "put_the_wine_bottle_on_top_of_the_cabinet",
    "turn_on_the_stove",
]

FEAT_DIRS = {
    "trained_with_inst": FEAT_BASE / "trained_libero_goal",
    "untrained_with_inst": FEAT_BASE / "untrained_libero_goal",
    "trained_no_inst": FEAT_BASE / "trained_libero_goal_no_inst",
    "untrained_no_inst": FEAT_BASE / "untrained_libero_goal_no_inst",
    "random_s0": FEAT_BASE / "trained_libero_goal_random_s0",
    "shuffled": FEAT_BASE / "trained_libero_goal_shuffled",
}

CONDITION_AGGS = {
    "trained_with_inst": ["image_mean", "last_preaction"],
    "untrained_with_inst": ["image_mean", "last_preaction"],
    "trained_no_inst": ["image_mean"],
    "untrained_no_inst": ["image_mean"],
    "random_s0": ["image_mean"],
    "shuffled": ["image_mean"],
}

N_LAYERS = 33
N_SAMPLE = 20


def subsample_to_length(arr, target_len):
    T = arr.shape[0]
    if T <= target_len:
        return arr
    idx = np.linspace(0, T - 1, target_len, dtype=int)
    return arr[idx]


def load_actions(task):
    path = DATA_DIR / f"{task}_demo.hdf5"
    result = {}
    with h5py.File(path, "r") as f:
        for key in f["data"].keys():
            if key.startswith("demo_"):
                did = int(key.split("_")[1])
                result[did] = f[f"data/{key}/actions"][:].astype(np.float32)
    return result


def bootstrap_ci(values, n_boot=1000, ci=0.95):
    values = np.array(values)
    boot_means = [
        np.mean(np.random.choice(values, len(values), replace=True))
        for _ in range(n_boot)
    ]
    lo = np.percentile(boot_means, (1 - ci) / 2 * 100)
    hi = np.percentile(boot_means, (1 + ci) / 2 * 100)
    return float(np.mean(values)), float(lo), float(hi)


def compute_rsa_all_layers(feat_dir, task, aggs, actions_cache):
    if task not in actions_cache:
        actions_cache[task] = load_actions(task)
    actions = actions_cache[task]

    results = {}

    feat_path = feat_dir / f"{task}.h5"
    if not feat_path.exists():
        for agg in aggs:
            results[agg] = {layer: None for layer in range(N_LAYERS)}
        return results

    with h5py.File(feat_path, "r") as f:
        demo_keys = [k for k in f.keys() if k.startswith("demo_")]
        common_dids = sorted(
            set(int(k.split("_")[1]) for k in demo_keys) & set(actions.keys())
        )

        if len(common_dids) < 2:
            for agg in aggs:
                results[agg] = {layer: None for layer in range(N_LAYERS)}
            return results

        n = len(common_dids)
        n_pairs = n * (n - 1) // 2

        sub_acts = np.stack(
            [subsample_to_length(actions[d], N_SAMPLE) for d in common_dids]
        )
        act_dists = np.zeros(n_pairs)
        for t in range(sub_acts.shape[1]):
            act_dists += pdist(sub_acts[:, t, :], metric="euclidean")
        act_dists /= sub_acts.shape[1]

        for agg in aggs:
            sub_feats = []
            for did in common_dids:
                raw = f[f"demo_{did}/{agg}"][:]
                sub = subsample_to_length(raw, N_SAMPLE).astype(np.float32)
                sub_feats.append(sub)

            feat_stack = np.stack(sub_feats)  # (n, 20, 33, 4096)
            del sub_feats

            results[agg] = {}
            for layer in range(N_LAYERS):
                feat_layer = feat_stack[:, :, layer, :]  # (n, 20, 4096)

                rep_dists = np.zeros(n_pairs)
                for t in range(feat_layer.shape[1]):
                    rep_dists += pdist(feat_layer[:, t, :], metric="cosine")
                rep_dists /= feat_layer.shape[1]

                valid = ~(np.isnan(rep_dists) | np.isnan(act_dists))
                if valid.sum() < 3:
                    results[agg][layer] = None
                else:
                    rsa, _ = spearmanr(rep_dists[valid], act_dists[valid])
                    results[agg][layer] = float(rsa)

            del feat_stack

    return results


def main():
    np.random.seed(42)
    t0 = time.time()

    actions_cache = {}
    all_results = {}

    for cond, feat_dir in FEAT_DIRS.items():
        if not feat_dir.exists():
            print(f"SKIP {cond}: {feat_dir} not found")
            continue

        aggs = CONDITION_AGGS[cond]
        cond_results = {}

        for agg in aggs:
            print(f"\n=== {cond} / {agg} ===")
            layer_data = {layer: {"per_task": {}, "rsa_values": []} for layer in range(N_LAYERS)}

            for task in TASKS:
                task_t = time.time()
                rsa_by_layer = compute_rsa_all_layers(feat_dir, task, [agg], actions_cache)

                for layer in range(N_LAYERS):
                    val = rsa_by_layer[agg][layer]
                    layer_data[layer]["per_task"][task] = (
                        round(val, 4) if val is not None else None
                    )
                    if val is not None:
                        layer_data[layer]["rsa_values"].append(val)

                print(f"  {task}: {time.time()-task_t:.1f}s")

            layer_results = {}
            for layer in range(N_LAYERS):
                vals = layer_data[layer]["rsa_values"]
                if vals:
                    mean_rsa, ci_lo, ci_hi = bootstrap_ci(vals)
                    layer_results[f"layer_{layer}"] = {
                        "mean_rsa": round(mean_rsa, 4),
                        "ci95": [round(ci_lo, 4), round(ci_hi, 4)],
                        "per_task": layer_data[layer]["per_task"],
                    }
                else:
                    layer_results[f"layer_{layer}"] = {
                        "mean_rsa": None,
                        "per_task": layer_data[layer]["per_task"],
                    }

            cond_results[agg] = layer_results

            valid_layers = {
                k: v["mean_rsa"]
                for k, v in layer_results.items()
                if v["mean_rsa"] is not None
            }
            if valid_layers:
                best_k = max(valid_layers, key=valid_layers.get)
                best_l = int(best_k.split("_")[1])
                best_r = valid_layers[best_k]
                print(f"  BEST: layer {best_l}, RSA = {best_r:.4f}")

        all_results[cond] = cond_results

    # Build summary
    summary = {}
    for cond, cond_res in all_results.items():
        for agg, layer_res in cond_res.items():
            valid = {
                k: v["mean_rsa"]
                for k, v in layer_res.items()
                if v["mean_rsa"] is not None
            }
            if valid:
                best_k = max(valid, key=valid.get)
                best_l = int(best_k.split("_")[1])
                best_r = valid[best_k]
                summary[f"{cond}_{agg}_best"] = {"layer": best_l, "rsa": best_r}

    # Build instruction_control section
    ic_mapping = {
        "normal": "trained_with_inst",
        "no_inst": "trained_no_inst",
        "random_s0": "random_s0",
        "shuffled": "shuffled",
    }
    instruction_control = {}
    for ic_name, cond_name in ic_mapping.items():
        if cond_name in all_results and "image_mean" in all_results[cond_name]:
            layer_res = all_results[cond_name]["image_mean"]
            valid = {
                k: v["mean_rsa"]
                for k, v in layer_res.items()
                if v["mean_rsa"] is not None
            }
            if valid:
                best_k = max(valid, key=valid.get)
                best_l = int(best_k.split("_")[1])
                best_r = valid[best_k]
                instruction_control[ic_name] = {
                    "best_layer": best_l,
                    "best_rsa": best_r,
                    "all_layers": {k: v["mean_rsa"] for k, v in layer_res.items()},
                }

    output = {
        "method": "B (within-task + cosine rep dist + euclidean action dist + full trajectory)",
        "rep_distance": "cosine",
        "action_distance": "euclidean (L2)",
        "n_sample": N_SAMPLE,
        "n_layers": N_LAYERS,
        "n_tasks": len(TASKS),
        "seed": 42,
        "conditions": all_results,
        "instruction_control": instruction_control,
        "summary": summary,
        "note_empty_condition": "No 'empty' instruction control features found. 'no_inst' (trained_no_inst) used as equivalent.",
        "elapsed_seconds": round(time.time() - t0, 1),
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n{'='*60}")
    print(f"Saved to {OUT_PATH}")
    print(f"Total time: {time.time()-t0:.1f}s\n")

    print("Summary (best layer per condition):")
    for k, v in summary.items():
        print(f"  {k}: layer {v['layer']}, RSA = {v['rsa']:.4f}")

    print(f"\nInstruction Control:")
    for k, v in instruction_control.items():
        print(f"  {k}: best layer {v['best_layer']}, RSA = {v['best_rsa']:.4f}")


if __name__ == "__main__":
    main()
