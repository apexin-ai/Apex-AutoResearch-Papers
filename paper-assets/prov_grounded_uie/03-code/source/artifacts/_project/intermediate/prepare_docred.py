"""
DocRED → evidence-co-prediction SFT 格式转换脚本

输入: DocRED 原始 JSON (train_annotated.json.gz, dev.json.gz, rel_info.json.gz)
      从 HuggingFace thunlp/docred 数据集仓库下载

输出: JSONL 文件 (train.jsonl, dev.jsonl)，每行格式:
      {"input": "Document: ...\nSchema: ...\nTask: ...",
       "output": "{\"relations\": [...]}",
       "meta": {"doc_id": ..., "num_relations": ..., "num_evidence_sents": ...}}

依赖: Python 3.10+, 无额外库依赖 (仅 stdlib)

用法: python prepare_docred.py --output_dir ./docred_processed/ [--stats] [--raw_dir ./docred_raw/data/]
"""

import argparse
import gzip
import json
import os
import sys
from collections import Counter
from pathlib import Path


def load_gz_json(path: str):
    with gzip.open(path, "rt", encoding="utf-8") as f:
        return json.load(f)


def build_document_text(sents: list[list[str]]) -> str:
    """将 DocRED 的 token 列表列表转为带句子标记的文本。"""
    parts = []
    for i, tokens in enumerate(sents):
        parts.append(f"[S{i}] " + " ".join(tokens))
    return " ".join(parts)


def get_entity_canonical(vertex: list[dict]) -> tuple[str, str]:
    """从 entity 的多个 mention 中取第一个的 name 和 type。"""
    first = vertex[0]
    return first["name"], first["type"]


def convert_document(doc: dict, rel_info: dict) -> dict | None:
    """将一个 DocRED 文档转为 SFT 训练格式。

    Returns None if the document has no annotated relations.
    """
    labels = doc.get("labels", [])
    if not labels:
        return None

    vertex_set = doc["vertexSet"]
    sents = doc["sents"]

    doc_text = build_document_text(sents)

    relation_types_in_doc = sorted(set(
        rel_info.get(lab["r"], lab["r"]) for lab in labels
    ))
    schema_str = ", ".join(relation_types_in_doc)

    input_text = (
        f"Document: {doc_text}\n"
        f"Schema: [{schema_str}]\n"
        f"Task: Extract all relation triplets with supporting evidence sentences."
    )

    relations = []
    evidence_sent_ids = set()
    for lab in labels:
        h_name, h_type = get_entity_canonical(vertex_set[lab["h"]])
        t_name, t_type = get_entity_canonical(vertex_set[lab["t"]])
        rel_name = rel_info.get(lab["r"], lab["r"])
        ev = [f"S{sid}" for sid in lab["evidence"]]
        evidence_sent_ids.update(lab["evidence"])

        relations.append({
            "head": {"name": h_name, "type": h_type},
            "tail": {"name": t_name, "type": t_type},
            "relation": rel_name,
            "evidence": ev,
        })

    output_obj = {"relations": relations}
    output_text = json.dumps(output_obj, ensure_ascii=False)

    meta = {
        "doc_id": doc.get("title", ""),
        "num_relations": len(relations),
        "num_evidence_sents": len(evidence_sent_ids),
        "num_sents": len(sents),
        "num_tokens": sum(len(s) for s in sents),
    }

    return {"input": input_text, "output": output_text, "meta": meta}


def process_split(docs: list[dict], rel_info: dict, output_path: str) -> list[dict]:
    """处理一个 split 的全部文档，写 JSONL，返回 meta 列表。"""
    metas = []
    with open(output_path, "w", encoding="utf-8") as f:
        for doc in docs:
            result = convert_document(doc, rel_info)
            if result is None:
                continue
            f.write(json.dumps(result, ensure_ascii=False) + "\n")
            metas.append(result["meta"])
    return metas


def compute_stats(metas: list[dict], split_name: str, all_jsonl_path: str) -> dict:
    """计算并返回统计信息。"""
    if not metas:
        return {"split": split_name, "num_docs": 0}

    num_docs = len(metas)
    num_rels = [m["num_relations"] for m in metas]
    num_ev = [m["num_evidence_sents"] for m in metas]
    num_sents = [m["num_sents"] for m in metas]
    num_tokens = [m["num_tokens"] for m in metas]

    # Per-relation evidence count
    per_rel_ev_counts = []
    with open(all_jsonl_path, "r") as f:
        for line in f:
            obj = json.loads(line)
            output = json.loads(obj["output"])
            for rel in output["relations"]:
                per_rel_ev_counts.append(len(rel["evidence"]))

    rel_type_counter = Counter()
    with open(all_jsonl_path, "r") as f:
        for line in f:
            obj = json.loads(line)
            output = json.loads(obj["output"])
            for rel in output["relations"]:
                rel_type_counter[rel["relation"]] += 1

    sorted_ev = sorted(per_rel_ev_counts)
    mid = len(sorted_ev) // 2
    median_ev = sorted_ev[mid] if sorted_ev else 0

    return {
        "split": split_name,
        "num_docs": num_docs,
        "total_relations": sum(num_rels),
        "avg_relations_per_doc": round(sum(num_rels) / num_docs, 2),
        "evidence_per_relation": {
            "mean": round(sum(per_rel_ev_counts) / max(len(per_rel_ev_counts), 1), 2),
            "median": median_ev,
            "max": max(per_rel_ev_counts) if per_rel_ev_counts else 0,
        },
        "sents_per_doc": {
            "mean": round(sum(num_sents) / num_docs, 2),
            "median": sorted(num_sents)[num_docs // 2],
            "max": max(num_sents),
        },
        "tokens_per_doc": {
            "mean": round(sum(num_tokens) / num_docs, 2),
            "median": sorted(num_tokens)[num_docs // 2],
            "max": max(num_tokens),
        },
        "top20_relation_types": rel_type_counter.most_common(20),
    }


def print_stats(stats: dict):
    s = stats
    print(f"\n{'='*60}")
    print(f"  Split: {s['split']}  |  Documents: {s['num_docs']}")
    print(f"{'='*60}")
    if s["num_docs"] == 0:
        print("  (no data)\n")
        return
    print(f"  Total relations:         {s['total_relations']}")
    print(f"  Avg relations/doc:       {s['avg_relations_per_doc']}")
    print(f"  Evidence sents/relation: mean={s['evidence_per_relation']['mean']}, "
          f"median={s['evidence_per_relation']['median']}, "
          f"max={s['evidence_per_relation']['max']}")
    print(f"  Sents/doc:               mean={s['sents_per_doc']['mean']}, "
          f"median={s['sents_per_doc']['median']}, "
          f"max={s['sents_per_doc']['max']}")
    print(f"  Tokens/doc:              mean={s['tokens_per_doc']['mean']}, "
          f"median={s['tokens_per_doc']['median']}, "
          f"max={s['tokens_per_doc']['max']}")
    print(f"\n  Top 20 relation types:")
    for rel, cnt in s["top20_relation_types"]:
        print(f"    {cnt:>5d}  {rel}")
    print()


def write_stats_markdown(all_stats: list[dict], output_path: str):
    with open(output_path, "w") as f:
        f.write("# DocRED Dataset Statistics (Evidence-Co-Prediction Format)\n\n")
        for s in all_stats:
            f.write(f"## {s['split']}\n\n")
            if s["num_docs"] == 0:
                f.write("No annotated data.\n\n")
                continue
            f.write(f"| Metric | Value |\n|--------|-------|\n")
            f.write(f"| Documents | {s['num_docs']} |\n")
            f.write(f"| Total relations | {s['total_relations']} |\n")
            f.write(f"| Avg relations/doc | {s['avg_relations_per_doc']} |\n")
            ev = s["evidence_per_relation"]
            f.write(f"| Evidence sents/relation (mean/median/max) | {ev['mean']} / {ev['median']} / {ev['max']} |\n")
            sd = s["sents_per_doc"]
            f.write(f"| Sents/doc (mean/median/max) | {sd['mean']} / {sd['median']} / {sd['max']} |\n")
            td = s["tokens_per_doc"]
            f.write(f"| Tokens/doc (mean/median/max) | {td['mean']} / {td['median']} / {td['max']} |\n")
            f.write(f"\n### Top 20 Relation Types\n\n")
            f.write(f"| Relation | Count |\n|----------|-------|\n")
            for rel, cnt in s["top20_relation_types"]:
                f.write(f"| {rel} | {cnt} |\n")
            f.write("\n")


def print_samples(jsonl_path: str, n: int = 3):
    print(f"\n{'='*60}")
    print(f"  Sample outputs from {os.path.basename(jsonl_path)}")
    print(f"{'='*60}")
    with open(jsonl_path, "r") as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            obj = json.loads(line)
            print(f"\n--- Sample {i+1} (doc_id={obj['meta']['doc_id']}) ---")
            # Truncate input for display
            inp = obj["input"]
            if len(inp) > 300:
                inp = inp[:300] + "..."
            print(f"INPUT: {inp}")
            output = json.loads(obj["output"])
            print(f"OUTPUT: {len(output['relations'])} relations")
            for r in output["relations"][:3]:
                print(f"  ({r['head']['name']}, {r['relation']}, {r['tail']['name']}) <- [{', '.join(r['evidence'])}]")
            if len(output["relations"]) > 3:
                print(f"  ... and {len(output['relations'])-3} more")
            print(f"META: {json.dumps(obj['meta'])}")


def main():
    parser = argparse.ArgumentParser(description="Convert DocRED to evidence-co-prediction SFT format")
    parser.add_argument("--raw_dir", default="./docred_raw/data/",
                        help="Directory containing DocRED .json.gz files")
    parser.add_argument("--output_dir", default="./docred_processed/",
                        help="Output directory for JSONL files")
    parser.add_argument("--stats", action="store_true",
                        help="Print statistics after processing")
    parser.add_argument("--stats_output", default=None,
                        help="Path to write stats markdown (default: <output_dir>/../docred_stats.md)")
    args = parser.parse_args()

    raw_dir = Path(args.raw_dir)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    print("Loading rel_info...")
    rel_info = load_gz_json(raw_dir / "rel_info.json.gz")
    print(f"  {len(rel_info)} relation types")

    all_stats = []

    # Train (annotated)
    print("Loading train_annotated...")
    train_docs = load_gz_json(raw_dir / "train_annotated.json.gz")
    print(f"  {len(train_docs)} documents")
    train_path = str(output_dir / "train.jsonl")
    train_metas = process_split(train_docs, rel_info, train_path)
    print(f"  Written {len(train_metas)} examples to {train_path}")

    # Dev
    print("Loading dev...")
    dev_docs = load_gz_json(raw_dir / "dev.json.gz")
    print(f"  {len(dev_docs)} documents")
    dev_path = str(output_dir / "dev.jsonl")
    dev_metas = process_split(dev_docs, rel_info, dev_path)
    print(f"  Written {len(dev_metas)} examples to {dev_path}")

    # Test (no labels — skip conversion, just note it)
    print("Loading test...")
    test_docs = load_gz_json(raw_dir / "test.json.gz")
    print(f"  {len(test_docs)} documents (no labels — skipped)")

    if args.stats:
        train_stats = compute_stats(train_metas, "train", train_path)
        dev_stats = compute_stats(dev_metas, "dev", dev_path)
        all_stats = [train_stats, dev_stats]

        print_stats(train_stats)
        print_stats(dev_stats)

        stats_path = args.stats_output or str(output_dir.parent / "docred_stats.md")
        write_stats_markdown(all_stats, stats_path)
        print(f"Stats written to {stats_path}")

    # Print samples
    print_samples(train_path, n=3)


if __name__ == "__main__":
    main()
