"""Update Table 2 (tab:scaling) with 14B 3-seed results + TOST equivalence test."""

import numpy as np
from scipy import stats

# ── 14B seed accuracies ──────────────────────────────────────────────
# Fill in after training completes. s42 already evaluated.
CLS_SEEDS = {"s42": 89.21, "s123": None, "s456": None}  # placeholder
CWM_SEEDS = {"s42": 89.26, "s123": None, "s456": None}  # placeholder

# 8B means (for Δ computation)
CLS_8B_MEAN = 89.94
CWM_8B_MEAN = 87.33

# TOST parameters
SESOI = 2.0  # ±2 pp, consistent with paper


def tost_ind(x, y, sesoi):
    """Two One-Sided T-tests for equivalence (independent samples)."""
    n1, n2 = len(x), len(y)
    diff = np.mean(x) - np.mean(y)
    se = np.sqrt(np.var(x, ddof=1) / n1 + np.var(y, ddof=1) / n2)
    df = n1 + n2 - 2

    if se == 0:
        p_lower = 0.0 if diff > -sesoi else 1.0
        p_upper = 0.0 if diff < sesoi else 1.0
    else:
        t_lower = (diff - (-sesoi)) / se
        t_upper = (diff - sesoi) / se
        p_lower = 1 - stats.t.cdf(t_lower, df)
        p_upper = stats.t.cdf(t_upper, df)

    return max(p_lower, p_upper), diff, se


def fmt_delta(val):
    if val >= 0:
        return f"+{val:.2f}"
    return f"$-${abs(val):.2f}"


def main():
    # Validate inputs
    cls_vals = []
    cwm_vals = []
    seeds_present = []
    for seed in ["s42", "s123", "s456"]:
        c, w = CLS_SEEDS[seed], CWM_SEEDS[seed]
        if c is not None and w is not None:
            cls_vals.append(c)
            cwm_vals.append(w)
            seeds_present.append(seed)

    n = len(cls_vals)
    print(f"Seeds with data: {seeds_present} (n={n})")

    if n == 0:
        print("ERROR: No seed data available. Fill in CLS_SEEDS and CWM_SEEDS.")
        return

    cls_arr = np.array(cls_vals)
    cwm_arr = np.array(cwm_vals)

    cls_mean, cls_std = cls_arr.mean(), cls_arr.std(ddof=1) if n > 1 else 0.0
    cwm_mean, cwm_std = cwm_arr.mean(), cwm_arr.std(ddof=1) if n > 1 else 0.0

    print(f"\n{'='*60}")
    print("14B 3-seed results")
    print(f"{'='*60}")
    print(f"CLS: {cls_mean:.2f} ± {cls_std:.2f}  (seeds: {cls_vals})")
    print(f"CWM: {cwm_mean:.2f} ± {cwm_std:.2f}  (seeds: {cwm_vals})")
    print(f"Gap: {abs(cls_mean - cwm_mean):.2f} pp (CLS - CWM = {cls_mean - cwm_mean:+.2f})")

    # TOST
    if n >= 2:
        p_equiv, diff, se = tost_ind(cls_arr, cwm_arr, SESOI)
        print(f"\nTOST equivalence test (SESOI = ±{SESOI} pp):")
        print(f"  Mean diff (CLS-CWM): {diff:+.4f}")
        print(f"  SE: {se:.4f}")
        print(f"  p-value: {p_equiv:.4f}")
        if p_equiv < 0.05:
            print(f"  → Equivalent at α=0.05")
        else:
            print(f"  → NOT equivalent at α=0.05 (p={p_equiv:.4f})")
    else:
        print("\nTOST: skipped (need ≥2 seeds)")

    # Deltas from 8B
    cls_delta = cls_mean - CLS_8B_MEAN
    cwm_delta = cwm_mean - CWM_8B_MEAN

    # LaTeX output
    print(f"\n{'='*60}")
    print("Updated LaTeX rows for tab:scaling")
    print(f"{'='*60}")

    if n == 3:
        # Full 3-seed row: need s456 column added to table
        print("% NOTE: Add s456 column to table header")
        print(f"% \\textbf{{Method}} & \\textbf{{Size}} & \\textbf{{s42}} & \\textbf{{s123}} & \\textbf{{s456}} & \\textbf{{Mean}} & \\textbf{{$\\Delta$}} \\\\")
        print()
        s42c, s123c, s456c = CLS_SEEDS["s42"], CLS_SEEDS["s123"], CLS_SEEDS["s456"]
        s42w, s123w, s456w = CWM_SEEDS["s42"], CWM_SEEDS["s123"], CWM_SEEDS["s456"]
        print(f" & 14B & {s42c:.2f} & {s123c:.2f} & {s456c:.2f} & \\textbf{{{cls_mean:.2f} $\\pm$ {cls_std:.2f}}} & {fmt_delta(cls_delta)} \\\\")
        print(f" & 14B & {s42w:.2f} & {s123w:.2f} & {s456w:.2f} & {cwm_mean:.2f} $\\pm$ {cwm_std:.2f} & {fmt_delta(cwm_delta)} \\\\")
    elif n == 2:
        # 2-seed row (current table format works)
        available = {s: (CLS_SEEDS[s], CWM_SEEDS[s]) for s in seeds_present}
        s_names = list(available.keys())
        print(f" & 14B & {available[s_names[0]][0]:.2f} & {available[s_names[1]][0]:.2f} & \\textbf{{{cls_mean:.2f}}} & {fmt_delta(cls_delta)} \\\\")
        print(f" & 14B & {available[s_names[0]][1]:.2f} & {available[s_names[1]][1]:.2f} & {cwm_mean:.2f} & {fmt_delta(cwm_delta)} \\\\")
    else:
        # Single seed (current state)
        print(f" & 14B & {cls_vals[0]:.2f} & --- & {cls_vals[0]:.2f}\\textsuperscript{{$\\dagger$}} & {fmt_delta(cls_delta)} \\\\")
        print(f" & 14B & {cwm_vals[0]:.2f} & --- & {cwm_vals[0]:.2f}\\textsuperscript{{$\\dagger$}} & {fmt_delta(cwm_delta)} \\\\")

    # Also print caption update suggestion
    if n == 3:
        print(f"\n% Suggested caption update:")
        print(f"% Seeds 42/123/456 (14B), seeds 42/123 (4B/8B). All bfloat16 inference.")
        print(f"% Remove 'exploratory' qualifier for 14B.")


if __name__ == "__main__":
    main()
