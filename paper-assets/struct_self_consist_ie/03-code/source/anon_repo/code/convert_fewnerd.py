"""Convert Few-NERD SUPERVISED dataset to UIE char-offset JSON format.

Downloads from HuggingFace (DFKI-SLT/few-nerd, supervised config).
Uses coarse 8-type entity schema with flat (non-BIO) tags.
Consecutive tokens with the same non-O tag form a single entity span.

Entity types: art, building, event, location, organization, other, person, product
"""

import json
import os
import sys
from collections import Counter


DATA_DIR = "/root/autodl-tmp/struct_self_consist_ie/data/fewnerd"
HF_CACHE = "/root/autodl-tmp/.hf_cache"

SCHEMA_HINT = (
    "Entity types: person, organization, location, building, art, product, event, other"
)

PROMPT_TEMPLATE = (
    "Extract all structured information (entities and relations) from the "
    "following text. Output a JSON object.\n\n"
    "Text: {text}\n"
    "{schema_hint}\n\n"
    'Output format: {{"entities": [...], "relations": [...], "events": []}}\n'
    "For relations, head is the subject entity and tail is the object entity."
)


def flat_tags_to_spans(ner_tags, tag_names):
    """Extract entity spans from flat (non-BIO) tags.

    Consecutive tokens with the same non-O tag form one entity.
    Returns list of (start_tok, end_tok_exclusive, type_str).
    """
    spans = []
    cur_type = None
    cur_start = None

    for i, tag_id in enumerate(ner_tags):
        tag = tag_names[tag_id]
        if tag == "O":
            if cur_type is not None:
                spans.append((cur_start, i, cur_type))
                cur_type = None
                cur_start = None
        else:
            if cur_type is None:
                cur_type = tag
                cur_start = i
            elif tag != cur_type:
                spans.append((cur_start, i, cur_type))
                cur_type = tag
                cur_start = i
            # else: same type, continue span

    if cur_type is not None:
        spans.append((cur_start, len(ner_tags), cur_type))

    return spans


def convert_example(example, tag_names, idx, split):
    tokens = example["tokens"]
    ner_tags = example["ner_tags"]
    text = " ".join(tokens)

    char_offsets = []
    pos = 0
    for tok in tokens:
        char_offsets.append((pos, pos + len(tok)))
        pos += len(tok) + 1

    spans = flat_tags_to_spans(ner_tags, tag_names)

    entities = []
    for tok_s, tok_e, etype in spans:
        char_s = char_offsets[tok_s][0]
        char_e = char_offsets[tok_e - 1][1]
        ent_text = text[char_s:char_e]
        entities.append({
            "text": ent_text,
            "type": etype,
            "start": char_s,
            "end": char_e,
        })

    return {
        "id": f"fewnerd_{split}_{idx:05d}",
        "text": text,
        "entities": entities,
        "relations": [],
        "events": [],
    }


def convert_split(dataset, split, tag_names, output_path):
    results = []
    type_counter = Counter()
    total_entities = 0
    total_tokens = 0
    errors = 0

    for idx, example in enumerate(dataset):
        inst = convert_example(example, tag_names, idx, split)
        total_tokens += len(example["tokens"])

        for ent in inst["entities"]:
            actual = inst["text"][ent["start"]:ent["end"]]
            if actual != ent["text"]:
                errors += 1
                if errors <= 5:
                    print(f"  OFFSET ERROR {inst['id']}: '{actual}' != '{ent['text']}'")
            type_counter[ent["type"]] += 1
            total_entities += 1

        results.append(inst)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for inst in results:
            f.write(json.dumps(inst, ensure_ascii=False) + "\n")

    avg_tokens = total_tokens / len(results) if results else 0
    avg_entities = total_entities / len(results) if results else 0

    return {
        "n_instances": len(results),
        "n_entities": total_entities,
        "type_counts": dict(type_counter),
        "avg_tokens": round(avg_tokens, 1),
        "avg_entities": round(avg_entities, 2),
        "errors": errors,
    }


def make_sharegpt(input_path, output_path):
    records = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            inst = json.loads(line)
            human_msg = PROMPT_TEMPLATE.format(text=inst["text"], schema_hint=SCHEMA_HINT)
            output = {"entities": inst["entities"], "relations": [], "events": []}
            records.append({
                "conversations": [
                    {"from": "human", "value": human_msg},
                    {"from": "gpt", "value": json.dumps(output, ensure_ascii=False)},
                ]
            })
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    return len(records)


def main():
    from datasets import load_dataset

    print("Loading Few-NERD SUPERVISED from HuggingFace...")
    ds = load_dataset("DFKI-SLT/few-nerd", "supervised", cache_dir=HF_CACHE)
    print(f"Dataset: {ds}")

    tag_names = ds["train"].features["ner_tags"].feature.names
    print(f"\nTag names ({len(tag_names)}): {tag_names}")

    # Verify first example
    ex = ds["train"][0]
    print(f"\nFirst example tokens: {ex['tokens']}")
    print(f"First example ner_tags: {ex['ner_tags']}")
    print(f"Decoded tags: {[tag_names[t] for t in ex['ner_tags']]}")

    # Convert splits
    split_map = {"train": "train", "validation": "dev", "test": "test"}
    all_stats = {}

    for hf_split, out_name in split_map.items():
        out_path = os.path.join(DATA_DIR, f"{out_name}.json")
        stats = convert_split(ds[hf_split], out_name, tag_names, out_path)
        all_stats[out_name] = stats

        print(f"\n{out_name}: {stats['n_instances']} instances, {stats['n_entities']} entities -> {out_path}")
        print(f"  avg tokens/sent: {stats['avg_tokens']}, avg entities/sent: {stats['avg_entities']}")
        if stats["errors"]:
            print(f"  ERRORS: {stats['errors']}")
        for t, c in sorted(stats["type_counts"].items(), key=lambda x: -x[1]):
            print(f"  {t}: {c}")

    # Generate LLaMA Factory data
    for split_name in ("train", "dev"):
        in_path = os.path.join(DATA_DIR, f"{split_name}.json")
        lf_path = os.path.join(DATA_DIR, f"llmfactory_{split_name}.json")
        if os.path.exists(in_path):
            n = make_sharegpt(in_path, lf_path)
            print(f"\nLLaMA Factory ({split_name}): {n} instances -> {lf_path}")

    # Validation: sample 10 from test
    print("\n" + "=" * 60)
    print("VALIDATION: 10 sampled test instances with entities")
    print("=" * 60)
    test_path = os.path.join(DATA_DIR, "test.json")
    with open(test_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    shown = 0
    import random
    random.seed(42)
    indices = list(range(len(lines)))
    random.shuffle(indices)

    for i in indices:
        if shown >= 10:
            break
        inst = json.loads(lines[i])
        if not inst["entities"]:
            continue
        shown += 1
        print(f"\n--- [{inst['id']}] ---")
        print(f'Text: "{inst["text"][:150]}{"..." if len(inst["text"]) > 150 else ""}"')
        for ent in inst["entities"]:
            verified = inst["text"][ent["start"]:ent["end"]]
            ok = "OK" if verified == ent["text"] else f"MISMATCH(got '{verified}')"
            print(f'  [{ent["start"]}:{ent["end"]}] "{ent["text"]}" -> {ent["type"]}  [{ok}]')

    # Summary
    print("\n" + "=" * 60)
    print("SUMMARY")
    print("=" * 60)
    print(json.dumps(all_stats, indent=2))

    # README
    readme = f"""# Few-NERD SUPERVISED Dataset (UIE Format)

## Source
- HuggingFace: `DFKI-SLT/few-nerd` (supervised config)
- Paper: Ding et al., "Few-NERD: A Few-shot Named Entity Recognition Dataset" (ACL 2021)

## Schema
Coarse 8-type entity schema:
- person, organization, location, building, art, product, event, other

## Format
JSONL files, one JSON object per line:
```json
{{"id": "fewnerd_{{split}}_{{idx:05d}}", "text": "...", "entities": [{{"text": "...", "type": "...", "start": int, "end": int}}], "relations": [], "events": []}}
```
Character-level offsets (start inclusive, end exclusive).

## Statistics
"""
    for split_name, stats in all_stats.items():
        readme += f"\n### {split_name}\n"
        readme += f"- Instances: {stats['n_instances']}\n"
        readme += f"- Total entities: {stats['n_entities']}\n"
        readme += f"- Avg tokens/sentence: {stats['avg_tokens']}\n"
        readme += f"- Avg entities/sentence: {stats['avg_entities']}\n"
        readme += f"- Entity type distribution:\n"
        for t, c in sorted(stats["type_counts"].items(), key=lambda x: -x[1]):
            readme += f"  - {t}: {c}\n"

    readme += f"\n## Conversion\nGenerated by `code/convert_fewnerd.py` on {__import__('datetime').date.today()}\n"

    readme_path = os.path.join(DATA_DIR, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme)
    print(f"\nREADME -> {readme_path}")

    total_errors = sum(s["errors"] for s in all_stats.values())
    if total_errors:
        print(f"\nWARNING: {total_errors} total offset errors")
        sys.exit(1)
    print("\nAll conversions and validations passed.")


if __name__ == "__main__":
    main()
