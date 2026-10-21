"""合并 4 个 shard 的 generation JSONL 到一个文件。

Dedup strategy: last-wins (shard > root). Root data was generated before
generation_config fix (top_k=20, T=0.6), shards are post-fix (top_k=0, T=0.7).

用法:
  python -m freige.training.merge_shards \
      --shard_dir ./outputs \
      --output ./outputs
"""
import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard_dir", type=str, required=True,
                        help="包含 shard_0..shard_N 子目录 + 可选 top-level generations.jsonl 的目录")
    parser.add_argument("--output", type=str, required=True,
                        help="合并后的输出文件路径")
    args = parser.parse_args()

    shard_dir = Path(args.shard_dir)
    output_path = Path(args.output)

    sources = []

    # top-level generations.jsonl (早期单卡运行的输出)
    top_level = shard_dir / "generations.jsonl"
    if top_level.exists() and str(output_path.resolve()) != str(top_level.resolve()):
        sources.append(top_level)

    # shard 子目录 (按编号排序)
    shard_dirs = sorted(shard_dir.glob("shard_*"))
    for sd in shard_dirs:
        gen_file = sd / "generations.jsonl"
        if gen_file.exists():
            sources.append(gen_file)

    print(f"Found {len(sources)} source files:")

    # last-wins: shard 版本覆盖 root 版本
    seen = {}  # key: (doc_id, generation_idx) -> line
    overwritten = 0

    for src in sources:
        n = 0
        src_overwritten = 0
        for line in open(src):
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            key = (rec["doc_id"], rec["generation_idx"])
            if key in seen:
                src_overwritten += 1
                overwritten += 1
            seen[key] = line
            n += 1
        extra = f" ({src_overwritten} overwriting earlier)" if src_overwritten else ""
        print(f"  {src}: {n} records{extra}")

    total_lines = len(seen)
    with open(output_path, "w") as fout:
        for line in seen.values():
            fout.write(line + "\n")

    unique_docs = len(set(k[0] for k in seen))
    print(f"\nMerged: {total_lines} records, {unique_docs} unique docs")
    if overwritten:
        print(f"{overwritten} records overwritten by shard version")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()
