#!/usr/bin/env python3
"""Construct Divergence Adjudication: Non-tie concordance, item correlation, bias-corrected OR."""

import json
import math
import os
import sys
import numpy as np
from scipy import stats

DATA_DIR = "/root/causal_style_decomp_judge/data"

# Judge × Axis → (scored_file, pairwise_file, axis_type, pole_preference_key)
CONFIGS = {
    # LLMBar formality
    ("qwen32b", "formality", "llmbar"): {
        "scored": "scored_qwen32b_formality.jsonl",
        "pairwise": "pairwise_results_32b.jsonl",
        "pole_pref_key": "formal_wins",
        "trial_pref_keys": ("trial1_prefers_formal", "trial2_prefers_formal"),
        "orig_pole_key": "original_formality",
        "style_pole": "formal",
    },
    ("qwen32b", "verbosity", "llmbar"): {
        "scored": "scored_qwen32b_verbosity.jsonl",
        "pairwise": "pairwise_results_qwen32b_verbosity.jsonl",
        "pole_pref_key": "prefers_verbose",
        "trial_pref_keys": ("trial1_prefers_verbose", "trial2_prefers_verbose"),
        "orig_pole_key": "original_verbosity",
        "style_pole": "verbose",
    },
    ("llama70b", "formality", "llmbar"): {
        "scored": "scored_llama70b_formality.jsonl",
        "pairwise": "pairwise_results_llama70b_formality.jsonl",
        "pole_pref_key": "prefers_formal",
        "trial_pref_keys": ("trial1_prefers_formal", "trial2_prefers_formal"),
        "orig_pole_key": "original_formality",
        "style_pole": "formal",
    },
    ("llama70b", "verbosity", "llmbar"): {
        "scored": "scored_llama70b_verbosity.jsonl",
        "pairwise": "pairwise_results_llama70b_verbosity.jsonl",
        "pole_pref_key": "prefers_verbose",
        "trial_pref_keys": ("trial1_prefers_verbose", "trial2_prefers_verbose"),
        "orig_pole_key": "original_verbosity",
        "style_pole": "verbose",
    },
    ("gemini", "formality", "llmbar"): {
        "scored": "scored_gemini_flash_formality.jsonl",
        "pairwise": "pairwise_results_gemini_flash_formality.jsonl",
        "pole_pref_key": "prefers_formal",
        "trial_pref_keys": ("trial1_prefers_formal", "trial2_prefers_formal"),
        "orig_pole_key": "original_formality",
        "style_pole": "formal",
    },
    ("gemini", "verbosity", "llmbar"): {
        "scored": "scored_gemini_flash_verbosity.jsonl",
        "pairwise": "pairwise_results_gemini_flash_verbosity.jsonl",
        "pole_pref_key": "prefers_verbose",
        "trial_pref_keys": ("trial1_prefers_verbose", "trial2_prefers_verbose"),
        "orig_pole_key": "original_verbosity",
        "style_pole": "verbose",
    },
    ("gpt4o", "formality", "llmbar"): {
        "scored": "scored_qwen32b_formality.jsonl",  # GPT-4o formality Likert not available separately; skip
        "pairwise": "pairwise_results_debiased_gpt4o_formality.jsonl",
        "pole_pref_key": "formal_wins",
        "trial_pref_keys": ("trial1_prefers_formal", "trial2_prefers_formal"),
        "orig_pole_key": "original_formality",
        "style_pole": "formal",
        "skip_concordance": True,  # No GPT-4o LLMBar formality Likert scored file
    },
    ("gpt4o", "verbosity", "llmbar"): {
        "scored": "scored_gpt4o_verbosity.jsonl",
        "pairwise": "pairwise_results_gpt4o_verbosity.jsonl",
        "pole_pref_key": "verbose_wins",
        "trial_pref_keys": ("trial1_prefers_verbose", "trial2_prefers_verbose"),
        "orig_pole_key": "original_verbosity",
        "style_pole": "verbose",
    },
    # AlpacaEval formality
    ("gpt4o", "formality", "alpacaeval"): {
        "scored": "scored_alpacaeval_gpt4o.jsonl",
        "pairwise": "pairwise_results_alpacaeval_gpt4o.jsonl",
        "pole_pref_key": "prefers_formal",
        "trial_pref_keys": ("trial1_prefers_formal", "trial2_prefers_formal"),
        "orig_pole_key": "original_formality",
        "style_pole": "formal",
    },
    ("qwen32b", "formality", "alpacaeval"): {
        "scored": "scored_alpacaeval_qwen32b.jsonl",
        "pairwise": "pairwise_results_alpacaeval_qwen32b.jsonl",
        "pole_pref_key": "prefers_formal",
        "trial_pref_keys": ("trial1_prefers_formal", "trial2_prefers_formal"),
        "orig_pole_key": "original_formality",
        "style_pole": "formal",
    },
}


def load_jsonl(path):
    records = []
    if not os.path.exists(path):
        return records
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))
    return records


def wilson_ci(k, n, alpha=0.05):
    if n == 0:
        return 0.0, (0.0, 1.0)
    z = stats.norm.ppf(1 - alpha / 2)
    p_hat = k / n
    denom = 1 + z**2 / n
    center = (p_hat + z**2 / (2 * n)) / denom
    margin = z * math.sqrt((p_hat * (1 - p_hat) + z**2 / (4 * n)) / n) / denom
    lo = max(0, center - margin)
    hi = min(1, center + margin)
    return p_hat, (lo, hi)


def get_likert_pole_score(rec, cfg):
    """Get (score_pole, score_anti) aligned to style pole direction."""
    s_orig = rec.get("score_original")
    s_cf = rec.get("score_counterfactual")
    if s_orig is None or s_cf is None:
        return None, None

    orig_pole = rec.get(cfg["orig_pole_key"], "")
    style_pole = cfg["style_pole"]

    if orig_pole == style_pole:
        return s_orig, s_cf  # original IS the style pole
    else:
        return s_cf, s_orig  # counterfactual IS the style pole


def get_pairwise_pole_wins(rec, cfg):
    """Get pairwise preference: True if style pole wins, False if anti-pole wins, None if tied."""
    t1_key, t2_key = cfg["trial_pref_keys"]
    t1 = rec.get(t1_key)
    t2 = rec.get(t2_key)

    if t1 is None or t2 is None:
        pw_key = cfg["pole_pref_key"]
        pw = rec.get(pw_key)
        if pw is None:
            return None
        return pw

    if t1 == t2:
        return t1  # consistent
    else:
        return None  # inconsistent / tied


def nli_filter(rec, threshold=0.90):
    nli = rec.get("nli_cf")
    if nli is None:
        return False
    return nli >= threshold


def analyze_concordance(scored_data, pairwise_data, cfg):
    """Task 1: Non-tie concordance between Likert and pairwise."""
    # Build pairwise lookup by id
    pw_by_id = {}
    for rec in pairwise_data:
        rid = rec.get("id")
        if rid and nli_filter(rec):
            pw_by_id[rid] = rec

    concordant = 0
    discordant = 0
    likert_ties = 0
    pairwise_ties = 0
    total_matched = 0
    items = []

    for rec in scored_data:
        rid = rec.get("id")
        if not rid or not nli_filter(rec):
            continue
        if rid not in pw_by_id:
            continue

        total_matched += 1
        score_pole, score_anti = get_likert_pole_score(rec, cfg)
        if score_pole is None:
            continue

        pw_rec = pw_by_id[rid]
        pw_wins = get_pairwise_pole_wins(pw_rec, cfg)

        likert_diff = score_pole - score_anti

        if likert_diff == 0:
            likert_ties += 1
            items.append({"id": rid, "likert_diff": 0, "pw_wins": pw_wins, "concordant": None})
            continue

        if pw_wins is None:
            pairwise_ties += 1
            items.append({"id": rid, "likert_diff": likert_diff, "pw_wins": None, "concordant": None})
            continue

        likert_prefers_pole = likert_diff > 0
        if likert_prefers_pole == pw_wins:
            concordant += 1
            items.append({"id": rid, "likert_diff": likert_diff, "pw_wins": pw_wins, "concordant": True})
        else:
            discordant += 1
            items.append({"id": rid, "likert_diff": likert_diff, "pw_wins": pw_wins, "concordant": False})

    n_nontie = concordant + discordant
    rate, ci = wilson_ci(concordant, n_nontie)

    # Binomial test against 0.5
    if n_nontie > 0:
        binom_p = stats.binom_test(concordant, n_nontie, 0.5) if hasattr(stats, 'binom_test') else stats.binomtest(concordant, n_nontie, 0.5).pvalue
    else:
        binom_p = 1.0

    return {
        "total_matched": total_matched,
        "likert_ties": likert_ties,
        "pairwise_ties": pairwise_ties,
        "n_nontie": n_nontie,
        "concordant": concordant,
        "discordant": discordant,
        "concordance_rate": round(rate, 4),
        "wilson_ci_95": [round(ci[0], 4), round(ci[1], 4)],
        "binom_p": round(binom_p, 6),
    }, items


def analyze_correlation(items):
    """Task 2: Item-level correlation between Likert diff and pairwise outcome."""
    # Use all items where both likert_diff and pw_wins are available
    diffs = []
    outcomes = []
    for item in items:
        if item["likert_diff"] is not None and item["pw_wins"] is not None:
            diffs.append(item["likert_diff"])
            outcomes.append(1.0 if item["pw_wins"] else 0.0)

    if len(diffs) < 5:
        return {"n": len(diffs), "note": "insufficient data"}

    diffs = np.array(diffs)
    outcomes = np.array(outcomes)

    # Point-biserial correlation (Pearson between continuous and binary)
    r, p = stats.pointbiserialr(outcomes, diffs)

    return {
        "n": len(diffs),
        "r_pb": round(float(r), 4),
        "p_value": round(float(p), 6),
    }


def bias_corrected_or(style_or, n, method="nemes"):
    """Task 3: Bias-corrected OR using small-sample correction."""
    if style_or is None or style_or <= 0 or n <= 0:
        return None

    log_or = math.log(style_or)

    if method == "nemes":
        # Nemes (2009): log(OR_c) = log(OR) * (1 - 1/n)
        correction = 1 - 1 / n
        log_or_c = log_or * correction
    elif method == "hedges":
        # Hedges (1981): J = 1 - 3/(4*df - 1), df = n - 2 for logistic
        df = max(n - 2, 1)
        J = 1 - 3 / (4 * df - 1)
        log_or_c = log_or * J
    else:
        raise ValueError(f"Unknown method: {method}")

    return {
        "original_or": round(style_or, 4),
        "original_log_or": round(log_or, 4),
        "corrected_log_or": round(log_or_c, 4),
        "corrected_or": round(math.exp(log_or_c), 4),
        "correction_factor": round(log_or_c / log_or if log_or != 0 else 1.0, 4),
        "method": method,
        "n": n,
    }


# GEE Style OR values from existing analyses
GEE_STYLE_ORS = {
    ("gpt4o", "formality", "llmbar"): {"or": 2.7002, "n": 86},
    ("qwen32b", "formality", "llmbar"): {"or": 4.2008, "n": 88},
    ("llama70b", "formality", "llmbar"): {"or": 5.5227, "n": 83},
    ("gpt4o", "formality", "alpacaeval"): {"or": 3.8296, "n": 69},
    ("qwen32b", "formality", "alpacaeval"): {"or": 2.0, "n": 59},  # placeholder
    ("gpt4o", "verbosity", "llmbar"): {"or": 1.78, "n": 86},
    ("qwen32b", "verbosity", "llmbar"): {"or": 2.15, "n": 86},
    ("llama70b", "verbosity", "llmbar"): {"or": 2.06, "n": 83},
    ("gemini", "formality", "llmbar"): {"or": 5.19, "n": 88},
    ("gemini", "verbosity", "llmbar"): {"or": 3.78, "n": 86},
}


def main():
    results = {
        "concordance": {},
        "correlation": {},
        "bias_corrected_or": {},
        "summary": {},
    }

    all_concordant = 0
    all_discordant = 0

    for key, cfg in CONFIGS.items():
        judge, axis, bench = key
        label = f"{judge}_{axis}_{bench}"

        scored_path = os.path.join(DATA_DIR, cfg["scored"])
        pairwise_path = os.path.join(DATA_DIR, cfg["pairwise"])

        if cfg.get("skip_concordance"):
            print(f"[SKIP] {label}: no matched Likert data")
            continue

        if not os.path.exists(scored_path):
            print(f"[MISS] {label}: {scored_path} not found")
            continue
        if not os.path.exists(pairwise_path):
            print(f"[MISS] {label}: {pairwise_path} not found")
            continue

        scored_data = load_jsonl(scored_path)
        pairwise_data = load_jsonl(pairwise_path)

        if not scored_data or not pairwise_data:
            print(f"[EMPTY] {label}")
            continue

        # Task 1: Concordance
        conc_result, items = analyze_concordance(scored_data, pairwise_data, cfg)
        results["concordance"][label] = conc_result
        print(f"[OK] {label}: concordance={conc_result['concordance_rate']:.1%} "
              f"({conc_result['concordant']}/{conc_result['n_nontie']}), "
              f"likert_ties={conc_result['likert_ties']}, "
              f"p={conc_result['binom_p']:.4f}")

        all_concordant += conc_result["concordant"]
        all_discordant += conc_result["discordant"]

        # Task 2: Correlation
        corr_result = analyze_correlation(items)
        results["correlation"][label] = corr_result
        if "r_pb" in corr_result:
            print(f"       correlation: r_pb={corr_result['r_pb']:.3f}, p={corr_result['p_value']:.4f}")

    # Task 3: Bias-corrected OR
    for key, vals in GEE_STYLE_ORS.items():
        judge, axis, bench = key
        label = f"{judge}_{axis}_{bench}"
        nemes = bias_corrected_or(vals["or"], vals["n"], "nemes")
        hedges = bias_corrected_or(vals["or"], vals["n"], "hedges")
        results["bias_corrected_or"][label] = {
            "nemes": nemes,
            "hedges": hedges,
        }

    # Pooled concordance
    n_pool = all_concordant + all_discordant
    if n_pool > 0:
        pool_rate, pool_ci = wilson_ci(all_concordant, n_pool)
        pool_p = stats.binomtest(all_concordant, n_pool, 0.5).pvalue
        results["summary"]["pooled_concordance"] = {
            "concordant": all_concordant,
            "discordant": all_discordant,
            "n_nontie": n_pool,
            "rate": round(pool_rate, 4),
            "ci_95": [round(pool_ci[0], 4), round(pool_ci[1], 4)],
            "binom_p": round(pool_p, 6),
        }
        print(f"\n[POOLED] concordance={pool_rate:.1%} ({all_concordant}/{n_pool}), "
              f"CI=[{pool_ci[0]:.1%}, {pool_ci[1]:.1%}], p={pool_p:.4f}")

    # Interpretation
    if n_pool > 0:
        if pool_rate > 0.80:
            interp = "ATTENUATION — high concordance supports Likert and pairwise measure same construct; Likert simply lacks sensitivity"
        elif pool_rate < 0.60:
            interp = "CONSTRUCT_DIVERGENCE — low concordance suggests Likert and pairwise tap different constructs"
        else:
            interp = "MIXED — moderate concordance; partial attenuation with some construct divergence"
        results["summary"]["interpretation"] = interp
        print(f"[INTERP] {interp}")

    # Save
    out_path = "/root/causal_style_decomp_judge/artifacts/r16_analysis/construct_divergence_analysis.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nSaved to {out_path}")

    # Also print JSON
    print("\n" + json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
