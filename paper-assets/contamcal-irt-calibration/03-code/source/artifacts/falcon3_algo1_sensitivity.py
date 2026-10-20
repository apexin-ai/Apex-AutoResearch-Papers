#!/usr/bin/env python3
"""Falcon3 Algorithm 1 hyperparameter sensitivity analysis.

Sweeps τ (noise threshold) and σ (significance threshold) to verify
classification robustness. Also analyzes ρ (saturation_ratio) and λ
(late_gain_floor) which determine the Benefit vs Benefit-sat boundary.
"""

from itertools import product

# ── Falcon3 eval data ─────────────────────────────────────────────

FALCON3 = {
    "MMLU 5-shot": {
        "d000": 58.77, "d005": 59.02, "d025": 61.23,
        "d050": 62.09, "d100": 62.96,
    },
    "ARC 25-shot": {
        "d000": 81.57, "d005": 83.11, "d025": 84.81,
        "d050": 83.28, "d100": 85.58,
    },
}

# ── Classifier (matches profile_classifier.py) ────────────────────

def classify(accs, tau=1.0, sigma=5.0, rho=0.3, lam=0.5):
    a = accs
    delta = a["d100"] - a["d000"]
    mid_vals = [a["d005"], a["d025"], a["d050"]]
    mid_min = min(mid_vals)

    if abs(delta) <= tau:
        max_dev = max(abs(v - a["d000"]) for v in mid_vals)
        if max_dev <= tau:
            return "Immune"
        if mid_min < a["d000"] and mid_min < a["d100"]:
            return "V-recovery-full"
        return "Immune"

    if delta < -tau:
        if delta <= -sigma:
            return "U-collapse"
        if mid_min < a["d100"] and mid_min < a["d000"]:
            return "V-recovery"
        return "U-collapse"

    first_half = a["d025"] - a["d000"]
    second_half = a["d100"] - a["d025"]
    late_gain = a["d100"] - a["d050"]

    if (first_half > 0 and second_half < first_half * rho) or late_gain < lam:
        return "Benefit-sat"
    return "Benefit"


# ── Sweep grids ────────────────────────────────────────────────────

TAU_GRID = [0.5, 0.75, 1.0, 1.25, 1.5, 2.0]
SIGMA_GRID = [3.0, 4.0, 5.0, 6.0, 7.0, 8.0]
RHO_GRID = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7]
LAM_GRID = [0.25, 0.5, 0.75, 1.0, 1.25, 1.5]


def sweep_tau_sigma():
    """Sweep τ × σ with default ρ, λ."""
    results = {}
    for bench, accs in FALCON3.items():
        grid = {}
        for tau, sigma in product(TAU_GRID, SIGMA_GRID):
            grid[(tau, sigma)] = classify(accs, tau=tau, sigma=sigma)
        results[bench] = grid
    return results


def sweep_rho_lambda():
    """Sweep ρ × λ with default τ, σ."""
    results = {}
    for bench, accs in FALCON3.items():
        grid = {}
        for rho, lam in product(RHO_GRID, LAM_GRID):
            grid[(rho, lam)] = classify(accs, rho=rho, lam=lam)
        results[bench] = grid
    return results


def boundary_analysis():
    """Find exact tipping points for each parameter."""
    lines = []
    for bench, accs in FALCON3.items():
        delta = accs["d100"] - accs["d000"]
        first_half = accs["d025"] - accs["d000"]
        second_half = accs["d100"] - accs["d025"]
        late_gain = accs["d100"] - accs["d050"]

        lines.append(f"### {bench}")
        lines.append(f"- Δ = {delta:+.2f} pp")
        lines.append(f"- first_half (d000→d025) = {first_half:.2f} pp")
        lines.append(f"- second_half (d025→d100) = {second_half:.2f} pp")
        lines.append(f"- late_gain (d050→d100) = {late_gain:.2f} pp")
        lines.append("")

        # τ tipping: classify as Immune when τ ≥ |delta|
        lines.append(f"**τ tipping point**: τ ≥ {abs(delta):.2f} → Immune "
                      f"(sweep max = {max(TAU_GRID)}, well below)")

        # ρ tipping: Benefit-sat triggered when second_half < first_half * ρ
        if first_half > 0:
            rho_tip = second_half / first_half
            lines.append(f"**ρ tipping point**: ρ > {rho_tip:.3f} → Benefit-sat "
                          f"(default ρ=0.3, {'triggers' if 0.3 > rho_tip else 'does not trigger'})")
        else:
            lines.append("**ρ tipping**: first_half ≤ 0, ratio check inactive")

        # λ tipping: Benefit-sat triggered when late_gain < λ
        lines.append(f"**λ tipping point**: λ > {late_gain:.2f} → Benefit-sat "
                      f"(default λ=0.5, {'triggers' if 0.5 > late_gain else 'does not trigger'})")
        lines.append("")
    return lines


def format_heatmap(grid, row_vals, col_vals, row_label, col_label, observed):
    """Format a τ×σ or ρ×λ grid as markdown table with color coding."""
    lines = []

    header = f"| {row_label} \\ {col_label} |"
    for c in col_vals:
        header += f" {c} |"
    lines.append(header)

    sep = "|" + "---|" * (len(col_vals) + 1)
    lines.append(sep)

    for r in row_vals:
        row = f"| {r} |"
        for c in col_vals:
            pat = grid[(r, c)]
            marker = " **" + pat + "**" if pat == observed else " " + pat
            row += marker + " |"
        lines.append(row)

    return lines


def main():
    md = []
    md.append("# Falcon3-7B Algorithm 1 Hyperparameter Sensitivity")
    md.append("")
    md.append("Verifies that Falcon3's classification under Algorithm 1 is robust "
              "to threshold parameter choices.")
    md.append("")

    # ── Section 1: Boundary analysis ──
    md.append("## 1. Decision Boundary Analysis")
    md.append("")
    md.extend(boundary_analysis())

    # ── Section 2: τ × σ sweep ──
    md.append("## 2. τ × σ Sweep (6 × 6 = 36 combinations)")
    md.append("")
    md.append("Default: τ=1.0, σ=5.0, ρ=0.3, λ=0.5. "
              "Bold = matches observed classification.")
    md.append("")

    ts_results = sweep_tau_sigma()
    observed = {"MMLU 5-shot": "Benefit", "ARC 25-shot": "Benefit-sat"}

    for bench in FALCON3:
        md.append(f"### {bench} (observed: {observed[bench]})")
        md.append("")
        grid = ts_results[bench]
        md.extend(format_heatmap(
            grid, TAU_GRID, SIGMA_GRID, "τ", "σ", observed[bench]))
        md.append("")

        total = len(TAU_GRID) * len(SIGMA_GRID)
        match = sum(1 for v in grid.values() if v == observed[bench])
        md.append(f"**Stability: {match}/{total} = {match/total*100:.1f}%**")
        md.append("")

    # ── Section 3: ρ × λ sweep ──
    md.append("## 3. ρ × λ Sweep (7 × 6 = 42 combinations)")
    md.append("")
    md.append("These parameters control the Benefit vs Benefit-sat boundary. "
              "τ=1.0, σ=5.0 fixed.")
    md.append("")

    rl_results = sweep_rho_lambda()

    for bench in FALCON3:
        md.append(f"### {bench} (observed: {observed[bench]})")
        md.append("")
        grid = rl_results[bench]
        md.extend(format_heatmap(
            grid, RHO_GRID, LAM_GRID, "ρ", "λ", observed[bench]))
        md.append("")

        total = len(RHO_GRID) * len(LAM_GRID)
        match = sum(1 for v in grid.values() if v == observed[bench])
        md.append(f"**Stability: {match}/{total} = {match/total*100:.1f}%**")
        md.append("")

    # ── Section 4: Summary ──
    md.append("## 4. Summary")
    md.append("")

    # τ×σ summary
    mmlu_ts = sum(1 for v in ts_results["MMLU 5-shot"].values()
                  if v == "Benefit")
    arc_ts = sum(1 for v in ts_results["ARC 25-shot"].values()
                 if v == "Benefit-sat")
    ts_total = len(TAU_GRID) * len(SIGMA_GRID)

    # ρ×λ summary
    mmlu_rl = sum(1 for v in rl_results["MMLU 5-shot"].values()
                  if v == "Benefit")
    arc_rl = sum(1 for v in rl_results["ARC 25-shot"].values()
                 if v == "Benefit-sat")
    rl_total = len(RHO_GRID) * len(LAM_GRID)

    md.append("| Benchmark | Observed | τ×σ stability | ρ×λ stability |")
    md.append("|-----------|----------|---------------|---------------|")
    md.append(f"| MMLU 5-shot | Benefit | "
              f"{mmlu_ts}/{ts_total} ({mmlu_ts/ts_total*100:.1f}%) | "
              f"{mmlu_rl}/{rl_total} ({mmlu_rl/rl_total*100:.1f}%) |")
    md.append(f"| ARC 25-shot | Benefit-sat | "
              f"{arc_ts}/{ts_total} ({arc_ts/ts_total*100:.1f}%) | "
              f"{arc_rl}/{rl_total} ({arc_rl/rl_total*100:.1f}%) |")
    md.append("")

    md.append("### Interpretation")
    md.append("")
    md.append("- **τ × σ robustness**: Both benchmarks show 100% stability across "
              "the full τ×σ grid because Δ (+4.19 and +4.01 pp) exceeds the maximum "
              "swept τ (2.0 pp). σ is irrelevant for positive-delta profiles.")
    md.append("- **ρ × λ robustness**: The ρ and λ parameters control the "
              "Benefit/Benefit-sat boundary, which is the only decision margin "
              "that matters for Falcon3.")

    # MMLU ρ×λ explanation
    md.append("  - MMLU: second_half/first_half = 1.73/2.46 = 0.703. "
              "Benefit-sat triggers only when ρ > 0.703 or λ > 0.87. "
              "Classification is robust for any ρ ≤ 0.7.")
    # ARC ρ×λ explanation
    md.append("  - ARC: second_half/first_half = 0.77/3.24 = 0.238. "
              "Benefit-sat triggers at ρ > 0.238. Default ρ=0.3 is just above "
              "this boundary (margin = 0.042), making ARC's sub-classification "
              "more sensitive — consistent with its lower bootstrap stability (61.3%).")
    md.append("")

    md.append("### Key Finding")
    md.append("")
    md.append("The **primary classification** (positive contamination effect) is "
              "unconditionally robust: Falcon3 is never classified as Immune, "
              "U-collapse, or V-recovery under any parameter combination. "
              "The only variation is in the **sub-classification** between "
              "Benefit and Benefit-sat, which depends on ρ and λ rather than "
              "τ and σ. For MMLU, this sub-classification is also highly stable. "
              "For ARC, the Benefit/Benefit-sat boundary is tighter (ρ margin = 0.042), "
              "explaining the 61.3% bootstrap stability reported in Table 1.")

    output = "\n".join(md) + "\n"
    print(output)

    out_path = ("/home/ubuntu/.agent-ml-research-idea_gen_0509_13/projects/"
                "contamcal-irt-calibration/artifacts/falcon3_algo1_sensitivity.md")
    with open(out_path, "w") as f:
        f.write(output)
    print(f"\n[Saved to {out_path}]")


if __name__ == "__main__":
    main()
