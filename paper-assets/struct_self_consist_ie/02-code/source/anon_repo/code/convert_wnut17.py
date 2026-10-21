"""Convert WNUT-17 CoNLL NER data to UIE char-offset JSON format.

Input: Raw CoNLL files from emerging_entities_17 repo
Output: {train,dev,test}.json in UIE format + llmfactory_train.json in sharegpt format

Entity types: corporation, creative-work, group, location, person, product
"""

import json
import os
import sys
from collections import Counter

RAW_DIR = "/root/autodl-tmp/.hf_cache/wnut17_raw"
DATA_DIR = "/root/autodl-tmp/struct_self_consist_ie/data/wnut17"

VALID_TYPES = {"corporation", "creative-work", "group", "location", "person", "product"}

WNUT17_SCHEMA_HINT = (
    "Entity types: corporation, creative-work, group, location, person, product"
)

PROMPT_TEMPLATE = (
    "Extract all structured information (entities and relations) from the "
    "following text. Output a JSON object.\n\n"
    "Text: {text}\n"
    "{schema_hint}\n\n"
    'Output format: {{"entities": [...], "relations": [...], "events": []}}\n'
    "For relations, head is the subject entity and tail is the object entity."
)


def read_conll(path):
    """Read CoNLL file, return list of (tokens, tags) per sentence."""
    sentences = []
    tokens, tags = [], []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.isspace():
                if tokens:
                    sentences.append((tokens, tags))
                    tokens, tags = [], []
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                tokens.append(parts[0])
                tags.append(parts[1])
    if tokens:
        sentences.append((tokens, tags))
    return sentences


def bio_to_spans(tags):
    """Extract (type, start_tok, end_tok_exclusive) spans from BIO tags."""
    spans = []
    cur_type, cur_start = None, None

    for i, tag in enumerate(tags):
        if tag.startswith("B-"):
            if cur_type is not None:
                spans.append((cur_type, cur_start, i))
            cur_type = tag[2:]
            cur_start = i
        elif tag.startswith("I-"):
            etype = tag[2:]
            if cur_type != etype:
                if cur_type is not None:
                    spans.append((cur_type, cur_start, i))
                cur_type = etype
                cur_start = i
        else:
            if cur_type is not None:
                spans.append((cur_type, cur_start, i))
                cur_type, cur_start = None, None

    if cur_type is not None:
        spans.append((cur_type, cur_start, len(tags)))

    return [(t, s, e) for t, s, e in spans if t in VALID_TYPES]


def convert_sentence(tokens, tags, idx, split):
    """Convert one sentence to UIE format."""
    text = " ".join(tokens)

    # Build token -> char offset mapping
    char_offsets = []
    pos = 0
    for tok in tokens:
        char_offsets.append((pos, pos + len(tok)))
        pos += len(tok) + 1

    spans = bio_to_spans(tags)
    entities = []
    for etype, tok_s, tok_e in spans:
        char_s = char_offsets[tok_s][0]
        char_e = char_offsets[tok_e - 1][1]
        entity_text = text[char_s:char_e]
        assert text[char_s:char_e] == entity_text
        entities.append({
            "text": entity_text,
            "type": etype,
            "start": char_s,
            "end": char_e,
        })

    return {
        "id": f"wnut17_{split}_{idx:05d}",
        "text": text,
        "entities": entities,
        "relations": [],
        "events": [],
    }


def convert_split(path, split):
    sentences = read_conll(path)
    return [convert_sentence(toks, tags, i, split) for i, (toks, tags) in enumerate(sentences)]


def make_sharegpt(instances):
    records = []
    for inst in instances:
        human_msg = PROMPT_TEMPLATE.format(text=inst["text"], schema_hint=WNUT17_SCHEMA_HINT)
        output = {"entities": inst["entities"], "relations": [], "events": []}
        records.append({
            "conversations": [
                {"from": "human", "value": human_msg},
                {"from": "gpt", "value": json.dumps(output, ensure_ascii=False)},
            ]
        })
    return records


def print_stats(instances, split):
    tc = Counter()
    for inst in instances:
        for e in inst["entities"]:
            tc[e["type"]] += 1
    total = sum(tc.values())
    print(f"\n[{split}] {len(instances)} instances, {total} entities")
    for t, c in sorted(tc.items(), key=lambda x: -x[1]):
        print(f"  {t}: {c}")


def validate(instances, split, n=10):
    errors = 0
    for inst in instances:
        for e in inst["entities"]:
            if inst["text"][e["start"]:e["end"]] != e["text"]:
                errors += 1
                print(f"  OFFSET ERROR {inst['id']}: expected '{e['text']}', got '{inst['text'][e['start']:e['end']]}'")
            if not e["text"]:
                errors += 1
                print(f"  EMPTY ENTITY {inst['id']}")

    shown = 0
    for inst in instances:
        if inst["entities"] and shown < n:
            print(f"\n  [{inst['id']}] {inst['text'][:100]}{'...' if len(inst['text']) > 100 else ''}")
            for e in inst["entities"]:
                ok = inst["text"][e["start"]:e["end"]] == e["text"]
                print(f"    {'OK' if ok else 'FAIL'} {e['type']}: '{e['text']}' ({e['start']}:{e['end']})")
            shown += 1

    total = sum(len(inst["entities"]) for inst in instances)
    print(f"\n  Validated {total} entities in {split}, {errors} errors")
    return errors


def main():
    os.makedirs(DATA_DIR, exist_ok=True)

    files = {"train": "train.conll", "dev": "dev.conll", "test": "test.conll"}
    all_data = {}

    for split, fname in files.items():
        path = os.path.join(RAW_DIR, fname)
        instances = convert_split(path, split)
        all_data[split] = instances

        out = os.path.join(DATA_DIR, f"{split}.json")
        with open(out, "w", encoding="utf-8") as f:
            json.dump(instances, f, ensure_ascii=False, indent=2)
        print(f"Saved {len(instances)} -> {out}")
        print_stats(instances, split)

    # Validate
    print("\n" + "=" * 50)
    print("Validation (test set, 10 samples with entities):")
    errors = validate(all_data["test"], "test", n=10)

    # Sharegpt
    sharegpt = make_sharegpt(all_data["train"])
    sp = os.path.join(DATA_DIR, "llmfactory_train.json")
    with open(sp, "w", encoding="utf-8") as f:
        json.dump(sharegpt, f, ensure_ascii=False, indent=2)
    print(f"\nSaved {len(sharegpt)} sharegpt instances -> {sp}")

    # First 3 test instances
    print("\n" + "=" * 50)
    print("First 3 test instances:")
    for inst in all_data["test"][:3]:
        print(json.dumps(inst, ensure_ascii=False, indent=2))

    if errors:
        print(f"\nFAILED: {errors} errors")
        sys.exit(1)
    print("\nAll validations passed.")


if __name__ == "__main__":
    main()
