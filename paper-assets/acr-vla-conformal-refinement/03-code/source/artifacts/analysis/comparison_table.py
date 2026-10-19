#!/usr/bin/env python3
"""Six-way comparison table: seed42 + seed43 + pooled, LaTeX tabular output.

Dependencies: numpy
Usage: python comparison_table.py [--json INPUT.json] [--out TABLE.tex] [--dry-run]
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np

OUT_DIR = Path(__file__).parent.parent / "figures"
OUT_DIR.mkdir(parents=True, exist_ok=True)

SPATIAL_TASKS = [
    "between_plate_and_ramekin",
    "next_to_ramekin",
    "from_table_center",
    "on_cookie_box",
    "in_top_drawer",
    "on_ramekin",
    "next_to_cookie_box",
    "on_stove",
    "next_to_plate",
    "on_wooden_cabinet",
]

TASK_DISPLAY = {
    "between_plate_and_ramekin": "Betw. Plate \\& Ramekin",
    "next_to_ramekin": "Next to Ramekin",
    "from_table_center": "Table Center",
    "on_cookie_box": "On Cookie Box",
    "in_top_drawer": "In Top Drawer",
    "on_ramekin": "On Ramekin",
    "next_to_cookie_box": "Next to Cookie Box",
    "on_stove": "On Stove",
    "next_to_plate": "Next to Plate",
    "on_wooden_cabinet": "On Wooden Cabinet",
}

TRIALS_PER_TASK = 10

# Six methods for comparison
METHODS = [
    "vla_only",
    "vla_mean",
    "argmin",
    "acr_scalar",
    "acr_perdof",
    "acr_obs_only",
]

METHOD_DISPLAY = {
    "vla_only":     "VLA-only (K=1)",
    "vla_mean":     "VLA-mean (K=10)",
    "argmin":       "Argmin (K=10)",
    "acr_scalar":   "ACR scalar",
    "acr_perdof":   "ACR per-DOF",
    "acr_obs_only": "ACR obs-only",
}

# ── placeholder data ──────────────────────────────────────────────────
# Format: {method: {task: SR_0_to_1}}
# Fill these or pass --json
SEED42_DATA = {m: {t: None for t in SPATIAL_TASKS} for m in METHODS}
SEED43_DATA = {m: {t: None for t in SPATIAL_TASKS} for m in METHODS}


def load_data(json_path=None):
    if json_path:
        with open(json_path) as f:
            raw = json.load(f)
        return raw["seed42"], raw["seed43"]
    return SEED42_DATA, SEED43_DATA


def compute_overall_sr(data, method):
    """Compute overall SR for a method from per-task data."""
    vals = [data[method][t] for t in SPATIAL_TASKS if data[method].get(t) is not None]
    if not vals:
        return None
    return np.mean(vals) * 100


def compute_pooled_sr(s42, s43, method):
    """Pool two seeds: average the per-task SRs across seeds, then average across tasks."""
    task_srs = []
    for t in SPATIAL_TASKS:
        sr42 = s42[method].get(t)
        sr43 = s43[method].get(t)
        seed_srs = [s for s in [sr42, sr43] if s is not None]
        if seed_srs:
            task_srs.append(np.mean(seed_srs))
    if not task_srs:
        return None
    return np.mean(task_srs) * 100


def fmt_sr(sr):
    if sr is None:
        return "—"
    return f"{sr:.1f}"


def fmt_sr_bold_best(sr, is_best):
    s = fmt_sr(sr)
    if is_best and s != "—":
        return f"\\textbf{{{s}}}"
    return s


def generate_overall_table(s42, s43):
    """Generate the overall SR comparison table (3 columns: seed42, seed43, pooled)."""
    lines = []
    lines.append("\\begin{tabular}{l ccc}")
    lines.append("\\toprule")
    lines.append("Method & Seed 42 & Seed 43 & Pooled \\\\")
    lines.append("\\midrule")

    pooled_srs = {}
    for m in METHODS:
        pooled_srs[m] = compute_pooled_sr(s42, s43, m)

    valid_pooled = [v for v in pooled_srs.values() if v is not None]
    best_pooled = max(valid_pooled) if valid_pooled else None

    for m in METHODS:
        sr42 = compute_overall_sr(s42, m)
        sr43 = compute_overall_sr(s43, m)
        pooled = pooled_srs[m]
        is_best = (pooled is not None and pooled == best_pooled)
        lines.append(
            f"{METHOD_DISPLAY[m]} & {fmt_sr(sr42)} & {fmt_sr(sr43)} & "
            f"{fmt_sr_bold_best(pooled, is_best)} \\\\"
        )

    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    return "\n".join(lines)


def generate_pertask_table(s42, s43):
    """Generate per-task breakdown for the best two methods (obs_only vs argmin)."""
    m_a, m_b = "acr_obs_only", "argmin"

    lines = []
    lines.append("\\begin{tabular}{l cc cc cc}")
    lines.append("\\toprule")
    lines.append(f" & \\multicolumn{{2}}{{c}}{{Seed 42}} & \\multicolumn{{2}}{{c}}{{Seed 43}} & \\multicolumn{{2}}{{c}}{{Pooled}} \\\\")
    lines.append(f"\\cmidrule(lr){{2-3}} \\cmidrule(lr){{4-5}} \\cmidrule(lr){{6-7}}")
    lines.append(f"Task & {METHOD_DISPLAY[m_a]} & {METHOD_DISPLAY[m_b]} & {METHOD_DISPLAY[m_a]} & {METHOD_DISPLAY[m_b]} & {METHOD_DISPLAY[m_a]} & {METHOD_DISPLAY[m_b]} \\\\")
    lines.append("\\midrule")

    for t in SPATIAL_TASKS:
        sr42_a = s42[m_a].get(t)
        sr42_b = s42[m_b].get(t)
        sr43_a = s43[m_a].get(t)
        sr43_b = s43[m_b].get(t)

        pool_a_vals = [s for s in [sr42_a, sr43_a] if s is not None]
        pool_b_vals = [s for s in [sr42_b, sr43_b] if s is not None]
        pool_a = np.mean(pool_a_vals) * 100 if pool_a_vals else None
        pool_b = np.mean(pool_b_vals) * 100 if pool_b_vals else None

        def pct(v):
            return f"{v*100:.0f}" if v is not None else "—"

        lines.append(
            f"{TASK_DISPLAY[t]} & {pct(sr42_a)} & {pct(sr42_b)} & "
            f"{pct(sr43_a)} & {pct(sr43_b)} & {fmt_sr(pool_a)} & {fmt_sr(pool_b)} \\\\"
        )

    # Overall row
    lines.append("\\midrule")
    sr42_a_all = compute_overall_sr(s42, m_a)
    sr42_b_all = compute_overall_sr(s42, m_b)
    sr43_a_all = compute_overall_sr(s43, m_a)
    sr43_b_all = compute_overall_sr(s43, m_b)
    pool_a_all = compute_pooled_sr(s42, s43, m_a)
    pool_b_all = compute_pooled_sr(s42, s43, m_b)
    lines.append(
        f"\\textbf{{Overall}} & {fmt_sr(sr42_a_all)} & {fmt_sr(sr42_b_all)} & "
        f"{fmt_sr(sr43_a_all)} & {fmt_sr(sr43_b_all)} & "
        f"\\textbf{{{fmt_sr(pool_a_all)}}} & {fmt_sr(pool_b_all)} \\\\"
    )

    lines.append("\\bottomrule")
    lines.append("\\end{tabular}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Six-way comparison table (LaTeX)")
    parser.add_argument("--json", type=str, default=None, help="JSON data file")
    parser.add_argument("--out", type=str, default=None, help="Output .tex file")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if args.dry_run:
        print("dry-run OK: all imports successful")
        return

    s42, s43 = load_data(args.json)

    overall = generate_overall_table(s42, s43)
    pertask = generate_pertask_table(s42, s43)

    out_path = args.out or str(OUT_DIR / "comparison_table.tex")

    output = (
        "% Auto-generated by comparison_table.py\n"
        "% Overall SR comparison (6 methods × 3 columns)\n"
        f"{overall}\n\n"
        "% Per-task breakdown (obs_only vs argmin)\n"
        f"{pertask}\n"
    )

    Path(out_path).write_text(output)
    print(f"Saved: {out_path}")
    print("\n% ── Overall table preview ──")
    print(overall)
    print("\n% ── Per-task table preview ──")
    print(pertask)


if __name__ == "__main__":
    main()
