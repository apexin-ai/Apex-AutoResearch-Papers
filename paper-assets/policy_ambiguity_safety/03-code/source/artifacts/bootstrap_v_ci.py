"""
Bootstrap 95% CI for Cramer's V from the type x mechanism contingency table.

Input: 6x4 contingency table (6 ambiguity types x 4 mechanism categories)
       from analysis_type_mechanism_mapping.json (confusion_matrix_3way).
       N = 614 violation traces.

Method: Resample 614 rows (episodes) with replacement B=10,000 times,
        compute Cramer's V for each resample, report percentile 95% CI.

Output: Point estimate V, 95% CI [lower, upper], histogram saved as PNG.
"""

import json
import numpy as np
from scipy.stats import chi2_contingency
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────
B = 10_000
SEED = 42
ALPHA = 0.05

# ── Load contingency table from JSON ────────────────────────────────────────
DATA_PATH = Path(__file__).parent / "analysis_type_mechanism_mapping.json"
with open(DATA_PATH) as f:
    data = json.load(f)

type_labels = data["types"]  # 6 types (alphabetical)
mech_labels = data["confusion_matrix_3way"]["labels"]  # structural_misparse, gap_filling, boundary_violation, other
ct_matrix = np.array(data["confusion_matrix_3way"]["matrix"])  # shape (6, 4)

print(f"Contingency table shape: {ct_matrix.shape}")
print(f"Types: {type_labels}")
print(f"Mechanisms: {mech_labels}")
print(f"Total N: {ct_matrix.sum()}")
print()
print("Contingency table (counts):")
header = f"{'':>25s} " + " ".join(f"{m:>20s}" for m in mech_labels)
print(header)
for i, t in enumerate(type_labels):
    row = " ".join(f"{ct_matrix[i, j]:>20d}" for j in range(len(mech_labels)))
    print(f"{t:>25s} {row}")
print()

# ── Reconstruct episode-level data from contingency table ───────────────────
# Each cell (i, j) with count c contributes c rows with type=i, mechanism=j.
type_ids = []
mech_ids = []
for i in range(ct_matrix.shape[0]):
    for j in range(ct_matrix.shape[1]):
        count = ct_matrix[i, j]
        type_ids.extend([i] * count)
        mech_ids.extend([j] * count)

type_ids = np.array(type_ids)
mech_ids = np.array(mech_ids)
N = len(type_ids)
assert N == ct_matrix.sum(), f"Expected {ct_matrix.sum()}, got {N}"
print(f"Reconstructed {N} episode-level rows\n")


# ── Cramer's V function ─────────────────────────────────────────────────────
def cramers_v_from_table(ct):
    """Compute Cramer's V from a contingency table (numpy array).

    Uses bias-corrected formula: V = sqrt(phi2_corr / min(r-1, k-1))
    where phi2_corr = max(0, phi2 - (r-1)(k-1)/(n-1)).

    For consistency with the project's existing code (compute_cramer_nmi.py),
    we use the uncorrected formula: V = sqrt(chi2 / (n * min(r-1, k-1))).
    """
    # Remove zero-sum rows/columns to avoid degenerate tables
    ct = ct[ct.sum(axis=1) > 0][:, ct.sum(axis=0) > 0]
    if ct.shape[0] < 2 or ct.shape[1] < 2:
        return 0.0
    chi2, p, dof, expected = chi2_contingency(ct, correction=False)
    n = ct.sum()
    r, k = ct.shape
    v = np.sqrt(chi2 / (n * min(r - 1, k - 1)))
    return v


# ── Point estimate ──────────────────────────────────────────────────────────
V_point = cramers_v_from_table(ct_matrix)
print(f"Point estimate: Cramer's V = {V_point:.4f}")
# Cross-check with JSON value
V_json = data["cramers_v_3way"]["V"]
print(f"JSON reference:  Cramer's V = {V_json:.4f}")
print()

# ── Bootstrap ────────────────────────────────────────────────────────────────
rng = np.random.default_rng(SEED)
n_types = ct_matrix.shape[0]
n_mechs = ct_matrix.shape[1]

boot_vs = np.empty(B)
for b in range(B):
    # Resample episode indices with replacement
    idx = rng.integers(0, N, size=N)
    t_boot = type_ids[idx]
    m_boot = mech_ids[idx]

    # Build contingency table from resampled data
    ct_boot = np.zeros((n_types, n_mechs), dtype=int)
    for i, j in zip(t_boot, m_boot):
        ct_boot[i, j] += 1

    boot_vs[b] = cramers_v_from_table(ct_boot)

# ── Results ──────────────────────────────────────────────────────────────────
ci_low = np.percentile(boot_vs, 100 * ALPHA / 2)
ci_high = np.percentile(boot_vs, 100 * (1 - ALPHA / 2))

print("=" * 60)
print(f"Bootstrap Cramer's V (B = {B:,}, seed = {SEED})")
print(f"  Point estimate:  V = {V_point:.2f}")
print(f"  95% CI:          [{ci_low:.2f}, {ci_high:.2f}]")
print(f"  Bootstrap mean:  {boot_vs.mean():.4f}")
print(f"  Bootstrap std:   {boot_vs.std():.4f}")
print("=" * 60)

# ── Save results to JSON ────────────────────────────────────────────────────
results = {
    "statistic": "cramers_v",
    "contingency": "3way",
    "n_episodes": int(N),
    "n_types": int(n_types),
    "n_mechanisms": int(n_mechs),
    "point_estimate": round(float(V_point), 4),
    "bootstrap_B": B,
    "seed": SEED,
    "ci_95_lower": round(float(ci_low), 4),
    "ci_95_upper": round(float(ci_high), 4),
    "bootstrap_mean": round(float(boot_vs.mean()), 4),
    "bootstrap_std": round(float(boot_vs.std()), 4),
}

out_json = Path(__file__).parent / "bootstrap_cramers_v_ci.json"
with open(out_json, "w") as f:
    json.dump(results, f, indent=2)
print(f"\nResults saved to {out_json}")

# ── Optional: histogram ─────────────────────────────────────────────────────
try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots(figsize=(5, 3))
    ax.hist(boot_vs, bins=60, color="#4C72B0", edgecolor="white", linewidth=0.3, alpha=0.85)
    ax.axvline(V_point, color="red", linestyle="--", linewidth=1.2, label=f"V = {V_point:.2f}")
    ax.axvline(ci_low, color="orange", linestyle=":", linewidth=1.0, label=f"95% CI: [{ci_low:.2f}, {ci_high:.2f}]")
    ax.axvline(ci_high, color="orange", linestyle=":", linewidth=1.0)
    ax.set_xlabel("Cramer's V")
    ax.set_ylabel("Frequency")
    ax.set_title(f"Bootstrap distribution (B = {B:,})")
    ax.legend(fontsize=8)
    plt.tight_layout()
    fig_path = Path(__file__).parent / "bootstrap_cramers_v_hist.png"
    plt.savefig(fig_path, dpi=150)
    print(f"Histogram saved to {fig_path}")
except ImportError:
    print("matplotlib not available; skipping histogram.")
