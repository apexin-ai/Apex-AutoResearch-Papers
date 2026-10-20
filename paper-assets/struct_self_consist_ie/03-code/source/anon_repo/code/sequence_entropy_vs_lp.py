"""Analyze rank correlation between mean log-prob and cumulative log-prob (sequence entropy)."""
import json
import argparse
import numpy as np
from scipy import stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples_file", required=True)
    args = parser.parse_args()

    instances = []
    with open(args.samples_file) as f:
        for line in f:
            instances.append(json.loads(line))

    rhos = []
    rank1_differs = []
    token_cvs = []
    n_skipped = 0

    for inst in instances:
        samples = inst["samples"]
        if len(samples) < 3:
            n_skipped += 1
            continue

        mean_lps = [s["mean_logprob"] for s in samples]
        cum_lps = [s["cumulative_logprob"] for s in samples]
        n_tokens_list = [s["n_tokens"] for s in samples]

        # Spearman rho between mean_lp ranking and cumulative_lp ranking
        rho, _ = stats.spearmanr(mean_lps, cum_lps)
        if np.isnan(rho):
            n_skipped += 1
            continue

        rhos.append(rho)

        # Check if rank-1 (best = highest logprob) differs
        best_mean = np.argmax(mean_lps)
        best_cum = np.argmax(cum_lps)
        rank1_differs.append(best_mean != best_cum)

        # Token count CV for this instance
        cv = np.std(n_tokens_list) / np.mean(n_tokens_list) if np.mean(n_tokens_list) > 0 else 0
        token_cvs.append(cv)

    rhos = np.array(rhos)
    token_cvs = np.array(token_cvs)
    rank1_differs = np.array(rank1_differs)

    print(f"=== Sequence Entropy vs Mean LP: Rank Correlation Analysis ===")
    print(f"Total instances: {len(instances)}, Analyzed: {len(rhos)}, Skipped: {n_skipped}")
    print()
    print(f"--- Spearman rho(mean_LP_rank, cumulative_LP_rank) ---")
    print(f"  Mean:   {rhos.mean():.4f}")
    print(f"  Median: {np.median(rhos):.4f}")
    print(f"  Std:    {rhos.std():.4f}")
    print()
    print(f"--- Threshold Analysis ---")
    print(f"  rho > 0.95:  {(rhos > 0.95).mean()*100:.1f}% ({(rhos > 0.95).sum()}/{len(rhos)})")
    print(f"  rho > 0.90:  {(rhos > 0.90).mean()*100:.1f}% ({(rhos > 0.90).sum()}/{len(rhos)})")
    print(f"  rho < 0.90:  {(rhos < 0.90).mean()*100:.1f}% ({(rhos < 0.90).sum()}/{len(rhos)})")
    print(f"  rho < 0.80:  {(rhos < 0.80).mean()*100:.1f}% ({(rhos < 0.80).sum()}/{len(rhos)})")
    print()
    print(f"--- Rank-1 Disagreement ---")
    print(f"  Best sample differs: {rank1_differs.mean()*100:.1f}% ({rank1_differs.sum()}/{len(rank1_differs)})")
    print()

    # Stratified analysis by token count CV
    print(f"--- Token Count Variance Stratification ---")
    print(f"  Token CV stats: mean={token_cvs.mean():.4f}, median={np.median(token_cvs):.4f}, "
          f"min={token_cvs.min():.4f}, max={token_cvs.max():.4f}")
    print()

    low_cv_mask = token_cvs < 0.05
    mid_cv_mask = (token_cvs >= 0.05) & (token_cvs <= 0.10)
    high_cv_mask = token_cvs > 0.10

    for name, mask in [("Low CV (<0.05)", low_cv_mask),
                       ("Mid CV (0.05-0.10)", mid_cv_mask),
                       ("High CV (>0.10)", high_cv_mask)]:
        if mask.sum() > 0:
            subset_rhos = rhos[mask]
            subset_rank1 = rank1_differs[mask]
            print(f"  {name}: n={mask.sum()}, rho_mean={subset_rhos.mean():.4f}, "
                  f"rho_median={np.median(subset_rhos):.4f}, "
                  f"rank1_diff={subset_rank1.mean()*100:.1f}%")
        else:
            print(f"  {name}: n=0")

    # Correlation between CV and rho
    if len(token_cvs) > 10:
        cv_rho_corr, cv_rho_p = stats.spearmanr(token_cvs, rhos)
        print(f"\n  Correlation(token_CV, rho): r={cv_rho_corr:.4f}, p={cv_rho_p:.2e}")

    print()
    # Conclusion
    if rhos.mean() > 0.95 and rank1_differs.mean() < 0.05:
        conclusion = "RANK-EQUIVALENT: mean LP and cumulative LP produce nearly identical rankings."
    elif rhos.mean() > 0.90:
        conclusion = "LARGELY EQUIVALENT: high correlation but some rank disagreements exist."
    else:
        conclusion = "NON-TRIVIALLY DIFFERENT: rankings diverge meaningfully."
    print(f"=== CONCLUSION: {conclusion} ===")


if __name__ == "__main__":
    main()
