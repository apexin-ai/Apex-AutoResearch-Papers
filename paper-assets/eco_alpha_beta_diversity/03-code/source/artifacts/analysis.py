# Bootstrap CI, rarefaction sensitivity, and Pass/Fail judgment.

import numpy as np
from collections import Counter

from diversity import (
    hill_number, jost_partition, baselga_multi, baselga_pairwise,
    sample_coverage, rarefy_to_size, _expand_freq, size_for_target_coverage,
)


# ---------------------------------------------------------------------------
# Bootstrap confidence intervals
# ---------------------------------------------------------------------------

def bootstrap_diversity(stories_by_cond, nboot=200, rng=None):
    """
    Bootstrap 95% CI for Jost partition (alpha, gamma, beta) at q=0,1,2.
    Resamples stories with replacement within each condition.
    """
    if rng is None:
        rng = np.random.default_rng(42)

    results = {}
    for q in [0, 1, 2]:
        results[f"q{q}"] = {}
        for cond, stories in stories_by_cond.items():
            freqs = [s["word_freq"] for s in stories]
            N = len(freqs)
            alphas, gammas, betas = [], [], []
            for _ in range(nboot):
                idx = rng.choice(N, size=N, replace=True)
                sample = [freqs[i] for i in idx]
                a, g, b = jost_partition(sample, q)
                alphas.append(a)
                gammas.append(g)
                betas.append(b)

            # point estimate on full data
            a0, g0, b0 = jost_partition(freqs, q)
            results[f"q{q}"][cond] = {
                "alpha": a0, "gamma": g0, "beta": b0,
                "alpha_ci": _ci(alphas), "gamma_ci": _ci(gammas), "beta_ci": _ci(betas),
                "alpha_boot": alphas, "gamma_boot": gammas, "beta_boot": betas,
            }
    return results


def bootstrap_baselga(stories_by_cond, nboot=200, rng=None):
    """Bootstrap 95% CI for Baselga decomposition components."""
    if rng is None:
        rng = np.random.default_rng(42)

    results = {}
    for cond, stories in stories_by_cond.items():
        freqs = [s["word_freq"] for s in stories]
        N = len(freqs)

        # point estimate
        point = baselga_multi(freqs)

        boot_bal, boot_gra, boot_tot = [], [], []
        for _ in range(nboot):
            idx = rng.choice(N, size=N, replace=True)
            sample = [freqs[i] for i in idx]
            r = baselga_multi(sample)
            boot_bal.append(r["bc_balanced"])
            boot_gra.append(r["bc_gradient"])
            boot_tot.append(r["bc_total"])

        results[cond] = {
            "bc_total": point["bc_total"],
            "bc_balanced": point["bc_balanced"],
            "bc_gradient": point["bc_gradient"],
            "bc_total_ci": _ci(boot_tot),
            "bc_balanced_ci": _ci(boot_bal),
            "bc_gradient_ci": _ci(boot_gra),
            # keep pairwise values for FAIL test 2
            "bc_total_vals": point["bc_total_vals"],
            "bc_balanced_vals": point["bc_balanced_vals"],
            "bc_gradient_vals": point["bc_gradient_vals"],
            "n_pairs": point["n_pairs"],
        }
    return results


def _ci(vals, lo=2.5, hi=97.5):
    return [float(np.percentile(vals, lo)), float(np.percentile(vals, hi))]


# ---------------------------------------------------------------------------
# Coverage-based rarefaction sensitivity check
# ---------------------------------------------------------------------------

def rarefaction_sensitivity(stories_by_cond, n_iter=30, rng=None):
    """
    Rarefy all stories to the minimum word count, recompute Jost partition.
    Reports whether the alpha↑ beta↓ pattern survives length standardisation.
    """
    if rng is None:
        rng = np.random.default_rng(42)

    all_wc = [s["word_count"] for ss in stories_by_cond.values() for s in ss]
    min_wc = int(np.min(all_wc))

    coverages = {}
    for cond, stories in stories_by_cond.items():
        coverages[cond] = float(np.mean([sample_coverage(s["word_freq"]) for s in stories]))

    results = {"min_word_count": min_wc, "coverage_original": coverages}

    for q in [0, 1, 2]:
        q_res = {}
        for cond, stories in stories_by_cond.items():
            freqs = [s["word_freq"] for s in stories]
            a_vals, g_vals, b_vals = [], [], []
            for _ in range(n_iter):
                rarefied = [rarefy_to_size(f, min_wc, rng) for f in freqs]
                a, g, b = jost_partition(rarefied, q)
                a_vals.append(a)
                g_vals.append(g)
                b_vals.append(b)
            q_res[cond] = {
                "alpha": float(np.mean(a_vals)),
                "gamma": float(np.mean(g_vals)),
                "beta": float(np.mean(b_vals)),
                "alpha_ci": _ci(a_vals),
                "gamma_ci": _ci(g_vals),
                "beta_ci": _ci(b_vals),
            }
        results[f"q{q}"] = q_res

    return results


def multi_cutoff_rarefaction(stories_by_cond, cutoffs=(50, 75, 100),
                             n_iter=30, rng=None):
    """
    Rarefaction sensitivity at multiple cutoff sizes.
    For each cutoff, only stories with word_count >= cutoff are kept,
    then rarefied to that cutoff size. Returns Hill numbers + CI per cutoff.
    """
    if rng is None:
        rng = np.random.default_rng(42)

    results = {}
    for m in cutoffs:
        m_res = {"cutoff": m}
        kept_counts = {}
        for q in [0, 1, 2]:
            q_res = {}
            for cond, stories in stories_by_cond.items():
                eligible = [s for s in stories if s["word_count"] >= m]
                kept_counts[cond] = len(eligible)
                if len(eligible) < 3:
                    q_res[cond] = {
                        "alpha": float("nan"), "gamma": float("nan"),
                        "beta": float("nan"),
                        "alpha_ci": [float("nan")] * 2,
                        "gamma_ci": [float("nan")] * 2,
                        "beta_ci": [float("nan")] * 2,
                        "n_stories": len(eligible),
                    }
                    continue
                freqs = [s["word_freq"] for s in eligible]
                a_vals, g_vals, b_vals = [], [], []
                for _ in range(n_iter):
                    rarefied = [rarefy_to_size(f, m, rng) for f in freqs]
                    a, g, b = jost_partition(rarefied, q)
                    a_vals.append(a)
                    g_vals.append(g)
                    b_vals.append(b)
                q_res[cond] = {
                    "alpha": float(np.mean(a_vals)),
                    "gamma": float(np.mean(g_vals)),
                    "beta": float(np.mean(b_vals)),
                    "alpha_ci": _ci(a_vals),
                    "gamma_ci": _ci(g_vals),
                    "beta_ci": _ci(b_vals),
                    "n_stories": len(eligible),
                }
            m_res[f"q{q}"] = q_res
        m_res["kept_counts"] = kept_counts
        results[str(m)] = m_res

    return results


def coverage_based_standardization(stories_by_cond, n_iter=30, rng=None):
    """
    Coverage-based rarefaction: standardize all stories to a common
    target coverage, then compute Hill numbers + CI.

    Target coverage = min across conditions of 10th-percentile coverage.
    Stories below target coverage are skipped.
    """
    if rng is None:
        rng = np.random.default_rng(42)

    cov_by_cond = {}
    for cond, stories in stories_by_cond.items():
        covs = [sample_coverage(s["word_freq"]) for s in stories]
        cov_by_cond[cond] = covs

    p10_per_cond = {c: float(np.percentile(v, 10)) for c, v in cov_by_cond.items()}
    target_cov = min(p10_per_cond.values())
    target_cov = max(target_cov, 0.5)

    results = {
        "target_coverage": float(target_cov),
        "p10_per_condition": p10_per_cond,
        "coverage_distributions": {
            c: {"mean": float(np.mean(v)), "std": float(np.std(v)),
                "min": float(np.min(v)), "max": float(np.max(v))}
            for c, v in cov_by_cond.items()
        },
    }

    kept_counts = {}
    for q in [0, 1, 2]:
        q_res = {}
        for cond, stories in stories_by_cond.items():
            eligible = [s for s in stories
                        if sample_coverage(s["word_freq"]) >= target_cov]
            kept_counts[cond] = len(eligible)
            if len(eligible) < 3:
                q_res[cond] = {
                    "alpha": float("nan"), "gamma": float("nan"),
                    "beta": float("nan"),
                    "alpha_ci": [float("nan")] * 2,
                    "gamma_ci": [float("nan")] * 2,
                    "beta_ci": [float("nan")] * 2,
                    "n_stories": len(eligible),
                }
                continue

            freqs = [s["word_freq"] for s in eligible]
            a_vals, g_vals, b_vals = [], [], []
            for _ in range(n_iter):
                rarefied = []
                for f in freqs:
                    m = size_for_target_coverage(f, target_cov, rng)
                    rarefied.append(rarefy_to_size(f, m, rng))
                a, g, b = jost_partition(rarefied, q)
                a_vals.append(a)
                g_vals.append(g)
                b_vals.append(b)

            q_res[cond] = {
                "alpha": float(np.mean(a_vals)),
                "gamma": float(np.mean(g_vals)),
                "beta": float(np.mean(b_vals)),
                "alpha_ci": _ci(a_vals),
                "gamma_ci": _ci(g_vals),
                "beta_ci": _ci(b_vals),
                "n_stories": len(eligible),
            }
        results[f"q{q}"] = q_res
    results["kept_counts"] = kept_counts

    return results


# ---------------------------------------------------------------------------
# Pass / Fail judgment
# ---------------------------------------------------------------------------

def _ci_non_overlap_gt(ci_a, ci_b):
    """True if ci_a is entirely above ci_b (lower bound of a > upper bound of b)."""
    return ci_a[0] > ci_b[1]


def _ci_non_overlap_lt(ci_a, ci_b):
    """True if ci_a is entirely below ci_b."""
    return ci_a[1] < ci_b[0]


def pass_fail_judgment(hill_results, baselga_results, cosine_results, fail2_results):
    """
    Evaluate Pass/Fail criteria.

    PASS (all required):
      1. alpha_AI > alpha_noAI  — q=1 must pass; q=0 or q=2 must also pass
      2. beta_AI  < beta_noAI   — q=1 must pass; q=0 or q=2 must also pass
      3. Baselga bc_balanced CI ≠ bc_gradient CI  (at least one condition)
      4. within/between cosine r > 0.3 and p < 0.05

    FAIL (any):
      1. alpha-beta pattern absent (q=1 CI overlap or wrong direction)
      2. Cosine recovers Baselga ratio within ±10%
    """
    judgments = {}

    ai_conditions = [c for c in hill_results.get("q1", {}) if c != "no-AI"]
    has_noai = "no-AI" in hill_results.get("q1", {})

    # --- PASS 1 & 2: alpha↑ beta↓ with tightened logic ---
    # q=1 (Shannon entropy / perplexity) is the mathematical bridge between
    # Hill numbers and NLP perplexity — strongest interpretability, core of
    # the framework. Must pass. Additionally, at least one of q=0 or q=2 must
    # also show both alpha↑ AND beta↓ (joint requirement).
    pass1_q1 = False
    pass2_q1 = False
    pass1_detail = {}
    pass2_detail = {}
    secondary_pass = False
    secondary_detail = {}

    if has_noai:
        for ac in ai_conditions:
            # q=1 mandatory checks
            ci_ai_a = hill_results["q1"][ac]["alpha_ci"]
            ci_no_a = hill_results["q1"]["no-AI"]["alpha_ci"]
            ok_a1 = _ci_non_overlap_gt(ci_ai_a, ci_no_a)
            pass1_detail[f"q1_{ac}"] = ok_a1
            if ok_a1:
                pass1_q1 = True

            ci_ai_b = hill_results["q1"][ac]["beta_ci"]
            ci_no_b = hill_results["q1"]["no-AI"]["beta_ci"]
            ok_b1 = _ci_non_overlap_lt(ci_ai_b, ci_no_b)
            pass2_detail[f"q1_{ac}"] = ok_b1
            if ok_b1:
                pass2_q1 = True

            # q=0 and q=2: secondary requirement — both alpha↑ AND beta↓
            for q in ["q0", "q2"]:
                ci_ai_a = hill_results[q][ac]["alpha_ci"]
                ci_no_a = hill_results[q]["no-AI"]["alpha_ci"]
                ok_a = _ci_non_overlap_gt(ci_ai_a, ci_no_a)
                pass1_detail[f"{q}_{ac}"] = ok_a

                ci_ai_b = hill_results[q][ac]["beta_ci"]
                ci_no_b = hill_results[q]["no-AI"]["beta_ci"]
                ok_b = _ci_non_overlap_lt(ci_ai_b, ci_no_b)
                pass2_detail[f"{q}_{ac}"] = ok_b

                both = ok_a and ok_b
                secondary_detail[f"{q}_{ac}"] = both
                if both:
                    secondary_pass = True

    pass1 = pass1_q1 and secondary_pass
    pass2 = pass2_q1 and secondary_pass

    judgments["pass1_alpha_higher"] = {
        "pass": pass1, "detail": pass1_detail,
        "q1_pass": pass1_q1, "secondary_pass": secondary_pass,
        "secondary_detail": secondary_detail,
    }
    judgments["pass2_beta_lower"] = {
        "pass": pass2, "detail": pass2_detail,
        "q1_pass": pass2_q1, "secondary_pass": secondary_pass,
        "secondary_detail": secondary_detail,
    }

    # --- PASS 3: Baselga components distinguishable ---
    pass3 = False
    pass3_detail = {}
    for cond in baselga_results:
        ci_bal = baselga_results[cond]["bc_balanced_ci"]
        ci_gra = baselga_results[cond]["bc_gradient_ci"]
        ok = (ci_bal[0] > ci_gra[1]) or (ci_gra[0] > ci_bal[1])
        pass3_detail[cond] = ok
        if ok:
            pass3 = True
    judgments["pass3_baselga_distinguishable"] = {"pass": pass3, "detail": pass3_detail}

    # --- PASS 4: cosine r > 0.3 and p < 0.05 ---
    r_val = cosine_results.get("r_pb", 0.0)
    p_val = cosine_results.get("p_pb", 1.0)
    pass4 = (abs(r_val) > 0.3) and (p_val < 0.05)
    judgments["pass4_cosine_correlation"] = {
        "pass": pass4, "r": r_val, "p": p_val,
    }

    # --- FAIL 1: pattern absent ---
    fail1 = not (pass1 and pass2)
    judgments["fail1_pattern_absent"] = {"fail": fail1}

    # --- FAIL 2: flat metrics recover Baselga ratio ---
    fail2 = fail2_results.get("fail", False)
    judgments["fail2_flat_recovery"] = fail2_results

    # --- overall ---
    all_pass = pass1 and pass2 and pass3 and pass4
    any_fail = fail1 or fail2
    if any_fail:
        overall = "FAIL"
    elif all_pass:
        overall = "PASS"
    else:
        overall = "INCONCLUSIVE"

    judgments["overall"] = overall
    return judgments
