#!/usr/bin/env python3
"""Verify item ordering alignment between PSN-IRT combine.csv and Open LLM Leaderboard v1."""

import os
import csv
import json
import sys
import numpy as np

os.environ["HF_HUB_DISABLE_XET"] = "1"

from datasets import load_dataset

PROJECT = "/home/ubuntu/.agent-ml-research-be-idea-gen-0519-3/projects/irt_personfit_contam"
COMBINE_CSV = f"{PROJECT}/artifacts/psn_irt_phase_b/combine.csv"
OUT_DIR = f"{PROJECT}/artifacts/item_alignment_check"

# PSN-IRT model list (row index -> model)
PSN_MODELS = {
    0: "360GPT2-Pro", 1: "DeepSeek-V3", 2: "Doubao-pro", 3: "Gemini-1.5",
    4: "Gemma-2B-it", 5: "Hunyuan-Turbo", 6: "Mistral-7B-Instruct-v0.1",
    7: "Moonshot-v1", 8: "Qwen-Plus", 9: "Qwen2.5-3B-Instruct",
    10: "Vicuna-7B-v1.3", 11: "Yi-Lightning"
}

# Benchmark column ranges in combine.csv
BENCH_RANGES = {
    "arc_c": (0, 295),
    "bbh": (295, 6806),
    "chinese_simpleqa": (6806, 9806),
    "gpqa_diamond": (9806, 10004),
    "gsm8k": (10004, 11323),
    "hellaswag": (11323, 21365),
    "humaneval": (21365, 21529),
    "math": (21529, 26529),
    "mbpp": (26529, 27029),
    "mmlu": (27029, 41071),
    "theoremqa": (41071, 41871),
}

# v1 leaderboard dataset names for target models
V1_DATASETS = {
    "Mistral-7B-Instruct-v0.1": "open-llm-leaderboard-old/details_mistralai__Mistral-7B-Instruct-v0.1",
    "Vicuna-7B-v1.3": "open-llm-leaderboard-old/details_lmsys__vicuna-7b-v1.3",
    "Gemma-2B-it": "open-llm-leaderboard-old/details_google__gemma-2b-it",
}

# MMLU 57 subtasks
MMLU_SUBTASKS = [
    "abstract_algebra", "anatomy", "astronomy", "business_ethics", "clinical_knowledge",
    "college_biology", "college_chemistry", "college_computer_science", "college_mathematics",
    "college_medicine", "college_physics", "computer_security", "conceptual_physics",
    "econometrics", "electrical_engineering", "elementary_mathematics", "formal_logic",
    "global_facts", "high_school_biology", "high_school_chemistry", "high_school_computer_science",
    "high_school_european_history", "high_school_geography", "high_school_government_and_politics",
    "high_school_macroeconomics", "high_school_mathematics", "high_school_microeconomics",
    "high_school_physics", "high_school_psychology", "high_school_statistics",
    "high_school_us_history", "high_school_world_history", "human_aging", "human_sexuality",
    "international_law", "jurisprudence", "logical_fallacies", "machine_learning",
    "management", "marketing", "medical_genetics", "miscellaneous", "moral_disputes",
    "moral_scenarios", "nutrition", "philosophy", "prehistory", "professional_accounting",
    "professional_law", "professional_medicine", "professional_psychology", "public_relations",
    "security_studies", "sociology", "us_foreign_policy", "virology", "world_religions",
]


def load_combine_csv():
    """Load PSN-IRT combine.csv as numpy array."""
    rows = []
    with open(COMBINE_CSV, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append([float(x) for x in row])
    data = np.array(rows)
    print(f"combine.csv shape: {data.shape}")
    return data


def extract_psn_mmlu(combine_data, model_row):
    """Extract MMLU responses for a model from combine.csv."""
    start, end = BENCH_RANGES["mmlu"]
    return combine_data[model_row, start:end]


def load_v1_mmlu(dataset_name):
    """Load MMLU responses from v1 leaderboard for a model."""
    print(f"\nLoading v1 MMLU data from: {dataset_name}")

    # First, discover available configs
    from datasets import get_dataset_config_names
    try:
        configs = get_dataset_config_names(dataset_name)
    except Exception as e:
        print(f"  Error getting configs: {e}")
        return None, None

    mmlu_configs = sorted([c for c in configs if c.startswith("harness_hendrycksTest_")])
    print(f"  Found {len(mmlu_configs)} MMLU configs")

    all_responses = []
    subtask_info = []

    for config in mmlu_configs:
        subtask_name = config.replace("harness_hendrycksTest_", "").replace("_5", "")
        try:
            ds = load_dataset(dataset_name, config, split="latest")
            # Extract binary accuracy
            if "acc" in ds.column_names:
                accs = ds["acc"]
            elif "metrics" in ds.column_names:
                accs = [row.get("acc", None) for row in ds["metrics"]]
            else:
                print(f"  WARNING: No acc field in {config}, columns: {ds.column_names}")
                # Try to find the accuracy field
                for col in ds.column_names:
                    print(f"    {col}: {ds[col][:3]}")
                continue

            n_items = len(accs)
            all_responses.extend(accs)
            subtask_info.append({
                "config": config,
                "subtask": subtask_name,
                "n_items": n_items,
                "start_idx": len(all_responses) - n_items,
            })
            print(f"  {config}: {n_items} items")
        except Exception as e:
            print(f"  Error loading {config}: {e}")

    responses = np.array(all_responses, dtype=float)
    print(f"  Total v1 MMLU items: {len(responses)}")
    return responses, subtask_info


def load_v1_mmlu_alternative(dataset_name):
    """Alternative: try loading without subtask splitting, look at data structure."""
    from datasets import get_dataset_config_names
    configs = get_dataset_config_names(dataset_name)
    mmlu_configs = sorted([c for c in configs if "hendrycksTest" in c or "mmlu" in c.lower()])

    print(f"\nAll MMLU-related configs ({len(mmlu_configs)}):")
    for c in mmlu_configs[:5]:
        print(f"  {c}")
    if len(mmlu_configs) > 5:
        print(f"  ... and {len(mmlu_configs) - 5} more")

    # Load first config to inspect structure
    if mmlu_configs:
        ds = load_dataset(dataset_name, mmlu_configs[0], split="latest")
        print(f"\nSample config '{mmlu_configs[0]}':")
        print(f"  Columns: {ds.column_names}")
        print(f"  Num rows: {len(ds)}")
        if len(ds) > 0:
            print(f"  First row: {ds[0]}")

    return mmlu_configs


def compare_responses(psn_vec, v1_vec, label=""):
    """Compare two binary response vectors."""
    min_len = min(len(psn_vec), len(v1_vec))
    psn = psn_vec[:min_len]
    v1 = v1_vec[:min_len]

    match = np.sum(psn == v1)
    match_rate = match / min_len if min_len > 0 else 0

    result = {
        "label": label,
        "psn_len": len(psn_vec),
        "v1_len": len(v1_vec),
        "compared": min_len,
        "matches": int(match),
        "match_rate": float(match_rate),
        "mismatches": int(min_len - match),
    }

    print(f"\n{'='*60}")
    print(f"Comparison: {label}")
    print(f"  PSN-IRT items: {len(psn_vec)}, v1 items: {len(v1_vec)}")
    print(f"  Compared: {min_len}")
    print(f"  Match rate: {match_rate:.4f} ({match}/{min_len})")

    if match_rate < 0.99 and min_len > 0:
        # Analyze mismatch pattern
        diffs = np.where(psn != v1)[0]
        print(f"  First 20 mismatch positions: {diffs[:20].tolist()}")

        # Check if it's a block-shift pattern
        if len(diffs) > 100:
            gaps = np.diff(diffs)
            print(f"  Mismatch gap stats: mean={gaps.mean():.1f}, median={np.median(gaps):.1f}")

    return result


def try_subtask_reorder(psn_mmlu, v1_responses, v1_subtask_info):
    """Try different subtask orderings to find best alignment."""
    from itertools import permutations

    n_subtasks = len(v1_subtask_info)
    print(f"\nTrying subtask reordering ({n_subtasks} subtasks)...")

    # Build subtask response blocks from v1
    v1_blocks = []
    for info in v1_subtask_info:
        start = info["start_idx"]
        end = start + info["n_items"]
        v1_blocks.append(v1_responses[start:end])

    # First: check if sorted-by-name order matches PSN-IRT
    # (PSN-IRT likely uses alphabetical subtask order from lm-eval-harness)
    sorted_indices = list(range(n_subtasks))  # already sorted alphabetically
    sorted_concat = np.concatenate([v1_blocks[i] for i in sorted_indices])
    match = np.sum(psn_mmlu[:len(sorted_concat)] == sorted_concat)
    rate = match / len(sorted_concat) if len(sorted_concat) > 0 else 0
    print(f"  Alphabetical order match: {rate:.4f}")

    if rate > 0.99:
        return "alphabetical", rate, sorted_indices

    # Try to find best single-subtask alignment
    print("\n  Per-subtask alignment scan:")
    best_matches = []
    psn_offset = 0
    for i, info in enumerate(v1_subtask_info):
        n = info["n_items"]
        block = v1_blocks[i]

        # Slide this block across PSN MMLU to find best position
        best_pos = -1
        best_rate = 0
        for pos in range(0, len(psn_mmlu) - n + 1, 1):
            r = np.mean(psn_mmlu[pos:pos+n] == block)
            if r > best_rate:
                best_rate = r
                best_pos = pos

        best_matches.append({
            "subtask": info["subtask"],
            "n_items": n,
            "best_pos": best_pos,
            "best_rate": float(best_rate),
        })
        if best_rate > 0.8:
            print(f"    {info['subtask']}: best match at pos {best_pos} ({best_rate:.4f})")

    return best_matches, None, None


def main():
    print("=" * 60)
    print("PSN-IRT vs v1 Leaderboard Item Alignment Check")
    print("=" * 60)

    # Load combine.csv
    combine = load_combine_csv()

    results = {"models": {}, "summary": {}}

    # Primary model: Mistral-7B-Instruct-v0.1 (row 6)
    for model_name, psn_row in [("Mistral-7B-Instruct-v0.1", 6), ("Vicuna-7B-v1.3", 10)]:
        print(f"\n{'#'*60}")
        print(f"# Model: {model_name} (PSN row {psn_row})")
        print(f"{'#'*60}")

        dataset_name = V1_DATASETS.get(model_name)
        if not dataset_name:
            print(f"  No v1 dataset mapping for {model_name}")
            continue

        # Extract PSN MMLU
        psn_mmlu = extract_psn_mmlu(combine, psn_row)
        print(f"PSN-IRT MMLU vector: {len(psn_mmlu)} items, mean acc: {psn_mmlu.mean():.4f}")

        # Load v1 MMLU
        v1_responses, subtask_info = load_v1_mmlu(dataset_name)

        if v1_responses is None:
            # Try alternative loading
            print("Primary loading failed, trying alternative...")
            load_v1_mmlu_alternative(dataset_name)
            continue

        # Direct comparison
        direct_result = compare_responses(psn_mmlu, v1_responses, f"{model_name} - direct order")

        model_results = {
            "direct_comparison": direct_result,
        }

        # If direct comparison is poor, try reordering
        if direct_result["match_rate"] < 0.95 and subtask_info:
            reorder_result = try_subtask_reorder(psn_mmlu, v1_responses, subtask_info)
            model_results["reorder_analysis"] = str(reorder_result[0]) if reorder_result else None

        results["models"][model_name] = model_results

    # Summary
    match_rates = [r["direct_comparison"]["match_rate"] for r in results["models"].values() if "direct_comparison" in r]
    if match_rates:
        results["summary"] = {
            "n_models_checked": len(match_rates),
            "avg_match_rate": float(np.mean(match_rates)),
            "all_aligned": all(r > 0.99 for r in match_rates),
            "conclusion": "aligned" if all(r > 0.99 for r in match_rates) else
                         "partially_aligned" if any(r > 0.90 for r in match_rates) else "not_aligned",
        }

    # Save results
    out_path = f"{OUT_DIR}/alignment_results.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\nResults saved to {out_path}")

    return results


if __name__ == "__main__":
    results = main()
