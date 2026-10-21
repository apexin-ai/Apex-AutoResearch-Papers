import numpy as np
import json
from scipy.stats import norm

def bca_bootstrap_ci(data, B=10000, alpha=0.05, seed=42):
    """BCa bootstrap CI for the mean."""
    rng = np.random.RandomState(seed)
    n = len(data)
    theta_hat = np.mean(data)

    boot_thetas = np.array([np.mean(rng.choice(data, size=n, replace=True)) for _ in range(B)])

    z0 = norm.ppf(np.mean(boot_thetas < theta_hat))

    jackknife_means = np.array([np.mean(np.delete(data, i)) for i in range(n)])
    jack_mean = np.mean(jackknife_means)
    num = np.sum((jack_mean - jackknife_means)**3)
    den = 6 * (np.sum((jack_mean - jackknife_means)**2))**1.5
    a = num / den if den != 0 else 0

    z_alpha = norm.ppf(alpha / 2)
    z_1alpha = norm.ppf(1 - alpha / 2)

    alpha1 = norm.cdf(z0 + (z0 + z_alpha) / (1 - a * (z0 + z_alpha)))
    alpha2 = norm.cdf(z0 + (z0 + z_1alpha) / (1 - a * (z0 + z_1alpha)))

    ci_lower = np.percentile(boot_thetas, 100 * alpha1)
    ci_upper = np.percentile(boot_thetas, 100 * alpha2)

    return theta_hat, ci_lower, ci_upper


# === Qwen-14B delta data (d100 - d000) ===
# s0:   MMLU 43.85 - 68.84 = -24.99,  ARC 81.06 - 90.44 = -9.38
# s42:  MMLU 60.07 - 69.44 = -9.37,   ARC 88.48 - 91.04 = -2.56
# s123: MMLU 55.93 - 68.67 = -12.74,  ARC 87.29 - 90.44 = -3.15

mmlu_deltas = np.array([-24.99, -9.37, -12.74])
arc_deltas = np.array([-9.38, -2.56, -3.15])

mmlu_mean, mmlu_lo, mmlu_hi = bca_bootstrap_ci(mmlu_deltas, B=10000, seed=42)
arc_mean, arc_lo, arc_hi = bca_bootstrap_ci(arc_deltas, B=10000, seed=42)

mmlu_sig = not (mmlu_lo <= 0 <= mmlu_hi)
arc_sig = not (arc_lo <= 0 <= arc_hi)

dir_con = (mmlu_mean > 0 and arc_mean > 0) or (mmlu_mean < 0 and arc_mean < 0)

if mmlu_mean < 0 and arc_mean < 0:
    taxonomy = "Collapse"
elif mmlu_mean > 0 and arc_mean > 0:
    taxonomy = "Lift"
else:
    taxonomy = "Mixed"

result = {
    "family": "Qwen-14B",
    "n_seeds": 3,
    "method": "BCa bootstrap",
    "B": 10000,
    "seed": 42,
    "mmlu": {
        "deltas": mmlu_deltas.tolist(),
        "mean_delta": round(mmlu_mean, 2),
        "ci_lower": round(mmlu_lo, 2),
        "ci_upper": round(mmlu_hi, 2),
        "significant": bool(mmlu_sig)
    },
    "arc": {
        "deltas": arc_deltas.tolist(),
        "mean_delta": round(arc_mean, 2),
        "ci_lower": round(arc_lo, 2),
        "ci_upper": round(arc_hi, 2),
        "significant": bool(arc_sig)
    },
    "direction_consistent": bool(dir_con),
    "taxonomy_pattern": taxonomy
}

out_path = "/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/contamcal-irt-calibration/artifacts/qwen14b_n3_bootstrap/qwen14b_n3_bootstrap_ci.json"
with open(out_path, "w") as f:
    json.dump(result, f, indent=2)

print("=" * 60)
print("Qwen-14B  n=3 BCa Bootstrap CI (B=10000, seed=42)")
print("=" * 60)
print(f"\nMMLU  deltas: {mmlu_deltas.tolist()}")
print(f"  mean = {mmlu_mean:.2f},  95% CI [{mmlu_lo:.2f}, {mmlu_hi:.2f}]")
print(f"  significant (CI excludes 0): {mmlu_sig}")
print(f"\nARC   deltas: {arc_deltas.tolist()}")
print(f"  mean = {arc_mean:.2f},  95% CI [{arc_lo:.2f}, {arc_hi:.2f}]")
print(f"  significant (CI excludes 0): {arc_sig}")
print(f"\nDirection-Consistent: {dir_con}")
print(f"Taxonomy: {taxonomy}")
print(f"\nJSON saved to: {out_path}")
