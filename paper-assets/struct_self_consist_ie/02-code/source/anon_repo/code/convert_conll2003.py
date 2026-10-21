"""Convert CoNLL-2003 BIO-tagged NER data to UIE char-offset JSON format."""

import json
import os
import sys
from collections import Counter

def bio_to_spans(tokens, ner_tags, tag_names):
    """Extract entity spans from BIO tags, returning (start_tok, end_tok, type) tuples."""
    spans = []
    current_type = None
    current_start = None

    for i, tag_id in enumerate(ner_tags):
        tag = tag_names[tag_id]
        if tag.startswith("B-"):
            if current_type is not None:
                spans.append((current_start, i - 1, current_type))
            current_type = tag[2:]
            current_start = i
        elif tag.startswith("I-"):
            etype = tag[2:]
            if current_type != etype:
                if current_type is not None:
                    spans.append((current_start, i - 1, current_type))
                current_type = etype
                current_start = i
        else:  # O
            if current_type is not None:
                spans.append((current_start, i - 1, current_type))
                current_type = None
                current_start = None

    if current_type is not None:
        spans.append((current_start, len(ner_tags) - 1, current_type))

    return spans

def convert_example(example, tag_names, idx, split):
    tokens = example["tokens"]
    ner_tags = example["ner_tags"]
    text = " ".join(tokens)

    # Compute char offsets for each token
    char_offsets = []
    pos = 0
    for tok in tokens:
        char_offsets.append((pos, pos + len(tok)))
        pos += len(tok) + 1

    spans = bio_to_spans(tokens, ner_tags, tag_names)

    entities = []
    for tok_s, tok_e, etype in spans:
        char_s = char_offsets[tok_s][0]
        char_e = char_offsets[tok_e][1]
        ent_text = text[char_s:char_e]
        entities.append({
            "text": ent_text,
            "type": etype,
            "start": char_s,
            "end": char_e,
        })

    return {
        "id": f"conll2003_{split}_{idx:05d}",
        "text": text,
        "entities": entities,
        "relations": [],
        "events": [],
    }

def convert_split(dataset, split_name, tag_names, output_path):
    results = []
    type_counter = Counter()
    total_entities = 0

    for idx, example in enumerate(dataset):
        inst = convert_example(example, tag_names, idx, split_name)

        # Validate: text[start:end] == entity["text"]
        for ent in inst["entities"]:
            actual = inst["text"][ent["start"]:ent["end"]]
            assert actual == ent["text"], (
                f"Mismatch in {inst['id']}: text[{ent['start']}:{ent['end']}] = "
                f"'{actual}' != '{ent['text']}'"
            )
            type_counter[ent["type"]] += 1
            total_entities += 1

        results.append(inst)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        for inst in results:
            f.write(json.dumps(inst, ensure_ascii=False) + "\n")

    return len(results), total_entities, type_counter

def generate_llamafactory(input_path, output_path):
    PROMPT_TEMPLATE = (
        "Extract all structured information (entities and relations) from the "
        "following text. Output a JSON object.\n\n"
        "Text: {text}\n"
        "Entity types: PER, ORG, LOC, MISC\n\n"
        'Output format: {{"entities": [...], "relations": [], "events": []}}\n'
        "For relations, head is the subject entity and tail is the object entity."
    )
    results = []
    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            inst = json.loads(line)
            human_msg = PROMPT_TEMPLATE.format(text=inst["text"])
            output = {
                "entities": inst.get("entities", []),
                "relations": [],
                "events": [],
            }
            results.append({
                "conversations": [
                    {"from": "human", "value": human_msg},
                    {"from": "gpt", "value": json.dumps(output, ensure_ascii=False)},
                ]
            })
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    return len(results)

def main():
    from datasets import load_dataset

    print("Loading CoNLL-2003 dataset...")
    ds = load_dataset("BramVanroy/conll2003", cache_dir="/root/autodl-tmp/.hf_cache")

    tag_names = ds["train"].features["ner_tags"].feature.names
    print(f"Tag names: {tag_names}")

    data_dir = "/root/autodl-tmp/struct_self_consist_ie/data/conll2003"
    split_map = {"train": "train", "validation": "dev", "test": "test"}

    all_stats = {}
    for hf_split, out_name in split_map.items():
        out_path = os.path.join(data_dir, f"{out_name}.json")
        n_inst, n_ent, type_cnt = convert_split(ds[hf_split], out_name, tag_names, out_path)
        all_stats[out_name] = (n_inst, n_ent, type_cnt)
        print(f"\n{out_name}: {n_inst} instances, {n_ent} entities -> {out_path}")
        for t, c in sorted(type_cnt.items()):
            print(f"  {t}: {c}")

    # Generate LLaMA Factory sharegpt training data
    train_path = os.path.join(data_dir, "train.json")
    lf_path = os.path.join(data_dir, "llmfactory_train.json")
    n_lf = generate_llamafactory(train_path, lf_path)
    print(f"\nLLaMA Factory: {n_lf} instances -> {lf_path}")

    # Validation: sample 10 from test
    print("\n" + "=" * 60)
    print("VALIDATION: 10 sampled test instances")
    print("=" * 60)
    test_path = os.path.join(data_dir, "test.json")
    with open(test_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    import random
    random.seed(42)
    sample_indices = sorted(random.sample(range(len(lines)), min(10, len(lines))))

    for i in sample_indices:
        inst = json.loads(lines[i])
        print(f"\n--- [{inst['id']}] ---")
        print(f'Text: "{inst["text"]}"')
        if inst["entities"]:
            print("Entities:")
            for ent in inst["entities"]:
                verified = inst["text"][ent["start"]:ent["end"]]
                ok = "OK" if verified == ent["text"] else f"MISMATCH(got '{verified}')"
                print(f'  [{ent["start"]}:{ent["end"]}] "{ent["text"]}" -> {ent["type"]}  [{ok}]')
        else:
            print("Entities: (none)")

    # First 3 detailed visualization
    print("\n" + "=" * 60)
    print("FIRST 3 TEST INSTANCES (detailed)")
    print("=" * 60)
    for i in range(min(3, len(lines))):
        inst = json.loads(lines[i])
        print(f"\n--- [{inst['id']}] ---")
        print(f'Text: "{inst["text"]}"')
        if inst["entities"]:
            print("Entities:")
            for ent in inst["entities"]:
                print(f'  [{ent["start"]}:{ent["end"]}] "{ent["text"]}" -> {ent["type"]}')
        else:
            print("Entities: (none)")

if __name__ == "__main__":
    main()
