"""Seed determinism sanity check for vLLM.

Verifies that vLLM seed control produces deterministic outputs under greedy
decoding and measures diversity under stochastic sampling.

Output: JSON report to ``results/sanity_check.json``.
"""

import argparse
import json
import re
from pathlib import Path

import numpy as np

from src.data.prompt_templates import ANSWER_MAP, format_prompt
from src.inference.vllm_runner import VLLMRunner

ANSWER_PATTERN = re.compile(r"^\s*([A-Da-d])\b")

N_REPEATS = 10
SEED = 42
N_ITEMS = 5
TEMPLATE_ID = 1
ORDERING = 1


def extract_answer(text: str) -> str | None:
    m = ANSWER_PATTERN.match(text)
    return m.group(1).upper() if m else None


def build_prompts(items: list[dict], few_shot: dict) -> list[str]:
    prompts = []
    for item in items:
        subject = item["subject"]
        examples = few_shot[subject][str(ORDERING)]
        prompts.append(
            format_prompt(
                template_id=TEMPLATE_ID,
                subject=subject,
                question=item["question"],
                choices=item["choices"],
                few_shot_examples=examples,
            )
        )
    return prompts


def run_sanity_check(
    model_name: str,
    gpu_id: int,
    output_path: str,
) -> dict:
    with open("data/mmlu_items.json") as f:
        all_items = json.load(f)
    with open("data/few_shot_examples.json") as f:
        few_shot = json.load(f)

    items = all_items[:N_ITEMS]
    prompts = build_prompts(items, few_shot)

    print(f"Loading {model_name} (bfloat16) on GPU {gpu_id} ...")
    runner = VLLMRunner(model_name, gpu_id, "bfloat16", SEED)

    # --- Greedy (T=0) ---
    print(f"Greedy test: {N_REPEATS} repeats × {N_ITEMS} items ...")
    greedy_results: dict[str, dict] = {}
    for item in items:
        greedy_results[item["item_id"]] = {"outputs": []}

    for _ in range(N_REPEATS):
        results = runner.generate(prompts, temperature=0.0, top_p=None, seed=SEED)
        for item, result in zip(items, results):
            greedy_results[item["item_id"]]["outputs"].append(result.generated_text)

    greedy_report = {}
    for item_id, data in greedy_results.items():
        unique = list(set(data["outputs"]))
        greedy_report[item_id] = {
            "unique_outputs": len(unique),
            "all_outputs": data["outputs"],
        }

    # --- Phase 1: Seed control (same seed, T=0.5 → expect identical) ---
    print(f"Phase 1 — seed control: {N_REPEATS}× same seed, T=0.5 ...")
    phase1_results: dict[str, dict] = {}
    for item in items:
        phase1_results[item["item_id"]] = {"outputs": [], "correct": []}

    for _ in range(N_REPEATS):
        results = runner.generate(prompts, temperature=0.5, top_p=0.9, seed=SEED)
        for item, result in zip(items, results):
            phase1_results[item["item_id"]]["outputs"].append(
                result.generated_text
            )
            predicted = extract_answer(result.generated_text)
            gold = ANSWER_MAP[item["answer_idx"]]
            phase1_results[item["item_id"]]["correct"].append(
                int(predicted == gold) if predicted else 0
            )

    phase1_report = {}
    for item_id, data in phase1_results.items():
        unique = list(set(data["outputs"]))
        phase1_report[item_id] = {
            "unique_outputs": len(unique),
            "outputs": data["outputs"],
        }

    # --- Phase 2: Sampling path (different seeds, T=0.5 → expect diversity) ---
    diff_seeds = list(range(SEED, SEED + N_REPEATS))
    print(f"Phase 2 — sampling path: seeds {diff_seeds}, T=0.5 ...")
    phase2_results: dict[str, dict] = {}
    for item in items:
        phase2_results[item["item_id"]] = {"outputs": [], "correct": []}

    for s in diff_seeds:
        results = runner.generate(prompts, temperature=0.5, top_p=0.9, seed=s)
        for item, result in zip(items, results):
            phase2_results[item["item_id"]]["outputs"].append(
                result.generated_text
            )
            predicted = extract_answer(result.generated_text)
            gold = ANSWER_MAP[item["answer_idx"]]
            phase2_results[item["item_id"]]["correct"].append(
                int(predicted == gold) if predicted else 0
            )

    phase2_report = {}
    for item_id, data in phase2_results.items():
        unique = list(set(data["outputs"]))
        acc_std = float(np.std(data["correct"]))
        phase2_report[item_id] = {
            "unique_outputs": len(unique),
            "outputs": data["outputs"],
            "accuracy_std": round(acc_std, 6),
        }

    # --- Summary ---
    all_greedy_unique = [v["unique_outputs"] for v in greedy_report.values()]
    all_p1_unique = [v["unique_outputs"] for v in phase1_report.values()]
    all_p2_unique = [v["unique_outputs"] for v in phase2_report.values()]

    phase1_pass = all(u == 1 for u in all_p1_unique)
    phase2_pass = any(u > 1 for u in all_p2_unique)

    report = {
        "greedy": greedy_report,
        "stochastic_same_seed": phase1_report,
        "stochastic_diff_seeds": phase2_report,
        "summary": {
            "greedy_deterministic": all(u == 1 for u in all_greedy_unique),
            "phase1_seed_control": phase1_pass,
            "phase2_sampling_diversity": round(
                sum(all_p2_unique) / len(all_p2_unique), 2
            ),
            "sanity_check_pass": all(u == 1 for u in all_greedy_unique)
                and phase1_pass and phase2_pass,
        },
    }

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

    s = report["summary"]
    print(f"\nGreedy deterministic: {s['greedy_deterministic']}")
    print(f"Phase 1 (same seed → identical): {s['phase1_seed_control']}")
    print(f"Phase 2 (diff seeds → diverse): avg {s['phase2_sampling_diversity']} unique")
    print(f"SANITY CHECK {'PASS' if s['sanity_check_pass'] else 'FAIL'}")
    print(f"→ {output_path}")

    del runner
    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="vLLM seed determinism sanity check")
    parser.add_argument(
        "--model", default="meta-llama/Llama-3.1-8B-Instruct"
    )
    parser.add_argument("--gpu-id", type=int, default=0)
    parser.add_argument("--output", default="results/sanity_check.json")
    args = parser.parse_args()
    run_sanity_check(args.model, args.gpu_id, args.output)
