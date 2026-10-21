#!/usr/bin/env python3
"""CLS verifier inference on 59 re-repair instances for condition B predictions."""

import argparse
import json
import logging
import time
from collections import Counter

import torch
from sklearn.metrics import accuracy_score, f1_score

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a code verifier. Given a code patch (git diff) and a test name, "
    "predict whether the test will pass or fail when run against the patched code."
)
USER_TEMPLATE = "## Patch (git diff)\n{code}\n\n## Test\n{test}\n\nWill this test pass or fail?"

CHECKPOINT_DIR = "/home/sonny/exec-sim-repair-verifier/checkpoints_repo_cls_v5/checkpoint-4600"
BASE_MODEL = "Qwen/Qwen3-4B"
INPUT_PATH = "/home/sonny/exec-sim-repair-verifier/data/re_repair_v2/re_repair_instances_final.jsonl"
OUTPUT_PATH = "/home/sonny/exec-sim-repair-verifier/data/re_repair_v2/cls_predictions.jsonl"


def detect_thinking_support(tokenizer):
    try:
        tokenizer.apply_chat_template(
            [{"role": "user", "content": "hi"}],
            tokenize=False, enable_thinking=False,
        )
        return {"enable_thinking": False}
    except TypeError:
        return {}


def build_prompt_ids(tokenizer, code, test, tmpl_kw, max_len):
    def _apply_tmpl(msgs, gen_prompt=True):
        out = tokenizer.apply_chat_template(
            msgs, tokenize=True, add_generation_prompt=gen_prompt, **tmpl_kw,
        )
        if hasattr(out, "input_ids"):
            out = out.input_ids
        return list(out) if not isinstance(out, list) else out

    user_msg = USER_TEMPLATE.format(code=code, test=test)
    msgs = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
    ]
    ids = _apply_tmpl(msgs)

    if len(ids) > max_len:
        shell_msg = USER_TEMPLATE.format(code="", test=test)
        shell_msgs = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": shell_msg},
        ]
        overhead = len(_apply_tmpl(shell_msgs))
        budget = max(0, max_len - overhead)

        code_tokens = tokenizer.encode(code, add_special_tokens=False)
        if len(code_tokens) > budget:
            code_tokens = code_tokens[:budget]
            code = tokenizer.decode(code_tokens, skip_special_tokens=False)

        user_msg = USER_TEMPLATE.format(code=code, test=test)
        msgs = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_msg},
        ]
        ids = _apply_tmpl(msgs)

        if len(ids) > max_len:
            ids_no_gen = _apply_tmpl(msgs, gen_prompt=False)
            gen_suffix = ids[len(ids_no_gen):]
            ids = ids[:max_len - len(gen_suffix)] + gen_suffix

        return ids, True
    return ids, False


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


def load_model(checkpoint_dir, base_model_name, device):
    from peft import PeftModel
    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(
        base_model_name, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    try:
        import flash_attn  # noqa: F401
        attn_impl = "flash_attention_2"
    except ImportError:
        attn_impl = "sdpa"
    log.info(f"Attention: {attn_impl}")

    base_model = AutoModelForCausalLM.from_pretrained(
        base_model_name,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        attn_implementation=attn_impl,
    )
    model = PeftModel.from_pretrained(base_model, checkpoint_dir)
    model.eval()
    model = model.to(device)
    if hasattr(model, "generation_config"):
        model.generation_config.enable_thinking = False
    return model, tokenizer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--max-seq-length", type=int, default=4096)
    args = parser.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    log.info(f"Device: {device}")

    # Load model
    log.info("Loading model...")
    model, tokenizer = load_model(CHECKPOINT_DIR, BASE_MODEL, device)
    tmpl_kw = detect_thinking_support(tokenizer)
    log.info(f"Template kwargs: {tmpl_kw}")

    # Load data
    with open(INPUT_PATH) as f:
        instances = [json.loads(line) for line in f]
    log.info(f"Loaded {len(instances)} instances")

    # Flatten to (instance_idx, test_name) pairs
    pairs = []
    for idx, inst in enumerate(instances):
        for test_name in inst["all_test_names"]:
            pairs.append((idx, test_name))
    log.info(f"Total predictions to make: {len(pairs)}")

    # Build all prompts
    log.info("Building prompts...")
    all_ids = []
    n_truncated = 0
    for inst_idx, test_name in pairs:
        code = instances[inst_idx]["mutation_patch"]
        ids, truncated = build_prompt_ids(tokenizer, code, test_name, tmpl_kw, args.max_seq_length)
        all_ids.append(ids)
        if truncated:
            n_truncated += 1
    log.info(f"Prompts built. Truncated: {n_truncated}/{len(pairs)}")

    # Batch inference
    eos_ids = [tokenizer.eos_token_id]
    if hasattr(tokenizer, "added_tokens_encoder"):
        for tok_str in ["<|im_end|>", "<|endoftext|>"]:
            tid = tokenizer.convert_tokens_to_ids(tok_str)
            if tid != tokenizer.unk_token_id and tid not in eos_ids:
                eos_ids.append(tid)

    predictions = [None] * len(pairs)
    raw_outputs = [None] * len(pairs)

    t0 = time.time()
    bs = args.batch_size
    total_batches = (len(pairs) + bs - 1) // bs

    for batch_idx in range(total_batches):
        start = batch_idx * bs
        end = min(start + bs, len(pairs))
        batch_ids = all_ids[start:end]

        max_len_batch = max(len(ids) for ids in batch_ids)
        input_ids = torch.full((len(batch_ids), max_len_batch), tokenizer.pad_token_id, dtype=torch.long)
        attention_mask = torch.zeros((len(batch_ids), max_len_batch), dtype=torch.long)

        for i, ids in enumerate(batch_ids):
            offset = max_len_batch - len(ids)
            input_ids[i, offset:] = torch.tensor(ids, dtype=torch.long)
            attention_mask[i, offset:] = 1

        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)

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

        if (batch_idx + 1) % 20 == 0 or batch_idx == total_batches - 1:
            elapsed = time.time() - t0
            done = end
            rate = done / elapsed
            eta = (len(pairs) - done) / rate if rate > 0 else 0
            log.info(f"Batch {batch_idx+1}/{total_batches} | {done}/{len(pairs)} | "
                     f"{rate:.1f} pred/s | ETA {eta:.0f}s")

    elapsed_total = time.time() - t0
    log.info(f"Inference done in {elapsed_total:.1f}s ({len(pairs)/elapsed_total:.1f} pred/s)")

    # Aggregate per-instance results
    results = []
    all_preds = []
    all_labels = []

    for idx, inst in enumerate(instances):
        oracle = inst["oracle_per_test"]
        per_test_preds = {}
        inst_pairs = [(i, p) for i, (iidx, _) in enumerate(pairs) if iidx == idx for p in [predictions[i]]]

        # More efficient: collect by index range
        start_idx = sum(len(instances[j]["all_test_names"]) for j in range(idx))
        for t_offset, test_name in enumerate(inst["all_test_names"]):
            global_idx = start_idx + t_offset
            pred = predictions[global_idx]
            pred_bool = True if pred == 1 else False  # unparseable (-1) → False (fail)
            per_test_preds[test_name] = pred_bool

            label = oracle.get(test_name)
            if label is not None:
                all_preds.append(1 if pred_bool else 0)
                all_labels.append(1 if label else 0)

        n_pass = sum(1 for v in per_test_preds.values() if v)
        n_fail = sum(1 for v in per_test_preds.values() if not v)

        results.append({
            "instance_id": inst["instance_id"],
            "mutation_type": inst["mutation_type"],
            "per_test_predictions": per_test_preds,
            "n_tests": len(per_test_preds),
            "n_predicted_pass": n_pass,
            "n_predicted_fail": n_fail,
        })

    # Write output
    with open(OUTPUT_PATH, "w") as f:
        for r in results:
            f.write(json.dumps(r) + "\n")
    log.info(f"Output written to {OUTPUT_PATH}")

    # Statistics
    n_unparseable = sum(1 for p in predictions if p == -1)
    n_all_pass = sum(1 for r in results if r["n_predicted_fail"] == 0)
    acc = accuracy_score(all_labels, all_preds)
    f1 = f1_score(all_labels, all_preds, average="macro")

    pass_count = sum(1 for p in all_preds if p == 1)
    fail_count = sum(1 for p in all_preds if p == 0)

    log.info("=" * 60)
    log.info(f"Total predictions: {len(pairs)}")
    log.info(f"Unparseable: {n_unparseable}")
    log.info(f"Pass/Fail distribution: {pass_count} pass / {fail_count} fail")
    log.info(f"Instances with all-pass prediction: {n_all_pass}/{len(results)}")
    log.info(f"Accuracy vs oracle: {acc:.4f} ({acc*100:.2f}%)")
    log.info(f"F1 macro vs oracle: {f1:.4f} ({f1*100:.2f}%)")
    log.info(f"Total time: {elapsed_total:.1f}s")
    log.info("=" * 60)


if __name__ == "__main__":
    main()
