#!/usr/bin/env python3
"""Heuristic threshold sensitivity analysis for Qwen ack detection."""
import json, os, sys
from collections import defaultdict

TRACES_PATH = '/root/autodl-tmp/comm_gate_mas/outputs/full_scale/qwen_round_robin/traces/traces.jsonl'
ANN_PATH = '/root/autodl-tmp/comm_gate_mas/outputs/full_scale/qwen_round_robin/annotations/annotations.jsonl'
OUTPUT_PATH = '/root/autodl-tmp/comm_gate_mas/outputs/v7_analysis/heuristic_threshold_sweep.json'

annotations = {}
with open(ANN_PATH) as f:
    for line in f:
        if not line.strip(): continue
        rec = json.loads(line)
        task_id = rec.get('task_id', '')
        msg_idx = rec.get('message_index', 0)
        ann_a = rec.get('annotation_a', {})
        ann_s = rec.get('annotation', {})
        fn_type = ann_a.get('type') or ann_s.get('type') or 'unknown'
        annotations[(task_id, msg_idx)] = (fn_type == 'acknowledgment')

msg_lengths = {}
with open(TRACES_PATH) as f:
    for line in f:
        if not line.strip(): continue
        rec = json.loads(line)
        task_id = rec.get('task_id', '')
        messages = rec.get('messages', [])
        for idx, msg in enumerate(messages):
            content = msg.get('content', '')
            msg_lengths[(task_id, idx)] = len(content)

thresholds = [10, 15, 20, 25, 30, 35, 40, 50, 60, 75, 100, 150, 200]

results = []
for threshold in thresholds:
    tp = fp = fn = tn = 0
    total_msgs = 0
    pruned = 0

    for key, is_ack_gt in annotations.items():
        if key not in msg_lengths:
            continue
        length = msg_lengths[key]
        is_ack_pred = (length < threshold)
        total_msgs += 1

        if is_ack_pred:
            pruned += 1

        if is_ack_pred and is_ack_gt:
            tp += 1
        elif is_ack_pred and not is_ack_gt:
            fp += 1
        elif not is_ack_pred and is_ack_gt:
            fn += 1
        else:
            tn += 1

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0
    prune_pct = pruned / total_msgs * 100 if total_msgs > 0 else 0

    results.append({
        'threshold': threshold,
        'precision': round(precision, 4),
        'recall': round(recall, 4),
        'f1': round(f1, 4),
        'prune_pct': round(prune_pct, 2),
        'tp': tp, 'fp': fp, 'fn': fn, 'tn': tn,
        'total_msgs': total_msgs
    })

    print(f"threshold={threshold:>3d}: P={precision:.3f} R={recall:.3f} F1={f1:.3f} prune={prune_pct:.1f}%")

print("\n=== ROBUSTNESS CHECK ===")
f1_values = [r['f1'] for r in results if 20 <= r['threshold'] <= 50]
if f1_values:
    f1_range = max(f1_values) - min(f1_values)
    print(f"F1 range in [20,50] threshold: {min(f1_values):.3f} - {max(f1_values):.3f} (delta={f1_range:.3f})")
    print(f"Robustness claim: {'SUPPORTED' if f1_range < 0.05 else 'NOT SUPPORTED'} (delta < 5%)")

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
output = {
    'metadata': {
        'dataset': 'Qwen/GSM8K',
        'traces_path': TRACES_PATH,
        'annotations_path': ANN_PATH,
        'method': 'length_threshold_only',
        'total_annotations': len(annotations),
        'total_matched': results[0]['total_msgs'] if results else 0
    },
    'thresholds': results,
    'robustness': {
        'range_20_50': {
            'min_f1': min(f1_values) if f1_values else None,
            'max_f1': max(f1_values) if f1_values else None,
            'delta': f1_range if f1_values else None,
            'supported': f1_range < 0.05 if f1_values else False
        }
    }
}
with open(OUTPUT_PATH, 'w') as f:
    json.dump(output, f, indent=2)
print(f"\nSaved to {OUTPUT_PATH}")
