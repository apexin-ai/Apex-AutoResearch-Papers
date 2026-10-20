"""合并 4 个 shard 的 generation JSONL 到一个文件。

用法:
  cd /root/autodl-tmp && python -m freige.training.merge_shards \
      --shard_dir /root/autodl-tmp/rsft_generations \
      --output /root/autodl-tmp/rsft_generations/generations_merged.jsonl
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
    total_lines = 0
    seen_doc_ids = set()
    duplicates = 0

    with open(output_path, "w") as fout:
        for src in sources:
            n = 0
            for line in open(src):
                line = line.strip()
                if not line:
                    continue
                rec = json.loads(line)
                key = (rec["doc_id"], rec["generation_idx"])
                if key in seen_doc_ids:
                    duplicates += 1
                    continue
                seen_doc_ids.add(key)
                fout.write(line + "\n")
                n += 1
                total_lines += 1
            print(f"  {src}: {n} records")

    unique_docs = len(set(k[0] for k in seen_doc_ids))
    print(f"\nMerged: {total_lines} records, {unique_docs} unique docs")
    if duplicates:
        print(f"Skipped {duplicates} duplicates")
    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()
