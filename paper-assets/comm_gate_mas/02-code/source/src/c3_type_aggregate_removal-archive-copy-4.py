"""C3: Type-level aggregate removal control experiment.

For each function type, remove ALL messages of that type from Qwen/GSM8K
offline traces and measure accuracy impact. Tests whether cascade dissolution
is ack-specific or a general property of aggregate removal.

Input: traces.jsonl + annotations.jsonl (offline)
Output: per-type Δ, McNemar exact test, message counts
"""

import json
import re
import sys
from pathlib import Path
from scipy.stats import binomtest


def extract_gsm8k_answer(text: str) -> str | None:
    patterns = [
        r'[Tt]he answer is\s*\$?\\?boxed\{([^}]+)\}',
        r'[Tt]he answer is\s*\$?\s*([+-]?\d[\d,]*\.?\d*)',
        r'####\s*([+-]?\d[\d,]*\.?\d*)',
        r'\$?\s*\\?boxed\{([^}]+)\}',
    ]
    for pat in patterns:
        m = re.findall(pat, text)
        if m:
            val = m[-1].replace(",", "").strip().rstrip(".")
            return val
    nums = re.findall(r'[+-]?\d[\d,]*\.?\d*', text)
    return nums[-1].replace(",", "") if nums else None


def check_answer(pred, truth) -> bool:
    if pred is None:
        return False
    try:
        return abs(float(pred) - float(str(truth).replace(",", ""))) < 1e-3
    except (ValueError, TypeError):
        return str(pred).strip() == str(truth).strip()


def load_annotations(ann_path: str) -> dict[str, str]:
    labels = {}
    with open(ann_path) as f:
        for line in f:
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            msg_idx = rec["message_index"]
            rnd = msg_idx + 1
            key = f"{task_id}_r{rnd}"
            ann_a = rec.get("annotation_a", {})
            ann_single = rec.get("annotation", {})
            fn_type = ann_a.get("type") or ann_single.get("type") or "unknown"
            labels[key] = fn_type
    return labels


def run_experiment(traces_path: str, annotations: dict[str, str],
                   prune_type: str | None, num_tasks: int = 200):
    """Run offline removal for one function type. prune_type=None for baseline."""
    results = []
    with open(traces_path) as f:
        for i, line in enumerate(f):
            if i >= num_tasks:
                break
            if not line.strip():
                continue
            rec = json.loads(line)
            task_id = rec["task_id"]
            ground_truth = rec["ground_truth"]

            remaining_msgs = []
            pruned_count = 0
            total_agent_msgs = 0

            for msg in rec.get("messages", []):
                rnd = msg.get("round", 0)
                if rnd == 0:
                    remaining_msgs.append(msg)
                    continue

                total_agent_msgs += 1
                key = f"{task_id}_r{rnd}"
                fn_type = annotations.get(key, "unknown")

                if prune_type and fn_type == prune_type:
                    pruned_count += 1
                else:
                    remaining_msgs.append(msg)

            final_answer = None
            for msg in reversed(remaining_msgs):
                final_answer = extract_gsm8k_answer(msg.get("content", ""))
                if final_answer is not None:
                    break

            correct = check_answer(final_answer, ground_truth)
            results.append({
                "task_id": task_id,
                "correct": correct,
                "pruned_count": pruned_count,
                "total_agent_msgs": total_agent_msgs,
            })

    return results


def mcnemar_exact(baseline_results, pruned_results):
    """McNemar exact test (two-sided binomial test on discordant pairs)."""
    b = 0  # baseline correct, pruned wrong
    c = 0  # baseline wrong, pruned correct
    for base, prune in zip(baseline_results, pruned_results):
        if base["correct"] and not prune["correct"]:
            b += 1
        elif not base["correct"] and prune["correct"]:
            c += 1

    n_discord = b + c
    if n_discord == 0:
        return {"b": b, "c": c, "n_discordant": 0, "p_value": 1.0}

    p = binomtest(b, n_discord, 0.5).pvalue
    return {"b": b, "c": c, "n_discordant": n_discord, "p_value": round(p, 6)}


def main():
    traces_path = "outputs/full_scale/qwen_round_robin/traces/traces.jsonl"
    ann_path = "outputs/full_scale/qwen_round_robin/annotations/annotations.jsonl"

    base_dir = Path(__file__).parent.parent
    traces_path = str(base_dir / traces_path)
    ann_path = str(base_dir / ann_path)

    num_tasks = 200
    function_types = [
        "acknowledgment",
        "reasoning_guidance",
        "verification",
        "information_provision",
        "coordination",
    ]

    print(f"Loading annotations from {ann_path}")
    annotations = load_annotations(ann_path)
    print(f"Loaded {len(annotations)} annotation labels")

    type_counts = {}
    for v in annotations.values():
        type_counts[v] = type_counts.get(v, 0) + 1
    print(f"Type distribution: {json.dumps(type_counts, indent=2)}")

    print(f"\nRunning baseline (no pruning, N={num_tasks})...")
    baseline = run_experiment(traces_path, annotations, None, num_tasks)
    baseline_acc = sum(1 for r in baseline if r["correct"]) / len(baseline)
    print(f"Baseline accuracy: {baseline_acc*100:.1f}% ({sum(1 for r in baseline if r['correct'])}/{len(baseline)})")

    print(f"\n{'='*80}")
    print(f"{'Type':<25} {'Acc%':>6} {'Δ(pp)':>7} {'Pruned':>7} {'McNemar p':>10} {'b':>4} {'c':>4} {'Sig':>5}")
    print(f"{'='*80}")
    print(f"{'baseline':<25} {baseline_acc*100:>6.1f} {'---':>7} {'0':>7} {'---':>10} {'':>4} {'':>4} {'':>5}")

    results_summary = {"baseline_acc": baseline_acc, "n_tasks": num_tasks, "types": {}}

    for fn_type in function_types:
        pruned = run_experiment(traces_path, annotations, fn_type, num_tasks)
        pruned_acc = sum(1 for r in pruned if r["correct"]) / len(pruned)
        delta_pp = (pruned_acc - baseline_acc) * 100
        total_pruned = sum(r["pruned_count"] for r in pruned)

        mcnemar = mcnemar_exact(baseline, pruned)
        sig = "*" if mcnemar["p_value"] < 0.05 else "NS"

        print(f"{fn_type:<25} {pruned_acc*100:>6.1f} {delta_pp:>+7.1f} {total_pruned:>7} {mcnemar['p_value']:>10.4f} {mcnemar['b']:>4} {mcnemar['c']:>4} {sig:>5}")

        results_summary["types"][fn_type] = {
            "accuracy": round(pruned_acc, 4),
            "delta_pp": round(delta_pp, 2),
            "total_pruned_msgs": total_pruned,
            "mcnemar_b": mcnemar["b"],
            "mcnemar_c": mcnemar["c"],
            "mcnemar_p": mcnemar["p_value"],
            "significant_005": mcnemar["p_value"] < 0.05,
        }

    print(f"{'='*80}")

    out_path = str(base_dir / "outputs" / "c3_type_aggregate_removal.json")
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results_summary, f, indent=2)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
