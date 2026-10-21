"""Extract binary ack classifier training data from full_scale annotations + traces.

Joins dual-annotator annotations (annotations.jsonl) with conversation traces
(traces.jsonl) to produce text + binary label pairs. Uses annotation_a as the
primary label. Splits by task_id hash into train/val/test.

Input:
    outputs/full_scale/{backbone}_round_robin/annotations/annotations.jsonl
    outputs/full_scale/{backbone}_round_robin/traces/traces.jsonl
    (optional) outputs/{domain}/{backbone}_round_robin/annotations/annotations.jsonl

Output:
    data/classifier/train.jsonl
    data/classifier/val.jsonl
    data/classifier/test.jsonl
    data/classifier/metadata.json
"""
import argparse
import hashlib
import json
import logging
import os
import sys
from collections import Counter, defaultdict
from typing import Dict, List, Optional, Tuple

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
log = logging.getLogger(__name__)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUTS_DIR = os.path.join(PROJECT_ROOT, "outputs")
OUT_DIR = os.path.join(PROJECT_ROOT, "data", "classifier")

BACKBONES = ["llama", "qwen", "gemma"]
TOPOLOGIES = ["round_robin"]
DOMAINS_EXTRA = ["stratqa", "arc", "math"]

ACK_LABEL = "acknowledgment"


def task_id_split_bucket(task_id: str, n_buckets: int = 10) -> int:
    h = hashlib.md5(task_id.encode()).hexdigest()
    return int(h, 16) % n_buckets


def load_traces(traces_path: str) -> Dict[str, dict]:
    trace_map = {}
    with open(traces_path) as f:
        for i, line in enumerate(f):
            line = line.strip()
            if not line:
                continue
            try:
                t = json.loads(line)
            except json.JSONDecodeError:
                log.debug("Skipping malformed JSON at %s:%d", traces_path, i)
                continue
            trace_map[t["task_id"]] = t
    return trace_map


def load_annotations(ann_path: str) -> List[dict]:
    records = []
    with open(ann_path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records


def get_label(rec: dict) -> str:
    if "annotation_a" in rec:
        return rec["annotation_a"].get("type", "unknown")
    if "annotation" in rec:
        return rec["annotation"].get("type", "unknown")
    return "unknown"


def extract_full_text_records(backbone: str, domain: str = "gsm8k") -> List[dict]:
    """Extract records from full_scale round_robin where traces provide full text."""
    ann_path = os.path.join(
        OUTPUTS_DIR, "full_scale", f"{backbone}_round_robin",
        "annotations", "annotations.jsonl"
    )
    traces_path = os.path.join(
        OUTPUTS_DIR, "full_scale", f"{backbone}_round_robin",
        "traces", "traces.jsonl"
    )

    if not os.path.exists(ann_path) or not os.path.exists(traces_path):
        log.warning("Missing files for %s: ann=%s traces=%s",
                     backbone, os.path.exists(ann_path), os.path.exists(traces_path))
        return []

    trace_map = load_traces(traces_path)
    annotations = load_annotations(ann_path)
    records = []

    for ann in annotations:
        task_id = ann["task_id"]
        msg_idx = ann["message_index"]
        label_str = get_label(ann)

        if task_id not in trace_map:
            continue

        messages = trace_map[task_id].get("messages", [])
        target_round = msg_idx + 1
        text = None
        prev_text = ""
        for msg in messages:
            if msg["round"] == target_round:
                text = msg["content"]
            if msg["round"] == target_round - 1:
                prev_text = msg["content"]

        if text is None:
            continue

        records.append({
            "text": text,
            "prev_text": prev_text,
            "label": 1 if label_str == ACK_LABEL else 0,
            "label_5class": label_str,
            "backbone": backbone,
            "domain": domain,
            "task_id": task_id,
            "message_index": msg_idx,
            "sender": ann.get("sender", ""),
        })

    log.info("  %s round_robin: %d records extracted", backbone, len(records))
    return records


def extract_preview_records(domain: str, backbone: str) -> List[dict]:
    """Extract records from domains without traces, using content_preview.

    Only includes records where content_preview is NOT truncated (< 100 chars).
    """
    ann_path = os.path.join(
        OUTPUTS_DIR, domain, f"{backbone}_round_robin",
        "annotations", "annotations.jsonl"
    )
    if not os.path.exists(ann_path):
        return []

    annotations = load_annotations(ann_path)
    records = []

    for ann in annotations:
        preview = ann.get("content_preview", "")
        if len(preview) >= 100:
            continue

        label_str = get_label(ann)
        records.append({
            "text": preview,
            "prev_text": "",
            "label": 1 if label_str == ACK_LABEL else 0,
            "label_5class": label_str,
            "backbone": backbone,
            "domain": domain.replace("stratqa", "strategyqa"),
            "task_id": ann["task_id"],
            "message_index": ann["message_index"],
            "sender": ann.get("sender", ""),
        })

    log.info("  %s/%s preview (non-truncated): %d records", domain, backbone, len(records))
    return records


def deduplicate(records: List[dict]) -> List[dict]:
    """Remove duplicates by (task_id, message_index, backbone)."""
    seen = set()
    deduped = []
    for rec in records:
        key = (rec["task_id"], rec["message_index"], rec["backbone"])
        if key not in seen:
            seen.add(key)
            deduped.append(rec)
    return deduped


def split_records(
    records: List[dict],
    train_buckets: Tuple[int, ...] = (0, 1, 2, 3, 4, 5, 6),
    val_buckets: Tuple[int, ...] = (7, 8),
    test_buckets: Tuple[int, ...] = (9,),
) -> Tuple[List[dict], List[dict], List[dict]]:
    train, val, test = [], [], []
    for rec in records:
        bucket = task_id_split_bucket(rec["task_id"])
        if bucket in train_buckets:
            train.append(rec)
        elif bucket in val_buckets:
            val.append(rec)
        elif bucket in test_buckets:
            test.append(rec)
    return train, val, test


def write_jsonl(records: List[dict], path: str) -> None:
    with open(path, "w") as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + "\n")


def compute_metadata(
    train: List[dict], val: List[dict], test: List[dict]
) -> dict:
    def split_stats(records: List[dict], name: str) -> dict:
        label_counts = Counter(r["label"] for r in records)
        backbone_counts = Counter(r["backbone"] for r in records)
        domain_counts = Counter(r["domain"] for r in records)
        label_5class = Counter(r["label_5class"] for r in records)
        return {
            "name": name,
            "total": len(records),
            "ack": label_counts.get(1, 0),
            "non_ack": label_counts.get(0, 0),
            "ack_ratio": round(label_counts.get(1, 0) / max(len(records), 1), 4),
            "per_backbone": dict(backbone_counts),
            "per_domain": dict(domain_counts),
            "per_5class": dict(label_5class.most_common()),
        }

    return {
        "total_records": len(train) + len(val) + len(test),
        "split_ratio": "70/20/10 by task_id hash",
        "label_mapping": {"acknowledgment": 1, "other": 0},
        "train": split_stats(train, "train"),
        "val": split_stats(val, "val"),
        "test": split_stats(test, "test"),
    }


def main():
    parser = argparse.ArgumentParser(
        description="Extract binary ack classifier data from annotations + traces."
    )
    parser.add_argument(
        "--include-preview", action="store_true",
        help="Include non-truncated content_preview records from stratqa/arc/math."
    )
    parser.add_argument(
        "--output-dir", default=OUT_DIR,
        help="Output directory (default: data/classifier/)."
    )
    args = parser.parse_args()

    os.makedirs(args.output_dir, exist_ok=True)
    all_records = []

    log.info("Extracting full-text records from full_scale round_robin traces...")
    for backbone in BACKBONES:
        recs = extract_full_text_records(backbone, domain="gsm8k")
        all_records.extend(recs)

    if args.include_preview:
        log.info("Extracting non-truncated preview records from extra domains...")
        for domain in DOMAINS_EXTRA:
            for backbone in BACKBONES:
                recs = extract_preview_records(domain, backbone)
                all_records.extend(recs)

    all_records = deduplicate(all_records)
    log.info("Total after dedup: %d records", len(all_records))

    label_dist = Counter(r["label"] for r in all_records)
    log.info("Label distribution: ack=%d, non_ack=%d (%.1f%% ack)",
             label_dist[1], label_dist[0],
             100 * label_dist[1] / max(len(all_records), 1))

    train, val, test = split_records(all_records)
    log.info("Split: train=%d, val=%d, test=%d", len(train), len(val), len(test))

    train_path = os.path.join(args.output_dir, "train.jsonl")
    val_path = os.path.join(args.output_dir, "val.jsonl")
    test_path = os.path.join(args.output_dir, "test.jsonl")
    meta_path = os.path.join(args.output_dir, "metadata.json")

    write_jsonl(train, train_path)
    write_jsonl(val, val_path)
    write_jsonl(test, test_path)

    metadata = compute_metadata(train, val, test)
    with open(meta_path, "w") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)

    log.info("Written: %s, %s, %s, %s", train_path, val_path, test_path, meta_path)


if __name__ == "__main__":
    main()
