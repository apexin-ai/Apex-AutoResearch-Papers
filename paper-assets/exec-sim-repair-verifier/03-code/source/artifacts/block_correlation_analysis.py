# block_correlation_analysis.py — Verify that per-test classifier errors are
# block-correlated (within problem_id) rather than i.i.d.
# Computes: ICC, permutation test, all-correct/all-wrong rates, design effect.

import argparse
import json
import logging
import os
import sys
from collections import defaultdict

import numpy as np
import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a code verifier. Given a code snippet and a test case, "
    "predict whether the test will pass or fail."
)


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def detect_thinking_support(tokenizer):
    try:
        tokenizer.apply_chat_template(
            [{"role": "user", "content": "hi"}],
            tokenize=False,
            enable_thinking=False,
        )
        return {"enable_thinking": False}
    except TypeError:
        return {}


def build_prompt_ids(tokenizer, code, test, tmpl_kw, max_len):
    user_msg = f"## Code\n{code}\n\n## Test\n{test}\n\nWill this test pass or fail?"
    msgs = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
    ]
    ids = tokenizer.apply_chat_template(
        msgs, tokenize=True, add_generation_prompt=True, **tmpl_kw,
    )
    if len(ids) > max_len:
        ids = ids[:max_len]
    return ids


def parse_prediction(text):
    if "</think>" in text:
        text = text.split("</think>")[-1]
    text = text.strip().lower()
    if text.startswith("pass"):
        return 1
    if text.startswith("fail"):
        return 0
    if "pass" in text and "fail" not in text:
        return 1
    if "fail" in text and "pass" not in text:
        return 0
    return -1


def compute_icc(errors_by_group):
    """One-way random effects ICC for unbalanced groups."""
    groups = list(errors_by_group.values())
    K = len(groups)
    if K < 2:
        return float("nan")

    N = sum(len(g) for g in groups)
    grand_mean = sum(sum(g) for g in groups) / N

    ss_between = sum(len(g) * (np.mean(g) - grand_mean) ** 2 for g in groups)
    ss_within = sum(sum((x - np.mean(g)) ** 2 for x in g) for g in groups)

    ms_between = ss_between / (K - 1)
    ms_within = ss_within / (N - K)

    # Adjusted group size for unbalanced design
    n_sq_sum = sum(len(g) ** 2 for g in groups)
    k0 = (N - n_sq_sum / N) / (K - 1)

    if ms_between + (k0 - 1) * ms_within == 0:
        return 0.0

    icc = (ms_between - ms_within) / (ms_between + (k0 - 1) * ms_within)
    return float(icc)


def permutation_test_icc(errors, problem_ids, n_permutations=2000):
    """Permutation test: shuffle problem_id assignments, recompute ICC."""
    observed_groups = defaultdict(list)
    for e, pid in zip(errors, problem_ids):
        observed_groups[pid].append(e)
    observed_icc = compute_icc(observed_groups)

    rng = np.random.default_rng(42)
    shuffled_iccs = []
    pid_array = np.array(problem_ids)

    for _ in range(n_permutations):
        shuffled_pids = rng.permutation(pid_array)
        shuffled_groups = defaultdict(list)
        for e, pid in zip(errors, shuffled_pids):
            shuffled_groups[pid].append(e)
        shuffled_iccs.append(compute_icc(shuffled_groups))

    shuffled_iccs = np.array(shuffled_iccs)
    p_value = float(np.mean(shuffled_iccs >= observed_icc))

    return {
        "observed_icc": round(observed_icc, 6),
        "shuffle_mean": round(float(np.mean(shuffled_iccs)), 6),
        "shuffle_std": round(float(np.std(shuffled_iccs)), 6),
        "shuffle_p95": round(float(np.percentile(shuffled_iccs, 95)), 6),
        "shuffle_p99": round(float(np.percentile(shuffled_iccs, 99)), 6),
        "p_value": round(p_value, 6),
        "n_permutations": n_permutations,
    }


def compute_block_stats(errors_by_group, overall_error_rate):
    """Per-problem all-correct/all-wrong rates vs independence expectation."""
    n_groups = len(errors_by_group)
    n_all_correct = 0
    n_all_wrong = 0
    expected_all_correct = 0.0
    expected_all_wrong = 0.0

    per_problem = []
    for pid, errs in errors_by_group.items():
        k = len(errs)
        err_rate = np.mean(errs)
        n_errors = sum(errs)

        all_correct = int(n_errors == 0)
        all_wrong = int(n_errors == k)
        n_all_correct += all_correct
        n_all_wrong += all_wrong

        # Under i.i.d. assumption with global error rate
        exp_ac = (1 - overall_error_rate) ** k
        exp_aw = overall_error_rate ** k
        expected_all_correct += exp_ac
        expected_all_wrong += exp_aw

        per_problem.append({
            "problem_id": pid,
            "n_tests": k,
            "n_errors": n_errors,
            "error_rate": round(float(err_rate), 4),
            "all_correct": bool(all_correct),
            "all_wrong": bool(all_wrong),
        })

    return {
        "n_groups": n_groups,
        "observed_all_correct": n_all_correct,
        "observed_all_wrong": n_all_wrong,
        "expected_all_correct_iid": round(expected_all_correct, 2),
        "expected_all_wrong_iid": round(expected_all_wrong, 2),
        "ratio_all_correct": round(n_all_correct / max(expected_all_correct, 1e-9), 2),
        "ratio_all_wrong": round(n_all_wrong / max(expected_all_wrong, 1e-9), 2),
        "per_problem": sorted(per_problem, key=lambda x: x["problem_id"]),
    }


def compute_design_effect(errors_by_group):
    """Design effect (DEFF) = 1 + (k0-1)*ICC. DEFF>1 means block correlation inflates variance."""
    icc = compute_icc(errors_by_group)
    groups = list(errors_by_group.values())
    N = sum(len(g) for g in groups)
    K = len(groups)
    n_sq_sum = sum(len(g) ** 2 for g in groups)
    k0 = (N - n_sq_sum / N) / (K - 1)
    deff = 1 + (k0 - 1) * icc
    return {"design_effect": round(deff, 4), "avg_cluster_size_k0": round(k0, 2), "icc": round(icc, 6)}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--data_dir", required=True)
    p.add_argument("--checkpoint_dir", required=True)
    p.add_argument("--model_name", default="Qwen/Qwen3-4B")
    p.add_argument("--output", default="block_corr_results.json")
    p.add_argument("--batch_size", type=int, default=16)
    p.add_argument("--max_seq_length", type=int, default=2048)
    p.add_argument("--n_permutations", type=int, default=2000)
    args = p.parse_args()

    # --- Load model (same as eval_verifier.py) ---
    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_dir, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tmpl_kw = detect_thinking_support(tokenizer)

    log.info(f"Loading base model: {args.model_name}")
    try:
        import flash_attn  # noqa: F401
        attn_impl = "flash_attention_2"
    except ImportError:
        attn_impl = "sdpa"

    base_model = AutoModelForCausalLM.from_pretrained(
        args.model_name,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        attn_implementation=attn_impl,
    )
    log.info(f"Loading adapter: {args.checkpoint_dir}")
    model = PeftModel.from_pretrained(base_model, args.checkpoint_dir)
    model.eval()
    model = model.cuda()

    # --- Stop tokens ---
    eos_ids = [tokenizer.eos_token_id]
    im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
    if im_end_id is not None and isinstance(im_end_id, int) and im_end_id != tokenizer.unk_token_id:
        eos_ids.append(im_end_id)

    # --- Load test data ---
    test_data = load_jsonl(os.path.join(args.data_dir, "test.jsonl"))
    log.info(f"Test set: {len(test_data)} examples")

    # --- Run inference ---
    all_errors = []
    all_pids = []
    n_unparseable = 0
    majority_class = 1  # fallback

    for i in range(0, len(test_data), args.batch_size):
        batch = test_data[i : i + args.batch_size]
        batch_ids = [
            build_prompt_ids(tokenizer, ex["code"], ex["test"], tmpl_kw, args.max_seq_length)
            for ex in batch
        ]
        batch_labels = [ex["label"] for ex in batch]
        batch_pids = [ex["problem_id"] for ex in batch]

        max_len = max(len(ids) for ids in batch_ids)
        padded = [
            [tokenizer.pad_token_id] * (max_len - len(ids)) + ids for ids in batch_ids
        ]
        masks = [[0] * (max_len - len(ids)) + [1] * len(ids) for ids in batch_ids]

        input_ids = torch.tensor(padded, device="cuda")
        attention_mask = torch.tensor(masks, device="cuda")

        with torch.no_grad():
            outputs = model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_new_tokens=10,
                do_sample=False,
                eos_token_id=eos_ids,
            )

        for j in range(len(batch)):
            gen_ids = outputs[j][max_len:]
            gen_text = tokenizer.decode(gen_ids, skip_special_tokens=True)
            pred = parse_prediction(gen_text)

            if pred == -1:
                n_unparseable += 1
                pred = majority_class

            error = int(pred != batch_labels[j])
            all_errors.append(error)
            all_pids.append(batch_pids[j])

        done = min(i + args.batch_size, len(test_data))
        if done % (args.batch_size * 10) == 0 or done == len(test_data):
            log.info(f"Inference progress: {done}/{len(test_data)}")

    # --- Group errors by problem_id ---
    errors_by_group = defaultdict(list)
    for e, pid in zip(all_errors, all_pids):
        errors_by_group[pid].append(e)

    overall_error_rate = np.mean(all_errors)
    log.info(f"Overall error rate: {overall_error_rate:.4f} ({sum(all_errors)}/{len(all_errors)})")

    # --- Compute statistics ---
    log.info("Computing ICC and permutation test...")
    perm_results = permutation_test_icc(all_errors, all_pids, args.n_permutations)

    log.info("Computing block stats (all-correct / all-wrong rates)...")
    block_stats = compute_block_stats(errors_by_group, overall_error_rate)

    log.info("Computing design effect...")
    deff_results = compute_design_effect(errors_by_group)

    # --- Error rate distribution across problems ---
    group_error_rates = [np.mean(errs) for errs in errors_by_group.values()]
    error_rate_dist = {
        "mean": round(float(np.mean(group_error_rates)), 4),
        "std": round(float(np.std(group_error_rates)), 4),
        "min": round(float(np.min(group_error_rates)), 4),
        "max": round(float(np.max(group_error_rates)), 4),
        "q25": round(float(np.percentile(group_error_rates, 25)), 4),
        "q50": round(float(np.percentile(group_error_rates, 50)), 4),
        "q75": round(float(np.percentile(group_error_rates, 75)), 4),
        # Under i.i.d., std of group means ≈ sqrt(p*(1-p)/k).
        # If observed std >> expected, that's evidence of block correlation.
        "expected_std_iid": round(float(np.sqrt(overall_error_rate * (1 - overall_error_rate) / np.mean([len(g) for g in errors_by_group.values()]))), 4),
    }

    results = {
        "summary": {
            "n_samples": len(all_errors),
            "n_problems": len(errors_by_group),
            "overall_error_rate": round(float(overall_error_rate), 4),
            "unparseable_predictions": n_unparseable,
        },
        "icc_permutation_test": perm_results,
        "design_effect": deff_results,
        "block_stats": {k: v for k, v in block_stats.items() if k != "per_problem"},
        "error_rate_distribution": error_rate_dist,
        "per_problem_detail": block_stats["per_problem"],
    }

    # --- Conclusion ---
    icc = perm_results["observed_icc"]
    p_val = perm_results["p_value"]
    deff = deff_results["design_effect"]
    obs_ac = block_stats["observed_all_correct"]
    exp_ac = block_stats["expected_all_correct_iid"]
    obs_aw = block_stats["observed_all_wrong"]
    exp_aw = block_stats["expected_all_wrong_iid"]

    block_correlated = icc > 0 and p_val < 0.05
    results["conclusion"] = {
        "block_correlated": block_correlated,
        "icc": round(icc, 4),
        "icc_p_value": p_val,
        "design_effect": deff,
        "all_correct_ratio_vs_iid": block_stats["ratio_all_correct"],
        "all_wrong_ratio_vs_iid": block_stats["ratio_all_wrong"],
        "interpretation": (
            f"ICC={icc:.4f} (p={p_val:.4f}), DEFF={deff:.2f}. "
            f"All-correct: {obs_ac} observed vs {exp_ac:.1f} expected under i.i.d. (ratio={block_stats['ratio_all_correct']:.1f}x). "
            f"All-wrong: {obs_aw} observed vs {exp_aw:.1f} expected (ratio={block_stats['ratio_all_wrong']:.1f}x). "
            f"Error rate std across problems: {error_rate_dist['std']:.4f} vs {error_rate_dist['expected_std_iid']:.4f} expected under i.i.d. "
            + ("=> Strong evidence of block correlation." if block_correlated else "=> No significant block correlation detected.")
        ),
    }

    # --- Print report ---
    print("\n" + "=" * 70)
    print("BLOCK CORRELATION ANALYSIS REPORT")
    print("=" * 70)
    print(f"\nTest set: {len(all_errors)} samples, {len(errors_by_group)} problems")
    print(f"Overall error rate: {overall_error_rate:.4f}")
    print(f"\n--- ICC (Intra-class Correlation Coefficient) ---")
    print(f"  Observed ICC:     {icc:.6f}")
    print(f"  Shuffle mean:     {perm_results['shuffle_mean']:.6f}")
    print(f"  Shuffle p95:      {perm_results['shuffle_p95']:.6f}")
    print(f"  p-value:          {p_val:.4f}")
    print(f"  Significant:      {'YES' if p_val < 0.05 else 'NO'} (alpha=0.05)")
    print(f"\n--- Design Effect ---")
    print(f"  DEFF:             {deff:.4f}")
    print(f"  Avg cluster k0:   {deff_results['avg_cluster_size_k0']:.2f}")
    print(f"\n--- All-Correct / All-Wrong Rates ---")
    print(f"  All-correct: {obs_ac} observed vs {exp_ac:.1f} expected (ratio={block_stats['ratio_all_correct']:.1f}x)")
    print(f"  All-wrong:   {obs_aw} observed vs {exp_aw:.1f} expected (ratio={block_stats['ratio_all_wrong']:.1f}x)")
    print(f"\n--- Error Rate Distribution Across Problems ---")
    print(f"  Observed std: {error_rate_dist['std']:.4f}")
    print(f"  Expected std (i.i.d.): {error_rate_dist['expected_std_iid']:.4f}")
    print(f"  Ratio: {error_rate_dist['std'] / max(error_rate_dist['expected_std_iid'], 1e-9):.2f}x")
    print(f"\n--- Conclusion ---")
    print(f"  {'BLOCK-CORRELATED' if block_correlated else 'NOT SIGNIFICANTLY BLOCK-CORRELATED'}")
    print("=" * 70)

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    log.info(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
