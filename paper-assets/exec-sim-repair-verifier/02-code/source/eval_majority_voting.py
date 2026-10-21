#!/usr/bin/env python3
"""Per-test majority voting (K-pass self-consistency) evaluation."""

import argparse
import json
import logging
import os
import time
from collections import Counter

import torch
from peft import PeftModel
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
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


def run_inference(model, tokenizer, test_data, tmpl_kw, max_seq_length,
                  batch_size, temperature, do_sample, eos_ids, majority_class, device):
    """Run one pass of inference over all test data. Returns list of predictions."""
    y_pred = []
    n_unparseable = 0
    total = len(test_data)

    for i in range(0, total, batch_size):
        batch = test_data[i:i + batch_size]
        all_ids = []
        for ex in batch:
            ids = build_prompt_ids(tokenizer, ex["code"], ex["test"], tmpl_kw, max_seq_length)
            all_ids.append(ids)

        max_len = max(len(ids) for ids in all_ids)
        padded = []
        masks = []
        for ids in all_ids:
            pad_len = max_len - len(ids)
            padded.append([tokenizer.pad_token_id] * pad_len + ids)
            masks.append([0] * pad_len + [1] * len(ids))

        input_ids = torch.tensor(padded, device=device)
        attention_mask = torch.tensor(masks, device=device)

        gen_kwargs = dict(
            input_ids=input_ids,
            attention_mask=attention_mask,
            max_new_tokens=5,
            eos_token_id=eos_ids,
        )
        if do_sample:
            gen_kwargs.update(do_sample=True, temperature=temperature, top_p=0.9)
        else:
            gen_kwargs.update(do_sample=False)

        with torch.no_grad():
            outputs = model.generate(**gen_kwargs)

        for j in range(len(batch)):
            gen_ids = outputs[j][max_len:]
            gen_text = tokenizer.decode(gen_ids, skip_special_tokens=True)
            pred = parse_prediction(gen_text)
            if pred == -1:
                n_unparseable += 1
                pred = majority_class
            y_pred.append(pred)

    return y_pred, n_unparseable


def compute_metrics(y_true, y_pred, n_pass, n_fail, total, majority_baseline):
    acc = accuracy_score(y_true, y_pred)
    gap = acc - majority_baseline
    prec = precision_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)
    rec = recall_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)
    f1 = f1_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    return {
        "accuracy": round(acc * 100, 2),
        "accuracy_vs_baseline_gap_pp": round(gap * 100, 2),
        "per_class": {
            "FAIL": {"precision": round(float(prec[0]) * 100, 2), "recall": round(float(rec[0]) * 100, 2),
                      "f1": round(float(f1[0]) * 100, 2), "support": int(n_fail)},
            "PASS": {"precision": round(float(prec[1]) * 100, 2), "recall": round(float(rec[1]) * 100, 2),
                      "f1": round(float(f1[1]) * 100, 2), "support": int(n_pass)},
        },
        "confusion_matrix": {"tn": int(cm[0][0]), "fp": int(cm[0][1]), "fn": int(cm[1][0]), "tp": int(cm[1][1])},
        "unparseable": 0,
    }


def main():
    p = argparse.ArgumentParser(description="Per-test majority voting evaluation")
    p.add_argument("--base_model_path", required=True, help="Path to Qwen3-4B base model")
    p.add_argument("--checkpoint_path", required=True, help="Path to LoRA checkpoint")
    p.add_argument("--data_dir", required=True, help="Directory containing test.jsonl")
    p.add_argument("--output", default="eval_majority_voting.json")
    p.add_argument("--K", type=int, default=3, help="Number of sampled passes for majority voting")
    p.add_argument("--temperature", type=float, default=0.7)
    p.add_argument("--batch_size", type=int, default=16)
    p.add_argument("--max_seq_length", type=int, default=2048)
    p.add_argument("--gpu", type=int, default=0, help="GPU device index")
    args = p.parse_args()

    device = f"cuda:{args.gpu}"
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)
    device = "cuda:0"

    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_path, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tmpl_kw = detect_thinking_support(tokenizer)

    log.info(f"Loading base model: {args.base_model_path}")
    try:
        import flash_attn  # noqa: F401
        attn_impl = "flash_attention_2"
    except ImportError:
        attn_impl = "sdpa"

    base_model = AutoModelForCausalLM.from_pretrained(
        args.base_model_path,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        attn_implementation=attn_impl,
    )
    log.info(f"Loading adapter: {args.checkpoint_path}")
    model = PeftModel.from_pretrained(base_model, args.checkpoint_path)
    model.eval()
    model = model.to(device)

    eos_ids = [tokenizer.eos_token_id]
    im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
    if im_end_id is not None and im_end_id != tokenizer.unk_token_id:
        eos_ids.append(im_end_id)

    test_data = load_jsonl(os.path.join(args.data_dir, "test.jsonl"))
    total = len(test_data)
    y_true = [ex["label"] for ex in test_data]
    label_counts = Counter(y_true)
    n_pass, n_fail = label_counts.get(1, 0), label_counts.get(0, 0)
    majority_baseline = max(n_pass, n_fail) / total
    majority_class = 1 if n_pass >= n_fail else 0

    log.info(f"Test set: {total} examples, pass={n_pass}, fail={n_fail}")
    log.info(f"Majority baseline: {majority_baseline*100:.1f}%")

    # --- Single-pass greedy (baseline) ---
    log.info("=== Single-pass greedy (temperature=0) ===")
    t0 = time.time()
    y_greedy, n_unparse_greedy = run_inference(
        model, tokenizer, test_data, tmpl_kw, args.max_seq_length,
        args.batch_size, temperature=0, do_sample=False,
        eos_ids=eos_ids, majority_class=majority_class, device=device,
    )
    greedy_time = time.time() - t0
    greedy_acc = accuracy_score(y_true, y_greedy)
    log.info(f"Greedy accuracy: {greedy_acc*100:.2f}% ({greedy_time:.1f}s)")

    # --- K-pass sampling ---
    log.info(f"=== {args.K}-pass sampling (temperature={args.temperature}) ===")
    all_pass_preds = []
    t0 = time.time()
    for k in range(args.K):
        log.info(f"Pass {k+1}/{args.K}...")
        y_k, n_unparse_k = run_inference(
            model, tokenizer, test_data, tmpl_kw, args.max_seq_length,
            args.batch_size, temperature=args.temperature, do_sample=True,
            eos_ids=eos_ids, majority_class=majority_class, device=device,
        )
        all_pass_preds.append(y_k)
        acc_k = accuracy_score(y_true, y_k)
        log.info(f"  Pass {k+1} accuracy: {acc_k*100:.2f}%")
    sampling_time = time.time() - t0

    # --- Majority voting ---
    y_majority = []
    agreement_counts = Counter()
    for i in range(total):
        votes = [all_pass_preds[k][i] for k in range(args.K)]
        vote_counts = Counter(votes)
        winner = vote_counts.most_common(1)[0][0]
        max_agreement = vote_counts.most_common(1)[0][1]
        y_majority.append(winner)
        agreement_counts[f"{max_agreement}/{args.K}"] += 1

    majority_acc = accuracy_score(y_true, y_majority)
    improvement = majority_acc - greedy_acc
    log.info(f"Majority vote accuracy: {majority_acc*100:.2f}%")
    log.info(f"Improvement over greedy: {improvement*100:+.2f}pp")

    # Agreement distribution
    log.info("Agreement distribution:")
    for key in sorted(agreement_counts.keys(), reverse=True):
        cnt = agreement_counts[key]
        log.info(f"  {key}: {cnt} ({cnt/total*100:.1f}%)")

    # Compute detailed metrics
    greedy_metrics = compute_metrics(y_true, y_greedy, n_pass, n_fail, total, majority_baseline)
    greedy_metrics["unparseable"] = n_unparse_greedy
    majority_metrics = compute_metrics(y_true, y_majority, n_pass, n_fail, total, majority_baseline)

    # Per-pass accuracies
    per_pass_accs = [round(accuracy_score(y_true, all_pass_preds[k]) * 100, 2) for k in range(args.K)]

    # Where majority voting flipped the prediction
    flipped_correct = 0
    flipped_wrong = 0
    for i in range(total):
        if y_majority[i] != y_greedy[i]:
            if y_majority[i] == y_true[i]:
                flipped_correct += 1
            else:
                flipped_wrong += 1

    results = {
        "test_set_size": total,
        "K": args.K,
        "temperature": args.temperature,
        "class_balance": {"pass": n_pass, "fail": n_fail, "pass_pct": round(n_pass / total * 100, 1)},
        "majority_baseline_accuracy": round(majority_baseline * 100, 2),
        "single_pass_accuracy": greedy_metrics["accuracy"],
        "majority_vote_accuracy": majority_metrics["accuracy"],
        "improvement_pp": round(improvement * 100, 2),
        "agreement_distribution": {k: {"count": v, "pct": round(v / total * 100, 1)} for k, v in sorted(agreement_counts.items(), reverse=True)},
        "per_pass_accuracies": per_pass_accs,
        "flipped_correct": flipped_correct,
        "flipped_wrong": flipped_wrong,
        "net_flips": flipped_correct - flipped_wrong,
        "single_pass": greedy_metrics,
        "majority_vote": majority_metrics,
        "timing": {
            "greedy_seconds": round(greedy_time, 1),
            "sampling_seconds": round(sampling_time, 1),
            "total_seconds": round(greedy_time + sampling_time, 1),
        },
    }

    # --- Print report ---
    print("\n" + "=" * 60)
    print("MAJORITY VOTING REPORT: Per-test Self-Consistency (K=%d)" % args.K)
    print("=" * 60)
    print(f"\nTest set: {total} examples (pass={n_pass}, fail={n_fail})")
    print(f"Temperature: {args.temperature}, K={args.K}")
    print(f"\nSingle-pass (greedy): {greedy_metrics['accuracy']:.2f}%")
    print(f"Majority vote (K={args.K}):  {majority_metrics['accuracy']:.2f}%")
    print(f"Improvement:           {improvement*100:+.2f}pp")
    print(f"\nAgreement distribution:")
    for key in sorted(agreement_counts.keys(), reverse=True):
        cnt = agreement_counts[key]
        print(f"  {key} unanimous: {cnt} ({cnt/total*100:.1f}%)")
    print(f"\nFlipped predictions: {flipped_correct} correct, {flipped_wrong} wrong (net: {flipped_correct - flipped_wrong:+d})")
    print(f"\nPer-pass accuracies: {per_pass_accs}")
    print(f"\nPer-class (majority vote):")
    print(f"  {'Class':<8} {'Precision':>10} {'Recall':>10} {'F1':>10}")
    for cls in ["FAIL", "PASS"]:
        m = majority_metrics["per_class"][cls]
        print(f"  {cls:<8} {m['precision']:>9.1f}% {m['recall']:>9.1f}% {m['f1']:>9.1f}%")
    print(f"\nTiming: greedy={greedy_time:.0f}s, sampling={sampling_time:.0f}s, total={greedy_time+sampling_time:.0f}s")
    print("=" * 60)

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    log.info(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
