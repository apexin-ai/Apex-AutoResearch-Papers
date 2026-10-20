"""Phase 3: Repair comparison across 4 trace conditions.

Compares repair success rates under four conditions:
  - no_trace: only issue description + buggy code
  - full_trace: complete execution trace (8000 token truncation)
  - structural_filtered: only Phase 2 "keep" structural segments
  - line_filtered: only Phase 2 "keep" line segments

Input:
  pipeline_output/phase2_structural_scores.json
  pipeline_output/phase2_line_scores.json
  pipeline_output/{key}_trace.json
  pipeline_output/{key}_structural_segments.json
  pipeline_output/{key}_line_segments.json

Output:
  pipeline_output/phase3_results.csv      -- per-instance per-condition results
  pipeline_output/phase3_summary.json     -- aggregated metrics + stratified analysis

Dependencies: openai, dtd_types, mvp_pipeline, run_phase2_scoring, bugsinpy_setup
"""
from __future__ import annotations

import argparse
import csv
import json
import logging
import os
import sys
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Any, Dict, List, Optional, Tuple

from dtd_types import TraceEvent, TraceSegment, ScoredSegment, estimate_tokens
from mvp_pipeline import REPAIR_PROMPT_TEMPLATE, TRACE_SECTION_TEMPLATE, MVPPipeline
from run_phase2_scoring import load_segments, get_buggy_code, INSTANCE_DESCRIPTIONS
from bugsinpy_setup import BugsInPySetup

logger = logging.getLogger(__name__)

PIPELINE_OUTPUT = "/root/trace_distill_repair/pipeline_output"
WORKSPACE = "/root/trace_distill_repair/bugsinpy_workspace"
CONDITIONS = ["no_trace", "full_trace", "structural_filtered", "line_filtered"]

CSV_FIELDS = [
    "instance_id", "condition", "repair_success", "eval_method",
    "line_overlap", "tokens_input", "tokens_output",
    "full_trace_tokens", "num_structural_segments", "num_structural_keep",
    "num_line_keep", "generated_fix",
]


def load_phase2_scores(mode: str) -> Dict[str, list]:
    """Load Phase 2 scoring results. Returns {instance_key: [score_dicts]}."""
    path = os.path.join(PIPELINE_OUTPUT, f"phase2_{mode}_scores.json")
    if not os.path.isfile(path):
        raise FileNotFoundError(
            f"{path} not found.\n"
            f"Run Phase 2 {mode} scoring first:  python run_phase2_scoring.py --mode {mode}"
        )
    with open(path) as f:
        data = json.load(f)
    return {
        key: inst.get("scores", [])
        for key, inst in data.get("results", {}).items()
    }


def load_trace_events(instance_key: str) -> List[TraceEvent]:
    """Load raw trace events from JSON file."""
    path = os.path.join(PIPELINE_OUTPUT, f"{instance_key}_trace.json")
    if not os.path.isfile(path):
        return []
    with open(path) as f:
        raw = json.load(f)
    events = []
    for e in raw:
        exc_info = None
        ei = e.get("exception_info")
        if ei:
            if isinstance(ei, dict):
                exc_info = (ei.get("type", ""), ei.get("value", ""), ei.get("traceback", ""))
            elif isinstance(ei, (list, tuple)):
                exc_info = tuple(ei)
        events.append(TraceEvent(
            event_type=e["event_type"],
            function_name=e["function_name"],
            filename=e["filename"],
            lineno=e["lineno"],
            locals_snapshot=e.get("locals_snapshot", {}),
            call_depth=e["call_depth"],
            timestamp=e.get("timestamp", 0.0),
            return_value=e.get("return_value"),
            exception_info=exc_info,
        ))
    return events


def build_keep_segments(instance_key: str, mode: str, scores: list) -> List[ScoredSegment]:
    """Load segments and return only those labeled 'keep' in Phase 2 scores."""
    segments = load_segments(instance_key, mode)
    if not segments or not scores:
        return []
    seg_map = {(s.segment_type, s.start_idx, s.end_idx): s for s in segments}
    result = []
    for sc in scores:
        if sc.get("label") != "keep":
            continue
        key = (sc["segment_type"], sc["start_idx"], sc["end_idx"])
        seg = seg_map.get(key)
        if seg:
            result.append(ScoredSegment(
                segment=seg, label="keep",
                confidence=sc.get("confidence", 0.0),
                reasoning=sc.get("reasoning", ""),
            ))
    return result


def get_fixed_code_direct(instance_key: str) -> str:
    """Get fixed code from workspace without triggering git checkout."""
    fixed_dir = os.path.join(WORKSPACE, "instances", instance_key, "fixed")
    if not os.path.isdir(fixed_dir):
        return ""
    setup = BugsInPySetup(WORKSPACE)
    parts = instance_key.rsplit("_", 1)
    project, bug_id = parts[0], int(parts[1])
    bug_dir = os.path.join(WORKSPACE, "BugsInPy", "projects", project, "bugs", str(bug_id))
    bug_info = setup._read_bug_info(bug_dir)
    buggy_file = bug_info.get("buggy_file", "")
    if buggy_file:
        path = os.path.join(fixed_dir, buggy_file)
        if os.path.isfile(path):
            with open(path) as f:
                return f.read()
    return setup._find_main_python_file(fixed_dir)


def get_instance_info(instance_key: str) -> dict:
    """Get instance metadata (issue_description, buggy_dir, test_command, bug_info)."""
    parts = instance_key.rsplit("_", 1)
    project, bug_id = parts[0], int(parts[1])
    setup = BugsInPySetup(WORKSPACE)
    try:
        return setup.setup_instance(project, bug_id)
    except Exception as e:
        logger.warning("setup_instance failed for %s: %s", instance_key, e)
        buggy_dir = os.path.join(WORKSPACE, "instances", instance_key, "buggy")
        return {
            "project": project,
            "bug_id": bug_id,
            "buggy_dir": buggy_dir if os.path.isdir(buggy_dir) else "",
            "test_command": "",
            "issue_description": INSTANCE_DESCRIPTIONS.get(instance_key, f"{project} bug #{bug_id}"),
            "bug_info": {},
        }


def call_repair_llm(pipeline: MVPPipeline, prompt: str) -> Tuple[str, int, int]:
    """Call repair LLM. Returns (generated_code, tokens_input, tokens_output)."""
    client = pipeline._get_repair_client()
    response = client.chat.completions.create(
        model=pipeline.repair_model,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
        max_tokens=4096,
    )
    raw_content = response.choices[0].message.content
    content = raw_content.strip() if raw_content else ""
    if content.startswith("```python"):
        content = content[len("```python"):].strip()
    if content.startswith("```"):
        content = content[3:].strip()
    if content.endswith("```"):
        content = content[:-3].strip()

    usage = response.usage
    tokens_in = getattr(usage, "prompt_tokens", 0) if usage else 0
    tokens_out = getattr(usage, "completion_tokens", 0) if usage else 0
    if not tokens_in:
        tokens_in = estimate_tokens(prompt)
    if not tokens_out:
        tokens_out = estimate_tokens(content)
    return content, tokens_in, tokens_out


def run_instance(
    pipeline: MVPPipeline,
    instance_key: str,
    structural_scores: list,
    line_scores: list,
) -> List[dict]:
    """Run 4-condition repair for one instance. Returns list of result dicts."""
    logger.info("Processing %s", instance_key)
    t0 = time.time()

    info = get_instance_info(instance_key)
    issue = info.get("issue_description", "") or INSTANCE_DESCRIPTIONS.get(instance_key, "")
    buggy_code = get_buggy_code(instance_key)
    fixed_code = get_fixed_code_direct(instance_key)
    events = load_trace_events(instance_key)
    buggy_dir = info.get("buggy_dir", "")
    test_command = info.get("test_command", "")
    buggy_file = info.get("bug_info", {}).get("buggy_file", "")

    if not buggy_code:
        logger.warning("No buggy code for %s, skipping", instance_key)
        return []

    if events:
        full_trace_text, _ = pipeline._format_full_trace(events, max_tokens=8000)
    else:
        full_trace_text = ""
    full_trace_tokens = estimate_tokens(full_trace_text)

    structural_keep = build_keep_segments(instance_key, "structural", structural_scores)
    line_keep = build_keep_segments(instance_key, "line", line_scores)

    structural_trace = pipeline._format_filtered_trace(structural_keep) if structural_keep else ""
    line_trace = pipeline._format_filtered_trace(line_keep) if line_keep else ""

    trace_map = {
        "no_trace": "",
        "full_trace": full_trace_text,
        "structural_filtered": structural_trace,
        "line_filtered": line_trace,
    }

    rows = []
    for condition in CONDITIONS:
        if condition == "line_filtered" and not line_scores:
            logger.info("  %s/%s: skipped (no line scores)", instance_key, condition)
            continue
        trace_ctx = trace_map[condition]
        prompt = pipeline._build_repair_prompt(issue, buggy_code, trace_ctx, condition)

        try:
            generated_fix, tokens_in, tokens_out = call_repair_llm(pipeline, prompt)
        except Exception as e:
            logger.error("%s/%s LLM error: %s", instance_key, condition, e)
            generated_fix = ""
            tokens_in = estimate_tokens(prompt)
            tokens_out = 0

        if not generated_fix:
            eval_result = {"pass": False, "method": "empty_response", "line_overlap": 0.0}
        else:
            eval_result = pipeline._evaluate_repair(
                generated_fix, fixed_code, test_command, buggy_dir,
                buggy_file_relpath=buggy_file,
            )

        rows.append({
            "instance_id": instance_key,
            "condition": condition,
            "repair_success": eval_result.get("pass", False),
            "eval_method": eval_result.get("method", "none"),
            "line_overlap": round(eval_result.get("line_overlap", 0.0), 4),
            "tokens_input": tokens_in,
            "tokens_output": tokens_out,
            "full_trace_tokens": full_trace_tokens,
            "num_structural_segments": len(structural_scores),
            "num_structural_keep": len(structural_keep),
            "num_line_keep": len(line_keep),
            "generated_fix": generated_fix[:5000],
        })
        logger.info("  %s/%s: success=%s method=%s tokens=%d+%d",
                     instance_key, condition, eval_result.get("pass"),
                     eval_result.get("method", "none"), tokens_in, tokens_out)

    logger.info("Done %s (%.1fs)", instance_key, time.time() - t0)
    return rows


def load_checkpoint(checkpoint_path: str) -> Dict[str, List[dict]]:
    """Load checkpoint with completed instance results."""
    if not os.path.isfile(checkpoint_path):
        return {}
    with open(checkpoint_path) as f:
        return json.load(f)


def save_checkpoint(checkpoint_path: str, data: dict):
    """Save checkpoint atomically."""
    os.makedirs(os.path.dirname(checkpoint_path), exist_ok=True)
    tmp = checkpoint_path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, default=str)
    os.replace(tmp, checkpoint_path)


def write_csv(results: List[dict], path: str):
    """Write results to CSV."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=CSV_FIELDS)
        writer.writeheader()
        writer.writerows(results)
    logger.info("CSV saved to %s (%d rows)", path, len(results))


def build_summary(results: List[dict]) -> dict:
    """Build JSON summary with per-condition stats and stratified analysis."""
    by_condition = defaultdict(list)
    by_instance = defaultdict(dict)

    for r in results:
        by_condition[r["condition"]].append(r)
        by_instance[r["instance_id"]][r["condition"]] = r

    condition_summary = {}
    for cond in CONDITIONS:
        rows = by_condition[cond]
        n = len(rows)
        if n == 0:
            continue
        successes = sum(1 for r in rows if r["repair_success"])
        condition_summary[cond] = {
            "count": n,
            "success": successes,
            "success_rate": round(successes / n, 4) if n else 0,
            "avg_tokens_input": round(sum(r["tokens_input"] for r in rows) / n, 1),
            "avg_tokens_output": round(sum(r["tokens_output"] for r in rows) / n, 1),
        }

    stratified = _stratified_analysis(results, by_instance)

    by_eval_method = defaultdict(list)
    for r in results:
        by_eval_method[r.get("eval_method", "none")].append(r)
    eval_method_summary = {}
    for method, rows in sorted(by_eval_method.items()):
        n = len(rows)
        successes = sum(1 for r in rows if r["repair_success"])
        eval_method_summary[method] = {
            "count": n,
            "success": successes,
            "success_rate": round(successes / n, 4) if n else 0,
        }

    return {
        "num_instances": len(by_instance),
        "conditions": condition_summary,
        "eval_methods": eval_method_summary,
        "stratified": stratified,
    }


def _stratified_analysis(results: List[dict], by_instance: dict) -> dict:
    """Compute stratified win rates."""
    stratified = {}

    # (a) >2K full trace tokens subset
    heavy_ids = set()
    light_ids = set()
    for iid, conds in by_instance.items():
        ft_tokens = 0
        for c in conds.values():
            ft_tokens = c.get("full_trace_tokens", 0)
            break
        if ft_tokens > 2000:
            heavy_ids.add(iid)
        else:
            light_ids.add(iid)

    for label, ids in [("full_trace_gt_2k_tokens", heavy_ids), ("full_trace_le_2k_tokens", light_ids)]:
        stratified[label] = _condition_stats(results, ids)

    # (b) >=5 structural segments vs <5
    high_seg_ids = set()
    low_seg_ids = set()
    for iid, conds in by_instance.items():
        ns = 0
        for c in conds.values():
            ns = c.get("num_structural_segments", 0)
            break
        if ns >= 5:
            high_seg_ids.add(iid)
        else:
            low_seg_ids.add(iid)

    for label, ids in [("structural_segments_ge5", high_seg_ids), ("structural_segments_lt5", low_seg_ids)]:
        stratified[label] = _condition_stats(results, ids)

    # (c) structural_filtered vs line_filtered head-to-head
    struct_wins = 0
    line_wins = 0
    ties = 0
    for iid, conds in by_instance.items():
        sf = conds.get("structural_filtered", {}).get("repair_success", False)
        lf = conds.get("line_filtered", {}).get("repair_success", False)
        if sf and not lf:
            struct_wins += 1
        elif lf and not sf:
            line_wins += 1
        else:
            ties += 1

    stratified["head_to_head_structural_vs_line"] = {
        "structural_wins": struct_wins,
        "line_wins": line_wins,
        "ties": ties,
        "total": struct_wins + line_wins + ties,
    }

    return stratified


def _condition_stats(results: List[dict], instance_ids: set) -> dict:
    """Per-condition success stats for a subset of instances."""
    by_cond = defaultdict(list)
    for r in results:
        if r["instance_id"] in instance_ids:
            by_cond[r["condition"]].append(r)
    stats = {"count": len(instance_ids)}
    for cond in CONDITIONS:
        rows = by_cond[cond]
        n = len(rows)
        if n == 0:
            continue
        s = sum(1 for r in rows if r["repair_success"])
        stats[cond] = {"count": n, "success": s, "success_rate": round(s / n, 4)}
    return stats


def main():
    parser = argparse.ArgumentParser(
        description="Phase 3: Repair comparison across 4 trace conditions (DTD)"
    )
    parser.add_argument(
        "--output-dir", default=PIPELINE_OUTPUT,
        help="Output directory (default: pipeline_output/)"
    )
    parser.add_argument(
        "--max-workers", type=int, default=3,
        help="Max concurrent repair API calls (default: 3)"
    )
    parser.add_argument(
        "--instances", type=str, default=None,
        help="Comma-separated instance keys to run (default: all)"
    )
    parser.add_argument(
        "--repair-model", default="deepseek/deepseek-v4-pro",
        help="Repair LLM model (default: deepseek/deepseek-v4-pro)"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="List instances and conditions without calling API"
    )
    args = parser.parse_args()

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(name)s %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )

    output_dir = args.output_dir
    os.makedirs(output_dir, exist_ok=True)

    # Validate required inputs
    try:
        structural_scores_map = load_phase2_scores("structural")
    except FileNotFoundError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    try:
        line_scores_map = load_phase2_scores("line")
    except FileNotFoundError:
        line_scores_map = {}
        logger.warning("Line scores not found, line_filtered condition will be skipped")

    # Instance discovery: based on structural scores (line scores optional)
    all_keys = sorted(set(structural_scores_map))
    if args.instances:
        requested = set(args.instances.split(","))
        all_keys = [k for k in all_keys if k in requested]

    if not all_keys:
        print("ERROR: No instances found in structural score file.", file=sys.stderr)
        sys.exit(1)

    has_line_scores = bool(line_scores_map)
    active_conditions = [c for c in CONDITIONS if c != "line_filtered" or has_line_scores]
    logger.info("Found %d instances (line scores: %s), conditions: %s",
                len(all_keys), "available" if has_line_scores else "missing", active_conditions)

    if args.dry_run:
        print(f"\n=== Phase 3 Dry Run ===")
        print(f"Instances: {len(all_keys)}")
        print(f"Conditions: {active_conditions}")
        print(f"Total API calls: {len(all_keys) * len(active_conditions)}")
        print(f"\nInstances:")
        for key in all_keys:
            ns = len(structural_scores_map.get(key, []))
            nsk = sum(1 for s in structural_scores_map.get(key, []) if s.get("label") == "keep")
            line_info = ""
            if key in line_scores_map:
                nl = len(line_scores_map[key])
                nlk = sum(1 for s in line_scores_map[key] if s.get("label") == "keep")
                line_info = f", line={nl} (keep={nlk})"
            print(f"  {key}: structural={ns} (keep={nsk}){line_info}")
        return

    # Resume support
    checkpoint_path = os.path.join(output_dir, "phase3_checkpoint.json")
    checkpoint = load_checkpoint(checkpoint_path)
    done_keys = set(checkpoint.keys())
    todo_keys = [k for k in all_keys if k not in done_keys]

    if done_keys:
        logger.info("Resuming: %d done, %d remaining", len(done_keys), len(todo_keys))

    if not todo_keys:
        logger.info("All instances already completed, regenerating outputs")
    else:
        # Initialize pipeline
        api_key = [REDACTED]"OPENROUTER_API_KEY", "") or os.environ.get("DEEPSEEK_API_KEY", "")
        if not api_key:
            print("ERROR: Set OPENROUTER_API_KEY or DEEPSEEK_API_KEY", file=sys.stderr)
            sys.exit(1)

        pipeline = MVPPipeline(
            repair_api_key=[REDACTED],
            repair_model=args.repair_model,
            output_dir=output_dir,
        )

        # Run with concurrency
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=args.max_workers) as pool:
            futures = {
                pool.submit(
                    run_instance, pipeline, key,
                    structural_scores_map[key], line_scores_map.get(key, []),
                ): key
                for key in todo_keys
            }
            for future in as_completed(futures):
                key = futures[future]
                try:
                    rows = future.result()
                    if rows:
                        checkpoint[key] = rows
                        save_checkpoint(checkpoint_path, checkpoint)
                        logger.info("Checkpoint saved (%d/%d)",
                                    len(checkpoint), len(all_keys))
                except Exception as e:
                    logger.error("Instance %s failed: %s", key, e)

        elapsed = time.time() - t0
        logger.info("All instances processed in %.1fs", elapsed)

    # Collect all results
    all_results = []
    for key in all_keys:
        if key in checkpoint:
            all_results.extend(checkpoint[key])

    # Write CSV
    csv_path = os.path.join(output_dir, "phase3_results.csv")
    write_csv(all_results, csv_path)

    # Build and write summary
    summary = build_summary(all_results)
    summary_path = os.path.join(output_dir, "phase3_summary.json")
    with open(summary_path, "w") as f:
        json.dump(summary, f, indent=2)
    logger.info("Summary saved to %s", summary_path)

    # Print summary
    print(f"\n{'='*60}")
    print(f"Phase 3 Results: {summary['num_instances']} instances x {len(CONDITIONS)} conditions")
    print(f"{'='*60}")
    for cond in CONDITIONS:
        cs = summary["conditions"].get(cond, {})
        if cs:
            print(f"  {cond:25s}: {cs['success']}/{cs['count']} "
                  f"({cs['success_rate']:.1%}) "
                  f"avg_tokens={cs['avg_tokens_input']:.0f}+{cs['avg_tokens_output']:.0f}")

    eval_methods = summary.get("eval_methods", {})
    if eval_methods:
        print(f"\nBy eval method:")
        for method, ms in eval_methods.items():
            print(f"  {method:25s}: {ms['success']}/{ms['count']} ({ms['success_rate']:.1%})")

    strat = summary.get("stratified", {})
    h2h = strat.get("head_to_head_structural_vs_line", {})
    if h2h:
        print(f"\nHead-to-head (structural vs line filtered):")
        print(f"  structural wins: {h2h['structural_wins']}")
        print(f"  line wins:       {h2h['line_wins']}")
        print(f"  ties:            {h2h['ties']}")

    for label in ["full_trace_gt_2k_tokens", "full_trace_le_2k_tokens",
                   "structural_segments_ge5", "structural_segments_lt5"]:
        sub = strat.get(label, {})
        if sub and sub.get("count", 0) > 0:
            print(f"\n  [{label}] (n={sub['count']}):")
            for cond in CONDITIONS:
                cs = sub.get(cond, {})
                if cs:
                    print(f"    {cond:25s}: {cs['success']}/{cs['count']} ({cs['success_rate']:.1%})")


if __name__ == "__main__":
    main()
