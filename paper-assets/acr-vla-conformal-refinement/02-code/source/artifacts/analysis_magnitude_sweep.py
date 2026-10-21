#!/usr/bin/env python3
"""Magnitude sweep analysis: norm sensitivity curve for perdof vs obs_only on spatial benchmark."""

import json
import os
import re
import sys

import yaml
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

# ── paths ──────────────────────────────────────────────────────────────
REGISTRY = os.path.join(os.path.dirname(__file__), "..", "registry.yaml")
OUT_DIR = os.path.join(os.path.dirname(__file__), "figures")
os.makedirs(OUT_DIR, exist_ok=True)

# ── experiment ID patterns ─────────────────────────────────────────────
# Magnitude sweep experiments follow: eval-mag-{method}-norm{nnn}
MAG_PERDOF_PREFIX = "eval-mag-perdof-norm"
MAG_OBSONLY_PREFIX = "eval-mag-obsonly-norm"

# Also include norm=0.1 baseline runs (original spatial evals)
PERDOF_NORM01 = "eval-acr-spatial-v4-small"      # perdof, norm=0.1 (7/10 partial)
PERDOF_NORM01_R2 = "eval-acr-spatial-v4-small-r2" # restart tasks 8-10
OBSONLY_NORM01 = "eval-acr-spatial-v4-obs-only-r2" # obs_only, norm=0.1
OBSONLY_NORM01_R3 = "eval-acr-spatial-v4-obs-only-r3" # restart

# Baselines
RECONVLA_ARGMIN = "eval-reconvla-spatial-v3"  # 34%
VLA_ONLY = "eval-spatial-v7-full"              # 30%
VLA_MEAN = "eval-vla-mean-spatial"             # 32%


def load_registry():
    with open(REGISTRY) as f:
        return yaml.safe_load(f)


def normalize_sr(val):
    """Normalize success rate to 0-1 scale, handling mixed registry formats.

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


def extract_overall_sr(exp):
    """Extract overall success rate from experiment metrics, handling inconsistent field names."""
    m = exp.get("metrics", {})
    if not m:
        return None

    for key in ("overall_success_rate", "overall_sr", "overall_success_rate_10tasks",
                "overall_SR", "avg_SR_10task", "overall_sr_10task"):
        if key in m:
            return normalize_sr(m[key])

    # Try computing from per_task
    per_task = m.get("per_task", {})
    if per_task and len(per_task) == 10:
        return sum(normalize_sr(v) for v in per_task.values()) / len(per_task)

    return None


def extract_partial_sr(exp):
    """Extract SR from partial results (in-progress experiments)."""
    m = exp.get("metrics", {})
    if not m:
        return None, 0

    partial = m.get("partial_results", {})
    if partial:
        successes = 0
        trials = 0
        for v in partial.values():
            match = re.search(r"\((\d+)/(\d+)\)", str(v))
            if match:
                successes += int(match.group(1))
                trials += int(match.group(2))
        if trials > 0:
            return successes / trials, len(partial)
        return None, 0

    per_task_partial = m.get("per_task_partial", {})
    if per_task_partial:
        normalized = [normalize_sr(v) for v in per_task_partial.values()]
        return sum(normalized) / len(normalized), len(per_task_partial)

    # Try running_avg fields
    for key, val in m.items():
        if key.startswith("running_avg"):
            match = re.search(r"([\d.]+)%", str(val))
            if match:
                return float(match.group(1)) / 100.0, int(re.search(r"(\d+)tasks?", key).group(1)) if re.search(r"(\d+)tasks?", key) else 0
    return None, 0


def parse_norm_from_id(exp_id, prefix):
    """Parse norm value from experiment ID.

    Convention: digits after 'norm' represent the fractional part.
    "003"->0.03, "005"->0.05, "02"->0.2, "03"->0.3, "01"->0.1
    """
    suffix = exp_id[len(prefix):]
    norm_part = suffix.split("-")[0]

    if not norm_part:
        return None

    if "p" in norm_part:
        try:
            return float(norm_part.replace("p", "."))
        except ValueError:
            return None

    if not norm_part.isdigit():
        return None

    # Insert decimal point: "003"->"0.03", "02"->"0.2", "3"->"0.3"
    if norm_part.startswith("0") and len(norm_part) >= 2:
        return float("0." + norm_part[1:])
    else:
        return float("0." + norm_part)


def merge_partial_results(exps, base_id, restart_ids):
    """Merge base + restart partial results into combined SR."""
    all_results = {}

    for eid in [base_id] + restart_ids:
        if eid not in exps:
            continue
        m = exps[eid].get("metrics", {})

        # From per_task (completed)
        for k, v in m.get("per_task", {}).items():
            short = k.replace("pick_up_black_bowl_", "")
            all_results[short] = normalize_sr(v)

        # From partial_results
        for k, v in m.get("partial_results", {}).items():
            short = k.replace("pick_up_black_bowl_", "")
            match = re.search(r"([\d.]+)%", str(v))
            if match:
                all_results[short] = normalize_sr(match.group(1))

        # From per_task_partial
        for k, v in m.get("per_task_partial", {}).items():
            short = k.replace("pick_up_black_bowl_", "")
            all_results[short] = normalize_sr(v)

    if all_results:
        return sum(all_results.values()) / len(all_results), len(all_results), all_results
    return None, 0, {}


def _is_benchmark(exp_id, exp, benchmark):
    """Check if experiment belongs to the given benchmark (spatial/object)."""
    if benchmark == "object":
        return "object" in exp_id.lower()
    # spatial: no "object" in ID
    return "object" not in exp_id.lower()


def collect_sweep_data(exps, benchmark="spatial"):
    """Collect norm -> SR data for perdof and obs_only methods, filtered by benchmark."""
    perdof_data = {}
    obsonly_data = {}

    for eid, exp in exps.items():
        if exp.get("status") not in ("RUNNING", "DONE"):
            continue
        if exp.get("conclusion") in ("killed", "failed"):
            continue

        if eid.startswith(MAG_PERDOF_PREFIX):
            if not _is_benchmark(eid, exp, benchmark):
                continue
            norm = parse_norm_from_id(eid, MAG_PERDOF_PREFIX)
            if norm is None:
                continue
            sr = extract_overall_sr(exp)
            if sr is None:
                sr, n = extract_partial_sr(exp)
            if sr is not None:
                existing = perdof_data.get(norm)
                if existing is None or exp.get("status") == "DONE":
                    perdof_data[norm] = {"sr": sr, "exp_id": eid, "status": exp.get("status")}

        elif eid.startswith(MAG_OBSONLY_PREFIX):
            if not _is_benchmark(eid, exp, benchmark):
                continue
            norm = parse_norm_from_id(eid, MAG_OBSONLY_PREFIX)
            if norm is None:
                continue
            sr = extract_overall_sr(exp)
            if sr is None:
                sr, n = extract_partial_sr(exp)
            if sr is not None:
                existing = obsonly_data.get(norm)
                if existing is None or exp.get("status") == "DONE":
                    obsonly_data[norm] = {"sr": sr, "exp_id": eid, "status": exp.get("status")}

    # Add norm=0.1 from original evals (spatial only — object norm=0.1 comes from mag experiments)
    if benchmark == "spatial":
        # Prefer final overall_sr from restart experiment (avoids per_task key mismatch during merge)
        sr_perdof_01 = None
        n_perdof = 0
        for eid in [PERDOF_NORM01_R2, PERDOF_NORM01]:
            if eid in exps and exps[eid].get("conclusion") == "success":
                sr_perdof_01 = extract_overall_sr(exps[eid])
                if sr_perdof_01 is not None:
                    n_perdof = 10
                    break
        if sr_perdof_01 is None:
            sr_perdof_01, n_perdof, _ = merge_partial_results(exps, PERDOF_NORM01, [PERDOF_NORM01_R2])
        if sr_perdof_01 is not None:
            perdof_data[0.1] = {"sr": sr_perdof_01, "exp_id": f"{PERDOF_NORM01}+restart", "status": "DONE", "n_tasks": n_perdof}

        sr_obsonly_01 = None
        n_obsonly = 0
        for eid in [OBSONLY_NORM01_R3, OBSONLY_NORM01]:
            if eid in exps and exps[eid].get("conclusion") == "success":
                sr_obsonly_01 = extract_overall_sr(exps[eid])
                if sr_obsonly_01 is not None:
                    n_obsonly = 10
                    break
        if sr_obsonly_01 is None:
            sr_obsonly_01, n_obsonly, _ = merge_partial_results(exps, OBSONLY_NORM01, [OBSONLY_NORM01_R3])
        if sr_obsonly_01 is not None:
            obsonly_data[0.1] = {"sr": sr_obsonly_01, "exp_id": f"{OBSONLY_NORM01}+restart", "status": "DONE", "n_tasks": n_obsonly}

    return perdof_data, obsonly_data


def plot_sensitivity_curve(perdof_data, obsonly_data, baselines, benchmark="spatial"):
    """Generate norm sensitivity curve plot."""
    # ── style ──────────────────────────────────────────────────────────
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman", "DejaVu Serif"],
        "font.size": 11,
        "axes.labelsize": 13,
        "axes.titlesize": 14,
        "legend.fontsize": 10,
        "xtick.labelsize": 11,
        "ytick.labelsize": 11,
        "axes.linewidth": 0.8,
        "lines.linewidth": 2.0,
        "lines.markersize": 8,
        "figure.dpi": 150,
    })

    colors = {
        "perdof": "#2E86AB",      # steel blue
        "obs_only": "#A23B72",    # raspberry
        "argmin": "#555555",      # dark gray
        "vla_only": "#999999",    # light gray
        "vla_mean": "#BBBBBB",    # lighter gray
    }

    fig, ax = plt.subplots(figsize=(6.5, 4.5))

    # Plot perdof
    if perdof_data:
        norms = sorted(perdof_data.keys())
        srs = [perdof_data[n]["sr"] * 100 for n in norms]
        markers = ["o" if perdof_data[n].get("status") == "DONE" or perdof_data[n].get("n_tasks", 10) == 10
                   else "^" for n in norms]
        ax.plot(norms, srs, "-o", color=colors["perdof"], label="ACR per-DOF", zorder=5)
        # Mark partial results with open markers
        for i, n in enumerate(norms):
            status = perdof_data[n].get("status")
            n_tasks = perdof_data[n].get("n_tasks", 10)
            if status == "RUNNING" or (n_tasks is not None and n_tasks < 10):
                ax.plot(n, srs[i], "^", color=colors["perdof"], markerfacecolor="white",
                       markeredgewidth=2, markersize=9, zorder=6)

    # Plot obs_only
    if obsonly_data:
        norms = sorted(obsonly_data.keys())
        srs = [obsonly_data[n]["sr"] * 100 for n in norms]
        ax.plot(norms, srs, "-s", color=colors["obs_only"], label="ACR obs-only", zorder=5)
        for i, n in enumerate(norms):
            status = obsonly_data[n].get("status")
            n_tasks = obsonly_data[n].get("n_tasks", 10)
            if status == "RUNNING" or (n_tasks is not None and n_tasks < 10):
                ax.plot(n, srs[i], "D", color=colors["obs_only"], markerfacecolor="white",
                       markeredgewidth=2, markersize=9, zorder=6)

    # Baseline horizontal lines
    xmin, xmax = 0.02, 0.35
    if baselines.get("argmin") is not None:
        ax.axhline(baselines["argmin"] * 100, color=colors["argmin"], ls="--", lw=1.5,
                   label=f"ReconVLA argmin ({baselines['argmin']*100:.0f}%)", zorder=3)
    if baselines.get("vla_mean") is not None:
        ax.axhline(baselines["vla_mean"] * 100, color=colors["vla_mean"], ls=":", lw=1.5,
                   label=f"VLA mean ({baselines['vla_mean']*100:.0f}%)", zorder=2)
    if baselines.get("vla_only") is not None:
        ax.axhline(baselines["vla_only"] * 100, color=colors["vla_only"], ls="-.", lw=1.0,
                   label=f"VLA-only ({baselines['vla_only']*100:.0f}%)", zorder=1)

    ax.set_xlabel("Correction Magnitude (max norm)")
    ax.set_ylabel("Success Rate (%)")
    ax.set_title(f"Norm Sensitivity: {benchmark.title()} Benchmark")
    ax.set_xscale("log")
    ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
    ax.xaxis.set_minor_formatter(mticker.NullFormatter())
    ax.set_xticks([0.03, 0.05, 0.1, 0.2, 0.3])
    ax.get_xaxis().set_major_formatter(mticker.FormatStrFormatter("%.2f"))
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(0, 65)
    ax.grid(True, alpha=0.3, ls="-", lw=0.5)
    ax.legend(loc="best", framealpha=0.9, edgecolor="gray")

    # Annotation for open markers
    ax.annotate("Open markers = partial (< 10 tasks)", xy=(0.98, 0.02),
                xycoords="axes fraction", ha="right", va="bottom",
                fontsize=8, color="gray", style="italic")

    fig.tight_layout()
    out_path = os.path.join(OUT_DIR, "magnitude_sweep_spatial.pdf")
    fig.savefig(out_path, bbox_inches="tight", dpi=300)
    print(f"Saved: {out_path}")

    # Also save PNG for quick preview
    png_path = out_path.replace(".pdf", ".png")
    fig.savefig(png_path, bbox_inches="tight", dpi=200)
    print(f"Saved: {png_path}")
    plt.close(fig)


def generate_summary_json(perdof_data, obsonly_data, baselines):
    """Generate JSON summary table."""
    summary = {
        "baselines": {k: v for k, v in baselines.items() if v is not None},
        "perdof": {},
        "obs_only": {},
    }

    argmin_sr = baselines.get("argmin", 0.34)

    for norm in sorted(set(list(perdof_data.keys()) + list(obsonly_data.keys()))):
        norm_str = f"{norm:.2f}"
        if norm in perdof_data:
            sr = perdof_data[norm]["sr"]
            summary["perdof"][norm_str] = {
                "sr": round(sr, 4),
                "sr_pct": f"{sr*100:.1f}%",
                "delta_vs_argmin": f"{(sr - argmin_sr)*100:+.1f}pp",
                "exp_id": perdof_data[norm]["exp_id"],
                "status": perdof_data[norm].get("status", "UNKNOWN"),
            }
        if norm in obsonly_data:
            sr = obsonly_data[norm]["sr"]
            summary["obs_only"][norm_str] = {
                "sr": round(sr, 4),
                "sr_pct": f"{sr*100:.1f}%",
                "delta_vs_argmin": f"{(sr - argmin_sr)*100:+.1f}pp",
                "exp_id": obsonly_data[norm]["exp_id"],
                "status": obsonly_data[norm].get("status", "UNKNOWN"),
            }

    out_path = os.path.join(OUT_DIR, "magnitude_sweep_summary.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"Saved: {out_path}")
    return summary


def main():
    benchmark = sys.argv[1] if len(sys.argv) > 1 else "spatial"
    data = load_registry()
    exps = data.get("experiments", {})

    # Collect baseline SRs
    baselines = {}
    for bid, bname in [(RECONVLA_ARGMIN, "argmin"), (VLA_ONLY, "vla_only"), (VLA_MEAN, "vla_mean")]:
        if bid in exps:
            baselines[bname] = extract_overall_sr(exps[bid])

    perdof_data, obsonly_data = collect_sweep_data(exps, benchmark=benchmark)

    # Print status
    print("=" * 60)
    print("MAGNITUDE SWEEP ANALYSIS")
    print("=" * 60)
    print(f"\nBaselines: {', '.join(f'{k}={v*100:.0f}%' for k, v in baselines.items() if v)}")
    print(f"\nPer-DOF data points: {len(perdof_data)}")
    for n in sorted(perdof_data.keys()):
        d = perdof_data[n]
        print(f"  norm={n:.2f}: SR={d['sr']*100:.1f}%  [{d.get('status', '?')}]  ({d['exp_id']})")
    print(f"\nObs-only data points: {len(obsonly_data)}")
    for n in sorted(obsonly_data.keys()):
        d = obsonly_data[n]
        print(f"  norm={n:.2f}: SR={d['sr']*100:.1f}%  [{d.get('status', '?')}]  ({d['exp_id']})")

    if not perdof_data and not obsonly_data:
        print("\n⚠ No magnitude sweep results available yet. Experiments are still RUNNING.")
        print("Re-run this script once experiments have metrics.")
        # Still generate empty JSON
        generate_summary_json(perdof_data, obsonly_data, baselines)
        return

    plot_sensitivity_curve(perdof_data, obsonly_data, baselines)
    summary = generate_summary_json(perdof_data, obsonly_data, baselines)

    print("\n── Summary ──")
    for method in ["perdof", "obs_only"]:
        if summary[method]:
            best_norm = min(summary[method], key=lambda n: -summary[method][n]["sr"])
            print(f"  Best {method}: norm={best_norm}, SR={summary[method][best_norm]['sr_pct']}")


if __name__ == "__main__":
    main()
