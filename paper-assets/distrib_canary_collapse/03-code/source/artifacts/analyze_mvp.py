"""Analyze MVP experiment: metric trends, cross-correlation, lead time.

Reads all_metrics.json from each rep, produces:
  - metric_trends.png : canary + downstream metrics vs generation
  - cross_correlation.png : cross-correlation heatmap
  - lead_time_table.csv : lead time estimates per canary-downstream pair
  - analysis_summary.json : machine-readable summary with graded verdict

Evaluation pipeline (per mvp_evaluation_criteria.md):
  1. MAUVE floor effect detection (§4) — demote if Gen 0 < 0.10 and CV < 0.50
  2. effective_rank monotonicity check (§3) — Gen 4-9 OLS slope consistency
  3. Permutation test (§1) — per-triplet significance via 10k permutations
  4. Per-seed significance filtering (§2) — 3/3 consistency requirement
  5. Graded verdict (§5) — STRONG PASS / PASS / CONDITIONAL PASS / FAIL
  6. Lag dispersion statistics — mean, std, min, max per consistent pair

Usage:
    python analyze_mvp.py --results_dir results/mvp --seeds 42 43 44
    python analyze_mvp.py --results_dir results/mvp --n_permutations 5000
"""

import argparse
import json
import os
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


CANARY_METRICS = ["token_entropy", "self_bleu", "ece", "effective_rank"]
DOWNSTREAM_METRICS = ["perplexity", "distinct_1", "distinct_2", "distinct_3", "mauve"]

HIGHER_IS_WORSE = {"self_bleu", "ece", "perplexity"}
LOWER_IS_WORSE = {"token_entropy", "effective_rank", "distinct_1", "distinct_2",
                   "distinct_3", "mauve"}


def load_metrics(results_dir, seeds):
    """Load all_metrics.json from each rep, return dict {seed: [metrics_per_gen]}."""
    data = {}
    for seed in seeds:
        path = os.path.join(results_dir, f"rep_{seed}", "all_metrics.json")
        with open(path) as f:
            data[seed] = json.load(f)
    return data


def metrics_to_df(data):
    """Convert {seed: [metrics_per_gen]} to a long-form DataFrame."""
    rows = []
    for seed, gens in data.items():
        for m in gens:
            m_copy = dict(m)
            m_copy["seed"] = seed
            rows.append(m_copy)
    return pd.DataFrame(rows)


def normalize_for_correlation(series, metric_name):
    """Flip sign so that 'getting worse' is always positive direction."""
    s = series.copy()
    if metric_name in LOWER_IS_WORSE:
        s = -s
    s = (s - s.mean()) / (s.std() + 1e-12)
    return s


def cross_correlate(x, y, max_lag=5):
    """Cross-correlation of x and y at lags -max_lag..+max_lag.

    Positive lag k means y leads x by k steps.
    Negative lag k means x leads y by |k| steps.
    """
    x = (x - x.mean()) / (x.std() + 1e-12)
    y = (y - y.mean()) / (y.std() + 1e-12)
    n = len(x)
    correlations = {}
    for lag in range(-max_lag, max_lag + 1):
        if lag >= 0:
            c = np.corrcoef(x[lag:], y[:n - lag])[0, 1] if n - lag > 1 else 0
        else:
            c = np.corrcoef(x[:n + lag], y[-lag:])[0, 1] if n + lag > 1 else 0
        correlations[lag] = c
    return correlations


def estimate_lead_time(canary_series, downstream_series, canary_name,
                       downstream_name, max_lag=5):
    """Estimate how many generations canary leads downstream.

    Returns (peak_lag, peak_corr, corrs). Negative peak_lag = canary leads.
    """
    c_norm = normalize_for_correlation(canary_series, canary_name)
    d_norm = normalize_for_correlation(downstream_series, downstream_name)
    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)
    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))
    return peak_lag, corrs[peak_lag], corrs


def permutation_test(canary_series, downstream_series, canary_name,
                     downstream_name, max_lag=5, n_permutations=10000, seed=0):
    """Permutation test for cross-correlation significance.

    Shuffles the downstream series to break temporal structure, recomputes
    max |r| across all lags for each permutation. p-value is the fraction
    of permutation max|r| >= observed peak|r|.

    Returns (peak_lag, peak_corr, p_value).
    """
    c_norm = normalize_for_correlation(canary_series, canary_name)
    d_norm = normalize_for_correlation(downstream_series, downstream_name)

    corrs = cross_correlate(c_norm, d_norm, max_lag=max_lag)
    peak_lag = max(corrs, key=lambda k: abs(corrs[k]))
    observed_peak_r = abs(corrs[peak_lag])

    rng = np.random.RandomState(seed)
    count_ge = 0
    for _ in range(n_permutations):
        d_perm = rng.permutation(d_norm)
        perm_corrs = cross_correlate(c_norm, d_perm, max_lag=max_lag)
        perm_max_r = max(abs(v) for v in perm_corrs.values())
        if perm_max_r >= observed_peak_r:
            count_ge += 1

    p_value = count_ge / n_permutations
    return peak_lag, corrs[peak_lag], p_value


def check_mauve_floor(df, seeds):
    """Check MAUVE floor effect: Gen 0 < 0.10 and CV < 0.50 across all seeds.

    Returns (demoted: bool, reason: str or None).
    """
    for seed in seeds:
        seed_df = df[df["seed"] == seed].sort_values("generation")
        gen0_mauve = seed_df[seed_df["generation"] == 0]["mauve"].values
        if len(gen0_mauve) == 0:
            return False, None
        if gen0_mauve[0] >= 0.10:
            return False, None
        mauve_vals = seed_df["mauve"].values
        mean_m = np.mean(mauve_vals)
        std_m = np.std(mauve_vals)
        cv = std_m / (mean_m + 1e-12)
        if cv >= 0.50:
            return False, None
    return True, "floor_effect"


def check_effective_rank_monotonicity(df, seeds):
    """Check effective_rank Gen 4-9 slope consistency across seeds.

    Returns (status: str, slopes: dict).
    status is one of: "decreasing", "increasing", "inconclusive".
    """
    slopes = {}
    for seed in seeds:
        seed_df = df[df["seed"] == seed].sort_values("generation")
        late = seed_df[seed_df["generation"] >= 4]
        if len(late) < 2:
            return "inconclusive", {}
        gens = late["generation"].values.astype(float)
        vals = late["effective_rank"].values.astype(float)
        coeffs = np.polyfit(gens, vals, 1)
        slopes[str(seed)] = float(coeffs[0])

    slope_vals = list(slopes.values())
    if all(s < 0 for s in slope_vals):
        return "decreasing", slopes
    if all(s > 0 for s in slope_vals):
        return "increasing", slopes
    return "inconclusive", slopes


def classify_pair(per_seed_results):
    """Classify a (canary, downstream) pair based on per-seed results.

    Returns one of: "SIGNIFICANT LEAD", "WEAK LEAD", "NO LEAD".
    """
    if not all(r["peak_lag"] < 0 for r in per_seed_results):
        return "NO LEAD"
    if all(r["p_value"] < 0.10 and abs(r["peak_corr"]) >= 0.60
           for r in per_seed_results):
        return "SIGNIFICANT LEAD"
    return "WEAK LEAD"


def check_near_miss(per_seed_results):
    """Check if a NO LEAD pair is a near miss (2/3 seeds lead, 1 at lag=0)."""
    lags = [r["peak_lag"] for r in per_seed_results]
    neg_seeds = [r for r in per_seed_results if r["peak_lag"] < 0]
    zero_seeds = [r for r in per_seed_results if r["peak_lag"] == 0]
    if len(neg_seeds) == 2 and len(zero_seeds) == 1:
        if all(r["peak_lag"] <= -2 and r["p_value"] < 0.05 for r in neg_seeds):
            return True
    return False


def compute_lag_dispersion(per_seed_results):
    """Compute lag dispersion statistics for a consistent pair."""
    lags = [r["peak_lag"] for r in per_seed_results]
    lag_std = float(np.std(lags))
    return {
        "mean_lag": float(np.mean(lags)),
        "lag_std": lag_std,
        "min_lag": int(min(lags)),
        "max_lag": int(max(lags)),
        "high_dispersion": lag_std > 2.0,
    }


def compute_verdict(per_pair_results, effective_rank_status):
    """Compute graded verdict from per-pair results.

    Returns (verdict, reasoning, significant_pairs, weak_pairs).
    """
    significant_pairs = []
    weak_pairs = []

    for pr in per_pair_results:
        if pr["canary"] == "effective_rank" and effective_rank_status == "inconclusive":
            continue
        if pr["pair_verdict"] == "SIGNIFICANT LEAD":
            significant_pairs.append(pr)
        elif pr["pair_verdict"] == "WEAK LEAD":
            weak_pairs.append(pr)

    sig_families = set(p["canary"] for p in significant_pairs)
    weak_families = set(p["canary"] for p in weak_pairs)

    if len(sig_families) >= 2:
        verdict = "STRONG PASS"
        reasoning = (f"{len(sig_families)} canary families ({', '.join(sorted(sig_families))}) "
                     f"each have >= 1 SIGNIFICANT LEAD pair.")
    elif len(sig_families) >= 1:
        verdict = "PASS"
        reasoning = (f"{len(sig_families)} canary family ({', '.join(sorted(sig_families))}) "
                     f"has >= 1 SIGNIFICANT LEAD pair.")
    elif len(weak_families) >= 1:
        verdict = "CONDITIONAL PASS"
        reasoning = (f"No SIGNIFICANT LEAD pairs, but {len(weak_families)} canary "
                     f"family ({', '.join(sorted(weak_families))}) has >= 1 WEAK LEAD pair.")
    else:
        verdict = "FAIL"
        reasoning = "No canary family achieves even WEAK LEAD consistency across seeds."

    return verdict, reasoning, significant_pairs, weak_pairs


def plot_metric_trends(df, output_dir):
    """Plot metric-vs-generation with mean +/- std across seeds."""
    all_metrics = CANARY_METRICS + DOWNSTREAM_METRICS
    fig, axes = plt.subplots(3, 3, figsize=(15, 12))
    axes = axes.flatten()

    for idx, metric in enumerate(all_metrics):
        if idx >= len(axes):
            break
        ax = axes[idx]
        grouped = df.groupby("generation")[metric]
        mean = grouped.mean()
        std = grouped.std()

        ax.plot(mean.index, mean.values, "o-", linewidth=2)
        ax.fill_between(mean.index, mean.values - std.values,
                        mean.values + std.values, alpha=0.2)
        ax.set_title(metric, fontsize=11, fontweight="bold")
        ax.set_xlabel("Generation")
        ax.set_ylabel(metric)
        ax.grid(True, alpha=0.3)

        is_canary = metric in CANARY_METRICS
        ax.set_facecolor("#fff8f0" if is_canary else "#f0f8ff")

    for idx in range(len(all_metrics), len(axes)):
        axes[idx].set_visible(False)

    fig.suptitle("Metric Trends over Generations (mean ± std, 3 reps)",
                 fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "metric_trends.png"), dpi=150,
                bbox_inches="tight")
    plt.close()
    print("Saved metric_trends.png")


def plot_cross_correlation_heatmap(lead_table, output_dir):
    """Heatmap of peak lag (canary leads = negative lag)."""
    pivot_lag = lead_table.pivot(index="canary", columns="downstream",
                                values="peak_lag")
    pivot_corr = lead_table.pivot(index="canary", columns="downstream",
                                  values="peak_corr")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    im1 = ax1.imshow(pivot_lag.values, cmap="RdBu_r", aspect="auto",
                     vmin=-5, vmax=5)
    ax1.set_xticks(range(len(pivot_lag.columns)))
    ax1.set_xticklabels(pivot_lag.columns, rotation=45, ha="right")
    ax1.set_yticks(range(len(pivot_lag.index)))
    ax1.set_yticklabels(pivot_lag.index)
    ax1.set_title("Peak Lag (negative = canary leads)")
    for i in range(len(pivot_lag.index)):
        for j in range(len(pivot_lag.columns)):
            ax1.text(j, i, f"{pivot_lag.values[i, j]:.0f}",
                     ha="center", va="center", fontsize=10)
    plt.colorbar(im1, ax=ax1)

    im2 = ax2.imshow(np.abs(pivot_corr.values), cmap="YlOrRd", aspect="auto",
                     vmin=0, vmax=1)
    ax2.set_xticks(range(len(pivot_corr.columns)))
    ax2.set_xticklabels(pivot_corr.columns, rotation=45, ha="right")
    ax2.set_yticks(range(len(pivot_corr.index)))
    ax2.set_yticklabels(pivot_corr.index)
    ax2.set_title("|Peak Correlation|")
    for i in range(len(pivot_corr.index)):
        for j in range(len(pivot_corr.columns)):
            ax2.text(j, i, f"{pivot_corr.values[i, j]:.2f}",
                     ha="center", va="center", fontsize=10)
    plt.colorbar(im2, ax=ax2)

    fig.suptitle("Cross-Correlation: Canary → Downstream", fontsize=13,
                 fontweight="bold")
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "cross_correlation.png"), dpi=150,
                bbox_inches="tight")
    plt.close()
    print("Saved cross_correlation.png")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze MVP experiment with graded verdict system.")
    parser.add_argument("--results_dir", type=str, default="results/mvp")
    parser.add_argument("--seeds", type=int, nargs="+", default=[42, 43, 44])
    parser.add_argument("--max_lag", type=int, default=5)
    parser.add_argument("--n_permutations", type=int, default=10000,
                        help="Number of permutations for significance test (default: 10000)")
    args = parser.parse_args()

    output_dir = os.path.join(args.results_dir, "analysis")
    os.makedirs(output_dir, exist_ok=True)

    print("Loading metrics ...")
    data = load_metrics(args.results_dir, args.seeds)
    df = metrics_to_df(data)

    # --- Metric trend plots ---
    plot_metric_trends(df, output_dir)

    # --- §4: MAUVE floor effect detection ---
    mauve_demoted, mauve_reason = check_mauve_floor(df, args.seeds)
    active_downstream = list(DOWNSTREAM_METRICS)
    if mauve_demoted:
        print(f"MAUVE demoted to supplementary (reason: {mauve_reason})")

    # --- §3: effective_rank monotonicity check ---
    er_status, er_slopes = check_effective_rank_monotonicity(df, args.seeds)
    print(f"effective_rank status: {er_status} (slopes: {er_slopes})")

    # --- Cross-correlation with permutation tests ---
    total_triplets = len(CANARY_METRICS) * len(DOWNSTREAM_METRICS) * len(args.seeds)
    triplet_idx = 0

    per_pair_results = []
    lead_rows = []
    near_misses = []

    for canary in CANARY_METRICS:
        for downstream in DOWNSTREAM_METRICS:
            per_seed = []
            all_lags = []
            all_corrs = []

            for seed in args.seeds:
                triplet_idx += 1
                print(f"\r  Permutation test {triplet_idx}/{total_triplets}: "
                      f"{canary} vs {downstream} (seed {seed})", end="",
                      flush=True)

                seed_df = df[df["seed"] == seed].sort_values("generation")
                c_series = seed_df[canary].values
                d_series = seed_df[downstream].values

                peak_lag, peak_corr, p_value = permutation_test(
                    c_series, d_series, canary, downstream,
                    max_lag=args.max_lag,
                    n_permutations=args.n_permutations,
                    seed=seed)

                per_seed.append({
                    "seed": seed,
                    "peak_lag": int(peak_lag),
                    "peak_corr": round(float(peak_corr), 4),
                    "p_value": round(float(p_value), 4),
                })
                all_lags.append(peak_lag)
                all_corrs.append(peak_corr)

            pair_verdict = classify_pair(per_seed)

            pair_result = {
                "canary": canary,
                "downstream": downstream,
                "pair_verdict": pair_verdict,
                "per_seed": per_seed,
            }

            if pair_verdict in ("SIGNIFICANT LEAD", "WEAK LEAD"):
                disp = compute_lag_dispersion(per_seed)
                pair_result.update(disp)
            else:
                if check_near_miss(per_seed):
                    near_misses.append({"canary": canary, "downstream": downstream,
                                        "per_seed": per_seed})

            per_pair_results.append(pair_result)

            lead_rows.append({
                "canary": canary,
                "downstream": downstream,
                "peak_lag": np.mean(all_lags),
                "peak_corr": np.mean(all_corrs),
                "lag_std": np.std(all_lags),
                "corr_std": np.std(all_corrs),
                "consistent": all(l < 0 for l in all_lags),
            })

    print()

    lead_table = pd.DataFrame(lead_rows)
    lead_table.to_csv(os.path.join(output_dir, "lead_time_table.csv"),
                      index=False)
    print("Saved lead_time_table.csv")

    plot_cross_correlation_heatmap(lead_table, output_dir)

    # --- §5: Graded verdict ---
    verdict_pairs = per_pair_results
    if mauve_demoted:
        verdict_pairs = [p for p in per_pair_results if p["downstream"] != "mauve"]

    verdict, reasoning, sig_pairs, weak_pairs = compute_verdict(
        verdict_pairs, er_status)

    # --- Build summary ---
    summary = {
        "mauve_demoted": mauve_demoted,
        "mauve_demoted_reason": mauve_reason,
        "effective_rank_status": er_status,
        "effective_rank_slopes": er_slopes,
        "per_pair_results": per_pair_results,
        "verdict": verdict,
        "verdict_reasoning": reasoning,
        "significant_lead_pairs": [
            {"canary": p["canary"], "downstream": p["downstream"]}
            for p in sig_pairs
        ],
        "weak_lead_pairs": [
            {"canary": p["canary"], "downstream": p["downstream"]}
            for p in weak_pairs
        ],
        "near_misses": near_misses,
    }

    with open(os.path.join(output_dir, "analysis_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    # --- Console report ---
    print("\n" + "=" * 60)
    print("MVP ANALYSIS SUMMARY")
    print("=" * 60)

    if mauve_demoted:
        print(f"MAUVE: demoted to supplementary ({mauve_reason})")
    else:
        print("MAUVE: retained as primary downstream metric")

    print(f"effective_rank: {er_status}")
    if er_slopes:
        slope_str = ", ".join(f"seed {k}: {v:.4f}" for k, v in er_slopes.items())
        print(f"  slopes: {slope_str}")

    n_sig = len(sig_pairs)
    n_weak = len(weak_pairs)
    n_total = len(verdict_pairs)
    print(f"\nPair results ({n_total} pairs evaluated for verdict):")
    print(f"  SIGNIFICANT LEAD: {n_sig}")
    print(f"  WEAK LEAD: {n_weak}")
    print(f"  NO LEAD: {n_total - n_sig - n_weak}")

    if near_misses:
        print(f"  Near misses: {len(near_misses)}")
        for nm in near_misses:
            print(f"    {nm['canary']} -> {nm['downstream']}")

    verdict_icon = {"STRONG PASS": "STRONG PASS", "PASS": "PASS",
                    "CONDITIONAL PASS": "CONDITIONAL PASS", "FAIL": "FAIL"}
    print(f"\nVerdict: {verdict_icon[verdict]}")
    print(f"Reasoning: {reasoning}")

    if sig_pairs:
        print("\nSignificant lead pairs:")
        for p in sig_pairs:
            disp_flag = " [high_dispersion]" if p.get("high_dispersion") else ""
            print(f"  {p['canary']} -> {p['downstream']}: "
                  f"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}")
            for s in p["per_seed"]:
                print(f"    seed {s['seed']}: lag={s['peak_lag']}, "
                      f"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}")

    if weak_pairs:
        print("\nWeak lead pairs:")
        for p in weak_pairs:
            disp_flag = " [high_dispersion]" if p.get("high_dispersion") else ""
            print(f"  {p['canary']} -> {p['downstream']}: "
                  f"mean_lag={p['mean_lag']:.1f}, lag_std={p['lag_std']:.1f}{disp_flag}")
            for s in p["per_seed"]:
                print(f"    seed {s['seed']}: lag={s['peak_lag']}, "
                      f"|r|={abs(s['peak_corr']):.3f}, p={s['p_value']:.4f}")

    print("\nFull lead time table:")
    print(lead_table.to_string(index=False))
    print(f"\nResults saved to {output_dir}/")


if __name__ == "__main__":
    main()
