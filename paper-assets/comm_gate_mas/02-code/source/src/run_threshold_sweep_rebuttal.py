#!/usr/bin/env python3
"""Threshold sensitivity sweep for rebuttal — Qwen and Llama on GSM8K."""
import json, os, re, sys
from datetime import datetime

# --- Paths ---
BASE = "/root/autodl-tmp/comm_gate_mas"
CONFIGS = {
    "Qwen_GSM8K": {
        "traces": f"{BASE}/outputs/full_scale/qwen_round_robin/traces/traces.jsonl",
        "annotations": f"{BASE}/outputs/full_scale/qwen_round_robin/annotations/annotations.jsonl",
    },
    "Llama_GSM8K": {
        "traces": f"{BASE}/outputs/full_scale/llama_round_robin/traces/traces.jsonl",
        "annotations": f"{BASE}/outputs/full_scale/llama_round_robin/annotations/annotations.jsonl",
    },
}
THRESHOLDS = [10, 15, 20, 25, 30, 35, 40, 50, 60, 75, 100, 150, 200]
OUTPUT_DIR = f"{BASE}/artifacts/rebuttal"

# --- Qwen heuristic (parametric char_threshold) ---
ACK_PATTERNS = [
    r"^(the answer is|my answer is|final answer)",
    r"^(i agree|i concur|that'?s correct|you'?re right|correct)",
    r"^(yes,?\s|absolutely|exactly|indeed)",
    r"^(i confirm|confirmed|verified)",
    r"^(good|great|nice|well done)",
]
VERBOSE_ACK_PATTERNS = [
    r"^(the answer is|my answer is).*\b(correct|indeed|right)\b",
    r"^(your|the) (solution|calculation|answer|approach|reasoning) (is|are) (correct|right|indeed)",
    r"^(i agree|i concur|that'?s correct|exactly right|absolutely correct)",
    r"^(great|excellent|well done|good job|nice work)",
]

def qwen_is_ack(text: str, char_threshold: int) -> bool:
    ts = text.strip()
    if len(ts) < char_threshold:
        return True
    tl = ts.lower()
    for p in ACK_PATTERNS:
        if re.match(p, tl):
            if len(ts) <= 200:
                return True
            break
    if len(ts) <= 300:
        for p in VERBOSE_ACK_PATTERNS:
            if re.match(p, tl):
                return True
    return False

# --- Llama heuristic (parametric len_threshold) ---
LLAMA_ACK_KW = [
    "i'm glad", "you've broken", "your step-by-step",
    "your rephrased", "i appreciate the", "you've provided",
    "your solution is correct", "the answer is indeed",
]
LLAMA_NONACK_KW = [
    "here's another", "i have another", "let's break down",
    "let me solve", "i have a new", "i need help",
    "can you help", "solve this", "please solve",
]
OVERLAP_THRESHOLD = 0.3

def _four_gram_overlap(cur: str, prev: str) -> float:
    cw, pw = cur.lower().split(), prev.lower().split()
    if len(cw) < 4 or len(pw) < 4:
        return 0.0
    c4 = set(tuple(cw[i:i+4]) for i in range(len(cw)-3))
    p4 = set(tuple(pw[i:i+4]) for i in range(len(pw)-3))
    return len(c4 & p4) / len(c4) if c4 else 0.0

def llama_is_ack(text: str, prev_text: str, len_threshold: int) -> bool:
    tl = text.lower()
    if any(kw in tl for kw in LLAMA_NONACK_KW):
        return False
    if "however" in tl[:300]:
        return False
    if any(kw in tl[:300] for kw in LLAMA_ACK_KW):
        return True
    if len(text.strip()) < len_threshold:
        return True
    if prev_text and _four_gram_overlap(text, prev_text) > OVERLAP_THRESHOLD:
        return True
    return False

# --- Evaluation ---
def load_labels(ann_path):
    labels = {}
    with open(ann_path) as f:
        for line in f:
            if not line.strip(): continue
            rec = json.loads(line)
            tid = rec["task_id"]
            midx = rec["message_index"]
            ann_a = rec.get("annotation_a", {})
            ann_s = rec.get("annotation", {})
            fn_type = ann_a.get("type") or ann_s.get("type") or "unknown"
            labels[(tid, midx)] = (fn_type == "acknowledgment")
    return labels

def load_traces(traces_path):
    traces = {}
    with open(traces_path) as f:
        for line in f:
            if not line.strip(): continue
            rec = json.loads(line)
            traces[rec["task_id"]] = rec.get("messages", [])
    return traces

def evaluate(labels, traces, model_type, threshold):
    tp = fp = fn = tn = 0
    total = 0
    for (tid, midx), is_ack_gt in labels.items():
        if tid not in traces:
            continue
        msgs = traces[tid]
        target_round = midx + 1
        text = ""
        prev_text = ""
        for i, m in enumerate(msgs):
            if m.get("round", 0) == target_round:
                text = m.get("content", "")
                break
            if m.get("round", 0) == target_round - 1:
                prev_text = m.get("content", "")

        if model_type == "qwen":
            pred = qwen_is_ack(text, threshold)
        else:
            pred = llama_is_ack(text, prev_text, threshold)

        total += 1
        if pred and is_ack_gt: tp += 1
        elif pred and not is_ack_gt: fp += 1
        elif not pred and is_ack_gt: fn += 1
        else: tn += 1

    prec = tp/(tp+fp) if (tp+fp) else 0
    rec = tp/(tp+fn) if (tp+fn) else 0
    f1 = 2*prec*rec/(prec+rec) if (prec+rec) else 0
    prune_pct = (tp+fp)/total*100 if total else 0
    return {
        "threshold": threshold,
        "precision": round(prec, 4),
        "recall": round(rec, 4),
        "f1": round(f1, 4),
        "prune_pct": round(prune_pct, 2),
        "tp": tp, "fp": fp, "fn": fn, "tn": tn, "total": total
    }

# --- Main ---
def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_results = {}

    for name, cfg in CONFIGS.items():
        print(f"\n{'='*60}")
        print(f"  {name}")
        print(f"{'='*60}")
        model_type = "qwen" if "Qwen" in name else "llama"
        labels = load_labels(cfg["annotations"])
        traces = load_traces(cfg["traces"])
        print(f"  Annotations: {len(labels)}, Traces: {len(traces)}")

        results = []
        for t in THRESHOLDS:
            r = evaluate(labels, traces, model_type, t)
            results.append(r)
            print(f"  threshold={t:>3d}: P={r['precision']:.3f} R={r['recall']:.3f} F1={r['f1']:.3f} prune={r['prune_pct']:.1f}%")

        # Robustness check
        f1_mid = [r["f1"] for r in results if 20 <= r["threshold"] <= 100]
        f1_range = max(f1_mid) - min(f1_mid) if f1_mid else 0
        print(f"\n  Robustness [20-100]: F1 range = {min(f1_mid):.3f}–{max(f1_mid):.3f}, delta={f1_range:.4f}")
        print(f"  {'STABLE' if f1_range < 0.05 else 'UNSTABLE'} (threshold: delta < 0.05)")

        all_results[name] = {
            "model_type": model_type,
            "thresholds": results,
            "robustness": {
                "range_20_100": {"min_f1": min(f1_mid), "max_f1": max(f1_mid), "delta": round(f1_range, 4)},
                "stable": f1_range < 0.05
            }
        }

    # Save JSON
    output = {
        "metadata": {
            "generated": datetime.now().isoformat(),
            "thresholds_swept": THRESHOLDS,
            "method": "heuristic_ack_detection_with_char_threshold_sweep",
        },
        "results": all_results
    }
    json_path = os.path.join(OUTPUT_DIR, "a1_threshold_sensitivity.json")
    with open(json_path, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\n\nJSON saved: {json_path}")

    # Generate summary markdown
    md_lines = ["# A1: Heuristic Threshold Sensitivity Analysis\n"]
    md_lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    
    for name, data in all_results.items():
        md_lines.append(f"\n## {name}\n")
        md_lines.append("| Threshold | Precision | Recall | F1 | Prune% |")
        md_lines.append("|-----------|-----------|--------|------|--------|")
        for r in data["thresholds"]:
            md_lines.append(f"| {r['threshold']:>3d} | {r['precision']:.3f} | {r['recall']:.3f} | {r['f1']:.3f} | {r['prune_pct']:.1f}% |")
        rob = data["robustness"]["range_20_100"]
        md_lines.append(f"\n**Robustness [20–100]:** F1 ∈ [{rob['min_f1']:.3f}, {rob['max_f1']:.3f}], Δ = {rob['delta']:.4f} → {'STABLE' if data['robustness']['stable'] else 'UNSTABLE'}")

    # Overall conclusion
    md_lines.append("\n## Key Findings\n")
    all_stable = all(d["robustness"]["stable"] for d in all_results.values())
    min_f1_all = min(d["robustness"]["range_20_100"]["min_f1"] for d in all_results.values())
    max_delta = max(d["robustness"]["range_20_100"]["delta"] for d in all_results.values())
    
    if all_stable:
        md_lines.append(f"- F1 remains stable (>{min_f1_all:.2f}) across thresholds [20–100] for both Qwen and Llama")
        md_lines.append(f"- Maximum F1 variation: Δ = {max_delta:.4f} (< 0.05 threshold)")
    else:
        md_lines.append(f"- Maximum F1 variation: Δ = {max_delta:.4f}")
        for name, data in all_results.items():
            status = "stable" if data["robustness"]["stable"] else "unstable"
            md_lines.append(f"- {name}: {status} (Δ = {data['robustness']['range_20_100']['delta']:.4f})")

    md_lines.append("\n## Rebuttal Statement\n")
    if all_stable:
        md_lines.append(f'> "Heuristic detection F1 remains stable (>{min_f1_all:.2f}) across char-length thresholds [20–100] for both Qwen×GSM8K and Llama×GSM8K (max Δ={max_delta:.4f}), confirming robustness to threshold selection."')
    else:
        md_lines.append(f'> "Threshold sensitivity analysis shows max Δ={max_delta:.4f} across [20–100] range."')

    md_path = os.path.join(OUTPUT_DIR, "a1_threshold_sensitivity_summary.md")
    with open(md_path, "w") as f:
        f.write("\n".join(md_lines) + "\n")
    print(f"Summary saved: {md_path}")

    # Try to generate plot
    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(1, 1, figsize=(8, 5))
        for name, data in all_results.items():
            ts = [r["threshold"] for r in data["thresholds"]]
            f1s = [r["f1"] for r in data["thresholds"]]
            ax.plot(ts, f1s, "o-", label=name, markersize=5)
        ax.set_xlabel("Char-length Threshold")
        ax.set_ylabel("F1 Score")
        ax.set_title("Heuristic Ack Detection: Threshold Sensitivity")
        ax.legend()
        ax.grid(True, alpha=0.3)
        ax.set_ylim(0, 1.05)
        ax.axhspan(min_f1_all - 0.025, min_f1_all + max_delta + 0.025, alpha=0.1, color="green", label="Stable region")
        fig_path = os.path.join(OUTPUT_DIR, "a1_threshold_curve.png")
        plt.tight_layout()
        plt.savefig(fig_path, dpi=150)
        print(f"Plot saved: {fig_path}")
    except ImportError:
        print("matplotlib not available, skipping plot")

if __name__ == "__main__":
    main()
