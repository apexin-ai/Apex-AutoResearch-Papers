"""Convert Phase 2 teacher scoring results to student model training data (JSONL).

Reads phase2_{structural,line}_scores.json, pairs each scored segment with its
trace text and instance context, outputs JSONL with input/output/metadata fields.
Supports train/val splitting and flexible field name detection.

Usage:
    python convert_scoring_to_training.py --mode both --train-ratio 0.8
    python convert_scoring_to_training.py --mode structural --train-ratio 0.9 --with-context
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple

PIPELINE_OUTPUT = "/root/trace_distill_repair/pipeline_output"
WORKSPACE = "/root/trace_distill_repair/bugsinpy_workspace"
OUTPUT_DIR = "/root/trace_distill_repair/pipeline_output/training_data"

CANDIDATE_BUGS = [
    ("thefuck", 1, "multi-function call chain, rule matching logic"),
    ("thefuck", 2, "exception handling in shell command execution"),
    ("thefuck", 4, "string processing across helper functions"),
    ("black", 1, "AST traversal with recursive formatting"),
    ("black", 2, "multi-function string normalization"),
    ("black", 5, "bracket split trailing comma detection loop"),
    ("black", 14, "future imports recursive AST child traversal"),
    ("cookiecutter", 1, "template rendering call chain"),
    ("cookiecutter", 2, "file I/O with exception handling"),
    ("cookiecutter", 3, "config parsing multi-step pipeline"),
    ("fastapi", 1, "request routing with dependency injection"),
    ("fastapi", 2, "response model validation chain"),
    ("fastapi", 3, "middleware exception propagation"),
    ("fastapi", 5, "recursive model field cloning chain"),
    ("httpie", 1, "request building multi-function pipeline"),
    ("httpie", 2, "header parsing with edge cases"),
    ("luigi", 1, "task dependency resolution chain"),
    ("luigi", 2, "scheduler loop iteration bug"),
    ("luigi", 5, "task decorator inheritance chain (inherits/requires)"),
    ("luigi", 10, "worker pending task filtering in scheduler loop"),
    ("luigi", 14, "scheduler failure detection state machine"),
    ("pandas", 1, "DataFrame operation call chain"),
    ("pandas", 2, "indexing with type coercion across functions"),
    ("pandas", 3, "groupby aggregation pipeline"),
    ("rich", 1, "console rendering with style inheritance"),
    ("rich", 3, "table formatting recursive layout"),
    ("sanic", 1, "request handling middleware chain"),
    ("sanic", 2, "routing with exception fallback"),
    ("scrapy", 1, "spider callback chain processing"),
    ("scrapy", 2, "middleware pipeline with error handling"),
    ("scrapy", 3, "redirect middleware URL scheme rewriting chain"),
    ("scrapy", 4, "contract errback callback chain exc_info ordering"),
    ("scrapy", 7, "form request URL extraction pipeline"),
    ("tornado", 1, "async handler call chain"),
    ("tornado", 2, "IOLoop callback exception handling"),
    ("tornado", 4, "StaticFileHandler range request multi-branch processing"),
    ("tornado", 5, "PeriodicCallback timer update loop logic"),
    ("tornado", 7, "IOLoop run_in_executor future chaining"),
    ("tqdm", 1, "progress bar update loop logic"),
    ("tqdm", 2, "format_meter multi-branch computation"),
    ("youtube-dl", 1, "extractor call chain with fallback"),
    ("youtube-dl", 2, "format selection multi-step pipeline"),
    ("youtube-dl", 5, "unified_timestamp multi-format date parsing pipeline"),
    ("youtube-dl", 10, "js_to_json regex substitution pipeline"),
    ("youtube-dl", 20, "HTML element attribute extraction iteration"),
]

INSTANCE_DESCRIPTIONS = {f"{proj}_{bid}": desc for proj, bid, desc in CANDIDATE_BUGS}

LABEL_FIELD_NAMES = ("label", "decision", "score", "verdict", "classification")
VALID_LABELS = {"keep", "drop"}


def extract_label(entry: dict) -> Optional[str]:
    """Extract label from a score entry, handling field name variations."""
    for field_name in LABEL_FIELD_NAMES:
        val = entry.get(field_name)
        if val is None:
            continue
        val_lower = str(val).lower().strip()
        if val_lower in VALID_LABELS:
            return val_lower
        if val_lower in ("error", "parse_failure", "unknown", "skip"):
            return None
    return None


def extract_confidence(entry: dict) -> float:
    for field_name in ("confidence", "score", "prob", "probability"):
        val = entry.get(field_name)
        if val is not None and isinstance(val, (int, float)):
            return float(val)
    return 0.0


def extract_reasoning(entry: dict) -> str:
    for field_name in ("reasoning", "reason", "explanation", "rationale"):
        val = entry.get(field_name)
        if val and isinstance(val, str):
            return val
    return ""


def format_event_text(event: dict) -> str:
    parts = [
        f"[{event.get('event_type', '?'):9s}]",
        f"{event.get('function_name', '?')}:{event.get('lineno', 0)}",
        f"depth={event.get('call_depth', 0)}",
    ]
    locals_snap = event.get("locals_snapshot", {})
    if locals_snap:
        key_locals = dict(list(locals_snap.items())[:5])
        parts.append(f"locals={key_locals}")
    if event.get("return_value") is not None:
        parts.append(f"-> {repr(event['return_value'])[:100]}")
    exc = event.get("exception_info")
    if exc:
        if isinstance(exc, dict):
            parts.append(f"EXCEPTION: {exc.get('type', '')}: {exc.get('value', '')}")
        elif isinstance(exc, (list, tuple)) and len(exc) >= 2:
            parts.append(f"EXCEPTION: {exc[0]}: {exc[1]}")
    return " ".join(parts)


def format_segment_trace(segment_data: dict, max_events: int = 50) -> str:
    events = segment_data.get("events", [])
    lines = [format_event_text(ev) for ev in events[:max_events]]
    if len(events) > max_events:
        lines.append(f"... ({len(events) - max_events} more events)")
    return "\n".join(lines)


def load_segments_by_key(instance_key: str, mode: str, pipeline_dir: str) -> Dict[tuple, dict]:
    suffix = "structural_segments" if mode == "structural" else "line_segments"
    path = os.path.join(pipeline_dir, f"{instance_key}_{suffix}.json")
    if not os.path.isfile(path):
        return {}
    with open(path) as f:
        raw = json.load(f)
    index = {}
    for seg in raw:
        key = (seg.get("segment_type", ""), seg.get("start_idx", 0), seg.get("end_idx", 0))
        index[key] = seg
    return index


def get_buggy_code(instance_key: str, workspace: str) -> str:
    parts = instance_key.rsplit("_", 1)
    if len(parts) != 2:
        return ""
    project, bug_id = parts
    buggy_dir = os.path.join(workspace, "instances", instance_key, "buggy")
    if not os.path.isdir(buggy_dir):
        return ""
    bug_info_path = os.path.join(
        workspace, "BugsInPy", "projects", project, "bugs", bug_id, "bug.info"
    )
    buggy_file = ""
    if os.path.isfile(bug_info_path):
        with open(bug_info_path) as f:
            for line in f:
                line = line.strip()
                if "=" in line:
                    key, _, value = line.partition("=")
                    if key.strip().lower() == "buggy_file":
                        buggy_file = value.strip().strip('"')
                        break
    if buggy_file:
        path = os.path.join(buggy_dir, buggy_file)
        if os.path.isfile(path):
            with open(path) as f:
                return f.read()
    for root, dirs, files in os.walk(buggy_dir):
        dirs[:] = [d for d in dirs if d not in (".git", "__pycache__", ".tox", "venv")]
        for fn in sorted(files):
            if fn.endswith(".py") and not fn.startswith("test_") and fn != "setup.py":
                with open(os.path.join(root, fn)) as fh:
                    return fh.read()
    return ""


def build_input_text(
    trace_text: str,
    segment_type: str,
    instance_key: str,
    issue_desc: str,
    buggy_code: str,
    with_context: bool,
    neighbors: Optional[List[str]] = None,
) -> str:
    """Build the input string for a training sample."""
    parts = [f"## Trace Segment ({segment_type})\n{trace_text}"]
    if with_context:
        parts.insert(0, f"## Instance: {instance_key}\n## Bug: {issue_desc}")
        if buggy_code:
            code_snippet = buggy_code[:4000]
            if len(buggy_code) > 4000:
                code_snippet += "\n... (truncated)"
            parts.insert(1, f"## Buggy Code\n```python\n{code_snippet}\n```")
        if neighbors:
            parts.append("## Adjacent Segments (summary)\n" + "\n".join(neighbors[:3]))
    return "\n\n".join(parts)


def get_neighbor_summaries(
    seg_index: Dict[tuple, dict], current_key: tuple, n: int = 2
) -> List[str]:
    """Get short summaries of adjacent segments by index proximity."""
    all_keys = sorted(seg_index.keys(), key=lambda k: k[1])
    try:
        pos = all_keys.index(current_key)
    except ValueError:
        return []
    summaries = []
    for offset in range(-n, n + 1):
        if offset == 0:
            continue
        idx = pos + offset
        if 0 <= idx < len(all_keys):
            neighbor = seg_index[all_keys[idx]]
            ev_count = len(neighbor.get("events", []))
            summaries.append(
                f"[{neighbor.get('segment_type', '?')}] "
                f"idx {neighbor.get('start_idx', '?')}-{neighbor.get('end_idx', '?')}, "
                f"{ev_count} events"
            )
    return summaries


def convert_scores(
    scoring_path: str,
    mode: str,
    pipeline_dir: str,
    workspace: str,
    with_context: bool,
) -> Tuple[List[dict], dict]:
    """Convert a single scoring file to training samples."""
    with open(scoring_path) as f:
        scoring_data = json.load(f)

    results = scoring_data.get("results", scoring_data)
    if not isinstance(results, dict):
        print(f"ERROR: unexpected format in {scoring_path}", file=sys.stderr)
        return [], {"error": "unexpected format"}

    samples = []
    stats = Counter()

    for instance_key, inst_data in results.items():
        if isinstance(inst_data, dict):
            score_entries = inst_data.get("scores", inst_data.get("segments", []))
        elif isinstance(inst_data, list):
            score_entries = inst_data
        else:
            continue

        issue_desc = INSTANCE_DESCRIPTIONS.get(instance_key, f"{instance_key} bug")
        buggy_code = get_buggy_code(instance_key, workspace) if with_context else ""
        seg_index = load_segments_by_key(instance_key, mode, pipeline_dir)

        for entry in score_entries:
            stats["total_scored"] += 1
            label = extract_label(entry)
            if label is None:
                stats["filtered_error"] += 1
                continue

            seg_key = (
                entry.get("segment_type", ""),
                entry.get("start_idx", 0),
                entry.get("end_idx", 0),
            )
            segment_data = seg_index.get(seg_key)
            if segment_data is None:
                stats["missing_segment"] += 1
                trace_text = entry.get("segment_text", entry.get("content", entry.get("code", "")))
                if not trace_text:
                    continue
            else:
                trace_text = format_segment_trace(segment_data)

            neighbors = (
                get_neighbor_summaries(seg_index, seg_key)
                if with_context and segment_data
                else None
            )

            input_text = build_input_text(
                trace_text=trace_text,
                segment_type=entry.get("segment_type", mode),
                instance_key=instance_key,
                issue_desc=issue_desc,
                buggy_code=buggy_code,
                with_context=with_context,
                neighbors=neighbors,
            )

            sample = {
                "input": input_text,
                "output": label,
                "metadata": {
                    "instance_id": instance_key,
                    "segment_id": f"{entry.get('segment_type', mode)}_{seg_key[1]}_{seg_key[2]}",
                    "segment_type": mode,
                    "teacher_confidence": extract_confidence(entry),
                    "teacher_reasoning": extract_reasoning(entry),
                },
            }
            samples.append(sample)
            stats[f"label_{label}"] += 1

    summary = {
        "mode": mode,
        "source": os.path.basename(scoring_path),
        "total_scored": stats["total_scored"],
        "total_samples": len(samples),
        "filtered_error": stats["filtered_error"],
        "missing_segment": stats["missing_segment"],
        "label_keep": stats["label_keep"],
        "label_drop": stats["label_drop"],
        "instances": len(set(s["metadata"]["instance_id"] for s in samples)),
    }
    return samples, summary


def write_jsonl(samples: List[dict], path: str) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        for sample in samples:
            f.write(json.dumps(sample, ensure_ascii=False) + "\n")


def train_val_split(
    samples: List[dict], train_ratio: float, seed: int = 42
) -> Tuple[List[dict], List[dict]]:
    """Split samples by instance_id so all segments from one instance stay together."""
    instance_ids = sorted(set(s["metadata"]["instance_id"] for s in samples))
    rng = random.Random(seed)
    rng.shuffle(instance_ids)
    split_idx = max(1, int(len(instance_ids) * train_ratio))
    train_ids = set(instance_ids[:split_idx])
    val_ids = set(instance_ids[split_idx:])

    train = [s for s in samples if s["metadata"]["instance_id"] in train_ids]
    val = [s for s in samples if s["metadata"]["instance_id"] in val_ids]
    return train, val


def main():
    parser = argparse.ArgumentParser(
        description="Convert Phase 2 teacher scoring to student training data (JSONL)"
    )
    parser.add_argument(
        "--mode", choices=["structural", "line", "both"], default="both",
        help="Which scoring type to convert (default: both)",
    )
    parser.add_argument(
        "--train-ratio", type=float, default=0.8,
        help="Fraction of instances for training set (default: 0.8)",
    )
    parser.add_argument("--scoring-dir", default=PIPELINE_OUTPUT)
    parser.add_argument("--workspace", default=WORKSPACE)
    parser.add_argument("--output-dir", default=OUTPUT_DIR)
    parser.add_argument(
        "--with-context", action="store_true",
        help="Include instance context (bug description, buggy code, neighbor summaries) in input",
    )
    parser.add_argument("--seed", type=int, default=42, help="Random seed for split")
    parser.add_argument(
        "--structural-scores-file", default=None,
        help="Override structural scores filename",
    )
    parser.add_argument(
        "--line-scores-file", default=None,
        help="Override line scores filename",
    )
    args = parser.parse_args()

    modes = ["structural", "line"] if args.mode == "both" else [args.mode]
    all_samples: List[dict] = []

    for mode in modes:
        if mode == "structural" and args.structural_scores_file:
            scoring_path = os.path.join(args.scoring_dir, args.structural_scores_file)
        elif mode == "line" and args.line_scores_file:
            scoring_path = os.path.join(args.scoring_dir, args.line_scores_file)
        else:
            scoring_path = os.path.join(args.scoring_dir, f"phase2_{mode}_scores.json")

        if not os.path.isfile(scoring_path):
            print(f"SKIP {mode}: {scoring_path} not found")
            continue

        samples, summary = convert_scores(
            scoring_path, mode, args.scoring_dir, args.workspace, args.with_context
        )
        all_samples.extend(samples)

        print(f"\n=== {mode} ===")
        print(f"  source:    {summary['source']}")
        print(f"  samples:   {summary['total_samples']}")
        print(f"  keep/drop: {summary['label_keep']}/{summary['label_drop']}")
        print(f"  filtered:  {summary['filtered_error']} error, {summary['missing_segment']} missing segment")
        print(f"  instances: {summary['instances']}")

    if not all_samples:
        print("\nNo samples produced. Check that scoring files exist.")
        sys.exit(1)

    train, val = train_val_split(all_samples, args.train_ratio, args.seed)

    train_path = os.path.join(args.output_dir, "train.jsonl")
    val_path = os.path.join(args.output_dir, "val.jsonl")
    write_jsonl(train, train_path)
    write_jsonl(val, val_path)

    keep_total = sum(1 for s in all_samples if s["output"] == "keep")
    drop_total = sum(1 for s in all_samples if s["output"] == "drop")

    print(f"\n=== Summary ===")
    print(f"  total:     {len(all_samples)} samples ({keep_total} keep, {drop_total} drop)")
    if all_samples:
        print(f"  keep rate: {keep_total / len(all_samples):.1%}")
    print(f"  train:     {len(train)} -> {train_path}")
    print(f"  val:       {len(val)} -> {val_path}")


if __name__ == "__main__":
    main()
