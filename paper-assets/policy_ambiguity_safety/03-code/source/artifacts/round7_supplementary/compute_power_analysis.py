#!/usr/bin/env python3
"""
Post-hoc power analysis for policy ambiguity & LLM agent safety violations study.

Study parameters:
- 2,997 episodes total; ambiguous condition ~1,499; matched pairs design
- 5 models x 6 ambiguity types; ~50 episodes per cell
- Binary outcome: violation (moderate-or-above severity)

Computes power for:
  C1: McNemar's test (binary effect, matched pairs)
  C2: Chi-squared omnibus (type hierarchy, ambiguous condition only)
  TOST: Equivalence test between two types (+-15pp SESOI)
  Per-type Fisher's exact (ambiguous vs unambiguous per type)
"""

import json
import math
import numpy as np
from scipy import stats
from statsmodels.stats.power import GofChisquarePower, NormalIndPower


def mcnemar_power(n_pairs, n_discordant_a, n_discordant_b, alpha=0.05):
    """
    Power of McNemar's test for matched pairs.

    Under H1, the test statistic (b - c)^2 / (b + c) ~ chi2(1).
    The non-centrality parameter is (b - c)^2 / (b + c) where b, c are
    expected discordant counts.

    Parameters
    ----------
    n_pairs : int
        Total matched pairs.
    n_discordant_a : int
        Discordant pairs where ambiguous=violation, unambiguous=no violation.
    n_discordant_b : int
        Discordant pairs where ambiguous=no violation, unambiguous=violation.
    alpha : float
        Significance level.

    Returns
    -------
    float
        Statistical power.
    """
    b = n_discordant_a  # ambig-only violations
    c = n_discordant_b  # unambig-only violations

    # Non-centrality parameter for the chi-squared(1) test
    ncp = (b - c) ** 2 / (b + c)

    # Critical value under H0
    chi2_crit = stats.chi2.ppf(1 - alpha, df=1)

    # Power = P(chi2_noncen > chi2_crit)
    power = 1 - stats.ncx2.cdf(chi2_crit, df=1, nc=ncp)

    return power


def chisq_gof_power(n, w, df, alpha=0.05):
    """
    Power of chi-squared goodness-of-fit / test of independence.

    Parameters
    ----------
    n : int
        Sample size.
    w : float
        Cohen's w effect size (= Cramer's V for df=1 dimension).
    df : int
        Degrees of freedom.
    alpha : float
        Significance level.

    Returns
    -------
    float
        Statistical power.
    """
    gof = GofChisquarePower()
    power = gof.solve_power(effect_size=w, nobs=n, n_bins=df + 1, alpha=alpha)
    return power


def tost_two_proportions_power(p1, p2, n1, n2, delta, alpha=0.05):
    """
    Power of TOST equivalence test for two independent proportions.

    TOST declares equivalence if both one-sided tests reject:
      H01: p1 - p2 <= -delta  (lower bound)
      H02: p1 - p2 >= +delta  (upper bound)

    Parameters
    ----------
    p1, p2 : float
        True proportions in each group.
    n1, n2 : int
        Sample sizes.
    delta : float
        Equivalence margin (SESOI, one side).
    alpha : float
        Significance level for each one-sided test.

    Returns
    -------
    float
        Power to declare equivalence.
    """
    true_diff = p1 - p2
    se = math.sqrt(p1 * (1 - p1) / n1 + p2 * (1 - p2) / n2)

    z_alpha = stats.norm.ppf(1 - alpha)

    # Power of lower test: reject H01: diff <= -delta
    # Test stat: (diff - (-delta)) / se > z_alpha
    z_lower = (true_diff + delta) / se - z_alpha
    power_lower = stats.norm.cdf(z_lower)

    # Power of upper test: reject H02: diff >= +delta
    # Test stat: (delta - diff) / se > z_alpha
    z_upper = (delta - true_diff) / se - z_alpha
    power_upper = stats.norm.cdf(z_upper)

    # TOST power = P(both reject) = product for independent normal tests
    # More precisely, for the intersection:
    power = power_lower * power_upper

    return power


def fisher_exact_power(p1, p2, n1, n2, alpha=0.05, n_sim=200_000):
    """
    Simulated power of Fisher's exact test for two independent proportions.

    Parameters
    ----------
    p1, p2 : float
        True proportions (e.g., ambiguous=0.40, unambiguous=0.07).
    n1, n2 : int
        Sample sizes per group.
    alpha : float
        Significance level.
    n_sim : int
        Number of simulations.

    Returns
    -------
    float
        Estimated power.
    """
    rng = np.random.default_rng(42)

    reject_count = 0
    for _ in range(n_sim):
        x1 = rng.binomial(n1, p1)
        x2 = rng.binomial(n2, p2)

        table = np.array([[x1, n1 - x1], [x2, n2 - x2]])
        _, pval = stats.fisher_exact(table, alternative='two-sided')

        if pval < alpha:
            reject_count += 1

    return reject_count / n_sim


def main():
    results = {}

    # ---- C1: McNemar's test power ----
    # 1,497 matched pairs (after excluding 3 incomplete)
    # Observed discordant: 544 ambig-only violations, 36 unambig-only violations
    c1_power = mcnemar_power(
        n_pairs=1497,
        n_discordant_a=544,
        n_discordant_b=36,
        alpha=0.05
    )
    results["C1_mcnemar_power"] = round(c1_power, 6)

    # Also compute the observed McNemar chi2 and effect size (odds ratio)
    b, c = 544, 36
    chi2_obs = (b - c) ** 2 / (b + c)
    or_obs = b / c
    results["C1_mcnemar_chi2"] = round(chi2_obs, 2)
    results["C1_discordant_odds_ratio"] = round(or_obs, 2)
    results["C1_n_matched_pairs"] = 1497
    results["C1_n_discordant"] = b + c

    # ---- C2: Chi-squared omnibus power (type hierarchy) ----
    # n=1499, df=5 (6 ambiguity types - 1), Cramer's V = 0.137
    c2_power = chisq_gof_power(
        n=1499,
        w=0.137,  # Cohen's w = Cramer's V for k-1 df
        df=5,
        alpha=0.05
    )
    results["C2_omnibus_power"] = round(c2_power, 6)
    results["C2_n"] = 1499
    results["C2_df"] = 5
    results["C2_effect_size_w"] = 0.137

    # ---- TOST equivalence power (+-15pp SESOI) ----
    # Scenario: two types with true difference = 0pp
    # Each type has ~250 episodes in ambiguous condition
    # Assume base rate ~36% (overall ambiguous violation rate)
    p_base = 0.36
    tost_power = tost_two_proportions_power(
        p1=p_base,
        p2=p_base,  # true difference = 0
        n1=250,
        n2=250,
        delta=0.15,  # 15pp SESOI
        alpha=0.05
    )
    results["TOST_equivalence_power_15pp"] = round(tost_power, 6)
    results["TOST_n_per_type"] = 250
    results["TOST_SESOI"] = 0.15
    results["TOST_assumed_base_rate"] = p_base

    # Also compute TOST power at delta=10pp for sensitivity
    tost_power_10pp = tost_two_proportions_power(
        p1=p_base, p2=p_base, n1=250, n2=250, delta=0.10, alpha=0.05
    )
    results["TOST_equivalence_power_10pp"] = round(tost_power_10pp, 6)

    # ---- Per-type Fisher's exact power ----
    # Ambiguous ~40% violation rate vs unambiguous ~7%, n=250 per condition per type
    fisher_power = fisher_exact_power(
        p1=0.40,
        p2=0.07,
        n1=250,
        n2=250,
        alpha=0.05,
        n_sim=200_000
    )
    results["per_type_fisher_power"] = round(fisher_power, 6)
    results["per_type_fisher_p1_ambig"] = 0.40
    results["per_type_fisher_p2_unambig"] = 0.07
    results["per_type_fisher_n_per_group"] = 250

    # Also compute for the smallest cell (~50 per model*type)
    fisher_power_small = fisher_exact_power(
        p1=0.40,
        p2=0.07,
        n1=50,
        n2=50,
        alpha=0.05,
        n_sim=200_000
    )
    results["per_cell_fisher_power_n50"] = round(fisher_power_small, 6)

    # ---- Summary ----
    results["alpha"] = 0.05
    results["total_episodes"] = 2997
    results["n_models"] = 5
    results["n_ambiguity_types"] = 6
    results["episodes_per_cell"] = "~50"

    # Save
    outpath = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-4/projects/policy_ambiguity_safety/artifacts/round7_supplementary/power_analysis_results.json"
    with open(outpath, "w") as f:
        json.dump(results, f, indent=2)

    # Print summary
    print("=" * 60)
    print("POST-HOC POWER ANALYSIS RESULTS")
    print("=" * 60)
    print(f"C1 McNemar power (matched pairs):     {results['C1_mcnemar_power']:.4f}")
    print(f"   McNemar chi2 = {results['C1_mcnemar_chi2']}, OR = {results['C1_discordant_odds_ratio']}")
    print(f"C2 Chi-sq omnibus power (type hier.):  {results['C2_omnibus_power']:.4f}")
    print(f"   w = {results['C2_effect_size_w']}, df = {results['C2_df']}, n = {results['C2_n']}")
    print(f"TOST equivalence power (15pp SESOI):   {results['TOST_equivalence_power_15pp']:.4f}")
    print(f"TOST equivalence power (10pp SESOI):   {results['TOST_equivalence_power_10pp']:.4f}")
    print(f"   n_per_type = {results['TOST_n_per_type']}, base_rate = {results['TOST_assumed_base_rate']}")
    print(f"Per-type Fisher power (n=250/group):   {results['per_type_fisher_power']:.4f}")
    print(f"Per-cell Fisher power (n=50/group):    {results['per_cell_fisher_power_n50']:.4f}")
    print(f"   p_ambig={results['per_type_fisher_p1_ambig']}, p_unambig={results['per_type_fisher_p2_unambig']}")
    print("=" * 60)
    print(f"Results saved to: {outpath}")


if __name__ == "__main__":
    main()
