"""Compute Cohen's d + Bootstrap CI for contam_5 vs clean baseline."""
import json
import numpy as np
import sys

CLEAN_LZ_STARS = [9.4676, 7.0539, 9.5293, 8.9673, 8.5322, 8.2445, 8.7702, 9.1110, 9.0132, 8.1492]
CLEAN_MEAN = 8.6838
CLEAN_STD = 0.7353  # ddof=1

def cohens_d(contam_lz, clean_mean, clean_std):
    return (contam_lz - clean_mean) / clean_std

def bootstrap_ci(contam_lz, clean_values, n_boot=10000, seed=42, alpha=0.05):
    rng = np.random.RandomState(seed)
    clean_arr = np.array(clean_values)
    n = len(clean_arr)
    ds = np.zeros(n_boot)
    for i in range(n_boot):
        boot_sample = rng.choice(clean_arr, size=n, replace=True)
        boot_mean = boot_sample.mean()
        boot_std = boot_sample.std(ddof=1)
        if boot_std < 1e-10:
            boot_std = 1e-10
        ds[i] = (contam_lz - boot_mean) / boot_std
    # Percentile CI
    lo_pct = np.percentile(ds, 100 * alpha / 2)
    hi_pct = np.percentile(ds, 100 * (1 - alpha / 2))
    return ds, lo_pct, hi_pct

def bca_ci(contam_lz, clean_values, n_boot=10000, seed=42, alpha=0.05):
    rng = np.random.RandomState(seed)
    clean_arr = np.array(clean_values)
    n = len(clean_arr)
    
    # Point estimate
    d_hat = cohens_d(contam_lz, clean_arr.mean(), clean_arr.std(ddof=1))
    
    # Bootstrap distribution
    ds = np.zeros(n_boot)
    for i in range(n_boot):
        boot_sample = rng.choice(clean_arr, size=n, replace=True)
        boot_mean = boot_sample.mean()
        boot_std = boot_sample.std(ddof=1)
        if boot_std < 1e-10:
            boot_std = 1e-10
        ds[i] = (contam_lz - boot_mean) / boot_std
    
    # Bias correction (z0)
    from scipy.stats import norm
    prop_below = np.mean(ds < d_hat)
    if prop_below <= 0:
        prop_below = 1 / (2 * n_boot)
    elif prop_below >= 1:
        prop_below = 1 - 1 / (2 * n_boot)
    z0 = norm.ppf(prop_below)
    
    # Acceleration (jackknife)
    jack_ds = np.zeros(n)
    for j in range(n):
        jack_sample = np.delete(clean_arr, j)
        jack_mean = jack_sample.mean()
        jack_std = jack_sample.std(ddof=1)
        if jack_std < 1e-10:
            jack_std = 1e-10
        jack_ds[j] = (contam_lz - jack_mean) / jack_std
    jack_mean_d = jack_ds.mean()
    num = np.sum((jack_mean_d - jack_ds) ** 3)
    den = 6.0 * (np.sum((jack_mean_d - jack_ds) ** 2)) ** 1.5
    a_hat = num / den if abs(den) > 1e-15 else 0.0
    
    # Adjusted percentiles
    z_alpha = norm.ppf(alpha / 2)
    z_1alpha = norm.ppf(1 - alpha / 2)
    
    alpha1 = norm.cdf(z0 + (z0 + z_alpha) / (1 - a_hat * (z0 + z_alpha)))
    alpha2 = norm.cdf(z0 + (z0 + z_1alpha) / (1 - a_hat * (z0 + z_1alpha)))
    
    lo_bca = np.percentile(ds, 100 * alpha1)
    hi_bca = np.percentile(ds, 100 * alpha2)
    return lo_bca, hi_bca

if __name__ == "__main__":
    results_path = sys.argv[1] if len(sys.argv) > 1 else "/path/to/project/qwen/results/contam_5_results.json"
    
    with open(results_path) as f:
        results = json.load(f)
    
    contam_lz = results["lz_star"]
    
    # Verify clean stats
    clean_arr = np.array(CLEAN_LZ_STARS)
    assert abs(clean_arr.mean() - CLEAN_MEAN) < 0.001, f"Clean mean mismatch: {clean_arr.mean()} vs {CLEAN_MEAN}"
    assert abs(clean_arr.std(ddof=1) - CLEAN_STD) < 0.001, f"Clean std mismatch: {clean_arr.std(ddof=1)} vs {CLEAN_STD}"
    
    d = cohens_d(contam_lz, CLEAN_MEAN, CLEAN_STD)
    ds, lo_pct, hi_pct = bootstrap_ci(contam_lz, CLEAN_LZ_STARS)
    lo_bca, hi_bca = bca_ci(contam_lz, CLEAN_LZ_STARS)
    
    print(f"\n=== Cohen's d Results ===")
    print(f"contam_5 lz* = {contam_lz:.4f}")
    print(f"clean baseline: mean={CLEAN_MEAN:.4f}, std={CLEAN_STD:.4f}, n=10")
    print(f"Cohen's d = {d:.4f}")
    print(f"Percentile 95% CI: [{lo_pct:.4f}, {hi_pct:.4f}]")
    print(f"BCa 95% CI: [{lo_bca:.4f}, {hi_bca:.4f}]")
    print(f"\nFull results:")
    print(f"  theta_MLE = {results['theta_mle']:.4f}")
    print(f"  lz* = {contam_lz:.4f}")
    print(f"  acc_overall = {results['accuracy_overall']:.4f}")
    print(f"  acc_seen = {results.get('accuracy_seen')}")
    print(f"  acc_unseen = {results.get('accuracy_unseen')}")
    
    # Save combined results
    combined = {
        "condition": "contam_5",
        "lz_star": contam_lz,
        "theta_mle": results["theta_mle"],
        "accuracy_overall": results["accuracy_overall"],
        "accuracy_seen": results.get("accuracy_seen"),
        "accuracy_unseen": results.get("accuracy_unseen"),
        "lz_star_seen": results.get("lz_star_seen"),
        "lz_star_unseen": results.get("lz_star_unseen"),
        "cohens_d": d,
        "bootstrap_percentile_ci_95": [lo_pct, hi_pct],
        "bootstrap_bca_ci_95": [lo_bca, hi_bca],
        "clean_baseline": {
            "mean": CLEAN_MEAN,
            "std_ddof1": CLEAN_STD,
            "n": 10,
            "values": CLEAN_LZ_STARS
        }
    }
    out_path = "/path/to/project/qwen/results/contam_5_final.json"
    with open(out_path, "w") as f:
        json.dump(combined, f, indent=2)
    print(f"\nSaved to {out_path}")
