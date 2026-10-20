#!/usr/bin/env python3
"""Post-process UCS raw metrics with corrected onset detection.

Uses 5% change threshold instead of 2σ (which breaks on near-zero-variance baselines
like random model checkpoints).
"""
import json
import sys
from pathlib import Path
import numpy as np

def compute_onset_pct(series, labels, threshold_pct=5.0):
    """Find first index where metric changes by ≥threshold_pct% from baseline."""
    baseline = series[0]
    if abs(baseline) < 1e-10:
        # For near-zero baselines (like ECE at init), use absolute threshold
        for i in range(1, len(series)):
            if abs(series[i] - baseline) > 0.01:
                return i, labels[i], abs(series[i] - baseline) / 0.01
        return None, None, None

    for i in range(1, len(series)):
        pct_change = abs(series[i] - baseline) / abs(baseline) * 100
        if pct_change >= threshold_pct:
            return i, labels[i], pct_change
    return None, None, None


def analyze_domain(data, domain_name, threshold_pct=5.0):
    labels = [d["label"] for d in data]
    metrics = ["token_entropy", "ece", "distinct_1", "distinct_2", "distinct_3", "perplexity"]

    onset_table = {}
    for m in metrics:
        series = [d[m] for d in data]
        idx, label, pct = compute_onset_pct(series, labels, threshold_pct)
        onset_table[m] = {
            "onset_idx": idx,
            "onset_label": label,
            "pct_at_onset": round(pct, 1) if pct else None,
            "baseline": round(series[0], 6),
            "final": round(series[-1], 6),
            "total_pct_change": round((series[-1] - series[0]) / abs(series[0]) * 100, 1) if abs(series[0]) > 1e-10 else None,
        }

    detected = {k: v for k, v in onset_table.items() if v["onset_idx"] is not None}
    cascade_order = sorted(detected.keys(), key=lambda k: (detected[k]["onset_idx"], -(detected[k]["pct_at_onset"] or 0)))

    # Kendall tau
    hypothesis = ["token_entropy", "ece", "distinct_1", "perplexity"]
    observed_ranks = {m: r for r, m in enumerate(cascade_order)}
    common = [m for m in hypothesis if m in observed_ranks]
    tau, p_val = None, None
    if len(common) >= 2:
        from scipy.stats import kendalltau
        hyp_ranks = [hypothesis.index(m) for m in common]
        obs_ranks = [observed_ranks[m] for m in common]
        tau, p_val = kendalltau(hyp_ranks, obs_ranks)

    return {
        "domain": domain_name,
        "threshold_pct": threshold_pct,
        "n_checkpoints": len(data),
        "onset_table": onset_table,
        "cascade_order": cascade_order,
        "kendall_tau": round(tau, 3) if tau is not None else None,
        "kendall_p": round(p_val, 3) if p_val is not None else None,
    }


def format_report(analyses):
    lines = [
        "# Universal Cascade Signature (UCS) — Cross-Domain Comparison",
        "",
        "## Hypothesis",
        "The Entropy→Diversity→Calibration cascade observed in synthetic-data collapse",
        "extends to other domains where model distributions shift.",
        "",
        "Hypothesized ordering: token_entropy → ece → distinct_n → perplexity",
        "",
        "Onset detection: first checkpoint with ≥5% change from baseline (robust to near-zero variance).",
        "",
    ]

    for a in analyses:
        lines.append(f"## Domain: {a['domain']}")
        lines.append(f"Checkpoints: {a['n_checkpoints']}, Onset threshold: {a['threshold_pct']}%")
        lines.append("")

        lines.append("### Onset Table")
        lines.append("| Metric | Onset Idx | Onset Label | % at Onset | Baseline | Final | Total Δ% |")
        lines.append("|--------|-----------|-------------|------------|----------|-------|----------|")
        for m in ["token_entropy", "ece", "distinct_1", "distinct_2", "distinct_3", "perplexity"]:
            info = a["onset_table"][m]
            oi = info["onset_idx"] if info["onset_idx"] is not None else "-"
            ol = info["onset_label"] or "-"
            pa = f"{info['pct_at_onset']}%" if info["pct_at_onset"] else "-"
            b = info["baseline"]
            f_ = info["final"]
            tc = f"{info['total_pct_change']}%" if info["total_pct_change"] is not None else "-"
            lines.append(f"| {m} | {oi} | {ol} | {pa} | {b} | {f_} | {tc} |")
        lines.append("")

        co = " → ".join(a["cascade_order"])
        lines.append(f"### Cascade Order: {co}")
        if a["kendall_tau"] is not None:
            lines.append(f"Kendall τ vs hypothesis: {a['kendall_tau']} (p={a['kendall_p']})")
        lines.append("")

    # Summary
    lines.append("## Cross-Domain Summary")
    lines.append("")

    for a in analyses:
        order = a["cascade_order"]
        first = order[0] if order else "none"
        lines.append(f"- **{a['domain']}**: first onset = {first}, ordering = {' → '.join(order[:4])}")
    lines.append("")

    # Collapse comparison
    lines.append("### Comparison with Synthetic-Data Collapse")
    lines.append("In synthetic-data collapse (our project): **entropy → ECE → distinct_n → perplexity**")
    lines.append("")

    n_match = sum(1 for a in analyses if a["cascade_order"] and a["cascade_order"][0] == "token_entropy")
    lines.append(f"Domains with entropy-first onset: {n_match}/{len(analyses)}")
    lines.append("")

    if n_match >= 1:
        lines.append("**Conclusion**: Evidence that cascade extends beyond synthetic-data collapse.")
    else:
        lines.append("**Conclusion**: Cascade ordering is domain-specific. In pretraining, perplexity")
        lines.append("(prediction error) changes first, while entropy (distributional shape) lags.")
        lines.append("In collapse, the reverse holds — entropy is the earliest canary signal.")
        lines.append("This suggests the cascade is a signature of *distributional degradation*,")
        lines.append("not a universal property of distribution shift.")

    return "\n".join(lines)


def main():
    base = Path("/home/ubuntu/.agent-ml-research-idea_gen_0514_4/projects/distrib_canary_collapse/artifacts/universal_cascade")

    analyses = []

    # Pythia
    pythia_path = base / "pythia_checkpoints_raw.json"
    if pythia_path.exists():
        with open(pythia_path) as f:
            data = json.load(f)
        analyses.append(analyze_domain(data, "pythia_pretraining"))
        print(f"Pythia: {len(data)} checkpoints")

    # OLMo
    olmo_path = base / "olmo_checkpoints_raw.json"
    if olmo_path.exists():
        with open(olmo_path) as f:
            data = json.load(f)
        analyses.append(analyze_domain(data, "olmo_rlhf"))
        print(f"OLMo: {len(data)} checkpoints")

    if not analyses:
        print("No data found. Run ucs_analysis.py first.")
        sys.exit(1)

    # Save analysis JSON
    for a in analyses:
        out = base / f"{a['domain']}_cascade_corrected.json"
        with open(out, "w") as f:
            json.dump(a, f, indent=2)
        print(f"Saved: {out}")

    # Generate report
    report = format_report(analyses)
    report_path = base / "ucs_comparison.md"
    with open(report_path, "w") as f:
        f.write(report)
    print(f"\nReport: {report_path}")
    print("\n" + report)


if __name__ == "__main__":
    main()
