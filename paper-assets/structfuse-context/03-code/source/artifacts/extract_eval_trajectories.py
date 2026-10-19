#!/usr/bin/env python3
"""Extract per-step eval trajectories from wandb offline runs."""

import json
import os
import re
import csv
from pathlib import Path
from collections import defaultdict

import wandb
from wandb.sdk.internal.datastore import DataStore

WANDB_DIR = Path("/root/structfuse/wandb")
OUTPUT_DIR = Path("/root/autodl-tmp/structfuse/artifacts/neg_difficulty_analysis")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def parse_run_config(debug_log_path):
    """Extract config from debug.log."""
    config = {}
    with open(debug_log_path) as f:
        for line in f:
            if "config_cb" in line and "wandb_run_name" in line:
                # Extract the dict portion
                match = re.search(r"\{.*\}", line)
                if match:
                    try:
                        config = eval(match.group())
                    except:
                        pass
                break
    return config

def identify_model(config):
    """Determine model from config."""
    model_name = config.get("model_name", "")
    if "qwen" in model_name.lower() or "Qwen" in model_name:
        return "Qwen"
    elif "starcoder" in model_name.lower():
        return "StarCoder"
    return "unknown"

def parse_wandb_run(run_dir):
    """Parse a wandb offline run directory to extract step-level metrics."""
    run_dir = Path(run_dir)

    # Find the .wandb binary file
    wandb_files = list(run_dir.glob("run-*.wandb"))
    if not wandb_files:
        print(f"  No .wandb file in {run_dir}")
        return None, None

    # Get config from debug.log
    debug_log = run_dir / "logs" / "debug.log"
    config = {}
    if debug_log.exists():
        config = parse_run_config(debug_log)

    model = identify_model(config)
    strategy = config.get("hard_negative_strategy", "unknown")
    seed = config.get("seed", -1)
    run_name = config.get("wandb_run_name", run_dir.name)

    meta = {
        "model": model,
        "strategy": strategy,
        "seed": seed,
        "run_name": run_name,
        "run_dir": str(run_dir),
    }

    # Parse the binary wandb file using the internal API
    wandb_file = wandb_files[0]
    history = []

    try:
        ds = DataStore()
        ds.open_for_scan(str(wandb_file))

        while True:
            data = ds.scan_data()
            if data is None:
                break
            # data is a protobuf record - we need to decode it
            # Try to extract history records
    except Exception as e:
        print(f"  DataStore scan failed for {wandb_file}: {e}")

    return meta, history

def try_wandb_api_read(run_dir):
    """Alternative: use wandb Api to read offline run."""
    run_dir = Path(run_dir)
    wandb_files = list(run_dir.glob("run-*.wandb"))
    if not wandb_files:
        return []

    history = []
    try:
        from wandb.proto import wandb_internal_pb2
        import struct

        with open(wandb_files[0], "rb") as f:
            while True:
                # Read header
                header_bytes = f.read(4)
                if len(header_bytes) < 4:
                    break

                # Parse length-delimited protobuf records
                # wandb uses a custom format with Record messages
                try:
                    record = wandb_internal_pb2.Record()
                    # Read the full record
                    size_data = f.read(4)
                    if len(size_data) < 4:
                        break
                    size = struct.unpack("<I", size_data)[0]
                    if size > 10_000_000:  # sanity check
                        break
                    record_data = f.read(size)
                    if len(record_data) < size:
                        break
                    record.ParseFromString(record_data)

                    # Check if this is a history record
                    if record.HasField("history"):
                        row = {}
                        for item in record.history.item:
                            try:
                                row[item.key] = json.loads(item.value_json)
                            except:
                                pass
                        if row:
                            history.append(row)
                except Exception:
                    # Skip malformed records
                    f.seek(-3, 1)  # back up and try next byte
                    f.read(1)
                    continue
    except Exception as e:
        print(f"  Proto parse failed: {e}")

    return history

def extract_from_wandb_sdk(run_dir):
    """Use wandb's own reader to extract history from offline run."""
    import subprocess
    import tempfile

    run_dir = Path(run_dir)
    run_id = None
    wandb_files = list(run_dir.glob("run-*.wandb"))
    if wandb_files:
        # Extract run ID from filename
        match = re.search(r"run-(\w+)\.wandb", wandb_files[0].name)
        if match:
            run_id = match.group(1)

    if not run_id:
        return []

    # Use wandb sync --dry-run to get readable output, or directly parse
    # Actually let's use the wandb SDK's internal tools
    try:
        from wandb.sdk.internal.datastore import DataStore
        from wandb.proto import wandb_internal_pb2 as pb

        ds = DataStore()
        ds.open_for_scan(str(wandb_files[0]))

        history = []
        while True:
            data = ds.scan_data()
            if data is None:
                break

            record = pb.Record()
            try:
                record.ParseFromString(data)
            except:
                continue

            if record.HasField("history"):
                row = {}
                for item in record.history.item:
                    try:
                        row[item.key] = json.loads(item.value_json)
                    except:
                        pass
                if row:
                    history.append(row)

        return history
    except Exception as e:
        print(f"  SDK extraction failed for {run_dir}: {e}")
        return []


def main():
    print("=== Extracting eval trajectories from wandb offline runs ===\n")

    # Find all offline run directories
    run_dirs = sorted(WANDB_DIR.glob("offline-run-*"))
    print(f"Found {len(run_dirs)} offline runs\n")

    all_rows = []

    for run_dir in run_dirs:
        print(f"Processing: {run_dir.name}")

        # Get config
        debug_log = run_dir / "logs" / "debug.log"
        config = {}
        if debug_log.exists():
            config = parse_run_config(debug_log)

        model = identify_model(config)
        strategy = config.get("hard_negative_strategy", "unknown")
        seed = config.get("seed", -1)
        run_name = config.get("wandb_run_name", run_dir.name)

        print(f"  Config: model={model}, strategy={strategy}, seed={seed}, run_name={run_name}")

        # Extract history
        history = extract_from_wandb_sdk(run_dir)
        print(f"  History records: {len(history)}")

        # Filter for eval records (those with val_loss or recall@1)
        eval_records = []
        for row in history:
            if "val_loss" in row or "recall@1" in row:
                eval_records.append(row)

        print(f"  Eval records: {len(eval_records)}")

        for rec in eval_records:
            step = rec.get("_step", rec.get("train/global_step", -1))
            all_rows.append({
                "model": model,
                "strategy": strategy,
                "seed": seed,
                "step": step,
                "eval_loss": rec.get("val_loss", ""),
                "recall_at_1": rec.get("recall@1", ""),
                "recall_at_5": rec.get("recall@5", ""),
                "recall_at_10": rec.get("recall@10", ""),
                "mrr": rec.get("mrr", ""),
                "run_name": run_name,
            })

        # Also print all step-level records for debugging
        step_records = [r for r in history if "_step" in r]
        if step_records:
            print(f"  Step records sample (first 3):")
            for r in step_records[:3]:
                print(f"    {r}")
        elif history:
            print(f"  Sample records (first 3):")
            for r in history[:3]:
                keys = list(r.keys())[:10]
                print(f"    keys={keys}")

        print()

    # Write CSV
    csv_path = OUTPUT_DIR / "eval_trajectories.csv"
    if all_rows:
        fieldnames = ["model", "strategy", "seed", "step", "eval_loss",
                       "recall_at_1", "recall_at_5", "recall_at_10", "mrr", "run_name"]
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(all_rows)
        print(f"\nWrote {len(all_rows)} eval records to {csv_path}")
    else:
        print("\nNo eval records found! Dumping all history keys for debugging.")
        # Re-scan and show what keys exist
        for run_dir in run_dirs[:2]:
            history = extract_from_wandb_sdk(run_dir)
            if history:
                all_keys = set()
                for r in history:
                    all_keys.update(r.keys())
                print(f"  {run_dir.name}: keys = {sorted(all_keys)}")

    # Summary
    print(f"\n=== Summary ===")
    print(f"Total runs processed: {len(run_dirs)}")
    print(f"Total eval records: {len(all_rows)}")

    # Group by model/strategy/seed
    groups = defaultdict(list)
    for row in all_rows:
        key = f"{row['model']}_{row['strategy']}_s{row['seed']}"
        groups[key].append(row)

    for key in sorted(groups):
        rows = groups[key]
        steps = [r["step"] for r in rows]
        print(f"  {key}: {len(rows)} evals, steps {min(steps)}-{max(steps)}")


if __name__ == "__main__":
    main()
