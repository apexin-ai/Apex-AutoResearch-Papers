# build_cwm_data.py — Convert (code, test, label) data to CWM generation format
# Input: data/{train,val,test}.jsonl with fields: code, test, label, source, problem_id, mutation_type
# Output: data/{cwm_train,cwm_val,cwm_test}.jsonl with target = execution output string
# Key difference from classification: label 0/1 → target string with actual error messages
# For fail samples, re-executes code+test to capture stderr; pass samples get fixed string.

import argparse
import json
import logging
import os
import re
import subprocess
import sys
from collections import Counter

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

PASS_TARGET = "PASS: test completed successfully"
DEFAULT_TIMEOUT = 5


def load_jsonl(path):
    with open(path) as f:
        return [json.loads(line) for line in f]


def save_jsonl(data, path):
    with open(path, "w") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")


def execute_and_capture(code: str, test: str, timeout: int) -> str:
    """Execute code + test, return formatted error string for failures."""
    full_code = code + "\n" + test
    try:
        result = subprocess.run(
            [sys.executable, "-c", full_code],
            capture_output=True, text=True, timeout=timeout,
        )
        if result.returncode == 0:
            return PASS_TARGET

        stderr = result.stderr.strip()
        if not stderr:
            stdout = result.stdout.strip()
            if stdout:
                return f"FAIL: Error: {stdout.splitlines()[-1]}"
            return "FAIL: Error: non-zero exit code"

        # Extract the last exception line from traceback
        lines = stderr.strip().splitlines()
        # Find the last line that looks like an exception
        error_line = None
        for line in reversed(lines):
            line = line.strip()
            if re.match(r"^[A-Za-z][\w.]*Error:", line) or \
               re.match(r"^[A-Za-z][\w.]*Exception:", line) or \
               re.match(r"^AssertionError", line) or \
               re.match(r"^AssertionError:", line):
                error_line = line
                break

        if error_line is None:
            # Fallback: use last non-empty line
            for line in reversed(lines):
                if line.strip():
                    error_line = line.strip()
                    break

        if error_line:
            # Truncate overly long error messages
            if len(error_line) > 200:
                error_line = error_line[:200] + "..."
            return f"FAIL: {error_line}"
        return "FAIL: Error: unknown error"

    except subprocess.TimeoutExpired:
        return "FAIL: RuntimeError: execution timeout"
    except Exception as e:
        return f"FAIL: Error: {type(e).__name__}"


def process_split(data, timeout, split_name):
    """Process a data split, adding target field."""
    results = []
    stats = Counter()

    for i, ex in enumerate(data):
        label = ex["label"]

        if label == 1:
            target = PASS_TARGET
            stats["pass_direct"] += 1
        else:
            target = execute_and_capture(ex["code"], ex["test"], timeout)
            if target.startswith("PASS"):
                # Execution passed but label says fail — keep original label, force fail target
                log.warning(f"{split_name}[{i}]: label=0 but execution passed, using generic fail")
                target = "FAIL: AssertionError"
                stats["fail_mismatch"] += 1
            else:
                stats["fail_executed"] += 1

        # Extract error type for stats
        if target.startswith("FAIL:"):
            error_part = target[6:].strip()
            error_type = error_part.split(":")[0].strip() if ":" in error_part else error_part
            stats[f"error_type_{error_type}"] += 1

        results.append({
            "code": ex["code"],
            "test": ex["test"],
            "target": target,
            "label": label,
            "source": ex.get("source", ""),
            "problem_id": ex.get("problem_id", ""),
            "mutation_type": ex.get("mutation_type", ""),
        })

        if (i + 1) % 1000 == 0:
            log.info(f"  {split_name}: {i+1}/{len(data)} processed")

    return results, stats


def main():
    p = argparse.ArgumentParser(
        description="Convert classification data to CWM generation format"
    )
    p.add_argument("--input_dir", default="data/", help="Directory with {train,val,test}.jsonl")
    p.add_argument("--output_dir", default="data/", help="Output directory for cwm_*.jsonl")
    p.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT, help="Execution timeout per sample (seconds)")
    args = p.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)

    all_stats = {}
    for split in ["train", "val", "test"]:
        input_path = os.path.join(args.input_dir, f"{split}.jsonl")
        output_path = os.path.join(args.output_dir, f"cwm_{split}.jsonl")

        if not os.path.exists(input_path):
            log.warning(f"Skipping {split}: {input_path} not found")
            continue

        log.info(f"Processing {split}...")
        data = load_jsonl(input_path)
        log.info(f"  Loaded {len(data)} examples")

        results, stats = process_split(data, args.timeout, split)
        save_jsonl(results, output_path)

        all_stats[split] = dict(stats)
        log.info(f"  Saved {output_path}: {len(results)} examples")
        log.info(f"  Stats: {dict(stats)}")

    # Summary
    print(f"\n{'='*60}")
    print("CWM DATA CONVERSION SUMMARY")
    print(f"{'='*60}")
    for split, stats in all_stats.items():
        n_pass = stats.get("pass_direct", 0)
        n_fail = stats.get("fail_executed", 0) + stats.get("fail_mismatch", 0)
        print(f"\n{split}: {n_pass + n_fail} total (pass={n_pass}, fail={n_fail})")
        if stats.get("fail_mismatch", 0):
            print(f"  WARNING: {stats['fail_mismatch']} label=0 samples passed on re-execution")
        error_types = {k: v for k, v in stats.items() if k.startswith("error_type_")}
        if error_types:
            print("  Error types:")
            for k, v in sorted(error_types.items(), key=lambda x: -x[1]):
                print(f"    {k.replace('error_type_', '')}: {v}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
