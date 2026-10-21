#!/usr/bin/env python3
"""
Re-Repair Phase 0: Quick feasibility test with oracle labels.
No Docker verification — evaluates via diff similarity to gold patch.

Runs 10 instances × 1 mutation patch × 4 conditions × K=5 samples.
"""

import argparse
import difflib
import json
import logging
import os
import re
from collections import defaultdict
from pathlib import Path

import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

CONDITIONS = ["control", "cls-diag", "oracle-diag", "random-diag"]

SYSTEM_PROMPT = (
    "You are a software engineer. You are given a code patch that was intended "
    "to fix an issue but does not fully work. Your task is to produce a corrected "
    "patch. Output ONLY the corrected unified diff enclosed in ```diff ... ``` tags."
)

DIAGNOSTIC_TEMPLATE = (
    "## Test Diagnostic\n"
    "The current patch **fails** the following tests:\n{fail_list}\n\n"
    "The current patch **passes** the following tests:\n{pass_list}"
)


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    log.info(f"Saved {len(data)} records to {path}")


def extract_diff(text):
    """Extract unified diff from LLM response."""
    if "</think>" in text:
        text = text.split("</think>", 1)[-1]
    m = re.search(r"```diff\s*\n(.*?)```", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    m = re.search(r"```\s*\n(diff.*?)```", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    m = re.search(r"(diff --git.*)", text, re.DOTALL)
    if m:
        return m.group(1).strip()
    return text.strip()


def diff_similarity(generated, gold):
    """Compute normalized sequence similarity between two diffs."""
    if not generated or not gold:
        return 0.0
    return difflib.SequenceMatcher(None, generated, gold).ratio()


def format_diagnostic(per_test):
    """Format per-test results into diagnostic prompt section."""
    if not per_test:
        return ""
    fails = [t for t, passed in per_test.items() if not passed]
    passes = [t for t, passed in per_test.items() if passed]
    if not fails:
        return ""
    fail_list = "\n".join(f"- `{t}`" for t in fails)
    pass_list = "\n".join(f"- `{t}`" for t in passes) if passes else "*(none)*"
    return DIAGNOSTIC_TEMPLATE.format(fail_list=fail_list, pass_list=pass_list)


def build_prompt(item, condition, rng):
    """Build repair prompt messages for a given condition."""
    base = (
        f"## Issue Description\n{item['problem_statement']}\n\n"
        f"## Current (Incorrect) Patch\n```diff\n{item['mutation_patch']}\n```\n"
    )

    if condition == "control":
        diag = ""
    elif condition == "oracle-diag":
        diag = format_diagnostic(item["oracle_per_test"])
    elif condition == "cls-diag":
        # Phase 0: simulate CLS at ~84% accuracy by flipping 16% of oracle labels
        oracle = item["oracle_per_test"]
        simulated = {}
        for t, v in oracle.items():
            if rng.random() < 0.16:
                simulated[t] = not v
            else:
                simulated[t] = v
        diag = format_diagnostic(simulated)
    elif condition == "random-diag":
        all_tests = list(item["oracle_per_test"].keys())
        per_test = {t: bool(rng.random() > 0.5) for t in all_tests}
        diag = format_diagnostic(per_test)
    else:
        raise ValueError(f"Unknown condition: {condition}")

    user_content = base
    if diag:
        user_content += f"\n{diag}\n"
    user_content += (
        "\nPlease produce a corrected patch in unified diff format."
        "\nOutput ONLY the diff, enclosed in ```diff ... ``` tags."
    )

    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
    ]


def prepare_phase0_data(data_dir, n_instances=10, seed=42):
    """Prepare Phase 0 dataset from local data files + HF dataset."""
    from datasets import load_dataset

    log.info("Loading SWE-bench Verified from HuggingFace...")
    ds = load_dataset("princeton-nlp/SWE-bench_Verified", split="test")
    instance_info = {}
    for row in ds:
        f2p = json.loads(row["FAIL_TO_PASS"])
        if len(f2p) >= 2:
            instance_info[row["instance_id"]] = {
                "problem_statement": row.get("problem_statement", ""),
                "fail_to_pass": f2p,
                "pass_to_pass": json.loads(row["PASS_TO_PASS"]),
                "gold_patch": row["patch"],
            }
    log.info(f"T>=2 instances from HF: {len(instance_info)}")

    # Load mutation patches
    mutation_files = list(Path(data_dir).glob("predictions_mutation_*.jsonl"))
    mutations_by_instance = defaultdict(list)
    for mf in mutation_files:
        mutation_type = mf.stem.replace("predictions_mutation_", "")
        for line in mf.open():
            rec = json.loads(line)
            iid = rec["instance_id"]
            if iid in instance_info:
                mutations_by_instance[iid].append({
                    "patch": rec["model_patch"],
                    "type": mutation_type,
                })

    # Load per-test oracle labels from swebench_test.jsonl
    test_data = load_jsonl(os.path.join(data_dir, "swebench_test.jsonl"))
    # Group by (problem_id, mutation_type, patch) -> {test_name: label}
    oracle_labels = defaultdict(dict)
    for row in test_data:
        if row.get("mutation_type", "gold") != "gold":
            key = (row["metadata"]["instance_id"], row.get("mutation_type", ""))
            test_name = row["test"] if isinstance(row["test"], str) else row["metadata"].get("test_name", "")
            oracle_labels[key][test_name] = bool(row["label"])

    # Select instances that have both: mutation patches AND oracle labels for them
    rng = np.random.default_rng(seed)
    candidates = []
    for iid, info in instance_info.items():
        muts = mutations_by_instance.get(iid, [])
        if not muts:
            continue
        # Check if we have oracle labels for any mutation
        for mut in muts:
            key = (iid, mut["type"])
            if key in oracle_labels and len(oracle_labels[key]) >= 2:
                candidates.append({
                    "instance_id": iid,
                    "problem_statement": info["problem_statement"],
                    "gold_patch": info["gold_patch"],
                    "fail_to_pass": info["fail_to_pass"],
                    "mutation_patch": mut["patch"],
                    "mutation_type": mut["type"],
                    "oracle_per_test": oracle_labels[key],
                })
                break  # one mutation per instance for Phase 0

    log.info(f"Candidates with mutation + oracle labels: {len(candidates)}")

    if len(candidates) < n_instances:
        log.warning(f"Only {len(candidates)} candidates available, using all")
        selected = candidates
    else:
        indices = rng.choice(len(candidates), size=n_instances, replace=False)
        selected = [candidates[i] for i in sorted(indices)]

    log.info(f"Selected {len(selected)} instances for Phase 0")
    for i, s in enumerate(selected):
        n_fail = sum(1 for v in s["oracle_per_test"].values() if not v)
        n_pass = sum(1 for v in s["oracle_per_test"].values() if v)
        log.info(f"  [{i}] {s['instance_id']} ({s['mutation_type']}) "
                 f"oracle: {n_fail} fail, {n_pass} pass")

    return selected


def generate_repairs(dataset, model_path, conditions, n_samples=5, output_dir="."):
    """Generate repairs using vLLM."""
    from vllm import LLM, SamplingParams

    log.info(f"Loading model: {model_path}")
    llm = LLM(
        model=model_path,
        tensor_parallel_size=1,
        max_model_len=8192,
        trust_remote_code=True,
        dtype="bfloat16",
        gpu_memory_utilization=0.85,
    )
    tokenizer = llm.get_tokenizer()

    sampling_params = SamplingParams(
        temperature=0.6,
        top_p=0.95,
        max_tokens=2048,
        n=n_samples,
    )

    rng = np.random.default_rng(42)
    all_results = []

    for cond in conditions:
        log.info(f"=== Condition: {cond} ===")
        prompts = []
        meta = []

        for item in dataset:
            messages = build_prompt(item, cond, rng)
            prompt_text = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
            prompts.append(prompt_text)
            meta.append({
                "instance_id": item["instance_id"],
                "condition": cond,
                "mutation_type": item["mutation_type"],
                "gold_patch": item["gold_patch"],
            })

        log.info(f"Generating {len(prompts)} prompts × {n_samples} samples...")
        outputs = llm.generate(prompts, sampling_params)

        for output, m in zip(outputs, meta):
            for k, completion in enumerate(output.outputs):
                diff = extract_diff(completion.text)
                sim = diff_similarity(diff, m["gold_patch"])
                all_results.append({
                    "instance_id": m["instance_id"],
                    "condition": m["condition"],
                    "mutation_type": m["mutation_type"],
                    "sample_k": k,
                    "extracted_diff": diff,
                    "gold_similarity": sim,
                    "diff_nonempty": len(diff) > 20,
                    "has_diff_header": diff.startswith("diff ") or diff.startswith("---"),
                })

        cond_sims = [r["gold_similarity"] for r in all_results if r["condition"] == cond]
        log.info(f"  Mean gold similarity: {np.mean(cond_sims):.3f} "
                 f"(max={np.max(cond_sims):.3f}, nonempty={sum(1 for r in all_results if r['condition']==cond and r['diff_nonempty'])}/{len(cond_sims)})")

    out_path = os.path.join(output_dir, "phase0_repairs.jsonl")
    save_jsonl(all_results, out_path)
    return all_results


def analyze_results(results, output_dir="."):
    """Analyze Phase 0 results."""
    log.info("=== Phase 0 Analysis ===")

    by_cond = defaultdict(list)
    for r in results:
        by_cond[r["condition"]].append(r)

    summary = {}
    for cond in CONDITIONS:
        if cond not in by_cond:
            continue
        entries = by_cond[cond]
        sims = [e["gold_similarity"] for e in entries]
        nonempty = sum(1 for e in entries if e["diff_nonempty"])
        has_header = sum(1 for e in entries if e["has_diff_header"])

        # Best-of-K similarity per instance
        by_inst = defaultdict(list)
        for e in entries:
            by_inst[e["instance_id"]].append(e["gold_similarity"])
        best_per_inst = [max(sims_list) for sims_list in by_inst.values()]

        summary[cond] = {
            "n_samples": len(entries),
            "mean_similarity": float(np.mean(sims)),
            "max_similarity": float(np.max(sims)),
            "best_of_k_mean": float(np.mean(best_per_inst)),
            "best_of_k_max": float(np.max(best_per_inst)),
            "pct_nonempty": nonempty / len(entries) * 100,
            "pct_valid_diff": has_header / len(entries) * 100,
        }

        log.info(f"\n  {cond}:")
        log.info(f"    Mean sim: {summary[cond]['mean_similarity']:.3f}")
        log.info(f"    Best-of-K mean: {summary[cond]['best_of_k_mean']:.3f}")
        log.info(f"    Best-of-K max: {summary[cond]['best_of_k_max']:.3f}")
        log.info(f"    Valid diff: {summary[cond]['pct_valid_diff']:.0f}%")

    # Deltas
    if "control" in summary and "oracle-diag" in summary:
        delta_oracle = summary["oracle-diag"]["best_of_k_mean"] - summary["control"]["best_of_k_mean"]
        log.info(f"\n  Δ(oracle-diag - control) best-of-K: {delta_oracle:+.3f}")
    if "control" in summary and "cls-diag" in summary:
        delta_cls = summary["cls-diag"]["best_of_k_mean"] - summary["control"]["best_of_k_mean"]
        log.info(f"  Δ(cls-diag - control) best-of-K: {delta_cls:+.3f}")
    if "control" in summary and "random-diag" in summary:
        delta_rand = summary["random-diag"]["best_of_k_mean"] - summary["control"]["best_of_k_mean"]
        log.info(f"  Δ(random-diag - control) best-of-K: {delta_rand:+.3f}")

    out_path = os.path.join(output_dir, "phase0_summary.json")
    os.makedirs(output_dir, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    log.info(f"\nSaved summary to {out_path}")

    return summary


def main():
    parser = argparse.ArgumentParser(description="Re-Repair Phase 0")
    parser.add_argument("--data-dir", required=True,
                        help="Path to data/swebench_full/")
    parser.add_argument("--model", default="/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B",
                        help="Model path")
    parser.add_argument("--n-instances", type=int, default=10)
    parser.add_argument("--n-samples", type=int, default=5,
                        help="Completions per (instance, condition)")
    parser.add_argument("--conditions", nargs="+", default=CONDITIONS)
    parser.add_argument("--output-dir", default="/root/autodl-tmp/eval_results/re_repair_phase0")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--analyze-only", type=str, default=None,
                        help="Path to existing phase0_repairs.jsonl to analyze")
    args = parser.parse_args()

    if args.analyze_only:
        results = load_jsonl(args.analyze_only)
        analyze_results(results, args.output_dir)
        return

    # Step 1: Prepare data
    dataset = prepare_phase0_data(args.data_dir, args.n_instances, args.seed)

    # Save prepared dataset
    prep_path = os.path.join(args.output_dir, "phase0_dataset.jsonl")
    save_jsonl(dataset, prep_path)

    # Step 2: Generate repairs
    results = generate_repairs(
        dataset, args.model, args.conditions, args.n_samples, args.output_dir
    )

    # Step 3: Analyze
    analyze_results(results, args.output_dir)


if __name__ == "__main__":
    main()
