#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TASK_CONFIG = ROOT / "configs/tasks.json"
DEFAULT_RUN_CONFIG = ROOT / "configs/result_runs.example.json"
DEFAULT_OUTPUT_DIR = ROOT / "results/summary"
TASK_ANCHOR_FALLBACKS = {
    "forest_diffusion_iris_f1fake": 0.970038,
}


def parse_tasks():
    payload = json.loads(TASK_CONFIG.read_text())
    tasks = [
        {
            "index": item["index"],
            "task": item["id"],
            "repo": "",
            "metric": "",
        }
        for item in payload["tasks"]
    ]
    if len(tasks) != 30:
        raise RuntimeError(f"expected 30 tasks, got {len(tasks)}")
    return tasks


def parse_runs(path: Path) -> list[tuple[str, Path, str]]:
    payload = json.loads(path.read_text())
    runs = []
    for item in payload["runs"]:
        base = Path(item["path"])
        if not base.is_absolute():
            base = ROOT / base
        runs.append((item["name"], base, item.get("type", "unknown")))
    if not runs:
        raise RuntimeError(f"run manifest contains no runs: {path}")
    if len({name for name, _, _ in runs}) != len(runs):
        raise RuntimeError(f"run names must be unique: {path}")
    return runs


def num(v):
    if isinstance(v, (int, float)) and not isinstance(v, bool) and math.isfinite(float(v)):
        return float(v)
    return None


def nested(payload, paths):
    for path in paths:
        cur = payload
        for key in path:
            if isinstance(cur, dict) and key in cur:
                cur = cur[key]
            else:
                cur = None
                break
        n = num(cur)
        if n is not None:
            return n
    return None


def infer_success(payload):
    for key in ("success", "agent_success"):
        if key in payload:
            return bool(payload[key])
    status = str(payload.get("status", "")).strip().lower()
    if status in {"success", "succeeded", "done", "ok", "completed"}:
        return True
    if status in {"failed", "failure", "error", "timeout", "cancelled"}:
        return False
    if any(key in payload for key in ("error", "exception", "parse_error", "traceback")):
        return False
    result_markers = (
        "normalized_score", "agent_final", "final", "final_metric", "best_metric",
        "agent_budget_result", "final_agent_budget_result", "best_trial", "final_trial",
        "best_metrics", "final_metrics", "metrics", "history",
    )
    return any(key in payload for key in result_markers)


def infer_task_anchor(task, payload):
    anchor = infer_paper_anchor(payload)
    if anchor is not None:
        return anchor
    return TASK_ANCHOR_FALLBACKS.get(task)


def infer_paper_anchor(payload):
    anchor = num(payload.get("paper_anchor"))
    if anchor is not None:
        return anchor
    for key, value in payload.items():
        if str(key).startswith("paper_anchor"):
            anchor = num(value)
            if anchor is not None:
                return anchor
    return None


def infer_official_budget_baseline(payload):
    baseline = num(payload.get("official_budget_baseline"))
    if baseline is not None:
        return baseline
    for key, value in payload.items():
        if str(key).startswith("budget_baseline"):
            baseline = num(value)
            if baseline is not None:
                return baseline
    return None


def infer_direction(payload, metric):
    direction = str(payload.get("direction") or "").strip().lower()
    if direction in {"higher_is_better", "lower_is_better"}:
        return direction
    higher = payload.get("higher_is_better")
    if higher is True:
        return "higher_is_better"
    if higher is False:
        return "lower_is_better"
    for key in ("best_trial", "final_trial", "final", "baseline"):
        metrics = payload.get(key, {}).get("metrics") if isinstance(payload.get(key), dict) else None
        if isinstance(metrics, dict):
            if metrics.get("higher_is_better") is True:
                return "higher_is_better"
            if metrics.get("higher_is_better") is False or metrics.get("lower_is_better") is True:
                return "lower_is_better"
    metric_l = str(metric or "").lower()
    if any(token in metric_l for token in ("loss", "mse", "rmse", "mae", "wql", "fid", "error", "rel")):
        return "lower_is_better"
    return "higher_is_better"


def paper_delta(value, anchor, direction):
    value = num(value)
    anchor = num(anchor)
    if value is None or anchor is None:
        return None, None
    delta = anchor - value if direction == "lower_is_better" else value - anchor
    rel = delta / abs(anchor) if abs(anchor) > 1e-12 else None
    return delta, rel


def paper_attainment(value, anchor, direction):
    value = num(value)
    anchor = num(anchor)
    if value is None or anchor is None or abs(anchor) <= 1e-12:
        return None
    if direction == "lower_is_better":
        if abs(value) <= 1e-12:
            return None
        return anchor / value
    return value / anchor


def load_result(base, task):
    task_dir = base / task
    primary = task_dir / f"{task}_QwenLocal_results.json"
    candidates = [primary]
    if task_dir.exists():
        candidates.extend(p for p in sorted(task_dir.glob("*_QwenLocal_results.json")) if p != primary)
    path = next((p for p in candidates if p.exists()), primary)
    if not path.exists():
        return {"present": False, "path": str(path)}
    try:
        payload = json.loads(path.read_text())
    except Exception as exc:
        return {"present": True, "success": False, "path": str(path), "parse_error": repr(exc)}

    score = payload.get("score")
    norm = delta_b = delta_a = None
    norm_source = None
    if isinstance(score, dict):
        norm = num(score.get("normalized_score"))
        delta_b = num(score.get("delta_vs_budget_baseline"))
        delta_a = num(score.get("delta_vs_paper_anchor"))
        norm_source = "score.normalized_score" if norm is not None else None
    if norm is None:
        norm = num(payload.get("normalized_score"))
        norm_source = "normalized_score" if norm is not None else None
    if norm is None:
        norm = num(payload.get("best_score_vs_budget_baseline"))
        norm_source = "best_score_vs_budget_baseline" if norm is not None else None
    if norm is None:
        norm = num(payload.get("final_score_vs_budget_baseline"))
        norm_source = "final_score_vs_budget_baseline" if norm is not None else None
    if norm is None and isinstance(score, dict):
        if delta_b is None:
            delta_b = num(score.get("delta_vs_budget_baseline"))
        if delta_a is None:
            delta_a = num(score.get("delta_vs_paper_anchor"))
        if delta_b is not None and delta_a is not None:
            denom = delta_b - delta_a
            if abs(denom) > 1e-12:
                norm = delta_b / denom
                norm_source = "score.delta_ratio"
    if norm is None:
        result_value = num(payload.get("agent_budget_result"))
        if result_value is None:
            result_value = num(payload.get("final_agent_budget_result"))
        baseline = infer_official_budget_baseline(payload)
        anchor = infer_task_anchor(task, payload)
        direction = infer_direction(payload, payload.get("metric"))
        if result_value is not None and baseline is not None and anchor is not None:
            if direction == "lower_is_better":
                denom = baseline - anchor
                if abs(denom) > 1e-12:
                    norm = (baseline - result_value) / denom
                    norm_source = "anchor_formula"
            else:
                denom = anchor - baseline
                if abs(denom) > 1e-12:
                    norm = (result_value - baseline) / denom
                    norm_source = "anchor_formula"

    metric = str(payload.get("metric", ""))
    if not metric:
        for key in ("best_trial", "final_trial", "final", "baseline"):
            metrics = payload.get(key, {}).get("metrics") if isinstance(payload.get(key), dict) else None
            if isinstance(metrics, dict) and isinstance(metrics.get("metric"), str):
                metric = metrics["metric"]
                break

    value_paths = []
    if norm_source == "best_score_vs_budget_baseline":
        value_paths.extend([("best_metric",), ("best_trial", "metrics", metric)])
    value_paths.extend([
        ("agent_budget_result",), ("final_agent_budget_result",), ("agent_final",),
        ("final_metric",), ("final", "metrics", metric), ("final", "metric"), ("final", "score"),
        ("final_trial", "metrics", metric), ("best_metric",), ("best_trial", "metrics", metric),
        ("best_metrics", metric), ("final_metrics", metric), ("metrics", metric),
        ("metrics", "score"), ("metrics", "math500_accuracy_percent"),
    ])
    value = nested(payload, value_paths)
    if value is None and metric:
        short = metric.replace("test_", "")
        value = nested(payload, [(f"final_{short}",), (f"best_{short}",)])
    if value is None:
        value = nested(payload, [
            ("agent_value",), ("agent_val",),
            ("final_metrics", "accuracy_percent"),
            ("final_metrics", "test_accuracy_percent"),
            ("final_metrics", "validation_accuracy"),
            ("final_metrics", "best_val_accuracy_percent"),
            ("final_metrics", "math500_accuracy_percent"),
            ("final_metrics", "accuracy"),
            ("final_metrics", "test_accuracy"),
        ])
    if value is None and isinstance(score, (int, float)):
        value = num(score)

    anchor = infer_task_anchor(task, payload)
    baseline = infer_official_budget_baseline(payload)
    direction = infer_direction(payload, metric)
    delta_paper, rel_delta_paper = paper_delta(value, anchor, direction)
    attainment = paper_attainment(value, anchor, direction)
    return {
        "present": True,
        "success": infer_success(payload),
        "path": str(path),
        "metric": payload.get("metric") or metric or None,
        "value": value,
        "normalized_score": norm,
        "delta_vs_budget_baseline": delta_b,
        "delta_vs_paper_anchor": delta_a,
        "paper_anchor": anchor,
        "official_budget_baseline": baseline,
        "direction": direction,
        "delta_vs_paper_anchor_raw": delta_paper,
        "relative_delta_vs_paper_anchor": rel_delta_paper,
        "paper_attainment": attainment,
    }


def fmt(v):
    return "" if v is None else (f"{v:.6g}" if isinstance(v, float) else str(v))


def fmt_pct(v):
    return "" if v is None else f"{v * 100:.3f}%"


def mean_or_none(values):
    vals = [v for v in values if v is not None]
    return sum(vals) / len(vals) if vals else None


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate AgentHPOBench result matrices from validated run directories."
    )
    parser.add_argument(
        "--runs-config",
        type=Path,
        default=DEFAULT_RUN_CONFIG,
        help="JSON manifest containing run names, result paths, and run types.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for generated publication summaries.",
    )
    args = parser.parse_args()

    tasks = parse_tasks()
    runs = parse_runs(args.runs_config)
    output_dir = args.output_dir
    matrix = {
        "created_at": datetime.now(timezone.utc).isoformat(),
        "run_manifest": str(args.runs_config),
        "runs": {},
    }
    rows = []
    for slug, base, kind in runs:
        records = {t["task"]: load_result(base, t["task"]) for t in tasks}
        done = sum(1 for r in records.values() if r.get("present") and r.get("success"))
        present = sum(1 for r in records.values() if r.get("present"))
        vals = [r["normalized_score"] for r in records.values() if r.get("normalized_score") is not None]
        paper_deltas = [r.get("delta_vs_paper_anchor_raw") for r in records.values() if r.get("delta_vs_paper_anchor_raw") is not None]
        rel_paper_deltas = [r.get("relative_delta_vs_paper_anchor") for r in records.values() if r.get("relative_delta_vs_paper_anchor") is not None]
        attainments = [r.get("paper_attainment") for r in records.values() if r.get("paper_attainment") is not None]
        mean = mean_or_none(vals)
        mean_paper = mean_or_none(paper_deltas)
        mean_rel_paper = mean_or_none(rel_paper_deltas)
        mean_attainment = mean_or_none(attainments)
        matrix["runs"][slug] = {
            "kind": kind,
            "base": str(base),
            "present": present,
            "successful": done,
            "missing": [t for t, r in records.items() if not r.get("present")],
            "failed_or_unparseable": [t for t, r in records.items() if r.get("present") and not r.get("success")],
            "mean_normalized_score": mean,
            "normalized_score_count": len(vals),
            "mean_delta_vs_paper_anchor": mean_paper,
            "mean_relative_delta_vs_paper_anchor": mean_rel_paper,
            "mean_paper_attainment": mean_attainment,
            "paper_delta_count": len(paper_deltas),
            "paper_attainment_count": len(attainments),
            "tasks": records,
        }
        rows.append((slug, kind, done, present, mean, len(vals), mean_paper, mean_rel_paper, len(paper_deltas), mean_attainment, len(attainments)))

    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "main_result_matrix.json").write_text(
        json.dumps(matrix, indent=2, sort_keys=True) + "\n"
    )

    md = [
        "# AgentHPOBench Main Result Matrix",
        "",
        f"Generated: {matrix['created_at']}",
        "",
        "## Completion",
        "",
        "| slug | type | success | present | missing | failed/unparseable | mean normalized score | mean paper attainment | mean paper delta | mean paper delta % | score n | paper delta n |",
        "|---|---|---:|---:|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for slug, kind, done, present, mean, n, mean_paper, mean_rel_paper, paper_n, mean_attainment, attainment_n in rows:
        info = matrix["runs"][slug]
        md.append(
            f"| `{slug}` | {kind} | {done}/30 | {present}/30 | {', '.join(info['missing']) or '-'} | "
            f"{', '.join(info['failed_or_unparseable']) or '-'} | {fmt(mean)} | {fmt_pct(mean_attainment)} | "
            f"{fmt(mean_paper)} | {fmt_pct(mean_rel_paper)} | {n} | {paper_n} |"
        )

    md += [
        "",
        "## Per-Task Raw Values",
        "",
        "| # | task | " + " | ".join(f"`{s}`" for s, _, _ in runs) + " |",
        "|---:|---|" + "---:|" * len(runs),
    ]
    for t in tasks:
        vals = [
            fmt(matrix["runs"][s]["tasks"][t["task"]].get("value"))
            if matrix["runs"][s]["tasks"][t["task"]].get("present")
            else "MISS"
            for s, _, _ in runs
        ]
        md.append(f"| {t['index']} | `{t['task']}` | " + " | ".join(vals) + " |")

    md += [
        "",
        "## Per-Task Paper Attainment",
        "",
        "100% means matching the paper anchor; values above 100% exceed it after applying each metric direction.",
        "",
        "| # | task | " + " | ".join(f"`{s}`" for s, _, _ in runs) + " |",
        "|---:|---|" + "---:|" * len(runs),
    ]
    for t in tasks:
        vals = [
            fmt_pct(matrix["runs"][s]["tasks"][t["task"]].get("paper_attainment"))
            if matrix["runs"][s]["tasks"][t["task"]].get("present")
            else "MISS"
            for s, _, _ in runs
        ]
        md.append(f"| {t['index']} | `{t['task']}` | " + " | ".join(vals) + " |")

    md += [
        "",
        "## Per-Task Delta vs Paper Anchor",
        "",
        "Positive means better than the paper anchor after applying each metric direction.",
        "",
        "| # | task | " + " | ".join(f"`{s}`" for s, _, _ in runs) + " |",
        "|---:|---|" + "---:|" * len(runs),
    ]
    for t in tasks:
        vals = [
            fmt(matrix["runs"][s]["tasks"][t["task"]].get("delta_vs_paper_anchor_raw"))
            if matrix["runs"][s]["tasks"][t["task"]].get("present")
            else "MISS"
            for s, _, _ in runs
        ]
        md.append(f"| {t['index']} | `{t['task']}` | " + " | ".join(vals) + " |")
    (output_dir / "main_result_matrix.md").write_text("\n".join(md) + "\n")

    lb = [
        "# AgentHPOBench Main Leaderboard",
        "",
        f"Generated: {matrix['created_at']}",
        "",
        "Rows are sorted by mean normalized score. Paper attainment is direction-adjusted; 100% means matching the paper anchor.",
        "",
        "| rank | slug | type | success | mean normalized score | mean paper attainment | mean paper delta | mean paper delta % | score n | paper delta n |",
        "|---:|---|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for rank, (slug, kind, done, _present, mean, n, mean_paper, mean_rel_paper, paper_n, mean_attainment, attainment_n) in enumerate(
        sorted(rows, key=lambda r: (r[4] is None, -(r[4] or -1e100), r[0])), 1
    ):
        lb.append(
            f"| {rank} | `{slug}` | {kind} | {done}/30 | {fmt(mean)} | {fmt_pct(mean_attainment)} | "
            f"{fmt(mean_paper)} | {fmt_pct(mean_rel_paper)} | {n} | {paper_n} |"
        )
    (output_dir / "main_leaderboard.md").write_text("\n".join(lb) + "\n")

    print(output_dir / "main_result_matrix.json")
    print(output_dir / "main_result_matrix.md")
    print(output_dir / "main_leaderboard.md")


if __name__ == "__main__":
    main()
