#!/usr/bin/env python3
"""Prepare DocRED data for Relation Extraction SC experiments.

DocRED is document-level RE: each document has multiple sentences, entity groups
(with coreference), and relation labels between entity groups.

Key adaptations from SciERC:
1. Document-level: flatten multi-sentence documents into single text
2. 96 relation types (vs SciERC's 7) — extracted from dataset at runtime
3. Entity groups with coreference: use first mention as representative
4. Use validation split (test has no labels)

Usage:
    python prepare_docred_data.py \
        --output /root/autodl-tmp/struct_self_consist_ie/data/docred_re_instances.jsonl \
        --n-instances 200 \
        --seed 42
"""

import argparse
import json
import os
import random
import sys

_project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, _project_root)
sys.path.insert(0, os.path.join(_project_root, "code"))

DOCRED_ENTITY_TYPES = ["PER", "ORG", "LOC", "TIME", "NUM", "MISC"]


def flatten_sents(sents: list[list[str]]) -> tuple[str, list[list[tuple[int, int]]]]:
    """Flatten list of word lists into single text with character offset tracking.

    Returns:
        text: The flattened document text.
        word_offsets: word_offsets[sent_i][word_j] = (char_start, char_end).
    """
    text = ""
    word_offsets: list[list[tuple[int, int]]] = []

    for sent_i, sent in enumerate(sents):
        if sent_i > 0:
            text += " "
        word_off: list[tuple[int, int]] = []
        for word_j, word in enumerate(sent):
            if word_j > 0:
                text += " "
            start = len(text)
            text += word
            end = len(text)
            word_off.append((start, end))
        word_offsets.append(word_off)

    return text, word_offsets


def mention_to_char_span(
    mention: dict,
    word_offsets: list[list[tuple[int, int]]],
) -> tuple[int, int] | None:
    """Convert a DocRED mention (sent_id, pos) to character offsets."""
    sent_id = mention["sent_id"]
    pos = mention["pos"]  # [start_word, end_word) within sentence

    if sent_id >= len(word_offsets):
        return None
    sent_woffs = word_offsets[sent_id]
    if pos[0] >= len(sent_woffs) or pos[1] > len(sent_woffs):
        return None
    if pos[0] >= pos[1]:
        return None

    char_start = sent_woffs[pos[0]][0]
    char_end = sent_woffs[pos[1] - 1][1]
    return (char_start, char_end)


def convert_docred_document(
    doc: dict,
    doc_idx: int,
    rel_id_to_name: dict[str, str] | None = None,
) -> dict | None:
    """Convert a DocRED document to UIE Instance format.

    Uses first mention of each entity group as the representative.
    Returns None if the document has no labeled relations.
    """
    sents = doc["sents"]
    vertex_set = doc["vertexSet"]
    if rel_id_to_name is None:
        rel_id_to_name = {}

    # Handle both raw format (list of dicts) and HF columnar format
    labels_raw = doc.get("labels", {})
    if isinstance(labels_raw, dict):
        n_labels = len(labels_raw.get("head", []))
        labels = []
        for i in range(n_labels):
            rel_id = labels_raw.get("relation_id", labels_raw.get("r", []))[i]
            labels.append({
                "h": labels_raw["head"][i] if "head" in labels_raw else labels_raw["h"][i],
                "t": labels_raw["tail"][i] if "tail" in labels_raw else labels_raw["t"][i],
                "r": rel_id,
            })
    elif isinstance(labels_raw, list):
        labels = labels_raw
    else:
        return None

    if not labels:
        return None

    text, word_offsets = flatten_sents(sents)

    entity_spans: list[tuple[int, int] | None] = []
    entity_names: list[str] = []
    entity_types: list[str] = []
    entities_uie: list[dict] = []

    for ent_group in vertex_set:
        if not ent_group:
            entity_spans.append(None)
            entity_names.append("")
            entity_types.append("MISC")
            continue

        best_mention = None
        best_span = None
        for m in ent_group:
            span = mention_to_char_span(m, word_offsets)
            if span is not None:
                best_mention = m
                best_span = span
                break

        if best_mention is None or best_span is None:
            entity_spans.append(None)
            entity_names.append(ent_group[0].get("name", ""))
            entity_types.append(ent_group[0].get("type", "MISC"))
            continue

        entity_spans.append(best_span)
        entity_names.append(best_mention["name"])
        entity_types.append(best_mention.get("type", "MISC"))
        entities_uie.append({
            "text": best_mention["name"],
            "type": best_mention.get("type", "MISC"),
            "start": best_span[0],
            "end": best_span[1],
        })

    relations_uie: list[dict] = []
    seen_rel_keys: set[tuple] = set()

    for label in labels:
        h_idx = label["h"]
        t_idx = label["t"]
        rel_id = label["r"]
        rel_text = rel_id_to_name.get(rel_id, rel_id)

        if h_idx >= len(entity_spans) or t_idx >= len(entity_spans):
            continue
        h_span = entity_spans[h_idx]
        t_span = entity_spans[t_idx]
        if h_span is None or t_span is None:
            continue

        rel_key = (h_span[0], h_span[1], t_span[0], t_span[1], rel_text)
        if rel_key in seen_rel_keys:
            continue
        seen_rel_keys.add(rel_key)

        relations_uie.append({
            "head": entity_names[h_idx],
            "tail": entity_names[t_idx],
            "type": rel_text,
            "head_start": h_span[0],
            "head_end": h_span[1],
            "tail_start": t_span[0],
            "tail_end": t_span[1],
        })

    if not relations_uie:
        return None

    title = doc.get("title", f"doc_{doc_idx}")

    return {
        "id": f"docred_val_{doc_idx}",
        "title": title,
        "text": text,
        "entities": entities_uie,
        "relations": relations_uie,
        "events": [],
    }


def extract_relation_types(docs: list[dict]) -> list[str]:
    """Extract all unique relation type names from converted documents."""
    types: set[str] = set()
    for doc in docs:
        for rel in doc.get("relations", []):
            types.add(rel["type"])
    return sorted(types)


def build_schema_hint(relation_types: list[str]) -> str:
    """Build DocRED schema hint string."""
    ent_line = f"Entity types: {', '.join(DOCRED_ENTITY_TYPES)}"
    rel_line = f"Relation types: {', '.join(relation_types)}"
    return f"{ent_line}\n{rel_line}"


def main():
    parser = argparse.ArgumentParser(description="Prepare DocRED RE data for SC experiments")
    parser.add_argument("--output", required=True, help="Output JSONL path")
    parser.add_argument("--schema-output", default=None, help="Output path for schema hint JSON")
    parser.add_argument("--n-instances", type=int, default=200, help="Number of instances to sample")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--min-relations", type=int, default=1)
    parser.add_argument("--max-text-length", type=int, default=3000,
                        help="Max text char length (skip very long documents)")
    parser.add_argument("--stats", action="store_true", help="Print dataset statistics")
    parser.add_argument("--local-data", default=None, help="Path to local DocRED JSON file")
    parser.add_argument("--rel-info", default=None,
                        help="Path to rel_info.json (Wikidata ID -> human-readable name)")
    args = parser.parse_args()

    # Load relation ID -> name mapping
    rel_id_to_name: dict[str, str] = {}
    if args.rel_info and os.path.exists(args.rel_info):
        with open(args.rel_info, "r") as f:
            rel_id_to_name = json.load(f)
        print(f"Loaded {len(rel_id_to_name)} relation type names from {args.rel_info}")

    print("Loading DocRED validation split...")
    if args.local_data:
        with open(args.local_data, "r") as f:
            raw_docs = json.load(f)
    else:
        from datasets import load_dataset
        ds = load_dataset("docred", split="validation")
        raw_docs = list(ds)

    print(f"  Raw documents: {len(raw_docs)}")

    converted: list[dict] = []
    skipped_no_rel = 0
    skipped_long = 0

    for i, doc in enumerate(raw_docs):
        inst = convert_docred_document(doc, i, rel_id_to_name=rel_id_to_name)
        if inst is None:
            skipped_no_rel += 1
            continue
        if len(inst["text"]) > args.max_text_length:
            skipped_long += 1
            continue
        if len(inst["relations"]) < args.min_relations:
            skipped_no_rel += 1
            continue
        converted.append(inst)

    print(f"  Converted: {len(converted)} (skipped: {skipped_no_rel} no-rel, {skipped_long} too-long)")

    rel_types = extract_relation_types(converted)
    schema_hint = build_schema_hint(rel_types)

    if args.stats:
        n_rels = sum(len(d["relations"]) for d in converted)
        n_ents = sum(len(d["entities"]) for d in converted)
        text_lens = [len(d["text"]) for d in converted]
        rels_per_doc = [len(d["relations"]) for d in converted]
        print(f"\n  Dataset statistics:")
        print(f"    Documents: {len(converted)}")
        print(f"    Total relations: {n_rels}")
        print(f"    Total entities: {n_ents}")
        print(f"    Unique relation types: {len(rel_types)}")
        print(f"    Text length: mean={sum(text_lens)/len(text_lens):.0f}, "
              f"min={min(text_lens)}, max={max(text_lens)}")
        print(f"    Relations/doc: mean={sum(rels_per_doc)/len(rels_per_doc):.1f}, "
              f"min={min(rels_per_doc)}, max={max(rels_per_doc)}")
        print(f"    Relation types: {rel_types[:10]}... ({len(rel_types)} total)")

    rng = random.Random(args.seed)
    if len(converted) > args.n_instances:
        sampled = rng.sample(converted, args.n_instances)
    else:
        sampled = converted
        print(f"  Warning: only {len(converted)} instances available, requested {args.n_instances}")

    sampled_rel_types = extract_relation_types(sampled)
    sampled_schema = build_schema_hint(sampled_rel_types)

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        for inst in sampled:
            f.write(json.dumps(inst, ensure_ascii=False) + "\n")

    print(f"\nWrote {len(sampled)} RE instances to {args.output}")
    print(f"  Relation types in sample: {len(sampled_rel_types)}")
    print(f"  Total gold relations: {sum(len(d['relations']) for d in sampled)}")

    if args.schema_output:
        os.makedirs(os.path.dirname(args.schema_output) or ".", exist_ok=True)
        with open(args.schema_output, "w") as f:
            json.dump({
                "entity_types": DOCRED_ENTITY_TYPES,
                "relation_types": sampled_rel_types,
                "schema_hint": sampled_schema,
            }, f, indent=2)
        print(f"  Schema hint saved to {args.schema_output}")


if __name__ == "__main__":
    main()
