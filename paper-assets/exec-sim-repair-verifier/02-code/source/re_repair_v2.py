#!/usr/bin/env python3
"""
Re-Repair v2: Generation-stage script for the Re-Repair downstream experiment.

Given a buggy patch + varying levels of diagnostic information, measure whether
richer diagnostics help an LLM produce better repairs.

Conditions (information ascending):
  A1 — "Your patch failed some tests. Generate a fixed version." (minimal)
  A2 — A1 + list of all test function names (no pass/fail labels)
  B  — A2 + CLS verifier predicted pass/fail per test
  C  — A2 + ground-truth pass/fail per test (oracle)
  D  — A2 + random pass/fail labels (negative control)

CLI usage:
  # Full generation run
  python re_repair_v2.py generate \
      --data-dir /home/sonny/exec-sim-repair-verifier/swebench_full/ \
      --model /root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B \
      --conditions A1 A2 B C D \
      --n-instances 50 --n-samples 5 \
      --cls-predictions /path/to/cls_preds.jsonl \
      --output-dir /root/autodl-tmp/eval_results/re_repair_v2/

  # Data preparation only (no GPU needed)
  python re_repair_v2.py prepare \
      --data-dir /home/sonny/exec-sim-repair-verifier/swebench_full/ \
      --n-instances 50 \
      --output-dir /root/autodl-tmp/eval_results/re_repair_v2/

  # Analyze existing results
  python re_repair_v2.py analyze \
      --results /root/autodl-tmp/eval_results/re_repair_v2/generated_repairs.jsonl \
      --output-dir /root/autodl-tmp/eval_results/re_repair_v2/
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

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ALL_CONDITIONS = ["A1", "A2", "B", "C", "D"]
MIN_F2P_TESTS = 2

SYSTEM_PROMPT = (
    "You are a software engineer. You are given a code patch that was intended "
    "to fix an issue but does not fully work. Your task is to produce a corrected "
    "patch. Output ONLY the corrected unified diff enclosed in ```diff ... ``` tags."
)

# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(data, path):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
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
    """Normalized sequence similarity between two diffs."""
    if not generated or not gold:
        return 0.0
    return difflib.SequenceMatcher(None, generated, gold).ratio()


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------


def _format_test_list(test_names):
    """Format test names as a markdown bullet list."""
    return "\n".join(f"- `{t}`" for t in test_names)


def _format_diagnostic_with_labels(per_test):
    """Format per-test pass/fail labels into diagnostic section."""
    fails = [t for t, passed in per_test.items() if not passed]
    passes = [t for t, passed in per_test.items() if passed]
    parts = ["## Test Diagnostic"]
    if fails:
        parts.append(f"The current patch **fails** the following tests:\n{_format_test_list(fails)}")
    if passes:
        parts.append(f"The current patch **passes** the following tests:\n{_format_test_list(passes)}")
    return "\n\n".join(parts)


def build_prompt(item, condition, rng):
    """Build chat messages for a given (instance, condition).

    Args:
        item: dict with keys instance_id, problem_statement, mutation_patch,
              oracle_per_test, cls_per_test, all_test_names
        condition: one of A1, A2, B, C, D
        rng: numpy random generator (for condition D)

    Returns:
        list of {role, content} messages
    """
    patch_section = (
        f"## Issue Description\n{item['problem_statement']}\n\n"
        f"## Current (Incorrect) Patch\n```diff\n{item['mutation_patch']}\n```\n"
    )

    all_tests = item["all_test_names"]

    if condition == "A1":
        diagnostic = (
            "Your patch failed some tests. "
            "Please produce a corrected patch in unified diff format.\n"
            "Output ONLY the diff, enclosed in ```diff ... ``` tags."
        )
    elif condition == "A2":
        diagnostic = (
            "Your patch failed some tests. The relevant test functions are:\n"
            f"{_format_test_list(all_tests)}\n\n"
            "Please produce a corrected patch in unified diff format.\n"
            "Output ONLY the diff, enclosed in ```diff ... ``` tags."
        )
    elif condition == "B":
        per_test = item.get("cls_per_test", {})
        if not per_test:
            per_test = {t: bool(rng.random() > 0.5) for t in all_tests}
        diagnostic = (
            "Your patch failed some tests. The relevant test functions are:\n"
            f"{_format_test_list(all_tests)}\n\n"
            f"{_format_diagnostic_with_labels(per_test)}\n\n"
            "(These pass/fail labels are predicted by an automated verifier.)\n\n"
            "Please produce a corrected patch in unified diff format.\n"
            "Output ONLY the diff, enclosed in ```diff ... ``` tags."
        )
    elif condition == "C":
        per_test = item["oracle_per_test"]
        diagnostic = (
            "Your patch failed some tests. The relevant test functions are:\n"
            f"{_format_test_list(all_tests)}\n\n"
            f"{_format_diagnostic_with_labels(per_test)}\n\n"
            "Please produce a corrected patch in unified diff format.\n"
            "Output ONLY the diff, enclosed in ```diff ... ``` tags."
        )
    elif condition == "D":
        per_test = {t: bool(rng.random() > 0.5) for t in all_tests}
        diagnostic = (
            "Your patch failed some tests. The relevant test functions are:\n"
            f"{_format_test_list(all_tests)}\n\n"
            f"{_format_diagnostic_with_labels(per_test)}\n\n"
            "Please produce a corrected patch in unified diff format.\n"
            "Output ONLY the diff, enclosed in ```diff ... ``` tags."
        )
    else:
        raise ValueError(f"Unknown condition: {condition}")

    user_content = patch_section + "\n" + diagnostic

    return [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_content},
    ]


# ---------------------------------------------------------------------------
# Data preparation
# ---------------------------------------------------------------------------


def prepare_dataset(data_dir, n_instances=50, seed=42, cls_predictions_path=None):
    """Prepare dataset from SWE-bench Verified + local mutation patches + oracle labels.

    Returns list of instance dicts ready for prompt construction.
    """
    from datasets import load_dataset

    log.info("Loading SWE-bench Verified from HuggingFace...")
    ds = load_dataset("princeton-nlp/SWE-bench_Verified", split="test")
    instance_info = {}
    for row in ds:
        f2p = json.loads(row["FAIL_TO_PASS"])
        if len(f2p) >= MIN_F2P_TESTS:
            instance_info[row["instance_id"]] = {
                "problem_statement": row.get("problem_statement", ""),
                "fail_to_pass": f2p,
                "pass_to_pass": json.loads(row["PASS_TO_PASS"]),
                "gold_patch": row["patch"],
            }
    log.info(f"Instances with T_f2p >= {MIN_F2P_TESTS}: {len(instance_info)}")

    # Load mutation patches
    data_path = Path(data_dir)
    mutation_files = list(data_path.glob("predictions_mutation_*.jsonl"))
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
    log.info(f"Loaded mutations for {len(mutations_by_instance)} instances")

    # Load per-test oracle labels from swebench_test.jsonl
    test_file = os.path.join(data_dir, "swebench_test.jsonl")
    oracle_labels = defaultdict(dict)
    if os.path.exists(test_file):
        test_data = load_jsonl(test_file)
        for row in test_data:
            if row.get("mutation_type", "gold") != "gold":
                key = (row["metadata"]["instance_id"], row.get("mutation_type", ""))
                test_name = row["test"] if isinstance(row["test"], str) else row["metadata"].get("test_name", "")
                oracle_labels[key][test_name] = bool(row["label"])
        log.info(f"Oracle labels loaded: {len(oracle_labels)} (instance, mutation) pairs")
    else:
        log.warning(f"Oracle labels file not found: {test_file}")

    # Load CLS predictions if provided
    cls_by_key = defaultdict(dict)
    if cls_predictions_path and os.path.exists(cls_predictions_path):
        cls_data = load_jsonl(cls_predictions_path)
        for row in cls_data:
            key = (row["instance_id"], row.get("mutation_type", ""))
            test_name = row.get("test_name", row.get("test", ""))
            pred = row.get("cls_pred", row.get("prediction", -1))
            if pred != -1:
                cls_by_key[key][test_name] = bool(pred)
        log.info(f"CLS predictions loaded: {len(cls_by_key)} (instance, mutation) pairs")

    # Select candidates: instances with mutation patches AND oracle labels
    rng = np.random.default_rng(seed)
    candidates = []
    for iid, info in instance_info.items():
        muts = mutations_by_instance.get(iid, [])
        if not muts:
            continue
        for mut in muts:
            key = (iid, mut["type"])
            if key in oracle_labels and len(oracle_labels[key]) >= MIN_F2P_TESTS:
                oracle = oracle_labels[key]
                all_test_names = sorted(oracle.keys())
                cls_preds = cls_by_key.get(key, {})
                candidates.append({
                    "instance_id": iid,
                    "problem_statement": info["problem_statement"],
                    "gold_patch": info["gold_patch"],
                    "fail_to_pass": info["fail_to_pass"],
                    "mutation_patch": mut["patch"],
                    "mutation_type": mut["type"],
                    "oracle_per_test": oracle,
                    "cls_per_test": cls_preds,
                    "all_test_names": all_test_names,
                })
                break

    log.info(f"Candidates with mutation + oracle labels: {len(candidates)}")

    if len(candidates) <= n_instances:
        selected = candidates
    else:
        indices = rng.choice(len(candidates), size=n_instances, replace=False)
        selected = [candidates[i] for i in sorted(indices)]

    log.info(f"Selected {len(selected)} instances")
    for i, s in enumerate(selected[:5]):
        n_fail = sum(1 for v in s["oracle_per_test"].values() if not v)
        n_pass = sum(1 for v in s["oracle_per_test"].values() if v)
        log.info(f"  [{i}] {s['instance_id']} ({s['mutation_type']}) "
                 f"tests: {n_fail} fail, {n_pass} pass, cls_avail={len(s['cls_per_test'])>0}")

    return selected


# ---------------------------------------------------------------------------
# CLS real-time inference (fallback when no precomputed predictions)
# ---------------------------------------------------------------------------


def run_cls_inference(dataset, cls_checkpoint, cls_base_model):
    """Run CLS model inference to populate cls_per_test for each instance.

    Modifies dataset in-place.
    """
    import torch
    from peft import PeftModel
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info(f"Loading CLS model: {cls_base_model} + LoRA from {cls_checkpoint}")
    tokenizer = AutoTokenizer.from_pretrained(cls_base_model, trust_remote_code=True)
    base_model = AutoModelForCausalLM.from_pretrained(
        cls_base_model, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True,
    )
    model = PeftModel.from_pretrained(base_model, cls_checkpoint)
    model.eval()

    total_preds = 0
    for item in dataset:
        if item["cls_per_test"]:
            continue
        preds = {}
        for test_name in item["all_test_names"]:
            messages = [
                {"role": "system", "content": "You are a code verifier. Predict whether the test will pass or fail given the patch."},
                {"role": "user", "content": f"## Patch\n```diff\n{item['mutation_patch']}\n```\n\n## Test\n`{test_name}`\n\nWill this test pass or fail? Answer with one word: pass or fail."},
            ]
            input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
            inputs = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=4096).to(model.device)
            with torch.no_grad():
                outputs = model.generate(**inputs, max_new_tokens=8, do_sample=False)
            generated = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
            pred = _parse_cls_output(generated)
            if pred != -1:
                preds[test_name] = bool(pred)
            total_preds += 1

        item["cls_per_test"] = preds

    log.info(f"CLS inference complete: {total_preds} predictions made")
    del model
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def _parse_cls_output(text):
    """Parse CLS model output to 0 (fail) / 1 (pass) / -1 (unparseable)."""
    if "</think>" in text:
        text = text.split("</think>")[-1]
    text = text.strip().lower()
    if "pass" in text and "fail" not in text:
        return 1
    if "fail" in text:
        return 0
    return -1


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------


def generate_repairs(dataset, model_path, conditions, n_samples=5, output_dir=".",
                     tensor_parallel_size=1, gpu_memory_utilization=0.90):
    """Generate repair patches using vLLM across all conditions.

    Args:
        dataset: prepared instance list
        model_path: path to Instruct model
        conditions: list of condition names (subset of ALL_CONDITIONS)
        n_samples: completions per (instance, condition)
        output_dir: output directory
        tensor_parallel_size: number of GPUs for tensor parallelism
        gpu_memory_utilization: fraction of GPU memory to use

    Returns:
        list of result dicts
    """
    from vllm import LLM, SamplingParams

    log.info(f"Loading model: {model_path}")
    llm = LLM(
        model=model_path,
        tensor_parallel_size=tensor_parallel_size,
        max_model_len=8192,
        trust_remote_code=True,
        dtype="bfloat16",
        gpu_memory_utilization=gpu_memory_utilization,
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
        log.info(f"=== Condition: {cond} ({len(dataset)} instances x {n_samples} samples) ===")
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
                "prompt_messages": messages,
            })

        log.info(f"Generating {len(prompts)} prompts x {n_samples} samples...")
        outputs = llm.generate(prompts, sampling_params)

        for output, m in zip(outputs, meta):
            for k, completion in enumerate(output.outputs):
                diff = extract_diff(completion.text)
                sim = diff_similarity(diff, m["gold_patch"])
                all_results.append({
                    "instance_id": m["instance_id"],
                    "condition": m["condition"],
                    "sample_k": k,
                    "prompt_messages": m["prompt_messages"],
                    "raw_response": completion.text,
                    "extracted_diff": diff,
                    "metadata": {
                        "patch_source": m["mutation_type"],
                        "model": model_path,
                        "gold_similarity": sim,
                        "diff_nonempty": len(diff) > 20,
                        "has_diff_header": diff.startswith("diff ") or diff.startswith("---"),
                    },
                })

        cond_results = [r for r in all_results if r["condition"] == cond]
        sims = [r["metadata"]["gold_similarity"] for r in cond_results]
        nonempty = sum(1 for r in cond_results if r["metadata"]["diff_nonempty"])
        log.info(f"  Mean gold similarity: {np.mean(sims):.3f}, "
                 f"max: {np.max(sims):.3f}, nonempty: {nonempty}/{len(sims)}")

    out_path = os.path.join(output_dir, "generated_repairs.jsonl")
    save_jsonl(all_results, out_path)
    return all_results


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------


def analyze_results(results, output_dir="."):
    """Analyze generation results: similarity metrics per condition."""
    log.info(f"=== Analyzing {len(results)} results ===")

    by_cond = defaultdict(list)
    for r in results:
        by_cond[r["condition"]].append(r)

    summary = {}
    for cond in ALL_CONDITIONS:
        if cond not in by_cond:
            continue
        entries = by_cond[cond]
        sims = [e["metadata"]["gold_similarity"] for e in entries]
        nonempty = sum(1 for e in entries if e["metadata"]["diff_nonempty"])
        has_header = sum(1 for e in entries if e["metadata"]["has_diff_header"])

        by_inst = defaultdict(list)
        for e in entries:
            by_inst[e["instance_id"]].append(e["metadata"]["gold_similarity"])
        best_per_inst = [max(v) for v in by_inst.values()]

        summary[cond] = {
            "n_instances": len(by_inst),
            "n_samples": len(entries),
            "mean_similarity": float(np.mean(sims)),
            "std_similarity": float(np.std(sims)),
            "best_of_k_mean": float(np.mean(best_per_inst)),
            "best_of_k_std": float(np.std(best_per_inst)),
            "pct_nonempty": nonempty / len(entries) * 100,
            "pct_valid_diff": has_header / len(entries) * 100,
        }

        log.info(f"  {cond}: mean_sim={summary[cond]['mean_similarity']:.3f}, "
                 f"best_of_k={summary[cond]['best_of_k_mean']:.3f}, "
                 f"valid_diff={summary[cond]['pct_valid_diff']:.0f}%")

    # Deltas relative to A1
    if "A1" in summary:
        log.info("  Deltas (best-of-K mean, relative to A1):")
        baseline = summary["A1"]["best_of_k_mean"]
        for cond in ALL_CONDITIONS[1:]:
            if cond in summary:
                delta = summary[cond]["best_of_k_mean"] - baseline
                log.info(f"    Δ({cond} - A1) = {delta:+.3f}")

    out_path = os.path.join(output_dir, "analysis_summary.json")
    os.makedirs(output_dir, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    log.info(f"Saved analysis to {out_path}")

    return summary


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------


def cmd_prepare(args):
    """Prepare dataset (no GPU needed)."""
    dataset = prepare_dataset(
        data_dir=args.data_dir,
        n_instances=args.n_instances,
        seed=args.seed,
        cls_predictions_path=args.cls_predictions,
    )
    out_path = os.path.join(args.output_dir, "prepared_dataset.jsonl")
    save_jsonl(dataset, out_path)
    log.info(f"Dataset prepared: {len(dataset)} instances saved to {out_path}")


def cmd_generate(args):
    """Full generation pipeline: prepare data + generate repairs."""
    dataset = prepare_dataset(
        data_dir=args.data_dir,
        n_instances=args.n_instances,
        seed=args.seed,
        cls_predictions_path=args.cls_predictions,
    )

    # If condition B requested but no CLS predictions available, run inference
    if "B" in args.conditions:
        missing_cls = [item for item in dataset if not item["cls_per_test"]]
        if missing_cls:
            if args.cls_checkpoint and args.cls_base_model:
                log.info(f"{len(missing_cls)} instances missing CLS predictions, running inference...")
                run_cls_inference(dataset, args.cls_checkpoint, args.cls_base_model)
            else:
                log.warning(f"{len(missing_cls)} instances have no CLS predictions and no "
                            f"checkpoint specified. Condition B will use random fallback.")

    # Save prepared dataset
    prep_path = os.path.join(args.output_dir, "prepared_dataset.jsonl")
    save_jsonl(dataset, prep_path)

    # Generate
    results = generate_repairs(
        dataset=dataset,
        model_path=args.model,
        conditions=args.conditions,
        n_samples=args.n_samples,
        output_dir=args.output_dir,
        tensor_parallel_size=args.tensor_parallel_size,
        gpu_memory_utilization=args.gpu_memory_utilization,
    )

    # Quick analysis
    analyze_results(results, args.output_dir)


def cmd_analyze(args):
    """Analyze existing results."""
    results = load_jsonl(args.results)
    analyze_results(results, args.output_dir)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(
        description="Re-Repair v2: Generation stage for re-repair downstream experiment"
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # --- prepare ---
    p_prep = sub.add_parser("prepare", help="Prepare dataset (no GPU needed)")
    p_prep.add_argument("--data-dir", required=True,
                        help="Path to swebench_full/ directory")
    p_prep.add_argument("--n-instances", type=int, default=50,
                        help="Number of instances to select")
    p_prep.add_argument("--seed", type=int, default=42)
    p_prep.add_argument("--cls-predictions", default=None,
                        help="Path to precomputed CLS predictions JSONL")
    p_prep.add_argument("--output-dir", default="/root/autodl-tmp/eval_results/re_repair_v2/")

    # --- generate ---
    p_gen = sub.add_parser("generate", help="Prepare data + generate repairs (needs GPU)")
    p_gen.add_argument("--data-dir", required=True,
                       help="Path to swebench_full/ directory")
    p_gen.add_argument("--model", default="/root/autodl-tmp/.hf_cache/Qwen/Qwen3-8B",
                       help="Path to Instruct model for repair generation (Qwen3-8B = Instruct)")
    p_gen.add_argument("--conditions", nargs="+", default=ALL_CONDITIONS,
                       choices=ALL_CONDITIONS,
                       help="Which conditions to run")
    p_gen.add_argument("--n-instances", type=int, default=50,
                       help="Number of instances to select")
    p_gen.add_argument("--n-samples", type=int, default=5,
                       help="Completions per (instance, condition)")
    p_gen.add_argument("--seed", type=int, default=42)
    p_gen.add_argument("--cls-predictions", default=None,
                       help="Path to precomputed CLS predictions JSONL")
    p_gen.add_argument("--cls-checkpoint", default=None,
                       help="LoRA checkpoint for real-time CLS inference (condition B fallback)")
    p_gen.add_argument("--cls-base-model", default="deepseek-ai/deepseek-coder-6.7b-instruct",
                       help="Base model for CLS inference")
    p_gen.add_argument("--tensor-parallel-size", type=int, default=1,
                       help="Number of GPUs for tensor parallelism")
    p_gen.add_argument("--gpu-memory-utilization", type=float, default=0.90,
                       help="Fraction of GPU memory for vLLM")
    p_gen.add_argument("--output-dir", default="/root/autodl-tmp/eval_results/re_repair_v2/")

    # --- analyze ---
    p_ana = sub.add_parser("analyze", help="Analyze existing results")
    p_ana.add_argument("--results", required=True,
                       help="Path to generated_repairs.jsonl")
    p_ana.add_argument("--output-dir", default="/root/autodl-tmp/eval_results/re_repair_v2/")

    args = parser.parse_args()

    if args.command == "prepare":
        cmd_prepare(args)
    elif args.command == "generate":
        cmd_generate(args)
    elif args.command == "analyze":
        cmd_analyze(args)


if __name__ == "__main__":
    main()
