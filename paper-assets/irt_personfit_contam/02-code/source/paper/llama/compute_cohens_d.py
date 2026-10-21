"""Compute Cohen's d and bootstrap CIs for contam_25 lz* result."""
import json
import numpy as np
import os

BASE_DIR = "/path/to/project/llama"

# Clean baseline (n=10 seeds, Snijders lz*)
clean_lz_stars = np.array([
    -0.4891, -0.7793, 0.4109, 0.6498, -0.3043,
    -1.1483, 0.1419, 0.7175, -0.3718, -1.9506
])
clean_mean = clean_lz_stars.mean()
clean_std = clean_lz_stars.std(ddof=1)

def cohens_d(contam_val, clean_mean, clean_std):
    return (contam_val - clean_mean) / clean_std

def bootstrap_percentile_ci(contam_val, clean_vals, n_boot=10000, alpha=0.05, seed=42):
    rng = np.random.RandomState(seed)
    n = len(clean_vals)
    ds = []
    for _ in range(n_boot):
        boot = rng.choice(clean_vals, size=n, replace=True)
        d = (contam_val - boot.mean()) / boot.std(ddof=1)
        ds.append(d)
    ds = np.array(ds)
    lo = np.percentile(ds, 100 * alpha / 2)
    hi = np.percentile(ds, 100 * (1 - alpha / 2))
    return lo, hi, ds

def bca_ci(contam_val, clean_vals, n_boot=10000, alpha=0.05, seed=42):
    from scipy import stats as sp_stats
    rng = np.random.RandomState(seed)
    n = len(clean_vals)
    
    # Original statistic
    d_obs = cohens_d(contam_val, clean_vals.mean(), clean_vals.std(ddof=1))
    
    # Bootstrap distribution
    ds = []
    for _ in range(n_boot):
        boot = rng.choice(clean_vals, size=n, replace=True)
        d = (contam_val - boot.mean()) / boot.std(ddof=1)
        ds.append(d)
    ds = np.array(ds)
    
    # Bias correction (z0)
    z0 = sp_stats.norm.ppf(np.mean(ds < d_obs))
    
    # Acceleration (jackknife)
    jack_ds = []
    for i in range(n):
        jack_vals = np.delete(clean_vals, i)
        jack_d = (contam_val - jack_vals.mean()) / jack_vals.std(ddof=1)
        jack_ds.append(jack_d)
    jack_ds = np.array(jack_ds)
    jack_mean = jack_ds.mean()
    num = np.sum((jack_mean - jack_ds) ** 3)
    den = 6.0 * (np.sum((jack_mean - jack_ds) ** 2)) ** 1.5
    a_hat = num / den if den != 0 else 0.0
    
    # Adjusted percentiles
    z_alpha = sp_stats.norm.ppf(alpha / 2)
    z_1alpha = sp_stats.norm.ppf(1 - alpha / 2)
    
    p_lo = sp_stats.norm.cdf(z0 + (z0 + z_alpha) / (1 - a_hat * (z0 + z_alpha)))
    p_hi = sp_stats.norm.cdf(z0 + (z0 + z_1alpha) / (1 - a_hat * (z0 + z_1alpha)))
    
    lo = np.percentile(ds, 100 * p_lo)
    hi = np.percentile(ds, 100 * p_hi)
    return lo, hi

def main():
    results_path = os.path.join(BASE_DIR, "results", "contam_25_results.json")
    with open(results_path) as f:
        results = json.load(f)
    
    lz_star = results["lz_star"]
    theta = results["theta_mle"]
    acc_overall = results["accuracy_overall"]
    acc_seen = results["accuracy_seen"]
    acc_unseen = results["accuracy_unseen"]
    
    print(f"=== Llama contam_25 Results ===")
    print(f"lz* = {lz_star:.4f}")
    print(f"theta_MLE = {theta:.4f}")
    print(f"acc_overall = {acc_overall:.4f}")
    print(f"acc_seen = {acc_seen:.4f}" if acc_seen is not None else "acc_seen = N/A")
    print(f"acc_unseen = {acc_unseen:.4f}" if acc_unseen is not None else "acc_unseen = N/A")
    
    print(f"\n=== Clean Baseline (n=10) ===")
    print(f"mean = {clean_mean:.4f}, std(ddof=1) = {clean_std:.4f}")
    
    d = cohens_d(lz_star, clean_mean, clean_std)
    print(f"\n=== Cohen's d ===")
    print(f"d = ({lz_star:.4f} - {clean_mean:.4f}) / {clean_std:.4f} = {d:.4f}")
    
    lo_pct, hi_pct, boot_ds = bootstrap_percentile_ci(lz_star, clean_lz_stars)
    print(f"\n=== Bootstrap Percentile CI (10,000 resamples) ===")
    print(f"95% CI = [{lo_pct:.4f}, {hi_pct:.4f}]")
    
    lo_bca, hi_bca = bca_ci(lz_star, clean_lz_stars)
    print(f"\n=== BCa Bootstrap CI ===")
    print(f"95% CI = [{lo_bca:.4f}, {hi_bca:.4f}]")
    
    # Save summary
    summary = {
        "condition": "contam_25",
        "model": "Llama-3.1-8B-Instruct",
        "lz_star": float(lz_star),
        "theta_mle": float(theta),
        "accuracy_overall": acc_overall,
        "accuracy_seen": acc_seen,
        "accuracy_unseen": acc_unseen,
        "lz_star_seen": results.get("lz_star_seen"),
        "lz_star_unseen": results.get("lz_star_unseen"),
        "clean_baseline": {
            "mean": float(clean_mean),
            "std_ddof1": float(clean_std),
            "n": 10,
            "values": clean_lz_stars.tolist(),
        },
        "cohens_d": float(d),
        "bootstrap_percentile_ci_95": [float(lo_pct), float(hi_pct)],
        "bca_ci_95": [float(lo_bca), float(hi_bca)],
        "n_boot": 10000,
    }
    
    out_path = os.path.join(BASE_DIR, "results", "contam_25_cohens_d.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"\nSaved to {out_path}")

if __name__ == "__main__":
    main()
