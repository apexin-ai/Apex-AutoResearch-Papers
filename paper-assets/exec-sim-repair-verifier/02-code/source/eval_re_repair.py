#!/usr/bin/env python3
"""Re-Repair Docker eval pipeline using SWE-bench harness v4.1.0."""

import argparse
import hashlib
import json
import time
from collections import defaultdict
from pathlib import Path

from datasets import load_dataset
from swebench.harness.run_evaluation import (
    RUN_EVALUATION_LOG_DIR,
    LOG_REPORT,
    main as swebench_main,
)


def dedup_predictions(entries):
    """Deduplicate entries by (instance_id, extracted_diff). Returns dedup map and unique list."""
    seen = {}
    for entry in entries:
        key = (entry["instance_id"], entry["extracted_diff"])
        if key not in seen:
            seen[key] = []
        seen[key].append(entry)
    return seen


def make_model_name(diff_text):
    """Generate a deterministic model name from diff content."""
    h = hashlib.md5(diff_text.encode()).hexdigest()[:12]
    return f"re_repair_{h}"


def batch_by_instance_id(unique_pairs):
    """Split unique (instance_id, diff) pairs into batches where each batch has unique instance_ids."""
    instance_to_pairs = defaultdict(list)
    for key in unique_pairs:
        instance_id = key[0]
        instance_to_pairs[instance_id].append(key)

    max_batches = max(len(v) for v in instance_to_pairs.values()) if instance_to_pairs else 1
    batches = [[] for _ in range(max_batches)]
    for instance_id, pairs in instance_to_pairs.items():
        for i, pair in enumerate(pairs):
            batches[i].append(pair)
    return batches


def write_predictions_file(batch_keys, dedup_map, output_path):
    """Write a swebench-compatible predictions JSONL for a batch."""
    preds = []
    for key in batch_keys:
        instance_id, diff = key
        model_name = make_model_name(diff)
        preds.append({
            "instance_id": instance_id,
            "model_name_or_path": model_name,
            "model_patch": diff,
        })
    with open(output_path, "w") as f:
        for pred in preds:
            f.write(json.dumps(pred) + "\n")
    return preds


def parse_reports(run_id, preds):
    """Parse swebench report files and return results keyed by (instance_id, model_name)."""
    results = {}
    for pred in preds:
        instance_id = pred["instance_id"]
        model_name = pred["model_name_or_path"].replace("/", "__")
        report_path = RUN_EVALUATION_LOG_DIR / run_id / model_name / instance_id / LOG_REPORT
        result = {
            "resolved": False,
            "error": None,
        }
        if report_path.exists():
            try:
                content = report_path.read_text().strip()
                if content:
                    report = json.loads(content)
                    if instance_id in report:
                        result["resolved"] = report[instance_id].get("resolved", False)
                        tests_status = report[instance_id].get("tests_status", {})
                        result["tests_status"] = tests_status
            except (json.JSONDecodeError, KeyError) as e:
                result["error"] = str(e)
        else:
            result["error"] = f"Report not found: {report_path}"
        results[(instance_id, pred["model_patch"])] = result
    return results


def extract_test_details(tests_status):
    """Extract f2p_passed, f2p_failed, p2p_regressed from tests_status.

    SWE-bench v4.1.0 format: {"FAIL_TO_PASS": {"success": [...], "failure": [...]}, ...}
    """
    f2p_passed = []
    f2p_failed = []
    p2p_regressed = []

    if not tests_status:
        return f2p_passed, f2p_failed, p2p_regressed

    f2p = tests_status.get("FAIL_TO_PASS", {})
    f2p_passed = f2p.get("success", [])
    f2p_failed = f2p.get("failure", [])

    p2p = tests_status.get("PASS_TO_PASS", {})
    p2p_regressed = p2p.get("failure", [])

    return f2p_passed, f2p_failed, p2p_regressed


def main():
    parser = argparse.ArgumentParser(description="Re-Repair eval via SWE-bench Docker harness")
    parser.add_argument("--predictions", required=True, help="Input JSONL with extracted_diff")
    parser.add_argument("--output-dir", required=True, help="Output directory for results")
    parser.add_argument("--max-workers", type=int, default=4, help="Max parallel Docker containers")
    parser.add_argument("--timeout", type=int, default=300, help="Timeout per instance (seconds)")
    parser.add_argument("--dataset", default="princeton-nlp/SWE-bench_Verified", help="SWE-bench dataset name")
    parser.add_argument("--split", default="test", help="Dataset split")
    parser.add_argument("--cache-level", default="env", choices=["none", "base", "env", "instance"],
                        help="Docker image cache level")
    parser.add_argument("--instance-ids", nargs="*", default=None, help="Filter to specific instance IDs")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Load input predictions
    with open(args.predictions) as f:
        entries = [json.loads(line) for line in f if line.strip()]
    print(f"Loaded {len(entries)} entries from {args.predictions}")

    # Filter by instance_ids if specified
    if args.instance_ids:
        id_set = set(args.instance_ids)
        entries = [e for e in entries if e["instance_id"] in id_set]
        print(f"Filtered to {len(entries)} entries for {len(id_set)} instance IDs")

    # Deduplicate
    dedup_map = dedup_predictions(entries)
    unique_keys = list(dedup_map.keys())
    print(f"Unique (instance_id, diff) pairs: {len(unique_keys)}")

    # Batch so each batch has unique instance_ids
    batches = batch_by_instance_id(unique_keys)
    print(f"Split into {len(batches)} eval batches")

    # Run each batch
    all_results = {}
    total_start = time.time()

    for batch_idx, batch_keys in enumerate(batches):
        run_id = f"re_repair_batch_{batch_idx}"
        pred_file = output_dir / f"_tmp_preds_batch_{batch_idx}.jsonl"

        print(f"\n--- Batch {batch_idx + 1}/{len(batches)}: {len(batch_keys)} instances ---")
        preds = write_predictions_file(batch_keys, dedup_map, pred_file)

        batch_start = time.time()
        try:
            swebench_main(
                dataset_name=args.dataset,
                split=args.split,
                instance_ids=[k[0] for k in batch_keys],
                predictions_path=str(pred_file),
                max_workers=args.max_workers,
                force_rebuild=False,
                cache_level=args.cache_level,
                clean=False,
                open_file_limit=4096,
                run_id=run_id,
                timeout=args.timeout,
                namespace="swebench",
                rewrite_reports=False,
                modal=False,
                report_dir=str(output_dir),
            )
        except Exception as e:
            print(f"Batch {batch_idx} error: {e}")

        batch_duration = time.time() - batch_start
        print(f"Batch {batch_idx} completed in {batch_duration:.1f}s")

        # Parse reports
        batch_results = parse_reports(run_id, preds)
        all_results.update(batch_results)

        # Cleanup temp file
        pred_file.unlink(missing_ok=True)

    total_duration = time.time() - total_start
    print(f"\nTotal eval time: {total_duration:.1f}s")

    # Map results back to original entries and write output
    output_file = output_dir / "eval_results.jsonl"
    resolved_count = 0
    with open(output_file, "w") as f:
        for entry in entries:
            key = (entry["instance_id"], entry["extracted_diff"])
            result = all_results.get(key, {"resolved": False, "error": "eval not run"})
            tests_status = result.get("tests_status", {})
            f2p_passed, f2p_failed, p2p_regressed = extract_test_details(tests_status)

            out = {
                "instance_id": entry["instance_id"],
                "condition": entry.get("condition", ""),
                "sample_k": entry.get("sample_k", 0),
                "resolved": result["resolved"],
                "f2p_passed": f2p_passed,
                "f2p_failed": f2p_failed,
                "p2p_regressed": p2p_regressed,
                "eval_duration_seconds": total_duration / max(len(unique_keys), 1),
                "error": result.get("error"),
            }
            if out["resolved"]:
                resolved_count += 1
            f.write(json.dumps(out) + "\n")

    print(f"\nResults written to {output_file}")
    print(f"Resolved: {resolved_count}/{len(entries)} ({100*resolved_count/max(len(entries),1):.1f}%)")


if __name__ == "__main__":
    main()
