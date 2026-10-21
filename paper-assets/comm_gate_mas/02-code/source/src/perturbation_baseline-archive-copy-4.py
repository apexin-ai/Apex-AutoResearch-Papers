#!/usr/bin/env python3
"""Perturbation-guided pruning baseline: does sim_remove predict prunability?

Compares three message pruning strategies at matched volume (K msgs per task):
  (a) Ack-only: remove acknowledgment messages
  (b) Perturbation-guided: remove messages with highest sim_remove (least disruptive by perturbation)
  (c) Random: remove K messages randomly (100 trials, mean ± std)

K is determined per-task as the number of ack messages among messages with
impact data (message indices 1-3, i.e., rounds 2-4).

Accuracy is estimated via per-message ablation data: a task is "at risk" if any
removed message has remove.action_level == "final_answer" (i.e., removing it
changed the extracted answer in the ablated response). This is conservative —
it treats any answer-changing removal as incorrect.

Input:
  outputs/full_scale/{combo}/annotations/annotations.jsonl
  outputs/full_scale/{combo}/local_impact/impact.jsonl
  outputs/full_scale/{combo}/traces/traces.jsonl

Output:
  outputs/v7_analysis/perturbation_baseline.json
"""

import json
import os
import random
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from scipy.stats import chi2 as chi2_dist

BASE = Path(__file__).resolve().parent.parent / "outputs" / "full_scale"
OUT_DIR = Path(__file__).resolve().parent.parent / "outputs" / "v7_analysis"
COMBOS = ["qwen_round_robin", "llama_round_robin"]
N_RANDOM_TRIALS = 100


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


def get_function_type(ann_record):
    ann_a = ann_record.get("annotation_a", {})
    ann_single = ann_record.get("annotation", {})
    return ann_a.get("type") or ann_single.get("type") or "unknown"


def load_combo(combo_name):
    """Load and join annotations, impact, and traces for one backbone×topology."""
    combo_dir = BASE / combo_name

    annotations = load_jsonl(combo_dir / "annotations" / "annotations.jsonl")
    impacts = load_jsonl(combo_dir / "local_impact" / "impact.jsonl")
    traces = load_jsonl(combo_dir / "traces" / "traces.jsonl")

    ann_by_key = {}
    for a in annotations:
        key = (a["task_id"], a["message_index"])
        ann_by_key[key] = get_function_type(a)

    impact_by_key = {}
    for imp in impacts:
        key = (imp["task_id"], imp["message_index"])
        impact_by_key[key] = {
            "sim_remove": imp["remove"]["semantic_similarity"],
            "action_level_remove": imp["remove"]["action_level"],
        }

    task_correct = {}
    for trace in traces:
        task_correct[trace["task_id"]] = trace.get("is_correct", False)

    # Per-task message list: only messages with BOTH annotation and impact data
    task_messages = defaultdict(list)
    for key in sorted(impact_by_key.keys()):
        if key not in ann_by_key:
            continue
        tid, midx = key
        task_messages[tid].append({
            "task_id": tid,
            "message_index": midx,
            "func_type": ann_by_key[key],
            "sim_remove": impact_by_key[key]["sim_remove"],
            "action_level_remove": impact_by_key[key]["action_level_remove"],
        })

    return task_messages, task_correct


def per_functype_diagnostics(task_messages):
    """Per-function-type sim_remove and action_level breakdown across all messages."""
    from collections import Counter, defaultdict
    sims = defaultdict(list)
    action_counts = defaultdict(lambda: Counter())
    for msgs in task_messages.values():
        for m in msgs:
            ft = m["func_type"]
            sims[ft].append(m["sim_remove"])
            action_counts[ft][m["action_level_remove"]] += 1

    result = {}
    for ft in sorted(sims.keys()):
        s = sims[ft]
        acts = action_counts[ft]
        total = sum(acts.values())
        result[ft] = {
            "n": len(s),
            "sim_remove_mean": round(float(np.mean(s)), 4),
            "sim_remove_std": round(float(np.std(s)), 4),
            "final_answer_risk_pct": round(acts.get("final_answer", 0) / total * 100, 1) if total else 0,
            "action_level_counts": dict(acts),
        }
    return result


def mcnemar_pvalue(correct_a, correct_b):
    """McNemar test (continuity-corrected) on paired binary outcomes."""
    b = sum(1 for a, bb in zip(correct_a, correct_b) if a and not bb)
    c = sum(1 for a, bb in zip(correct_a, correct_b) if not a and bb)
    if b + c == 0:
        return 1.0
    chi2_stat = (abs(b - c) - 1) ** 2 / (b + c)
    return float(1 - chi2_dist.cdf(chi2_stat, df=1))


def analyze_combo(combo_name):
    task_messages, task_correct = load_combo(combo_name)
    functype_diag = per_functype_diagnostics(task_messages)

    # Per-task, per-strategy tracking
    ack_correct_list = []
    pert_correct_list = []
    rand_correct_trials = defaultdict(list)  # trial_idx -> [bool]

    ack_selected_types = []
    pert_selected_types = []
    rand_selected_types_agg = []

    ack_selected_sim = []
    pert_selected_sim = []

    ack_n_risk = 0
    pert_n_risk = 0
    rand_n_risk_trials = defaultdict(int)

    # Overlap tracking: per-task, are perturbation-selected msgs the same as ack msgs?
    overlap_counts = []  # fraction of perturbation-selected that are ack

    n_tasks = 0
    n_tasks_with_ack = 0
    n_correct_baseline = 0
    k_distribution = Counter()

    for tid in sorted(task_messages.keys()):
        msgs = task_messages[tid]
        is_correct = task_correct.get(tid, False)
        n_tasks += 1
        if is_correct:
            n_correct_baseline += 1

        ack_msgs = [m for m in msgs if m["func_type"] == "acknowledgment"]
        K = len(ack_msgs)
        k_distribution[K] += 1

        if K == 0:
            ack_correct_list.append(is_correct)
            pert_correct_list.append(is_correct)
            for t in range(N_RANDOM_TRIALS):
                rand_correct_trials[t].append(is_correct)
            continue

        n_tasks_with_ack += 1

        # (a) Ack-only
        ack_risk = any(m["action_level_remove"] == "final_answer" for m in ack_msgs)
        ack_correct_list.append(is_correct and not ack_risk)
        ack_selected_types.extend(m["func_type"] for m in ack_msgs)
        ack_selected_sim.extend(m["sim_remove"] for m in ack_msgs)
        if ack_risk and is_correct:
            ack_n_risk += 1

        # (b) Perturbation-guided: highest sim_remove first
        sorted_msgs = sorted(msgs, key=lambda m: m["sim_remove"], reverse=True)
        pert_selected = sorted_msgs[:K]
        pert_risk = any(m["action_level_remove"] == "final_answer" for m in pert_selected)
        pert_correct_list.append(is_correct and not pert_risk)
        pert_selected_types.extend(m["func_type"] for m in pert_selected)
        pert_selected_sim.extend(m["sim_remove"] for m in pert_selected)
        if pert_risk and is_correct:
            pert_n_risk += 1

        # Overlap: how many perturbation-selected are also ack?
        pert_keys = {(m["task_id"], m["message_index"]) for m in pert_selected}
        ack_keys = {(m["task_id"], m["message_index"]) for m in ack_msgs}
        overlap_counts.append(len(pert_keys & ack_keys) / K)

        # (c) Random
        for t in range(N_RANDOM_TRIALS):
            rng = random.Random(42 + t)
            rand_selected = rng.sample(msgs, K)
            rand_risk = any(m["action_level_remove"] == "final_answer" for m in rand_selected)
            rand_correct_trials[t].append(is_correct and not rand_risk)
            rand_selected_types_agg.extend(m["func_type"] for m in rand_selected)
            if rand_risk and is_correct:
                rand_n_risk_trials[t] += 1

    # --- Aggregate metrics ---
    baseline_acc = n_correct_baseline / n_tasks
    ack_acc = sum(ack_correct_list) / n_tasks
    pert_acc = sum(pert_correct_list) / n_tasks
    rand_accs = [sum(rand_correct_trials[t]) / n_tasks for t in range(N_RANDOM_TRIALS)]

    # McNemar: perturbation vs ack, perturbation vs random (median trial), ack vs random
    median_trial = int(np.median(range(N_RANDOM_TRIALS)))
    p_pert_ack = mcnemar_pvalue(pert_correct_list, ack_correct_list)
    p_pert_rand = mcnemar_pvalue(pert_correct_list, rand_correct_trials[median_trial])
    p_ack_rand = mcnemar_pvalue(ack_correct_list, rand_correct_trials[median_trial])

    # Function type distributions (normalized to proportions)
    def type_dist(counter):
        total = sum(counter.values())
        return {k: round(v / total, 4) for k, v in sorted(counter.items(), key=lambda x: -x[1])} if total else {}

    ack_dist = type_dist(Counter(ack_selected_types))
    pert_dist = type_dist(Counter(pert_selected_types))
    rand_dist_raw = Counter(rand_selected_types_agg)
    rand_dist = type_dist(Counter({k: v // N_RANDOM_TRIALS for k, v in rand_dist_raw.items()}))

    output = {
        "combo": combo_name,
        "n_tasks": n_tasks,
        "n_tasks_with_ack_in_impact_range": n_tasks_with_ack,
        "n_correct_baseline": n_correct_baseline,
        "baseline_accuracy": round(baseline_acc, 4),
        "k_distribution": dict(k_distribution),
        "strategies": {
            "ack_only": {
                "accuracy": round(ack_acc, 4),
                "delta_vs_baseline_pp": round((ack_acc - baseline_acc) * 100, 2),
                "n_at_risk": ack_n_risk,
                "accuracy_risk_pct": round(ack_n_risk / n_correct_baseline * 100, 2) if n_correct_baseline else 0,
                "mean_sim_remove": round(float(np.mean(ack_selected_sim)), 4) if ack_selected_sim else None,
                "std_sim_remove": round(float(np.std(ack_selected_sim)), 4) if ack_selected_sim else None,
                "func_type_distribution": ack_dist,
                "func_type_counts": dict(Counter(ack_selected_types)),
                "n_messages_selected": len(ack_selected_types),
            },
            "perturbation_guided": {
                "accuracy": round(pert_acc, 4),
                "delta_vs_baseline_pp": round((pert_acc - baseline_acc) * 100, 2),
                "n_at_risk": pert_n_risk,
                "accuracy_risk_pct": round(pert_n_risk / n_correct_baseline * 100, 2) if n_correct_baseline else 0,
                "mean_sim_remove": round(float(np.mean(pert_selected_sim)), 4) if pert_selected_sim else None,
                "std_sim_remove": round(float(np.std(pert_selected_sim)), 4) if pert_selected_sim else None,
                "func_type_distribution": pert_dist,
                "func_type_counts": dict(Counter(pert_selected_types)),
                "n_messages_selected": len(pert_selected_types),
            },
            "random": {
                "accuracy_mean": round(float(np.mean(rand_accs)), 4),
                "accuracy_std": round(float(np.std(rand_accs)), 4),
                "delta_vs_baseline_pp": round((float(np.mean(rand_accs)) - baseline_acc) * 100, 2),
                "n_at_risk_mean": round(float(np.mean([rand_n_risk_trials[t] for t in range(N_RANDOM_TRIALS)])), 2),
                "accuracy_risk_pct_mean": round(
                    float(np.mean([rand_n_risk_trials[t] / n_correct_baseline * 100
                                   for t in range(N_RANDOM_TRIALS)])), 2
                ) if n_correct_baseline else 0,
                "func_type_distribution": rand_dist,
                "n_trials": N_RANDOM_TRIALS,
            },
        },
        "mcnemar_p_values": {
            "perturbation_vs_ack_only": round(p_pert_ack, 6),
            "perturbation_vs_random": round(p_pert_rand, 6),
            "ack_only_vs_random": round(p_ack_rand, 6),
        },
        "per_functype_diagnostics": functype_diag,
        "overlap_analysis": {
            "mean_overlap_frac": round(float(np.mean(overlap_counts)), 4) if overlap_counts else None,
            "std_overlap_frac": round(float(np.std(overlap_counts)), 4) if overlap_counts else None,
            "interpretation": "Fraction of perturbation-selected messages that are also ack messages",
        },
    }

    return output


def print_summary(r):
    print(f"\n{'='*70}")
    print(f"{r['combo']} — {r['n_tasks']} tasks, {r['n_correct_baseline']} correct baseline")
    print(f"Baseline accuracy: {r['baseline_accuracy']:.1%}")
    print(f"K distribution (ack count per task): {r['k_distribution']}")
    print(f"Tasks with K>0: {r['n_tasks_with_ack_in_impact_range']}")
    print(f"{'='*70}")

    strats = r["strategies"]
    print(f"\n  {'Strategy':<25} {'Accuracy':>10} {'Δ(pp)':>8} {'Risk%':>8} {'sim̄':>8}")
    print(f"  {'-'*60}")

    s = strats["ack_only"]
    print(f"  {'Ack-only':<25} {s['accuracy']:>9.1%} {s['delta_vs_baseline_pp']:>+7.1f} "
          f"{s['accuracy_risk_pct']:>7.1f} {s['mean_sim_remove']:>7.4f}")

    s = strats["perturbation_guided"]
    print(f"  {'Perturbation-guided':<25} {s['accuracy']:>9.1%} {s['delta_vs_baseline_pp']:>+7.1f} "
          f"{s['accuracy_risk_pct']:>7.1f} {s['mean_sim_remove']:>7.4f}")

    s = strats["random"]
    print(f"  {'Random (100 trials)':<25} {s['accuracy_mean']:>9.1%} {s['delta_vs_baseline_pp']:>+7.1f} "
          f"{s['accuracy_risk_pct_mean']:>7.1f}     —")

    print(f"\n  McNemar p-values:")
    for pair, p in r["mcnemar_p_values"].items():
        sig = "***" if p < 0.001 else "**" if p < 0.01 else "*" if p < 0.05 else "n.s."
        print(f"    {pair}: p={p:.6f} {sig}")

    print(f"\n  Perturbation-guided selects (func type distribution):")
    for ft, prop in strats["perturbation_guided"]["func_type_distribution"].items():
        count = strats["perturbation_guided"]["func_type_counts"].get(ft, 0)
        print(f"    {ft:<25} {prop:>6.1%}  (n={count})")

    ov = r["overlap_analysis"]
    if ov["mean_overlap_frac"] is not None:
        print(f"\n  Overlap (perturbation ∩ ack-only): {ov['mean_overlap_frac']:.1%} ± {ov['std_overlap_frac']:.1%}")

    print(f"\n  Per-function-type diagnostics:")
    print(f"    {'Type':<25} {'n':>5} {'sim̄':>7} {'σ':>7} {'FA risk%':>9}")
    for ft, d in sorted(r["per_functype_diagnostics"].items(), key=lambda x: -x[1]["sim_remove_mean"]):
        print(f"    {ft:<25} {d['n']:>5} {d['sim_remove_mean']:>7.4f} {d['sim_remove_std']:>7.4f} "
              f"{d['final_answer_risk_pct']:>8.1f}%")


def main():
    results = {}
    for combo in COMBOS:
        combo_dir = BASE / combo
        if not (combo_dir / "local_impact" / "impact.jsonl").exists():
            print(f"Skipping {combo}: no impact data")
            continue
        print(f"Analyzing {combo}...")
        results[combo] = analyze_combo(combo)
        print_summary(results[combo])

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = OUT_DIR / "perturbation_baseline.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\nResults saved to {out_path}")


if __name__ == "__main__":
    main()
