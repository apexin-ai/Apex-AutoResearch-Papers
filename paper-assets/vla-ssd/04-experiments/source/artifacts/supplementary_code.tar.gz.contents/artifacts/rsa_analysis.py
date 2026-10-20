"""RSA (Representational Similarity Analysis) for LIBERO-Goal VLA features.

Input:
  - Trained/Untrained VLA features: /root/autodl-tmp/vla-ssd/features/{trained,untrained}_libero_goal/*.h5
    Keys: demo_X/last_preaction, shape=(T, 33, 4096)
  - DINO features: /root/autodl-tmp/vla-ssd/features/dinov2_libero_goal/*.h5
    Keys: traj_X/cls_token, shape=(T, 1024)
  - Actions: /root/autodl-tmp/vla-ssd/data/libero/libero_goal/*_demo.hdf5
    Keys: data/demo_X/actions, shape=(T, 7)

Output:
  - /root/autodl-tmp/vla-ssd/results/rsa/rsa_results.json
  - stdout summary table

Dependencies: numpy, scipy, h5py, json, argparse
"""

import argparse
import json
import os
import time
from pathlib import Path

import h5py
import numpy as np
from scipy.spatial.distance import cosine as cosine_dist
from scipy.stats import spearmanr


# ── paths ──────────────────────────────────────────────────────────────
FEAT_ROOT = Path("/root/autodl-tmp/vla-ssd/features")
DATA_ROOT = Path("/root/autodl-tmp/vla-ssd/data/libero/libero_goal")
OUT_DIR   = Path("/root/autodl-tmp/vla-ssd/results/rsa")

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

TEMPORAL_BINS = {
    "early": (0.0, 0.33),
    "mid":   (0.33, 0.67),
    "late":  (0.67, 1.0),
}

N_VLA_LAYERS = 33


# ── data loading ───────────────────────────────────────────────────────

def load_vla_features(model_type: str, task: str, demo_ids: list[int], layer: int, suffix: str = "") -> dict:
    """Load VLA features for specific demos and layer. Returns {demo_id: (T, D) array}."""
    path = FEAT_ROOT / f"{model_type}_libero_goal{suffix}" / f"{task}.h5"
    result = {}
    with h5py.File(path, "r") as f:
        for did in demo_ids:
            key = f"demo_{did}/last_preaction"
            if key in f:
                data = f[key][:, layer, :]  # (T, 4096)
                result[did] = data.astype(np.float32)
    return result


def load_dino_features(task: str, demo_ids: list[int]) -> dict:
    """Load DINO cls_token features. Returns {demo_id: (T, D) array}."""
    path = FEAT_ROOT / "dinov2_libero_goal" / f"{task}.h5"
    result = {}
    with h5py.File(path, "r") as f:
        for did in demo_ids:
            key = f"traj_{did}/cls_token"
            if key in f:
                result[did] = f[key][:].astype(np.float32)
    return result


def load_actions(task: str, demo_ids: list[int]) -> dict:
    """Load actions. Returns {demo_id: (T, 7) array}."""
    path = DATA_ROOT / f"{task}_demo.hdf5"
    result = {}
    with h5py.File(path, "r") as f:
        for did in demo_ids:
            key = f"data/demo_{did}/actions"
            if key in f:
                result[did] = f[key][:].astype(np.float32)
    return result


# ── temporal binning ───────────────────────────────────────────────────

def get_temporal_indices(T: int, phase: str) -> np.ndarray:
    """Return frame indices for a temporal phase."""
    lo, hi = TEMPORAL_BINS[phase]
    t_norm = np.linspace(0, 1, T, endpoint=False)
    mask = (t_norm >= lo) & (t_norm < hi)
    if phase == "late":
        mask = (t_norm >= lo) & (t_norm <= 1.0)
    return np.where(mask)[0]


def subsample_to_length(arr: np.ndarray, target_len: int) -> np.ndarray:
    """Uniformly subsample temporal axis to target length."""
    T = arr.shape[0]
    if T <= target_len:
        return arr
    idx = np.linspace(0, T - 1, target_len, dtype=int)
    return arr[idx]


# ── dissimilarity computation ─────────────────────────────────────────

def compute_mean_cosine_distance(feat_a: np.ndarray, feat_b: np.ndarray, n_sample: int = 20) -> float:
    """Cosine distance between two trajectories, aligned by subsampling to equal length."""
    L = min(len(feat_a), len(feat_b), n_sample)
    a = subsample_to_length(feat_a, L)
    b = subsample_to_length(feat_b, L)
    dists = []
    for i in range(L):
        na = np.linalg.norm(a[i])
        nb = np.linalg.norm(b[i])
        if na < 1e-8 or nb < 1e-8:
            dists.append(1.0)
        else:
            dists.append(cosine_dist(a[i], b[i]))
    return float(np.mean(dists))


def build_dissimilarity_matrix(
    data: dict[tuple, np.ndarray],
    keys: list[tuple],
    phase: str,
) -> np.ndarray:
    """Build pairwise cosine dissimilarity matrix for given data and temporal phase."""
    N = len(keys)
    dm = np.zeros((N, N), dtype=np.float32)

    phase_cache = {}
    for i, k in enumerate(keys):
        arr = data[k]
        idx = get_temporal_indices(len(arr), phase)
        if len(idx) == 0:
            idx = np.array([0])
        phase_cache[i] = arr[idx]

    for i in range(N):
        for j in range(i + 1, N):
            d = compute_mean_cosine_distance(phase_cache[i], phase_cache[j])
            dm[i, j] = d
            dm[j, i] = d

    return dm


def compute_rsa(rdm: np.ndarray, adm: np.ndarray) -> float:
    """Spearman correlation between upper triangles."""
    idx = np.triu_indices_from(rdm, k=1)
    r_vec = rdm[idx]
    a_vec = adm[idx]
    if np.std(r_vec) < 1e-10 or np.std(a_vec) < 1e-10:
        return 0.0
    rho, _ = spearmanr(r_vec, a_vec)
    return float(rho)


# ── bootstrap CI ─────────────────────────────────────────────────────

def bootstrap_ci(values: list[float], n_boot: int = 1000, ci: float = 0.95) -> tuple[float, float]:
    """Bootstrap confidence interval for the mean of values."""
    rng = np.random.default_rng(42)
    arr = np.array(values)
    boot_means = np.array([rng.choice(arr, size=len(arr), replace=True).mean() for _ in range(n_boot)])
    alpha = (1 - ci) / 2
    lo = float(np.percentile(boot_means, alpha * 100))
    hi = float(np.percentile(boot_means, (1 - alpha) * 100))
    return lo, hi


# ── linear CKA ────────────────────────────────────────────────────────

def linear_cka(X: np.ndarray, Y: np.ndarray) -> float:
    """Linear CKA between two feature matrices (N, D1) and (N, D2)."""
    X = X - X.mean(axis=0, keepdims=True)
    Y = Y - Y.mean(axis=0, keepdims=True)
    hsic_xy = np.linalg.norm(X.T @ Y, "fro") ** 2
    hsic_xx = np.linalg.norm(X.T @ X, "fro") ** 2
    hsic_yy = np.linalg.norm(Y.T @ Y, "fro") ** 2
    if hsic_xx < 1e-10 or hsic_yy < 1e-10:
        return 0.0
    return float(hsic_xy / np.sqrt(hsic_xx * hsic_yy))


# ── main ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="RSA analysis for LIBERO-Goal VLA features")
    parser.add_argument("--n_demos", type=int, default=10, help="demos per task (default: 10)")
    parser.add_argument("--n_tasks", type=int, default=10, help="number of tasks (default: 10)")
    parser.add_argument("--layers", type=str, default="all",
                        help="layers to analyze: 'all' or comma-separated (e.g. '0,8,16,24,32')")
    parser.add_argument("--skip_cka", action="store_true", help="skip CKA computation")
    parser.add_argument("--feat_suffix", type=str, default="",
                        help="Suffix for feature dirs (e.g. '_no_inst')")
    args = parser.parse_args()

    tasks = TASKS[:args.n_tasks]
    demo_ids = list(range(args.n_demos))

    if args.layers == "all":
        layers = list(range(N_VLA_LAYERS))
    else:
        layers = [int(x) for x in args.layers.split(",")]

    print(f"Config: {len(tasks)} tasks × {args.n_demos} demos = {len(tasks) * args.n_demos} trajectories")
    print(f"Layers: {len(layers)} | CKA: {'skip' if args.skip_cka else 'yes'}")
    print()

    # ── load all actions (shared across models) ──
    print("Loading actions...")
    all_actions = {}
    for task in tasks:
        act = load_actions(task, demo_ids)
        for did, a in act.items():
            all_actions[(task, did)] = a
    print(f"  Loaded {len(all_actions)} demos")

    # ── load DINO features (constant across VLA layers) ──
    print("Loading DINO features...")
    dino_feats = {}
    for task in tasks:
        df = load_dino_features(task, demo_ids)
        for did in df:
            dino_feats[(task, did)] = df[did]
    print(f"  Loaded {len(dino_feats)} DINO demos")

    # common keys across all sources
    common_keys_base = set(dino_feats) & set(all_actions)
    sorted_keys = sorted(common_keys_base)
    N_demos = len(sorted_keys)
    print(f"  Common demos: {N_demos}")

    # ── precompute ADM and DINO RDM (invariant across VLA layers) ──
    print("Precomputing ADM and DINO RDM...")
    act_common = {k: all_actions[k] for k in sorted_keys}
    dino_common = {k: dino_feats[k] for k in sorted_keys}
    adm_cache = {}
    dino_rdm_cache = {}
    dino_rsa_cache = {}
    for phase in TEMPORAL_BINS:
        adm_cache[phase] = build_dissimilarity_matrix(act_common, sorted_keys, phase)
        dino_rdm_cache[phase] = build_dissimilarity_matrix(dino_common, sorted_keys, phase)
        dino_rsa_cache[phase] = compute_rsa(dino_rdm_cache[phase], adm_cache[phase])
    print("  Done")

    # ── per-layer RSA ──
    results = {
        "per_layer": {},
        "per_timestep": {phase: {} for phase in TEMPORAL_BINS},
        "cka": {},
        "gates": {},
    }

    phase_rsa_accum = {phase: {"trained": [], "untrained": [], "dino": []}
                       for phase in TEMPORAL_BINS}

    for li, layer in enumerate(layers):
        t0 = time.time()
        layer_key = f"layer_{layer}"

        # load VLA features for this layer
        trained_feats = {}
        untrained_feats = {}
        for task in tasks:
            tf = load_vla_features("trained", task, demo_ids, layer, suffix=args.feat_suffix)
            uf = load_vla_features("untrained", task, demo_ids, layer, suffix=args.feat_suffix)
            for did in tf:
                trained_feats[(task, did)] = tf[did]
            for did in uf:
                untrained_feats[(task, did)] = uf[did]

        # ensure we only use keys present in all sources
        common_keys = common_keys_base & set(trained_feats) & set(untrained_feats)
        keys = sorted(common_keys)

        feat_t = {k: trained_feats[k] for k in keys}
        feat_u = {k: untrained_feats[k] for k in keys}

        layer_rsa = {"trained": {}, "untrained": {}, "dino": {}}
        for phase in TEMPORAL_BINS:
            adm = adm_cache[phase]
            rdm_t = build_dissimilarity_matrix(feat_t, keys, phase)
            rdm_u = build_dissimilarity_matrix(feat_u, keys, phase)

            rsa_t = compute_rsa(rdm_t, adm)
            rsa_u = compute_rsa(rdm_u, adm)
            rsa_d = dino_rsa_cache[phase]

            layer_rsa["trained"][phase] = rsa_t
            layer_rsa["untrained"][phase] = rsa_u
            layer_rsa["dino"][phase] = rsa_d

            phase_rsa_accum[phase]["trained"].append(rsa_t)
            phase_rsa_accum[phase]["untrained"].append(rsa_u)
            phase_rsa_accum[phase]["dino"].append(rsa_d)

        rsa_t_all = np.mean([layer_rsa["trained"][p] for p in TEMPORAL_BINS])
        rsa_u_all = np.mean([layer_rsa["untrained"][p] for p in TEMPORAL_BINS])
        rsa_d_all = np.mean([layer_rsa["dino"][p] for p in TEMPORAL_BINS])

        results["per_layer"][layer_key] = {
            "trained_rsa": round(float(rsa_t_all), 4),
            "untrained_rsa": round(float(rsa_u_all), 4),
            "dino_rsa": round(float(rsa_d_all), 4),
            "per_phase": {
                phase: {
                    "trained_rsa": round(layer_rsa["trained"][phase], 4),
                    "untrained_rsa": round(layer_rsa["untrained"][phase], 4),
                    "dino_rsa": round(layer_rsa["dino"][phase], 4),
                }
                for phase in TEMPORAL_BINS
            },
        }

        if not args.skip_cka:
            t_mat = np.stack([trained_feats[k].mean(axis=0) for k in keys])
            u_mat = np.stack([untrained_feats[k].mean(axis=0) for k in keys])
            cka_val = linear_cka(t_mat, u_mat)
            results["cka"][layer_key] = round(cka_val, 4)

        elapsed = time.time() - t0
        print(f"  Layer {layer:2d}/{layers[-1]}: trained={rsa_t_all:.4f}  untrained={rsa_u_all:.4f}  "
              f"dino={rsa_d_all:.4f}  [{elapsed:.1f}s]")

    # ── per-timestep summary (mean across layers) ──
    for phase in TEMPORAL_BINS:
        results["per_timestep"][phase] = {
            "trained_rsa": round(float(np.mean(phase_rsa_accum[phase]["trained"])), 4),
            "untrained_rsa": round(float(np.mean(phase_rsa_accum[phase]["untrained"])), 4),
            "dino_rsa": round(float(np.mean(phase_rsa_accum[phase]["dino"])), 4),
        }

    # ── bootstrap CI on per-task RSA ──
    print("\nComputing bootstrap CIs...")
    task_rsa_trained = {}
    task_rsa_untrained = {}
    task_rsa_dino = {}
    for task in tasks:
        task_keys = [k for k in sorted_keys if k[0] == task]
        if len(task_keys) < 2:
            continue
        task_act = {k: all_actions[k] for k in task_keys}
        task_dino = {k: dino_feats[k] for k in task_keys}

        best_layer = max(layers, key=lambda l: results["per_layer"][f"layer_{l}"]["trained_rsa"])
        task_trained = {}
        task_untrained = {}
        for did in demo_ids:
            if (task, did) in sorted_keys:
                tf = load_vla_features("trained", task, [did], best_layer, suffix=args.feat_suffix)
                uf = load_vla_features("untrained", task, [did], best_layer, suffix=args.feat_suffix)
                if did in tf:
                    task_trained[(task, did)] = tf[did]
                if did in uf:
                    task_untrained[(task, did)] = uf[did]

        tk = sorted(set(task_keys) & set(task_trained) & set(task_untrained))
        if len(tk) < 2:
            continue

        adm_task = build_dissimilarity_matrix({k: all_actions[k] for k in tk}, tk, "early")
        rdm_t = build_dissimilarity_matrix({k: task_trained[k] for k in tk}, tk, "early")
        rdm_u = build_dissimilarity_matrix({k: task_untrained[k] for k in tk}, tk, "early")
        rdm_d = build_dissimilarity_matrix({k: dino_feats[k] for k in tk}, tk, "early")

        rsa_t = compute_rsa(rdm_t, adm_task)
        rsa_u = compute_rsa(rdm_u, adm_task)
        rsa_d = compute_rsa(rdm_d, adm_task)
        task_rsa_trained[task] = rsa_t
        task_rsa_untrained[task] = rsa_u
        task_rsa_dino[task] = rsa_d

    trained_per_task = list(task_rsa_trained.values())
    untrained_per_task = list(task_rsa_untrained.values())
    dino_per_task = list(task_rsa_dino.values())

    ci_trained = bootstrap_ci(trained_per_task) if len(trained_per_task) >= 2 else (0.0, 0.0)
    ci_untrained = bootstrap_ci(untrained_per_task) if len(untrained_per_task) >= 2 else (0.0, 0.0)
    ci_dino = bootstrap_ci(dino_per_task) if len(dino_per_task) >= 2 else (0.0, 0.0)
    delta_per_task = [t - u for t, u in zip(trained_per_task, untrained_per_task)]
    ci_delta = bootstrap_ci(delta_per_task) if len(delta_per_task) >= 2 else (0.0, 0.0)

    results["bootstrap_ci"] = {
        "n_tasks": len(trained_per_task),
        "trained_mean": round(float(np.mean(trained_per_task)), 4) if trained_per_task else None,
        "trained_ci95": [round(ci_trained[0], 4), round(ci_trained[1], 4)],
        "untrained_mean": round(float(np.mean(untrained_per_task)), 4) if untrained_per_task else None,
        "untrained_ci95": [round(ci_untrained[0], 4), round(ci_untrained[1], 4)],
        "dino_mean": round(float(np.mean(dino_per_task)), 4) if dino_per_task else None,
        "dino_ci95": [round(ci_dino[0], 4), round(ci_dino[1], 4)],
        "delta_mean": round(float(np.mean(delta_per_task)), 4) if delta_per_task else None,
        "delta_ci95": [round(ci_delta[0], 4), round(ci_delta[1], 4)],
        "delta_ci_excludes_zero": bool(ci_delta[0] > 0 or ci_delta[1] < 0),
    }
    print(f"  Trained CI: [{ci_trained[0]:.4f}, {ci_trained[1]:.4f}]")
    print(f"  Untrained CI: [{ci_untrained[0]:.4f}, {ci_untrained[1]:.4f}]")
    print(f"  Delta CI: [{ci_delta[0]:.4f}, {ci_delta[1]:.4f}]")

    # ── gates ──
    trained_peaks = [results["per_layer"][f"layer_{l}"]["trained_rsa"] for l in layers]
    untrained_peaks = [results["per_layer"][f"layer_{l}"]["untrained_rsa"] for l in layers]

    g1_trained_peak = max(trained_peaks)
    g1_untrained_peak = max(untrained_peaks)
    g1_delta = g1_trained_peak - g1_untrained_peak
    g1_pass = g1_delta > 0.05

    g2_count = sum(1 for l in layers
                   if results["per_layer"][f"layer_{l}"]["trained_rsa"]
                   > results["per_layer"][f"layer_{l}"]["untrained_rsa"])
    g2_pass = g2_count > len(layers) / 2

    results["gates"] = {
        "G1_trained_peak": round(g1_trained_peak, 4),
        "G1_untrained_peak": round(g1_untrained_peak, 4),
        "G1_delta": round(g1_delta, 4),
        "G1_pass": bool(g1_pass),
        "G2_layers_trained_gt_untrained": g2_count,
        "G2_total_layers": len(layers),
        "G2_pass": bool(g2_pass),
    }

    # ── save ──
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"rsa_results{args.feat_suffix}.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    # ── summary table ──
    print("\n" + "=" * 80)
    print("RSA SUMMARY (Spearman corr between representation & action dissimilarity)")
    print("=" * 80)

    print(f"\n{'Layer':>8} | {'Trained':>10} | {'Untrained':>10} | {'DINO':>10} | {'T-U Delta':>10}"
          + (f" | {'CKA(T,U)':>10}" if not args.skip_cka else ""))
    print("-" * (55 + (13 if not args.skip_cka else 0)))
    for l in layers:
        lk = f"layer_{l}"
        r = results["per_layer"][lk]
        row = (f"{l:>8d} | {r['trained_rsa']:>10.4f} | {r['untrained_rsa']:>10.4f} | "
               f"{r['dino_rsa']:>10.4f} | {r['trained_rsa'] - r['untrained_rsa']:>+10.4f}")
        if not args.skip_cka and lk in results["cka"]:
            row += f" | {results['cka'][lk]:>10.4f}"
        print(row)

    print(f"\n{'Phase':>8} | {'Trained':>10} | {'Untrained':>10} | {'DINO':>10}")
    print("-" * 48)
    for phase in TEMPORAL_BINS:
        r = results["per_timestep"][phase]
        print(f"{phase:>8} | {r['trained_rsa']:>10.4f} | {r['untrained_rsa']:>10.4f} | "
              f"{r['dino_rsa']:>10.4f}")

    print(f"\nBootstrap CI (per-task RSA at peak layer, 1000 resamples):")
    bc = results["bootstrap_ci"]
    print(f"  Trained:   {bc['trained_mean']:.4f}  [{bc['trained_ci95'][0]:.4f}, {bc['trained_ci95'][1]:.4f}]")
    print(f"  Untrained: {bc['untrained_mean']:.4f}  [{bc['untrained_ci95'][0]:.4f}, {bc['untrained_ci95'][1]:.4f}]")
    print(f"  DINO:      {bc['dino_mean']:.4f}  [{bc['dino_ci95'][0]:.4f}, {bc['dino_ci95'][1]:.4f}]")
    print(f"  Delta:     {bc['delta_mean']:.4f}  [{bc['delta_ci95'][0]:.4f}, {bc['delta_ci95'][1]:.4f}]"
          f"  excludes_0={'YES' if bc['delta_ci_excludes_zero'] else 'NO'}")

    print(f"\nGates:")
    g = results["gates"]
    print(f"  G1: peak RSA trained={g['G1_trained_peak']:.4f} vs untrained={g['G1_untrained_peak']:.4f}"
          f"  delta={g['G1_delta']:+.4f}  {'PASS' if g['G1_pass'] else 'FAIL'}")
    print(f"  G2: trained > untrained in {g['G2_layers_trained_gt_untrained']}/{g['G2_total_layers']} layers"
          f"  {'PASS' if g['G2_pass'] else 'FAIL'}")


if __name__ == "__main__":
    main()
