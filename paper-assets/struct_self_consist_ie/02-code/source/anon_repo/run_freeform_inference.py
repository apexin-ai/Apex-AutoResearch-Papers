"""Free-form (unconstrained) decoding ablation for structured self-consistency IE.

Runs the same vLLM inference pipeline as constrained decoding (exp_012_rerun_1024),
but WITHOUT XGrammar JSON grammar constraint. Post-hoc JSON parsing is applied.

Input: SciERC test set (551 instances)
Output: results/exp_freeform_ablation/samples.jsonl
Dependencies: vLLM 0.18.1, code/{sampling,data_utils}.py
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "code"))

from data_utils import load_scierc
from sampling import (
    VLLMSampler,
    build_uie_prompt,
    parse_extraction_output,
    realign_spans,
    SCIERC_SCHEMA_HINT,
)


def parse_args():
    p = argparse.ArgumentParser(description="Free-form decoding ablation for structured IE")
    p.add_argument("--model_path", type=str,
                    default="checkpoints/qwen3-8b-scierc-merged-v2")
    p.add_argument("--data_dir", type=str, default="data/scierc/processed_data")
    p.add_argument("--output_dir", type=str, default="results/exp_freeform_ablation")
    p.add_argument("--num_samples", type=int, default=8)
    p.add_argument("--temperature", type=float, default=1.0)
    p.add_argument("--max_tokens", type=int, default=1024)
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--tensor_parallel", type=int, default=1)
    p.add_argument("--num_test", type=int, default=99999)
    return p.parse_args()


def try_parse_json(raw_text):
    """Attempt JSON extraction from free-form text. Returns (dict_or_None, success)."""
    text = raw_text.strip()

    # Direct parse
    try:
        data = json.loads(text)
        if isinstance(data, dict):
            return data, True
    except json.JSONDecodeError:
        pass

    # Find outermost { ... }
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end > start:
        try:
            data = json.loads(text[start:end + 1])
            if isinstance(data, dict):
                return data, True
        except json.JSONDecodeError:
            pass

    # Regex for ```json ... ``` blocks
    m = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', text, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(1))
            if isinstance(data, dict):
                return data, True
        except json.JSONDecodeError:
            pass

    return None, False


def parse_and_validate(raw_text, source_text):
    """Parse raw text, validate, realign. Returns (extraction, parse_success)."""
    data, success = try_parse_json(raw_text)

    if success:
        extraction = parse_extraction_output(json.dumps(data))
        extraction = realign_spans(extraction, source_text)
        return extraction, True

    # Fallback: use existing parser (handles partial JSON)
    extraction = parse_extraction_output(raw_text)
    has_content = bool(extraction["entities"] or extraction["relations"] or extraction["events"])
    if has_content:
        extraction = realign_spans(extraction, source_text)
        return extraction, True

    return extraction, False


def main():
    args = parse_args()
    os.makedirs(args.output_dir, exist_ok=True)
    os.makedirs("logs", exist_ok=True)

    # Load data
    splits = load_scierc(args.data_dir)
    test_instances = splits["test"][:args.num_test]
    print(f"Loaded {len(test_instances)} test instances from scierc")

    # Init vLLM sampler (identical to constrained)
    sampler = VLLMSampler(
        model_path=args.model_path,
        tensor_parallel_size=args.tensor_parallel,
        max_model_len=4096,
        gpu_memory_utilization=0.90,
    )

    # Build prompts (identical to constrained)
    prompts = [
        build_uie_prompt(inst["text"], subtask="joint",
                         schema_hint=SCIERC_SCHEMA_HINT,
                         use_train_format=True)
        for inst in test_instances
    ]

    print(f"Free-form sampling: N={args.num_samples}, T={args.temperature}, "
          f"max_tokens={args.max_tokens}, seed={args.seed}")
    t0 = time.time()

    # Stochastic sampling — NO grammar constraint
    raw_samples, stoch_logprobs = sampler.sample(
        prompts,
        n_samples=args.num_samples,
        temperature=args.temperature,
        max_tokens=args.max_tokens,
        use_grammar=False,
        use_chat_template=True,
        collect_logprobs=True,
        seed=args.seed,
    )

    # Greedy — also no grammar
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

    # Post-hoc parsing
    total_samples = 0
    total_parsed = 0
    sampled_instances = []

    for idx, inst in enumerate(test_instances):
        gold = {
            "entities": inst.get("entities", []),
            "relations": inst.get("relations", []),
            "events": inst.get("events", []),
        }

        parsed_samples = []
        sample_parse_success = []

        for j, raw_text in enumerate(raw_samples[idx]):
            total_samples += 1
            extraction, success = parse_and_validate(raw_text, inst["text"])

            if success:
                total_parsed += 1

            extraction.update(stoch_logprobs[idx][j])
            extraction["raw_text"] = raw_text
            extraction["parse_success"] = success
            parsed_samples.append(extraction)
            sample_parse_success.append(success)

        # Greedy
        greedy_raw = raw_greedy[idx][0]
        parsed_greedy, greedy_success = parse_and_validate(greedy_raw, inst["text"])
        parsed_greedy.update(greedy_logprobs[idx][0])
        parsed_greedy["raw_text"] = greedy_raw
        parsed_greedy["parse_success"] = greedy_success

        inst_dict = {
            "id": inst.get("id", str(idx)),
            "text": inst["text"],
            "gold": gold,
            "samples": parsed_samples,
            "greedy": parsed_greedy,
            "logprobs": [lp["mean_logprob"] for lp in stoch_logprobs[idx]],
            "parse_success": sample_parse_success,
        }
        sampled_instances.append(inst_dict)

    # Save results
    output_path = os.path.join(args.output_dir, "samples.jsonl")
    with open(output_path, "w", encoding="utf-8") as f:
        for inst in sampled_instances:
            f.write(json.dumps(inst, ensure_ascii=False) + "\n")

    parse_rate = total_parsed / total_samples * 100 if total_samples > 0 else 0

    summary = {
        "experiment": "exp_freeform_ablation",
        "model": args.model_path,
        "dataset": "scierc",
        "n_instances": len(test_instances),
        "n_samples": args.num_samples,
        "temperature": args.temperature,
        "max_tokens": args.max_tokens,
        "seed": args.seed,
        "use_grammar": False,
        "total_samples": total_samples,
        "total_parsed": total_parsed,
        "parse_rate_pct": round(parse_rate, 2),
        "elapsed_seconds": round(elapsed, 1),
    }

    with open(os.path.join(args.output_dir, "run_summary.json"), "w") as f:
        json.dump(summary, f, indent=2)

    print(f"\nResults: {output_path}")
    print(f"Parse rate: {parse_rate:.1f}% ({total_parsed}/{total_samples})")


if __name__ == "__main__":
    main()
