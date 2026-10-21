#!/usr/bin/env python3
"""
Re-Repair Downstream Experiment: evaluate whether CLS per-test diagnostic
information improves LLM patch repair success rate.

Conditions:
  control     — "patch is incorrect, please fix" (no per-test info)
  cls-diag    — control + CLS-predicted per-test pass/fail
  oracle-diag — control + ground-truth per-test pass/fail
  random-diag — control + randomly assigned per-test pass/fail

Usage:
  # Phase 1: prepare data (collect incorrect patches + CLS predictions)
  python re_repair_eval.py prepare \
      --swebench-predictions predictions_dir/ \
      --cls-checkpoint checkpoints/cls8b-s42-ckpt3600 \
      --output-dir artifacts/re_repair

  # Phase 2: generate repairs
  python re_repair_eval.py generate \
      --data artifacts/re_repair/repair_dataset.jsonl \
      --model Qwen/Qwen3-8B-Instruct \
      --conditions control cls-diag oracle-diag random-diag \
      --output-dir artifacts/re_repair

  # Phase 3: verify repairs via Docker execution
  python re_repair_eval.py verify \
      --repairs artifacts/re_repair/generated_repairs.jsonl \
      --output-dir artifacts/re_repair

  # Phase 4: analyze results
  python re_repair_eval.py analyze \
      --results artifacts/re_repair/verification_results.jsonl \
      --output-dir artifacts/re_repair
"""

import argparse
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

MIN_F2P_TESTS = 2

CONDITIONS = ["control", "cls-diag", "oracle-diag", "random-diag"]

SYSTEM_PROMPT_REPAIR = (
    "You are a software engineer. You are given a code patch that was intended "
    "to fix an issue but does not fully work. Your task is to produce a corrected "
    "patch. Output ONLY the corrected unified diff enclosed in ```diff ... ``` tags."
)

DIAGNOSTIC_TEMPLATE = (
    "## Test Diagnostic\n"
    "The current patch **fails** the following tests:\n{fail_list}\n\n"
    "The current patch **passes** the following tests:\n{pass_list}"
)

# ---------------------------------------------------------------------------
# Data loading utilities
# ---------------------------------------------------------------------------


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(data, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")
    log.info(f"Saved {len(data)} records to {path}")


def load_swebench_verified():
    """Load SWE-bench Verified and filter to T_f2p >= MIN_F2P_TESTS."""
    from datasets import load_dataset

    ds = load_dataset("princeton-nlp/SWE-bench_Verified", split="test")
    filtered = []
    for row in ds:
        f2p = json.loads(row["FAIL_TO_PASS"])
        if len(f2p) >= MIN_F2P_TESTS:
            filtered.append({
                "instance_id": row["instance_id"],
                "repo": row["repo"],
                "base_commit": row["base_commit"],
                "gold_patch": row["patch"],
                "test_patch": row["test_patch"],
                "fail_to_pass": f2p,
                "pass_to_pass": json.loads(row["PASS_TO_PASS"]),
                "problem_statement": row.get("problem_statement", row.get("hints_text", "")),
                "version": row["version"],
            })
    log.info(f"SWE-bench Verified: {len(ds)} total, {len(filtered)} with T_f2p >= {MIN_F2P_TESTS}")
    return filtered


# ---------------------------------------------------------------------------
# Phase 1: Prepare — collect incorrect patches + run CLS predictions
# ---------------------------------------------------------------------------


def collect_incorrect_patches(instances, predictions_dir):
    """Collect incorrect patches from public SWE-bench agent predictions.

    Reads prediction JSONL files from predictions_dir/, matches to T>=2
    instances, and filters to patches that are incorrect (not all F2P pass).

    Returns list of {instance_id, patch, source, ...}.
    """
    instance_ids = {inst["instance_id"] for inst in instances}
    patches = []

    pred_dir = Path(predictions_dir)
    for pred_file in pred_dir.glob("*.jsonl"):
        source_name = pred_file.stem
        for line in pred_file.open():
            rec = json.loads(line)
            iid = rec.get("instance_id")
            if iid not in instance_ids:
                continue
            model_patch = rec.get("model_patch", rec.get("patch", ""))
            if not model_patch or not model_patch.strip():
                continue
            patches.append({
                "instance_id": iid,
                "patch": model_patch,
                "source": source_name,
            })

    log.info(f"Collected {len(patches)} candidate incorrect patches from {predictions_dir}")
    return patches


def run_cls_predictions(patches_with_tests, cls_checkpoint, model_name="Qwen/Qwen3-8B"):
    """Run CLS model to predict per-test pass/fail for each (patch, test).

    Args:
        patches_with_tests: list of {instance_id, patch, test_name, test_code, ...}
        cls_checkpoint: path to LoRA checkpoint
        model_name: base model name

    Returns:
        list of {instance_id, patch_id, test_name, cls_pred (0/1), cls_prob}
    """
    import torch
    from peft import PeftModel
    from transformers import AutoModelForCausalLM, AutoTokenizer

    log.info(f"Loading CLS model: {model_name} + {cls_checkpoint}")
    tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
    base_model = AutoModelForCausalLM.from_pretrained(
        model_name, torch_dtype=torch.bfloat16, device_map="auto", trust_remote_code=True,
    )
    model = PeftModel.from_pretrained(base_model, cls_checkpoint)
    model.eval()

    results = []
    for i, item in enumerate(patches_with_tests):
        messages = [
            {"role": "system", "content": "You are a code verifier. Given a code patch and a test case, predict whether the test will pass or fail."},
            {"role": "user", "content": f"## Code\n{item['patch']}\n\n## Test\n{item['test_code']}\n\nWill this test pass or fail?"},
        ]
        input_text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
        inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

        with torch.no_grad():
            outputs = model.generate(**inputs, max_new_tokens=8, do_sample=False)

        generated = tokenizer.decode(outputs[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True)
        pred = parse_cls_output(generated)

        results.append({
            "instance_id": item["instance_id"],
            "patch_id": item.get("patch_id", i),
            "test_name": item["test_name"],
            "cls_pred": pred,
            "cls_raw": generated.strip(),
        })

        if (i + 1) % 100 == 0:
            log.info(f"CLS inference: {i+1}/{len(patches_with_tests)}")

    return results


def parse_cls_output(text):
    """Parse CLS model output to binary 0 (fail) / 1 (pass)."""
    if "</think>" in text:
        text = text.split("</think>")[-1]
    text = text.strip().lower()
    if "pass" in text and "fail" not in text:
        return 1
    if "fail" in text:
        return 0
    return -1  # unparseable


def run_ground_truth_verification(instance, patch):
    """Run Docker execution to get ground-truth per-test results.

    Uses SWE-bench harness. Returns dict {test_name: bool(passed)}.
    """
    # TODO: implement using swebench.harness
    # from swebench.harness.run_evaluation import run_instances
    # from swebench.harness.test_spec import make_test_spec
    raise NotImplementedError("Requires SWE-bench Docker harness setup")


def cmd_prepare(args):
    log.info("=== Phase 1: Prepare repair dataset ===")

    instances = load_swebench_verified()
    patches = collect_incorrect_patches(instances, args.swebench_predictions)

    # TODO: for each (instance, patch), run ground-truth Docker verification
    # to confirm patch is actually incorrect and get per-test results.
    # Then run CLS model for per-test predictions.
    # Finally, assemble repair_dataset.jsonl.

    instance_map = {inst["instance_id"]: inst for inst in instances}

    dataset = []
    for p in patches:
        inst = instance_map.get(p["instance_id"])
        if inst is None:
            continue
        dataset.append({
            "instance_id": p["instance_id"],
            "repo": inst["repo"],
            "patch": p["patch"],
            "patch_source": p["source"],
            "gold_patch": inst["gold_patch"],
            "problem_statement": inst["problem_statement"],
            "fail_to_pass": inst["fail_to_pass"],
            "pass_to_pass": inst["pass_to_pass"],
            "gt_per_test": {},      # placeholder: ground-truth per-test results
            "cls_per_test": {},     # placeholder: CLS predictions
        })

    out_path = os.path.join(args.output_dir, "repair_dataset.jsonl")
    save_jsonl(dataset, out_path)
    log.info(f"Prepared {len(dataset)} repair instances")


# ---------------------------------------------------------------------------
# Phase 2: Generate — produce repair patches under each condition
# ---------------------------------------------------------------------------


def build_repair_prompt(item, condition, rng=None):
    """Build the repair prompt for a given condition.

    Returns list of chat messages [{role, content}].
    """
    base_content = (
        f"## Issue Description\n{item['problem_statement']}\n\n"
        f"## Current (Incorrect) Patch\n```diff\n{item['patch']}\n```\n"
    )

    if condition == "control":
        diagnostic = ""
    elif condition == "cls-diag":
        per_test = item.get("cls_per_test", {})
        diagnostic = _format_diagnostic(per_test)
    elif condition == "oracle-diag":
        per_test = item.get("gt_per_test", {})
        diagnostic = _format_diagnostic(per_test)
    elif condition == "random-diag":
        all_tests = item.get("fail_to_pass", []) + item.get("pass_to_pass", [])
        if rng is None:
            rng = np.random.default_rng(42)
        per_test = {t: bool(rng.random() > 0.5) for t in all_tests}
        diagnostic = _format_diagnostic(per_test)
    else:
        raise ValueError(f"Unknown condition: {condition}")

    user_content = base_content
    if diagnostic:
        user_content += f"\n{diagnostic}\n"
    user_content += (
        "\nPlease produce a corrected patch in unified diff format that "
        "resolves the issue.\nOutput ONLY the diff, enclosed in ```diff ... ``` tags."
    )

    return [
        {"role": "system", "content": SYSTEM_PROMPT_REPAIR},
        {"role": "user", "content": user_content},
    ]


def _format_diagnostic(per_test):
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


def extract_diff_from_response(text):
    """Extract unified diff from LLM response."""
    pattern = r"```diff\s*\n(.*?)```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    pattern_generic = r"```\s*\n(diff.*?)```"
    match = re.search(pattern_generic, text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()


def generate_repairs_vllm(dataset, conditions, model_name, n_samples, output_dir):
    """Generate repair patches using vLLM for all conditions.

    Args:
        dataset: list of repair instances from Phase 1
        conditions: list of condition names
        model_name: HF model name for repair LLM
        n_samples: number of completions per (instance, condition)
        output_dir: where to save results
    """
    from vllm import LLM, SamplingParams

    log.info(f"Loading repair LLM: {model_name}")
    llm = LLM(
        model=model_name,
        tensor_parallel_size=1,  # adjust based on GPU count
        max_model_len=8192,
        trust_remote_code=True,
        dtype="bfloat16",
    )
    sampling_params = SamplingParams(
        temperature=0.6, top_p=0.95, max_tokens=2048, n=n_samples,
    )

    all_repairs = []
    rng = np.random.default_rng(42)

    for cond in conditions:
        log.info(f"Generating repairs for condition: {cond}")
        prompts = []
        meta = []

        for item in dataset:
            messages = build_repair_prompt(item, cond, rng=rng)
            # vLLM chat: convert messages to single string
            # TODO: use tokenizer.apply_chat_template if needed
            prompt_text = "\n".join(
                f"<|im_start|>{m['role']}\n{m['content']}<|im_end|>" for m in messages
            ) + "\n<|im_start|>assistant\n"
            prompts.append(prompt_text)
            meta.append({
                "instance_id": item["instance_id"],
                "condition": cond,
                "patch_source": item.get("patch_source", "unknown"),
            })

        outputs = llm.generate(prompts, sampling_params)

        for output, m in zip(outputs, meta):
            for k, completion in enumerate(output.outputs):
                diff = extract_diff_from_response(completion.text)
                all_repairs.append({
                    **m,
                    "sample_k": k,
                    "raw_response": completion.text,
                    "extracted_diff": diff,
                    "diff_valid": diff.startswith("diff ") or diff.startswith("---"),
                })

    out_path = os.path.join(output_dir, "generated_repairs.jsonl")
    save_jsonl(all_repairs, out_path)
    log.info(f"Generated {len(all_repairs)} total repairs")
    return all_repairs


def cmd_generate(args):
    log.info("=== Phase 2: Generate repairs ===")
    dataset = load_jsonl(args.data)
    conditions = args.conditions or CONDITIONS
    generate_repairs_vllm(
        dataset, conditions, args.model, args.n_samples, args.output_dir,
    )


# ---------------------------------------------------------------------------
# Phase 3: Verify — Docker execution of generated repair patches
# ---------------------------------------------------------------------------


def cmd_verify(args):
    log.info("=== Phase 3: Verify repairs via Docker ===")
    repairs = load_jsonl(args.repairs)

    # Dedup: many samples produce identical diffs
    seen = set()
    unique_repairs = []
    for r in repairs:
        key = (r["instance_id"], r["extracted_diff"])
        if key in seen:
            r["dedup_ref"] = True
            continue
        seen.add(key)
        unique_repairs.append(r)

    log.info(f"Total repairs: {len(repairs)}, unique: {len(unique_repairs)}")

    # TODO: run SWE-bench Docker harness on each unique repair
    # For each repair:
    #   1. Apply extracted_diff to repo at base_commit
    #   2. Run test suite
    #   3. Record per-test pass/fail
    #   4. Mark resolved = all F2P pass & no P2P regressions

    results = []
    for r in unique_repairs:
        results.append({
            **r,
            "resolved": None,       # placeholder
            "f2p_passed": None,      # placeholder: list of passed F2P tests
            "f2p_failed": None,      # placeholder: list of failed F2P tests
            "p2p_regressed": None,   # placeholder: list of regressed P2P tests
            "error": None,
        })

    out_path = os.path.join(args.output_dir, "verification_results.jsonl")
    save_jsonl(results, out_path)


# ---------------------------------------------------------------------------
# Phase 4: Analyze — compute metrics and statistical tests
# ---------------------------------------------------------------------------


def compute_resolve_rates(results):
    """Compute resolve rate per condition.

    Returns dict {condition: {pass_at_1, pass_at_5, n_instances, n_patches}}.
    """
    by_condition = defaultdict(lambda: defaultdict(list))

    for r in results:
        cond = r["condition"]
        iid = r["instance_id"]
        resolved = r.get("resolved", False)
        by_condition[cond][iid].append(resolved)

    metrics = {}
    for cond, instances in by_condition.items():
        n_inst = len(instances)
        pass_at_1_sum = 0
        pass_at_5_sum = 0

        for iid, resolutions in instances.items():
            k = len(resolutions)
            n_pass = sum(resolutions)
            # pass@1: unbiased estimator
            pass_at_1_sum += 1 - (comb_ratio(k - n_pass, 1, k, 1) if k >= 1 else 1.0)
            # pass@5
            pass_at_5_sum += 1 - (comb_ratio(k - n_pass, 5, k, 5) if k >= 5 else (0.0 if n_pass > 0 else 1.0))

        metrics[cond] = {
            "pass_at_1": pass_at_1_sum / n_inst if n_inst else 0,
            "pass_at_5": pass_at_5_sum / n_inst if n_inst else 0,
            "n_instances": n_inst,
            "n_total_repairs": sum(len(v) for v in instances.values()),
        }

    return metrics


def comb_ratio(a, b, c, d):
    """Compute C(a,b) / C(c,d) safely."""
    from math import comb
    denom = comb(c, d)
    if denom == 0:
        return 0.0
    return comb(a, b) / denom


def mcnemar_test(results, cond_a="control", cond_b="cls-diag"):
    """McNemar's test comparing two conditions on paired instances.

    Returns (chi2, p_value, contingency_table).
    """
    from scipy.stats import chi2 as chi2_dist

    paired = defaultdict(lambda: {})
    for r in results:
        cond = r["condition"]
        iid = r["instance_id"]
        if cond in (cond_a, cond_b):
            # Use best-of-K (any resolved)
            if iid not in paired or cond not in paired[iid]:
                paired[iid][cond] = False
            if r.get("resolved", False):
                paired[iid][cond] = True

    a_only = 0  # cond_a resolves, cond_b doesn't
    b_only = 0  # cond_b resolves, cond_a doesn't
    both = 0
    neither = 0

    for iid, conds in paired.items():
        ra = conds.get(cond_a, False)
        rb = conds.get(cond_b, False)
        if ra and rb:
            both += 1
        elif ra and not rb:
            a_only += 1
        elif not ra and rb:
            b_only += 1
        else:
            neither += 1

    n_discord = a_only + b_only
    if n_discord == 0:
        return 0.0, 1.0, {"both": both, "neither": neither, "a_only": a_only, "b_only": b_only}

    chi2 = (abs(a_only - b_only) - 1) ** 2 / n_discord
    p_value = 1 - chi2_dist.cdf(chi2, df=1)

    return chi2, p_value, {"both": both, "neither": neither, "a_only": a_only, "b_only": b_only}


def clustered_bootstrap_ci(results, cond_a, cond_b, n_resamples=10000, seed=42):
    """Clustered bootstrap CI for Δ resolve rate (cond_b - cond_a).

    Clusters by instance_id. Returns (mean_delta, ci_lower, ci_upper).
    """
    rng = np.random.default_rng(seed)

    instance_resolve = defaultdict(lambda: defaultdict(bool))
    for r in results:
        if r.get("resolved", False):
            instance_resolve[r["instance_id"]][r["condition"]] = True

    instance_ids = list(instance_resolve.keys())
    n = len(instance_ids)
    if n == 0:
        return 0.0, 0.0, 0.0

    deltas = np.zeros(n_resamples)
    for b in range(n_resamples):
        idx = rng.choice(n, size=n, replace=True)
        ra = np.mean([instance_resolve[instance_ids[i]].get(cond_a, False) for i in idx])
        rb = np.mean([instance_resolve[instance_ids[i]].get(cond_b, False) for i in idx])
        deltas[b] = rb - ra

    return float(np.mean(deltas)), float(np.percentile(deltas, 2.5)), float(np.percentile(deltas, 97.5))


def stratify_by_cls_accuracy(results, cls_predictions):
    """Split results by CLS accuracy per instance.

    Returns {accuracy_bin: [results]}.
    """
    instance_cls_acc = defaultdict(list)
    for p in cls_predictions:
        correct = (p["cls_pred"] == p.get("gt_label"))
        instance_cls_acc[p["instance_id"]].append(correct)

    instance_acc = {
        iid: np.mean(corrects) for iid, corrects in instance_cls_acc.items()
    }

    bins = {"high_acc_ge90": [], "low_acc_lt90": []}
    for r in results:
        acc = instance_acc.get(r["instance_id"], 0.5)
        if acc >= 0.9:
            bins["high_acc_ge90"].append(r)
        else:
            bins["low_acc_lt90"].append(r)

    return bins


def cmd_analyze(args):
    log.info("=== Phase 4: Analyze results ===")
    results = load_jsonl(args.results)

    # Resolve rates
    rates = compute_resolve_rates(results)
    log.info("Resolve rates by condition:")
    for cond, m in rates.items():
        log.info(f"  {cond}: pass@1={m['pass_at_1']:.3f}, pass@5={m['pass_at_5']:.3f} (n={m['n_instances']})")

    # McNemar: control vs cls-diag
    chi2, p, table = mcnemar_test(results, "control", "cls-diag")
    log.info(f"McNemar control vs cls-diag: chi2={chi2:.3f}, p={p:.4f}, table={table}")

    # McNemar: control vs oracle-diag
    chi2_o, p_o, table_o = mcnemar_test(results, "control", "oracle-diag")
    log.info(f"McNemar control vs oracle-diag: chi2={chi2_o:.3f}, p={p_o:.4f}, table={table_o}")

    # Bootstrap CI
    delta_mean, ci_lo, ci_hi = clustered_bootstrap_ci(results, "control", "cls-diag")
    log.info(f"Bootstrap Δ(cls-diag − control): {delta_mean:.3f} [{ci_lo:.3f}, {ci_hi:.3f}]")

    delta_o_mean, ci_o_lo, ci_o_hi = clustered_bootstrap_ci(results, "control", "oracle-diag")
    log.info(f"Bootstrap Δ(oracle − control): {delta_o_mean:.3f} [{ci_o_lo:.3f}, {ci_o_hi:.3f}]")

    # Summary
    summary = {
        "resolve_rates": rates,
        "mcnemar_control_vs_cls": {"chi2": chi2, "p_value": p, "table": table},
        "mcnemar_control_vs_oracle": {"chi2": chi2_o, "p_value": p_o, "table": table_o},
        "bootstrap_cls_minus_control": {"mean": delta_mean, "ci_95": [ci_lo, ci_hi]},
        "bootstrap_oracle_minus_control": {"mean": delta_o_mean, "ci_95": [ci_o_lo, ci_o_hi]},
    }

    out_path = os.path.join(args.output_dir, "metrics_summary.json")
    os.makedirs(args.output_dir, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)
    log.info(f"Saved metrics summary to {out_path}")

    # Generate figure
    generate_resolve_rate_figure(rates, args.output_dir)


def generate_resolve_rate_figure(rates, output_dir):
    """Bar chart: resolve rate by condition."""
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
    except ImportError:
        log.warning("matplotlib not available, skipping figure generation")
        return

    conds = ["control", "cls-diag", "oracle-diag", "random-diag"]
    conds = [c for c in conds if c in rates]
    pass1 = [rates[c]["pass_at_1"] * 100 for c in conds]
    pass5 = [rates[c]["pass_at_5"] * 100 for c in conds]

    x = np.arange(len(conds))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 5))
    bars1 = ax.bar(x - width / 2, pass1, width, label="pass@1", color="#4C72B0")
    bars2 = ax.bar(x + width / 2, pass5, width, label="pass@5", color="#55A868")

    ax.set_ylabel("Resolve Rate (%)")
    ax.set_xlabel("Condition")
    ax.set_title("Re-Repair Resolve Rate by Diagnostic Condition")
    ax.set_xticks(x)
    ax.set_xticklabels(conds, rotation=15)
    ax.legend()
    ax.set_ylim(0, max(pass5 + pass1 + [10]) * 1.2)

    for bars in [bars1, bars2]:
        for bar in bars:
            h = bar.get_height()
            ax.annotate(f"{h:.1f}", xy=(bar.get_x() + bar.get_width() / 2, h),
                        xytext=(0, 3), textcoords="offset points", ha="center", fontsize=9)

    fig.tight_layout()
    out_path = os.path.join(output_dir, "fig_resolve_rate.pdf")
    fig.savefig(out_path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    log.info(f"Saved figure to {out_path}")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="Re-Repair Downstream Experiment")
    sub = parser.add_subparsers(dest="command", required=True)

    # prepare
    p_prep = sub.add_parser("prepare", help="Phase 1: prepare repair dataset")
    p_prep.add_argument("--swebench-predictions", required=True, help="Dir with agent prediction .jsonl files")
    p_prep.add_argument("--cls-checkpoint", required=True, help="Path to CLS LoRA checkpoint")
    p_prep.add_argument("--cls-base-model", default="Qwen/Qwen3-8B", help="CLS base model name")
    p_prep.add_argument("--output-dir", default="artifacts/re_repair")

    # generate
    p_gen = sub.add_parser("generate", help="Phase 2: generate repair patches")
    p_gen.add_argument("--data", required=True, help="repair_dataset.jsonl from Phase 1")
    p_gen.add_argument("--model", default="Qwen/Qwen3-8B-Instruct", help="Repair LLM")
    p_gen.add_argument("--conditions", nargs="+", default=CONDITIONS)
    p_gen.add_argument("--n-samples", type=int, default=10, help="Completions per (instance, condition)")
    p_gen.add_argument("--output-dir", default="artifacts/re_repair")

    # verify
    p_ver = sub.add_parser("verify", help="Phase 3: verify repairs via Docker")
    p_ver.add_argument("--repairs", required=True, help="generated_repairs.jsonl from Phase 2")
    p_ver.add_argument("--max-workers", type=int, default=4, help="Parallel Docker containers")
    p_ver.add_argument("--timeout", type=int, default=300, help="Per-instance timeout (seconds)")
    p_ver.add_argument("--output-dir", default="artifacts/re_repair")

    # analyze
    p_ana = sub.add_parser("analyze", help="Phase 4: analyze results")
    p_ana.add_argument("--results", required=True, help="verification_results.jsonl from Phase 3")
    p_ana.add_argument("--cls-predictions", default=None, help="CLS predictions for stratification")
    p_ana.add_argument("--output-dir", default="artifacts/re_repair")

    args = parser.parse_args()

    if args.command == "prepare":
        cmd_prepare(args)
    elif args.command == "generate":
        cmd_generate(args)
    elif args.command == "verify":
        cmd_verify(args)
    elif args.command == "analyze":
        cmd_analyze(args)


if __name__ == "__main__":
    main()
