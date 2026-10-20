import argparse
import json
import logging
import os
from collections import Counter

import torch
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

SYSTEM_PROMPTS = {
    "per_test": (
        "You are a code verifier. Given a code snippet and a test case, "
        "predict whether the test will pass or fail."
    ),
    "trajectory": (
        "You are a code repair verifier. Given the code patch and test summary, "
        "predict whether all tests pass (resolved) or any test fails (unresolved)."
    ),
}

LABEL_MAPS = {
    "per_test": {1: "pass", 0: "fail"},
    "trajectory": {1: "resolved", 0: "unresolved"},
}


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


def build_messages(mode, example):
    if mode == "per_test":
        user_msg = (
            f"## Code\n{example['code']}\n\n"
            f"## Test\n{example['test']}\n\n"
            "Will this test pass or fail?"
        )
    else:
        user_msg = (
            f"[Code]\n{example['code']}\n\n"
            f"[Test Summary]\n{example['test_summary']}"
        )
    return [
        {"role": "system", "content": SYSTEM_PROMPTS[mode]},
        {"role": "user", "content": user_msg},
    ]


def parse_prediction(text, mode):
    if "</think>" in text:
        text = text.split("</think>")[-1]
    text = text.strip().lower()

    if mode == "per_test":
        pos, neg = "pass", "fail"
    else:
        pos, neg = "resolved", "unresolved"

    if text.startswith(pos):
        return 1
    if text.startswith(neg):
        return 0
    if pos in text and neg not in text:
        return 1
    if neg in text and pos not in text:
        return 0
    return -1


def main():
    p = argparse.ArgumentParser(description="Zero-shot LLM judge for code verification")
    p.add_argument("--model_name", required=True, help="Model path")
    p.add_argument("--data_file", required=True, help="Path to test.jsonl or traj_test.jsonl")
    p.add_argument("--mode", required=True, choices=["per_test", "trajectory"])
    p.add_argument("--quantize_4bit", action="store_true")
    p.add_argument("--output", default="eval_judge_results.json")
    p.add_argument("--batch_size", type=int, default=4)
    p.add_argument("--max_seq_length", type=int, default=2048)
    args = p.parse_args()

    log.info(f"Loading tokenizer from {args.model_name}")
    tokenizer = AutoTokenizer.from_pretrained(
        args.model_name, trust_remote_code=True, padding_side="left",
    )
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    tmpl_kw = detect_thinking_support(tokenizer)

    load_kwargs = dict(
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto",
    )
    if args.quantize_4bit:
        load_kwargs["quantization_config"] = BitsAndBytesConfig(
            load_in_4bit=True,
            bnb_4bit_compute_dtype=torch.bfloat16,
            bnb_4bit_quant_type="nf4",
        )
    else:
        try:
            import flash_attn  # noqa: F401
            load_kwargs["attn_implementation"] = "flash_attention_2"
        except ImportError:
            load_kwargs["attn_implementation"] = "sdpa"

    log.info(f"Loading model (4bit={args.quantize_4bit})")
    model = AutoModelForCausalLM.from_pretrained(args.model_name, **load_kwargs)
    model.eval()

    data = load_jsonl(args.data_file)
    log.info(f"Loaded {len(data)} examples from {args.data_file} (mode={args.mode})")

    label_counts = Counter(ex["label"] for ex in data)
    n_pos = label_counts.get(1, 0)
    n_neg = label_counts.get(0, 0)
    total = len(data)
    majority_baseline = max(n_pos, n_neg) / total
    majority_class = 1 if n_pos >= n_neg else 0

    pos_name = LABEL_MAPS[args.mode][1]
    neg_name = LABEL_MAPS[args.mode][0]
    log.info(f"Class balance: {pos_name}={n_pos} ({n_pos/total*100:.1f}%), {neg_name}={n_neg} ({n_neg/total*100:.1f}%)")

    eos_ids = [tokenizer.eos_token_id]
    im_end_id = tokenizer.convert_tokens_to_ids("<|im_end|>")
    if im_end_id is not None and isinstance(im_end_id, int) and im_end_id != tokenizer.unk_token_id:
        eos_ids.append(im_end_id)

    y_true, y_pred = [], []
    n_unparseable = 0

    for i in range(0, total, args.batch_size):
        batch = data[i : i + args.batch_size]
        batch_labels = [ex["label"] for ex in batch]

        all_ids = []
        for ex in batch:
            msgs = build_messages(args.mode, ex)
            ids = tokenizer.apply_chat_template(
                msgs, tokenize=True, add_generation_prompt=True, **tmpl_kw,
            )
            if not isinstance(ids, list):
                ids = ids["input_ids"]
                if isinstance(ids[0], list):
                    ids = ids[0]
            if len(ids) > args.max_seq_length:
                ids = ids[: args.max_seq_length]
            all_ids.append(ids)

        max_len = max(len(ids) for ids in all_ids)
        padded = [
            [tokenizer.pad_token_id] * (max_len - len(ids)) + ids
            for ids in all_ids
        ]
        masks = [
            [0] * (max_len - len(ids)) + [1] * len(ids)
            for ids in all_ids
        ]

        device = next(model.parameters()).device
        input_ids = torch.tensor(padded, device=device)
        attention_mask = torch.tensor(masks, device=device)

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
            pred = parse_prediction(gen_text, args.mode)

            if pred == -1:
                n_unparseable += 1
                pred = majority_class
                log.warning(f"Unparseable [{i+j}]: '{gen_text}' -> majority fallback")

            y_true.append(batch_labels[j])
            y_pred.append(pred)

        done = min(i + args.batch_size, total)
        if done % (args.batch_size * 10) == 0 or done == total:
            log.info(f"Progress: {done}/{total}")

    acc = accuracy_score(y_true, y_pred)
    gap = acc - majority_baseline
    prec = precision_score(y_true, y_pred, average=None, labels=[0, 1])
    rec = recall_score(y_true, y_pred, average=None, labels=[0, 1])
    f1 = f1_score(y_true, y_pred, average=None, labels=[0, 1])
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])

    results = {
        "model": args.model_name,
        "mode": args.mode,
        "quantize_4bit": args.quantize_4bit,
        "test_set_size": total,
        "class_balance": {pos_name: n_pos, neg_name: n_neg, f"{pos_name}_pct": round(n_pos / total * 100, 1)},
        "majority_baseline_accuracy": round(majority_baseline * 100, 2),
        "overall_accuracy": round(acc * 100, 2),
        "accuracy_vs_baseline_gap_pp": round(gap * 100, 2),
        "per_class": {
            neg_name: {"precision": round(float(prec[0]) * 100, 2), "recall": round(float(rec[0]) * 100, 2), "f1": round(float(f1[0]) * 100, 2), "support": int(n_neg)},
            pos_name: {"precision": round(float(prec[1]) * 100, 2), "recall": round(float(rec[1]) * 100, 2), "f1": round(float(f1[1]) * 100, 2), "support": int(n_pos)},
        },
        "confusion_matrix": {"tn": int(cm[0][0]), "fp": int(cm[0][1]), "fn": int(cm[1][0]), "tp": int(cm[1][1])},
        "unparseable_predictions": n_unparseable,
    }

    print("\n" + "=" * 60)
    print(f"ZERO-SHOT LLM JUDGE: {args.mode} mode")
    print(f"Model: {os.path.basename(args.model_name)} (4bit={args.quantize_4bit})")
    print("=" * 60)
    print(f"\nTest set: {total} examples")
    print(f"Class balance: {pos_name}={n_pos} ({n_pos/total*100:.1f}%), {neg_name}={n_neg} ({n_neg/total*100:.1f}%)")
    print(f"Majority baseline accuracy: {majority_baseline*100:.1f}%")
    print(f"\nOverall accuracy: {acc*100:.1f}%")
    print(f"Accuracy vs baseline gap: {gap*100:+.1f}pp")
    print(f"\nPer-class metrics:")
    print(f"  {'Class':<12} {'Precision':>10} {'Recall':>10} {'F1':>10} {'Support':>10}")
    print(f"  {'---':<12} {'---':>10} {'---':>10} {'---':>10} {'---':>10}")
    for name, idx in [(neg_name, 0), (pos_name, 1)]:
        support = n_neg if idx == 0 else n_pos
        print(f"  {name:<12} {prec[idx]*100:>9.1f}% {rec[idx]*100:>9.1f}% {f1[idx]*100:>9.1f}% {support:>5}")
    print(f"\nConfusion matrix:")
    print(f"              Predicted")
    print(f"              {neg_name:<8} {pos_name:<8}")
    print(f"  Actual {neg_name:<8} {cm[0][0]:>5}   {cm[0][1]:>5}")
    print(f"  Actual {pos_name:<8} {cm[1][0]:>5}   {cm[1][1]:>5}")
    if n_unparseable:
        print(f"\nUnparseable: {n_unparseable} (majority class fallback)")
    print("=" * 60)

    with open(args.output, "w") as f:
        json.dump(results, f, indent=2)
    log.info(f"Results saved to {args.output}")


if __name__ == "__main__":
    main()
