"""Re-DocRED → DocRED 格式转换脚本。

Re-DocRED 与 DocRED 字段结构完全一致（title, vertexSet, labels, sents），
但有两个差异需要处理：
1. 文件名不同（train_revised.json vs train_annotated.json）
2. 约 55% 的 triples 的 evidence 字段为空列表（Re-DocRED 修正了 false negative
   但未为所有新增 triples 标注 evidence）

本脚本提供两种模式：
- full: 保留所有 triples，直接重命名输出（适合 RE 评估）
- evidence_only: 仅保留有 evidence 标注的 triples（适合 faith-evidence 项目）
"""

import argparse
import json
from pathlib import Path


def convert(src_dir: str, dst_dir: str, mode: str = "evidence_only"):
    src = Path(src_dir)
    dst = Path(dst_dir)
    dst.mkdir(parents=True, exist_ok=True)

    file_map = {
        "train_revised.json": "train_annotated.json",
        "dev_revised.json": "dev.json",
        "test_revised.json": "test.json",
    }

    stats = {}
    for src_name, dst_name in file_map.items():
        src_path = src / src_name
        if not src_path.exists():
            print(f"SKIP: {src_path} not found")
            continue

        with open(src_path) as f:
            data = json.load(f)

        total_triples = 0
        kept_triples = 0
        for doc in data:
            total_triples += len(doc.get("labels", []))
            if mode == "evidence_only":
                doc["labels"] = [
                    lbl for lbl in doc.get("labels", [])
                    if lbl.get("evidence")
                ]
            kept_triples += len(doc.get("labels", []))
            # Remove extra fields from vertexSet (optional cleanup)
            for entity in doc.get("vertexSet", []):
                for mention in entity:
                    mention.pop("global_pos", None)
                    mention.pop("index", None)

        dst_path = dst / dst_name
        with open(dst_path, "w") as f:
            json.dump(data, f, ensure_ascii=False)

        split = dst_name.replace(".json", "")
        stats[split] = {
            "docs": len(data),
            "total_triples": total_triples,
            "kept_triples": kept_triples,
        }
        print(f"{src_name} → {dst_name}: {len(data)} docs, "
              f"{kept_triples}/{total_triples} triples kept")

    # Write metadata
    meta = {"source": "Re-DocRED", "mode": mode, "stats": stats}
    with open(dst / "metadata.json", "w") as f:
        json.dump(meta, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Output: {dst}")
    print(f"Mode: {mode}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--src", default="./outputs")
    parser.add_argument("--dst", default="./outputs")
    parser.add_argument("--mode", choices=["full", "evidence_only"],
                        default="evidence_only",
                        help="full=keep all triples; evidence_only=filter out empty evidence")
    args = parser.parse_args()
    convert(args.src, args.dst, args.mode)
