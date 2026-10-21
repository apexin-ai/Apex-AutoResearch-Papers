# eval_cwm_baseline.py — Evaluate CWM generation baseline on pass/fail classification
# Input: data_dir/cwm_test.jsonl + LoRA checkpoint (generation model)
# Output: Formatted report to stdout + JSON to --output
# Key difference from eval_verifier.py:
#   - Generates execution output string instead of "pass"/"fail"
#   - Extracts pass/fail from generated output via keyword matching
#   - Additional metrics: exact match rate, per-error-type match, generation length stats
# Same metrics: class balance, majority baseline, per-class P/R/F1, accuracy, confusion matrix

import argparse
import json
import logging
import os
import re
from collections import Counter, defaultdict

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
    "You are a code execution simulator. Given a code snippet and a test case, "
    "predict the execution result."
)

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
        # DeepSeek-Coder uses <|EOT|> and <｜end▁of▁sentence｜> as stop tokens
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
    user_msg = f"## Code\n{code}\n\n## Test\n{test}\n\nWhat is the execution result?"
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
    if len(ids) > max_len:
        ids = ids[:max_len]
    return ids


def extract_pass_fail(text):
    """Extract pass/fail prediction from generated execution output."""
    if "</think>" in text:
        text = text.split("</think>")[-1]
    text_clean = text.strip()
    text_lower = text_clean.lower()

    if text_lower.startswith("pass"):
        return 1
    if text_lower.startswith("fail"):
        return 0

    fail_patterns = ["error", "assert", "traceback", "exception", "fail"]
    pass_patterns = ["pass", "success", "completed"]

    has_fail = any(p in text_lower for p in fail_patterns)
    has_pass = any(p in text_lower for p in pass_patterns)

    if has_fail and not has_pass:
        return 0
    if has_pass and not has_fail:
        return 1
    # Ambiguous or neither → conservative: predict fail
    return 0


def extract_error_type(target):
    """Extract error type from target string like 'FAIL: AssertionError: ...'."""
    if target.startswith("PASS"):
        return "PASS"
    match = re.match(r"FAIL:\s*(\w+Error|\w+Exception|Error)", target)
    if match:
        return match.group(1)
    return "Other"


def main():
    p = argparse.ArgumentParser(description="Evaluate CWM generation baseline")
    p.add_argument("--data_dir", required=True)
    p.add_argument("--checkpoint_dir", required=True)
    p.add_argument("--model_name", default="Qwen/Qwen3-4B",
                   help="Base model name/path (auto-detected family: qwen/deepseek)")
    p.add_argument("--output", default="eval_cwm_results.json")
    p.add_argument("--batch_size", type=int, default=16)
    p.add_argument("--max_seq_length", type=int, default=2048)
    p.add_argument("--max_new_tokens", type=int, default=64)
    args = p.parse_args()

    family = detect_model_family(args.model_name)
    log.info(f"Model: {args.model_name} → family={family}")

    tokenizer = AutoTokenizer.from_pretrained(
        args.checkpoint_dir, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tmpl_kw = get_chat_template_kwargs(family, tokenizer)

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

    test_data = load_jsonl(os.path.join(args.data_dir, "cwm_test.jsonl"))
    log.info(f"Test set: {len(test_data)} examples")

    label_counts = Counter(ex["label"] for ex in test_data)
    n_pass, n_fail = label_counts.get(1, 0), label_counts.get(0, 0)
    total = len(test_data)
    majority_baseline = max(n_pass, n_fail) / total
    majority_class = 1 if n_pass >= n_fail else 0

    log.info(f"Class balance: pass={n_pass} ({n_pass/total*100:.1f}%), fail={n_fail} ({n_fail/total*100:.1f}%)")
    log.info(f"Majority baseline: {majority_baseline*100:.1f}%")

    eos_ids = get_stop_token_ids(family, tokenizer)
    log.info(f"Stop token IDs: {eos_ids}")

    y_true, y_pred = [], []
    gen_texts = []
    gen_lengths = []
    n_unparseable = 0

    for i in range(0, total, args.batch_size):
        batch = test_data[i : i + args.batch_size]
        batch_ids = [
            build_prompt_ids(tokenizer, ex["code"], ex["test"], tmpl_kw, args.max_seq_length)
            for ex in batch
        ]
        batch_labels = [ex["label"] for ex in batch]

        max_len = max(len(ids) for ids in batch_ids)
        pad_id = tokenizer.pad_token_id
        padded = [([pad_id] * (max_len - len(ids))) + ids for ids in batch_ids]
        masks = [([0] * (max_len - len(ids))) + ([1] * len(ids)) for ids in batch_ids]

        input_ids = torch.tensor(padded, device="cuda")
        attention_mask = torch.tensor(masks, device="cuda")

        with torch.no_grad():
            outputs = model.generate(
                input_ids=input_ids,
                attention_mask=attention_mask,
                max_new_tokens=args.max_new_tokens,
                do_sample=False,
                eos_token_id=eos_ids,
            )

        for j in range(len(batch)):
            gen_ids = outputs[j][max_len:]
            gen_text = tokenizer.decode(gen_ids, skip_special_tokens=True)
            pred = extract_pass_fail(gen_text)

            gen_texts.append(gen_text)
            gen_lengths.append(len(gen_text))

            y_true.append(batch_labels[j])
            y_pred.append(pred)

        done = min(i + args.batch_size, total)
        if done % (args.batch_size * 10) == 0 or done == total:
            log.info(f"Progress: {done}/{total}")

    # === Classification metrics (same as eval_verifier.py) ===
    acc = accuracy_score(y_true, y_pred)
    gap = acc - majority_baseline
    prec = precision_score(y_true, y_pred, average=None, labels=[0, 1])
    rec = recall_score(y_true, y_pred, average=None, labels=[0, 1])
    f1 = f1_score(y_true, y_pred, average=None, labels=[0, 1])
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])

    # === CWM-specific metrics ===
    # Exact match rate
    n_exact = 0
    for k in range(total):
        gt_target = test_data[k].get("target", "")
        if gen_texts[k].strip() == gt_target.strip():
            n_exact += 1
    exact_match_rate = n_exact / total if total > 0 else 0

    # Per error-type match rate
    error_type_stats = defaultdict(lambda: {"total": 0, "exact": 0, "correct_pf": 0})
    for k in range(total):
        gt_target = test_data[k].get("target", "")
        etype = extract_error_type(gt_target)
        error_type_stats[etype]["total"] += 1
        if gen_texts[k].strip() == gt_target.strip():
            error_type_stats[etype]["exact"] += 1
        if y_pred[k] == y_true[k]:
            error_type_stats[etype]["correct_pf"] += 1

    error_type_results = {}
    for etype, st in sorted(error_type_stats.items(), key=lambda x: -x[1]["total"]):
        error_type_results[etype] = {
            "total": st["total"],
            "exact_match": st["exact"],
            "exact_match_rate": round(st["exact"] / st["total"] * 100, 2) if st["total"] else 0,
            "pass_fail_accuracy": round(st["correct_pf"] / st["total"] * 100, 2) if st["total"] else 0,
        }

    # Generation length stats
    import statistics
    gen_len_mean = statistics.mean(gen_lengths) if gen_lengths else 0
    gen_len_median = statistics.median(gen_lengths) if gen_lengths else 0
    gen_len_max = max(gen_lengths) if gen_lengths else 0

    # === Build results dict ===
    results = {
        "test_set_size": total,
        "class_balance": {"pass": n_pass, "fail": n_fail, "pass_pct": round(n_pass / total * 100, 1)},
        "majority_baseline_accuracy": round(majority_baseline * 100, 2),
        "overall_accuracy": round(acc * 100, 2),
        "accuracy_vs_baseline_gap_pp": round(gap * 100, 2),
        "per_class": {
            "fail": {
                "precision": round(float(prec[0]) * 100, 2),
                "recall": round(float(rec[0]) * 100, 2),
                "f1": round(float(f1[0]) * 100, 2),
                "support": int(n_fail),
            },
            "pass": {
                "precision": round(float(prec[1]) * 100, 2),
                "recall": round(float(rec[1]) * 100, 2),
                "f1": round(float(f1[1]) * 100, 2),
                "support": int(n_pass),
            },
        },
        "confusion_matrix": {
            "tn": int(cm[0][0]), "fp": int(cm[0][1]),
            "fn": int(cm[1][0]), "tp": int(cm[1][1]),
        },
        "cwm_metrics": {
            "exact_match_rate": round(exact_match_rate * 100, 2),
            "exact_match_count": n_exact,
            "by_error_type": error_type_results,
            "generation_length": {
                "mean": round(gen_len_mean, 1),
                "median": round(gen_len_median, 1),
                "max": gen_len_max,
            },
        },
        "unparseable_predictions": n_unparseable,
    }

    # === Print report ===
    print("\n" + "=" * 60)
    print("EVALUATION REPORT: CWM Generation Baseline")
    print("=" * 60)
    print(f"\nTest set: {total} examples")
    print(f"Class balance: pass={n_pass} ({n_pass/total*100:.1f}%), fail={n_fail} ({n_fail/total*100:.1f}%)")
    print(f"Majority baseline accuracy: {majority_baseline*100:.1f}%")
    print(f"\nOverall accuracy: {acc*100:.1f}%")
    gap_status = "PASS" if gap >= 0.10 else "FAIL"
    print(f"Accuracy vs baseline gap: {gap*100:+.1f}pp [{gap_status}] (threshold: >=10pp)")
    print(f"\nPer-class metrics:")
    print(f"  {'Class':<8} {'Precision':>10} {'Recall':>10} {'F1':>10} {'Support':>10}")
    print(f"  {'---':<8} {'---':>10} {'---':>10} {'---':>10} {'---':>10}")
    for name, idx in [("fail", 0), ("pass", 1)]:
        f1_status = "OK" if f1[idx] > 0.65 else "LOW"
        support = n_fail if idx == 0 else n_pass
        print(f"  {name:<8} {prec[idx]*100:>9.1f}% {rec[idx]*100:>9.1f}% {f1[idx]*100:>9.1f}% [{f1_status}] {support:>5}")
    print(f"\nConfusion matrix:")
    print(f"              Predicted")
    print(f"              fail    pass")
    print(f"  Actual fail  {cm[0][0]:>5}   {cm[0][1]:>5}")
    print(f"  Actual pass  {cm[1][0]:>5}   {cm[1][1]:>5}")

    print(f"\n--- CWM-Specific Metrics ---")
    print(f"Exact match rate: {exact_match_rate*100:.1f}% ({n_exact}/{total})")
    print(f"Generation length: mean={gen_len_mean:.1f}, median={gen_len_median:.1f}, max={gen_len_max}")
    print(f"\nPer error-type breakdown:")
    print(f"  {'Type':<25} {'Count':>6} {'ExactMatch':>12} {'P/F Acc':>10}")
    print(f"  {'---':<25} {'---':>6} {'---':>12} {'---':>10}")
    for etype, st in sorted(error_type_results.items(), key=lambda x: -x[1]["total"]):
        print(f"  {etype:<25} {st['total']:>6} {st['exact_match_rate']:>11.1f}% {st['pass_fail_accuracy']:>9.1f}%")

    f1_ok = all(x > 0.65 for x in f1)
    gap_ok = gap >= 0.10
    print(f"\nMVP-B CRITERIA (same thresholds as classification):")
    print(f"  Per-class F1 >65%: {'PASS' if f1_ok else 'FAIL'}")
    print(f"  Accuracy gap >=10pp: {'PASS' if gap_ok else 'FAIL'} ({gap*100:+.1f}pp)")
    print(f"  Overall: {'PASS' if f1_ok and gap_ok else 'FAIL'}")
    print("=" * 60)

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    log.info(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
