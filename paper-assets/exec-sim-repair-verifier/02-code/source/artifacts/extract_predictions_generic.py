#!/usr/bin/env python3
"""extract_predictions_generic.py — Extract per-sample predictions from any CLS or CWM checkpoint.

Loads a LoRA checkpoint, runs inference on the test set, and saves predictions as JSONL.

Usage:
  # CLS model
  python3 extract_predictions_generic.py \
    --mode cls \
    --checkpoint checkpoints/best \
    --base-model /root/.cache/huggingface/hub/Qwen/Qwen3-4B \
    --test-data data/test.jsonl \
    --output predictions_cls_seed42.jsonl

  # CWM model
  python3 extract_predictions_generic.py \
    --mode cwm \
    --checkpoint checkpoints_cwm_seed123/best \
    --base-model /root/.cache/huggingface/hub/Qwen/Qwen3-4B \
    --test-data data/cwm_test.jsonl \
    --output predictions_cwm_seed123.jsonl

Output JSONL fields: {index, problem_id, mutation_type, label, pred, gen_text}
"""

import argparse
import json
import logging
import os
from collections import Counter

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

CLS_SYSTEM = ("You are a code verifier. Given a code snippet and a test case, "
              "predict whether the test will pass or fail.")
CWM_SYSTEM = ("You are a code execution simulator. Given a code snippet and a test case, "
              "predict the execution result.")

BATCH_SIZE = 8
MAX_LEN = 2048


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def detect_thinking_support(tokenizer):
    try:
        tokenizer.apply_chat_template(
            [{"role": "user", "content": "hi"}], tokenize=False, enable_thinking=False)
        return {"enable_thinking": False}
    except TypeError:
        return {}


def build_ids(tokenizer, item, mode, tmpl_kw):
    if mode == "cls":
        user_msg = f"## Code\n{item['code']}\n\n## Test\n{item['test']}\n\nWill this test pass or fail?"
        system = CLS_SYSTEM
    else:
        user_msg = f"## Code\n{item['code']}\n\n## Test\n{item['test']}\n\nWhat is the execution result?"
        system = CWM_SYSTEM

    msgs = [{"role": "system", "content": system}, {"role": "user", "content": user_msg}]
    result = tokenizer.apply_chat_template(msgs, tokenize=True, add_generation_prompt=True, **tmpl_kw)
    if hasattr(result, "input_ids"):
        ids = result.input_ids[0] if hasattr(result.input_ids[0], "__len__") else result.input_ids
        ids = list(ids)
    elif isinstance(result, list):
        ids = result[0] if len(result) > 0 and isinstance(result[0], list) else result
    else:
        ids = list(result)
    return ids[:MAX_LEN] if len(ids) > MAX_LEN else ids


def parse_pred(text):
    if "</think>" in text:
        text = text.split("</think>")[-1]
    t = text.strip().lower()
    if t.startswith("pass"):
        return 1
    if t.startswith("fail"):
        return 0
    if "pass" in t and "fail" not in t:
        return 1
    if "fail" in t and "pass" not in t:
        return 0
    return -1


def main():
    ap = argparse.ArgumentParser(description="Extract predictions from CLS/CWM checkpoint")
    ap.add_argument("--mode", choices=["cls", "cwm"], required=True)
    ap.add_argument("--checkpoint", required=True, help="Path to LoRA adapter (best/ dir)")
    ap.add_argument("--base-model", required=True, help="Path to base model")
    ap.add_argument("--test-data", required=True, help="Path to test JSONL")
    ap.add_argument("--output", required=True, help="Output predictions JSONL")
    ap.add_argument("--device", default="cuda:0")
    ap.add_argument("--batch-size", type=int, default=BATCH_SIZE)
    args = ap.parse_args()

    if os.path.exists(args.output):
        log.info(f"Skip — {args.output} already exists")
        return

    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint, trust_remote_code=True, padding_side="left")
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tmpl_kw = detect_thinking_support(tokenizer)

    try:
        import flash_attn
        attn = "flash_attention_2"
    except ImportError:
        attn = "sdpa"

    log.info(f"Loading {args.base_model} + {args.checkpoint}")
    base = AutoModelForCausalLM.from_pretrained(
        args.base_model, torch_dtype=torch.bfloat16, trust_remote_code=True,
        attn_implementation=attn)
    model = PeftModel.from_pretrained(base, args.checkpoint)
    model.eval().to(args.device)

    eos_ids = [tokenizer.eos_token_id]
    im_end = tokenizer.convert_tokens_to_ids("<|im_end|>")
    if im_end is not None and im_end != tokenizer.unk_token_id:
        eos_ids.append(im_end)

    data = load_jsonl(args.test_data)
    total = len(data)
    majority = Counter(d["label"] for d in data).most_common(1)[0][0]
    max_new = 10 if args.mode == "cls" else 128

    results = []
    n_bad = 0
    for i in range(0, total, args.batch_size):
        batch = data[i:i + args.batch_size]
        all_ids = [build_ids(tokenizer, item, args.mode, tmpl_kw) for item in batch]
        ml = max(len(ids) for ids in all_ids)

        padded, masks = [], []
        for ids in all_ids:
            pad = ml - len(ids)
            padded.append([tokenizer.pad_token_id] * pad + ids)
            masks.append([0] * pad + [1] * len(ids))

        input_ids = torch.tensor(padded, device=args.device)
        attn_mask = torch.tensor(masks, device=args.device)
        with torch.no_grad():
            out = model.generate(
                input_ids=input_ids, attention_mask=attn_mask,
                max_new_tokens=max_new, do_sample=False, eos_token_id=eos_ids)

        for j, item in enumerate(batch):
            gen_ids = out[j][ml:]
            gen_text = tokenizer.decode(gen_ids, skip_special_tokens=True)
            pred = parse_pred(gen_text)
            if pred == -1:
                n_bad += 1
                pred = majority
            results.append({
                "index": i + j,
                "problem_id": item["problem_id"],
                "mutation_type": item.get("mutation_type", ""),
                "label": item["label"],
                "pred": pred,
                "gen_text": gen_text.strip(),
            })

        done = min(i + args.batch_size, total)
        if done % (args.batch_size * 10) == 0 or done == total:
            acc = sum(1 for r in results if r["pred"] == r["label"]) / len(results) * 100
            log.info(f"[{args.mode}] {done}/{total} (acc={acc:.1f}%)")

    with open(args.output, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")

    correct = sum(1 for r in results if r["pred"] == r["label"])
    log.info(f"Done. {correct}/{total} ({correct/total*100:.2f}%) unparseable={n_bad}")
    log.info(f"Saved to {args.output}")


if __name__ == "__main__":
    main()
