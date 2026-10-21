#!/usr/bin/env python3
"""eval_cwm_constrained.py — Constrained decoding for CWM models via vLLM.

Forces CWM model to output in valid format using vLLM's structured output.
Two modes:
  1. choice: Force output to exactly "PASS" or "FAIL" (binary classification)
  2. regex:  Force output to match "PASS: ..." or "FAIL: ..." pattern

Requires: vLLM 0.18+, merged LoRA checkpoint (use merge_lora.py first).

Usage:
  # Step 1: Merge LoRA into base model
  python merge_lora.py --base Qwen/Qwen3-8B --adapter <ckpt> --output <merged_dir>

  # Step 2: Run constrained decoding
  python eval_cwm_constrained.py \
    --model_path <merged_dir> \
    --data_path data/swebench_full/swebench_test.jsonl \
    --mode choice \
    --output_dir /root/autodl-tmp/eval_results/cwm_8b_constrained/
"""

import argparse
import json
import logging
import os
import time
from collections import Counter

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a code execution simulator. Given a code patch (git diff) and a test name, "
    "predict the execution result when the test is run against the patched code."
)
USER_TEMPLATE = "## Patch (git diff)\n{code}\n\n## Test\n{test}\n\nWhat is the execution result?"


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(data, path):
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")


def build_prompt(tokenizer, code, test):
    user_msg = USER_TEMPLATE.format(code=code, test=test)
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
    ]
    try:
        text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
            enable_thinking=False,
        )
    except TypeError:
        text = tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True,
        )
    return text


def extract_verdict(text: str) -> int:
    text = text.strip().upper()
    if text.startswith("PASS"):
        return 1
    if text.startswith("FAIL"):
        return 0
    return -1


def main():
    p = argparse.ArgumentParser(description="Constrained decoding CWM eval via vLLM")
    p.add_argument("--model_path", required=True,
                   help="Path to merged model (base + LoRA merged)")
    p.add_argument("--data_path", required=True,
                   help="Test data JSONL with code, test, label fields")
    p.add_argument("--mode", choices=["choice", "regex"], default="choice",
                   help="Constrained decoding mode")
    p.add_argument("--output_dir", required=True)
    p.add_argument("--max_model_len", type=int, default=4096)
    p.add_argument("--max_new_tokens", type=int, default=64)
    p.add_argument("--tensor_parallel_size", type=int, default=1)
    p.add_argument("--batch_size", type=int, default=256,
                   help="Number of prompts per vLLM.generate() call")
    p.add_argument("--limit", type=int, default=None,
                   help="Limit number of test samples (for debugging)")
    args = p.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    if args.mode == "choice":
        structured = StructuredOutputsParams(choice=["PASS", "FAIL"])
        max_tokens = 5
    else:
        structured = StructuredOutputsParams(
            regex=r"(PASS: [^\n]{1,200}|FAIL: [^\n]{1,200})"
        )
        max_tokens = args.max_new_tokens

    sampling_params = SamplingParams(
        max_tokens=max_tokens,
        temperature=0,
        structured_outputs=structured,
    )

    log.info(f"Loading model: {args.model_path}")
    llm = LLM(
        model=args.model_path,
        max_model_len=args.max_model_len,
        tensor_parallel_size=args.tensor_parallel_size,
        trust_remote_code=True,
        dtype="bfloat16",
        gpu_memory_utilization=0.90,
    )
    tokenizer = llm.get_tokenizer()

    log.info(f"Loading test data: {args.data_path}")
    test_data = load_jsonl(args.data_path)
    if args.limit:
        test_data = test_data[:args.limit]
    log.info(f"Test set: {len(test_data)} samples")

    labels = [ex["label"] for ex in test_data]
    label_counts = Counter(labels)
    majority = 1 if label_counts.get(1, 0) >= label_counts.get(0, 0) else 0
    log.info(f"Labels: pass={label_counts.get(1,0)}, fail={label_counts.get(0,0)}, majority={majority}")

    prompts = []
    for ex in test_data:
        prompts.append(build_prompt(tokenizer, ex["code"], ex["test"]))

    log.info(f"Running inference with mode={args.mode}...")
    t0 = time.time()

    all_outputs = []
    for i in range(0, len(prompts), args.batch_size):
        batch = prompts[i:i + args.batch_size]
        outputs = llm.generate(batch, sampling_params)
        all_outputs.extend(outputs)
        done = min(i + args.batch_size, len(prompts))
        log.info(f"Progress: {done}/{len(prompts)}")

    elapsed = time.time() - t0
    log.info(f"Inference done in {elapsed:.1f}s ({len(prompts)/elapsed:.1f} samples/s)")

    results = []
    y_true, y_pred = [], []
    n_unparseable = 0

    for idx, (ex, output) in enumerate(zip(test_data, all_outputs)):
        gen_text = output.outputs[0].text
        pred = extract_verdict(gen_text)
        if pred == -1:
            n_unparseable += 1
            pred = majority

        correct = int(pred == ex["label"])
        y_true.append(ex["label"])
        y_pred.append(pred)

        pid = ex.get("problem_id", ex.get("metadata", {}).get("instance_id", f"idx_{idx}"))
        results.append({
            "index": idx,
            "problem_id": pid,
            "label": ex["label"],
            "pred": pred,
            "correct": correct,
            "gen_text": gen_text,
            "unparseable": pred == -1,
            "mutation_type": ex.get("mutation_type", "unknown"),
        })

    from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
    acc = accuracy_score(y_true, y_pred)
    f1_macro = f1_score(y_true, y_pred, average="macro")
    f1_per = f1_score(y_true, y_pred, average=None, labels=[0, 1])
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    maj_baseline = max(label_counts.values()) / len(labels)

    print("\n" + "=" * 60)
    print(f"CONSTRAINED DECODING RESULTS (mode={args.mode})")
    print("=" * 60)
    print(f"  Samples:           {len(labels)}")
    print(f"  Unparseable:       {n_unparseable} ({n_unparseable/len(labels)*100:.1f}%)")
    print(f"  Majority baseline: {maj_baseline*100:.1f}%")
    print(f"  Accuracy:          {acc*100:.1f}%")
    print(f"  Gap vs majority:   {(acc-maj_baseline)*100:+.1f}pp")
    print(f"  F1 macro:          {f1_macro*100:.1f}%")
    print(f"  F1 fail/pass:      {f1_per[0]*100:.1f}% / {f1_per[1]*100:.1f}%")
    print(f"\n  Confusion Matrix:")
    print(f"              Pred=Fail  Pred=Pass")
    print(f"  GT=Fail     {cm[0][0]:>8}   {cm[0][1]:>8}")
    print(f"  GT=Pass     {cm[1][0]:>8}   {cm[1][1]:>8}")
    print(f"\n  Inference time: {elapsed:.1f}s")
    print("=" * 60)

    pred_path = os.path.join(args.output_dir, f"constrained_{args.mode}_predictions.jsonl")
    save_jsonl(results, pred_path)

    summary = {
        "mode": args.mode,
        "model_path": args.model_path,
        "data_path": args.data_path,
        "n_samples": len(labels),
        "n_unparseable": n_unparseable,
        "accuracy": round(acc * 100, 2),
        "majority_baseline": round(maj_baseline * 100, 2),
        "gap_pp": round((acc - maj_baseline) * 100, 2),
        "f1_macro": round(f1_macro * 100, 2),
        "f1_fail": round(f1_per[0] * 100, 2),
        "f1_pass": round(f1_per[1] * 100, 2),
        "confusion_matrix": {"tn": int(cm[0][0]), "fp": int(cm[0][1]),
                             "fn": int(cm[1][0]), "tp": int(cm[1][1])},
        "inference_time_s": round(elapsed, 1),
    }
    summary_path = os.path.join(args.output_dir, f"constrained_{args.mode}_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)

    log.info(f"Predictions: {pred_path}")
    log.info(f"Summary: {summary_path}")


if __name__ == "__main__":
    main()
