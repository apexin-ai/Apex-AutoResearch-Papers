"""Heuristic ack detector — rule-based alternative to LLM annotation.

Identifies acknowledgment messages using simple text features:
  - Short messages (< threshold characters)
  - Pattern matching for common ack phrases

Evaluates against LLM annotations as ground truth.
"""
import json
import re
import os
from collections import Counter


def heuristic_is_ack(text: str, char_threshold: int = 80) -> bool:
    text_stripped = text.strip()

    if len(text_stripped) < char_threshold:
        return True

    ack_patterns = [
        r"^(the answer is|my answer is|final answer)",
        r"^(i agree|i concur|that'?s correct|you'?re right|correct)",
        r"^(yes,?\s|absolutely|exactly|indeed)",
        r"^(i confirm|confirmed|verified)",
        r"^(good|great|nice|well done)",
    ]
    text_lower = text_stripped.lower()
    for pattern in ack_patterns:
        if re.match(pattern, text_lower):
            if len(text_stripped) <= 200:
                return True
            break

    # Extended patterns for verbose acks (14B-style "The answer is indeed X. Your solution is correct.")
    if len(text_stripped) <= 300:
        verbose_ack_patterns = [
            r"^(the answer is|my answer is).*\b(correct|indeed|right)\b",
            r"^(your|the) (solution|calculation|answer|approach|reasoning) (is|are) (correct|right|indeed)",
            r"^(i agree|i concur|that'?s correct|exactly right|absolutely correct)",
            r"^(great|excellent|well done|good job|nice work)",
        ]
        for pattern in verbose_ack_patterns:
            if re.match(pattern, text_lower):
                return True

    return False


# ---------------------------------------------------------------------------
# Llama-specific heuristic (keyword + length + 4-gram overlap)
# ---------------------------------------------------------------------------

ACK_KEYWORDS = [
    "i'm glad", "you've broken", "your step-by-step",
    "your rephrased", "i appreciate the", "you've provided",
    "your solution is correct", "the answer is indeed",
]
NONACK_KEYWORDS = [
    "here's another", "i have another", "let's break down",
    "let me solve", "i have a new", "i need help",
    "can you help", "solve this", "please solve",
]
LEN_THRESHOLD = 300
OVERLAP_THRESHOLD = 0.3


def _four_gram_overlap(cur_text: str, prev_text: str) -> float:
    cw = cur_text.lower().split()
    pw = prev_text.lower().split()
    if len(cw) < 4 or len(pw) < 4:
        return 0.0
    c4 = set(tuple(cw[i:i+4]) for i in range(len(cw) - 3))
    p4 = set(tuple(pw[i:i+4]) for i in range(len(pw) - 3))
    return len(c4 & p4) / len(c4) if c4 else 0.0


def heuristic_is_ack_llama(text: str, prev_text: str = "") -> bool:
    tl = text.lower()
    if any(kw in tl for kw in NONACK_KEYWORDS):
        return False
    if "however" in tl[:300]:
        return False
    if any(kw in tl[:300] for kw in ACK_KEYWORDS):
        return True
    if len(text.strip()) < LEN_THRESHOLD:
        return True
    if prev_text and _four_gram_overlap(text, prev_text) > OVERLAP_THRESHOLD:
        return True
    return False


def evaluate_heuristic(traces_path: str, annotations_path: str, char_threshold: int = 80):
    labels = {}
    with open(annotations_path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            msg_idx = rec["message_index"]
            ann_a = rec.get("annotation_a", {})
            ann_single = rec.get("annotation", {})
            fn_type = ann_a.get("type") or ann_single.get("type") or "unknown"
            labels[(task_id, msg_idx)] = fn_type

    traces = []
    with open(traces_path) as f:
        for line in f:
            if line.strip():
                traces.append(json.loads(line))
    trace_map = {t["task_id"]: t for t in traces}

    tp = fp = fn = tn = 0
    for (task_id, msg_idx), true_label in labels.items():
        if task_id not in trace_map:
            continue
        msgs = trace_map[task_id].get("messages", [])
        target_round = msg_idx + 1
        text = ""
        for m in msgs:
            if m.get("round", 0) == target_round:
                text = m.get("content", "")
                break

        predicted_ack = heuristic_is_ack(text, char_threshold)
        true_ack = (true_label == "acknowledgment")

        if predicted_ack and true_ack:
            tp += 1
        elif predicted_ack and not true_ack:
            fp += 1
        elif not predicted_ack and true_ack:
            fn += 1
        else:
            tn += 1

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    accuracy = (tp + tn) / (tp + fp + fn + tn) if (tp + fp + fn + tn) > 0 else 0

    return {
        "tp": tp, "fp": fp, "fn": fn, "tn": tn,
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "f1": round(f1, 4),
        "accuracy": round(accuracy, 4),
        "char_threshold": char_threshold,
        "total": tp + fp + fn + tn,
        "predicted_ack": tp + fp,
        "true_ack": tp + fn,
    }


def generate_heuristic_annotations(traces_path: str, output_path: str, char_threshold: int = 80):
    traces = []
    with open(traces_path) as f:
        for line in f:
            if line.strip():
                traces.append(json.loads(line))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as out:
        for trace in traces:
            task_id = trace["task_id"]
            for msg in trace.get("messages", []):
                rnd = msg.get("round", 0)
                if rnd == 0:
                    continue
                msg_idx = rnd - 1
                text = msg.get("content", "")
                is_ack = heuristic_is_ack(text, char_threshold)
                rec = {
                    "task_id": task_id,
                    "message_index": msg_idx,
                    "annotation_a": {"type": "acknowledgment" if is_ack else "non_ack"},
                }
                out.write(json.dumps(rec) + "\n")


if __name__ == "__main__":
    import sys

    base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "outputs", "full_scale", "qwen_round_robin")
    traces_path = os.path.join(base, "traces", "traces.jsonl")
    annotations_path = os.path.join(base, "annotations", "annotations.jsonl")

    print("=== Heuristic Ack Detector Evaluation ===")
    print(f"{'Threshold':<12} {'Precision':<12} {'Recall':<10} {'F1':<8} {'Pred_ack':<10} {'True_ack':<10}")

    best_f1 = 0
    best_threshold = 80
    for threshold in [30, 50, 80, 100, 150, 200, 300]:
        result = evaluate_heuristic(traces_path, annotations_path, threshold)
        print(f"{threshold:<12} {result['precision']:<12} {result['recall']:<10} {result['f1']:<8} {result['predicted_ack']:<10} {result['true_ack']:<10}")
        if result['f1'] > best_f1:
            best_f1 = result['f1']
            best_threshold = threshold

    print(f"\nBest threshold: {best_threshold} (F1={best_f1:.4f})")

    final = evaluate_heuristic(traces_path, annotations_path, best_threshold)
    print(f"\nFinal results (threshold={best_threshold}):")
    print(json.dumps(final, indent=2))

    heuristic_ann_path = os.path.join(base, "annotations_heuristic", "annotations.jsonl")
    generate_heuristic_annotations(traces_path, heuristic_ann_path, best_threshold)
    print(f"\nHeuristic annotations written to: {heuristic_ann_path}")
