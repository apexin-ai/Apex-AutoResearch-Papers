#!/usr/bin/env python3
"""0-shot and 3-shot CLS baseline for Qwen3-14B on function-level test set.

Usage:
  # 0-shot
  python eval_14b_baseline.py --model_path /dev/shm/Qwen3-14B --num_shots 0 --device cuda:0

  # 3-shot
  python eval_14b_baseline.py --model_path /dev/shm/Qwen3-14B --num_shots 3 --device cuda:0
"""

import argparse
import json
import logging
import os
import random
import time
from collections import Counter

import torch
from sklearn.metrics import accuracy_score, confusion_matrix, f1_score
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a code verifier. Given a code patch (git diff) and a test name, "
    "predict whether the test will pass or fail when run against the patched code. "
    "Answer with exactly one word: PASS or FAIL."
)
USER_TEMPLATE = "## Code\n{code}\n\n## Test\n{test}\n\nWill this test pass or fail?"
LABEL_MAP = {1: "PASS", 0: "FAIL"}


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def select_demonstrations(train_data, num_shots, seed=42):
    rng = random.Random(seed)
    pass_ex = [ex for ex in train_data if ex["label"] == 1]
    fail_ex = [ex for ex in train_data if ex["label"] == 0]
    pass_ex.sort(key=lambda x: len(x["code"]))
    fail_ex.sort(key=lambda x: len(x["code"]))
    short_pass = pass_ex[:200]
    short_fail = fail_ex[:200]
    n_fail = num_shots // 2 + (num_shots % 2)  # 2 fail for 3-shot
    n_pass = num_shots - n_fail                 # 1 pass for 3-shot
    demos = []
    demos.extend(rng.sample(short_fail, min(n_fail, len(short_fail))))
    demos.extend(rng.sample(short_pass, min(n_pass, len(short_pass))))
    rng.shuffle(demos)
    return demos


def detect_thinking_support(tokenizer):
    try:
        tokenizer.apply_chat_template(
            [{"role": "user", "content": "hi"}],
            tokenize=False, enable_thinking=False,
        )
        return {"enable_thinking": False}
    except TypeError:
        return {}


def build_messages(demos, query_ex):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for demo in demos:
        messages.append({"role": "user", "content": USER_TEMPLATE.format(code=demo["code"], test=demo["test"])})
        messages.append({"role": "assistant", "content": LABEL_MAP[demo["label"]]})
    messages.append({"role": "user", "content": USER_TEMPLATE.format(code=query_ex["code"], test=query_ex["test"])})
    return messages


def build_prompt_ids(tokenizer, messages, tmpl_kw, max_len):
    ids = tokenizer.apply_chat_template(
        messages, tokenize=True, add_generation_prompt=True, **tmpl_kw,
    )
    if hasattr(ids, "input_ids"):
        ids = ids.input_ids
    ids = list(ids) if not isinstance(ids, list) else ids
    truncated = False
    if len(ids) > max_len:
        ids = ids[:max_len]
        truncated = True
    return ids, truncated


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


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model_path", default="/dev/shm/Qwen3-14B")
    p.add_argument("--data_dir", default="/home/sonny/exec-sim-repair-verifier/data")
    p.add_argument("--num_shots", type=int, default=0, choices=[0, 3])
    p.add_argument("--device", default="cuda:0")
    p.add_argument("--batch_size", type=int, default=32)
    p.add_argument("--max_seq_length", type=int, default=4096)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--output", default=None)
    args = p.parse_args()

    if args.output is None:
        args.output = f"/home/sonny/exec-sim-repair-verifier/results_14b_{args.num_shots}shot.json"

    log.info(f"Model: {args.model_path}, shots: {args.num_shots}, device: {args.device}")

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    tokenizer = AutoTokenizer.from_pretrained(
        args.model_path, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    tmpl_kw = detect_thinking_support(tokenizer)
    log.info(f"Template kwargs: {tmpl_kw}")

    try:
        import flash_attn  # noqa: F401
        attn_impl = "flash_attention_2"
    except ImportError:
        attn_impl = "sdpa"
    log.info(f"Attention: {attn_impl}")

    model = AutoModelForCausalLM.from_pretrained(
        args.model_path,
        quantization_config=bnb_config,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        attn_implementation=attn_impl,
        device_map=args.device,
    )
    model.eval()
    if hasattr(model, "generation_config"):
        model.generation_config.enable_thinking = False

    test_data = load_jsonl(f"{args.data_dir}/test.jsonl")
    log.info(f"Test set: {len(test_data)} instances")

    demos = []
    if args.num_shots > 0:
        train_data = load_jsonl(f"{args.data_dir}/train.jsonl")
        demos = select_demonstrations(train_data, args.num_shots, args.seed)
        log.info(f"Selected {len(demos)} demonstrations: {[LABEL_MAP[d['label']] for d in demos]}")

    eos_ids = [tokenizer.eos_token_id]
    for tok_str in ["<|im_end|>", "<|endoftext|>"]:
        tid = tokenizer.convert_tokens_to_ids(tok_str)
        if tid != tokenizer.unk_token_id and tid not in eos_ids:
            eos_ids.append(tid)

    log.info("Building prompts...")
    all_ids = []
    n_truncated = 0
    for ex in test_data:
        messages = build_messages(demos, ex)
        ids, trunc = build_prompt_ids(tokenizer, messages, tmpl_kw, args.max_seq_length)
        all_ids.append(ids)
        if trunc:
            n_truncated += 1
    log.info(f"Prompts built. Truncated: {n_truncated}/{len(test_data)}")

    predictions = [None] * len(test_data)
    raw_outputs = [None] * len(test_data)
    bs = args.batch_size
    total_batches = (len(test_data) + bs - 1) // bs
    t0 = time.time()

    for batch_idx in range(total_batches):
        start = batch_idx * bs
        end = min(start + bs, len(test_data))
        batch_ids = all_ids[start:end]

        max_len_batch = max(len(ids) for ids in batch_ids)
        input_ids = torch.full((len(batch_ids), max_len_batch), tokenizer.pad_token_id, dtype=torch.long)
        attention_mask = torch.zeros((len(batch_ids), max_len_batch), dtype=torch.long)

        for i, ids in enumerate(batch_ids):
            offset = max_len_batch - len(ids)
            input_ids[i, offset:] = torch.tensor(ids, dtype=torch.long)
            attention_mask[i, offset:] = 1

        input_ids = input_ids.to(args.device)
        attention_mask = attention_mask.to(args.device)

        with torch.no_grad():
            out = model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_new_tokens=8,
                do_sample=False,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=eos_ids,
            )

        for i in range(len(batch_ids)):
            gen_ids = out[i, input_ids.shape[1]:]
            text = tokenizer.decode(gen_ids, skip_special_tokens=True)
            pred = parse_prediction(text)
            predictions[start + i] = pred
            raw_outputs[start + i] = text.strip()

        if (batch_idx + 1) % 10 == 0 or batch_idx == total_batches - 1:
            elapsed = time.time() - t0
            done = end
            rate = done / elapsed if elapsed > 0 else 0
            eta = (len(test_data) - done) / rate if rate > 0 else 0
            log.info(f"Batch {batch_idx+1}/{total_batches} | {done}/{len(test_data)} | "
                     f"{rate:.1f} ex/s | ETA {eta:.0f}s")

    elapsed_total = time.time() - t0

    y_true = [ex["label"] for ex in test_data]
    y_pred = [p if p != -1 else 0 for p in predictions]  # unparseable → fail
    n_unparseable = sum(1 for p in predictions if p == -1)

    acc = accuracy_score(y_true, y_pred)
    f1_per = f1_score(y_true, y_pred, average=None, labels=[0, 1])
    f1_macro = f1_score(y_true, y_pred, average="macro")
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])

    label_counts = Counter(y_true)
    majority_baseline = max(label_counts.values()) / len(y_true)

    print("\n" + "=" * 60)
    model_name = os.path.basename(args.model_path.rstrip("/"))
    print(f"{model_name.upper()} {args.num_shots}-SHOT CLS BASELINE (function-level)")
    print("=" * 60)
    print(f"Test set: {len(test_data)} instances")
    print(f"Class balance: pass={label_counts[1]} ({label_counts[1]/len(test_data)*100:.1f}%), "
          f"fail={label_counts[0]} ({label_counts[0]/len(test_data)*100:.1f}%)")
    print(f"Majority baseline: {majority_baseline*100:.1f}%")
    print(f"\nPer-test accuracy: {acc*100:.2f}%")
    print(f"Gap vs majority:   {(acc - majority_baseline)*100:+.2f}pp")
    print(f"F1 (fail):  {f1_per[0]*100:.2f}%")
    print(f"F1 (pass):  {f1_per[1]*100:.2f}%")
    print(f"F1 (macro): {f1_macro*100:.2f}%")
    print(f"\nConfusion matrix:")
    print(f"              Predicted")
    print(f"              fail    pass")
    print(f"  Actual fail  {cm[0][0]:>5}   {cm[0][1]:>5}")
    print(f"  Actual pass  {cm[1][0]:>5}   {cm[1][1]:>5}")
    print(f"\nUnparseable: {n_unparseable}")
    print(f"Truncated: {n_truncated}")
    print(f"Elapsed: {elapsed_total:.1f}s ({len(test_data)/elapsed_total:.1f} ex/s)")
    print("=" * 60)

    results = {
        "model": args.model_path,
        "method": f"{args.num_shots}-shot",
        "quantization": "NF4",
        "dataset": "function-level",
        "n_instances": len(test_data),
        "class_balance": {"pass": label_counts[1], "fail": label_counts[0]},
        "majority_baseline": round(majority_baseline * 100, 2),
        "per_test_accuracy": round(acc * 100, 2),
        "gap_vs_majority_pp": round((acc - majority_baseline) * 100, 2),
        "f1_fail": round(f1_per[0] * 100, 2),
        "f1_pass": round(f1_per[1] * 100, 2),
        "f1_macro": round(f1_macro * 100, 2),
        "confusion_matrix": {
            "tn": int(cm[0][0]), "fp": int(cm[0][1]),
            "fn": int(cm[1][0]), "tp": int(cm[1][1]),
        },
        "n_unparseable": n_unparseable,
        "n_truncated": n_truncated,
        "elapsed_seconds": round(elapsed_total, 1),
        "config": {
            "batch_size": args.batch_size,
            "max_seq_length": args.max_seq_length,
            "num_shots": args.num_shots,
            "seed": args.seed,
        },
    }

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    log.info(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
