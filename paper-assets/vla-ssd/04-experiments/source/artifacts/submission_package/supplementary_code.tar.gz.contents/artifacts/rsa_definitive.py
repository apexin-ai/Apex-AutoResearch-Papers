#!/usr/bin/env python3
"""
Definitive RSA calculation — all models, unified method B.
50 demos/task, within-task pairing, euclidean action distance,
cosine rep distance, N_SAMPLE=20, per-task mean +/- std + bootstrap CI.
"""
# --- Path configuration (set env vars to override defaults) ---
import os as _os
PROJECT_ROOT = _os.environ.get("VLA_SSD_ROOT", ".")
LIBERO_ROOT = _os.environ.get("LIBERO_ROOT", "./LIBERO")
# ---

import itertools
import json
import os
import sys
import time
from pathlib import Path

os.environ["HDF5_USE_FILE_LOCKING"] = "FALSE"

import h5py
import numpy as np
from scipy.stats import spearmanr, ttest_rel

FEAT_BASE = Path(f"{PROJECT_ROOT}/features")
DATA_DIR = Path(f"{PROJECT_ROOT}/data/libero/libero_goal")
OUT_JSON = Path(f"{PROJECT_ROOT}/results/rsa/rsa_definitive.json")

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
N_BOOTSTRAP = 1000
RNG_SEED = 42
N_LAYERS = 33

# ── Non-VLA feature configs ────────────────────────────────────────────

SINGLE_LAYER_CONFIGS = {
    "clip_cls": {
        "dir": "clip_libero_goal", "format": "traj", "key": "cls_token",
        "desc": "CLIP ViT-L/14 [CLS] token",
    },
    "clip_patch_mean": {
        "dir": "clip_libero_goal", "format": "traj", "key": "patch_mean",
        "desc": "CLIP ViT-L/14 patch spatial mean",
    },
    "dino_cls": {
        "dir": "dinov2_libero_goal", "format": "traj", "key": "cls_token",
        "desc": "DINOv2 ViT-L/14 [CLS] token",
    },
    "dino_patch_mean": {
        "dir": "dinov2_libero_goal", "format": "traj", "key": "patch_mean",
        "desc": "DINOv2 ViT-L/14 patch spatial mean",
    },
    "fused_backbone": {
        "dir": "fused_backbone_libero_goal", "format": "demo", "key": "patch_mean",
        "desc": "DinoSigLIP fused backbone patch mean (2176-d, pre-projector)",
    },
    "siglip_projector": {
        "dir": "siglip_only_libero_goal", "format": "demo", "key": "last_preaction",
        "desc": "SigLIP projected features (4096-d, post-projector spatial mean)",
    },
}

# ── VLA model configs ──────────────────────────────────────────────────

VLA_CONFIGS = {
    "vla_trained": {
        "dir": "trained_libero_goal",
        "desc": "OpenVLA trained, with instruction",
    },
    "vla_trained_no_inst": {
        "dir": "trained_libero_goal_no_inst",
        "desc": "OpenVLA trained, no instruction",
    },
    "vla_untrained": {
        "dir": "untrained_libero_goal",
        "desc": "OpenVLA untrained, with instruction",
    },
    "vla_untrained_no_inst": {
        "dir": "untrained_libero_goal_no_inst",
        "desc": "OpenVLA untrained, no instruction",
    },
}

# ── Instruction control configs ────────────────────────────────────────

INST_CTRL_CONFIGS = {
    "inst_normal": {
        "dir": "trained_libero_goal",
        "desc": "Normal instruction",
    },
    "inst_random": {
        "dir": "trained_libero_goal_random_s0",
        "desc": "Random instruction (seed 0)",
    },
    "inst_shuffled": {
        "dir": "trained_libero_goal_shuffled",
        "desc": "Shuffled instruction",
    },
    "inst_no_inst": {
        "dir": "trained_libero_goal_no_inst",
        "desc": "No instruction",
    },
}


# ── Core RSA functions (matching rsa_clip.py methodology) ──────────────

def subsample_to_length(arr, target_len):
    T = arr.shape[0]
    if T <= target_len:
        return arr
    idx = np.linspace(0, T - 1, target_len, dtype=int)
    return arr[idx]


def mean_cosine_distance(feat_a, feat_b):
    a = subsample_to_length(feat_a, N_SAMPLE).astype(np.float64)
    b = subsample_to_length(feat_b, N_SAMPLE).astype(np.float64)
    n = min(len(a), len(b))
    a, b = a[:n], b[:n]
    dot = np.einsum('ij,ij->i', a, b)
    norm_a = np.linalg.norm(a, axis=1)
    norm_b = np.linalg.norm(b, axis=1)
    denom = norm_a * norm_b
    valid = denom > 0
    cos_dist = np.ones(n)
    cos_dist[valid] = 1.0 - dot[valid] / denom[valid]
    return float(np.mean(cos_dist))


def mean_action_distance(act_a, act_b):
    a = subsample_to_length(act_a, N_SAMPLE).astype(np.float64)
    b = subsample_to_length(act_b, N_SAMPLE).astype(np.float64)
    n = min(len(a), len(b))
    return float(np.mean(np.linalg.norm(a[:n] - b[:n], axis=1)))


def compute_task_rsa(feat_dict, act_dict):
    common = sorted(set(feat_dict.keys()) & set(act_dict.keys()))
    if len(common) < 2:
        return None
    pairs = list(itertools.combinations(common, 2))
    rep_dists = [mean_cosine_distance(feat_dict[a], feat_dict[b]) for a, b in pairs]
    act_dists = [mean_action_distance(act_dict[a], act_dict[b]) for a, b in pairs]
    rho, _ = spearmanr(rep_dists, act_dists)
    if np.isnan(rho):
        return None
    return float(rho)


# ── Loading functions ──────────────────────────────────────────────────

_action_cache = {}


def load_actions(task):
    if task in _action_cache:
        return _action_cache[task]
    path = DATA_DIR / f"{task}_demo.hdf5"
    result = {}
    with h5py.File(path, "r") as f:
        for key in f["data"].keys():
            if key.startswith("demo_"):
                did = int(key.split("_")[1])
                result[did] = f[f"data/{key}/actions"][:].astype(np.float32)
    _action_cache[task] = result
    return result


def load_features_traj(feat_dir, task, feature_key):
    path = feat_dir / f"{task}.h5"
    result = {}
    with h5py.File(path, "r") as f:
        for key in f.keys():
            if key.startswith("traj_"):
                did = int(key.split("_")[1])
                result[did] = f[key][feature_key][:].astype(np.float32)
    return result


def load_features_demo(feat_dir, task, feature_key):
    path = feat_dir / f"{task}.h5"
    result = {}
    with h5py.File(path, "r") as f:
        for key in f.keys():
            if key.startswith("demo"):
                did = int(key.replace("demo_", "").replace("demo", ""))
                result[did] = f[key][feature_key][:].astype(np.float32)
    return result


# ── Statistics ─────────────────────────────────────────────────────────

def bootstrap_ci(values, n_boot=N_BOOTSTRAP, seed=RNG_SEED):
    rng = np.random.RandomState(seed)
    values = np.array(values)
    n = len(values)
    means = [np.mean(rng.choice(values, size=n, replace=True)) for _ in range(n_boot)]
    return float(np.percentile(means, 2.5)), float(np.percentile(means, 97.5))


def paired_comparison(vals_a, vals_b):
    rng = np.random.RandomState(RNG_SEED)
    a = np.array(vals_a, dtype=np.float64)
    b = np.array(vals_b, dtype=np.float64)
    deltas = a - b
    n = len(deltas)
    boot_means = [float(np.mean(rng.choice(deltas, size=n, replace=True)))
                  for _ in range(N_BOOTSTRAP)]
    ci = (float(np.percentile(boot_means, 2.5)), float(np.percentile(boot_means, 97.5)))
    p_boot = float(min(np.mean([m <= 0 for m in boot_means]) * 2, 1.0))
    t_stat, p_ttest = ttest_rel(a, b)
    return {
        "delta": round(float(np.mean(deltas)), 6),
        "ci_95": [round(ci[0], 6), round(ci[1], 6)],
        "p_bootstrap": round(p_boot, 4),
        "p_ttest": round(float(p_ttest), 6),
    }


# ── Computation ────────────────────────────────────────────────────────

def compute_single_model(name, config):
    feat_dir = FEAT_BASE / config["dir"]
    fmt = config["format"]
    fkey = config["key"]

    per_task = {}
    rsa_values = []

    for task in TASKS:
        actions = load_actions(task)
        if fmt == "traj":
            feats = load_features_traj(feat_dir, task, fkey)
        else:
            feats = load_features_demo(feat_dir, task, fkey)

        rsa = compute_task_rsa(feats, actions)
        per_task[task] = rsa
        if rsa is not None:
            rsa_values.append(rsa)

    if not rsa_values:
        return None

    ci = bootstrap_ci(rsa_values)
    return {
        "mean_rsa": round(float(np.mean(rsa_values)), 6),
        "std": round(float(np.std(rsa_values)), 6),
        "per_task": {k: round(v, 6) if v is not None else None for k, v in per_task.items()},
        "ci_95": [round(ci[0], 6), round(ci[1], 6)],
        "n_tasks": len(rsa_values),
        "desc": config["desc"],
    }


def compute_vla_all_layers(name, config):
    feat_dir = FEAT_BASE / config["dir"]
    results = {}

    for agg_key in ["image_mean", "last_preaction"]:
        per_layer_task_rsa = {l: {} for l in range(N_LAYERS)}

        for ti, task in enumerate(TASKS):
            actions = load_actions(task)
            path = feat_dir / f"{task}.h5"

            all_feats = {}
            with h5py.File(path, "r") as f:
                for key in f.keys():
                    if key.startswith("demo"):
                        did = int(key.replace("demo_", "").replace("demo", ""))
                        all_feats[did] = f[key][agg_key][:]  # (T, 33, 4096) float16

            for layer_idx in range(N_LAYERS):
                feats_layer = {
                    did: arr[:, layer_idx, :].astype(np.float32)
                    for did, arr in all_feats.items()
                }
                rsa = compute_task_rsa(feats_layer, actions)
                per_layer_task_rsa[layer_idx][task] = rsa

            del all_feats
            sys.stdout.write(f"\r  {name}/{agg_key}: task {ti+1}/{len(TASKS)}")
            sys.stdout.flush()

        print()

        per_layer = {}
        for layer_idx in range(N_LAYERS):
            pt = per_layer_task_rsa[layer_idx]
            rsa_values = [v for v in pt.values() if v is not None]
            if rsa_values:
                ci = bootstrap_ci(rsa_values)
                per_layer[str(layer_idx)] = {
                    "mean_rsa": round(float(np.mean(rsa_values)), 6),
                    "std": round(float(np.std(rsa_values)), 6),
                    "per_task": {k: round(v, 6) if v is not None else None
                                 for k, v in pt.items()},
                    "ci_95": [round(ci[0], 6), round(ci[1], 6)],
                }

        if per_layer:
            best_layer = max(per_layer.keys(), key=lambda l: per_layer[l]["mean_rsa"])
            results[agg_key] = {
                "per_layer": per_layer,
                "best_layer": int(best_layer),
                "best_rsa": per_layer[best_layer]["mean_rsa"],
                "best_ci": per_layer[best_layer]["ci_95"],
                "best_std": per_layer[best_layer]["std"],
                "best_per_task": per_layer[best_layer]["per_task"],
                "desc": f"{config['desc']} — {agg_key}",
            }
            print(f"  -> best layer={best_layer}, RSA={per_layer[best_layer]['mean_rsa']:.4f}")

    return results


def compute_inst_ctrl_at_layer(layer_idx):
    results = {}
    for name, config in INST_CTRL_CONFIGS.items():
        feat_dir = FEAT_BASE / config["dir"]
        per_task = {}
        rsa_values = []

        for task in TASKS:
            actions = load_actions(task)
            path = feat_dir / f"{task}.h5"
            feats = {}
            with h5py.File(path, "r") as f:
                for key in f.keys():
                    if key.startswith("demo"):
                        did = int(key.replace("demo_", "").replace("demo", ""))
                        feats[did] = f[key]["image_mean"][:, layer_idx, :].astype(np.float32)

            rsa = compute_task_rsa(feats, actions)
            per_task[task] = rsa
            if rsa is not None:
                rsa_values.append(rsa)

        if rsa_values:
            ci = bootstrap_ci(rsa_values)
            results[name] = {
                "mean_rsa": round(float(np.mean(rsa_values)), 6),
                "std": round(float(np.std(rsa_values)), 6),
                "per_task": {k: round(v, 6) if v is not None else None
                             for k, v in per_task.items()},
                "ci_95": [round(ci[0], 6), round(ci[1], 6)],
                "layer": layer_idx,
                "desc": config["desc"],
            }
            print(f"  {name}: RSA={results[name]['mean_rsa']:.4f}")

    return results


# ── Main ───────────────────────────────────────────────────────────────

def main():
    np.random.seed(RNG_SEED)
    t0 = time.time()

    all_results = {
        "method": {
            "pairing": "within-task",
            "rep_distance": "cosine",
            "act_distance": "euclidean",
            "n_sample": N_SAMPLE,
            "demos_per_task": 50,
            "bootstrap_n": N_BOOTSTRAP,
            "seed": RNG_SEED,
            "n_tasks": len(TASKS),
            "tasks": TASKS,
        },
        "models": {},
        "instruction_control": {},
        "pairwise_comparisons": {},
    }

    # 1. Non-VLA models
    print("=" * 60)
    print("NON-VLA MODELS")
    print("=" * 60)
    for name, config in SINGLE_LAYER_CONFIGS.items():
        print(f"\n{name}...")
        result = compute_single_model(name, config)
        if result:
            all_results["models"][name] = result
            print(f"  RSA = {result['mean_rsa']:.4f} +/- {result['std']:.4f}  "
                  f"CI [{result['ci_95'][0]:.4f}, {result['ci_95'][1]:.4f}]")
        else:
            print("  FAILED")

    # 2. VLA models
    print("\n" + "=" * 60)
    print("VLA MODELS (33 layers x 2 aggregations)")
    print("=" * 60)
    vla_results = {}
    for name, config in VLA_CONFIGS.items():
        print(f"\n{name}...")
        result = compute_vla_all_layers(name, config)
        if result:
            vla_results[name] = result
            for agg_key in ["image_mean", "last_preaction"]:
                if agg_key in result:
                    model_key = f"{name}_{agg_key}"
                    all_results["models"][model_key] = result[agg_key]

    # 3. Instruction control
    print("\n" + "=" * 60)
    print("INSTRUCTION CONTROL")
    print("=" * 60)
    if "vla_trained" in vla_results and "image_mean" in vla_results["vla_trained"]:
        best_layer = vla_results["vla_trained"]["image_mean"]["best_layer"]
        print(f"Using vla_trained/image_mean best layer: {best_layer}")
        inst_results = compute_inst_ctrl_at_layer(best_layer)
        all_results["instruction_control"] = inst_results
    else:
        print("Skipped — vla_trained image_mean not available")

    # 4. Pairwise comparisons
    print("\n" + "=" * 60)
    print("PAIRWISE COMPARISONS")
    print("=" * 60)
    comparisons = {}

    def get_ptv(model_key, layer=None):
        m = all_results["models"].get(model_key)
        if m is None:
            return None
        if "per_layer" in m:
            if layer is None:
                layer = m["best_layer"]
            pt = m["per_layer"].get(str(layer), {}).get("per_task", {})
        else:
            pt = m.get("per_task", {})
        vals = [pt.get(t) for t in TASKS]
        if any(v is None for v in vals):
            return None
        return vals

    # C1: trained vs untrained — image_mean
    if "vla_trained" in vla_results and "vla_untrained" in vla_results:
        bl = vla_results["vla_trained"]["image_mean"]["best_layer"]
        va = get_ptv("vla_trained_image_mean", bl)
        vb = get_ptv("vla_untrained_image_mean", bl)
        if va and vb:
            c = paired_comparison(va, vb)
            c["layer"] = bl
            c["desc"] = f"trained vs untrained image_mean at L{bl}"
            comparisons["trained_vs_untrained_image_mean"] = c
            print(f"\n  C1 trained vs untrained image_mean (L{bl}): "
                  f"d={c['delta']:.4f}, p={c['p_ttest']:.4f}")

    # C2: trained vs untrained — last_preaction
    if "vla_trained" in vla_results and "vla_untrained" in vla_results:
        bl = vla_results["vla_trained"]["last_preaction"]["best_layer"]
        va = get_ptv("vla_trained_last_preaction", bl)
        vb = get_ptv("vla_untrained_last_preaction", bl)
        if va and vb:
            c = paired_comparison(va, vb)
            c["layer"] = bl
            c["desc"] = f"trained vs untrained last_preaction at L{bl}"
            comparisons["trained_vs_untrained_last_preaction"] = c
            print(f"  C2 trained vs untrained last_preaction (L{bl}): "
                  f"d={c['delta']:.4f}, p={c['p_ttest']:.4f}")

    # C3: siglip_projector vs vla_trained image_mean (like-for-like)
    if "siglip_projector" in all_results["models"] and "vla_trained" in vla_results:
        bl = vla_results["vla_trained"]["image_mean"]["best_layer"]
        va = get_ptv("siglip_projector")
        vb = get_ptv("vla_trained_image_mean", bl)
        if va and vb:
            c = paired_comparison(va, vb)
            c["layer"] = bl
            c["desc"] = f"siglip_projector vs vla_trained image_mean at L{bl}"
            comparisons["siglip_projector_vs_vla_trained_image_mean"] = c
            print(f"  C3 siglip_projector vs vla_trained image_mean (L{bl}): "
                  f"d={c['delta']:.4f}, p={c['p_ttest']:.4f}")

    # C4: siglip_projector vs vla_trained last_preaction
    if "siglip_projector" in all_results["models"] and "vla_trained" in vla_results:
        bl = vla_results["vla_trained"]["last_preaction"]["best_layer"]
        va = get_ptv("siglip_projector")
        vb = get_ptv("vla_trained_last_preaction", bl)
        if va and vb:
            c = paired_comparison(va, vb)
            c["layer"] = bl
            c["desc"] = f"siglip_projector vs vla_trained last_preaction at L{bl}"
            comparisons["siglip_projector_vs_vla_trained_last_preaction"] = c
            print(f"  C4 siglip_projector vs vla_trained last_preaction (L{bl}): "
                  f"d={c['delta']:.4f}, p={c['p_ttest']:.4f}")

    # C5: dino_cls vs siglip_projector
    va = get_ptv("dino_cls")
    vb = get_ptv("siglip_projector")
    if va and vb:
        c = paired_comparison(va, vb)
        c["desc"] = "dino_cls vs siglip_projector"
        comparisons["dino_cls_vs_siglip_projector"] = c
        print(f"  C5 dino_cls vs siglip_projector: "
              f"d={c['delta']:.4f}, p={c['p_ttest']:.4f}")

    # C6: fused_backbone vs siglip_projector
    va = get_ptv("fused_backbone")
    vb = get_ptv("siglip_projector")
    if va and vb:
        c = paired_comparison(va, vb)
        c["desc"] = "fused_backbone vs siglip_projector"
        comparisons["fused_backbone_vs_siglip_projector"] = c
        print(f"  C6 fused_backbone vs siglip_projector: "
              f"d={c['delta']:.4f}, p={c['p_ttest']:.4f}")

    # C7: trained with-inst vs no-inst image_mean
    if "vla_trained" in vla_results and "vla_trained_no_inst" in vla_results:
        bl = vla_results["vla_trained"]["image_mean"]["best_layer"]
        va = get_ptv("vla_trained_image_mean", bl)
        vb = get_ptv("vla_trained_no_inst_image_mean", bl)
        if va and vb:
            c = paired_comparison(va, vb)
            c["layer"] = bl
            c["desc"] = f"trained with-inst vs no-inst image_mean at L{bl}"
            comparisons["trained_with_vs_no_inst_image_mean"] = c
            print(f"  C7 trained with-inst vs no-inst image_mean (L{bl}): "
                  f"d={c['delta']:.4f}, p={c['p_ttest']:.4f}")

    # C8: untrained with-inst vs no-inst image_mean
    if "vla_untrained" in vla_results and "vla_untrained_no_inst" in vla_results:
        bl = vla_results["vla_untrained"]["image_mean"]["best_layer"]
        va = get_ptv("vla_untrained_image_mean", bl)
        vb = get_ptv("vla_untrained_no_inst_image_mean", bl)
        if va and vb:
            c = paired_comparison(va, vb)
            c["layer"] = bl
            c["desc"] = f"untrained with-inst vs no-inst image_mean at L{bl}"
            comparisons["untrained_with_vs_no_inst_image_mean"] = c
            print(f"  C8 untrained with-inst vs no-inst image_mean (L{bl}): "
                  f"d={c['delta']:.4f}, p={c['p_ttest']:.4f}")

    all_results["pairwise_comparisons"] = comparisons

    # Save
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w") as f:
        json.dump(all_results, f, indent=2)

    elapsed = time.time() - t0
    print(f"\n{'=' * 60}")
    print(f"DONE in {elapsed:.1f}s")
    print(f"Saved to {OUT_JSON}")

    # Summary table
    print(f"\n{'=' * 60}")
    print("SUMMARY TABLE (sorted by RSA)")
    print(f"{'=' * 60}")
    print(f"{'Model':<50} {'RSA':>8} {'std':>8} {'CI_lo':>8} {'CI_hi':>8}")
    print("-" * 84)

    summary = []
    for name, m in all_results["models"].items():
        if "per_layer" in m:
            rsa = m["best_rsa"]
            std = m["best_std"]
            ci = m["best_ci"]
            bl = m["best_layer"]
            label = f"{name} (best L{bl})"
        else:
            rsa = m["mean_rsa"]
            std = m["std"]
            ci = m["ci_95"]
            label = name
        summary.append((label, rsa, std, ci))

    summary.sort(key=lambda x: x[1], reverse=True)
    for label, rsa, std, ci in summary:
        print(f"{label:<50} {rsa:>8.4f} {std:>8.4f} {ci[0]:>8.4f} {ci[1]:>8.4f}")

    if all_results["instruction_control"]:
        print(f"\nINSTRUCTION CONTROL (image_mean at best layer)")
        print(f"{'Condition':<30} {'RSA':>8} {'std':>8}")
        print("-" * 48)
        for name, m in all_results["instruction_control"].items():
            print(f"{name:<30} {m['mean_rsa']:>8.4f} {m['std']:>8.4f}")


if __name__ == "__main__":
    main()
