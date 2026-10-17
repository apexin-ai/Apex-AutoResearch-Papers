# Diagnostic: free-form generation (no structured output constraint) for LLaMA-3.1-8B NER.
# Purpose: Determine if StructuredOutputsParams causes all-zero predictions in exp012.
# Usage: python scripts/diagnose_llama8b_freeform.py [--n_samples 5] [--n_types 6]

import argparse
import json
import logging
import sys
import time
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

DEFAULT_MODEL = "~/.cache/models/llama-3.1-8b-instruct/LLM-Research/Meta-Llama-3___1-8B-Instruct"
DEFAULT_TYPES_FILE = "./configs/few_nerd_types.json"
DEFAULT_DATA_DIR = "./data/parquet"
DEFAULT_OUTPUT = "./artifacts/llama8b_freeform_diagnostic.json"

DIAGNOSTIC_TYPES = [
    "person-athlete",
    "organization-company",
    "location-GPE",
    "event-sportsevent",
    "product-car",
    "other-award",
]


def build_prompt_v2(input_text, type_definitions, type_subset):
    type_desc_lines = []
    for t in sorted(type_subset):
        defn = type_definitions.get(t, t)
        type_desc_lines.append(f"- {t}: {defn}")
    type_desc = "\n".join(type_desc_lines)

    return (
        f"Extract all named entities from the following text. "
        f"Only extract entities of the following types:\n{type_desc}\n\n"
        f"Text: {input_text}\n\n"
        f"Only extract entities that clearly match one of the given types. "
        f"If no entities of these types exist in the text, output an empty list [].\n\n"
        f'Output as JSON: [{{"text": "...", "type": "..."}}]'
    )


def main():
    parser = argparse.ArgumentParser(description="Free-form NER diagnostic for LLaMA-3.1-8B")
    parser.add_argument("--model_path", default=DEFAULT_MODEL)
    parser.add_argument("--types_file", default=DEFAULT_TYPES_FILE)
    parser.add_argument("--data_dir", default=DEFAULT_DATA_DIR)
    parser.add_argument("--output_path", default=DEFAULT_OUTPUT)
    parser.add_argument("--n_samples", type=int, default=5)
    parser.add_argument("--n_types", type=int, default=6, help="Number of entity types in prompt")
    parser.add_argument("--max_model_len", type=int, default=4096)
    parser.add_argument("--gpu_memory_utilization", type=float, default=0.90)
    args = parser.parse_args()

    sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
    from few_nerd_utils import load_few_nerd, load_type_definitions

    logger.info("Loading type definitions from %s", args.types_file)
    type_definitions = load_type_definitions(args.types_file)

    logger.info("Loading Few-NERD test data (first %d samples)...", args.n_samples)
    samples = load_few_nerd(split="test", max_samples=args.n_samples, data_dir=args.data_dir)
    logger.info("Loaded %d samples", len(samples))

    batch_types = DIAGNOSTIC_TYPES[:args.n_types]
    logger.info("Using %d diagnostic types: %s", len(batch_types), batch_types)

    prompts = []
    for sample in samples:
        prompt = build_prompt_v2(sample["text"], type_definitions, batch_types)
        prompts.append(prompt)

    logger.info("Loading vLLM model from %s (NO structured output constraint)...", args.model_path)
    from vllm import LLM, SamplingParams

    llm = LLM(
        model=args.model_path,
        dtype="bfloat16",
        gpu_memory_utilization=args.gpu_memory_utilization,
        enforce_eager=True,
        max_model_len=args.max_model_len,
        trust_remote_code=True,
        disable_log_stats=True,
    )

    # Apply chat template for LLaMA-3.1-Instruct
    tokenizer = llm.get_tokenizer()
    formatted_prompts = [
        tokenizer.apply_chat_template(
            [{"role": "user", "content": p}],
            tokenize=False,
            add_generation_prompt=True,
        )
        for p in prompts
    ]
    logger.info("Applied chat template. Example formatted prompt (first 300 chars): %s",
                formatted_prompts[0][:300] if formatted_prompts else "NONE")

    sampling_params = SamplingParams(
        max_tokens=2048,
        temperature=0.0,
    )

    logger.info("Generating %d samples (free-form, no JSON constraint)...", len(formatted_prompts))
    t0 = time.time()
    outputs = llm.generate(formatted_prompts, sampling_params)
    elapsed = time.time() - t0
    logger.info("Generation done in %.1fs", elapsed)

    results = []
    print("\n" + "=" * 80)
    print("FREE-FORM GENERATION DIAGNOSTIC RESULTS")
    print("=" * 80)

    for i, (sample, prompt, output) in enumerate(zip(samples, prompts, outputs)):
        raw_text = output.outputs[0].text
        prompt_tokens = len(output.prompt_token_ids)
        gen_tokens = len(output.outputs[0].token_ids)

        print(f"\n--- Sample {i} ---")
        print(f"Input text (first 200 chars): {sample['text'][:200]}")
        print(f"Ground truth entities: {sample['entities'][:5]}")
        print(f"Prompt tokens: {prompt_tokens}, Gen tokens: {gen_tokens}")
        print(f"Raw output ({len(raw_text)} chars):")
        print(raw_text)
        print()

        results.append({
            "sample_id": i,
            "input_text": sample["text"],
            "ground_truth": sample["entities"],
            "prompt": prompt,
            "raw_output": raw_text,
            "prompt_tokens": prompt_tokens,
            "gen_tokens": gen_tokens,
            "output_length": len(raw_text),
            "batch_types": batch_types,
        })

    output_path = Path(args.output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info("Saved diagnostic results to %s", output_path)

    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    print(f"Samples: {len(results)}")
    print(f"Total time: {elapsed:.1f}s")
    avg_gen = sum(r["gen_tokens"] for r in results) / len(results)
    print(f"Avg gen tokens: {avg_gen:.0f}")
    non_empty = sum(1 for r in results if len(r["raw_output"].strip()) > 2)
    print(f"Non-empty outputs: {non_empty}/{len(results)}")
    print(f"Results saved to: {output_path}")


if __name__ == "__main__":
    main()
