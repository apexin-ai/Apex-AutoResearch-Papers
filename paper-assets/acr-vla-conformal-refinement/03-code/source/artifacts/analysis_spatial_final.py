#!/usr/bin/env python3
"""Spatial benchmark final analysis: merge partial + restart results, generate comparison table."""

import json
import os
import re
import sys

import yaml
import matplotlib
matplotlib.use("Agg")

# ── paths ──────────────────────────────────────────────────────────────
REGISTRY = os.path.join(os.path.dirname(__file__), "..", "registry.yaml")
OUT_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# ── canonical spatial tasks (order from eval-spatial-v7-full) ──────────
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

TASK_SHORT_TO_FULL = {t: f"pick_up_black_bowl_{t}" for t in SPATIAL_TASKS}

TASK_DISPLAY = {
    "between_plate_and_ramekin": "Betw. Plate\n& Ramekin",
    "next_to_ramekin": "Next to\nRamekin",
    "from_table_center": "Table\nCenter",
    "on_cookie_box": "On Cookie\nBox",
    "in_top_drawer": "In Top\nDrawer",
    "on_ramekin": "On\nRamekin",
    "next_to_cookie_box": "Next to\nCookie Box",
    "on_stove": "On\nStove",
    "next_to_plate": "Next to\nPlate",
    "on_wooden_cabinet": "On Wooden\nCabinet",
}

# ── experiments to merge per method ────────────────────────────────────
# Each method maps to a list of experiment IDs to merge (base + restarts).
# Later experiments overwrite earlier ones for the same task.
SPATIAL_METHODS = {
    "VLA-only (K=1)": {
        "exp_ids": ["eval-spatial-v7-full"],
        "color": "#AAAAAA",
    },
    "VLA-mean (K=10)": {
        "exp_ids": ["eval-vla-mean-spatial", "eval-vla-mean-spatial-t10"],
        "color": "#888888",
    },
    "ReconVLA argmin (K=10)": {
        "exp_ids": ["eval-reconvla-spatial-v3"],
        "color": "#555555",
    },
    "Argmin-only (K=10)": {
        "exp_ids": ["eval-argmin-only-spatial", "eval-argmin-only-spatial-r2"],
        "color": "#777777",
    },
    "ACR per-DOF": {
        "exp_ids": ["eval-acr-spatial-v4-small", "eval-acr-spatial-v4-small-r2"],
        "color": "#2E86AB",
    },
    "ACR obs-only": {
        "exp_ids": ["eval-acr-spatial-v4-obs-only-r2", "eval-acr-spatial-v4-obs-only-r3"],
        "color": "#A23B72",
    },
    "ACR scalar": {
        "exp_ids": ["eval-acr-spatial-v4-scalar", "eval-acr-spatial-v4-scalar-r2"],
        "color": "#E8A838",
    },
    "ACR tiny (norm=0.05)": {
        "exp_ids": ["eval-tiny-correction-spatial"],
        "color": "#6B4C9A",
    },
}

# T-index to task mapping (registry uses T0-T9, not T1-T10)
T_INDEX_MAP = {f"T{i}": SPATIAL_TASKS[i] for i in range(10)}
# Also map "on_wooden_shelf" -> "on_wooden_cabinet" (known alias)
TASK_ALIASES = {
    "on_wooden_shelf": "on_wooden_cabinet",
    "between_plate_ramekin": "between_plate_and_ramekin",
}


def load_registry():
    with open(REGISTRY) as f:
        return yaml.safe_load(f)


def normalize_sr(val):
    """Convert any SR format to 0-1 float. Downstream code multiplies by 100 for display.

    Handles: int(19), float(19.0), "19%", "19.0% (19/100)", float(0.19),
    dict({"sr": 0.19, ...})
    """
    if isinstance(val, dict):
        val = val.get("sr", val.get("success_rate", 0))
    if isinstance(val, str):
        match = re.search(r"([\d.]+)\s*%", val)
        if match:
            return float(match.group(1)) / 100
        try:
            val = float(val)
        except ValueError:
            return 0.0
    val = float(val)
    if val > 1:
        val = val / 100
    return val


def normalize_task_name(name):
    """Normalize task name to canonical short form."""
    # Strip full prefix
    name = name.replace("pick_up_black_bowl_", "")
    # Strip T{n}_ prefix (e.g. "T1_between_plate_ramekin" -> "between_plate_ramekin")
    name = re.sub(r"^T\d+_", "", name)
    # T-index mapping (bare "T1", "T2", ...)
    if name in T_INDEX_MAP:
        return T_INDEX_MAP[name]
    # Aliases
    name = TASK_ALIASES.get(name, name)
    # Fuzzy alias match
    for alias, canonical in TASK_ALIASES.items():
        if alias in name:
            return canonical
    return name


def extract_task_results(exp):
    """Extract per-task results from experiment, returning {task_short: sr}."""
    m = exp.get("metrics", {})
    if not m:
        return {}

    results = {}

    # per_task dict (completed experiments)
    for key, val in m.get("per_task", {}).items():
        task = normalize_task_name(key)
        if task in SPATIAL_TASKS:
            results[task] = normalize_sr(val)

    # partial_results (in-progress, format: "60.0% (6/10)")
    for key, val in m.get("partial_results", {}).items():
        task = normalize_task_name(key)
        if task in SPATIAL_TASKS:
            match = re.search(r"([\d.]+)%", str(val))
            if match:
                results[task] = float(match.group(1)) / 100.0

    # per_task_partial
    for key, val in m.get("per_task_partial", {}).items():
        task = normalize_task_name(key)
        if task in SPATIAL_TASKS:
            results[task] = normalize_sr(val)

    # Handle T1-T10 at metrics top level (e.g. eval-vla-mean-spatial)
    for key, val in m.items():
        if re.match(r"^T\d+$", key) and key in T_INDEX_MAP:
            task = T_INDEX_MAP[key]
            results[task] = normalize_sr(val)
        elif re.match(r"^T\d+_", key):
            task = normalize_task_name(key)
            if task in SPATIAL_TASKS:
                if isinstance(val, (int, float)):
                    results[task] = normalize_sr(val)
                else:
                    match = re.search(r"(\d+)%", str(val))
                    if match:
                        results[task] = float(match.group(1)) / 100.0

    return results


def merge_method_results(exps, exp_ids):
    """Merge results from multiple experiments (base + restarts). Later overwrite earlier."""
    merged = {}
    sources = {}

    for eid in exp_ids:
        if eid not in exps:
            continue
        task_results = extract_task_results(exps[eid])
        for task, sr in task_results.items():
            merged[task] = sr
            sources[task] = eid

    return merged, sources


def collect_all_methods(exps):
    """Collect per-task results for all methods."""
    all_methods = {}

    for method_name, cfg in SPATIAL_METHODS.items():
        merged, sources = merge_method_results(exps, cfg["exp_ids"])
        n_tasks = len(merged)
        overall = sum(merged.values()) / n_tasks if n_tasks > 0 else None

        all_methods[method_name] = {
            "per_task": merged,
            "sources": sources,
            "n_tasks": n_tasks,
            "overall_sr": overall,
            "complete": n_tasks == 10,
            "color": cfg["color"],
        }

    return all_methods


def generate_latex_table(all_methods):
    """Generate LaTeX table: methods × spatial tasks."""
    n_tasks = len(SPATIAL_TASKS)
    col_spec = "l" + "c" * n_tasks + "c"

    lines = []
    lines.append(r"\begin{table*}[t]")
    lines.append(r"\centering")
    lines.append(r"\caption{Spatial Benchmark: Per-Task Success Rate (\%). Best per-task in \textbf{bold}.}")
    lines.append(r"\label{tab:spatial-final}")
    lines.append(r"\resizebox{\textwidth}{!}{%")
    lines.append(r"\begin{tabular}{" + col_spec + "}")
    lines.append(r"\toprule")

    # Header
    header = "Method"
    for t in SPATIAL_TASKS:
        short = t.replace("_", " ").title()
        # Abbreviate long names
        abbrev_map = {
            "Between Plate And Ramekin": "Btw P\\&R",
            "Next To Ramekin": "Nxt Ram",
            "From Table Center": "Tbl Ctr",
            "On Cookie Box": "On CkBx",
            "In Top Drawer": "Top Drw",
            "On Ramekin": "On Ram",
            "Next To Cookie Box": "Nxt CkBx",
            "On Stove": "On Stv",
            "Next To Plate": "Nxt Plt",
            "On Wooden Cabinet": "On WdCb",
        }
        short = abbrev_map.get(short, short[:8])
        header += f" & \\rotatebox{{60}}{{{short}}}"
    header += r" & \textbf{Avg.} \\"
    lines.append(header)
    lines.append(r"\midrule")

    # Find best per task (for bolding)
    best_per_task = {}
    for t in SPATIAL_TASKS:
        best_sr = -1
        for m, mdata in all_methods.items():
            sr = mdata["per_task"].get(t)
            if sr is not None and sr > best_sr:
                best_sr = sr
        if best_sr >= 0:
            best_per_task[t] = best_sr

    # Method rows — baselines first, then ACR variants
    method_order = [
        "VLA-only (K=1)", "VLA-mean (K=10)", "ReconVLA argmin (K=10)", "Argmin-only (K=10)",
        "ACR per-DOF", "ACR obs-only", "ACR scalar", "ACR tiny (norm=0.05)",
    ]
    active_methods = [m for m in method_order if m in all_methods]

    for i, method in enumerate(active_methods):
        if i == 4 and any(m.startswith("ACR") for m in active_methods[i:]):
            lines.append(r"\midrule")

        mdata = all_methods[method]
        row = method.replace("_", r"\_").replace("&", r"\&")
        if not mdata["complete"]:
            row += f"$^{{{mdata['n_tasks']}}}$"

        task_srs = []
        for t in SPATIAL_TASKS:
            sr = mdata["per_task"].get(t)
            if sr is not None:
                val = sr * 100
                task_srs.append(val)
                cell = f"{val:.0f}"
                if t in best_per_task and abs(sr - best_per_task[t]) < 1e-6:
                    cell = f"\\textbf{{{cell}}}"
                row += f" & {cell}"
            else:
                row += " & --"

        # Overall
        if mdata["overall_sr"] is not None:
            avg = mdata["overall_sr"] * 100
            avg_str = f"{avg:.1f}"
            if mdata["complete"]:
                row += f" & \\textbf{{{avg_str}}}"
            else:
                row += f" & {avg_str}$^*$"
        else:
            row += " & --"

        row += r" \\"
        lines.append(row)

    lines.append(r"\bottomrule")
    lines.append(r"\multicolumn{" + str(n_tasks + 2) + r"}{l}{\footnotesize $^n$ = only $n$/10 tasks completed. $^*$ = partial average.} \\")
    lines.append(r"\end{tabular}}")
    lines.append(r"\end{table*}")

    latex = "\n".join(lines)

    out_path = os.path.join(OUT_DIR, "spatial_final_table.tex")
    with open(out_path, "w") as f:
        f.write(latex)
    print(f"Saved: {out_path}")

    return latex


def generate_json_summary(all_methods):
    """Generate JSON summary of all spatial results."""
    summary = {}

    for method, mdata in all_methods.items():
        summary[method] = {
            "per_task": {t: mdata["per_task"].get(t) for t in SPATIAL_TASKS},
            "overall_sr": mdata["overall_sr"],
            "n_tasks": mdata["n_tasks"],
            "complete": mdata["complete"],
            "sources": mdata["sources"],
        }

    out_path = os.path.join(OUT_DIR, "spatial_final_data.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Saved: {out_path}")

    return summary


def main():
    data = load_registry()
    exps = data.get("experiments", {})
    all_methods = collect_all_methods(exps)

    print("=" * 60)
    print("SPATIAL BENCHMARK - FINAL COMPARISON")
    print("=" * 60)

    # Summary table
    header = f"{'Method':<28} {'Tasks':>5} {'Overall':>8}  Status"
    print(f"\n{header}")
    print("-" * len(header))

    for method, mdata in all_methods.items():
        sr_str = f"{mdata['overall_sr']*100:.1f}%" if mdata['overall_sr'] else "N/A"
        status = "COMPLETE" if mdata['complete'] else f"PARTIAL ({mdata['n_tasks']}/10)"
        print(f"{method:<28} {mdata['n_tasks']:>5} {sr_str:>8}  {status}")

    # Per-task detail
    print(f"\n{'Task':<30}", end="")
    method_names = list(all_methods.keys())
    for m in method_names:
        print(f" {m[:12]:>12}", end="")
    print()
    print("-" * (30 + 13 * len(method_names)))

    for t in SPATIAL_TASKS:
        print(f"{t:<30}", end="")
        for m in method_names:
            sr = all_methods[m]["per_task"].get(t)
            if sr is not None:
                print(f" {sr*100:>11.0f}%", end="")
            else:
                print(f" {'--':>12}", end="")
        print()

    # Improvement analysis
    print("\n── ACR vs Baselines ──")
    baselines = {
        "VLA-only (K=1)": all_methods.get("VLA-only (K=1)", {}).get("overall_sr"),
        "ReconVLA argmin (K=10)": all_methods.get("ReconVLA argmin (K=10)", {}).get("overall_sr"),
    }

    for method in all_methods:
        if not method.startswith("ACR"):
            continue
        mdata = all_methods[method]
        if mdata["overall_sr"] is None:
            continue

        sr = mdata["overall_sr"]
        for bname, bsr in baselines.items():
            if bsr is not None:
                delta = (sr - bsr) * 100
                rel = (sr - bsr) / bsr * 100 if bsr > 0 else float("inf")
                suffix = f"({'PARTIAL' if not mdata['complete'] else 'FULL'})"
                print(f"  {method} vs {bname}: {delta:+.1f}pp ({rel:+.1f}% relative) {suffix}")

    # Generate outputs
    latex = generate_latex_table(all_methods)
    summary = generate_json_summary(all_methods)

    print("\n── LaTeX Table ──")
    print(latex)


if __name__ == "__main__":
    main()
