#!/usr/bin/env python3
"""
MVP experiment: ecological alpha-beta-gamma diversity decomposition
applied to the Doshi & Hauser (2024) creative-writing dataset.

Usage:
    python run_mvp.py                         # download data + run
    python run_mvp.py --synthetic             # dry-run with synthetic data
    python run_mvp.py --data-dir ./data       # use local data
    python run_mvp.py --nboot 200             # set bootstrap iterations
"""

import argparse
import json
import os
import sys
import time
from collections import OrderedDict

import numpy as np

# ---------------------------------------------------------------------------
# Imports from local modules
# ---------------------------------------------------------------------------
from data_loader import (
    download_dataset, load_stories, text_length_stats, generate_synthetic_data,
    STANDARD_CONDITIONS,
)
from diversity import hill_number, jost_partition, sample_coverage
from flat_metrics import (
    compute_tfidf, pairwise_cosine, within_between_analysis,
    fail_test_2_tfidf, fail_test_2_regression, fail_test_2_perpair,
)
from analysis import (
    bootstrap_diversity, bootstrap_baselga, rarefaction_sensitivity,
    multi_cutoff_rarefaction, coverage_based_standardization,
    pass_fail_judgment,
)
from visualization import (
    plot_hill_comparison, plot_baselga_decomposition,
    plot_cosine_heatmap, plot_rarefaction, plot_multi_cutoff_rarefaction,
)


def _group_by_condition(stories):
    """Group stories by condition, preserving order."""
    groups = OrderedDict()
    for c in STANDARD_CONDITIONS:
        group = [s for s in stories if s["condition"] == c]
        if group:
            groups[c] = group
    # catch any unmapped conditions
    seen = set(groups.keys())
    for s in stories:
        if s["condition"] not in seen:
            groups.setdefault(s["condition"], []).append(s)
            seen.add(s["condition"])
    return groups


def main():
    parser = argparse.ArgumentParser(description="Ecological diversity MVP experiment")
    parser.add_argument("--synthetic", action="store_true",
                        help="Use synthetic data (dry-run)")
    parser.add_argument("--data-dir", type=str, default=None,
                        help="Path to pre-downloaded data directory")
    parser.add_argument("--output-dir", type=str, default=None,
                        help="Output directory for results and plots")
    parser.add_argument("--nboot", type=int, default=200,
                        help="Number of bootstrap iterations (default: 200)")
    parser.add_argument("--seed", type=int, default=42,
                        help="Random seed")
    args = parser.parse_args()

    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = args.output_dir or os.path.join(script_dir, "results")
    os.makedirs(output_dir, exist_ok=True)

    rng = np.random.default_rng(args.seed)
    t0 = time.time()

    # ==================================================================
    # 1. Load data
    # ==================================================================
    print("=" * 60)
    print("STEP 1: Load data")
    print("=" * 60)

    if args.synthetic:
        stories = generate_synthetic_data(n_per_condition=40, rng=rng)
    elif args.data_dir:
        stories = load_stories(args.data_dir)
    else:
        data_dir = download_dataset(script_dir)
        stories = load_stories(data_dir)

    stories_by_cond = _group_by_condition(stories)
    conditions = list(stories_by_cond.keys())

    # ==================================================================
    # 2. Text length statistics
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 2: Text length statistics (confound control)")
    print("=" * 60)

    len_stats = text_length_stats(stories)
    for c, st in len_stats.items():
        print(f"  {c:25s}  mean={st['mean']:.0f}  med={st['median']:.0f}  "
              f"std={st['std']:.0f}  [{st['min']}, {st['max']}]  n={st['n']}")

    # ==================================================================
    # 3. Hill numbers + Jost partition (point estimates)
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 3: Hill numbers + Jost partition")
    print("=" * 60)

    for q in [0, 1, 2]:
        print(f"\n  q = {q}:")
        for cond in conditions:
            freqs = [s["word_freq"] for s in stories_by_cond[cond]]
            a, g, b = jost_partition(freqs, q)
            # per-story Hill numbers
            ind = [hill_number(f, q) for f in freqs]
            print(f"    {cond:25s}  alpha={a:.2f}  gamma={g:.2f}  beta={b:.3f}  "
                  f"indiv_mean={np.mean(ind):.2f}")

    # ==================================================================
    # 4. Bootstrap CI
    # ==================================================================
    print("\n" + "=" * 60)
    print(f"STEP 4: Bootstrap CI (nboot={args.nboot})")
    print("=" * 60)

    hill_boot = bootstrap_diversity(stories_by_cond, nboot=args.nboot, rng=rng)

    for q in ["q0", "q1", "q2"]:
        print(f"\n  {q}:")
        for cond in conditions:
            r = hill_boot[q][cond]
            print(f"    {cond:25s}  alpha={r['alpha']:.2f} {r['alpha_ci']}  "
                  f"beta={r['beta']:.3f} {r['beta_ci']}")

    # ==================================================================
    # 5. Baselga decomposition + bootstrap
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 5: Baselga decomposition")
    print("=" * 60)

    baselga_boot = bootstrap_baselga(stories_by_cond, nboot=args.nboot, rng=rng)

    for cond in conditions:
        r = baselga_boot[cond]
        print(f"  {cond:25s}  BC_total={r['bc_total']:.4f}  "
              f"BC_bal={r['bc_balanced']:.4f} {r['bc_balanced_ci']}  "
              f"BC_gra={r['bc_gradient']:.4f} {r['bc_gradient_ci']}")

    # ==================================================================
    # 6. TF-IDF cosine similarity (flat baseline)
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 6: TF-IDF cosine similarity baseline")
    print("=" * 60)

    # build flat list aligned with stories_by_cond order
    flat_stories = []
    flat_labels = []
    for cond in conditions:
        for s in stories_by_cond[cond]:
            flat_stories.append(s)
            flat_labels.append(cond)

    tfidf_mat, vectorizer, _ = compute_tfidf(flat_stories)
    sim_matrix = pairwise_cosine(tfidf_mat)
    cosine_results = within_between_analysis(sim_matrix, flat_labels)

    print(f"  Within-cond similarity:  mean={cosine_results['within_mean']:.4f} "
          f"± {cosine_results['within_std']:.4f}")
    print(f"  Between-cond similarity: mean={cosine_results['between_mean']:.4f} "
          f"± {cosine_results['between_std']:.4f}")
    print(f"  Point-biserial r={cosine_results['r_pb']:.4f}  p={cosine_results['p_pb']:.2e}")

    # ==================================================================
    # 7. FAIL standard 2: can cosine recover Baselga ratio?
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 7: FAIL standard 2 test")
    print("=" * 60)

    # PRIMARY: per-pair method
    fail2_perpair = fail_test_2_perpair(stories_by_cond, tfidf_mat, flat_labels, vectorizer)
    print("  [per-pair method — PRIMARY]")
    for cond in conditions:
        pp = fail2_perpair["per_condition"].get(cond, {})
        print(f"    {cond:25s}  R²={pp.get('r2', 0):.4f}  MAE={pp.get('mae', 0):.4f}  "
              f"ratio_mean={pp.get('ratio_mean', 0):.4f}±{pp.get('ratio_std', 0):.4f}")
    print(f"    Overall R²={fail2_perpair['overall_r2']:.4f}  MAE={fail2_perpair['overall_mae']:.4f}")
    print(f"    Per-pair FAIL: {fail2_perpair['fail']}")

    # SUPPLEMENTARY: old tfidf + regression approaches
    fail2_tfidf = fail_test_2_tfidf(stories_by_cond, tfidf_mat, flat_labels, vectorizer)

    cosine_dist_by_cond = {}
    idx_start = 0
    for cond in conditions:
        n = len(stories_by_cond[cond])
        dists = []
        for i in range(n):
            for j in range(i + 1, n):
                dists.append(1.0 - sim_matrix[idx_start + i, idx_start + j])
        cosine_dist_by_cond[cond] = dists
        idx_start += n

    fail2_reg = fail_test_2_regression(baselga_boot, cosine_dist_by_cond)

    print("  [supplementary methods]")
    for cond in conditions:
        t = fail2_tfidf["per_condition"].get(cond, {})
        r = fail2_reg["per_condition"].get(cond, {})
        print(f"    {cond:25s}  tfidf_err={t.get('recovery_error', '?'):.3f}  "
              f"reg_err={r.get('recovery_error', '?'):.3f}")

    fail2_combined = {
        "perpair_approach": fail2_perpair,
        "tfidf_approach": fail2_tfidf,
        "regression_approach": fail2_reg,
        "fail": fail2_perpair["fail"],
    }
    print(f"  FAIL-2 triggered (per-pair primary): {fail2_combined['fail']}")

    # ==================================================================
    # 8a. Original rarefaction (min word count)
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 8a: Rarefaction sensitivity (min word count)")
    print("=" * 60)

    rare_results = rarefaction_sensitivity(stories_by_cond, n_iter=30, rng=rng)
    print(f"  Rarefied to {rare_results['min_word_count']} words")
    for q in ["q0", "q1", "q2"]:
        print(f"  {q}:")
        for cond in conditions:
            r = rare_results[q][cond]
            print(f"    {cond:25s}  alpha={r['alpha']:.2f}  beta={r['beta']:.3f}")

    # ==================================================================
    # 8b. Multi-cutoff rarefaction (50, 75, 100 words)
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 8b: Multi-cutoff rarefaction sensitivity")
    print("=" * 60)

    multi_cutoff = multi_cutoff_rarefaction(stories_by_cond, cutoffs=(50, 75, 100),
                                            n_iter=30, rng=rng)
    for m_str in sorted(multi_cutoff.keys(), key=int):
        m_data = multi_cutoff[m_str]
        kept = m_data["kept_counts"]
        print(f"\n  Cutoff = {m_str} words (kept: {kept})")
        for q in ["q0", "q1", "q2"]:
            print(f"    {q}:")
            for cond in conditions:
                r = m_data[q].get(cond, {})
                a = r.get("alpha", float("nan"))
                b = r.get("beta", float("nan"))
                aci = r.get("alpha_ci", [float("nan")] * 2)
                bci = r.get("beta_ci", [float("nan")] * 2)
                if np.isnan(a):
                    print(f"      {cond:25s}  (too few stories)")
                else:
                    print(f"      {cond:25s}  alpha={a:.2f} [{aci[0]:.2f},{aci[1]:.2f}]  "
                          f"beta={b:.3f} [{bci[0]:.3f},{bci[1]:.3f}]")

    # ==================================================================
    # 8c. Coverage-based standardization
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 8c: Coverage-based standardization")
    print("=" * 60)

    cov_results = coverage_based_standardization(stories_by_cond, n_iter=30, rng=rng)
    print(f"  Target coverage: {cov_results['target_coverage']:.4f}")
    print(f"  Coverage distributions:")
    for cond in conditions:
        cd = cov_results["coverage_distributions"][cond]
        print(f"    {cond:25s}  mean={cd['mean']:.4f}  min={cd['min']:.4f}")
    print(f"  Kept counts: {cov_results['kept_counts']}")
    for q in ["q0", "q1", "q2"]:
        print(f"  {q}:")
        for cond in conditions:
            r = cov_results[q].get(cond, {})
            a = r.get("alpha", float("nan"))
            b = r.get("beta", float("nan"))
            if np.isnan(a):
                print(f"    {cond:25s}  (too few stories)")
            else:
                aci = r.get("alpha_ci", [a, a])
                bci = r.get("beta_ci", [b, b])
                print(f"    {cond:25s}  alpha={a:.2f} [{aci[0]:.2f},{aci[1]:.2f}]  "
                      f"beta={b:.3f} [{bci[0]:.3f},{bci[1]:.3f}]")

    # ==================================================================
    # 9. Pass / Fail judgment
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 9: Pass / Fail judgment")
    print("=" * 60)

    judgment = pass_fail_judgment(hill_boot, baselga_boot, cosine_results, fail2_combined)

    print(f"\n  PASS 1 (alpha↑):    {judgment['pass1_alpha_higher']['pass']}")
    print(f"  PASS 2 (beta↓):     {judgment['pass2_beta_lower']['pass']}")
    print(f"  PASS 3 (Baselga):   {judgment['pass3_baselga_distinguishable']['pass']}")
    print(f"  PASS 4 (cosine r):  {judgment['pass4_cosine_correlation']['pass']}  "
          f"(r={judgment['pass4_cosine_correlation']['r']:.4f})")
    print(f"  FAIL 1 (no pattern):{judgment['fail1_pattern_absent']['fail']}")
    print(f"  FAIL 2 (flat≈eco):  {judgment['fail2_flat_recovery'].get('fail', '?')}")
    print(f"\n  {'=' * 30}")
    print(f"  OVERALL: {judgment['overall']}")
    print(f"  {'=' * 30}")

    # ==================================================================
    # 10. Save results
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 10: Save results")
    print("=" * 60)

    # strip non-serialisable boot arrays
    hill_serial = {}
    for q in ["q0", "q1", "q2"]:
        hill_serial[q] = {}
        for cond in hill_boot[q]:
            d = dict(hill_boot[q][cond])
            d.pop("alpha_boot", None)
            d.pop("gamma_boot", None)
            d.pop("beta_boot", None)
            hill_serial[q][cond] = d

    baselga_serial = {}
    for cond in baselga_boot:
        d = dict(baselga_boot[cond])
        d.pop("bc_total_vals", None)
        d.pop("bc_balanced_vals", None)
        d.pop("bc_gradient_vals", None)
        baselga_serial[cond] = d

    results = {
        "metadata": {
            "dataset": "synthetic" if args.synthetic else "doshi_hauser_2024",
            "n_stories": len(stories),
            "conditions": conditions,
            "nboot": args.nboot,
            "seed": args.seed,
        },
        "text_length": len_stats,
        "hill_numbers": hill_serial,
        "baselga": baselga_serial,
        "cosine_similarity": cosine_results,
        "fail_test_2": {
            "perpair": fail2_perpair,
            "tfidf": fail2_tfidf,
            "regression": {k: v for k, v in fail2_reg.items() if k != "per_condition"}
                        | {"per_condition": {
                            c: {kk: vv for kk, vv in v.items()}
                            for c, v in fail2_reg["per_condition"].items()
                        }},
            "combined_fail": fail2_combined["fail"],
        },
        "rarefaction": rare_results,
        "multi_cutoff_rarefaction": multi_cutoff,
        "coverage_standardization": cov_results,
        "judgment": judgment,
    }

    json_path = os.path.join(output_dir, "mvp_results.json")
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"  Results → {json_path}")

    # ==================================================================
    # 11. Visualisation
    # ==================================================================
    print("\n" + "=" * 60)
    print("STEP 11: Generating plots")
    print("=" * 60)

    try:
        plot_hill_comparison(hill_serial, output_dir)
        plot_baselga_decomposition(baselga_serial, output_dir)
        plot_cosine_heatmap(sim_matrix, flat_labels, output_dir)
        plot_rarefaction(hill_serial, rare_results, output_dir)
        plot_multi_cutoff_rarefaction(multi_cutoff, output_dir)
    except Exception as e:
        print(f"[plot] Error: {e}")
        import traceback; traceback.print_exc()

    elapsed = time.time() - t0
    print(f"\nDone in {elapsed:.1f}s.  Output directory: {output_dir}")


if __name__ == "__main__":
    main()
