#!/usr/bin/env python3
"""Pool A MDE Power Analysis with Wild Cluster Bootstrap (Webb 6-point).

Vectorized implementation: batches all N_sim simulations together for each
(condition, beta_std, position) to avoid Python-level sim loops.
"""

import json
import time
import itertools
import logging
import argparse
import numpy as np
import statsmodels.api as sm
from pathlib import Path
from scipy.interpolate import interp1d

MI_MODELS = [
    "qwen2.5-72b", "llama3.1-70b", "mistral-large",
    "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b",
    "claude-opus-4-6", "gpt-5.5", "gemini-3.1-pro-preview", "gpt-4.1",
    "claude-sonnet-4-6", "gpt-4.1-nano", "gemini-3.5-flash",
    "gpt-4.1-mini", "claude-3-haiku",
]
POOL_A = MI_MODELS[6:]
POOL_A_INDICES = list(range(6, 15))

DATASETS = ["mmlu", "arc_challenge"]
ATTACKS = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]
EPS = 1e-6
BETA_STD_GRID = [0.1, 0.15, 0.2, 0.25, 0.3, 0.5, 0.7, 1.0]
SEED = 42

WEBB_6 = np.array([
    -np.sqrt(3/2), -1.0, -np.sqrt(1/2),
     np.sqrt(1/2),  1.0,  np.sqrt(3/2),
])

BASE_DIR = Path("/root/cert_manip_resist_eval")
SCORES_DIR = BASE_DIR / "artifacts/results/plan001/individual_scores"
MI_PATH = BASE_DIR / "artifacts/results/plan001/mi_matrix/mi_matrix_15models.json"
CKPT_PATH = BASE_DIR / "artifacts/results/_taxonomy_checkpoint.json"
OUT_PATH = BASE_DIR / "artifacts/results/plan001/pool_a_mde.json"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("pool_a_mde")


def _json_default(obj):
    if isinstance(obj, np.floating):
        v = float(obj)
        return None if (np.isnan(v) or np.isinf(v)) else v
    if isinstance(obj, np.integer):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    if isinstance(obj, np.bool_):
        return bool(obj)
    raise TypeError(f"Not JSON serializable: {type(obj)}")


def load_mi_matrix():
    with open(MI_PATH) as f:
        data = json.load(f)
    return {ds: np.array(data["mi_matrix"][ds]) for ds in DATASETS}


def load_pairs():
    with open(CKPT_PATH) as f:
        data = json.load(f)
    return {ds: data["pairs"][ds][:300] for ds in DATASETS}


def load_individual_scores(model, dataset, condition):
    path = SCORES_DIR / f"{model}__{dataset}__{condition}.json"
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f).get("scores", [])


def load_pool_a_scores():
    clean = {ds: {} for ds in DATASETS}
    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}
    for m in POOL_A:
        for ds in DATASETS:
            scores = load_individual_scores(m, ds, "clean")
            if scores:
                clean[ds][m] = scores
            for atk in ATTACKS:
                scores = load_individual_scores(m, ds, atk)
                if scores:
                    attacked[ds][atk][m] = scores
    return clean, attacked


def mi_based_keff(mi_matrix, model_indices):
    K = len(model_indices)
    if K <= 1:
        return 1.0
    keff = 0.0
    for i_idx in model_indices:
        term = 1.0
        for j_idx in model_indices:
            if i_idx != j_idx:
                term += np.exp(-2 * mi_matrix[i_idx, j_idx])
        keff += term
    return keff / K


def _is_valid(s):
    if s.get("error") or s.get("format_error"):
        return False
    return s.get("winner") in ("A", "B", "tie")


def majority_vote(votes):
    counts = {"A": 0, "B": 0, "tie": 0}
    for v in votes:
        counts[v] = counts.get(v, 0) + 1
    mc = max(counts.values())
    winners = [k for k, c in counts.items() if c == mc]
    if len(winners) == 1:
        return winners[0]
    for w in winners:
        if w != "tie":
            return w
    return "tie"


def compute_individual_asr(clean_list, attacked_list, pairs):
    n = min(len(clean_list), len(attacked_list), len(pairs))
    n_flips = n_correct = 0
    for i in range(n):
        if not _is_valid(clean_list[i]) or not _is_valid(attacked_list[i]):
            continue
        gt = pairs[i]["ground_truth_winner"]
        if clean_list[i]["winner"] == gt:
            n_correct += 1
            if attacked_list[i]["winner"] != gt:
                n_flips += 1
    return n_flips / max(n_correct, 1)


def compute_panel_asr(jids, clean, attacked, pairs):
    n = min(len(pairs), *(len(clean[j]) for j in jids),
            *(len(attacked[j]) for j in jids))
    n_flips = n_correct = 0
    for i in range(n):
        if not all(_is_valid(clean[j][i]) for j in jids):
            continue
        if not all(_is_valid(attacked[j][i]) for j in jids):
            continue
        gt = pairs[i]["ground_truth_winner"]
        cv = majority_vote([clean[j][i]["winner"] for j in jids])
        if cv != gt:
            continue
        n_correct += 1
        av = majority_vote([attacked[j][i]["winner"] for j in jids])
        if av != gt:
            n_flips += 1
    return n_flips / max(n_correct, 1)


# ── Vectorized wild cluster bootstrap across all sims ────────────────

def batched_wcb_power(X, log_keff, log_eta, intercept, beta_eta, sigma,
                      panel_jids_list, K, beta_std_grid, n_sim, n_boot,
                      rng, batch_size=100):
    """Vectorized power analysis: batch sims to avoid Python loop.

    For each (beta_std, position):
      - Generate all n_sim y_sim at once
      - For each batch of sims, vectorize bootstrap across sims and reps
    """
    n, p = X.shape
    sd_y_val = sigma  # approximate sd_y with sigma for DGP
    sd_lk = np.std(log_keff)
    if sd_lk < 1e-10:
        return {str(b): 0.0 for b in beta_std_grid}

    # Precompute X-dependent quantities
    XtX_inv = np.linalg.inv(X.T @ X)
    M_hat = XtX_inv @ X.T  # p x n
    diag_keff = XtX_inv[1, 1]

    # Restricted model (drop column 1 = log_keff)
    X_r = X[:, [0, 2]]
    M_hat_r = np.linalg.inv(X_r.T @ X_r) @ X_r.T  # 2 x n

    # Build cluster assignments per position
    position_clusters = []
    for pos in range(K):
        cids_raw = np.array([jids[pos] for jids in panel_jids_list])
        unique_c = np.unique(cids_raw)
        c2i = {c: i for i, c in enumerate(unique_c)}
        pci = np.array([c2i[c] for c in cids_raw])
        position_clusters.append((pci, len(unique_c)))

    results = {}

    for beta_std in beta_std_grid:
        beta_raw_approx = beta_std * sigma / sd_lk  # first approximation
        # Better: compute sd_y from DGP
        y_mean_signal = intercept + beta_raw_approx * log_keff + beta_eta * log_eta
        sd_y_dgp = np.sqrt(np.var(y_mean_signal) + sigma**2)
        beta_raw = beta_std * sd_y_dgp / sd_lk

        # Generate all n_sim y values at once: n_sim x n
        noise = rng.normal(0, sigma, size=(n_sim, n))
        Y_sim = (intercept
                 + beta_raw * log_keff[None, :]
                 + beta_eta * log_eta[None, :]
                 + noise)

        # Unrestricted OLS for all sims: Beta_u = Y_sim @ M_hat.T -> n_sim x p
        Beta_u = Y_sim @ M_hat.T
        Resid_u = Y_sim - Beta_u @ X.T
        Sigma2_u = np.sum(Resid_u ** 2, axis=1) / (n - p)
        T_obs = Beta_u[:, 1] / np.sqrt(Sigma2_u * diag_keff)  # n_sim

        # Restricted OLS for all sims
        Beta_r = Y_sim @ M_hat_r.T  # n_sim x 2
        Y_hat_r = Beta_r @ X_r.T   # n_sim x n
        E_r = Y_sim - Y_hat_r      # n_sim x n

        # For each position, compute bootstrap p-values for all sims
        # sig_mask[i] = True if all positions have p < 0.05
        sig_mask = np.ones(n_sim, dtype=bool)

        for pci, n_clusters in position_clusters:
            # Process in batches to limit memory
            p_values = np.empty(n_sim)

            for start in range(0, n_sim, batch_size):
                end = min(start + batch_size, n_sim)
                bs = end - start

                # Generate bootstrap weights: bs x B x n_clusters
                W_cluster = rng.choice(WEBB_6, size=(bs, n_boot, n_clusters))
                # Expand to panel level: bs x B x n
                W_panel = W_cluster[:, :, pci]

                # Bootstrap Y: bs x B x n
                Y_boot = Y_hat_r[start:end, None, :] + W_panel * E_r[start:end, None, :]

                # Reshape for batch OLS: (bs*B) x n
                Y_flat = Y_boot.reshape(bs * n_boot, n)
                Beta_flat = Y_flat @ M_hat.T  # (bs*B) x p
                Resid_flat = Y_flat - Beta_flat @ X.T
                S2_flat = np.sum(Resid_flat ** 2, axis=1) / (n - p)
                SE_flat = np.sqrt(S2_flat * diag_keff)
                SE_flat = np.maximum(SE_flat, 1e-15)
                T_flat = Beta_flat[:, 1] / SE_flat

                # Reshape to bs x B
                T_boot = T_flat.reshape(bs, n_boot)
                T_obs_batch = T_obs[start:end]

                # P-values
                exceed = np.sum(np.abs(T_boot) >= np.abs(T_obs_batch[:, None]),
                                axis=1)
                p_values[start:end] = (1 + exceed) / (1 + n_boot)

            # Update sig_mask: only keep sig if this position also < 0.05
            # (max p across positions < 0.05 iff all positions < 0.05)
            sig_mask &= (p_values < 0.05)

        power = np.mean(sig_mask)
        results[str(beta_std)] = round(float(power), 4)

    return results


# ── Build panel data ─────────────────────────────────────────────────

def build_panel_data(K, mi_matrices, clean, attacked, pairs):
    combos = list(itertools.combinations(range(len(POOL_A)), K))
    logger.info(f"  K={K}: {len(combos)} panels from {len(POOL_A)} models")

    all_cond_data = {}
    for ds in DATASETS:
        mi_mat = mi_matrices[ds]
        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            ds_clean = clean.get(ds, {})
            ds_attacked = attacked.get(ds, {}).get(atk, {})
            ds_pairs = pairs.get(ds, [])
            if not ds_clean or not ds_attacked or not ds_pairs:
                continue

            ind_asr = {}
            for m in POOL_A:
                if m in ds_clean and m in ds_attacked:
                    ind_asr[m] = compute_individual_asr(
                        ds_clean[m], ds_attacked[m], ds_pairs
                    )

            p_asrs, p_keffs, p_etas = [], [], []
            panel_jids_list = []

            for combo in combos:
                jids = [POOL_A[i] for i in combo]
                if not all(j in ind_asr for j in jids):
                    continue
                if not all(j in ds_clean and j in ds_attacked for j in jids):
                    continue

                global_indices = [POOL_A_INDICES[i] for i in combo]
                keff = mi_based_keff(mi_mat, global_indices)
                eta_max = max(ind_asr[j] for j in jids)
                p_asr = compute_panel_asr(
                    jids,
                    {j: ds_clean[j] for j in jids},
                    {j: ds_attacked[j] for j in jids},
                    ds_pairs,
                )

                p_asrs.append(p_asr)
                p_keffs.append(keff)
                p_etas.append(eta_max)
                panel_jids_list.append(jids)

            n_panels = len(p_asrs)
            if n_panels < 10:
                continue
            p_asrs = np.array(p_asrs)
            if np.std(p_asrs) < 1e-10:
                continue

            log_keff = np.log(np.array(p_keffs))
            log_eta = np.log(np.array(p_etas) + EPS)
            y = np.log(p_asrs + EPS)

            X = sm.add_constant(np.column_stack([log_keff, log_eta]))
            fit = sm.OLS(y, X).fit()

            n_clusters_per_pos = []
            for pos in range(K):
                cids = np.array([jids[pos] for jids in panel_jids_list])
                n_clusters_per_pos.append(len(np.unique(cids)))

            all_cond_data[cond] = {
                "y": y,
                "X": X,
                "log_keff": log_keff,
                "log_eta": log_eta,
                "panel_jids_list": panel_jids_list,
                "n_panels": n_panels,
                "R2": fit.rsquared,
                "intercept": fit.params[0],
                "beta_keff_actual": fit.params[1],
                "beta_eta": fit.params[2],
                "sigma_resid": np.sqrt(fit.mse_resid),
                "sd_y": np.std(y),
                "sd_log_keff": np.std(log_keff),
                "n_clusters_per_pos": n_clusters_per_pos,
            }

    logger.info(f"  Built {len(all_cond_data)} conditions for K={K}")
    return all_cond_data


# ── Power analysis ───────────────────────────────────────────────────

def run_mde_power(K, cond_data_dict, n_sim, n_boot, rng):
    cond_keys = sorted(cond_data_dict.keys())
    n_conds = len(cond_keys)

    ref_cond = cond_keys[0]
    cl_info = cond_data_dict[ref_cond]["n_clusters_per_pos"]
    logger.info(f"  K={K}: {n_conds} conditions, clusters/pos={cl_info}")

    power_per_cond = {str(b): [] for b in BETA_STD_GRID}

    for ci, cond in enumerate(cond_keys):
        d = cond_data_dict[cond]
        t_cond = time.time()

        cond_power = batched_wcb_power(
            X=d["X"],
            log_keff=d["log_keff"],
            log_eta=d["log_eta"],
            intercept=d["intercept"],
            beta_eta=d["beta_eta"],
            sigma=d["sigma_resid"],
            panel_jids_list=d["panel_jids_list"],
            K=K,
            beta_std_grid=BETA_STD_GRID,
            n_sim=n_sim,
            n_boot=n_boot,
            rng=rng,
            batch_size=200,
        )

        for b in BETA_STD_GRID:
            power_per_cond[str(b)].append(cond_power[str(b)])

        dt = time.time() - t_cond
        logger.info(f"    [{ci+1}/{n_conds}] {cond}: {dt:.1f}s, R2={d['R2']:.3f}, "
                    f"power@0.3={cond_power.get('0.3','?')}")

    # Average across conditions
    power_avg = {}
    for b in BETA_STD_GRID:
        vals = power_per_cond[str(b)]
        power_avg[str(b)] = round(float(np.mean(vals)), 4) if vals else 0.0

    betas = np.array(BETA_STD_GRID)
    powers = np.array([power_avg[str(b)] for b in BETA_STD_GRID])

    mde_80 = None
    if powers.max() >= 0.80 and powers.min() <= 0.80:
        try:
            f_interp = interp1d(powers, betas, kind='linear',
                                bounds_error=False, fill_value=np.nan)
            mde_80 = float(f_interp(0.80))
            if np.isnan(mde_80):
                mde_80 = None
            else:
                mde_80 = round(mde_80, 4)
        except Exception:
            pass
    elif powers[0] > 0.80:
        mde_80 = round(float(betas[0]), 4)

    logger.info(f"  K={K} avg power: {power_avg}")
    if mde_80 is not None:
        logger.info(f"  MDE@80%: {mde_80}")
    else:
        logger.info(f"  MDE@80%: not achievable (max power={powers.max():.3f})")

    return power_avg, mde_80


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n-sim", type=int, default=1000)
    parser.add_argument("--n-boot", type=int, default=999)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    n_sim = 5 if args.dry_run else args.n_sim
    n_boot = 99 if args.dry_run else args.n_boot

    logger.info("=" * 60)
    logger.info("Pool A MDE Power Analysis (Webb 6-point WCB)")
    logger.info(f"  n_sim={n_sim}, n_boot={n_boot}, seed={SEED}")
    logger.info(f"  beta_std grid: {BETA_STD_GRID}")
    logger.info(f"  Pool A: {POOL_A}")
    logger.info("=" * 60)

    t0 = time.time()
    rng = np.random.default_rng(SEED)

    logger.info("Loading data...")
    mi_matrices = load_mi_matrix()
    pairs = load_pairs()
    clean, attacked = load_pool_a_scores()
    n_loaded = sum(1 for ds in DATASETS for m in POOL_A if m in clean[ds])
    logger.info(f"  Loaded {n_loaded}/{len(POOL_A)*len(DATASETS)} clean score sets")

    logger.info("\nBuilding K=3 panel data...")
    data_k3 = build_panel_data(3, mi_matrices, clean, attacked, pairs)

    logger.info("\nBuilding K=5 panel data...")
    data_k5 = build_panel_data(5, mi_matrices, clean, attacked, pairs)

    logger.info("\n--- K=3 Power Analysis ---")
    power_k3, mde_k3 = run_mde_power(3, data_k3, n_sim, n_boot, rng)

    logger.info("\n--- K=5 Power Analysis ---")
    power_k5, mde_k5 = run_mde_power(5, data_k5, n_sim, n_boot, rng)

    elapsed = time.time() - t0

    ref_k3 = list(data_k3.values())[0]
    ref_k5 = list(data_k5.values())[0]

    output = {
        "pool_a_models": POOL_A,
        "pool_a_panels": {"K3": 84, "K5": 126},
        "beta_std_values": BETA_STD_GRID,
        "n_simulations": n_sim,
        "n_bootstrap": n_boot,
        "bootstrap_weights": "webb_6point",
        "seed": SEED,
        "clusters_per_position": {
            "K3": ref_k3["n_clusters_per_pos"],
            "K5": ref_k5["n_clusters_per_pos"],
        },
        "power_by_beta": {
            "K3": power_k3,
            "K5": power_k5,
        },
        "mde_at_80pct": {
            "K3": mde_k3,
            "K5": mde_k5,
        },
        "elapsed_seconds": round(elapsed, 1),
        "notes": (
            "Power per-condition then averaged across 12 conditions "
            "(2 datasets x 6 attacks). "
            "Wild cluster bootstrap with Webb 6-point weights, "
            f"B={n_boot}, max p-value across K judge positions. "
            "Regression: log(ASR+eps) ~ log(K_eff) + log(eta_max+eps). "
            "Few clusters per position (7 for K=3, 5 for K=5) make WCB "
            "very conservative, limiting detectable effect size."
        ),
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {OUT_PATH}")
    logger.info(f"Total time: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
