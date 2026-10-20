"""Extract sequence log-probabilities for structured IE samples.

Re-generates N=8 stochastic samples + 1 greedy with logprobs enabled,
saving both parsed structures and per-sample log-probability metadata.
"""

import json
import os
import sys
import time

sys.path.insert(0, '/root/autodl-tmp/struct_self_consist_ie/code')

from data_utils import load_uie_jsonl
from sampling import (
    VLLMSampler, build_uie_prompt, parse_extraction_output,
    realign_spans, SCIERC_SCHEMA_HINT, UIE_JSON_SCHEMA,
)

MODEL = "/root/autodl-tmp/struct_self_consist_ie/checkpoints/qwen3-8b-scierc-merged-v2"
TEST_DATA = "/root/autodl-tmp/struct_self_consist_ie/data/test.jsonl"
OUTPUT_DIR = "/root/autodl-tmp/struct_self_consist_ie/output/exp_012_logprob"


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    print(f"Loading test data from {TEST_DATA}")
    instances = load_uie_jsonl(TEST_DATA)
    print(f"Loaded {len(instances)} instances")

    print(f"Initializing VLLMSampler with model {MODEL}")
    sampler = VLLMSampler(
        MODEL, tensor_parallel_size=1, max_model_len=2048, gpu_memory_utilization=0.9
    )

    prompts = [
        build_uie_prompt(
            inst["text"], subtask="full",
            schema_hint=SCIERC_SCHEMA_HINT, use_train_format=True,
        )
        for inst in instances
    ]
    chat_prompts = [sampler.format_chat_prompt(p) for p in prompts]
    print(f"Built {len(chat_prompts)} chat prompts")

    from vllm import SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    guided = StructuredOutputsParams(json=UIE_JSON_SCHEMA)

    # N=8 stochastic at T=1.0 with logprobs
    print("Starting N=8 stochastic sampling at T=1.0 with logprobs ...")
    t0 = time.time()
    stoch_params = SamplingParams(
        n=8, temperature=1.0, max_tokens=512,
        logprobs=1, structured_outputs=guided,
    )
    stoch_outputs = sampler.llm.generate(chat_prompts, stoch_params)
    t_stoch = time.time() - t0
    print(f"Stochastic sampling done in {t_stoch:.1f}s")

    # Greedy at T=0 with logprobs
    print("Starting N=1 greedy decoding at T=0 with logprobs ...")
    t0 = time.time()
    greedy_params = SamplingParams(
        n=1, temperature=0.0, max_tokens=512,
        logprobs=1, structured_outputs=guided,
    )
    greedy_outputs = sampler.llm.generate(chat_prompts, greedy_params)
    t_greedy = time.time() - t0
    print(f"Greedy decoding done in {t_greedy:.1f}s")

    # Parse + save with logprob metadata
    print("Parsing outputs and extracting logprobs ...")
    results = []
    for i, inst in enumerate(instances):
        gold = {
            "entities": inst.get("entities", []),
            "relations": inst.get("relations", []),
            "events": [],
        }

        samples = []
        for out in stoch_outputs[i].outputs:
            parsed = realign_spans(parse_extraction_output(out.text), inst["text"])
            n_tokens = len(out.token_ids)
            cum_lp = out.cumulative_logprob if out.cumulative_logprob is not None else 0.0
            mean_lp = cum_lp / n_tokens if n_tokens > 0 else 0.0
            samples.append({
                **parsed,
                "cumulative_logprob": cum_lp,
                "n_tokens": n_tokens,
                "mean_logprob": mean_lp,
            })

        g_out = greedy_outputs[i].outputs[0]
        g_parsed = realign_spans(parse_extraction_output(g_out.text), inst["text"])
        g_ntok = len(g_out.token_ids)
        g_cum = g_out.cumulative_logprob if g_out.cumulative_logprob is not None else 0.0
        g_mean = g_cum / g_ntok if g_ntok > 0 else 0.0

        results.append({
            "id": inst.get("id", str(i)),
            "text": inst["text"],
            "gold": gold,
            "samples": samples,
            "greedy": {
                **g_parsed,
                "cumulative_logprob": g_cum,
                "n_tokens": g_ntok,
                "mean_logprob": g_mean,
            },
        })

    output_path = os.path.join(OUTPUT_DIR, "samples_with_logprobs.jsonl")
    with open(output_path, "w", encoding="utf-8") as f:
        for r in results:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    print(f"\nSaved {len(results)} instances to {output_path}")
    print(f"Time: stochastic={t_stoch:.1f}s, greedy={t_greedy:.1f}s, total={t_stoch+t_greedy:.1f}s")

    # Quick sanity check
    lps = [s["mean_logprob"] for r in results for s in r["samples"]]
    print(f"Logprob stats: min={min(lps):.4f}, max={max(lps):.4f}, mean={sum(lps)/len(lps):.4f}")


if __name__ == "__main__":
    main()
