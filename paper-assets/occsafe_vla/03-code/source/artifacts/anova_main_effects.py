"""
2x2 Factorial Analysis: gradient_flow (ON/OFF) x norm_type (BN/LN)
Overall CAR metric, v2 data only.
"""
import numpy as np
import itertools
import warnings
warnings.filterwarnings("ignore")

# ---------- Data ----------
cell1 = np.array([0.746, 0.654, 0.776])  # Grad ON + BN  (Full OCC BN)
cell2 = np.array([0.740, 0.792, 0.798])  # Grad ON + LN  (Full OCC LN)
cell3 = np.array([0.774, 0.736, 0.762, 0.794])  # Grad OFF + BN (Detach BN)
cell4 = np.array([0.826])                # Grad OFF + LN (Detach LN)
vanilla = np.array([0.768, 0.748, 0.720])  # No OCC head

cells = {"Cell1_GradON_BN": cell1, "Cell2_GradON_LN": cell2,
         "Cell3_GradOFF_BN": cell3, "Cell4_GradOFF_LN": cell4}

rng = np.random.default_rng(42)
N_BOOT = 10000
N_PERM = 10000

out_lines = []
def pr(s=""):
    out_lines.append(s)

def cohens_d(a, b):
    na, nb = len(a), len(b)
    pooled_std = np.sqrt(((na-1)*np.var(a,ddof=1) + (nb-1)*np.var(b,ddof=1)) / (na+nb-2))
    if pooled_std == 0:
        return float('inf') if np.mean(a) != np.mean(b) else 0.0
    return (np.mean(a) - np.mean(b)) / pooled_std

def hedges_g(a, b):
    d = cohens_d(a, b)
    n = len(a) + len(b)
    correction = 1 - 3 / (4*(n-2) - 1)
    return d * correction

def bootstrap_ci_diff(a, b, n_boot=N_BOOT, ci=0.95):
    diffs = []
    for _ in range(n_boot):
        a_boot = rng.choice(a, size=len(a), replace=True)
        b_boot = rng.choice(b, size=len(b), replace=True)
        diffs.append(np.mean(a_boot) - np.mean(b_boot))
    diffs = np.sort(diffs)
    lo = np.percentile(diffs, (1-ci)/2*100)
    hi = np.percentile(diffs, (1+ci)/2*100)
    return lo, hi

def permutation_test(a, b, n_perm=N_PERM):
    obs_diff = np.mean(a) - np.mean(b)
    combined = np.concatenate([a, b])
    na = len(a)
    count = 0
    for _ in range(n_perm):
        perm = rng.permutation(combined)
        perm_diff = np.mean(perm[:na]) - np.mean(perm[na:])
        if abs(perm_diff) >= abs(obs_diff):
            count += 1
    return count / n_perm

# ============================================================
pr("=" * 70)
pr("2×2 FACTORIAL ANALYSIS: gradient_flow × norm_type")
pr("Metric: Overall CAR (v2)")
pr("=" * 70)
pr()

# ---------- A. Normalization Main Effect ----------
pr("A. NORMALIZATION MAIN EFFECT (BN vs LN)")
pr("-" * 50)
bn_pooled = np.concatenate([cell1, cell3])  # all BN seeds
ln_pooled = np.concatenate([cell2, cell4])  # all LN seeds
pr(f"BN pooled (n={len(bn_pooled)}): {bn_pooled.tolist()}")
pr(f"   mean = {np.mean(bn_pooled):.4f}, sd = {np.std(bn_pooled,ddof=1):.4f}")
pr(f"LN pooled (n={len(ln_pooled)}): {ln_pooled.tolist()}")
pr(f"   mean = {np.mean(ln_pooled):.4f}, sd = {np.std(ln_pooled,ddof=1):.4f}")
pr()

d_norm = cohens_d(ln_pooled, bn_pooled)
g_norm = hedges_g(ln_pooled, bn_pooled)
ci_lo, ci_hi = bootstrap_ci_diff(ln_pooled, bn_pooled)
p_norm = permutation_test(ln_pooled, bn_pooled)
direction = "LN > BN" if np.mean(ln_pooled) > np.mean(bn_pooled) else "BN > LN"

pr(f"Mean diff (LN - BN) = {np.mean(ln_pooled) - np.mean(bn_pooled):+.4f}")
pr(f"Direction: {direction}")
pr(f"Cohen's d = {d_norm:.4f}")
pr(f"Hedges' g = {g_norm:.4f}")
pr(f"95% Bootstrap CI (LN-BN) = [{ci_lo:.4f}, {ci_hi:.4f}]")
pr(f"Permutation p (two-sided) = {p_norm:.4f}")
pr(f"Reviewer estimated d ≈ 1.03 → Our computed d = {d_norm:.4f}")
pr()

# ---------- B. Gradient Flow Main Effect ----------
pr("B. GRADIENT FLOW MAIN EFFECT (Grad ON vs Grad OFF)")
pr("-" * 50)
grad_on = np.concatenate([cell1, cell2])
grad_off = np.concatenate([cell3, cell4])
pr(f"Grad ON pooled (n={len(grad_on)}): {grad_on.tolist()}")
pr(f"   mean = {np.mean(grad_on):.4f}, sd = {np.std(grad_on,ddof=1):.4f}")
pr(f"Grad OFF pooled (n={len(grad_off)}): {grad_off.tolist()}")
pr(f"   mean = {np.mean(grad_off):.4f}, sd = {np.std(grad_off,ddof=1):.4f}")
pr()

d_grad = cohens_d(grad_on, grad_off)
g_grad = hedges_g(grad_on, grad_off)
ci_lo_g, ci_hi_g = bootstrap_ci_diff(grad_on, grad_off)
p_grad = permutation_test(grad_on, grad_off)
dir_grad = "Grad ON > Grad OFF" if np.mean(grad_on) > np.mean(grad_off) else "Grad OFF > Grad ON"

pr(f"Mean diff (ON - OFF) = {np.mean(grad_on) - np.mean(grad_off):+.4f}")
pr(f"Direction: {dir_grad}")
pr(f"Cohen's d = {d_grad:.4f}")
pr(f"Hedges' g = {g_grad:.4f}")
pr(f"95% Bootstrap CI (ON-OFF) = [{ci_lo_g:.4f}, {ci_hi_g:.4f}]")
pr(f"Permutation p (two-sided) = {p_grad:.4f}")
pr()

# ---------- C. 2×2 ANOVA (Type III) ----------
pr("C. 2×2 ANOVA TABLE (Type III SS, unbalanced)")
pr("-" * 50)
pr("NOTE: Cell 4 (Grad OFF + LN) has n=1. ANOVA interaction estimate")
pr("is unreliable. Reported for transparency per Reviewer request.")
pr()

try:
    import pandas as pd
    import statsmodels.api as sm
    from statsmodels.formula.api import ols
    from statsmodels.stats.anova import anova_lm

    data = []
    for val in cell1:
        data.append({"gradient": "ON", "norm": "BN", "car": val})
    for val in cell2:
        data.append({"gradient": "ON", "norm": "LN", "car": val})
    for val in cell3:
        data.append({"gradient": "OFF", "norm": "BN", "car": val})
    for val in cell4:
        data.append({"gradient": "OFF", "norm": "LN", "car": val})

    df = pd.DataFrame(data)
    df["gradient"] = pd.Categorical(df["gradient"], categories=["OFF", "ON"])
    df["norm"] = pd.Categorical(df["norm"], categories=["BN", "LN"])

    model = ols("car ~ C(gradient) * C(norm)", data=df).fit()
    anova_table = anova_lm(model, typ=3)

    pr(f"{'Source':<20} {'SS':>10} {'df':>5} {'MS':>10} {'F':>8} {'p':>8} {'partial η²':>12}")
    pr("-" * 75)

    ss_resid = anova_table.loc["Residual", "sum_sq"]
    df_resid = anova_table.loc["Residual", "df"]

    for src in ["C(gradient)", "C(norm)", "C(gradient):C(norm)", "Residual"]:
        row = anova_table.loc[src]
        ss = row["sum_sq"]
        dof = int(row["df"])
        ms = row["mean_sq"] if "mean_sq" in row.index else ss / dof
        f_val = row["F"] if "F" in row.index and not np.isnan(row["F"]) else float("nan")
        p_val = row["PR(>F)"] if "PR(>F)" in row.index and not np.isnan(row["PR(>F)"]) else float("nan")

        if src == "Residual":
            label = "Residual"
            eta2 = ""
        else:
            label = {"C(gradient)": "Gradient Flow",
                     "C(norm)": "Norm Type",
                     "C(gradient):C(norm)": "Interaction"}[src]
            eta2_val = ss / (ss + ss_resid)
            eta2 = f"{eta2_val:.4f}"

        if np.isnan(f_val):
            pr(f"{label:<20} {ss:>10.6f} {dof:>5} {ms:>10.6f} {'':>8} {'':>8} {eta2:>12}")
        else:
            pr(f"{label:<20} {ss:>10.6f} {dof:>5} {ms:>10.6f} {f_val:>8.4f} {p_val:>8.4f} {eta2:>12}")
    pr()

    pr("Interpretation:")
    for src, label in [("C(norm)", "Norm Type"), ("C(gradient)", "Gradient Flow"),
                       ("C(gradient):C(norm)", "Interaction")]:
        p = anova_table.loc[src, "PR(>F)"]
        sig = "significant" if p < 0.05 else "NOT significant"
        pr(f"  {label}: F={anova_table.loc[src,'F']:.4f}, p={p:.4f} → {sig} at α=0.05")
    pr()
    ANOVA_OK = True

except ImportError as e:
    pr(f"statsmodels import failed: {e}")
    pr("Falling back to manual Type III SS computation...")
    ANOVA_OK = False

    # Manual implementation using normal equations
    # ... (would be very long, statsmodels should be available)
    pr("Manual ANOVA not implemented — install statsmodels.")
    pr()

# ---------- D. Pairwise Comparisons ----------
pr("D. PAIRWISE COMPARISONS (all 6 pairs)")
pr("-" * 50)

cell_names = ["Cell1_GradON_BN", "Cell2_GradON_LN", "Cell3_GradOFF_BN", "Cell4_GradOFF_LN"]
cell_data = [cell1, cell2, cell3, cell4]

pr(f"{'Comparison':<35} {'Δmean':>8} {'Cohen d':>9} {'perm p':>8} {'Note':>15}")
pr("-" * 80)

for i, j in itertools.combinations(range(4), 2):
    a, b = cell_data[i], cell_data[j]
    name = f"{cell_names[i]} vs {cell_names[j]}"
    diff = np.mean(a) - np.mean(b)
    note = ""

    if len(a) == 1 or len(b) == 1:
        # Cohen's d with n=1: use the other group's SD
        if len(a) == 1 and len(b) == 1:
            d = float('inf') if diff != 0 else 0.0
            p = 1.0
        elif len(a) == 1:
            sd_b = np.std(b, ddof=1)
            d = diff / sd_b if sd_b > 0 else float('inf')
            p = permutation_test(a, b)
        else:
            sd_a = np.std(a, ddof=1)
            d = diff / sd_a if sd_a > 0 else float('inf')
            p = permutation_test(a, b)
        note = "n=1, ref only"
    else:
        d = cohens_d(a, b)
        p = permutation_test(a, b)

    pr(f"{name:<35} {diff:>+8.4f} {d:>9.4f} {p:>8.4f} {note:>15}")

pr()

# ---------- E. vs Vanilla ----------
pr("E. EACH CELL vs VANILLA BASELINE")
pr("-" * 50)
pr(f"Vanilla (n={len(vanilla)}): mean = {np.mean(vanilla):.4f}, sd = {np.std(vanilla,ddof=1):.4f}")
pr()

pr(f"{'Cell':<25} {'Cell mean':>10} {'Δ':>8} {'Cohen d':>9} {'Direction':>15}")
pr("-" * 70)

for name, data in cells.items():
    diff = np.mean(data) - np.mean(vanilla)
    if len(data) == 1:
        sd_v = np.std(vanilla, ddof=1)
        d = diff / sd_v if sd_v > 0 else float('inf')
        direction = "Cell > Van" if diff > 0 else "Van > Cell"
        note = " (n=1)"
    else:
        d = cohens_d(data, vanilla)
        direction = "Cell > Van" if diff > 0 else "Van > Cell"
        note = ""
    pr(f"{name+note:<25} {np.mean(data):>10.4f} {diff:>+8.4f} {d:>9.4f} {direction:>15}")

pr()
pr("=" * 70)
pr("END OF ANALYSIS")
pr("=" * 70)

# Write results
output = "\n".join(out_lines)
print(output)
with open("/root/occsafe_vla/analysis/anova_main_effects_results.txt", "w") as f:
    f.write(output + "\n")
print("\nResults saved to /root/occsafe_vla/analysis/anova_main_effects_results.txt")
