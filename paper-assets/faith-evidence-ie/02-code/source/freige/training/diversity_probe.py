"""Diversity probe: sample N docs, generate K candidates each, measure triple-set diversity."""

import argparse
import json
import random
import sys
import os
from collections import Counter
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from freige.training.rsft_generate import (
    load_model_and_tokenizer,
    prepare_generation_data,
    generate_batch,
)
from freige.eval.evaluator import parse_model_output


def run_probe(args):
    model, tokenizer = load_model_and_tokenizer(
        args.base_model, args.sft_adapter, quantize=args.quantize,
    )

    model.generation_config.temperature = args.temperature
    model.generation_config.top_k = 0
    model.generation_config.top_p = args.top_p
    if args.repetition_penalty != 1.0:
        model.generation_config.repetition_penalty = args.repetition_penalty

    print(f"generation_config: temperature={model.generation_config.temperature}, "
          f"top_k={model.generation_config.top_k}, top_p={model.generation_config.top_p}, "
          f"repetition_penalty={getattr(model.generation_config, 'repetition_penalty', 'N/A')}")

    all_items = prepare_generation_data(args.data_path, args.split, tokenizer)

    rng = random.Random(args.seed)
    sampled = rng.sample(all_items, min(args.n_docs, len(all_items)))
    print(f"Sampled {len(sampled)} docs from {len(all_items)} total")

    results = []
    for idx, item in enumerate(sampled):
        try:
            generations, trunc_flags = generate_batch(
                model, tokenizer, [item["prompt"]],
                args.n_gen, args.temperature, args.max_new_tokens,
            )
        except torch.cuda.OutOfMemoryError:
            torch.cuda.empty_cache()
            print(f"  OOM on doc {item['doc_id']}, skipping")
            continue

        doc_outputs = generations[0]
        doc_truncs = trunc_flags[0]

        triple_sets = []
        format_oks = []
        parsed_list = []
        for gen_idx, raw_text in enumerate(doc_outputs):
            parsed_triples, format_ok = parse_model_output(raw_text)
            format_oks.append(format_ok)
            triple_key = frozenset(
                (t["head"].lower(), t["relation"].lower(), t["tail"].lower())
                for t in parsed_triples
            )
            triple_sets.append(triple_key)
            parsed_list.append(parsed_triples)

        unique_triple_sets = len(set(triple_sets))
        format_ok_rate = sum(format_oks) / len(format_oks)
        truncated_rate = sum(doc_truncs) / len(doc_truncs)

        doc_result = {
            "doc_id": item["doc_id"],
            "unique_triple_sets": unique_triple_sets,
            "n_gen": args.n_gen,
            "format_ok_rate": format_ok_rate,
            "truncated_rate": truncated_rate,
            "n_triples_per_gen": [len(p) for p in parsed_list],
        }
        results.append(doc_result)

        print(f"  [{idx+1}/{len(sampled)}] {item['doc_id'][:40]:40s} "
              f"unique={unique_triple_sets}/{args.n_gen}  "
              f"fmt_ok={format_ok_rate:.0%}  trunc={truncated_rate:.0%}")

    if not results:
        print("No results!")
        return

    mean_unique = sum(r["unique_triple_sets"] for r in results) / len(results)
    mean_fmt = sum(r["format_ok_rate"] for r in results) / len(results)
    mean_trunc = sum(r["truncated_rate"] for r in results) / len(results)
    dist = Counter(r["unique_triple_sets"] for r in results)

    print(f"\n{'='*60}")
    print(f"CONFIG: T={args.temperature}, top_p={args.top_p}, rep_pen={args.repetition_penalty}")
    print(f"DOCS: {len(results)}, GEN_PER_DOC: {args.n_gen}")
    print(f"UNIQUE TRIPLE-SETS: mean={mean_unique:.2f}/{args.n_gen}")
    print(f"FORMAT OK: {mean_fmt:.1%}")
    print(f"TRUNCATED: {mean_trunc:.1%}")
    print(f"Distribution of unique counts:")
    for k in sorted(dist.keys()):
        pct = dist[k] * 100 / len(results)
        bar = '#' * int(pct / 2)
        print(f"  {k}/{args.n_gen}: {dist[k]:3d} ({pct:5.1f}%) {bar}")

    pass_threshold = 4
    pass_rate = sum(1 for r in results if r["unique_triple_sets"] >= pass_threshold) / len(results)
    verdict = "PASS" if mean_unique >= pass_threshold else "FAIL"
    print(f"\nVERDICT: {verdict} (mean={mean_unique:.2f}, target>={pass_threshold}, pass_rate={pass_rate:.0%})")

    summary = {
        "config": {
            "temperature": args.temperature,
            "top_p": args.top_p,
            "repetition_penalty": args.repetition_penalty,
            "n_docs": len(results),
            "n_gen": args.n_gen,
        },
        "metrics": {
            "mean_unique_triple_sets": round(mean_unique, 3),
            "mean_format_ok_rate": round(mean_fmt, 4),
            "mean_truncated_rate": round(mean_trunc, 4),
            "pass_rate_ge4": round(pass_rate, 4),
            "distribution": {str(k): v for k, v in sorted(dist.items())},
        },
        "per_doc": results,
    }

    if args.output:
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w") as f:
            json.dump(summary, f, indent=2, ensure_ascii=False)
        print(f"\nSaved to {args.output}")


def main():
    parser = argparse.ArgumentParser(description="Diversity Probe")
    parser.add_argument("--base_model", type=str, default="./outputs")
    parser.add_argument("--sft_adapter", type=str, default="./outputs")
    parser.add_argument("--data_path", type=str, default="./data/docred")
    parser.add_argument("--split", type=str, default="train")
    parser.add_argument("--n_docs", type=int, default=20)
    parser.add_argument("--n_gen", type=int, default=8)
    parser.add_argument("--temperature", type=float, default=1.0)
    parser.add_argument("--top_p", type=float, default=0.95)
    parser.add_argument("--repetition_penalty", type=float, default=1.0)
    parser.add_argument("--max_new_tokens", type=int, default=1024)
    parser.add_argument("--quantize", action="store_true")
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--output", type=str, default=None)
    args = parser.parse_args()
    run_probe(args)


if __name__ == "__main__":
    main()
