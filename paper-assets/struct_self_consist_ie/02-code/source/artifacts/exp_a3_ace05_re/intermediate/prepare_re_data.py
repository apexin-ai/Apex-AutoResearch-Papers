#!/usr/bin/env python3
"""Prepare SciERC data for Relation Extraction SC experiments.

Loads SciERC test split, filters to instances with ≥1 gold relation,
builds few-shot RE prompts, and outputs JSONL for the sampling pipeline.

Usage:
    python prepare_re_data.py \
        --scierc-dir /path/to/scierc \
        --output /path/to/re_test_instances.jsonl \
        --few-shot-k 3
"""

import argparse
import json
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "../.."))

from data_utils import load_scierc, Instance
from sampling import SCIERC_SCHEMA_HINT


SCHEMA_HINT = SCIERC_SCHEMA_HINT

RE_FEWSHOT_INSTRUCTION = (
    "Extract all relations (head entity, relation type, tail entity) from the given text. "
    "Output a JSON object with fields: entities, relations, events.\n\n"
    f"{SCHEMA_HINT}\n\n"
    "Output format: "
    '{"entities": [], '
    '"relations": [{"head": "...", "tail": "...", "type": "...", '
    '"head_start": <int>, "head_end": <int>, "tail_start": <int>, "tail_end": <int>}], '
    '"events": []}\n'
)


def instance_to_demo(inst: Instance) -> str:
    """Format a gold instance as a few-shot demonstration."""
    text = inst["text"]
    gold_rels = inst.get("relations", [])
    gold_json = json.dumps(
        {"entities": [], "relations": gold_rels, "events": []},
        ensure_ascii=False,
    )
    return f"Text: {text}\nOutput: {gold_json}"


def build_fewshot_prompt(
    inst: Instance,
    demos: list[Instance],
) -> str:
    """Build a few-shot RE prompt for a test instance."""
    parts = [RE_FEWSHOT_INSTRUCTION]
    for i, demo in enumerate(demos):
        parts.append(f"### Example {i + 1}\n{instance_to_demo(demo)}")
    parts.append(f"### Now extract:\nText: {inst['text']}\nOutput:")
    return "\n\n".join(parts)


def build_zeroshot_prompt(inst: Instance) -> str:
    """Build a zero-shot RE prompt for a test instance."""
    return (
        f"{RE_FEWSHOT_INSTRUCTION}\n"
        f"Text: {inst['text']}\nOutput:"
    )


def select_demos(
    train_instances: list[Instance],
    k: int,
    seed: int = 42,
) -> list[Instance]:
    """Select k diverse few-shot demonstrations from training set.

    Picks instances that have relations AND cover diverse relation types.
    """
    rel_instances = [inst for inst in train_instances if inst.get("relations")]
    if not rel_instances:
        return []

    rng = random.Random(seed)

    seen_types: set[str] = set()
    selected: list[Instance] = []

    rng.shuffle(rel_instances)
    for inst in rel_instances:
        rel_types = {r["type"] for r in inst["relations"]}
        new_types = rel_types - seen_types
        if new_types:
            selected.append(inst)
            seen_types |= rel_types
            if len(selected) >= k:
                break

    while len(selected) < k and len(selected) < len(rel_instances):
        candidate = rng.choice(rel_instances)
        if candidate not in selected:
            selected.append(candidate)

    return selected[:k]


def main():
    parser = argparse.ArgumentParser(description="Prepare SciERC RE data for SC experiments")
    parser.add_argument("--scierc-dir", required=True, help="Path to SciERC data directory")
    parser.add_argument("--output", required=True, help="Output JSONL path for test instances")
    parser.add_argument("--demo-output", default=None, help="Output path for few-shot demos JSON")
    parser.add_argument("--few-shot-k", type=int, default=3, help="Number of few-shot examples")
    parser.add_argument("--prompt-mode", choices=["zeroshot", "fewshot", "train_aligned"],
                        default="fewshot", help="Prompt construction mode")
    parser.add_argument("--min-relations", type=int, default=1,
                        help="Minimum gold relations to include instance")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--stats", action="store_true", help="Print dataset statistics")
    args = parser.parse_args()

    splits = load_scierc(args.scierc_dir)
    train_all = splits["train"]
    test_all = splits["test"]

    test_re = [inst for inst in test_all if len(inst.get("relations", [])) >= args.min_relations]

    if args.stats:
        for split_name, insts in [("train", train_all), ("test", test_all), ("test_re_filtered", test_re)]:
            n_rels = sum(len(inst.get("relations", [])) for inst in insts)
            n_with_rel = sum(1 for inst in insts if inst.get("relations"))
            rel_types = set()
            for inst in insts:
                for r in inst.get("relations", []):
                    rel_types.add(r["type"])
            print(f"{split_name}: {len(insts)} instances, {n_with_rel} with relations, "
                  f"{n_rels} total relations, types: {sorted(rel_types)}")

    demos = select_demos(train_all, args.few_shot_k, seed=args.seed)

    output_instances = []
    for inst in test_re:
        if args.prompt_mode == "fewshot":
            prompt = build_fewshot_prompt(inst, demos)
        elif args.prompt_mode == "zeroshot":
            prompt = build_zeroshot_prompt(inst)
        else:
            prompt = None

        record = {
            "id": inst["id"],
            "text": inst["text"],
            "entities": inst.get("entities", []),
            "relations": inst.get("relations", []),
            "events": [],
        }
        if prompt is not None:
            record["prompt"] = prompt

        output_instances.append(record)

    os.makedirs(os.path.dirname(args.output) or ".", exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        for inst in output_instances:
            f.write(json.dumps(inst, ensure_ascii=False) + "\n")

    print(f"Wrote {len(output_instances)} RE instances to {args.output}")
    print(f"  Relation types in test set: {sorted({r['type'] for inst in output_instances for r in inst['relations']})}")
    print(f"  Total gold relations: {sum(len(inst['relations']) for inst in output_instances)}")

    if args.demo_output and demos:
        os.makedirs(os.path.dirname(args.demo_output) or ".", exist_ok=True)
        with open(args.demo_output, "w", encoding="utf-8") as f:
            json.dump([dict(d) for d in demos], f, indent=2, ensure_ascii=False)
        print(f"Wrote {len(demos)} few-shot demos to {args.demo_output}")


if __name__ == "__main__":
    main()
