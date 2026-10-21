#!/usr/bin/env python3
"""Convert FewRel val set to UIE JSONL format for RE SC experiments."""

import json
import os
import random
import sys

_project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
sys.path.insert(0, _project_root)
sys.path.insert(0, os.path.join(_project_root, "code"))

FEWREL_VAL_RELATION_NAMES = {
    "P155": "follows",
    "P177": "crosses",
    "P206": "located in or next to body of water",
    "P2094": "competition class",
    "P25": "mother",
    "P26": "spouse",
    "P361": "part of",
    "P364": "original language of film or TV show",
    "P40": "child",
    "P410": "military rank",
    "P412": "voice type",
    "P413": "position played on team / speciality",
    "P463": "member of",
    "P59": "constellation",
    "P641": "sport",
    "P921": "main subject",
}


def token_offsets(tokens):
    offsets = []
    pos = 0
    for tok in tokens:
        offsets.append((pos, pos + len(tok)))
        pos += len(tok) + 1
    return offsets


def convert_instance(inst, relation_name, instance_id):
    tokens = inst["tokens"]
    text = " ".join(tokens)
    offsets = token_offsets(tokens)

    h_name, _, h_token_idxs = inst["h"]
    t_name, _, t_token_idxs = inst["t"]
    h_indices = h_token_idxs[0]
    t_indices = t_token_idxs[0]

    if not h_indices or not t_indices:
        return None
    if max(h_indices) >= len(tokens) or max(t_indices) >= len(tokens):
        return None

    h_start_char = offsets[h_indices[0]][0]
    h_end_char = offsets[h_indices[-1]][1]
    t_start_char = offsets[t_indices[0]][0]
    t_end_char = offsets[t_indices[-1]][1]

    h_text = text[h_start_char:h_end_char]
    t_text = text[t_start_char:t_end_char]

    entities = [
        {"text": h_text, "type": "ENTITY", "start": h_start_char, "end": h_end_char},
        {"text": t_text, "type": "ENTITY", "start": t_start_char, "end": t_end_char},
    ]
    relations = [
        {
            "head": h_text, "tail": t_text, "type": relation_name,
            "head_start": h_start_char, "head_end": h_end_char,
            "tail_start": t_start_char, "tail_end": t_end_char,
        }
    ]

    return {
        "id": instance_id,
        "text": text,
        "entities": entities,
        "relations": relations,
        "events": [],
    }


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--fewrel-dir", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--n-instances", type=int, default=256)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    with open(os.path.join(args.fewrel_dir, "val_wiki.json")) as f:
        val_data = json.load(f)

    rng = random.Random(args.seed)
    n_per_type = max(1, args.n_instances // len(val_data))
    remainder = args.n_instances - n_per_type * len(val_data)

    all_instances = []
    for pid, instances in sorted(val_data.items()):
        rel_name = FEWREL_VAL_RELATION_NAMES.get(pid, pid)
        converted = []
        for i, inst in enumerate(instances):
            result = convert_instance(inst, rel_name, f"fewrel_{pid}_{i:04d}")
            if result is not None:
                converted.append(result)
        rng.shuffle(converted)
        selected = converted[:n_per_type]
        all_instances.extend(selected)
        if remainder > 0 and len(converted) > n_per_type:
            extra = converted[n_per_type:n_per_type + 1]
            all_instances.extend(extra)
            remainder -= len(extra)

    rng.shuffle(all_instances)
    all_instances = all_instances[:args.n_instances]

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        for inst in all_instances:
            f.write(json.dumps(inst, ensure_ascii=False) + "\n")

    rel_types = set()
    for inst in all_instances:
        for r in inst["relations"]:
            rel_types.add(r["type"])
    print(f"Wrote {len(all_instances)} instances to {args.output}")
    print(f"Relation types ({len(rel_types)}): {sorted(rel_types)}")
    print(f"Total gold relations: {sum(len(inst['relations']) for inst in all_instances)}")


if __name__ == "__main__":
    main()
