"""
IRT 2PL+gamma data preparation: build per-item binary response matrices
from eval_results.json files for seed=42 aligned checkpoints.
"""

import csv
import json
import os
import re
import sys
from pathlib import Path

EVAL_DIR = "/root/autodl-tmp/exp001/eval_results"
MMLU_CACHE = "/root/autodl-tmp/.hf_cache"
OUTPUT_DIR = "/root/contamcal-irt-calibration/analysis/irt_data"
SEED = 42
BENCHMARKS = ["mmlu", "gsm8k", "arc_challenge", "humaneval"]

DEPRECATED_DIRS = {
    "Qwen2.5-3B_d000_s42", "Qwen2.5-3B_d000_v2_s42",
    "Qwen2.5-3B_d005_s42", "Qwen2.5-3B_d025_s42", "Qwen2.5-3B_d100_s42",
}

DOSAGE_RE = re.compile(
    r"_d(\d+)(?:_(?:v\d+|a(\d+)))?_s(\d+)(?:_a(\d+))?(_para)?(_aligned)?(?:_v\d+)?$"
)

MMLU_DOMAINS = {
    "abstract_algebra": "STEM", "anatomy": "STEM", "astronomy": "STEM",
    "college_biology": "STEM", "college_chemistry": "STEM",
    "college_computer_science": "STEM", "college_mathematics": "STEM",
    "college_physics": "STEM", "computer_security": "STEM",
    "conceptual_physics": "STEM", "electrical_engineering": "STEM",
    "elementary_mathematics": "STEM", "high_school_biology": "STEM",
    "high_school_chemistry": "STEM", "high_school_computer_science": "STEM",
    "high_school_mathematics": "STEM", "high_school_physics": "STEM",
    "high_school_statistics": "STEM", "machine_learning": "STEM",
    "formal_logic": "Humanities", "high_school_european_history": "Humanities",
    "high_school_us_history": "Humanities", "high_school_world_history": "Humanities",
    "international_law": "Humanities", "jurisprudence": "Humanities",
    "logical_fallacies": "Humanities", "moral_disputes": "Humanities",
    "moral_scenarios": "Humanities", "philosophy": "Humanities",
    "prehistory": "Humanities", "professional_law": "Humanities",
    "world_religions": "Humanities",
    "econometrics": "Social Sciences", "high_school_geography": "Social Sciences",
    "high_school_government_and_politics": "Social Sciences",
    "high_school_macroeconomics": "Social Sciences",
    "high_school_microeconomics": "Social Sciences",
    "high_school_psychology": "Social Sciences",
    "human_sexuality": "Social Sciences", "professional_psychology": "Social Sciences",
    "public_relations": "Social Sciences", "security_studies": "Social Sciences",
    "sociology": "Social Sciences", "us_foreign_policy": "Social Sciences",
    "business_ethics": "Other", "clinical_knowledge": "Other",
    "college_medicine": "Other", "global_facts": "Other",
    "human_aging": "Other", "management": "Other", "marketing": "Other",
    "medical_genetics": "Other", "miscellaneous": "Other", "nutrition": "Other",
    "professional_accounting": "Other", "professional_medicine": "Other",
    "virology": "Other",
}


def parse_dir(dirname):
    m = DOSAGE_RE.search(dirname)
    if not m:
        return None
    clean = re.sub(r"_aligned$", "", dirname)
    if clean in DEPRECATED_DIRS:
        return None
    return {
        "dirname": dirname,
        "family": dirname[:m.start()],
        "dosage": int(m.group(1)),
        "seed": int(m.group(3)),
        "is_para": m.group(5) is not None,
        "is_aligned": m.group(6) is not None,
        "has_alpha": m.group(2) is not None or m.group(4) is not None,
    }


def discover_respondents(eval_dir, seed=42):
    entries = []
    for name in sorted(os.listdir(eval_dir)):
        p = Path(eval_dir) / name
        if not p.is_dir() or not (p / "eval_results.json").exists():
            continue
        info = parse_dir(name)
        if info is None or info["seed"] != seed:
            continue
        if not info["is_aligned"] or info["is_para"]:
            continue
        entries.append(info)

    seen = {}
    for e in entries:
        key = (e["family"], e["dosage"])
        if key not in seen:
            seen[key] = e
        elif e["has_alpha"] and not seen[key]["has_alpha"]:
            seen[key] = e

    return sorted(seen.values(), key=lambda x: (x["family"], x["dosage"]))


def build_response_matrix(eval_dir, respondents, benchmark):
    responses = []
    valid_resp = []
    for r in respondents:
        path = Path(eval_dir) / r["dirname"] / "eval_results.json"
        with open(path) as f:
            data = json.load(f)
        if benchmark not in data["benchmarks"]:
            continue
        per_item = data["benchmarks"][benchmark]["per_item"]
        responses.append([int(item["correct"]) for item in per_item])
        valid_resp.append(r)

    if not responses:
        return None, [], 0

    lengths = [len(r) for r in responses]
    n_items = lengths[0]
    if not all(l == n_items for l in lengths):
        print(f"  WARNING: item count mismatch: {set(lengths)}, truncating to min")
        n_items = min(lengths)
        responses = [r[:n_items] for r in responses]

    return responses, valid_resp, n_items


def get_mmlu_subjects(cache_dir):
    os.environ["HF_HUB_OFFLINE"] = "1"
    from datasets import load_dataset
    ds = load_dataset("cais/mmlu", "all", split="test", cache_dir=cache_dir)
    return [row["subject"] for row in ds]


def save_benchmark(bench, matrix, valid_resp, n_items, bench_dir):
    os.makedirs(bench_dir, exist_ok=True)
    n_resp = len(matrix)

    # response_matrix.csv
    with open(os.path.join(bench_dir, "response_matrix.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["respondent"] + [f"item_{j}" for j in range(n_items)])
        for i, r in enumerate(valid_resp):
            label = f"{r['family']}_d{r['dosage']:03d}_s{r['seed']}"
            w.writerow([label] + matrix[i])

    # exposure_scores.csv
    with open(os.path.join(bench_dir, "exposure_scores.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["respondent", "dosage", "exposure"])
        for r in valid_resp:
            label = f"{r['family']}_d{r['dosage']:03d}_s{r['seed']}"
            w.writerow([label, r["dosage"], f"{r['dosage']/100:.2f}"])

    # item_metadata.csv
    d000_idx = [i for i, r in enumerate(valid_resp) if r["dosage"] == 0]
    if d000_idx:
        baseline = [
            sum(matrix[i][j] for i in d000_idx) / len(d000_idx)
            for j in range(n_items)
        ]
    else:
        baseline = [0.0] * n_items

    with open(os.path.join(bench_dir, "item_metadata.csv"), "w", newline="") as f:
        w = csv.writer(f)
        if bench == "mmlu":
            subjects = get_mmlu_subjects(MMLU_CACHE)
            w.writerow(["item_id", "subject", "domain", "difficulty_baseline"])
            for j in range(n_items):
                subj = subjects[j] if j < len(subjects) else "unknown"
                domain = MMLU_DOMAINS.get(subj, "Other")
                w.writerow([j, subj, domain, f"{baseline[j]:.4f}"])
        else:
            w.writerow(["item_id", "difficulty_baseline"])
            for j in range(n_items):
                w.writerow([j, f"{baseline[j]:.4f}"])


def main():
    respondents = discover_respondents(EVAL_DIR, seed=SEED)
    print(f"Discovered {len(respondents)} respondents:")
    for r in respondents:
        print(f"  {r['family']}_d{r['dosage']:03d}_s{r['seed']}  <- {r['dirname']}")

    for bench in BENCHMARKS:
        print(f"\n{'='*60}")
        print(f"Benchmark: {bench}")

        matrix, valid_resp, n_items = build_response_matrix(
            EVAL_DIR, respondents, bench
        )
        if matrix is None:
            print("  No data")
            continue

        n_resp = len(matrix)
        total_correct = sum(sum(row) for row in matrix)
        total_cells = n_resp * n_items

        print(f"  Matrix: {n_resp} respondents x {n_items} items")
        print(f"  Overall accuracy: {total_correct/total_cells:.4f}")
        print(f"  Sparsity (frac 0): {1 - total_correct/total_cells:.4f}")

        for i, r in enumerate(valid_resp):
            acc = sum(matrix[i]) / n_items
            print(f"    {r['family']}_d{r['dosage']:03d}: {acc:.4f}")

        bench_dir = os.path.join(OUTPUT_DIR, bench)
        save_benchmark(bench, matrix, valid_resp, n_items, bench_dir)
        print(f"  Saved to {bench_dir}/")


if __name__ == "__main__":
    main()
