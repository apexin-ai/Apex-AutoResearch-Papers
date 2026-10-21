#!/usr/bin/env python3
"""
ACE05 → parquet converter for schema-dag-extraction pipeline.

Reads ACE05 data in common preprocessed formats (DyGIE++ JSON or PURE JSON)
and converts to our internal parquet format:

  NER columns: text (str), entities (list[dict{text, type}])
  RE  columns: text (str), entities (list[dict{text, type}]),
               relations (list[dict{head:{text,type}, tail:{text,type}, type}])

Usage:
  # DyGIE++ format
  python preprocess_ace05.py --input data/ace05_dygie/test.json --format dygie \
      --output data/ace05/test.parquet --mode ner

  # PURE format
  python preprocess_ace05.py --input data/ace05_pure/test.json --format pure \
      --output data/ace05/test.parquet --mode re

  # Show help
  python preprocess_ace05.py --help

Input formats:

  DyGIE++ (https://github.com/dwadden/dygiepp):
    Each line is a JSON object with keys: doc_key, dataset, sentences, ner, relations.
    - sentences: list[list[str]]  (tokenized)
    - ner:       list[list[[start, end, type]]]  per-sentence entity spans
    - relations: list[list[[h_start, h_end, t_start, t_end, type]]]

  PURE (https://github.com/princeton-nlp/PURE):
    Each line is a JSON object with keys: doc_key, sentences, ner, relations.
    - sentences: list[list[str]]
    - ner:       list[list[[start, end, type]]]
    - relations: list[list[[subj_start, subj_end, obj_start, obj_end, relation, is_reverse]]]

Output: Parquet file loadable via datasets.load_dataset('parquet', data_files=...)
"""

import argparse
import json
import sys
from pathlib import Path

import pandas as pd

ACE05_ENTITY_TYPES = {"Person", "Organization", "GPE", "Location", "Facility", "Vehicle", "Weapon"}

ACE05_RELATION_SUBTYPES = {
    "ART:User-Owner-Inventor-Manufacturer",
    "GEN-AFF:Citizen-Resident-Religion-Ethnicity", "GEN-AFF:Org-Location",
    "ORG-AFF:Employment", "ORG-AFF:Founder", "ORG-AFF:Membership",
    "ORG-AFF:Ownership", "ORG-AFF:Sports-Affiliation", "ORG-AFF:Student-Alum",
    "ORG-AFF:Investor-Shareholder",
    "PART-WHOLE:Artifact", "PART-WHOLE:Geographical", "PART-WHOLE:Subsidiary",
    "PER-SOC:Business", "PER-SOC:Family", "PER-SOC:Lasting-Personal",
    "PHYS:Located", "PHYS:Near",
}


def _tokens_to_text(tokens):
    """Join tokens back into a string, preserving rough character offsets."""
    return " ".join(tokens)


def parse_dygie(input_path, mode):
    """Parse DyGIE++ JSON-lines format."""
    records = []
    with open(input_path) as f:
        for line in f:
            doc = json.loads(line.strip())
            sentences = doc["sentences"]
            ner_per_sent = doc.get("ner", [[] for _ in sentences])
            rel_per_sent = doc.get("relations", [[] for _ in sentences])

            flat_tokens = []
            sent_offsets = []
            for sent in sentences:
                sent_offsets.append(len(flat_tokens))
                flat_tokens.extend(sent)

            for sent_idx, sent in enumerate(sentences):
                offset = sent_offsets[sent_idx]
                sent_text = _tokens_to_text(sent)
                sent_tokens = sent

                entities = []
                ner_spans = ner_per_sent[sent_idx] if sent_idx < len(ner_per_sent) else []
                span_map = {}
                for span in ner_spans:
                    start, end, etype = span[0], span[1], span[2]
                    local_start = start - offset
                    local_end = end - offset
                    mention = " ".join(sent_tokens[local_start:local_end + 1])
                    entities.append({"text": mention, "type": etype})
                    span_map[(start, end)] = {"text": mention, "type": etype}

                record = {"text": sent_text, "entities": entities}

                if mode == "re":
                    relations = []
                    rel_spans = rel_per_sent[sent_idx] if sent_idx < len(rel_per_sent) else []
                    for rel in rel_spans:
                        h_start, h_end, t_start, t_end, rtype = rel[0], rel[1], rel[2], rel[3], rel[4]
                        head = span_map.get((h_start, h_end))
                        tail = span_map.get((t_start, t_end))
                        if head and tail:
                            relations.append({"head": head, "tail": tail, "type": rtype})
                    record["relations"] = relations

                records.append(record)

    return records


def parse_pure(input_path, mode):
    """Parse PURE JSON-lines format."""
    records = []
    with open(input_path) as f:
        for line in f:
            doc = json.loads(line.strip())
            sentences = doc["sentences"]
            ner_per_sent = doc.get("ner", [[] for _ in sentences])
            rel_per_sent = doc.get("relations", [[] for _ in sentences])

            flat_tokens = []
            sent_offsets = []
            for sent in sentences:
                sent_offsets.append(len(flat_tokens))
                flat_tokens.extend(sent)

            for sent_idx, sent in enumerate(sentences):
                offset = sent_offsets[sent_idx]
                sent_text = _tokens_to_text(sent)
                sent_tokens = sent

                entities = []
                ner_spans = ner_per_sent[sent_idx] if sent_idx < len(ner_per_sent) else []
                span_map = {}
                for span in ner_spans:
                    start, end, etype = span[0], span[1], span[2]
                    local_start = start - offset
                    local_end = end - offset
                    mention = " ".join(sent_tokens[local_start:local_end + 1])
                    entities.append({"text": mention, "type": etype})
                    span_map[(start, end)] = {"text": mention, "type": etype}

                record = {"text": sent_text, "entities": entities}

                if mode == "re":
                    relations = []
                    rel_spans = rel_per_sent[sent_idx] if sent_idx < len(rel_per_sent) else []
                    for rel in rel_spans:
                        subj_start, subj_end = rel[0], rel[1]
                        obj_start, obj_end = rel[2], rel[3]
                        rtype = rel[4]
                        head = span_map.get((subj_start, subj_end))
                        tail = span_map.get((obj_start, obj_end))
                        if head and tail:
                            relations.append({"head": head, "tail": tail, "type": rtype})
                    record["relations"] = relations

                records.append(record)

    return records


def validate_records(records, mode):
    """Validate entity and relation types against ACE05 schema."""
    unknown_entity_types = set()
    unknown_relation_types = set()
    for r in records:
        for e in r["entities"]:
            if e["type"] not in ACE05_ENTITY_TYPES:
                unknown_entity_types.add(e["type"])
        if mode == "re":
            for rel in r.get("relations", []):
                if rel["type"] not in ACE05_RELATION_SUBTYPES:
                    unknown_relation_types.add(rel["type"])

    if unknown_entity_types:
        print(f"WARNING: unknown entity types: {sorted(unknown_entity_types)}", file=sys.stderr)
    if unknown_relation_types:
        print(f"WARNING: unknown relation types: {sorted(unknown_relation_types)}", file=sys.stderr)

    return len(unknown_entity_types) == 0 and len(unknown_relation_types) == 0


def to_parquet(records, output_path):
    """Write records list to parquet."""
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df = pd.DataFrame(records)
    df.to_parquet(output_path, index=False)
    print(f"Wrote {len(df)} records to {output_path}")


def print_stats(records, mode):
    """Print dataset statistics."""
    n_entities = sum(len(r["entities"]) for r in records)
    entity_types = set()
    for r in records:
        for e in r["entities"]:
            entity_types.add(e["type"])

    print(f"Sentences: {len(records)}")
    print(f"Entities:  {n_entities} ({len(entity_types)} types)")

    if mode == "re":
        n_relations = sum(len(r.get("relations", [])) for r in records)
        rel_types = set()
        for r in records:
            for rel in r.get("relations", []):
                rel_types.add(rel["type"])
        print(f"Relations: {n_relations} ({len(rel_types)} types)")


def main():
    parser = argparse.ArgumentParser(
        description="Convert ACE05 preprocessed data to parquet format"
    )
    parser.add_argument("--input", required=True, help="Input JSON-lines file (DyGIE++ or PURE format)")
    parser.add_argument("--format", required=True, choices=["dygie", "pure"],
                        help="Input format: dygie (DyGIE++) or pure (PURE)")
    parser.add_argument("--output", required=True, help="Output parquet file path")
    parser.add_argument("--mode", default="ner", choices=["ner", "re"],
                        help="Extraction mode: ner (entities only) or re (entities + relations)")
    parser.add_argument("--stats", action="store_true", help="Print dataset statistics after conversion")
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"ERROR: input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    parsers = {"dygie": parse_dygie, "pure": parse_pure}
    records = parsers[args.format](args.input, args.mode)

    if not records:
        print("WARNING: no records parsed from input", file=sys.stderr)
        sys.exit(1)

    validate_records(records, args.mode)
    to_parquet(records, args.output)

    if args.stats:
        print_stats(records, args.mode)


if __name__ == "__main__":
    main()
