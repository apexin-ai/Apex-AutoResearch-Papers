#!/usr/bin/env python3
"""
analyze_cf_fallback.py — CF Fallback experiment analysis

Compares S1 (no fallback) vs S1 + CF fallback across 4 model-dataset configs.
Runs violation checkers, generates comparison tables, Pareto plots, and budget analysis.

Input:
  - CF fallback JSONL outputs: outputs/w1_cf_fallback_{scierc_pilot,docred,llama_scierc,llama_docred}.jsonl
  - Optional: fallback stats JSON: outputs/w1_cf_fallback_*_fallback_stats.json

Output:
  - Markdown comparison table (stdout + outputs/cf_analysis/comparison_table.md)
  - DR vs CF Pareto scatter plot (outputs/cf_analysis/dr_vs_cf_pareto.pdf + .png)
  - Violation budget analysis (stdout + outputs/cf_analysis/violation_budget.md)

Dependencies:
  - violation_checker.py (SciERC checker)
  - violation_checker_docred.py (DocRED checker)
  - matplotlib

Usage:
  python3 analyze_cf_fallback.py --results_dir outputs/ --output_dir outputs/cf_analysis/
"""

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


# ── Experiment configuration ──────────────────────────────────────────────────

EXPERIMENTS = [
    {
        "key": "qwen_scierc",
        "file": "w1_cf_fallback_scierc_pilot.jsonl",
        "dataset": "SciERC",
        "model": "Qwen",
        "checker": "scierc",
        "label": "Qwen SciERC",
    },
    {
        "key": "qwen_docred",
        "file": "w1_cf_fallback_docred.jsonl",
        "dataset": "DocRED",
        "model": "Qwen",
        "checker": "docred",
        "label": "Qwen DocRED",
    },
    {
        "key": "llama_scierc",
        "file": "w1_cf_fallback_llama_scierc.jsonl",
        "dataset": "SciERC",
        "model": "Llama",
        "checker": "scierc",
        "label": "Llama SciERC",
    },
    {
        "key": "llama_docred",
        "file": "w1_cf_fallback_llama_docred.jsonl",
        "dataset": "DocRED",
        "model": "Llama",
        "checker": "docred",
        "label": "Llama DocRED",
    },
]

# Baseline: S1 without fallback (from registry)
BASELINES = {
    "qwen_scierc":  {"DR": 0.93, "CF": 9.90, "R-F1": 8.36},
    "qwen_docred":  {"DR": 10.21, "CF": 2.57, "R-F1": 8.23},
    "llama_scierc": {"DR": 0.08, "CF": 6.56, "R-F1": 2.54},
    "llama_docred": {"DR": 2.55, "CF": 12.02, "R-F1": 6.27},
}


# ── Violation checking ────────────────────────────────────────────────────────

def run_checker(input_path, checker_type, scierc_checker, docred_checker,
                project_root, output_path):
    """Run the appropriate violation checker via subprocess, return parsed report dict."""
    if checker_type == "scierc":
        checker_script = scierc_checker
        constraints_path = os.path.join(project_root, "ontology_constraints.json")
    else:
        checker_script = docred_checker
        constraints_path = os.path.join(project_root, "data", "docred",
                                        "ontology_constraints_docred.json")

    if not os.path.exists(constraints_path):
        print(f"  [ERROR] Constraints file not found: {constraints_path}")
        return None

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    cmd = [
        sys.executable, checker_script,
        "--input_path", str(input_path),
        "--constraints_path", str(constraints_path),
        "--output_path", str(output_path),
    ]
    print(f"  Running: {os.path.basename(checker_script)} on {os.path.basename(input_path)}")
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=300)

    if result.returncode != 0:
        print(f"  [ERROR] Checker failed (rc={result.returncode})")
        if result.stderr:
            print(f"  stderr: {result.stderr[:500]}")
        return None

    with open(output_path) as f:
        return json.load(f)


def extract_metrics(report, checker_type):
    """Extract violation rates and F1 from checker report. All values in %.

    DocRED checker does not include F1 — R-F1 and E-F1 will be None.
    """
    s = report.get("summary", {})
    metrics = {
        "DR": s.get("domain_range_violation_rate", 0) * 100,
        "CF": s.get("cross_field_consistency_violation_rate", 0) * 100,
        "RV": s.get("relation_vocabulary_violation_rate", 0) * 100,
        "ET": s.get("entity_type_violation_rate", 0) * 100,
        "total_triples": s.get("total_triples_extracted", 0),
        "total_entities": s.get("total_entities_extracted",
                                s.get("total_entities", 0)),
        "parse_failures": s.get("json_parse_failures",
                                s.get("parse_failures", 0)),
    }

    quality = report.get("quality", {})
    if quality:
        metrics["R-F1"] = quality.get("relation_f1", {}).get("f1", 0) * 100
        metrics["E-F1"] = quality.get("entity_f1", {}).get("f1", 0) * 100
    else:
        metrics["R-F1"] = None
        metrics["E-F1"] = None

    return metrics


def compute_f1_from_jsonl(jsonl_path):
    """Compute relation and entity micro-F1 directly from JSONL records.

    Fallback for DocRED, whose checker doesn't output F1.
    Matching: case-insensitive, stripped text. Relations keyed by (head, tail, type).
    """
    rel_tp = rel_gold_total = rel_pred_total = 0
    ent_tp = ent_gold_total = ent_pred_total = 0

    def rel_key(r):
        return (r.get("head", "").lower().strip(),
                r.get("tail", "").lower().strip(),
                r.get("type", ""))

    def ent_key(e):
        return (e.get("text", "").lower().strip(),
                e.get("type", ""))

    with open(jsonl_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            parsed = rec.get("parsed_output")
            if not parsed:
                continue

            gold_rels = set(rel_key(r) for r in rec.get("gold_relations", []))
            pred_rels = set(rel_key(r) for r in parsed.get("relations", []))
            rel_tp += len(gold_rels & pred_rels)
            rel_gold_total += len(gold_rels)
            rel_pred_total += len(pred_rels)

            gold_ents = set(ent_key(e) for e in rec.get("gold_entities", []))
            pred_ents = set(ent_key(e) for e in parsed.get("entities", []))
            ent_tp += len(gold_ents & pred_ents)
            ent_gold_total += len(gold_ents)
            ent_pred_total += len(pred_ents)

    def micro_f1(tp, gold, pred):
        p = tp / pred if pred else 0
        r = tp / gold if gold else 0
        return 2 * p * r / (p + r) if (p + r) else 0

    return {
        "R-F1": micro_f1(rel_tp, rel_gold_total, rel_pred_total) * 100,
        "E-F1": micro_f1(ent_tp, ent_gold_total, ent_pred_total) * 100,
    }


# ── Comparison table ──────────────────────────────────────────────────────────

def generate_comparison_table(results):
    """Generate markdown table: CF fallback vs no-fallback baselines."""
    header = "| 配置 | Mode | DR (%) | CF (%) | RV (%) | ET (%) | R-F1 (%) | E-F1 (%) | ΔDR | ΔCF |"
    sep    = "|------|------|--------|--------|--------|--------|----------|----------|-----|-----|"
    rows = [header, sep]

    for exp in EXPERIMENTS:
        key = exp["key"]
        label = exp["label"]
        bl = BASELINES[key]

        rows.append(
            f"| {label} | S1 (no fb) "
            f"| {bl['DR']:.2f} | {bl['CF']:.2f} | — | — "
            f"| {bl['R-F1']:.2f} | — | — | — |"
        )

        fb = results.get(key)
        if fb:
            delta_dr = fb["DR"] - bl["DR"]
            delta_cf = fb["CF"] - bl["CF"]
            rf1_str = f"{fb['R-F1']:.2f}" if fb.get("R-F1") is not None else "—"
            ef1_str = f"{fb['E-F1']:.2f}" if fb.get("E-F1") is not None else "—"
            rows.append(
                f"| {label} | S1 + CF fb "
                f"| {fb['DR']:.2f} | {fb['CF']:.2f} "
                f"| {fb['RV']:.2f} | {fb['ET']:.2f} "
                f"| {rf1_str} | {ef1_str} "
                f"| {delta_dr:+.2f} | {delta_cf:+.2f} |"
            )
        else:
            rows.append(
                f"| {label} | S1 + CF fb | — | — | — | — | — | — | — | — |"
            )

    return "\n".join(rows)


# ── Pareto plot ───────────────────────────────────────────────────────────────

def plot_pareto(results, output_dir):
    """DR vs CF scatter plot with arrows from no-fallback to fallback."""
    fig, ax = plt.subplots(figsize=(8, 6))

    dataset_colors = {"SciERC": "#2563eb", "DocRED": "#dc2626"}

    for exp in EXPERIMENTS:
        key = exp["key"]
        label = exp["label"]
        bl = BASELINES[key]
        color = dataset_colors[exp["dataset"]]

        ax.scatter(bl["CF"], bl["DR"], c=color, marker="o", s=100, zorder=5,
                   edgecolors="black", linewidths=0.5)
        ax.annotate(f"{label}\n(no fb)", (bl["CF"], bl["DR"]),
                    textcoords="offset points", xytext=(10, 8), fontsize=7,
                    color=color)

        fb = results.get(key)
        if fb:
            ax.scatter(fb["CF"], fb["DR"], c=color, marker="^", s=100, zorder=5,
                       edgecolors="black", linewidths=0.5)
            ax.annotate(f"{label}\n(+fb)", (fb["CF"], fb["DR"]),
                        textcoords="offset points", xytext=(10, -12), fontsize=7,
                        color=color)
            # Arrow: no-fallback → fallback
            ax.annotate(
                "", xy=(fb["CF"], fb["DR"]), xytext=(bl["CF"], bl["DR"]),
                arrowprops=dict(arrowstyle="->", color=color, lw=1.5,
                                linestyle="--", alpha=0.7),
            )

    handles = [
        mpatches.Patch(color="#2563eb", label="SciERC"),
        mpatches.Patch(color="#dc2626", label="DocRED"),
        plt.Line2D([], [], color="gray", marker="o", linestyle="None",
                   markersize=8, label="S1 (no fallback)"),
        plt.Line2D([], [], color="gray", marker="^", linestyle="None",
                   markersize=8, label="S1 + CF fallback"),
    ]
    ax.legend(handles=handles, loc="upper right", fontsize=9)

    ax.set_xlabel("CF Violation Rate (%)", fontsize=11)
    ax.set_ylabel("DR Violation Rate (%)", fontsize=11)
    ax.set_title("DR vs CF: Effect of CF Fallback", fontsize=13, fontweight="bold")
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    for ext in ("pdf", "png"):
        path = os.path.join(output_dir, f"dr_vs_cf_pareto.{ext}")
        fig.savefig(path, dpi=150, bbox_inches="tight")
        print(f"  Saved: {path}")
    plt.close(fig)


# ── Fallback stats ────────────────────────────────────────────────────────────

def analyze_fallback_stats(results_dir):
    """Read *_fallback_stats.json and summarize trigger rates."""
    print("\n" + "=" * 60)
    print("FALLBACK TRIGGER RATES")
    print("=" * 60)

    found_any = False
    stats_data = {}

    for exp in EXPERIMENTS:
        stats_file = os.path.join(
            results_dir,
            exp["file"].replace(".jsonl", "_fallback_stats.json"),
        )
        if not os.path.exists(stats_file):
            continue

        found_any = True
        with open(stats_file) as f:
            stats = json.load(f)

        stats_data[exp["key"]] = stats
        print(f"\n{exp['label']}  ({os.path.basename(stats_file)}):")

        for k in ("grammar_first_fallback_rate", "cf_registry_fallback_rate",
                   "total_samples", "fallback_triggered", "fallback_rate"):
            if k in stats:
                v = stats[k]
                if isinstance(v, float):
                    print(f"  {k}: {v:.4f}")
                else:
                    print(f"  {k}: {v}")

        # Any additional numeric fields
        shown = {"grammar_first_fallback_rate", "cf_registry_fallback_rate",
                 "total_samples", "fallback_triggered", "fallback_rate"}
        for k, v in sorted(stats.items()):
            if k not in shown and isinstance(v, (int, float)):
                print(f"  {k}: {v}")

    if not found_any:
        print("  No fallback stats files found yet.")

    return stats_data


# ── Violation budget ──────────────────────────────────────────────────────────

def analyze_violation_budget(results):
    """Compute total violation budget = DR + CF, compare with/without fallback."""
    print("\n" + "=" * 60)
    print("VIOLATION BUDGET ANALYSIS  (budget = DR + CF)")
    print("=" * 60)

    header = "| 配置 | Budget (no fb) | Budget (+fb) | ΔBudget | Result |"
    sep    = "|------|----------------|--------------|---------|--------|"
    rows = [header, sep]

    for exp in EXPERIMENTS:
        key = exp["key"]
        bl = BASELINES[key]
        budget_bl = bl["DR"] + bl["CF"]

        fb = results.get(key)
        if fb:
            budget_fb = fb["DR"] + fb["CF"]
            delta = budget_fb - budget_bl
            if delta < -0.5:
                result = "reduced"
            elif delta > 0.5:
                result = "increased"
            else:
                result = "neutral"
            rows.append(
                f"| {exp['label']} | {budget_bl:.2f} | {budget_fb:.2f} "
                f"| {delta:+.2f} | {result} |"
            )
        else:
            rows.append(
                f"| {exp['label']} | {budget_bl:.2f} | — | — | (pending) |"
            )

    table = "\n".join(rows)
    print(table)
    return table


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Analyze CF fallback experiment results vs no-fallback baselines.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
Examples:
  # Full analysis (after all experiments finish)
  python3 analyze_cf_fallback.py --results_dir outputs/ --output_dir outputs/cf_analysis/

  # Partial analysis (skips missing files)
  python3 analyze_cf_fallback.py

  # Custom checker paths
  python3 analyze_cf_fallback.py --scierc_checker violation_checker.py \\
                                 --docred_checker violation_checker_docred.py
""",
    )
    parser.add_argument("--results_dir", type=str, default="outputs/",
                        help="Directory with experiment JSONL files (default: outputs/)")
    parser.add_argument("--output_dir", type=str, default="outputs/cf_analysis/",
                        help="Directory for analysis outputs (default: outputs/cf_analysis/)")
    parser.add_argument("--scierc_checker", type=str, default="violation_checker.py",
                        help="Path to SciERC violation checker script")
    parser.add_argument("--docred_checker", type=str, default="violation_checker_docred.py",
                        help="Path to DocRED violation checker script")
    parser.add_argument("--project_root", type=str, default=".",
                        help="Project root for locating constraint files (default: .)")
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    results = {}

    # ── 1. Run violation checkers on each experiment ──
    print("=" * 60)
    print("RUNNING VIOLATION CHECKERS")
    print("=" * 60)

    for exp in EXPERIMENTS:
        key = exp["key"]
        input_path = os.path.join(args.results_dir, exp["file"])

        if not os.path.exists(input_path):
            print(f"\n[SKIP] {exp['label']}: {input_path} not found")
            continue

        print(f"\n[CHECK] {exp['label']}")
        report_path = os.path.join(args.output_dir,
                                   f"violation_report_cf_fb_{key}.json")
        report = run_checker(
            input_path, exp["checker"],
            args.scierc_checker, args.docred_checker,
            args.project_root, report_path,
        )
        if report is None:
            continue

        metrics = extract_metrics(report, exp["checker"])

        # DocRED checker doesn't include F1 — compute from JSONL
        if metrics["R-F1"] is None:
            print(f"  Computing F1 from JSONL...")
            f1_data = compute_f1_from_jsonl(input_path)
            metrics["R-F1"] = f1_data["R-F1"]
            metrics["E-F1"] = f1_data["E-F1"]

        results[key] = metrics
        print(f"  DR={metrics['DR']:.2f}%  CF={metrics['CF']:.2f}%  "
              f"R-F1={metrics['R-F1']:.2f}%  E-F1={metrics['E-F1']:.2f}%")

    # ── 2. Comparison table ──
    print("\n" + "=" * 60)
    print("COMPARISON TABLE")
    print("=" * 60)

    table = generate_comparison_table(results)
    print(table)

    table_path = os.path.join(args.output_dir, "comparison_table.md")
    with open(table_path, "w") as f:
        f.write("# CF Fallback vs No-Fallback Comparison\n\n")
        f.write(table + "\n")
    print(f"\nSaved: {table_path}")

    # ── 3. Pareto plot ──
    print("\n" + "=" * 60)
    print("GENERATING PARETO PLOT")
    print("=" * 60)

    plot_pareto(results, args.output_dir)

    # ── 4. Fallback trigger stats ──
    analyze_fallback_stats(args.results_dir)

    # ── 5. Violation budget ──
    budget_table = analyze_violation_budget(results)

    budget_path = os.path.join(args.output_dir, "violation_budget.md")
    with open(budget_path, "w") as f:
        f.write("# Violation Budget Analysis\n\n")
        f.write(budget_table + "\n")
    print(f"\nSaved: {budget_path}")

    # ── Summary ──
    print("\n" + "=" * 60)
    print(f"DONE: {len(results)}/{len(EXPERIMENTS)} configs analyzed")
    if len(results) < len(EXPERIMENTS):
        missing = [e["label"] for e in EXPERIMENTS if e["key"] not in results]
        print(f"Pending: {', '.join(missing)}")
    print("=" * 60)


if __name__ == "__main__":
    main()
