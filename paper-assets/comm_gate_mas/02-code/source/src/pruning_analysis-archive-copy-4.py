#!/usr/bin/env python3
"""Communication Pruning Analysis: accuracy vs token trade-off by function type.

Uses three complementary impact metrics:
1. action_change_rate — binary (ceiling effect, ~96-100%)
2. semantic_similarity — continuous (lower = higher impact after neutralize)
3. final_answer_change_rate — only counts messages where neutralization changes the final answer
4. task-level simulation — for correct tasks, estimates P(stays correct) when pruning a function type
"""

import json
import os
import statistics
from collections import defaultdict
from itertools import combinations
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "outputs" / "full_scale"
OUT_DIR = Path(__file__).resolve().parent.parent / "outputs" / "v7_analysis"

COMBOS = ["qwen_round_robin", "llama_round_robin", "gemma_round_robin"]
FUNC_TYPES = ["acknowledgment", "information_provision", "reasoning_guidance", "verification", "coordination"]


def load_jsonl(path):
    rows = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return rows


def get_function_type(ann):
    if ann.get("agreement"):
        return ann["annotation_a"]["type"]
    return ann["annotation_a"]["type"]


def estimate_tokens(text):
    return int(len(text.split()) * 1.3)


def build_msg_key(row):
    return (row["task_id"], row["message_index"])


def analyze_combo(combo_name):
    combo_dir = BASE / combo_name
    annotations = load_jsonl(combo_dir / "annotations" / "annotations.jsonl")
    impacts = load_jsonl(combo_dir / "local_impact" / "impact.jsonl")
    traces = load_jsonl(combo_dir / "traces" / "traces.jsonl")

    ann_by_key = {build_msg_key(a): a for a in annotations}
    impact_by_key = {build_msg_key(i): i for i in impacts}

    msg_text = {}
    task_msgs = defaultdict(list)
    for trace in traces:
        for i, msg in enumerate(trace["messages"]):
            key = (trace["task_id"], i)
            msg_text[key] = msg["content"]
            task_msgs[trace["task_id"]].append(i)

    task_correct = {}
    for trace in traces:
        task_correct[trace["task_id"]] = trace.get("is_correct", False)

    # Build per-message records: (key, func_type, tokens, impact_data)
    records = []
    for key, ann in ann_by_key.items():
        func = get_function_type(ann)
        text = msg_text.get(key, ann.get("content_preview", ""))
        tokens = estimate_tokens(text)
        impact = impact_by_key.get(key)
        records.append((key, func, tokens, impact))

    # Per-function statistics
    per_function = defaultdict(lambda: {
        "msg_count": 0, "total_tokens": 0, "token_list": [],
        "action_changed": 0, "final_answer_changed": 0, "action_total": 0,
        "sem_sims": [], "tasks_with_final_change": set(),
    })

    all_tokens = 0
    all_msg_count = 0

    for key, func, tokens, impact in records:
        pf = per_function[func]
        pf["msg_count"] += 1
        pf["total_tokens"] += tokens
        pf["token_list"].append(tokens)
        all_tokens += tokens
        all_msg_count += 1

        if impact:
            n = impact.get("neutralize", {})
            pf["action_total"] += 1
            al = n.get("action_level", "")

            if al in ("reasoning_step", "final_answer"):
                pf["action_changed"] += 1
            if al == "final_answer":
                pf["final_answer_changed"] += 1
                pf["tasks_with_final_change"].add(key[0])

            sim = n.get("semantic_similarity")
            if sim is not None:
                pf["sem_sims"].append(sim)

    # Task-level simulation: for each function type, compute fraction of correct tasks
    # that have at least one message of that type with final_answer change
    correct_tasks = {t for t, c in task_correct.items() if c}
    total_correct = len(correct_tasks)

    # Map: task_id -> set of func types that cause final_answer change
    task_critical_funcs = defaultdict(set)
    for key, func, tokens, impact in records:
        if impact:
            al = impact.get("neutralize", {}).get("action_level", "")
            if al == "final_answer":
                task_critical_funcs[key[0]].add(func)

    per_func_out = {}
    for func in FUNC_TYPES:
        pf = per_function.get(func)
        if pf is None or pf["msg_count"] == 0:
            per_func_out[func] = {
                "msg_count": 0, "msg_share_pct": 0, "avg_tokens": 0,
                "total_tokens": 0, "token_share_pct": 0,
                "action_change_rate": None, "final_answer_change_rate": None,
                "avg_semantic_similarity": None, "median_semantic_similarity": None,
                "tasks_with_final_change": 0, "accuracy_risk_pct": None,
            }
            continue

        acr = round(pf["action_changed"] / pf["action_total"], 4) if pf["action_total"] > 0 else None
        facr = round(pf["final_answer_changed"] / pf["action_total"], 4) if pf["action_total"] > 0 else None

        # Accuracy risk: fraction of correct tasks endangered by pruning this type
        tasks_at_risk = correct_tasks & pf["tasks_with_final_change"]
        acc_risk = round(len(tasks_at_risk) / total_correct * 100, 2) if total_correct > 0 else 0

        per_func_out[func] = {
            "msg_count": pf["msg_count"],
            "msg_share_pct": round(pf["msg_count"] / all_msg_count * 100, 2),
            "avg_tokens": round(pf["total_tokens"] / pf["msg_count"], 1),
            "total_tokens": pf["total_tokens"],
            "token_share_pct": round(pf["total_tokens"] / all_tokens * 100, 2) if all_tokens > 0 else 0,
            "action_change_rate": acr,
            "final_answer_change_rate": facr,
            "avg_semantic_similarity": round(statistics.mean(pf["sem_sims"]), 4) if pf["sem_sims"] else None,
            "median_semantic_similarity": round(statistics.median(pf["sem_sims"]), 4) if pf["sem_sims"] else None,
            "tasks_with_final_change": len(pf["tasks_with_final_change"]),
            "accuracy_risk_pct": acc_risk,
        }

    # === Pruning scenarios ===
    def compute_scenario(func_list):
        token_savings = sum(per_func_out[f]["token_share_pct"] for f in func_list)
        msgs_pruned = sum(per_func_out[f]["msg_count"] for f in func_list)

        # Accuracy retention based on final_answer changes
        total_fa_changed = sum(per_function[f]["final_answer_changed"] for f in func_list)
        total_impact = sum(per_function[f]["action_total"] for f in func_list)
        fa_rate = total_fa_changed / total_impact if total_impact > 0 else 0

        # Task-level: how many correct tasks lose their answer
        tasks_at_risk = set()
        for f in func_list:
            tasks_at_risk |= (correct_tasks & per_function[f]["tasks_with_final_change"])
        task_acc_retention = round((1 - len(tasks_at_risk) / total_correct) * 100, 2) if total_correct > 0 else 100

        # Semantic similarity (avg across pruned types)
        all_sims = []
        for f in func_list:
            all_sims.extend(per_function[f]["sem_sims"])
        avg_sim = round(statistics.mean(all_sims), 4) if all_sims else None

        return {
            "pruned_types": func_list,
            "token_savings_pct": round(token_savings, 2),
            "msgs_pruned": msgs_pruned,
            "final_answer_change_rate": round(fa_rate, 4),
            "task_accuracy_retention_pct": task_acc_retention,
            "avg_semantic_similarity": avg_sim,
        }

    scenarios = []
    active_funcs = [f for f in FUNC_TYPES if per_func_out[f]["msg_count"] > 0]

    # Single-type
    for func in active_funcs:
        scenarios.append(compute_scenario([func]))

    # Two-type combos
    for combo in combinations(active_funcs, 2):
        scenarios.append(compute_scenario(list(combo)))

    # Three-type combos
    for combo in combinations(active_funcs, 3):
        scenarios.append(compute_scenario(list(combo)))

    # Greedy cumulative: sort by accuracy_risk ascending, then by token_share descending
    ranked = sorted(
        [(f, per_func_out[f]) for f in active_funcs],
        key=lambda x: (x[1].get("accuracy_risk_pct", 0) or 0, -(x[1].get("token_share_pct", 0)))
    )

    cumulative = []
    cum_types = []
    for func, _ in ranked:
        cum_types.append(func)
        cumulative.append(compute_scenario(list(cum_types)))

    # Pareto front (token_savings vs task_accuracy_retention)
    valid = [s for s in scenarios if s["task_accuracy_retention_pct"] is not None]
    valid.sort(key=lambda x: x["token_savings_pct"])
    pareto = []
    best_ret = -1
    for s in valid:
        if s["task_accuracy_retention_pct"] >= best_ret:
            pareto.append(s)
            best_ret = s["task_accuracy_retention_pct"]

    # Best trade-off: maximize token_savings * accuracy_retention
    best = max(
        (s for s in scenarios if s["task_accuracy_retention_pct"] is not None),
        key=lambda s: s["token_savings_pct"] * s["task_accuracy_retention_pct"] / 100,
        default=None
    )
    rec = ""
    if best:
        rec = (f"Prune {'+'.join(best['pruned_types'])} for {best['token_savings_pct']:.1f}% token savings "
               f"with {best['task_accuracy_retention_pct']:.1f}% task accuracy retention "
               f"(final_answer change rate: {best['final_answer_change_rate']:.2%})")

    return {
        "total_messages": all_msg_count,
        "total_tokens": all_tokens,
        "total_tasks": len(task_correct),
        "total_correct_tasks": total_correct,
        "baseline_accuracy": round(total_correct / len(task_correct) * 100, 2) if task_correct else None,
        "per_function": per_func_out,
        "pruning_scenarios": scenarios,
        "pruning_cumulative_greedy": cumulative,
        "pareto_front": pareto,
        "greedy_pruning_order": [f for f, _ in ranked],
        "recommendation": rec,
    }


def cross_backbone_summary(results):
    summary = {}
    for func in FUNC_TYPES:
        func_data = {}
        for bb, res in results.items():
            pf = res["per_function"].get(func, {})
            func_data[bb] = {
                "msg_count": pf.get("msg_count", 0),
                "token_share_pct": pf.get("token_share_pct", 0),
                "action_change_rate": pf.get("action_change_rate"),
                "final_answer_change_rate": pf.get("final_answer_change_rate"),
                "accuracy_risk_pct": pf.get("accuracy_risk_pct"),
                "avg_semantic_similarity": pf.get("avg_semantic_similarity"),
            }
        summary[func] = func_data

    # Safest to prune: lowest accuracy_risk across backbones, highest token savings
    safe_funcs = []
    for func in FUNC_TYPES:
        risks = [summary[func][bb].get("accuracy_risk_pct", 0) or 0 for bb in results]
        tokens = [summary[func][bb].get("token_share_pct", 0) for bb in results]
        if risks:
            safe_funcs.append({
                "type": func,
                "max_accuracy_risk_pct": max(risks),
                "avg_token_share_pct": round(sum(tokens) / len(tokens), 2),
                "avg_semantic_similarity": round(
                    statistics.mean([summary[func][bb]["avg_semantic_similarity"]
                                     for bb in results if summary[func][bb].get("avg_semantic_similarity") is not None]),
                    4
                ) if any(summary[func][bb].get("avg_semantic_similarity") is not None for bb in results) else None,
            })
    safe_funcs.sort(key=lambda x: (x["max_accuracy_risk_pct"], -x["avg_token_share_pct"]))

    return {
        "per_function_across_backbones": summary,
        "pruning_priority": safe_funcs,
        "backbones_analyzed": list(results.keys()),
    }


def main():
    results = {}
    for combo in COMBOS:
        combo_dir = BASE / combo
        if not (combo_dir / "local_impact" / "impact.jsonl").exists():
            print(f"Skipping {combo}: no impact data")
            continue
        print(f"Analyzing {combo}...")
        results[combo] = analyze_combo(combo)

    output = {
        "per_backbone": results,
        "cross_backbone_summary": cross_backbone_summary(results),
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = OUT_DIR / "pruning_analysis.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\nOutput: {out_path}")

    # Print summary
    print("\n" + "=" * 90)
    print("PRUNING ANALYSIS SUMMARY")
    print("=" * 90)
    for combo, res in results.items():
        print(f"\n{'='*90}")
        print(f"{combo} | baseline accuracy: {res['baseline_accuracy']}% | {res['total_correct_tasks']}/{res['total_tasks']} correct")
        print(f"{'='*90}")
        print(f"{'Function':<22} {'Msgs':>5} {'TokShr%':>8} {'AvgTok':>7} {'ActChg%':>8} {'FinalAns%':>10} {'AccRisk%':>9} {'AvgSemSim':>10}")
        print("-" * 90)
        for func in FUNC_TYPES:
            pf = res["per_function"].get(func, {})
            acr = pf.get("action_change_rate")
            facr = pf.get("final_answer_change_rate")
            arisk = pf.get("accuracy_risk_pct")
            sim = pf.get("avg_semantic_similarity")
            print(f"{func:<22} {pf.get('msg_count',0):>5} {pf.get('token_share_pct',0):>7.1f}% "
                  f"{pf.get('avg_tokens',0):>7.1f} "
                  f"{acr*100 if acr is not None else 0:>7.1f}% "
                  f"{facr*100 if facr is not None else 0:>9.1f}% "
                  f"{arisk if arisk is not None else 0:>8.1f}% "
                  f"{sim if sim is not None else 0:>10.4f}")

        print(f"\nGreedy pruning order: {' → '.join(res['greedy_pruning_order'])}")
        print(f"Recommendation: {res['recommendation']}")

        print(f"\nCumulative greedy pruning:")
        for step in res["pruning_cumulative_greedy"]:
            print(f"  + {step['pruned_types'][-1]:<22} → save {step['token_savings_pct']:>5.1f}% tokens, "
                  f"retain {step['task_accuracy_retention_pct']:>5.1f}% accuracy, "
                  f"FA change: {step['final_answer_change_rate']:.2%}")

    # Cross-backbone summary
    print(f"\n{'='*90}")
    print("CROSS-BACKBONE PRUNING PRIORITY")
    print(f"{'='*90}")
    for item in output["cross_backbone_summary"]["pruning_priority"]:
        print(f"  {item['type']:<22} max_risk={item['max_accuracy_risk_pct']:>5.1f}%  "
              f"avg_tok_share={item['avg_token_share_pct']:>5.1f}%  "
              f"avg_sem_sim={item.get('avg_semantic_similarity', 'N/A')}")


if __name__ == "__main__":
    main()
