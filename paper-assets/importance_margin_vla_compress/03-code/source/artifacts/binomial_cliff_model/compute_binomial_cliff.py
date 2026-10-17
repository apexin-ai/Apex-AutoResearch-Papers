"""
Hypergeometric cliff prediction for vision token pruning.

Models the probability that random pruning hits critical tokens,
predicting the SR cliff observed at k=0.85-0.925 in π0.5.

N=256 (16x16 grid), critical set C estimated from heatmap norms.
"""

import numpy as np
from scipy.stats import hypergeom
from scipy.optimize import minimize_scalar
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

OUT_DIR = Path(__file__).parent

# === Constants ===
N = 256  # total vision tokens (16x16 grid, 224/14=16)

# Observed data (seed42)
OBS_OBJECT = {
    'k': np.array([0.95, 0.925, 0.9, 0.85]),
    'sr': np.array([72.8, 27.6, 5.0, 5.0]) / 100,
}
OBS_SPATIAL = {
    'k': np.array([0.95, 0.925, 0.9, 0.85]),
    'sr': np.array([84.4, 60.4, 54.6, 58.4]) / 100,
}

# Heatmap statistics
NORM_MEAN = 250.29
NORM_STD = 16.12
NORM_MIN = 170.95
NORM_MAX = 283.95


def p_hit_at_least_m(N, C, n_remove, m):
    """
    P(at least m critical tokens removed) under hypergeometric model.
    N: total tokens, C: critical tokens, n_remove: tokens removed, m: threshold.
    """
    if n_remove < m:
        return 0.0
    if C < m:
        return 0.0
    # P(X >= m) = 1 - P(X <= m-1) where X ~ Hypergeom(N, C, n_remove)
    return 1.0 - hypergeom.cdf(m - 1, N, C, n_remove)


def survival_curve(k_values, C, m):
    """
    Predicted survival rate = 1 - P(hit >= m critical).
    Returns array of predicted SR for each k.
    """
    sr = np.zeros_like(k_values, dtype=float)
    for i, k in enumerate(k_values):
        n_remove = int(round((1 - k) * N))
        n_remove = min(n_remove, N)
        p_fail = p_hit_at_least_m(N, C, n_remove, m)
        sr[i] = 1.0 - p_fail
    return sr


def residual_sse(C, m, obs_k, obs_sr):
    """Sum of squared errors between predicted and observed SR."""
    pred = survival_curve(obs_k, int(round(C)), m)
    return np.sum((pred - obs_sr) ** 2)


def r_squared(obs, pred):
    ss_res = np.sum((obs - pred) ** 2)
    ss_tot = np.sum((obs - np.mean(obs)) ** 2)
    if ss_tot == 0:
        return 0.0
    return 1.0 - ss_res / ss_tot


# === Method 1: Norm threshold estimate ===
# Tokens with norm > mean + 1*std are "critical"
# From heatmap: roughly Gaussian, so ~16% above mean+1*std
C_norm_threshold = int(round(N * 0.16))  # ~41 tokens

# === Method 2: Center region estimate ===
# Center 6x6 = 36 tokens, center 8x8 = 64 tokens
C_center_6x6 = 36
C_center_8x8 = 64

# === Method 3: Grid search for best (C, m) ===
print("=" * 60)
print("Grid search for best (C, m) fitting Object suite cliff")
print("=" * 60)

best_fit = {'sse': np.inf}
results_table = []

for m in range(1, 11):
    for C in range(5, 121):
        sse = residual_sse(C, m, OBS_OBJECT['k'], OBS_OBJECT['sr'])
        pred = survival_curve(OBS_OBJECT['k'], C, m)
        r2 = r_squared(OBS_OBJECT['sr'], pred)
        results_table.append((C, m, sse, r2))
        if sse < best_fit['sse']:
            best_fit = {'C': C, 'm': m, 'sse': sse, 'r2': r2}

print(f"Best fit: C={best_fit['C']}, m={best_fit['m']}, "
      f"SSE={best_fit['sse']:.6f}, R²={best_fit['r2']:.4f}")

# Show top 10 fits
results_table.sort(key=lambda x: x[2])
print("\nTop 10 (C, m) fits:")
print(f"{'C':>4} {'m':>3} {'SSE':>10} {'R²':>8}")
for C, m, sse, r2 in results_table[:10]:
    print(f"{C:4d} {m:3d} {sse:10.6f} {r2:8.4f}")

# Print predictions at observed k values for best fit
print(f"\nPredicted vs Observed (C={best_fit['C']}, m={best_fit['m']}):")
pred_best = survival_curve(OBS_OBJECT['k'], best_fit['C'], best_fit['m'])
print(f"{'k':>6} {'Obs SR':>8} {'Pred SR':>8} {'Δ':>8}")
for k, obs, pred in zip(OBS_OBJECT['k'], OBS_OBJECT['sr'], pred_best):
    print(f"{k:6.3f} {obs:8.3f} {pred:8.3f} {pred-obs:+8.3f}")

# === Also fit Spatial suite ===
print("\n" + "=" * 60)
print("Grid search for Spatial suite")
print("=" * 60)

best_spatial = {'sse': np.inf}
for m in range(1, 11):
    for C in range(5, 121):
        sse = residual_sse(C, m, OBS_SPATIAL['k'], OBS_SPATIAL['sr'])
        pred = survival_curve(OBS_SPATIAL['k'], C, m)
        r2 = r_squared(OBS_SPATIAL['sr'], pred)
        if sse < best_spatial['sse']:
            best_spatial = {'C': C, 'm': m, 'sse': sse, 'r2': r2}

print(f"Best fit: C={best_spatial['C']}, m={best_spatial['m']}, "
      f"SSE={best_spatial['sse']:.6f}, R²={best_spatial['r2']:.4f}")

pred_spatial = survival_curve(OBS_SPATIAL['k'], best_spatial['C'], best_spatial['m'])
print(f"\nPredicted vs Observed (C={best_spatial['C']}, m={best_spatial['m']}):")
print(f"{'k':>6} {'Obs SR':>8} {'Pred SR':>8} {'Δ':>8}")
for k, obs, pred in zip(OBS_SPATIAL['k'], OBS_SPATIAL['sr'], pred_spatial):
    print(f"{k:6.3f} {obs:8.3f} {pred:8.3f} {pred-obs:+8.3f}")

# === Compute theoretical cliff location ===
print("\n" + "=" * 60)
print("Theoretical cliff thresholds (P_fail crosses 50%)")
print("=" * 60)

k_fine = np.linspace(0.3, 1.0, 701)

for label, C, m in [
    ("Best-Object", best_fit['C'], best_fit['m']),
    ("Best-Spatial", best_spatial['C'], best_spatial['m']),
    ("Norm>μ+σ", C_norm_threshold, best_fit['m']),
    ("Center6x6", C_center_6x6, best_fit['m']),
    ("Center8x8", C_center_8x8, best_fit['m']),
]:
    sr = survival_curve(k_fine, C, m)
    # Find k where SR drops below 50%
    idx_50 = np.where(sr < 0.5)[0]
    if len(idx_50) > 0:
        k_cliff = k_fine[idx_50[0]]
        print(f"  {label:15s} (C={C:3d}, m={m}): cliff at k={k_cliff:.3f} "
              f"(remove {int(round((1-k_cliff)*N)):3d} tokens)")
    else:
        print(f"  {label:15s} (C={C:3d}, m={m}): no cliff in [0.3, 1.0]")


# ============================
# PLOTTING
# ============================
fig, axes = plt.subplots(1, 2, figsize=(16, 7))

# --- Left panel: Object suite ---
ax = axes[0]

# Theoretical curves for different (C, m)
configs = [
    (best_fit['C'], best_fit['m'], f"Best fit C={best_fit['C']},m={best_fit['m']}", '-', 'tab:blue', 2.5),
    (C_norm_threshold, best_fit['m'], f"Norm>μ+σ C={C_norm_threshold},m={best_fit['m']}", '--', 'tab:green', 1.5),
    (C_center_6x6, best_fit['m'], f"Center 6×6 C={C_center_6x6},m={best_fit['m']}", '--', 'tab:orange', 1.5),
    (C_center_8x8, best_fit['m'], f"Center 8×8 C={C_center_8x8},m={best_fit['m']}", '--', 'tab:purple', 1.5),
    (best_fit['C'], 1, f"C={best_fit['C']},m=1", ':', 'tab:gray', 1.2),
    (best_fit['C'], 5, f"C={best_fit['C']},m=5", ':', 'tab:red', 1.2),
]

for C, m, label, ls, color, lw in configs:
    sr = survival_curve(k_fine, C, m)
    ax.plot(k_fine, sr, ls=ls, color=color, lw=lw, label=label, alpha=0.85)

# Observed data points
ax.scatter(OBS_OBJECT['k'], OBS_OBJECT['sr'], s=120, c='red', marker='o',
           zorder=10, edgecolors='black', linewidths=1.2, label='Object (observed)')

# Cliff region
ax.axvspan(0.85, 0.95, alpha=0.08, color='red', label='Observed cliff zone')
ax.axhline(0.5, ls=':', color='gray', alpha=0.5, lw=0.8)

ax.set_xlabel('Keep ratio k', fontsize=13)
ax.set_ylabel('Predicted survival rate', fontsize=13)
ax.set_title('Object Suite: Hypergeometric Cliff Prediction', fontsize=14, fontweight='bold')
ax.set_xlim(0.5, 1.0)
ax.set_ylim(-0.05, 1.05)
ax.legend(fontsize=8.5, loc='lower left')
ax.grid(True, alpha=0.3)

# --- Right panel: Spatial suite ---
ax2 = axes[1]

configs_s = [
    (best_spatial['C'], best_spatial['m'],
     f"Best fit C={best_spatial['C']},m={best_spatial['m']}", '-', 'tab:blue', 2.5),
    (best_fit['C'], best_fit['m'],
     f"Object-fit C={best_fit['C']},m={best_fit['m']}", '--', 'tab:orange', 1.5),
]

for C, m, label, ls, color, lw in configs_s:
    sr = survival_curve(k_fine, C, m)
    ax2.plot(k_fine, sr, ls=ls, color=color, lw=lw, label=label, alpha=0.85)

ax2.scatter(OBS_SPATIAL['k'], OBS_SPATIAL['sr'], s=120, c='blue', marker='s',
            zorder=10, edgecolors='black', linewidths=1.2, label='Spatial (observed)')

ax2.axvspan(0.85, 0.95, alpha=0.08, color='blue', label='Observed cliff zone')
ax2.axhline(0.5, ls=':', color='gray', alpha=0.5, lw=0.8)

ax2.set_xlabel('Keep ratio k', fontsize=13)
ax2.set_ylabel('Predicted survival rate', fontsize=13)
ax2.set_title('Spatial Suite: Hypergeometric Cliff Prediction', fontsize=14, fontweight='bold')
ax2.set_xlim(0.5, 1.0)
ax2.set_ylim(-0.05, 1.05)
ax2.legend(fontsize=8.5, loc='lower left')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_DIR / 'cliff_prediction.png', dpi=300, bbox_inches='tight')
print(f"\nSaved: {OUT_DIR / 'cliff_prediction.png'}")


# === Additional plot: sensitivity analysis ===
fig2, axes2 = plt.subplots(1, 2, figsize=(16, 7))

# Left: vary C with fixed m
ax3 = axes2[0]
m_fixed = best_fit['m']
for C in [10, 20, 30, 40, 50, 60, 80, 100]:
    sr = survival_curve(k_fine, C, m_fixed)
    ax3.plot(k_fine, sr, label=f'C={C}', lw=1.5)

ax3.scatter(OBS_OBJECT['k'], OBS_OBJECT['sr'], s=100, c='red', marker='o',
            zorder=10, edgecolors='black', linewidths=1, label='Object obs.')
ax3.set_xlabel('Keep ratio k', fontsize=13)
ax3.set_ylabel('Predicted survival rate', fontsize=13)
ax3.set_title(f'Sensitivity to C (m={m_fixed} fixed)', fontsize=14, fontweight='bold')
ax3.set_xlim(0.5, 1.0)
ax3.set_ylim(-0.05, 1.05)
ax3.legend(fontsize=9, ncol=2)
ax3.grid(True, alpha=0.3)

# Right: vary m with fixed C
ax4 = axes2[1]
C_fixed = best_fit['C']
for m in [1, 2, 3, 4, 5, 7, 10]:
    sr = survival_curve(k_fine, C_fixed, m)
    ax4.plot(k_fine, sr, label=f'm={m}', lw=1.5)

ax4.scatter(OBS_OBJECT['k'], OBS_OBJECT['sr'], s=100, c='red', marker='o',
            zorder=10, edgecolors='black', linewidths=1, label='Object obs.')
ax4.set_xlabel('Keep ratio k', fontsize=13)
ax4.set_ylabel('Predicted survival rate', fontsize=13)
ax4.set_title(f'Sensitivity to m (C={C_fixed} fixed)', fontsize=14, fontweight='bold')
ax4.set_xlim(0.5, 1.0)
ax4.set_ylim(-0.05, 1.05)
ax4.legend(fontsize=9, ncol=2)
ax4.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_DIR / 'cliff_sensitivity.png', dpi=300, bbox_inches='tight')
print(f"Saved: {OUT_DIR / 'cliff_sensitivity.png'}")


# === L2norm comparison: why no cliff ===
print("\n" + "=" * 60)
print("L2norm strategy: why no cliff?")
print("=" * 60)
print(f"""
L2norm removes lowest-norm tokens first.
From heatmap: edge tokens have norm ~235, center ~265.
At k=0.85, remove {int(0.15*N)}={int(0.15*N)} tokens.
L2norm removes the {int(0.15*N)} lowest-norm tokens (edges).
Critical tokens (high-norm, center) are NEVER removed until k << 0.5.

For the hypergeometric model, L2norm effectively sets:
  P(hit critical) ≈ 0  for k > 1 - (N-C)/N = C/N

With C={best_fit['C']}: cliff only at k < {best_fit['C']/N:.3f}
This explains L2norm maintaining ~98% SR even at k=0.85.
""")

# === Summary ===
print("=" * 60)
print("SUMMARY")
print("=" * 60)
print(f"""
Model: Hypergeometric distribution H(N={N}, C, n_remove)
  P(failure) = P(remove ≥ m critical tokens out of C)

Object suite best fit:
  C = {best_fit['C']} critical tokens, m = {best_fit['m']} (tolerance)
  R² = {best_fit['r2']:.4f}, SSE = {best_fit['sse']:.6f}

Spatial suite best fit:
  C = {best_spatial['C']} critical tokens, m = {best_spatial['m']} (tolerance)
  R² = {best_spatial['r2']:.4f}, SSE = {best_spatial['sse']:.6f}

Key insight: Object tasks have a sharper cliff because they depend
on fewer critical tokens (lower C) with lower tolerance (lower m).
Spatial tasks are more distributed, requiring more tokens but tolerating
partial removal better.

Physical interpretation:
  C = number of tokens encoding task-critical visual features
  m = minimum disruption needed to cause policy failure
  The cliff occurs when P(remove ≥ m out of C) transitions from ~0 to ~1,
  which happens in a narrow k window due to the hypergeometric distribution's
  sharp combinatorial threshold.
""")
