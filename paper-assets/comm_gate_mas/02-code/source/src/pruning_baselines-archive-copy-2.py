#!/usr/bin/env python3
"""Pruning baseline comparison: Random + Position-based vs Function-guided."""

import json
import os
import random
import statistics
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "outputs" / "full_scale"
OUT_DIR = Path(__file__).resolve().parent.parent / "outputs" / "v7_analysis"
COMBOS = ["qwen_round_robin", "llama_round_robin", "gemma_round_robin"]


def load_jsonl(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                try:
                    rows.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
    return rows


def estimate_tokens(text):
    return int(len(text.split()) * 1.3)


def build_msg_key(row):
    return (row["task_id"], row["message_index"])


def load_combo_data(combo_name):
    combo_dir = BASE / combo_name
    annotations = load_jsonl(combo_dir / "annotations" / "annotations.jsonl")
    impacts = load_jsonl(combo_dir / "local_impact" / "impact.jsonl")
    traces = load_jsonl(combo_dir / "traces" / "traces.jsonl")

    ann_by_key = {build_msg_key(a): a for a in annotations}
    impact_by_key = {build_msg_key(i): i for i in impacts}

    task_correct = {}
    msg_text = {}
    msg_round = {}
    for trace in traces:
        task_correct[trace["task_id"]] = trace.get("is_correct", False)
        for i, msg in enumerate(trace["messages"]):
            key = (trace["task_id"], i)
            msg_text[key] = msg["content"]
            msg_round[key] = msg["round"]

    correct_tasks = {t for t, c in task_correct.items() if c}

    messages = []
    for key, ann in ann_by_key.items():
        func = ann["annotation_a"]["type"]
        text = msg_text.get(key, ann.get("content_preview", ""))
        tokens = estimate_tokens(text)
        impact = impact_by_key.get(key)
        action_level = impact["neutralize"]["action_level"] if impact else None
        is_final_answer_change = action_level == "final_answer"
        rnd = msg_round.get(key, 0)

        messages.append({
            "key": key,
            "task_id": key[0],
            "func": func,
            "tokens": tokens,
            "round": rnd,
            "is_final_answer_change": is_final_answer_change,
            "task_is_correct": key[0] in correct_tasks,
        })

    return messages, correct_tasks


def accuracy_risk(pruned_msgs, correct_tasks):
    """Fraction of correct tasks that lose their answer when pruned messages are removed."""
    if not correct_tasks:
        return 0.0
    tasks_at_risk = set()
    for m in pruned_msgs:
        if m["is_final_answer_change"] and m["task_id"] in correct_tasks:
            tasks_at_risk.add(m["task_id"])
    return len(tasks_at_risk) / len(correct_tasks) * 100


def random_pruning(messages, correct_tasks, total_tokens):
    seeds = list(range(42, 52))
    targets = list(range(10, 100, 10))
    points = []

    for target_pct in targets:
        n_to_prune = max(1, int(len(messages) * target_pct / 100))
        risks = []
        savings = []

        for seed in seeds:
            rng = random.Random(seed)
            pruned = rng.sample(messages, n_to_prune)
            risk = accuracy_risk(pruned, correct_tasks)
            tok_saved = sum(m["tokens"] for m in pruned)
            risks.append(risk)
            savings.append(tok_saved / total_tokens * 100)

        points.append({
            "target_pct": target_pct,
            "token_savings_pct": round(statistics.mean(savings), 2),
            "accuracy_risk_mean": round(statistics.mean(risks), 4),
            "accuracy_risk_std": round(statistics.stdev(risks), 4) if len(risks) > 1 else 0,
            "n_trials": len(seeds),
        })

    return {"points": points}


def position_based_pruning(messages, correct_tasks, total_tokens):
    max_round = max(m["round"] for m in messages)
    points = []

    for cutoff in range(max_round, 0, -1):
        pruned = [m for m in messages if m["round"] >= cutoff]
        if not pruned:
            continue
        risk = accuracy_risk(pruned, correct_tasks)
        tok_saved = sum(m["tokens"] for m in pruned)

        points.append({
            "rounds_removed_from": cutoff,
            "rounds_removed_count": max_round - cutoff + 1,
            "msgs_pruned": len(pruned),
            "token_savings_pct": round(tok_saved / total_tokens * 100, 2),
            "accuracy_risk_pct": round(risk, 4),
        })

    return {"points": points}


def function_guided_pruning(messages, correct_tasks, total_tokens):
    by_func = defaultdict(list)
    for m in messages:
        by_func[m["func"]].append(m)

    func_risk = {}
    for func, msgs in by_func.items():
        risk = accuracy_risk(msgs, correct_tasks)
        tok_share = sum(m["tokens"] for m in msgs) / total_tokens * 100
        func_risk[func] = (risk, -tok_share)

    ranked = sorted(func_risk.keys(), key=lambda f: func_risk[f])

    points = []
    cum_pruned = []
    for func in ranked:
        cum_pruned.extend(by_func[func])
        risk = accuracy_risk(cum_pruned, correct_tasks)
        tok_saved = sum(m["tokens"] for m in cum_pruned)
        points.append({
            "pruned_types": [f for f in ranked[:len(points) + 1]],
            "added_type": func,
            "msgs_pruned": len(cum_pruned),
            "token_savings_pct": round(tok_saved / total_tokens * 100, 2),
            "accuracy_risk_pct": round(risk, 4),
        })

    return {"points": points, "pruning_order": ranked}


def dominance_analysis(random_pts, position_pts, function_pts, correct_tasks):
    analysis = {}

    fg_points = [(p["token_savings_pct"], p["accuracy_risk_pct"]) for p in function_pts["points"]]
    rnd_points = [(p["token_savings_pct"], p["accuracy_risk_mean"]) for p in random_pts["points"]]
    pos_points = [(p["token_savings_pct"], p["accuracy_risk_pct"]) for p in position_pts["points"]]

    def max_safe_savings(points, threshold=0.0):
        safe = [s for s, r in points if r <= threshold]
        return round(max(safe), 2) if safe else 0.0

    fg_safe = max_safe_savings(fg_points)
    rnd_safe = max_safe_savings(rnd_points)
    pos_safe = max_safe_savings(pos_points)

    def advantage_at_savings(fg_pts, other_pts):
        results = []
        for fg_s, fg_r in fg_pts:
            closest = min(other_pts, key=lambda x: abs(x[0] - fg_s), default=None)
            if closest and abs(closest[0] - fg_s) < 15:
                results.append({
                    "savings_pct": fg_s,
                    "fg_risk": fg_r,
                    "other_risk": closest[1],
                    "other_savings": closest[0],
                    "risk_reduction": round(closest[1] - fg_r, 4),
                })
        return results

    fg_vs_rnd = advantage_at_savings(fg_points, rnd_points)
    fg_vs_pos = advantage_at_savings(fg_points, pos_points)

    fg_dominates_random = all(item["risk_reduction"] >= 0 for item in fg_vs_rnd) if fg_vs_rnd else False
    fg_dominates_position = all(item["risk_reduction"] >= 0 for item in fg_vs_pos) if fg_vs_pos else False

    analysis["function_vs_random"] = (
        f"function-guided {'dominates' if fg_dominates_random else 'does not dominate'} random; "
        f"max safe savings: fg={fg_safe}% vs random={rnd_safe}%"
    )
    analysis["function_vs_position"] = (
        f"function-guided {'dominates' if fg_dominates_position else 'does not dominate'} position-based; "
        f"max safe savings: fg={fg_safe}% vs position={pos_safe}%"
    )
    analysis["max_safe_savings"] = {
        "function_guided": fg_safe,
        "random": rnd_safe,
        "position_based": pos_safe,
    }
    analysis["detailed_comparison"] = {
        "fg_vs_random": fg_vs_rnd,
        "fg_vs_position": fg_vs_pos,
    }

    return analysis


def analyze_combo(combo_name):
    print(f"Analyzing {combo_name}...")
    messages, correct_tasks = load_combo_data(combo_name)
    total_tokens = sum(m["tokens"] for m in messages)

    rnd = random_pruning(messages, correct_tasks, total_tokens)
    pos = position_based_pruning(messages, correct_tasks, total_tokens)
    fg = function_guided_pruning(messages, correct_tasks, total_tokens)
    dom = dominance_analysis(rnd, pos, fg, correct_tasks)

    return {
        "n_messages": len(messages),
        "total_tokens": total_tokens,
        "n_correct_tasks": len(correct_tasks),
        "random": rnd,
        "position_based": pos,
        "function_guided": fg,
    }, dom


def main():
    per_backbone = {}
    dominance = {}

    for combo in COMBOS:
        combo_dir = BASE / combo
        if not (combo_dir / "local_impact" / "impact.jsonl").exists():
            print(f"Skipping {combo}: no impact data")
            continue
        result, dom = analyze_combo(combo)
        per_backbone[combo] = result
        dominance[combo] = dom

    output = {
        "per_backbone": per_backbone,
        "dominance_analysis": dominance,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = OUT_DIR / "pruning_baselines.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)
    print(f"\nOutput: {out_path}")

    for combo in per_backbone:
        res = per_backbone[combo]
        dom = dominance[combo]
        print(f"\n{'='*80}")
        print(f"{combo} ({res['n_messages']} msgs, {res['n_correct_tasks']} correct tasks)")
        print(f"{'='*80}")

        print("\n  Random pruning:")
        for p in res["random"]["points"]:
            print(f"    target={p['target_pct']:>2}%  savings={p['token_savings_pct']:>5.1f}%  "
                  f"risk={p['accuracy_risk_mean']:>6.2f}% ±{p['accuracy_risk_std']:.2f}")

        print("\n  Position-based pruning:")
        for p in res["position_based"]["points"]:
            print(f"    remove rounds≥{p['rounds_removed_from']}  ({p['msgs_pruned']} msgs)  "
                  f"savings={p['token_savings_pct']:>5.1f}%  risk={p['accuracy_risk_pct']:>6.2f}%")

        print("\n  Function-guided pruning:")
        for p in res["function_guided"]["points"]:
            print(f"    +{p['added_type']:<22}  savings={p['token_savings_pct']:>5.1f}%  "
                  f"risk={p['accuracy_risk_pct']:>6.2f}%")

        print(f"\n  Dominance: {dom['function_vs_random']}")
        print(f"  Dominance: {dom['function_vs_position']}")
        print(f"  Max safe savings (0% risk): fg={dom['max_safe_savings']['function_guided']}%, "
              f"random={dom['max_safe_savings']['random']}%, "
              f"position={dom['max_safe_savings']['position_based']}%")


if __name__ == "__main__":
    main()
