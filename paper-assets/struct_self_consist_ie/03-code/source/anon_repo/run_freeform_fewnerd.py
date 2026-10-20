#!/usr/bin/env python3
"""Free-form (unconstrained) decoding for FewNERD.
Tests whether LP compression is model-intrinsic across datasets.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "code"))

from data_utils import load_fewnerd
from sampling import (
    VLLMSampler,
    build_uie_prompt,
    parse_extraction_output,
    realign_spans,
    FEWNERD_SCHEMA_HINT,
)


def parse_args():
    p = argparse.ArgumentParser()
    p.add_argument("--seed", type=int, required=True)
    p.add_argument("--gpu", type=int, default=0)
    p.add_argument("--n_samples", type=int, default=8)
    p.add_argument("--temperature", type=float, default=1.0)
    p.add_argument("--max_tokens", type=int, default=1024)
    p.add_argument("--model_path", type=str,
                    default="checkpoints/qwen3-8b-fewnerd-exp021-merged/qwen3-8b-fewnerd-exp021-merged")
    p.add_argument("--data_dir", type=str, default="data/fewnerd/")
    p.add_argument("--output_dir", type=str,
                    default="output/fewnerd_freeform")
    return p.parse_args()


def main():
    args = parse_args()
    os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu)

    seed_dir = os.path.join(args.output_dir, f"seed_{args.seed}")
    os.makedirs(seed_dir, exist_ok=True)

    splits = load_fewnerd(args.data_dir)
    test = splits["test"]
    print(f"FewNERD test: {len(test)} instances")

    sampler = VLLMSampler(
        model_path=args.model_path,
        tensor_parallel_size=1,
        max_model_len=4096,
        gpu_memory_utilization=0.90,
    )

    prompts = [
        build_uie_prompt(inst["text"], subtask="ner",
                         schema_hint=FEWNERD_SCHEMA_HINT,
                         use_train_format=True)
        for inst in test
    ]

    print(f"Free-form sampling: N={args.n_samples}, T={args.temperature}, seed={args.seed}")
    t0 = time.time()

    raw_samples, stoch_logprobs = sampler.sample(
        prompts,
        n_samples=args.n_samples,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        use_grammar=False,
        use_chat_template=True,
        collect_logprobs=True,
        seed=args.seed,
    )

    raw_greedy, greedy_logprobs = sampler.sample(
        prompts,
        n_samples=1,
        temperature=0.0,
        max_tokens=args.max_tokens,
        use_grammar=False,
        use_chat_template=True,
        collect_logprobs=True,
    )

    elapsed = time.time() - t0
    print(f"Sampling done in {elapsed:.1f}s")

    total_samples = 0
    total_parsed = 0
    sampled_instances = []

    for idx, inst in enumerate(test):
        gold = {
            "entities": inst.get("entities", []),
            "relations": inst.get("relations", []),
            "events": inst.get("events", []),
        }

        parsed_samples = []
        for j, raw_text in enumerate(raw_samples[idx]):
            total_samples += 1
            extraction = parse_extraction_output(raw_text)
            extraction = realign_spans(extraction, inst["text"])
            has_content = bool(extraction["entities"] or extraction["relations"] or extraction["events"])
            if has_content:
                total_parsed += 1
            extraction.update(stoch_logprobs[idx][j])
            extraction["raw_text"] = raw_text
            extraction["parse_success"] = has_content or raw_text.strip().startswith("{")
            parsed_samples.append(extraction)

        greedy_raw = raw_greedy[idx][0]
        parsed_greedy = parse_extraction_output(greedy_raw)
        parsed_greedy = realign_spans(parsed_greedy, inst["text"])
        parsed_greedy.update(greedy_logprobs[idx][0])
        parsed_greedy["raw_text"] = greedy_raw

        inst_dict = {
            "id": inst.get("id", str(idx)),
            "text": inst["text"],
            "gold": gold,
            "samples": parsed_samples,
            "greedy": parsed_greedy,
            "logprobs": [lp["mean_logprob"] for lp in stoch_logprobs[idx]],
        }
        sampled_instances.append(inst_dict)

    output_path = os.path.join(seed_dir, "samples.jsonl")
    with open(output_path, "w", encoding="utf-8") as f:
        for inst in sampled_instances:
            f.write(json.dumps(inst, ensure_ascii=False) + "\n")

    parse_rate = total_parsed / total_samples * 100 if total_samples > 0 else 0

    summary = {
        "experiment": "exp_freeform_fewnerd",
        "model": args.model_path,
        "dataset": "fewnerd",
        "n_instances": len(test),
        "n_samples": args.n_samples,
        "temperature": args.temperature,
        "seed": args.seed,
        "use_grammar": False,
        "total_samples": total_samples,
        "nonempty_samples": total_parsed,
        "nonempty_rate_pct": round(parse_rate, 2),
        "elapsed_seconds": round(elapsed, 1),
    }

    with open(os.path.join(seed_dir, "run_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print(f"Results: {output_path}")
    print(f"Nonempty rate: {parse_rate:.1f}% ({total_parsed}/{total_samples})")


if __name__ == "__main__":
    main()
