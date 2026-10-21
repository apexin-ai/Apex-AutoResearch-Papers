#!/usr/bin/env python3
"""Fractional Logit V2 Data Audit.

GLM(Binomial, logit) with max-p clustered SE for K=3,5,7.
Uses V2 corrected data (model names from MI matrix).
"""

import os
os.environ["HF_HOME"] = "/root/autodl-tmp/.hf_cache"

import sys
sys.path.insert(0, "/root/cert_manip_resist_eval")

import json
import time
import logging
import itertools
import warnings
import numpy as np
import statsmodels.api as sm
from pathlib import Path
from statsmodels.genmod.families import Binomial
from statsmodels.stats.multitest import multipletests

warnings.filterwarnings("ignore", category=RuntimeWarning)

# ── Config ───────────────────────────────────────────────────────────

V2_MODELS = [
    "qwen2.5-72b", "llama3.1-70b", "mistral-large",
    "qwen2.5-32b", "qwen2.5-14b", "llama3.1-8b",
    "claude-opus-4-6", "gpt-5.5", "gemini-3.1-pro-preview", "gpt-4.1",
    "claude-sonnet-4-6", "gpt-4.1-nano", "gemini-3.5-flash",
    "gpt-4.1-mini", "claude-3-haiku",
]
LOCAL_MODELS = set(V2_MODELS[:6])
API_V2 = V2_MODELS[6:]

DATASETS = ["mmlu", "arc_challenge"]
ATTACKS = [
    "prompt_injection", "sycophancy", "score_manipulation",
    "verbosity_bias", "position_bias", "authority_bias",
]

SCORES_DIR = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/individual_scores")
MI_PATH = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/mi_matrix/mi_matrix_15models.json")
CKPT_FILES = [
    Path("/root/cert_manip_resist_eval/artifacts/results/_taxonomy_checkpoint.json"),
    Path("/root/cert_manip_resist_eval/artifacts/results/_step2v3_checkpoint.json"),
]
OUT_PATH = Path("/root/cert_manip_resist_eval/artifacts/results/plan001/fractional_logit_v2.json")

EPS = 1e-6
FDR_ALPHA = 0.05
LOG_PATH = "/tmp/fractional_logit_v2.log"

V1_TO_V2 = {
    "claude-opus-4": "claude-opus-4-6",
    "claude-sonnet-4": "claude-sonnet-4-6",
    "gemini-2.5-pro": "gemini-3.1-pro-preview",
    "gpt-4o": "gpt-4.1-nano",
    "gemini-2.5-flash": "gemini-3.5-flash",
    "gpt-4o-mini": "gpt-4.1-mini",
}

# ── Logging ──────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_PATH, mode="w"),
        logging.StreamHandler(),
    ],
)
logger = logging.getLogger("frac_logit_v2")


# ── Helpers ──────────────────────────────────────────────────────────

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


def _is_valid(s):
    if s.get("error") or s.get("format_error"):
        return False
    return s.get("winner") in ("A", "B", "tie")


def _invert(scores):
    swap = {"A": "B", "B": "A", "tie": "tie"}
    return [{**s, "winner": swap.get(s.get("winner", "tie"), "tie")} for s in scores]


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


# ── Data Loading ─────────────────────────────────────────────────────

def load_v2_scores():
    clean = {ds: {} for ds in DATASETS}
    attacked = {ds: {a: {} for a in ATTACKS} for ds in DATASETS}

    for ckpt_path in CKPT_FILES:
        if not ckpt_path.exists():
            continue
        with open(ckpt_path) as f:
            data = json.load(f)
        for ds in DATASETS:
            for mid, scores in data.get("clean_scores", {}).get(ds, {}).items():
                v2 = V1_TO_V2.get(mid, mid)
                if v2 in LOCAL_MODELS and v2 not in clean[ds]:
                    clean[ds][v2] = scores
            for atk in ATTACKS:
                for mid, scores in (
                    data.get("attacked_scores", {}).get(ds, {}).get(atk, {}).items()
                ):
                    v2 = V1_TO_V2.get(mid, mid)
                    if v2 in LOCAL_MODELS and v2 not in attacked[ds][atk]:
                        if atk == "position_bias":
                            scores = _invert(scores)
                        attacked[ds][atk][v2] = scores

    for mid in API_V2:
        for ds in DATASETS:
            fp = SCORES_DIR / f"{mid}__{ds}__clean.json"
            if fp.exists() and mid not in clean[ds]:
                with open(fp) as f:
                    clean[ds][mid] = json.load(f).get("scores", [])
            for atk in ATTACKS:
                fp = SCORES_DIR / f"{mid}__{ds}__{atk}.json"
                if fp.exists() and mid not in attacked[ds][atk]:
                    with open(fp) as f:
                        attacked[ds][atk][mid] = json.load(f).get("scores", [])

    return clean, attacked


def load_pairs():
    for ckpt_path in CKPT_FILES:
        if not ckpt_path.exists():
            continue
        with open(ckpt_path) as f:
            data = json.load(f)
        if "pairs" not in data:
            continue
        pairs = {}
        for ds in DATASETS:
            if ds in data["pairs"]:
                pairs[ds] = data["pairs"][ds][:300]
        if pairs:
            return pairs
    raise FileNotFoundError("No pairs found")


# ── ASR ──────────────────────────────────────────────────────────────

def individual_asr(cl, at, pairs):
    n = min(len(cl), len(at), len(pairs))
    flips = correct = 0
    for i in range(n):
        if not _is_valid(cl[i]) or not _is_valid(at[i]):
            continue
        gt = pairs[i]["ground_truth_winner"]
        if cl[i]["winner"] == gt:
            correct += 1
            if at[i]["winner"] != gt:
                flips += 1
    return flips / max(correct, 1)


def panel_asr(jids, clean, attacked, pairs):
    n = min(len(pairs), *(len(clean[j]) for j in jids),
            *(len(attacked[j]) for j in jids))
    flips = correct = 0
    for i in range(n):
        if not all(_is_valid(clean[j][i]) for j in jids):
            continue
        if not all(_is_valid(attacked[j][i]) for j in jids):
            continue
        gt = pairs[i]["ground_truth_winner"]
        cv = majority_vote([clean[j][i]["winner"] for j in jids])
        if cv != gt:
            continue
        correct += 1
        av = majority_vote([attacked[j][i]["winner"] for j in jids])
        if av != gt:
            flips += 1
    return flips / max(correct, 1)


def mi_keff(mi_mat, indices):
    K = len(indices)
    if K <= 1:
        return 1.0
    total = 0.0
    for i in indices:
        term = 1.0
        for j in indices:
            if i != j:
                term += np.exp(-2 * mi_mat[i, j])
        total += term
    return total / K


# ── Fractional Logit ─────────────────────────────────────────────────

def fit_fractional_logit(y, X, combos, K):
    model = sm.GLM(y, X, family=Binomial())
    try:
        base = model.fit(maxiter=200, method='IRLS')
    except Exception as e:
        logger.warning(f"GLM base fit failed: {e}")
        return None

    if not base.converged:
        logger.warning("GLM did not converge")

    n_coefs = X.shape[1]
    max_se = np.zeros(n_coefs)
    max_pv = base.pvalues.copy()

    for j in range(K):
        groups = np.array([c[j] for c in combos])
        n_clusters = len(np.unique(groups))
        if n_clusters < 3:
            continue
        try:
            cl = model.fit(cov_type='cluster', cov_kwds={'groups': groups},
                           maxiter=200, method='IRLS')
            for c in range(n_coefs):
                if cl.bse[c] > max_se[c]:
                    max_se[c] = cl.bse[c]
                    max_pv[c] = cl.pvalues[c]
        except Exception:
            continue

    null_dev = base.null_deviance if hasattr(base, 'null_deviance') and base.null_deviance else 1.0
    pseudo_r2 = 1 - base.deviance / null_dev if null_dev > 0 else 0.0

    return {
        "keff_coef": float(base.params[1]),
        "keff_base_se": float(base.bse[1]),
        "keff_base_p": float(base.pvalues[1]),
        "keff_cl_se": float(max_se[1]) if max_se[1] > 0 else float(base.bse[1]),
        "keff_p": float(max_pv[1]) if max_se[1] > 0 else float(base.pvalues[1]),
        "eta_coef": float(base.params[2]),
        "eta_base_se": float(base.bse[2]),
        "eta_base_p": float(base.pvalues[2]),
        "eta_cl_se": float(max_se[2]) if max_se[2] > 0 else float(base.bse[2]),
        "eta_p": float(max_pv[2]) if max_se[2] > 0 else float(base.pvalues[2]),
        "intercept": float(base.params[0]),
        "pseudo_r2": float(pseudo_r2),
        "converged": bool(base.converged),
        "n_obs": len(y),
        "se_inflation_keff": float(max_se[1] / base.bse[1]) if base.bse[1] > 0 and max_se[1] > 0 else 1.0,
        "se_inflation_eta": float(max_se[2] / base.bse[2]) if base.bse[2] > 0 and max_se[2] > 0 else 1.0,
    }


# ── Main ─────────────────────────────────────────────────────────────

def main():
    t0 = time.time()
    logger.info("=" * 70)
    logger.info("Fractional Logit V2 Data Audit")
    logger.info("=" * 70)

    clean, attacked = load_v2_scores()
    pairs = load_pairs()
    mi_data = json.load(open(MI_PATH))
    mi_models = mi_data["models"]
    assert mi_models == V2_MODELS, f"Model mismatch: {mi_models}"

    mi_mats = {ds: np.array(mi_data["mi_matrix"][ds]) for ds in DATASETS}

    n_loaded = sum(1 for ds in DATASETS for mid in V2_MODELS if mid in clean[ds])
    logger.info(f"Loaded {n_loaded}/{len(V2_MODELS)*len(DATASETS)} clean score sets")

    missing = []
    for ds in DATASETS:
        for mid in V2_MODELS:
            if mid not in clean[ds]:
                missing.append(f"clean:{ds}/{mid}")
            for atk in ATTACKS:
                if mid not in attacked[ds][atk]:
                    missing.append(f"atk:{ds}/{atk}/{mid}")
    if missing:
        for m in missing[:10]:
            logger.warning(f"MISSING {m}")
        if len(missing) > 10:
            logger.warning(f"... and {len(missing)-10} more missing")

    logger.info("Computing individual ASR...")
    ind_asr = {}
    for ds in DATASETS:
        for atk in ATTACKS:
            for mid in V2_MODELS:
                if mid in clean[ds] and mid in attacked[ds][atk]:
                    ind_asr[(ds, atk, mid)] = individual_asr(
                        clean[ds][mid], attacked[ds][atk][mid], pairs[ds])
    logger.info(f"  {len(ind_asr)} individual ASR values")

    # ── K=5 mmlu×sycophancy diagnostic ──
    logger.info("\n--- DIAGNOSTIC: K=5 mmlu x sycophancy ---")
    diag_combos = list(itertools.combinations(range(15), 5))
    diag_asrs, diag_keffs, diag_etas = [], [], []
    ds_d, atk_d = "mmlu", "sycophancy"
    for combo in diag_combos:
        jids = [V2_MODELS[i] for i in combo]
        try:
            a = panel_asr(jids, clean[ds_d], attacked[ds_d][atk_d], pairs[ds_d])
        except Exception:
            continue
        k = mi_keff(mi_mats[ds_d], combo)
        e = max(ind_asr.get((ds_d, atk_d, m), 0.0) for m in jids)
        diag_asrs.append(a)
        diag_keffs.append(k)
        diag_etas.append(e)

    diag_y = np.clip(np.array(diag_asrs), EPS, 1 - EPS)
    diag_X = sm.add_constant(np.column_stack([np.log(diag_keffs), np.log(np.array(diag_etas) + EPS)]))
    diag_res = fit_fractional_logit(diag_y, diag_X, diag_combos, 5)
    if diag_res:
        logger.info(f"  n={diag_res['n_obs']}, keff_coef={diag_res['keff_coef']:+.4f} "
                    f"(p={diag_res['keff_p']:.2e}), eta_coef={diag_res['eta_coef']:+.4f} "
                    f"(p={diag_res['eta_p']:.2e}), pseudo-R2={diag_res['pseudo_r2']:.4f}")
        logger.info(f"  SE inflation: keff={diag_res['se_inflation_keff']:.2f}x, "
                    f"eta={diag_res['se_inflation_eta']:.2f}x")
    logger.info("--- END DIAGNOSTIC ---\n")

    # ── Full analysis ──
    results_by_K = {}

    for K in [3, 5, 7]:
        logger.info(f"\n{'='*70}")
        all_combos = list(itertools.combinations(range(15), K))
        n_total = len(all_combos)
        logger.info(f"K={K}: {n_total} panels")

        raw_keff_ps, raw_eta_ps, valid_keys = [], [], []
        cond_res = {}

        for ds in DATASETS:
            mi_mat = mi_mats[ds]
            for atk in ATTACKS:
                cond = f"{ds}x{atk}"
                avail = [m for m in V2_MODELS
                         if m in clean[ds] and m in attacked[ds][atk]]
                if len(avail) < 15:
                    logger.warning(f"  {cond}: {len(avail)}/15 models, skip")
                    continue

                t1 = time.time()
                asrs, keffs, etas, valids = [], [], [], []
                for combo in all_combos:
                    jids = [V2_MODELS[i] for i in combo]
                    try:
                        a = panel_asr(jids, clean[ds], attacked[ds][atk], pairs[ds])
                    except Exception:
                        continue
                    asrs.append(a)
                    keffs.append(mi_keff(mi_mat, combo))
                    etas.append(max(ind_asr.get((ds, atk, m), 0.0) for m in jids))
                    valids.append(combo)

                n_p = len(valids)
                if n_p < 20:
                    logger.warning(f"  {cond}: only {n_p} panels, skip")
                    continue

                asrs = np.array(asrs)
                y = np.clip(asrs, EPS, 1 - EPS)
                log_k = np.log(np.array(keffs))
                log_e = np.log(np.array(etas) + EPS)
                X = sm.add_constant(np.column_stack([log_k, log_e]))

                res = fit_fractional_logit(y, X, valids, K)
                if res is None:
                    continue

                cond_res[cond] = {
                    "benchmark": ds, "attack": atk,
                    "n_panels": n_p,
                    **res,
                    "asr_mean": float(np.mean(asrs)),
                    "asr_std": float(np.std(asrs)),
                    "asr_pct_zero": float(np.mean(asrs == 0)),
                    "asr_pct_one": float(np.mean(asrs >= 1.0 - EPS)),
                }

                raw_keff_ps.append(res["keff_p"])
                raw_eta_ps.append(res["eta_p"])
                valid_keys.append(cond)

                elapsed = time.time() - t1
                logger.info(
                    f"  {cond:<35} n={n_p:>5}  "
                    f"keff={res['keff_coef']:+.4f} (p={res['keff_p']:.2e})  "
                    f"eta={res['eta_coef']:+.4f} (p={res['eta_p']:.2e})  "
                    f"R2={res['pseudo_r2']:.4f}  [{elapsed:.1f}s]"
                )

        # FDR
        n_cond = len(valid_keys)
        if n_cond > 0:
            _, fdr_k, _, _ = multipletests(raw_keff_ps, method="fdr_bh")
            _, fdr_e, _, _ = multipletests(raw_eta_ps, method="fdr_bh")
            for i, ck in enumerate(valid_keys):
                cond_res[ck]["keff_fdr_p"] = float(fdr_k[i])
                cond_res[ck]["keff_fdr_sig"] = bool(fdr_k[i] < FDR_ALPHA)
                cond_res[ck]["eta_fdr_p"] = float(fdr_e[i])
                cond_res[ck]["eta_fdr_sig"] = bool(fdr_e[i] < FDR_ALPHA)

        k_sig = sum(1 for ck in valid_keys if cond_res[ck].get("keff_fdr_sig", False))
        k_pos = all(cond_res[ck]["keff_coef"] > 0 for ck in valid_keys) if valid_keys else False
        e_sig = sum(1 for ck in valid_keys if cond_res[ck].get("eta_fdr_sig", False))

        results_by_K[f"K{K}"] = {
            "keff_sig_fdr": f"{k_sig}/{n_cond}",
            "keff_all_positive": k_pos,
            "eta_sig_fdr": f"{e_sig}/{n_cond}",
            "conditions": [
                {
                    "benchmark": cond_res[ck]["benchmark"],
                    "attack": cond_res[ck]["attack"],
                    "keff_coef": cond_res[ck]["keff_coef"],
                    "keff_p": cond_res[ck]["keff_p"],
                    "keff_fdr_p": cond_res[ck].get("keff_fdr_p"),
                    "keff_fdr_sig": cond_res[ck].get("keff_fdr_sig"),
                    "eta_coef": cond_res[ck]["eta_coef"],
                    "eta_p": cond_res[ck]["eta_p"],
                    "eta_fdr_p": cond_res[ck].get("eta_fdr_p"),
                    "eta_fdr_sig": cond_res[ck].get("eta_fdr_sig"),
                    "pseudo_r2": cond_res[ck]["pseudo_r2"],
                    "n_panels": cond_res[ck]["n_panels"],
                    "se_inflation_keff": cond_res[ck]["se_inflation_keff"],
                    "se_inflation_eta": cond_res[ck]["se_inflation_eta"],
                }
                for ck in valid_keys
            ],
        }

        logger.info(f"\nK={K} SUMMARY: keff_sig={k_sig}/{n_cond} FDR, "
                    f"all_positive={k_pos}, eta_sig={e_sig}/{n_cond}")

    # ── Output ──
    output = {
        "method": "fractional_logit_glm_binomial_clustered_se",
        "data_version": "V2 corrected",
        "data_source_file": str(SCORES_DIR),
        "mi_matrix_file": str(MI_PATH),
        "v2_models": V2_MODELS,
        "regression_spec": "GLM(ASR ~ log(K_eff) + log(eta_max + eps), family=Binomial(), link=logit)",
        "clustering": "max-p across K judge positions",
        "fdr_method": "Benjamini-Hochberg",
        "fdr_alpha": FDR_ALPHA,
        "eps": EPS,
        "results_by_K": results_by_K,
        "comparison_with_paper": {
            "paper_claims": {"K3": "9/12", "K5": "11/12", "K7": "12/12"},
            "registry_v1": {"K3": "4/12", "K5": "9/12", "K7": "10/12"},
            "actual_v2": {
                f"K{K}": results_by_K[f"K{K}"]["keff_sig_fdr"]
                for K in [3, 5, 7] if f"K{K}" in results_by_K
            },
            "discrepancy": "see actual_v2 vs paper_claims",
        },
        "adaptive_r2": {
            "value_found": None,
            "source_file": None,
            "paper_claims": 0.275,
            "registry_claims": 0.256,
            "note": "No adaptive R2 / random forest R2 data found in plan001 results"
        },
        "elapsed_seconds": time.time() - t0,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2, default=_json_default, ensure_ascii=False)

    logger.info(f"\nSaved: {OUT_PATH}")
    logger.info(f"Total: {output['elapsed_seconds']:.0f}s")

    logger.info("\n" + "=" * 70)
    logger.info("COMPARISON")
    logger.info("=" * 70)
    for K in [3, 5, 7]:
        kl = f"K{K}"
        if kl in results_by_K:
            a = results_by_K[kl]["keff_sig_fdr"]
            p = output["comparison_with_paper"]["paper_claims"][kl]
            r = output["comparison_with_paper"]["registry_v1"][kl]
            logger.info(f"  K={K}: actual_v2={a}  paper={p}  registry_v1={r}")


if __name__ == "__main__":
    main()
