# Plan-004: Three-condition ablation comparison — Explicit vs Implicit Routing.
#
# Loads evaluation results from all three conditions and produces a unified
# comparison report: accuracy, task scores, death rates, routing distributions.
#
# Conditions:
#   (a) 1.7B Explicit Router — plan-002 checkpoint (classification head)
#   (b) 1.7B Implicit Router — plan-004 checkpoint (causal LM, [SIMULATE] prefix)
#   (c) 7B Implicit Router  — prompt-only (tool-use, no training)
#
# Input:  eval_results.json from each condition's output directory,
#         or runs all three evaluations live if checkpoints are provided.
# Output: results/plan-004-ablation/comparison_report.json
#
# Dependencies: ablation_eval_common.py, router_sft_eval.py

import argparse
import json
import os
import sys
from typing import Dict, Any, Optional, List

SRC_DIR = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, SRC_DIR)


# ---------------------------------------------------------------------------
# Result loading (from pre-computed eval_results.json)
# ---------------------------------------------------------------------------

def load_condition_results(results_dir: str, condition_name: str) -> Optional[Dict]:
    """Load eval_results.json for a given condition."""
    path = os.path.join(results_dir, condition_name, "eval_results.json")
    if not os.path.exists(path):
        print(f"Warning: {path} not found, skipping condition '{condition_name}'")
        return None
    with open(path) as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# Live evaluation (runs router on ScienceWorld)
# ---------------------------------------------------------------------------

def run_explicit_eval(adapter_path: str, model_name: str, config) -> Dict:
    """Condition (a): explicit router from plan-002."""
    from router_sft_eval import ExplicitRouter
    from ablation_eval_common import run_ablation_eval

    router = ExplicitRouter(adapter_path=adapter_path, base_model=model_name)
    return run_ablation_eval(config, router_fn=router)


def run_implicit_1_7b_eval(adapter_path: str, model_name: str, config) -> Dict:
    """Condition (b): implicit 1.7B router."""
    from training.implicit_router_sft import Implicit1_7BRouter
    from ablation_eval_common import run_ablation_eval

    router = Implicit1_7BRouter(adapter_path=adapter_path, base_model=model_name)
    return run_ablation_eval(config, router_fn=router)


def run_prompt_7b_eval(model_path: Optional[str], gpu_id: int, config) -> Dict:
    """Condition (c): prompt-only 7B router."""
    from evaluation.prompt_routing_eval import Implicit7BRouter
    from ablation_eval_common import run_ablation_eval

    router = Implicit7BRouter(model_path=model_path, gpu_id=gpu_id)
    return run_ablation_eval(config, router_fn=router)


# ---------------------------------------------------------------------------
# Comparison report
# ---------------------------------------------------------------------------

CONDITION_NAMES = {
    "a": "explicit_1_7b",
    "b": "implicit_1_7b",
    "c": "implicit_7b",
}

CONDITION_LABELS = {
    "explicit_1_7b": "(a) 1.7B Explicit Router",
    "implicit_1_7b": "(b) 1.7B Implicit Router",
    "implicit_7b":   "(c) 7B Implicit Router (prompt-only)",
}


def build_comparison(results: Dict[str, Dict]) -> Dict[str, Any]:
    """Build a unified comparison report from per-condition results."""
    summary_rows = []
    per_task_all = {}

    for cond_key in ["explicit_1_7b", "implicit_1_7b", "implicit_7b"]:
        r = results.get(cond_key)
        if r is None:
            continue

        ep = r.get("episode_metrics", {})
        ra = r.get("routing_accuracy", {})

        row = {
            "condition": CONDITION_LABELS.get(cond_key, cond_key),
            "condition_key": cond_key,
            "mean_score": ep.get("mean_score"),
            "death_rate": ep.get("death_rate"),
            "routing_accuracy": ra.get("accuracy"),
            "route_ratio_det": ep.get("route_ratio_det"),
            "route_ratio_int": ep.get("route_ratio_int"),
            "n_episodes": ep.get("n_episodes"),
            "mean_steps": ep.get("mean_steps"),
        }
        summary_rows.append(row)

        per_task = ep.get("per_task_mean_score", {})
        for task, score in per_task.items():
            per_task_all.setdefault(task, {})[cond_key] = score

    # Pairwise deltas: (b) vs (a), (c) vs (a), (c) vs (b)
    deltas = {}
    if "explicit_1_7b" in results and "implicit_1_7b" in results:
        a_score = results["explicit_1_7b"]["episode_metrics"]["mean_score"]
        b_score = results["implicit_1_7b"]["episode_metrics"]["mean_score"]
        deltas["b_vs_a"] = {
            "score_delta": b_score - a_score,
            "description": "Implicit 1.7B minus Explicit 1.7B (controls for formulation)",
        }
    if "explicit_1_7b" in results and "implicit_7b" in results:
        a_score = results["explicit_1_7b"]["episode_metrics"]["mean_score"]
        c_score = results["implicit_7b"]["episode_metrics"]["mean_score"]
        deltas["c_vs_a"] = {
            "score_delta": c_score - a_score,
            "description": "Prompt 7B minus Explicit 1.7B (confounds capacity + formulation)",
        }
    if "implicit_1_7b" in results and "implicit_7b" in results:
        b_score = results["implicit_1_7b"]["episode_metrics"]["mean_score"]
        c_score = results["implicit_7b"]["episode_metrics"]["mean_score"]
        deltas["c_vs_b"] = {
            "score_delta": c_score - b_score,
            "description": "Prompt 7B minus Implicit 1.7B (controls for capacity)",
        }

    return {
        "summary": summary_rows,
        "per_task_scores": per_task_all,
        "pairwise_deltas": deltas,
    }


def print_comparison(report: Dict):
    """Pretty-print the comparison table."""
    rows = report["summary"]
    if not rows:
        print("No results to compare.")
        return

    print("\n" + "=" * 80)
    print("Plan-004 Ablation: Explicit vs Implicit Routing")
    print("=" * 80)

    header = f"{'Condition':<40} {'Score':>8} {'Death%':>8} {'RoutAcc':>8} {'Det%':>6}"
    print(header)
    print("-" * 80)
    for r in rows:
        score = f"{r['mean_score']:.2f}" if r["mean_score"] is not None else "N/A"
        death = f"{r['death_rate']:.1%}" if r["death_rate"] is not None else "N/A"
        acc = f"{r['routing_accuracy']:.3f}" if r["routing_accuracy"] is not None else "N/A"
        det = f"{r['route_ratio_det']:.1%}" if r["route_ratio_det"] is not None else "N/A"
        print(f"{r['condition']:<40} {score:>8} {death:>8} {acc:>8} {det:>6}")

    deltas = report.get("pairwise_deltas", {})
    if deltas:
        print(f"\n{'Pairwise Deltas':}")
        for key, d in deltas.items():
            print(f"  {key}: {d['score_delta']:+.2f}  ({d['description']})")

    per_task = report.get("per_task_scores", {})
    if per_task:
        print(f"\n{'Per-task Scores':}")
        tasks = sorted(per_task.keys())
        conds = ["explicit_1_7b", "implicit_1_7b", "implicit_7b"]
        header = f"  {'Task':<35}" + "".join(f" {c[:12]:>12}" for c in conds)
        print(header)
        for task in tasks:
            scores = per_task[task]
            vals = []
            for c in conds:
                s = scores.get(c)
                vals.append(f"{s:.2f}" if s is not None else "N/A")
            print(f"  {task:<35}" + "".join(f" {v:>12}" for v in vals))

    print("=" * 80)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Plan-004: Three-condition ablation comparison"
    )

    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument("--from_results", action="store_true", default=True,
                            help="Load pre-computed eval_results.json (default)")
    mode_group.add_argument("--run_live", action="store_true",
                            help="Run evaluations live (requires checkpoints)")

    parser.add_argument("--explicit_ckpt", type=str, default=None,
                        help="Path to plan-002 explicit router adapter (condition a)")
    parser.add_argument("--implicit_ckpt", type=str, default=None,
                        help="Path to plan-004 implicit router adapter (condition b)")
    parser.add_argument("--prompt_model", type=str, default=None,
                        help="Path/name of Qwen2.5-7B-Instruct for condition c")
    parser.add_argument("--data_dir", type=str, default="results/plan_c",
                        help="Data directory (used for oracle labels in live mode)")
    parser.add_argument("--output_dir", type=str, default="results/plan-004-ablation",
                        help="Output directory for comparison report")
    parser.add_argument("--results_dir", type=str, default=None,
                        help="Directory containing per-condition eval_results.json "
                             "(default: same as --output_dir)")

    from ablation_eval_common import add_eval_args
    add_eval_args(parser)

    args = parser.parse_args()
    results_dir = args.results_dir or args.output_dir
    os.makedirs(args.output_dir, exist_ok=True)

    if args.run_live:
        from ablation_eval_common import EvalConfig

        base_config = EvalConfig(
            task_types=[t.strip() for t in args.task_types.split(",")],
            max_variations=args.max_variations,
            max_steps=args.max_steps,
            gpu_id=args.gpu_id,
            output_dir=args.output_dir,
            oracle_data_path=args.oracle_data,
        )

        all_results = {}

        if args.explicit_ckpt:
            print("\n>>> Running Condition (a): Explicit 1.7B <<<")
            cfg = EvalConfig(**{**base_config.__dict__, "condition_name": "explicit_1_7b"})
            all_results["explicit_1_7b"] = run_explicit_eval(
                args.explicit_ckpt, "Qwen/Qwen3-1.7B", cfg
            )

        if args.implicit_ckpt:
            print("\n>>> Running Condition (b): Implicit 1.7B <<<")
            cfg = EvalConfig(**{**base_config.__dict__, "condition_name": "implicit_1_7b"})
            all_results["implicit_1_7b"] = run_implicit_1_7b_eval(
                args.implicit_ckpt, "Qwen/Qwen3-1.7B", cfg
            )

        if args.prompt_model:
            print("\n>>> Running Condition (c): Prompt 7B <<<")
            cfg = EvalConfig(**{**base_config.__dict__, "condition_name": "implicit_7b"})
            all_results["implicit_7b"] = run_prompt_7b_eval(
                args.prompt_model, args.gpu_id, cfg
            )

    else:
        all_results = {}
        for cond_key in ["explicit_1_7b", "implicit_1_7b", "implicit_7b"]:
            r = load_condition_results(results_dir, cond_key)
            if r is not None:
                all_results[cond_key] = r

    if not all_results:
        print("No results found. Provide checkpoints with --run_live, "
              "or ensure eval_results.json files exist in --results_dir.")
        return

    report = build_comparison(all_results)
    print_comparison(report)

    report_path = os.path.join(args.output_dir, "comparison_report.json")
    with open(report_path, "w") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"\nReport saved to {report_path}")


if __name__ == "__main__":
    main()
