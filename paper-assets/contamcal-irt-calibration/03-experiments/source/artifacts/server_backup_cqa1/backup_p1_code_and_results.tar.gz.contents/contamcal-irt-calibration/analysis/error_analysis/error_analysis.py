"""
Systematic error analysis for contamcal-irt-calibration (seed=42 data).

Analyzes item-level response flips across dosage levels for 5 model families
on MMLU, ARC-Challenge, and HumanEval. Produces:
  - forgetting_by_domain.csv: items correct@d000 but wrong@d100, by domain
  - knowledge_gain_by_domain.csv: items wrong@d000 but correct@d100, by domain
  - persistent_errors.csv: items wrong at all dosages across all families
  - error_analysis_results.json: summary statistics
  - error_analysis_figures.pdf: visualizations

Input:  /root/autodl-tmp/exp001/eval_results/<checkpoint>/correctness_matrix.json
Output: /root/contamcal-irt-calibration/analysis/error_analysis/
"""

import json
import os
import csv
from collections import defaultdict, Counter
from pathlib import Path

import numpy as np

# ── Configuration ──

EVAL_DIR = Path("/root/autodl-tmp/exp001/eval_results")
OUTPUT_DIR = Path("/root/contamcal-irt-calibration/analysis/error_analysis")
HF_CACHE = "/root/autodl-tmp/.hf_cache"

FAMILIES = {
    "Qwen2.5-0.5B": {
        "d000": "Qwen2.5-0.5B_d000_s42_aligned",
        "d005": "Qwen2.5-0.5B_d005_s42_aligned",
        "d025": "Qwen2.5-0.5B_d025_s42_aligned",
        "d100": "Qwen2.5-0.5B_d100_s42_aligned",
    },
    "Qwen2.5-1.5B": {
        "d000": "Qwen2.5-1.5B_d000_s42_aligned",
        "d005": "Qwen2.5-1.5B_d005_s42_aligned",
        "d025": "Qwen2.5-1.5B_d025_s42_aligned",
        "d100": "Qwen2.5-1.5B_d100_s42_aligned",
    },
    "Qwen2.5-3B": {
        "d000": "Qwen2.5-3B_d000_s42_a32_aligned",
        "d005": "Qwen2.5-3B_d005_s42_a32_aligned",
        "d025": "Qwen2.5-3B_d025_v3_s42_aligned",
        "d100": "Qwen2.5-3B_d100_a32_s42_aligned",
    },
    "Qwen2.5-7B": {
        "d000": "Qwen2.5-7B_d000_s42_aligned",
        "d005": "Qwen2.5-7B_d005_s42_aligned",
        "d025": "Qwen2.5-7B_d025_s42_aligned",
        "d050": "Qwen2.5-7B_d050_s42_aligned",
        "d100": "Qwen2.5-7B_d100_s42_aligned",
    },
    "Llama-3.2-3B": {
        "d000": "Llama-3.2-3B_d000_s42_aligned",
        "d005": "Llama-3.2-3B_d005_s42_aligned",
        "d025": "Llama-3.2-3B_d025_s42_aligned",
        "d100": "Llama-3.2-3B_d100_s42_aligned",
    },
}

BENCHMARKS = ["mmlu", "arc_challenge", "humaneval", "gsm8k"]

# MMLU subject → broad category mapping
MMLU_CATEGORIES = {
    "STEM": [
        "abstract_algebra", "anatomy", "astronomy", "college_biology",
        "college_chemistry", "college_computer_science", "college_mathematics",
        "college_physics", "computer_security", "conceptual_physics",
        "electrical_engineering", "elementary_mathematics", "high_school_biology",
        "high_school_chemistry", "high_school_computer_science",
        "high_school_mathematics", "high_school_physics", "high_school_statistics",
        "machine_learning", "medical_genetics", "virology",
    ],
    "Humanities": [
        "formal_logic", "high_school_european_history",
        "high_school_us_history", "high_school_world_history", "international_law",
        "jurisprudence", "logical_fallacies", "moral_disputes", "moral_scenarios",
        "philosophy", "prehistory", "professional_law", "world_religions",
    ],
    "Social Sciences": [
        "econometrics", "high_school_geography", "high_school_government_and_politics",
        "high_school_macroeconomics", "high_school_microeconomics",
        "high_school_psychology", "human_sexuality", "professional_psychology",
        "public_relations", "security_studies", "sociology", "us_foreign_policy",
    ],
    "Other": [
        "business_ethics", "clinical_knowledge", "college_medicine",
        "global_facts", "human_aging", "management", "marketing",
        "miscellaneous", "nutrition", "professional_accounting",
        "professional_medicine",
    ],
}

SUBJECT_TO_CATEGORY = {}
for cat, subjects in MMLU_CATEGORIES.items():
    for s in subjects:
        SUBJECT_TO_CATEGORY[s] = cat


def load_correctness(family: str, dosage: str) -> dict:
    """Load correctness_matrix.json for a family/dosage checkpoint."""
    dirname = FAMILIES[family].get(dosage)
    if dirname is None:
        return None
    path = EVAL_DIR / dirname / "correctness_matrix.json"
    if not path.exists():
        print(f"  WARNING: missing {path}")
        return None
    with open(path) as f:
        return json.load(f)


def build_mmlu_subject_map():
    """Build index→subject mapping from cached cais/mmlu dataset."""
    try:
        from datasets import load_dataset
        ds = load_dataset("cais/mmlu", "all", split="test", cache_dir=HF_CACHE)
        return [row["subject"] for row in ds]
    except Exception as e:
        print(f"  WARNING: Could not load MMLU subjects from HF: {e}")
        print("  Falling back to benchmark-level analysis only.")
        return None


def analyze_forgetting_and_gain(all_data, mmlu_subjects):
    """Analyze items that flip between d000 and d100."""
    results = {}

    for family in FAMILIES:
        d000 = all_data.get((family, "d000"))
        d100 = all_data.get((family, "d100"))
        if d000 is None or d100 is None:
            print(f"  SKIP {family}: missing d000 or d100")
            continue

        family_result = {"forgetting": {}, "gain": {}}

        for bench in BENCHMARKS:
            if bench not in d000 or bench not in d100:
                continue
            arr_d000 = d000[bench]
            arr_d100 = d100[bench]
            n = min(len(arr_d000), len(arr_d100))

            forgot_indices = []
            gain_indices = []
            for i in range(n):
                if arr_d000[i] and not arr_d100[i]:
                    forgot_indices.append(i)
                elif not arr_d000[i] and arr_d100[i]:
                    gain_indices.append(i)

            # Domain breakdown for MMLU
            if bench == "mmlu" and mmlu_subjects is not None:
                forgot_domains = Counter(
                    SUBJECT_TO_CATEGORY.get(mmlu_subjects[i], "Unknown")
                    for i in forgot_indices if i < len(mmlu_subjects)
                )
                forgot_subjects = Counter(
                    mmlu_subjects[i] for i in forgot_indices if i < len(mmlu_subjects)
                )
                gain_domains = Counter(
                    SUBJECT_TO_CATEGORY.get(mmlu_subjects[i], "Unknown")
                    for i in gain_indices if i < len(mmlu_subjects)
                )
                gain_subjects = Counter(
                    mmlu_subjects[i] for i in gain_indices if i < len(mmlu_subjects)
                )
            else:
                forgot_domains = Counter()
                forgot_subjects = Counter()
                gain_domains = Counter()
                gain_subjects = Counter()

            family_result["forgetting"][bench] = {
                "count": len(forgot_indices),
                "total": n,
                "rate": len(forgot_indices) / n if n > 0 else 0,
                "indices": forgot_indices,
                "domain_distribution": dict(forgot_domains),
                "top_subjects": dict(forgot_subjects.most_common(10)),
            }
            family_result["gain"][bench] = {
                "count": len(gain_indices),
                "total": n,
                "rate": len(gain_indices) / n if n > 0 else 0,
                "indices": gain_indices,
                "domain_distribution": dict(gain_domains),
                "top_subjects": dict(gain_subjects.most_common(10)),
            }

        results[family] = family_result
    return results


def analyze_persistent_errors(all_data, mmlu_subjects):
    """Find items wrong at ALL dosages across ALL families."""
    # Collect per-benchmark sets of always-wrong items per family
    family_always_wrong = {}
    for family in FAMILIES:
        dosages = list(FAMILIES[family].keys())
        bench_sets = {}
        for bench in BENCHMARKS:
            wrong_sets = []
            for dose in dosages:
                data = all_data.get((family, dose))
                if data is None or bench not in data:
                    continue
                arr = data[bench]
                wrong = set(i for i, v in enumerate(arr) if not v)
                wrong_sets.append(wrong)
            if wrong_sets:
                bench_sets[bench] = set.intersection(*wrong_sets)
        family_always_wrong[family] = bench_sets

    # Items wrong across ALL families at ALL their dosages
    persistent = {}
    for bench in BENCHMARKS:
        per_family_sets = []
        for family in FAMILIES:
            if bench in family_always_wrong.get(family, {}):
                per_family_sets.append(family_always_wrong[family][bench])
        if per_family_sets:
            cross_family = set.intersection(*per_family_sets)
            # Domain breakdown for MMLU
            if bench == "mmlu" and mmlu_subjects is not None:
                domain_dist = Counter(
                    SUBJECT_TO_CATEGORY.get(mmlu_subjects[i], "Unknown")
                    for i in cross_family if i < len(mmlu_subjects)
                )
                subject_dist = Counter(
                    mmlu_subjects[i] for i in cross_family if i < len(mmlu_subjects)
                )
            else:
                domain_dist = {}
                subject_dist = {}
            persistent[bench] = {
                "count": len(cross_family),
                "indices": sorted(cross_family),
                "domain_distribution": dict(domain_dist),
                "top_subjects": dict(Counter(subject_dist).most_common(15)),
            }

    # Also per-family persistent errors
    per_family = {}
    for family in FAMILIES:
        per_family[family] = {}
        for bench in BENCHMARKS:
            if bench in family_always_wrong.get(family, {}):
                items = family_always_wrong[family][bench]
                per_family[family][bench] = {
                    "count": len(items),
                    "indices": sorted(items),
                }
    return persistent, per_family


def analyze_cross_model_agreement(all_data, mmlu_subjects):
    """Analyze which items flip consistently across families at each dosage."""
    results = {}
    dosages_common = ["d005", "d025", "d100"]

    for dose in dosages_common:
        dose_result = {}
        for bench in BENCHMARKS:
            # For each item, count how many families flip (d000→dose)
            # Get all families that have both d000 and this dose
            families_with_data = []
            for family in FAMILIES:
                d000 = all_data.get((family, "d000"))
                d_dose = all_data.get((family, dose))
                if d000 and d_dose and bench in d000 and bench in d_dose:
                    families_with_data.append(family)

            if len(families_with_data) < 2:
                continue

            # Find the min item count across all relevant checkpoints
            n = min(
                len(all_data[(f, "d000")][bench])
                for f in families_with_data
            )
            n = min(n, min(
                len(all_data[(f, dose)][bench])
                for f in families_with_data
            ))

            # Count flips per item
            forgot_counts = defaultdict(int)  # item → how many families forgot
            gain_counts = defaultdict(int)
            for family in families_with_data:
                d000_arr = all_data[(family, "d000")][bench]
                dose_arr = all_data[(family, dose)][bench]
                for i in range(n):
                    if d000_arr[i] and not dose_arr[i]:
                        forgot_counts[i] += 1
                    elif not d000_arr[i] and dose_arr[i]:
                        gain_counts[i] += 1

            nf = len(families_with_data)
            # Unanimous forgetting: all families forgot
            unanimous_forgot = [i for i, c in forgot_counts.items() if c == nf]
            # Majority forgetting: >50% families forgot
            majority_forgot = [i for i, c in forgot_counts.items() if c > nf / 2]
            unanimous_gain = [i for i, c in gain_counts.items() if c == nf]
            majority_gain = [i for i, c in gain_counts.items() if c > nf / 2]

            # Model-specific flips: only 1 family flipped
            unique_forgot = [i for i, c in forgot_counts.items() if c == 1]
            unique_gain = [i for i, c in gain_counts.items() if c == 1]

            dose_result[bench] = {
                "n_families": nf,
                "n_items": n,
                "unanimous_forgot": len(unanimous_forgot),
                "majority_forgot": len(majority_forgot),
                "any_forgot": len(forgot_counts),
                "unique_forgot": len(unique_forgot),
                "unanimous_gain": len(unanimous_gain),
                "majority_gain": len(majority_gain),
                "any_gain": len(gain_counts),
                "unique_gain": len(unique_gain),
            }

            # Domain breakdown for unanimous flips (MMLU)
            if bench == "mmlu" and mmlu_subjects is not None:
                dose_result[bench]["unanimous_forgot_domains"] = dict(Counter(
                    SUBJECT_TO_CATEGORY.get(mmlu_subjects[i], "Unknown")
                    for i in unanimous_forgot if i < len(mmlu_subjects)
                ))
                dose_result[bench]["unanimous_gain_domains"] = dict(Counter(
                    SUBJECT_TO_CATEGORY.get(mmlu_subjects[i], "Unknown")
                    for i in unanimous_gain if i < len(mmlu_subjects)
                ))

        results[dose] = dose_result
    return results


def analyze_dosage_trajectory(all_data, mmlu_subjects):
    """Analyze per-family accuracy trajectory and item-level patterns across dosages."""
    trajectories = {}
    for family in FAMILIES:
        dosages = sorted(FAMILIES[family].keys(), key=lambda d: int(d[1:]))
        family_traj = {}
        for bench in BENCHMARKS:
            bench_traj = {}
            for dose in dosages:
                data = all_data.get((family, dose))
                if data and bench in data:
                    arr = data[bench]
                    bench_traj[dose] = {
                        "accuracy": sum(arr) / len(arr) if arr else 0,
                        "correct": sum(arr),
                        "total": len(arr),
                    }
            family_traj[bench] = bench_traj
        trajectories[family] = family_traj
    return trajectories


def write_forgetting_csv(fg_results, mmlu_subjects, output_path):
    """Write forgetting analysis to CSV."""
    rows = []
    for family, data in fg_results.items():
        for bench, stats in data["forgetting"].items():
            if bench == "mmlu" and mmlu_subjects:
                for domain, count in sorted(stats["domain_distribution"].items()):
                    rows.append({
                        "family": family,
                        "benchmark": bench,
                        "domain": domain,
                        "forgot_count": count,
                        "forgot_rate": stats["rate"],
                        "total_items": stats["total"],
                    })
            else:
                rows.append({
                    "family": family,
                    "benchmark": bench,
                    "domain": bench,
                    "forgot_count": stats["count"],
                    "forgot_rate": stats["rate"],
                    "total_items": stats["total"],
                })
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["family", "benchmark", "domain",
                                                "forgot_count", "forgot_rate", "total_items"])
        writer.writeheader()
        writer.writerows(rows)


def write_gain_csv(fg_results, mmlu_subjects, output_path):
    """Write knowledge gain analysis to CSV."""
    rows = []
    for family, data in fg_results.items():
        for bench, stats in data["gain"].items():
            if bench == "mmlu" and mmlu_subjects:
                for domain, count in sorted(stats["domain_distribution"].items()):
                    rows.append({
                        "family": family,
                        "benchmark": bench,
                        "domain": domain,
                        "gain_count": count,
                        "gain_rate": stats["rate"],
                        "total_items": stats["total"],
                    })
            else:
                rows.append({
                    "family": family,
                    "benchmark": bench,
                    "domain": bench,
                    "gain_count": stats["count"],
                    "gain_rate": stats["rate"],
                    "total_items": stats["total"],
                })
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["family", "benchmark", "domain",
                                                "gain_count", "gain_rate", "total_items"])
        writer.writeheader()
        writer.writerows(rows)


def write_persistent_csv(persistent, output_path, mmlu_subjects):
    """Write persistent errors to CSV."""
    rows = []
    for bench, data in persistent.items():
        if bench == "mmlu" and mmlu_subjects:
            for idx in data["indices"]:
                subj = mmlu_subjects[idx] if idx < len(mmlu_subjects) else "unknown"
                cat = SUBJECT_TO_CATEGORY.get(subj, "Unknown")
                rows.append({
                    "benchmark": bench,
                    "item_index": idx,
                    "subject": subj,
                    "category": cat,
                })
        else:
            for idx in data["indices"]:
                rows.append({
                    "benchmark": bench,
                    "item_index": idx,
                    "subject": "",
                    "category": bench,
                })
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["benchmark", "item_index", "subject", "category"])
        writer.writeheader()
        writer.writerows(rows)


def make_figures(fg_results, persistent, cross_model, trajectories, mmlu_subjects):
    """Generate visualization PDF."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_pdf import PdfPages
    except ImportError:
        print("  matplotlib not available, skipping figures")
        return

    pdf_path = OUTPUT_DIR / "error_analysis_figures.pdf"
    with PdfPages(str(pdf_path)) as pdf:

        # ── Fig 1: Forgetting & Gain rates by family (MMLU) ──
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))
        families_list = list(fg_results.keys())
        forget_rates = [fg_results[f]["forgetting"].get("mmlu", {}).get("rate", 0) for f in families_list]
        gain_rates = [fg_results[f]["gain"].get("mmlu", {}).get("rate", 0) for f in families_list]

        x = np.arange(len(families_list))
        axes[0].bar(x, forget_rates, color="#e74c3c", alpha=0.8)
        axes[0].set_xticks(x)
        axes[0].set_xticklabels(families_list, rotation=30, ha="right", fontsize=9)
        axes[0].set_ylabel("Forgetting Rate")
        axes[0].set_title("MMLU: Forgetting Rate (d000→d100)")
        axes[0].set_ylim(0, max(forget_rates) * 1.3 if max(forget_rates) > 0 else 0.1)

        axes[1].bar(x, gain_rates, color="#27ae60", alpha=0.8)
        axes[1].set_xticks(x)
        axes[1].set_xticklabels(families_list, rotation=30, ha="right", fontsize=9)
        axes[1].set_ylabel("Knowledge Gain Rate")
        axes[1].set_title("MMLU: Knowledge Gain Rate (d000→d100)")
        axes[1].set_ylim(0, max(gain_rates) * 1.3 if max(gain_rates) > 0 else 0.1)

        plt.tight_layout()
        pdf.savefig(fig)
        plt.close()

        # ── Fig 2: Forgetting by domain (MMLU) ──
        categories = ["STEM", "Humanities", "Social Sciences", "Other"]
        fig, ax = plt.subplots(figsize=(12, 6))
        bar_width = 0.15
        x = np.arange(len(categories))
        for i, family in enumerate(families_list):
            fdata = fg_results[family]["forgetting"].get("mmlu", {})
            domain_dist = fdata.get("domain_distribution", {})
            vals = [domain_dist.get(cat, 0) for cat in categories]
            ax.bar(x + i * bar_width, vals, bar_width, label=family, alpha=0.85)
        ax.set_xticks(x + bar_width * (len(families_list) - 1) / 2)
        ax.set_xticklabels(categories)
        ax.set_ylabel("Number of Forgotten Items")
        ax.set_title("MMLU Forgetting by Domain (d000→d100)")
        ax.legend(fontsize=8)
        plt.tight_layout()
        pdf.savefig(fig)
        plt.close()

        # ── Fig 3: Knowledge gain by domain (MMLU) ──
        fig, ax = plt.subplots(figsize=(12, 6))
        for i, family in enumerate(families_list):
            gdata = fg_results[family]["gain"].get("mmlu", {})
            domain_dist = gdata.get("domain_distribution", {})
            vals = [domain_dist.get(cat, 0) for cat in categories]
            ax.bar(x + i * bar_width, vals, bar_width, label=family, alpha=0.85)
        ax.set_xticks(x + bar_width * (len(families_list) - 1) / 2)
        ax.set_xticklabels(categories)
        ax.set_ylabel("Number of Gained Items")
        ax.set_title("MMLU Knowledge Gain by Domain (d000→d100)")
        ax.legend(fontsize=8)
        plt.tight_layout()
        pdf.savefig(fig)
        plt.close()

        # ── Fig 4: Accuracy trajectory across dosages (MMLU) ──
        fig, ax = plt.subplots(figsize=(10, 6))
        colors = ["#e74c3c", "#3498db", "#2ecc71", "#9b59b6", "#f39c12"]
        for i, family in enumerate(families_list):
            traj = trajectories.get(family, {}).get("mmlu", {})
            doses = sorted(traj.keys(), key=lambda d: int(d[1:]))
            dose_vals = [int(d[1:]) for d in doses]
            acc_vals = [traj[d]["accuracy"] for d in doses]
            ax.plot(dose_vals, acc_vals, "o-", label=family, color=colors[i % len(colors)], linewidth=2)
        ax.set_xlabel("Dosage (%)")
        ax.set_ylabel("Accuracy")
        ax.set_title("MMLU Accuracy Trajectory by Dosage")
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        pdf.savefig(fig)
        plt.close()

        # ── Fig 5: Cross-model agreement (d100 vs d000) ──
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        axes = axes.flatten()
        for idx, bench in enumerate(BENCHMARKS):
            cm = cross_model.get("d100", {}).get(bench, {})
            if not cm:
                axes[idx].text(0.5, 0.5, f"No data for {bench}", ha="center", va="center")
                axes[idx].set_title(bench)
                continue
            labels = ["Unanimous\nForgot", "Majority\nForgot", "Unique\nForgot",
                      "Unanimous\nGain", "Majority\nGain", "Unique\nGain"]
            vals = [cm.get("unanimous_forgot", 0), cm.get("majority_forgot", 0),
                    cm.get("unique_forgot", 0), cm.get("unanimous_gain", 0),
                    cm.get("majority_gain", 0), cm.get("unique_gain", 0)]
            bar_colors = ["#c0392b", "#e74c3c", "#f5b7b1", "#1e8449", "#27ae60", "#a9dfbf"]
            axes[idx].bar(range(len(labels)), vals, color=bar_colors, alpha=0.85)
            axes[idx].set_xticks(range(len(labels)))
            axes[idx].set_xticklabels(labels, fontsize=7, rotation=20, ha="right")
            axes[idx].set_title(f"{bench}: Cross-model Agreement (d100)")
            axes[idx].set_ylabel("# Items")
        plt.tight_layout()
        pdf.savefig(fig)
        plt.close()

        # ── Fig 6: Persistent errors domain distribution (MMLU) ──
        if "mmlu" in persistent and persistent["mmlu"]["domain_distribution"]:
            fig, ax = plt.subplots(figsize=(8, 5))
            domains = persistent["mmlu"]["domain_distribution"]
            labels = list(domains.keys())
            sizes = list(domains.values())
            colors_pie = ["#3498db", "#e74c3c", "#2ecc71", "#f39c12", "#9b59b6"]
            ax.pie(sizes, labels=labels, colors=colors_pie[:len(labels)],
                   autopct="%1.1f%%", startangle=90)
            ax.set_title(f"Persistent MMLU Errors by Domain (n={persistent['mmlu']['count']})")
            plt.tight_layout()
            pdf.savefig(fig)
            plt.close()

        # ── Fig 7: Net effect (gain - forgetting) per family per benchmark ──
        fig, ax = plt.subplots(figsize=(12, 5))
        bar_width = 0.15
        x = np.arange(len(BENCHMARKS))
        for i, family in enumerate(families_list):
            net_vals = []
            for bench in BENCHMARKS:
                gain_n = fg_results[family]["gain"].get(bench, {}).get("count", 0)
                forgot_n = fg_results[family]["forgetting"].get(bench, {}).get("count", 0)
                net_vals.append(gain_n - forgot_n)
            ax.bar(x + i * bar_width, net_vals, bar_width, label=family, alpha=0.85)
        ax.set_xticks(x + bar_width * (len(families_list) - 1) / 2)
        ax.set_xticklabels(BENCHMARKS)
        ax.axhline(y=0, color="black", linewidth=0.5)
        ax.set_ylabel("Net Items (Gain − Forgetting)")
        ax.set_title("Net Effect of d100 Contamination (Gain − Forgetting)")
        ax.legend(fontsize=8)
        plt.tight_layout()
        pdf.savefig(fig)
        plt.close()

    print(f"  Figures saved to {pdf_path}")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ── Step 1: Load all correctness matrices ──
    print("Loading correctness matrices...")
    all_data = {}
    for family, doses in FAMILIES.items():
        for dose, dirname in doses.items():
            data = load_correctness(family, dose)
            if data is not None:
                all_data[(family, dose)] = data
                benchmarks_loaded = list(data.keys())
                n_items = {k: len(v) for k, v in data.items()}
                print(f"  {family}/{dose}: {n_items}")
    print(f"  Loaded {len(all_data)} checkpoints total.\n")

    # ── Step 2: Build MMLU subject mapping ──
    print("Building MMLU subject index...")
    mmlu_subjects = build_mmlu_subject_map()
    if mmlu_subjects:
        print(f"  {len(mmlu_subjects)} MMLU items mapped to subjects.\n")

    # ── Step 3: Forgetting & Gain analysis ──
    print("Analyzing forgetting and knowledge gain (d000 → d100)...")
    fg_results = analyze_forgetting_and_gain(all_data, mmlu_subjects)
    for family, data in fg_results.items():
        for bench in BENCHMARKS:
            f_stats = data["forgetting"].get(bench, {})
            g_stats = data["gain"].get(bench, {})
            if f_stats or g_stats:
                print(f"  {family}/{bench}: forgot={f_stats.get('count',0)}, "
                      f"gained={g_stats.get('count',0)}, "
                      f"net={g_stats.get('count',0) - f_stats.get('count',0)}")
    print()

    # ── Step 4: Persistent errors ──
    print("Analyzing persistent errors (wrong everywhere)...")
    persistent, per_family_persistent = analyze_persistent_errors(all_data, mmlu_subjects)
    for bench, data in persistent.items():
        print(f"  {bench}: {data['count']} items wrong across ALL families at ALL dosages")
    print()

    # ── Step 5: Cross-model agreement ──
    print("Analyzing cross-model agreement...")
    cross_model = analyze_cross_model_agreement(all_data, mmlu_subjects)
    for dose, data in cross_model.items():
        for bench, stats in data.items():
            print(f"  {dose}/{bench}: unanimous_forgot={stats.get('unanimous_forgot',0)}, "
                  f"unanimous_gain={stats.get('unanimous_gain',0)}, "
                  f"unique_forgot={stats.get('unique_forgot',0)}, "
                  f"unique_gain={stats.get('unique_gain',0)}")
    print()

    # ── Step 6: Dosage trajectories ──
    print("Computing accuracy trajectories...")
    trajectories = analyze_dosage_trajectory(all_data, mmlu_subjects)

    # ── Step 7: Write outputs ──
    print("Writing outputs...")

    # CSV files
    write_forgetting_csv(fg_results, mmlu_subjects,
                         OUTPUT_DIR / "forgetting_by_domain.csv")
    write_gain_csv(fg_results, mmlu_subjects,
                   OUTPUT_DIR / "knowledge_gain_by_domain.csv")
    write_persistent_csv(persistent, OUTPUT_DIR / "persistent_errors.csv", mmlu_subjects)

    # JSON summary
    # Strip index lists for JSON (too large) — keep counts only
    fg_summary = {}
    for family, data in fg_results.items():
        fg_summary[family] = {}
        for direction in ["forgetting", "gain"]:
            fg_summary[family][direction] = {}
            for bench, stats in data[direction].items():
                fg_summary[family][direction][bench] = {
                    k: v for k, v in stats.items() if k != "indices"
                }

    persistent_summary = {}
    for bench, data in persistent.items():
        persistent_summary[bench] = {
            "count": data["count"],
            "domain_distribution": data.get("domain_distribution", {}),
            "top_subjects": data.get("top_subjects", {}),
        }

    per_family_persistent_summary = {}
    for family, fdata in per_family_persistent.items():
        per_family_persistent_summary[family] = {
            bench: {"count": d["count"]} for bench, d in fdata.items()
        }

    summary = {
        "metadata": {
            "seed": 42,
            "families": list(FAMILIES.keys()),
            "benchmarks": BENCHMARKS,
            "n_checkpoints_loaded": len(all_data),
        },
        "forgetting_and_gain": fg_summary,
        "persistent_errors": persistent_summary,
        "per_family_persistent_errors": per_family_persistent_summary,
        "cross_model_agreement": cross_model,
        "trajectories": trajectories,
    }

    with open(OUTPUT_DIR / "error_analysis_results.json", "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    # Figures
    try:
        make_figures(fg_results, persistent, cross_model, trajectories, mmlu_subjects)
    except Exception as e:
        print(f"  WARNING: Figure generation failed: {e}")

    print(f"\nAll outputs written to {OUTPUT_DIR}/")
    print("Files:")
    for p in sorted(OUTPUT_DIR.iterdir()):
        if p.is_file():
            size = p.stat().st_size
            print(f"  {p.name} ({size:,} bytes)")


if __name__ == "__main__":
    main()
