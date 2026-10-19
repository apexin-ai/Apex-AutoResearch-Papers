#!/usr/bin/env python3
"""Object benchmark analysis: grouped bar chart + LaTeX table for method comparison."""

import json
import os
import re
import sys

import yaml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

# ── paths ──────────────────────────────────────────────────────────────
REGISTRY = os.path.join(os.path.dirname(__file__), "..", "registry.yaml")
OUT_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# ── experiment IDs for object benchmark ────────────────────────────────
OBJECT_EXPERIMENTS = {
    "VLA-only":         ["eval-vla-only-object", "eval-object-v8-full"],
    "VLA-mean":         ["eval-vla-mean-object"],
    "ReconVLA":         ["eval-reconvla-object"],
    "ACR per-DOF":      ["eval-acr-object-v4-perdof"],
    "ACR obs-only":     ["eval-acr-object-v4-obs-only"],
    "ACR scalar":       ["eval-acr-object-v4-scalar"],
    "ACR obs-only-0.2": ["eval-acr-object-obs-only-norm02"],
}

# Canonical task order for object benchmark
OBJECT_TASKS = [
    "alphabet_soup", "cream_cheese", "salad_dressing", "bbq_sauce",
    "ketchup", "tomato_sauce", "butter", "milk",
    "chocolate_pudding", "orange_juice",
]

# Display-friendly task names
TASK_DISPLAY = {
    "alphabet_soup": "Alphabet\nSoup",
    "cream_cheese": "Cream\nCheese",
    "salad_dressing": "Salad\nDressing",
    "bbq_sauce": "BBQ\nSauce",
    "ketchup": "Ketchup",
    "tomato_sauce": "Tomato\nSauce",
    "butter": "Butter",
    "milk": "Milk",
    "chocolate_pudding": "Choc.\nPudding",
    "orange_juice": "Orange\nJuice",
}

METHOD_ORDER = ["VLA-only", "VLA-mean", "ReconVLA", "ACR per-DOF", "ACR obs-only", "ACR scalar"]


def load_registry():
    with open(REGISTRY) as f:
        return yaml.safe_load(f)


def normalize_sr(val):
    """Normalize success rate to 0-100 scale.

    Handles: int(19), float(19.0), "19%", "19.0% (19/100)", float(0.19),
    dict({"sr": 0.19, ...})
    """
    if isinstance(val, dict):
        val = val.get("sr", val.get("success_rate", 0))
    if isinstance(val, str):
        match = re.search(r"([\d.]+)\s*%", val)
        if match:
            return float(match.group(1))
        try:
            val = float(val)
        except ValueError:
            return 0.0
    val = float(val)
    if val <= 1.0 and val > 0:
        val = val * 100
    return val


def extract_per_task(exp, task_list):
    """Extract per-task SR from experiment metrics."""
    m = exp.get("metrics", {})
    if not m:
        return {}

    result = {}

    # From per_task dict (completed experiments)
    per_task = m.get("per_task", {})
    if per_task:
        for task in task_list:
            for key, val in per_task.items():
                if task in key.lower().replace(" ", "_"):
                    result[task] = normalize_sr(val)
                    break

    # From partial_results (in-progress)
    partial = m.get("partial_results", {})
    if partial:
        for task in task_list:
            for key, val in partial.items():
                if task in key.lower().replace(" ", "_"):
                    match = re.search(r"([\d.]+)%", str(val))
                    if match:
                        result[task] = float(match.group(1))
                    break

    # From per_task_partial
    per_task_partial = m.get("per_task_partial", {})
    if per_task_partial:
        for task in task_list:
            for key, val in per_task_partial.items():
                if task in key.lower().replace(" ", "_"):
                    result[task] = normalize_sr(val)
                    break

    return result


def extract_overall_sr(exp):
    m = exp.get("metrics", {})
    if not m:
        return None
    for key in ("overall_success_rate", "overall_sr", "overall_success_rate_10tasks",
                "overall_SR", "avg_SR_10task", "overall_sr_10task"):
        if key in m:
            return normalize_sr(m[key])
    per_task = m.get("per_task", {})
    if per_task:
        return sum(normalize_sr(v) for v in per_task.values()) / len(per_task)
    return None


def collect_object_data(exps):
    """Collect per-task and overall SR for each method."""
    methods = {}

    for method_name, exp_ids in OBJECT_EXPERIMENTS.items():
        best_exp = None
        best_n_tasks = 0

        for eid in exp_ids:
            if eid not in exps:
                continue
            exp = exps[eid]
            per_task = extract_per_task(exp, OBJECT_TASKS)
            if len(per_task) > best_n_tasks:
                best_n_tasks = len(per_task)
                best_exp = {
                    "exp_id": eid,
                    "status": exp.get("status"),
                    "conclusion": exp.get("conclusion"),
                    "per_task": per_task,
                    "overall_sr": extract_overall_sr(exp),
                    "n_tasks": len(per_task),
                }

        if best_exp:
            methods[method_name] = best_exp

    return methods


def plot_grouped_bar(methods):
    """Generate grouped bar chart for object benchmark."""
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "DejaVu Serif"],
        "font.size": 10,
        "axes.labelsize": 12,
        "axes.titlesize": 13,
        "legend.fontsize": 8.5,
        "xtick.labelsize": 8,
        "ytick.labelsize": 10,
        "axes.linewidth": 0.8,
        "figure.dpi": 150,
    })

    colors = {
        "VLA-only":         "#AAAAAA",
        "VLA-mean":         "#888888",
        "ReconVLA":         "#555555",
        "ACR per-DOF":      "#2E86AB",
        "ACR obs-only":     "#A23B72",
        "ACR scalar":       "#E8A838",
        "ACR obs-only-0.2": "#6B4C9A",
    }

    hatches = {
        "VLA-only":    "",
        "VLA-mean":    "//",
        "ReconVLA":    "",
        "ACR per-DOF": "",
        "ACR obs-only": "",
        "ACR scalar":  "",
        "ACR obs-only-0.2": "\\\\",
    }

    # Filter to methods that have data
    active_methods = [m for m in METHOD_ORDER if m in methods]
    if not active_methods:
        active_methods = [m for m in methods if m in METHOD_ORDER]
    # Add any extra methods not in standard order
    for m in methods:
        if m not in active_methods:
            active_methods.append(m)

    n_methods = len(active_methods)
    n_tasks = len(OBJECT_TASKS)

    if n_methods == 0:
        print("No object benchmark data available yet.")
        return

    fig, ax = plt.subplots(figsize=(12, 5))

    bar_width = 0.8 / n_methods
    x = np.arange(n_tasks)

    for i, method in enumerate(active_methods):
        mdata = methods[method]
        srs = [mdata["per_task"].get(t, float("nan")) for t in OBJECT_TASKS]
        offset = (i - n_methods / 2 + 0.5) * bar_width
        bars = ax.bar(x + offset, srs, bar_width * 0.9,
                      label=method, color=colors.get(method, f"C{i}"),
                      hatch=hatches.get(method, ""),
                      edgecolor="white", linewidth=0.5, zorder=3)

    ax.set_xlabel("Task")
    ax.set_ylabel("Success Rate (%)")
    ax.set_title("Object Benchmark: Per-Task Success Rate")
    ax.set_xticks(x)
    ax.set_xticklabels([TASK_DISPLAY.get(t, t) for t in OBJECT_TASKS], ha="center")
    ax.set_ylim(0, 55)
    ax.grid(True, axis="y", alpha=0.3, ls="-", lw=0.5, zorder=0)
    ax.legend(loc="upper right", ncol=2, framealpha=0.9, edgecolor="gray")

    # Add overall SR annotation
    overall_text = "  ".join(
        f"{m}: {methods[m]['overall_sr']:.0f}%" if methods[m]['overall_sr'] is not None
        else f"{m}: {methods[m]['n_tasks']}/10 tasks"
        for m in active_methods
    )
    ax.annotate(overall_text, xy=(0.5, -0.12), xycoords="axes fraction",
                ha="center", fontsize=7.5, color="gray", style="italic")

    fig.tight_layout()
    out_path = os.path.join(OUT_DIR, "object_benchmark.pdf")
    fig.savefig(out_path, bbox_inches="tight", dpi=300)
    print(f"Saved: {out_path}")

    png_path = out_path.replace(".pdf", ".png")
    fig.savefig(png_path, bbox_inches="tight", dpi=200)
    print(f"Saved: {png_path}")
    plt.close(fig)


def generate_latex_table(methods):
    """Generate LaTeX table: methods × tasks."""
    active_methods = [m for m in METHOD_ORDER if m in methods]
    for m in methods:
        if m not in active_methods:
            active_methods.append(m)

    if not active_methods:
        print("No data for LaTeX table.")
        return ""

    n_tasks = len(OBJECT_TASKS)
    short_tasks = [t.replace("_", " ").title() for t in OBJECT_TASKS]

    # Build table
    col_spec = "l" + "c" * n_tasks + "c"  # method + tasks + overall
    lines = []
    lines.append(r"\begin{table}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Object Benchmark: Per-Task Success Rate (\%)}")
    lines.append(r"\label{tab:object-benchmark}")
    lines.append(r"\resizebox{\textwidth}{!}{%")
    lines.append(r"\begin{tabular}{" + col_spec + "}")
    lines.append(r"\toprule")

    # Header
    header = "Method"
    for t in OBJECT_TASKS:
        short = t.replace("_", " ").title()
        if len(short) > 10:
            parts = short.split()
            short = parts[0][:4] + "."
            if len(parts) > 1:
                short += " " + parts[1][:4] + "."
        header += f" & \\rotatebox{{60}}{{{short}}}"
    header += r" & \textbf{Avg.} \\"
    lines.append(header)
    lines.append(r"\midrule")

    # Data rows
    for method in active_methods:
        mdata = methods[method]
        row = method.replace("_", r"\_")
        task_srs = []
        for t in OBJECT_TASKS:
            sr = mdata["per_task"].get(t)
            if sr is not None:
                val = sr
                task_srs.append(val)
                row += f" & {val:.0f}"
            else:
                row += " & --"

        # Overall
        if mdata["overall_sr"] is not None:
            row += f" & \\textbf{{{mdata['overall_sr']:.0f}}}"
        elif task_srs:
            avg = sum(task_srs) / len(task_srs)
            row += f" & {avg:.0f}$^*$"
        else:
            row += " & --"

        row += r" \\"
        lines.append(row)

    lines.append(r"\bottomrule")
    lines.append(r"\end{tabular}}")
    lines.append(r"\end{table}")

    latex = "\n".join(lines)

    out_path = os.path.join(OUT_DIR, "object_benchmark_table.tex")
    with open(out_path, "w") as f:
        f.write(latex)
    print(f"Saved: {out_path}")

    # Also save JSON
    json_data = {}
    for method in active_methods:
        mdata = methods[method]
        json_data[method] = {
            "per_task": {t: mdata["per_task"].get(t) for t in OBJECT_TASKS},
            "overall_sr": mdata["overall_sr"],
            "n_tasks_completed": mdata["n_tasks"],
            "exp_id": mdata["exp_id"],
            "status": mdata["status"],
        }

    json_path = os.path.join(OUT_DIR, "object_benchmark_data.json")
    with open(json_path, "w") as f:
        json.dump(json_data, f, indent=2)
    print(f"Saved: {json_path}")

    return latex


def main():
    data = load_registry()
    exps = data.get("experiments", {})
    methods = collect_object_data(exps)

    print("=" * 60)
    print("OBJECT BENCHMARK ANALYSIS")
    print("=" * 60)

    for method, mdata in methods.items():
        sr_str = f"{mdata['overall_sr']:.0f}%" if mdata['overall_sr'] else "N/A"
        print(f"\n{method} [{mdata['status']}] ({mdata['exp_id']})")
        print(f"  Overall: {sr_str}  ({mdata['n_tasks']}/{len(OBJECT_TASKS)} tasks)")
        for t in OBJECT_TASKS:
            if t in mdata["per_task"]:
                print(f"    {t}: {mdata['per_task'][t]:.0f}%")

    if not methods:
        print("\nNo object benchmark results available yet.")
        return

    plot_grouped_bar(methods)
    latex = generate_latex_table(methods)

    if latex:
        print("\n── LaTeX Table ──")
        print(latex)


if __name__ == "__main__":
    main()
