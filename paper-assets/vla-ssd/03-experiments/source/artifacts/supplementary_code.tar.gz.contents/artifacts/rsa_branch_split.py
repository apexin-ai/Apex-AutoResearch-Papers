"""Branch-split RSA: DINOv2 branch vs SigLIP branch of Prismatic fused backbone.

Reads 2176d projector input features (patch_mean), splits into
DINOv2 (first 1024d) and SigLIP (last 1152d), computes RSA against
action dissimilarity.

Method B: within-task pairing, cosine rep distance, euclidean action
distance, full trajectory (subsampled to 20 frames), Spearman rank
correlation, mean across tasks.
"""

import itertools
import json
import os
from pathlib import Path

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
from scipy.spatial.distance import cosine as cosine_dist
from scipy.stats import spearmanr

FEAT_DIR = Path("/root/autodl-tmp/vla-ssd/features/fused_backbone_libero_goal")
DATA_DIR = Path("/root/autodl-tmp/vla-ssd/data/libero/libero_goal")
OUT_PATH = Path("/root/autodl-tmp/vla-ssd/results/rsa/rsa_branch_split.json")

DINO_DIM = 1024
SIGLIP_DIM = 1152

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

N_SAMPLE = 20


def subsample_to_length(arr, target_len):
    T = arr.shape[0]
    if T <= target_len:
        return arr
    idx = np.linspace(0, T - 1, target_len, dtype=int)
    return arr[idx]


def mean_cosine_distance(feat_a, feat_b):
    a = subsample_to_length(feat_a, N_SAMPLE)
    b = subsample_to_length(feat_b, N_SAMPLE)
    n = min(len(a), len(b))
    return float(np.mean([cosine_dist(a[i], b[i]) for i in range(n)]))


def mean_action_distance(act_a, act_b):
    a = subsample_to_length(act_a, N_SAMPLE)
    b = subsample_to_length(act_b, N_SAMPLE)
    n = min(len(a), len(b))
    return float(np.mean([np.linalg.norm(a[i] - b[i]) for i in range(n)]))


def load_features(task, dim_slice=None):
    path = FEAT_DIR / f"{task}.h5"
    result = {}
    with h5py.File(path, "r") as f:
        for key in f.keys():
            if key.startswith("demo_"):
                did = int(key.split("_")[1])
                feat = f[key]["patch_mean"][:].astype(np.float32)
                if dim_slice is not None:
                    feat = feat[:, dim_slice]
                result[did] = feat
    return result


def load_actions(task):
    path = DATA_DIR / f"{task}_demo.hdf5"
    result = {}
    with h5py.File(path, "r") as f:
        for key in f["data"].keys():
            if key.startswith("demo_"):
                did = int(key.split("_")[1])
                result[did] = f[f"data/{key}/actions"][:].astype(np.float32)
    return result


def compute_rsa(feats, actions):
    common = sorted(set(feats.keys()) & set(actions.keys()))
    if len(common) < 2:
        return None
    pairs = list(itertools.combinations(common, 2))
    rep_dists = [mean_cosine_distance(feats[a], feats[b]) for a, b in pairs]
    act_dists = [mean_action_distance(actions[a], actions[b]) for a, b in pairs]
    rsa, _ = spearmanr(rep_dists, act_dists)
    return float(rsa)


def bootstrap_ci(values, n_boot=1000, ci=0.95):
    values = np.array(values)
    boot_means = [np.mean(np.random.choice(values, len(values), replace=True))
                  for _ in range(n_boot)]
    lo = np.percentile(boot_means, (1 - ci) / 2 * 100)
    hi = np.percentile(boot_means, (1 + ci) / 2 * 100)
    return float(np.mean(values)), float(lo), float(hi)


def run_rsa(label, dim_slice=None):
    per_task = {}
    rsa_values = []

    for task in TASKS:
        feats = load_features(task, dim_slice)
        actions = load_actions(task)
        rsa = compute_rsa(feats, actions)
        per_task[task] = rsa
        if rsa is not None:
            rsa_values.append(rsa)
        tag = f"{rsa:.4f}" if rsa is not None else "SKIP"
        print(f"  {task}: {tag}")

    if not rsa_values:
        return None

    mean_rsa, ci_lo, ci_hi = bootstrap_ci(rsa_values)
    std_rsa = float(np.std(rsa_values))
    print(f"\n  {label} RSA: {mean_rsa:.4f} +/- {std_rsa:.4f} [{ci_lo:.4f}, {ci_hi:.4f}]")
    return {
        "rsa": round(mean_rsa, 4),
        "std": round(std_rsa, 4),
        "ci95": [round(ci_lo, 4), round(ci_hi, 4)],
        "per_task": {k: round(v, 4) if v is not None else None for k, v in per_task.items()},
    }


def main():
    np.random.seed(42)

    results = {}

    print("\n--- DINOv2 branch (first 1024d) ---")
    results["dinov2_branch"] = run_rsa("DINOv2_branch", slice(0, DINO_DIM))

    print("\n--- SigLIP branch (last 1152d) ---")
    results["siglip_branch"] = run_rsa("SigLIP_branch", slice(DINO_DIM, None))

    print("\n--- Fused 2176d (sanity check) ---")
    results["fused_2176d"] = run_rsa("Fused_2176d", None)

    comparison = {
        "dinov2_branch": results["dinov2_branch"]["rsa"] if results["dinov2_branch"] else None,
        "siglip_branch": results["siglip_branch"]["rsa"] if results["siglip_branch"] else None,
        "fused_2176d": results["fused_2176d"]["rsa"] if results["fused_2176d"] else None,
        "fused_projector_4096d": 0.615,
        "standalone_dino_cls": 0.692,
        "standalone_dino_patch_mean": 0.631,
        "standalone_clip_patch_mean": 0.557,
    }

    output = {
        "experiment": "branch_split_rsa",
        "method": "within-task, cosine rep dist, euclidean action dist, N=20, Spearman",
        "concat_order": "DINOv2 (0:1024) | SigLIP (1024:2176)",
        "results": results,
        "comparison": comparison,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nComparison:")
    for k, v in comparison.items():
        print(f"  {k:30s}: {v}")
    print(f"\nSaved to {OUT_PATH}")


if __name__ == "__main__":
    main()
