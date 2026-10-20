#!/usr/bin/env python3
# eval_repo_cls.py — Evaluate repo-level CLS (pass/fail verifier) LoRA checkpoint
# v2: watchdog thread timeout (CUDA-safe), per-batch timing, incremental result saving

import argparse
import json
import logging
import os
import gc
import signal
import threading
import time
from collections import Counter

import numpy as np
import torch
from sklearn.metrics import (
    accuracy_score, confusion_matrix, f1_score,
    precision_score, recall_score,
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

SYSTEM_PROMPT = (
    "You are a code verifier. Given a code patch (git diff) and a test name, "
    "predict whether the test will pass or fail when run against the patched code."
)
USER_TEMPLATE = "## Patch (git diff)\n{code}\n\n## Test\n{test}\n\nWill this test pass or fail?"
LABEL_MAP = {1: "pass", 0: "fail"}

BATCH_TIMEOUT = 180

# ---------------------------------------------------------------------------
# Model family detection & configuration (shared with train_unified.py)
# ---------------------------------------------------------------------------

def detect_model_family(model_name: str) -> str:
    name_lower = model_name.lower()
    if "qwen" in name_lower:
        return "qwen"
    if "deepseek" in name_lower:
        return "deepseek"
    return "auto"


def get_chat_template_kwargs(family: str, tokenizer) -> dict:
    """Return extra kwargs for tokenizer.apply_chat_template(), per model family."""
    if family == "qwen":
        try:
            tokenizer.apply_chat_template(
                [{"role": "user", "content": "hi"}],
                tokenize=False, enable_thinking=False,
            )
            return {"enable_thinking": False}
        except TypeError:
            return {}
    return {}


def get_stop_token_ids(family: str, tokenizer) -> list[int]:
    """Return list of eos/stop token IDs for generation, per model family."""
    ids = [tokenizer.eos_token_id]
    if family == "qwen":
        im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
        if im_end_id is not None and im_end_id != tokenizer.eos_token_id:
            ids.append(im_end_id)
        endoftext_id = tokenizer.convert_tokens_to_ids("<|endoftext|>")
        if endoftext_id is not None and endoftext_id not in ids:
            ids.append(endoftext_id)
    elif family == "deepseek":
        for tok in ["<|EOT|>", "<｜end▁of▁sentence｜>"]:
            tid = tokenizer.convert_tokens_to_ids(tok)
            if tid is not None and tid not in ids:
                ids.append(tid)
    return ids


def _apply_chat_template_safe(tokenizer, messages, tmpl_kw, **kwargs):
    """apply_chat_template with fallback: merge system into user if unsupported."""
    try:
        return tokenizer.apply_chat_template(messages, **tmpl_kw, **kwargs)
    except Exception:
        merged = []
        sys_content = ""
        for m in messages:
            if m["role"] == "system":
                sys_content = m["content"]
            elif m["role"] == "user" and sys_content:
                merged.append({"role": "user", "content": sys_content + "\n\n" + m["content"]})
                sys_content = ""
            else:
                merged.append(m)
        return tokenizer.apply_chat_template(merged, **tmpl_kw, **kwargs)


# ---------------------------------------------------------------------------


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def build_prompt_ids(tokenizer, code, test, tmpl_kw, max_len):
    user_msg = USER_TEMPLATE.format(code=code, test=test)
    msgs = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_msg},
    ]
    ids = _apply_chat_template_safe(
        tokenizer, msgs, tmpl_kw, tokenize=True, add_generation_prompt=True,
    )
    if hasattr(ids, "input_ids"):
        ids = ids.input_ids
    if not isinstance(ids, list):
        ids = list(ids)
    original_length = len(ids)
    truncated = original_length > max_len
    if truncated:
        ids = ids[:max_len]
    return ids, truncated, original_length


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

    family = detect_model_family(base_model_name)
    log.info(f"Model: {base_model_name} → family={family}")

    tokenizer = AutoTokenizer.from_pretrained(
        base_model_name, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    try:
        import flash_attn
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
    return model, tokenizer, family


def run_inference(model, tokenizer, test_data, batch_size, max_seq_length, device, pred_output_path=None, family="auto"):
    tmpl_kw = get_chat_template_kwargs(family, tokenizer)
    eos_ids = get_stop_token_ids(family, tokenizer)
    log.info(f"Chat template kwargs: {tmpl_kw}, stop token IDs: {eos_ids}")
    total = len(test_data)
    label_counts = Counter(ex["label"] for ex in test_data)
    majority_class = 1 if label_counts.get(1, 0) >= label_counts.get(0, 0) else 0

    results = []
    n_unparseable = 0
    batch_times = []
    n_truncated = 0

    pred_file = open(pred_output_path, "w") if pred_output_path else None

    for i in range(0, total, batch_size):
        batch = test_data[i : i + batch_size]
        batch_idx = i // batch_size

        batch_built = [
            build_prompt_ids(tokenizer, ex["code"], ex["test"], tmpl_kw, max_seq_length)
            for ex in batch
        ]
        batch_ids = [r[0] for r in batch_built]
        batch_truncated = [r[1] for r in batch_built]
        batch_orig_lens = [r[2] for r in batch_built]

        for j, (trunc, orig_len) in enumerate(zip(batch_truncated, batch_orig_lens)):
            if trunc:
                n_truncated += 1
                log.info(f"TRUNCATED sample {i+j}: {orig_len} -> {max_seq_length} tokens")

        max_len = max(len(ids) for ids in batch_ids)
        padded = [[tokenizer.pad_token_id] * (max_len - len(ids)) + ids for ids in batch_ids]
        attn_mask = [[0] * (max_len - len(ids)) + [1] * len(ids) for ids in batch_ids]

        input_ids = torch.tensor(padded, device=device)
        attention_mask = torch.tensor(attn_mask, device=device)

        # Watchdog thread: os._exit if batch exceeds BATCH_TIMEOUT
        watchdog_event = threading.Event()
        def _watchdog(evt, bi=batch_idx, si=i, n=len(batch)):
            if not evt.wait(BATCH_TIMEOUT):
                log.error(f"WATCHDOG: Batch {bi} (samples {si}-{si+n-1}) exceeded {BATCH_TIMEOUT}s. Forcing exit.")
                if pred_file:
                    pred_file.flush()
                os._exit(1)
        wd_thread = threading.Thread(target=_watchdog, args=(watchdog_event,), daemon=True)
        wd_thread.start()

        batch_start = time.time()

        old_handler = signal.signal(signal.SIGALRM, lambda s, f: (_ for _ in ()).throw(TimeoutError('batch timeout')))
        signal.alarm(BATCH_TIMEOUT - 10)
        try:
            with torch.no_grad():
                out = model.generate(
                    input_ids=input_ids,
                    attention_mask=attention_mask,
                    max_new_tokens=8,
                    do_sample=False,
                    pad_token_id=tokenizer.pad_token_id,
                    eos_token_id=eos_ids,
                )
            torch.cuda.synchronize()
            signal.alarm(0)
        except TimeoutError:
            signal.alarm(0)
            watchdog_event.set()
            batch_elapsed = time.time() - batch_start
            log.warning(f'TIMEOUT at batch {batch_idx} (samples {i}-{i+len(batch)-1}) after {batch_elapsed:.1f}s, skipping')
            for j, ex in enumerate(batch):
                pid = ex.get('problem_id', ex.get('metadata', {}).get('instance_id', ''))
                r = {'index': i+j, 'problem_id': pid, 'label': ex['label'], 'pred': majority_class,
                     'correct': int(majority_class == ex['label']), 'truncated': batch_truncated[j],
                     'original_token_length': batch_orig_lens[j],
                     'gen_text': 'TIMEOUT', 'unparseable': True}
                results.append(r)
                if pred_file:
                    pred_file.write(json.dumps(r) + "\n")
                n_unparseable += 1
            if pred_file:
                pred_file.flush()
            signal.signal(signal.SIGALRM, old_handler)
            continue

        watchdog_event.set()
        signal.signal(signal.SIGALRM, old_handler)

        batch_elapsed = time.time() - batch_start
        batch_times.append(batch_elapsed)

        seq_lens = [len(ids) for ids in batch_ids]
        log.info(f"Batch {batch_idx} ({i}-{min(i+batch_size,total)-1}/{total}): {batch_elapsed:.1f}s, max_seq={max(seq_lens)}")
        if batch_elapsed > 60:
            log.warning(f"SLOW batch {batch_idx}: {batch_elapsed:.1f}s, seq_lens={seq_lens}")

        for j, ex in enumerate(batch):
            gen_ids = out[j][len(padded[j]):]
            gen_text = tokenizer.decode(gen_ids, skip_special_tokens=True)
            pred = parse_prediction(gen_text)
            was_unparseable = pred == -1
            if pred == -1:
                n_unparseable += 1
                pred = majority_class

            pid = ex.get("problem_id", ex.get("metadata", {}).get("instance_id", ""))
            r = {
                "index": i + j,
                "problem_id": pid,
                "label": ex["label"],
                "pred": pred,
                "correct": int(pred == ex["label"]),
                "truncated": batch_truncated[j],
                "original_token_length": batch_orig_lens[j],
                "gen_text": gen_text.strip(),
                "unparseable": was_unparseable,
            }
            results.append(r)
            if pred_file:
                pred_file.write(json.dumps(r) + "\n")

        if pred_file:
            pred_file.flush()

        done = min(i + batch_size, total)
        if done % (batch_size * 10) == 0 or done == total:
            acc_so_far = sum(r["correct"] for r in results) / len(results) * 100
            log.info(f"[CLS] {done}/{total}  running_acc={acc_so_far:.1f}%")

    if pred_file:
        pred_file.close()

    if batch_times:
        log.info(f"Batch timing: avg={np.mean(batch_times):.1f}s, max={np.max(batch_times):.1f}s, total={np.sum(batch_times):.1f}s")
    log.info(f"Truncated samples: {n_truncated}/{total}")

    if n_unparseable:
        log.warning(f"{n_unparseable} unparseable predictions (majority fallback)")
    return results


def compute_metrics(y_true, y_pred):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)
    rec = recall_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)
    f1 = f1_score(y_true, y_pred, average=None, labels=[0, 1], zero_division=0)
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    majority = max(Counter(y_true).values()) / len(y_true) if y_true else 0
    return {
        "accuracy": round(acc * 100, 2),
        "majority_baseline": round(majority * 100, 2),
        "gap_vs_majority_pp": round((acc - majority) * 100, 2),
        "f1_fail": round(float(f1[0]) * 100, 2),
        "f1_pass": round(float(f1[1]) * 100, 2),
        "f1_macro": round(float(f1.mean()) * 100, 2),
        "precision_fail": round(float(prec[0]) * 100, 2),
        "precision_pass": round(float(prec[1]) * 100, 2),
        "recall_fail": round(float(rec[0]) * 100, 2),
        "recall_pass": round(float(rec[1]) * 100, 2),
        "confusion_matrix": {
            "tn": int(cm[0][0]), "fp": int(cm[0][1]),
            "fn": int(cm[1][0]), "tp": int(cm[1][1]),
        },
        "support": {"fail": int(Counter(y_true)[0]), "pass": int(Counter(y_true)[1])},
    }


def print_report(metrics, n_total, n_unparseable):
    print("\n" + "=" * 60)
    print("REPO-LEVEL CLS EVALUATION")
    print("=" * 60)
    print(f"\nTest set: {n_total} instances")
    print(f"Class balance: pass={metrics['support']['pass']} fail={metrics['support']['fail']}")
    print(f"Majority baseline: {metrics['majority_baseline']:.1f}%")
    print(f"\nAccuracy: {metrics['accuracy']:.2f}%  (gap vs majority: {metrics['gap_vs_majority_pp']:+.1f}pp)")
    print(f"F1 macro: {metrics['f1_macro']:.2f}%")
    print(f"  fail: P={metrics['precision_fail']:.1f}% R={metrics['recall_fail']:.1f}% F1={metrics['f1_fail']:.1f}%")
    print(f"  pass: P={metrics['precision_pass']:.1f}% R={metrics['recall_pass']:.1f}% F1={metrics['f1_pass']:.1f}%")
    cm = metrics["confusion_matrix"]
    print(f"\nConfusion matrix:")
    print(f"              Predicted")
    print(f"              fail    pass")
    print(f"  Actual fail  {cm['tn']:>5}   {cm['fp']:>5}")
    print(f"  Actual pass  {cm['fn']:>5}   {cm['tp']:>5}")
    if n_unparseable:
        print(f"\nUnparseable: {n_unparseable}")
    print("=" * 60)


def main():
    p = argparse.ArgumentParser(
        description="Evaluate repo-level CLS (pass/fail verifier) LoRA checkpoint",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""Examples:
  python eval_repo_cls.py --checkpoint_dir checkpoints_repo_cls_home/checkpoint-600 --device cuda:1
  python eval_repo_cls.py --dry_run
""")
    p.add_argument("--checkpoint_dir", "--checkpoint_path", dest="checkpoint_dir",
                   help="LoRA checkpoint directory")
    p.add_argument("--model_name", default="Qwen/Qwen3-4B",
                   help="Base model name/path (auto-detected family: qwen/deepseek)")
    p.add_argument("--data_dir", default="data/swebench_full",
                   help="Data directory with swebench_{args.split}.jsonl")
    p.add_argument("--output", default="eval_repo_cls.json", help="Summary JSON output")
    p.add_argument("--pred_output", default="eval_repo_cls_predictions.jsonl",
                   help="Predictions JSONL output")
    p.add_argument("--output_dir", default=None,
                   help="Output directory (overrides --output and --pred_output paths)")
    p.add_argument("--batch_size", type=int, default=16)
    p.add_argument("--max_seq_length", type=int, default=2048)
    p.add_argument("--device", default="cuda:0")
    p.add_argument("--dry_run", action="store_true", help="Only test data loading, no model inference")
    p.add_argument("--split", choices=["val", "test"], default="test", help="Data split to evaluate")
    p.add_argument("--batch_timeout", type=int, default=BATCH_TIMEOUT,
                   help=f"Per-batch timeout in seconds (default: {BATCH_TIMEOUT})")
    args = p.parse_args()

    global BATCH_TIMEOUT
    BATCH_TIMEOUT = args.batch_timeout

    script_dir = os.path.dirname(os.path.abspath(__file__))

    if args.output_dir:
        out_dir = os.path.join(script_dir, args.output_dir)
        os.makedirs(out_dir, exist_ok=True)
        summary_path = os.path.join(out_dir, "eval_repo_cls.json")
        pred_path = os.path.join(out_dir, "eval_repo_cls_predictions.jsonl")
    else:
        summary_path = os.path.join(script_dir, args.output)
        pred_path = os.path.join(script_dir, args.pred_output)

    data_path = os.path.join(script_dir, args.data_dir, f"swebench_{args.split}.jsonl")
    if not os.path.exists(data_path):
        data_path = os.path.join(args.data_dir, f"swebench_{args.split}.jsonl")

    log.info(f"Loading {args.split} data: {data_path}")
    test_data = load_jsonl(data_path)
    log.info(f"Loaded {len(test_data)} {args.split} instances")

    label_counts = Counter(ex["label"] for ex in test_data)
    log.info(f"Label distribution: {dict(label_counts)}")

    if args.dry_run:
        log.info("Dry run — data loaded successfully. Exiting.")
        print(f"\nDry run OK: {len(test_data)} instances, labels={dict(label_counts)}")
        return

    if not args.checkpoint_dir:
        p.error("--checkpoint_dir required for inference (use --dry_run for data-only check)")

    log.info(f"Loading model from {args.checkpoint_dir}")
    model, tokenizer, family = load_model(args.checkpoint_dir, args.model_name, args.device)
    log.info(f"Model loaded. Starting inference (max_seq_length={args.max_seq_length}, batch_timeout={BATCH_TIMEOUT}s)...")

    results = run_inference(model, tokenizer, test_data, args.batch_size,
                            args.max_seq_length, args.device, pred_output_path=pred_path,
                            family=family)

    del model
    gc.collect()
    torch.cuda.empty_cache()

    labels = [r["label"] for r in results]
    preds = [r["pred"] for r in results]
    n_unparseable = sum(1 for r in results if r.get("unparseable", False))

    metrics = compute_metrics(labels, preds)
    print_report(metrics, len(results), n_unparseable)

    output = {
        "model": "CLS",
        "checkpoint": args.checkpoint_dir,
        "split": args.split,
        "n_instances": len(results),
        "n_cls_unparseable": n_unparseable,
        "n_truncated": sum(1 for r in results if r.get("truncated", False)),
        "metrics": metrics,
        "config": {
            "model_name": args.model_name,
            "max_seq_length": args.max_seq_length,
            "batch_size": args.batch_size,
            "batch_timeout": BATCH_TIMEOUT,
        },
    }
    with open(summary_path, "w") as f:
        json.dump(output, f, indent=2)
    log.info(f"Summary saved to {summary_path}")
    log.info(f"Predictions saved to {pred_path}")


if __name__ == "__main__":
    main()
