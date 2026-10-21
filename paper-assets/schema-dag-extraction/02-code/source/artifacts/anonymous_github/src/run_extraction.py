"""Constrained JSON decoding NER extraction using vLLM.

v2 changes (2026-05-14): Added prompt_version support (v1=with offsets, v2=text+type only).

Input: Few-NERD test data, type batch config, LLM model
Output: JSON with extraction results per (sample, batch) pair
Dependencies: vllm, transformers
"""
import argparse
import json
import logging
import time
from pathlib import Path
from typing import Dict, List, Optional, Set

logger = logging.getLogger(__name__)


# --- v1: original schema/prompt with start/end offsets ---

def build_json_schema_v1(batch_types: list) -> dict:
    """Build JSON schema with start/end offsets (v1)."""
    return {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "text": {"type": "string"},
                "type": {"type": "string", "enum": sorted(batch_types)},
                "start": {"type": "integer"},
                "end": {"type": "integer"},
            },
            "required": ["text", "type", "start", "end"],
        },
    }


def build_prompt_v1(input_text: str, type_definitions: Dict[str, str], type_subset: List[str]) -> str:
    """Build NER extraction prompt requesting start/end offsets (v1)."""
    type_desc_lines = []
    for t in sorted(type_subset):
        defn = type_definitions.get(t, t)
        type_desc_lines.append(f"- {t}: {defn}")
    type_desc = "\n".join(type_desc_lines)

    return (
        f"Extract all named entities from the following text. "
        f"Only extract entities of the following types:\n{type_desc}\n\n"
        f"Text: {input_text}\n\n"
        f'Output as JSON: [{{"text": "...", "type": "...", "start": ..., "end": ...}}]'
    )


# --- v2: text+type only, no offsets ---

def build_json_schema_v2(batch_types: list) -> dict:
    """Build JSON schema without start/end fields (v2: text+type only)."""
    return {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "text": {"type": "string"},
                "type": {"type": "string", "enum": sorted(batch_types)},
            },
            "required": ["text", "type"],
        },
    }


def build_prompt_v2(input_text: str, type_definitions: Dict[str, str], type_subset: List[str]) -> str:
    """Build NER extraction prompt without offsets (v2: text+type only)."""
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


# Backward-compatible aliases
build_json_schema = build_json_schema_v1
build_prompt = build_prompt_v1

# --- Event Detection prompts (for MAVEN-style tasks) ---

def build_prompt_v2_event(input_text: str, type_definitions: dict, type_subset: list) -> str:
    """Build event trigger extraction prompt (v2: text+type only)."""
    type_desc_lines = []
    for t in sorted(type_subset):
        defn = type_definitions.get(t, t)
        type_desc_lines.append(f"- {t}: {defn}")
    type_desc = "\n".join(type_desc_lines)

    return (
        f"Extract all event triggers from the following text. "
        f"A trigger is the word or phrase that most clearly expresses the event occurrence. "
        f"Only extract triggers of the following event types:\n{type_desc}\n\n"
        f"Text: {input_text}\n\n"
        f"Only extract triggers that clearly match one of the given event types. "
        f"If no events of these types exist in the text, output an empty list [].\n\n"
        f'Output as JSON: [{{\"text\": \"...\",''
        f' \"type\": \"...\"}}]'
    )


def build_prompt_v1_event(input_text: str, type_definitions: dict, type_subset: list) -> str:
    """Build event trigger extraction prompt with offsets (v1)."""
    type_desc_lines = []
    for t in sorted(type_subset):
        defn = type_definitions.get(t, t)
        type_desc_lines.append(f"- {t}: {defn}")
    type_desc = "\n".join(type_desc_lines)

    return (
        f"Extract all event triggers from the following text. "
        f"A trigger is the word or phrase that most clearly expresses the event occurrence. "
        f"Only extract triggers of the following event types:\n{type_desc}\n\n"
        f"Text: {input_text}\n\n"
        f'Output as JSON: [{{\"text\": \"...\",''
        f' \"type\": \"...\",''
        f' \"start\": ..., \"end\": ...}}]'
    )


# --- Relation Extraction prompts (for FewRel-style tasks) ---
# Pilot uses MiniLM BCS; production experiments should switch to Qwen3 embeddings


def build_json_schema_re(relation_types: List[str]) -> dict:
    return {
        "type": "object",
        "properties": {
            "relation": {
                "type": "string",
                "enum": sorted(relation_types) + ["none"],
            },
        },
        "required": ["relation"],
    }


def build_prompt_v2_re(sentence: str, head: str, tail: str,
                       relation_defs: Dict[str, str],
                       relation_types: List[str]) -> str:
    candidates = ", ".join(sorted(relation_types))
    return (
        "Given the following sentence and two entities, "
        "classify the relation between them.\n\n"
        f'Sentence: "{sentence}"\n'
        f'Head entity: "{head}"\n'
        f'Tail entity: "{tail}"\n\n'
        f"Candidate relations: {candidates}\n\n"
        'Output a single JSON object: {"relation": "<relation_type>"}\n'
        'If none of the candidate relations apply, output: {"relation": "none"}'
    )




def run_extraction(
    model_path: str,
    samples: List[Dict],
    batch_config: Dict,
    type_definitions: Dict[str, str],
    max_model_len: int = 4096,
    prompt_version: str = "v1",
    task: str = "ner",
    gpu_memory_utilization: float = 0.95,
) -> List[Dict]:
    """Run NER extraction for all (sample, type_batch) combinations.

    Args:
        model_path: Path to model directory.
        samples: List of {"text": str, "entities": [...]}.
        batch_config: Output of select_type_batches.py (nested dict by count).
        type_definitions: {type_name: definition}.
        max_model_len: vLLM max sequence length.
        prompt_version: "v1" (with offsets) or "v2" (text+type only).

    Returns:
        List of result dicts with predictions and metadata.
    """
    from vllm import LLM, SamplingParams
    from vllm.sampling_params import StructuredOutputsParams

    if task == "re":
        schema_fn = build_json_schema_re
        prompt_fn = None  # RE uses build_prompt_v2_re with different signature
    elif prompt_version == "v2":
        schema_fn = build_json_schema_v2
        prompt_fn = build_prompt_v2_event if task == "event_detection" else build_prompt_v2
    else:
        schema_fn = build_json_schema_v1
        prompt_fn = build_prompt_v1_event if task == "event_detection" else build_prompt_v1

    logger.info("Loading vLLM model from %s (prompt_version=%s)", model_path, prompt_version)
    llm = LLM(
        model=model_path,
        dtype="bfloat16",
        gpu_memory_utilization=gpu_memory_utilization,
        enforce_eager=True,
        max_model_len=max_model_len,
        trust_remote_code=True,
        disable_log_stats=True,
    )

    tokenizer = llm.get_tokenizer()
    _model_id = getattr(tokenizer, 'name_or_path', '') or model_path
    _needs_chat_template = any(kw in _model_id.lower() for kw in ['llama', 'mistral', 'gemma', 'phi'])
    if _needs_chat_template:
        logger.info("Chat template enabled for model: %s", _model_id)

    all_results = []

    for count_key, strategies in batch_config.items():
        batches_to_run = []

        for strat_key in ["low_bcs", "high_bcs"]:
            if strat_key not in strategies:
                continue
            strat = strategies[strat_key]
            if isinstance(strat, list):
                for bi, b in enumerate(strat):
                    batches_to_run.append((f"{strat_key}/{bi}", b["types"], b["bcs"]))
            else:
                batches_to_run.append((strat_key, strat["types"], strat["bcs"]))

        if "random" in strategies:
            for ri, rb in enumerate(strategies["random"]):
                batches_to_run.append((f"random/{ri}", rb["types"], rb["bcs"]))

        for batch_id, batch_types, batch_bcs in batches_to_run:
            full_batch_id = f"{count_key}/{batch_id}"
            type_set = set(batch_types)
            logger.info("Running batch %s (%d types, BCS=%.4f) on %d samples",
                        full_batch_id, len(batch_types), batch_bcs, len(samples))

            # Per-batch JSON schema with type enum constraint
            batch_schema = schema_fn(batch_types)
            structured_params = StructuredOutputsParams(json=batch_schema)
            sampling_params = SamplingParams(
                max_tokens=1024,
                temperature=0.0,
                structured_outputs=structured_params,
            )

            prompts = []
            sample_indices = []
            if task == "re":
                for si, sample in enumerate(samples):
                    if sample.get("relation_type") and sample["relation_type"] not in batch_types:
                        continue
                    prompt = build_prompt_v2_re(
                        sample["text"], sample["head_entity"],
                        sample["tail_entity"], type_definitions, batch_types)
                    prompts.append(prompt)
                    sample_indices.append(si)
                if not prompts:
                    logger.warning("No RE samples for batch %s", full_batch_id)
                    continue
            else:
                for si, sample in enumerate(samples):
                    prompt = prompt_fn(sample["text"], type_definitions, batch_types)
                    prompts.append(prompt)
                    sample_indices.append(si)

            if _needs_chat_template:
                prompts = [
                    tokenizer.apply_chat_template(
                        [{"role": "user", "content": p}],
                        tokenize=False,
                        add_generation_prompt=True,
                    )
                    for p in prompts
                ]

            t0 = time.time()
            outputs = llm.generate(prompts, sampling_params)
            elapsed = time.time() - t0

            for oi, output in enumerate(outputs):
                si = sample_indices[oi]
                generated_text = output.outputs[0].text
                prompt_tokens = len(output.prompt_token_ids)
                gen_tokens = len(output.outputs[0].token_ids)

                try:
                    predictions = json.loads(generated_text)
                except json.JSONDecodeError:
                    logger.warning("Failed to parse JSON for sample %d batch %s: %s",
                                   si, full_batch_id, generated_text[:200])
                    predictions = []

                all_results.append({
                    "sample_id": si,
                    "batch_id": full_batch_id,
                    "count_key": count_key,
                    "batch_types": batch_types,
                    "batch_bcs": batch_bcs,
                    "predictions": predictions,
                    "prompt_tokens": prompt_tokens,
                    "gen_tokens": gen_tokens,
                    "latency_s": elapsed / len(prompts),
                    "prompt_version": prompt_version,
                })

            logger.info("  Batch %s done: %.1fs total, %d outputs", full_batch_id, elapsed, len(outputs))

    return all_results


def main():
    parser = argparse.ArgumentParser(description="Run constrained JSON NER extraction with vLLM")
    parser.add_argument("--model_path", required=True, help="Path to model directory")
    parser.add_argument("--data_dir", default="./data", help="Data directory")
    parser.add_argument("--batch_config", required=True, help="Type batch JSON from select_type_batches.py")
    parser.add_argument("--output_path", required=True, help="Output results JSON path")
    parser.add_argument("--max_samples", type=int, default=None, help="Max test samples")
    parser.add_argument("--types_file", required=True, help="Type definitions JSON path")
    parser.add_argument("--max_model_len", type=int, default=4096, help="vLLM max model len")
    parser.add_argument("--prompt_version", choices=["v1", "v2"], default="v1",
                        help="Prompt version: v1 (with offsets) or v2 (text+type only)")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    import sys
    sys.path.insert(0, str(Path(__file__).parent))
    from few_nerd_utils import load_few_nerd, load_type_definitions

    logger.info("Loading data...")
    samples = load_few_nerd(split="test", max_samples=args.max_samples)
    type_definitions = load_type_definitions(args.types_file)

    with open(args.batch_config, "r") as f:
        batch_config = json.load(f)

    results = run_extraction(
        model_path=args.model_path,
        samples=samples,
        batch_config=batch_config,
        type_definitions=type_definitions,
        max_model_len=args.max_model_len,
        prompt_version=args.prompt_version,
    )

    Path(args.output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output_path, "w") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    logger.info("Saved %d results to %s", len(results), args.output_path)


if __name__ == "__main__":
    main()
