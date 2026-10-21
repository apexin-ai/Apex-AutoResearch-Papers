"""
merge_shards.py — Merge shard output files into a single generations.jsonl.

Reads data/{model_name}/generations_shard{0..N-1}.jsonl, re-assigns contiguous IDs
sorted by (seed_id, depth), writes to data/{model_name}/generations.jsonl.
"""

import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--num-shards", type=int, default=4)
    parser.add_argument("--data-dir", type=str, default="/root/gen-depth-fingerprint/data")
    parser.add_argument("--model-name", type=str, default=None,
                        help="Model subdirectory name (e.g. 'pythia-1b')")
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()

    shard_dir = os.path.join(args.data_dir, args.model_name) if args.model_name else args.data_dir
    output_path = args.output or os.path.join(shard_dir, "generations.jsonl")

    records = []
    for shard_id in range(args.num_shards):
        shard_path = os.path.join(shard_dir, f"generations_shard{shard_id}.jsonl")
        if not os.path.exists(shard_path):
            print(f"[WARN] Missing shard file: {shard_path}")
            continue
        with open(shard_path) as f:
            for line in f:
                records.append(json.loads(line))
        print(f"Loaded {shard_path}")

    records.sort(key=lambda r: (r["seed_id"], r["depth"]))

    for i, rec in enumerate(records):
        rec["id"] = i

    with open(output_path, "w") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")

    print(f"Merged {len(records)} records from {args.num_shards} shards -> {output_path}")


if __name__ == "__main__":
    main()
