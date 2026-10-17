#!/usr/bin/env python3
"""A3: API-only power analysis + β_std comparison with full pool.

Compares β_std(K_eff) between full 15-model pool and API-only 9-model subset
to distinguish power insufficiency from genuine effect shrinkage.
"""

import json
import time
import itertools
import logging
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
API_INDICES = list(range(6, 15))
API_MODELS = [MI_MODELS[i] for i in API_INDICES]

DATASETS = ["mmlu", "arc_challenge"]
ATTACKS = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]
EPS = 1e-6
SEED = 42
BETA_STD_GRID = [0.1, 0.15, 0.2, 0.25, 0.3, 0.5, 0.7, 1.0]

WEBB_6 = np.array([
    -np.sqrt(3/2), -1.0, -np.sqrt(1/2),
     np.sqrt(1/2),  1.0,  np.sqrt(3/2),
])

BASE_DIR = Path("/root/cert_manip_resist_eval")
SCORES_DIR = BASE_DIR / "artifacts/results/plan001/individual_scores"
MI_PATH = BASE_DIR / "artifacts/results/plan001/mi_matrix/mi_matrix_15models.json"
CKPT_PATHS = [
    BASE_DIR / "artifacts/results/_taxonomy_checkpoint.json",
    BASE_DIR / "artifacts/results/_step2v3_checkpoint.json",
]
OUT_PATH = BASE_DIR / "artifacts/results/plan001/api_only_power_beta.json"

N_SIM = 500
N_BOOT_MDE = 499
N_BOOT_WCB = 999

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S",
    handlers=[
        logging.FileHandler("/tmp/api_only_power.log", mode="w"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("api_only_power")


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


# ── Data loading ─────────────────────────────────────────────────────

def load_mi_matrix():
    with open(MI_PATH) as f:
        data = json.load(f)
    return {ds: np.array(data["mi_matrix"][ds]) for ds in DATASETS}


def load_pairs():
    for ckpt_path in CKPT_PATHS:
        if ckpt_path.exists():
            with open(ckpt_path) as f:
                data = json.load(f)
            if "pairs" in data:
                return {ds: data["pairs"][ds][:300] for ds in DATASETS}
    raise FileNotFoundError("No pairs found")


def _invert_winners(scores):
    swap = {"A": "B", "B": "A", "tie": "tie"}
    return [{**s, "winner": swap.get(s.get("winner", "tie"), "tie")} for s in scores]


def load_all_scores():
    """Load scores for all 15 models from checkpoints + individual files."""
    clean = {ds: {} for ds in DATASETS}
    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}

    # Local models from checkpoints
    for ckpt_path in CKPT_PATHS:
        if not ckpt_path.exists():
            continue
        with open(ckpt_path) as f:
            data = json.load(f)
        for ds in DATASETS:
            for mid, scores in data.get("clean_scores", {}).get(ds, {}).items():
                if mid not in clean[ds]:
                    clean[ds][mid] = scores
            for atk in ATTACKS:
                for mid, scores in (
                    data.get("attacked_scores", {}).get(ds, {}).get(atk, {}).items()
                ):
                    if mid not in attacked[ds][atk]:
                        if atk == "position_bias":
                            scores = _invert_winners(scores)
                        attacked[ds][atk][mid] = scores

    # API models from individual files
    for mid in MI_MODELS:
        for ds in DATASETS:
            fp = SCORES_DIR / f"{mid}__{ds}__clean.json"
            if fp.exists() and mid not in clean[ds]:
                with open(fp) as f:
                    clean[ds][mid] = json.load(f).get("scores", [])
            for atk in ATTACKS:
                fp = SCORES_DIR / f"{mid}__{ds}__{atk}.json"
                if fp.exists() and mid not in attacked[ds][atk]:
                    with open(fp) as f:
                        scores = json.load(f).get("scores", [])
                    if atk == "position_bias":
                        scores = _invert_winners(scores)
                    attacked[ds][atk][mid] = scores

    return clean, attacked


# ── Core functions ───────────────────────────────────────────────────

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


# ── Wild cluster bootstrap ──────────────────────────────────────────

def wild_cluster_bootstrap(y, X, cluster_ids, B=N_BOOT_WCB, seed=SEED,
                           test_col_idx=1):
    n, p = X.shape
    unique_clusters = np.unique(cluster_ids)
    n_clusters = len(unique_clusters)

    cluster_to_idx = {c: i for i, c in enumerate(unique_clusters)}
    panel_cluster_idx = np.array([cluster_to_idx[c] for c in cluster_ids])

    fit_full = sm.OLS(y, X).fit()
    t_original = fit_full.tvalues[test_col_idx]

    cols_restricted = [i for i in range(p) if i != test_col_idx]
    X_restricted = X[:, cols_restricted]
    fit_restricted = sm.OLS(y, X_restricted).fit()
    y_hat_r = fit_restricted.fittedvalues
    e_r = y - y_hat_r

    rng = np.random.RandomState(seed)
    t_boot = np.empty(B)

    for b in range(B):
        w_cluster = rng.choice([-1, 1], size=n_clusters)
        w_panel = w_cluster[panel_cluster_idx]
        y_boot = y_hat_r + w_panel * e_r
        try:
            fit_b = sm.OLS(y_boot, X).fit()
            t_boot[b] = fit_b.tvalues[test_col_idx]
        except Exception:
            t_boot[b] = 0.0

    p_value = (1 + np.sum(np.abs(t_boot) >= np.abs(t_original))) / (1 + B)
    return float(p_value), n_clusters


# ── Panel data building ─────────────────────────────────────────────

def build_panel_data(K, model_list, model_indices, mi_matrices,
                     clean, attacked, pairs):
    """Build regression data for panels from given model subset.

    model_list: list of model name strings
    model_indices: corresponding indices in the 15-model MI matrix
    """
    combos = list(itertools.combinations(range(len(model_list)), K))
    n_panels = len(combos)
    logger.info(f"  K={K}: {n_panels} panels from {len(model_list)} models")

    all_cond_data = {}

    for ds in DATASETS:
        mi_mat = mi_matrices[ds]
        ds_pairs = pairs[ds]
        ds_clean = clean[ds]

        for atk in ATTACKS:
            cond = f"{ds}x{atk}"
            ds_attacked = attacked[ds][atk]

            # Individual ASRs
            ind_asr = {}
            for m in model_list:
                if m in ds_clean and m in ds_attacked:
                    ind_asr[m] = compute_individual_asr(
                        ds_clean[m], ds_attacked[m], ds_pairs
                    )

            p_asrs, p_keffs, p_etas = [], [], []
            panel_jids_list = []

            for combo in combos:
                jids = [model_list[i] for i in combo]
                if not all(j in ind_asr for j in jids):
                    continue
                if not all(j in ds_clean and j in ds_attacked for j in jids):
                    continue

                global_indices = [model_indices[i] for i in combo]
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

            n_valid = len(p_asrs)
            if n_valid < 10:
                logger.warning(f"  {cond}: only {n_valid} valid panels, skip")
                continue

            p_asrs = np.array(p_asrs)
            if np.std(p_asrs) < 1e-10:
                logger.warning(f"  {cond}: zero variance in ASR, skip")
                continue

            log_keff = np.log(np.array(p_keffs))
            log_eta = np.log(np.array(p_etas) + EPS)
            y = np.log(p_asrs + EPS)

            X = sm.add_constant(np.column_stack([log_keff, log_eta]))
            fit = sm.OLS(y, X).fit()

            sd_y = np.std(y)
            sd_lk = np.std(log_keff)
            keff_std_beta = fit.params[1] * sd_lk / sd_y if sd_y > 1e-10 else 0.0

            n_clusters_per_pos = []
            for pos in range(K):
                cids = np.array([jids[pos] for jids in panel_jids_list])
                n_clusters_per_pos.append(int(len(np.unique(cids))))

            all_cond_data[cond] = {
                "y": y,
                "X": X,
                "log_keff": log_keff,
                "log_eta": log_eta,
                "panel_jids_list": panel_jids_list,
                "n_panels": n_valid,
                "R2": float(fit.rsquared),
                "intercept": float(fit.params[0]),
                "beta_keff": float(fit.params[1]),
                "beta_eta": float(fit.params[2]),
                "keff_std_beta": float(keff_std_beta),
                "sigma_resid": float(np.sqrt(fit.mse_resid)),
                "sd_y": float(sd_y),
                "sd_log_keff": float(sd_lk),
                "n_clusters_per_pos": n_clusters_per_pos,
            }

    return all_cond_data


# ── WCB for observed data ───────────────────────────────────────────

def run_wcb_analysis(K, cond_data, B=N_BOOT_WCB):
    """Run wild cluster bootstrap on observed API-only data."""
    results = {}
    n_sig = 0

    for cond, d in sorted(cond_data.items()):
        y, X = d["y"], d["X"]
        panel_jids = d["panel_jids_list"]

        pos_ps = []
        pos_nclusters = []
        for pos in range(K):
            cids = [jids[pos] for jids in panel_jids]
            p_val, nc = wild_cluster_bootstrap(y, X, cids, B=B)
            pos_ps.append(p_val)
            pos_nclusters.append(nc)

        final_p = max(pos_ps)
        sig = final_p < 0.05

        results[cond] = {
            "keff_std_beta": d["keff_std_beta"],
            "keff_beta": d["beta_keff"],
            "R2": d["R2"],
            "n_panels": d["n_panels"],
            "wcb_pos_p": [round(p, 4) for p in pos_ps],
            "wcb_final_p": round(final_p, 4),
            "n_clusters_per_pos": pos_nclusters,
            "sig_05": sig,
        }
        if sig:
            n_sig += 1

        logger.info(f"    {cond}: β_std={d['keff_std_beta']:.4f} "
                     f"p={final_p:.4f} {'*' if sig else ''}")

    return results, n_sig


# ── MDE power analysis (vectorized) ─────────────────────────────────

def batched_wcb_power(X, log_keff, log_eta, intercept, beta_eta, sigma,
                      panel_jids_list, K, beta_std_grid, n_sim, n_boot,
                      rng, batch_size=100):
    n, p = X.shape
    sd_lk = np.std(log_keff)
    if sd_lk < 1e-10:
        return {str(b): 0.0 for b in beta_std_grid}

    XtX_inv = np.linalg.inv(X.T @ X)
    M_hat = XtX_inv @ X.T
    diag_keff = XtX_inv[1, 1]

    X_r = X[:, [0, 2]]
    M_hat_r = np.linalg.inv(X_r.T @ X_r) @ X_r.T

    position_clusters = []
    for pos in range(K):
        cids_raw = np.array([jids[pos] for jids in panel_jids_list])
        unique_c = np.unique(cids_raw)
        c2i = {c: i for i, c in enumerate(unique_c)}
        pci = np.array([c2i[c] for c in cids_raw])
        position_clusters.append((pci, len(unique_c)))

    results = {}

    for beta_std in beta_std_grid:
        beta_raw_approx = beta_std * sigma / sd_lk
        y_mean_signal = intercept + beta_raw_approx * log_keff + beta_eta * log_eta
        sd_y_dgp = np.sqrt(np.var(y_mean_signal) + sigma**2)
        beta_raw = beta_std * sd_y_dgp / sd_lk

        noise = rng.normal(0, sigma, size=(n_sim, n))
        Y_sim = (intercept
                 + beta_raw * log_keff[None, :]
                 + beta_eta * log_eta[None, :]
                 + noise)

        Beta_u = Y_sim @ M_hat.T
        Resid_u = Y_sim - Beta_u @ X.T
        Sigma2_u = np.sum(Resid_u ** 2, axis=1) / (n - p)
        T_obs = Beta_u[:, 1] / np.sqrt(Sigma2_u * diag_keff)

        Beta_r = Y_sim @ M_hat_r.T
        Y_hat_r = Beta_r @ X_r.T
        E_r = Y_sim - Y_hat_r

        sig_mask = np.ones(n_sim, dtype=bool)

        for pci, n_clusters in position_clusters:
            p_values = np.empty(n_sim)

            for start in range(0, n_sim, batch_size):
                end = min(start + batch_size, n_sim)
                bs = end - start

                W_cluster = rng.choice(WEBB_6, size=(bs, n_boot, n_clusters))
                W_panel = W_cluster[:, :, pci]

                Y_boot = Y_hat_r[start:end, None, :] + W_panel * E_r[start:end, None, :]

                Y_flat = Y_boot.reshape(bs * n_boot, n)
                Beta_flat = Y_flat @ M_hat.T
                Resid_flat = Y_flat - Beta_flat @ X.T
                S2_flat = np.sum(Resid_flat ** 2, axis=1) / (n - p)
                SE_flat = np.sqrt(np.maximum(S2_flat * diag_keff, 1e-30))
                T_flat = Beta_flat[:, 1] / SE_flat

                T_boot = T_flat.reshape(bs, n_boot)
                T_obs_batch = T_obs[start:end]

                exceed = np.sum(np.abs(T_boot) >= np.abs(T_obs_batch[:, None]),
                                axis=1)
                p_values[start:end] = (1 + exceed) / (1 + n_boot)

            sig_mask &= (p_values < 0.05)

        power = np.mean(sig_mask)
        results[str(beta_std)] = round(float(power), 4)

    return results


def run_mde_power(K, cond_data_dict, n_sim, n_boot, rng):
    cond_keys = sorted(cond_data_dict.keys())
    n_conds = len(cond_keys)

    logger.info(f"  K={K}: {n_conds} conditions, n_sim={n_sim}, n_boot={n_boot}")

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
            batch_size=100,
        )

        for b in BETA_STD_GRID:
            power_per_cond[str(b)].append(cond_power[str(b)])

        dt = time.time() - t_cond
        logger.info(f"    [{ci+1}/{n_conds}] {cond}: {dt:.1f}s "
                     f"power@0.3={cond_power.get('0.3','?')} "
                     f"power@0.5={cond_power.get('0.5','?')}")

    power_avg = {}
    for b in BETA_STD_GRID:
        vals = power_per_cond[str(b)]
        power_avg[str(b)] = round(float(np.mean(vals)), 4) if vals else 0.0

    betas = np.array(BETA_STD_GRID)
    powers = np.array([power_avg[str(b)] for b in BETA_STD_GRID])

    mde_80 = None
    if powers.max() >= 0.80 and powers.min() <= 0.80:
        try:
            f_interp = interp1d(powers, betas, kind="linear",
                                bounds_error=False, fill_value=np.nan)
            mde_80 = float(f_interp(0.80))
            if np.isnan(mde_80):
                mde_80 = None
            else:
                mde_80 = round(mde_80, 4)
        except Exception:
            pass
    elif len(powers) > 0 and powers[0] > 0.80:
        mde_80 = round(float(betas[0]), 4)

    return power_avg, mde_80


# ── Main ─────────────────────────────────────────────────────────────

def main():
    t0 = time.time()

    logger.info("=" * 60)
    logger.info("A3: API-only Power Analysis + β_std Comparison")
    logger.info(f"  API models: {API_MODELS}")
    logger.info(f"  n_sim={N_SIM}, n_boot_mde={N_BOOT_MDE}, n_boot_wcb={N_BOOT_WCB}")
    logger.info("=" * 60)

    logger.info("Loading data...")
    mi_matrices = load_mi_matrix()
    pairs = load_pairs()
    clean, attacked = load_all_scores()

    n_api = sum(1 for ds in DATASETS for m in API_MODELS if m in clean[ds])
    n_all = sum(1 for ds in DATASETS for m in MI_MODELS if m in clean[ds])
    logger.info(f"  Loaded: {n_all}/{len(MI_MODELS)*2} full, "
                f"{n_api}/{len(API_MODELS)*2} API clean score sets")

    rng = np.random.default_rng(SEED)
    K_values = [3, 5, 7]

    beta_std_comparison = {}
    api_wcb_results = {}
    api_sig_counts = {}
    api_mde = {}
    api_power = {}
    full_pool_panels = {}
    api_only_panels = {}

    for K in K_values:
        logger.info(f"\n{'='*60}")
        logger.info(f"K={K}")
        logger.info(f"{'='*60}")

        # Full pool panels
        logger.info(f"\n--- Full pool K={K} ---")
        full_data = build_panel_data(
            K, MI_MODELS, list(range(15)), mi_matrices, clean, attacked, pairs
        )
        full_pool_panels[f"K{K}"] = (
            len(list(itertools.combinations(range(15), K)))
        )

        # API-only panels
        logger.info(f"\n--- API-only K={K} ---")
        api_data = build_panel_data(
            K, API_MODELS, API_INDICES, mi_matrices, clean, attacked, pairs
        )
        api_only_panels[f"K{K}"] = (
            len(list(itertools.combinations(range(9), K)))
        )

        # β_std comparison per condition
        k_comparison = {}
        full_betas = []
        api_betas = []

        for cond in sorted(set(full_data.keys()) | set(api_data.keys())):
            fb = full_data[cond]["keff_std_beta"] if cond in full_data else None
            ab = api_data[cond]["keff_std_beta"] if cond in api_data else None
            k_comparison[cond] = {
                "full_pool": round(fb, 4) if fb is not None else None,
                "api_only": round(ab, 4) if ab is not None else None,
            }
            if fb is not None:
                full_betas.append(fb)
            if ab is not None:
                api_betas.append(ab)

        avg_full = float(np.mean(full_betas)) if full_betas else None
        avg_api = float(np.mean(api_betas)) if api_betas else None
        ratio = avg_api / avg_full if avg_full and avg_api and abs(avg_full) > 1e-10 else None

        beta_std_comparison[f"K{K}"] = {
            "per_condition": k_comparison,
            "avg_full_pool": round(avg_full, 4) if avg_full is not None else None,
            "avg_api_only": round(avg_api, 4) if avg_api is not None else None,
            "ratio": round(ratio, 4) if ratio is not None else None,
        }

        logger.info(f"\n  β_std avg: full={avg_full:.4f}, "
                     f"api={avg_api:.4f}, ratio={ratio:.4f}")

        # WCB on API-only observed data
        if api_data:
            logger.info(f"\n--- WCB for API-only K={K} ---")
            wcb_res, n_sig = run_wcb_analysis(K, api_data, B=N_BOOT_WCB)
            api_wcb_results[f"K{K}"] = wcb_res
            api_sig_counts[f"K{K}"] = f"{n_sig}/12"
        else:
            api_sig_counts[f"K{K}"] = "0/12"

        # MDE power for API-only
        if api_data:
            logger.info(f"\n--- MDE Power for API-only K={K} ---")
            power_k, mde_k = run_mde_power(K, api_data, N_SIM, N_BOOT_MDE, rng)
            api_mde[f"K{K}"] = mde_k
            api_power[f"K{K}"] = power_k
        else:
            api_mde[f"K{K}"] = None
            api_power[f"K{K}"] = {}

    # Interpretation
    ratios = [
        beta_std_comparison[f"K{K}"].get("ratio")
        for K in K_values
        if beta_std_comparison[f"K{K}"].get("ratio") is not None
    ]
    avg_ratio = float(np.mean(ratios)) if ratios else None

    if avg_ratio is not None:
        if avg_ratio < 0.5:
            interpretation = "effect_shrinkage"
            explanation = (
                f"API-only β_std is {avg_ratio:.0%} of full pool — "
                "effect genuinely shrinks when removing local AWQ models, "
                "not just a power issue."
            )
        elif avg_ratio > 0.75:
            interpretation = "power_issue"
            explanation = (
                f"API-only β_std is {avg_ratio:.0%} of full pool — "
                "effect size preserved, low significance is due to "
                "fewer panels / clusters."
            )
        else:
            interpretation = "both"
            explanation = (
                f"API-only β_std is {avg_ratio:.0%} of full pool — "
                "moderate effect shrinkage combined with reduced power."
            )
    else:
        interpretation = "unknown"
        explanation = "Could not compute ratio."

    elapsed = time.time() - t0

    output = {
        "api_models": API_MODELS,
        "full_pool_models": MI_MODELS,
        "api_only_panels": api_only_panels,
        "full_pool_panels": full_pool_panels,
        "beta_std_comparison": beta_std_comparison,
        "api_only_sig_count": api_sig_counts,
        "api_only_wcb_details": api_wcb_results,
        "api_only_mde_80pct": api_mde,
        "api_only_power_by_beta": api_power,
        "interpretation": interpretation,
        "explanation": explanation,
        "avg_beta_std_ratio": round(avg_ratio, 4) if avg_ratio is not None else None,
        "config": {
            "n_sim": N_SIM,
            "n_boot_mde": N_BOOT_MDE,
            "n_boot_wcb": N_BOOT_WCB,
            "seed": SEED,
            "eps": EPS,
            "beta_std_grid": BETA_STD_GRID,
        },
        "elapsed_seconds": round(elapsed, 1),
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)
    logger.info(f"\nSaved: {OUT_PATH}")
    logger.info(f"Total time: {elapsed:.1f}s")
    logger.info(f"Interpretation: {interpretation}")
    logger.info(f"  {explanation}")


if __name__ == "__main__":
    main()
