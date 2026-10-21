"""Multi-sample inference module for structured IE with vLLM + XGrammar constrained decoding.

Provides VLLMSampler for batch sampling, prompt construction for UIE tasks,
and a full pipeline that produces SampledInstance dicts.
"""

from __future__ import annotations

import json
import os
from typing import Any


# ---------------------------------------------------------------------------
# UIE JSON schema for XGrammar constrained decoding
# ---------------------------------------------------------------------------

UIE_JSON_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "entities": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "text": {"type": "string"},
                    "type": {"type": "string"},
                    "start": {"type": "integer"},
                    "end": {"type": "integer"},
                },
                "required": ["text", "type", "start", "end"],
            },
        },
        "relations": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "head": {"type": "string"},
                    "tail": {"type": "string"},
                    "type": {"type": "string"},
                    "head_start": {"type": "integer"},
                    "head_end": {"type": "integer"},
                    "tail_start": {"type": "integer"},
                    "tail_end": {"type": "integer"},
                },
                "required": ["head", "tail", "type", "head_start", "head_end",
                             "tail_start", "tail_end"],
            },
        },
        "events": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "trigger": {
                        "type": "object",
                        "properties": {
                            "text": {"type": "string"},
                            "type": {"type": "string"},
                            "start": {"type": "integer"},
                            "end": {"type": "integer"},
                        },
                        "required": ["text", "type", "start", "end"],
                    },
                    "arguments": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "text": {"type": "string"},
                                "role": {"type": "string"},
                                "start": {"type": "integer"},
                                "end": {"type": "integer"},
                            },
                            "required": ["text", "role", "start", "end"],
                        },
                    },
                },
                "required": ["trigger", "arguments"],
            },
        },
    },
    "required": ["entities", "relations", "events"],
}

_EMPTY_EXTRACTION: dict[str, list] = {"entities": [], "relations": [], "events": []}


# ---------------------------------------------------------------------------
# VLLMSampler
# ---------------------------------------------------------------------------

class VLLMSampler:
    """Batch sampler backed by vLLM with optional XGrammar JSON constrained decoding."""

    def __init__(
        self,
        model_path: str,
        tensor_parallel_size: int = 1,
        max_model_len: int = 4096,
        gpu_memory_utilization: float = 0.90,
    ):
        """Initialise the vLLM engine.

        Args:
            model_path: Path to the HuggingFace model (local or hub id).
            tensor_parallel_size: Number of GPUs for tensor parallelism.
            max_model_len: Maximum sequence length.
            gpu_memory_utilization: Fraction of GPU memory to reserve.
        """
        from vllm import LLM

        self.llm = LLM(
            model=model_path,
            tensor_parallel_size=tensor_parallel_size,
            max_model_len=max_model_len,
            gpu_memory_utilization=gpu_memory_utilization,
        )

    def sample(
        self,
        prompts: list[str],
        n_samples: int = 8,
        temperature: float = 1.0,
        max_tokens: int = 1024,
        use_grammar: bool = True,
    ) -> list[list[str]]:
        """Sample *n_samples* completions for each prompt.

        Args:
            prompts: Input prompt strings.
            n_samples: Number of independent samples per prompt.
            temperature: Sampling temperature (0 = greedy).
            max_tokens: Maximum generated tokens per sample.
            use_grammar: If True, enable XGrammar JSON constrained decoding.

        Returns:
            Nested list of shape [len(prompts)][n_samples] containing raw output strings.
        """
        from vllm import SamplingParams
        from vllm.sampling_params import GuidedDecodingParams

        guided_params = GuidedDecodingParams(json=UIE_JSON_SCHEMA) if use_grammar else None

        params = SamplingParams(
            n=n_samples,
            temperature=temperature,
            max_tokens=max_tokens,
            guided_decoding=guided_params,
        )

        request_outputs = self.llm.generate(prompts, params)

        results: list[list[str]] = []
        for req_out in request_outputs:
            results.append([out.text for out in req_out.outputs])
        return results


# ---------------------------------------------------------------------------
# Prompt construction
# ---------------------------------------------------------------------------

_NER_TEMPLATE = (
    "Extract named entities from the following text. "
    "Output a JSON object with the fields: entities, relations, events.\n\n"
    "Text: {text}\n"
    "{schema_line}"
    "\nOutput format: "
    '{{"entities": [{{"text": "...", "type": "...", "start": <int>, "end": <int>}}], '
    '"relations": [], "events": []}}'
)

_EAE_TEMPLATE = (
    "Extract events (triggers and arguments) from the following text. "
    "Output a JSON object with the fields: entities, relations, events.\n\n"
    "Text: {text}\n"
    "{schema_line}"
    "\nOutput format: "
    '{{"entities": [], "relations": [], '
    '"events": [{{"trigger": {{"text": "...", "type": "...", "start": <int>, "end": <int>}}, '
    '"arguments": [{{"text": "...", "role": "...", "start": <int>, "end": <int>}}]}}]}}'
)

_FULL_TEMPLATE = (
    "Extract all structured information (entities, relations, events) from the following text. "
    "Output a JSON object with the fields: entities, relations, events.\n\n"
    "Text: {text}\n"
    "{schema_line}"
    "\nOutput:"
)


def build_uie_prompt(text: str, subtask: str = "ner", schema_hint: str = "") -> str:
    """Build a UIE extraction prompt.

    Args:
        text: Input sentence / passage.
        subtask: "ner" (entities only), "eae" (events), or "full" (all).
        schema_hint: Optional schema description (e.g. entity type list).

    Returns:
        Formatted prompt string.
    """
    schema_line = f"Schema: {schema_hint}\n" if schema_hint else ""

    if subtask == "ner":
        template = _NER_TEMPLATE
    elif subtask == "eae":
        template = _EAE_TEMPLATE
    elif subtask == "full":
        template = _FULL_TEMPLATE
    else:
        raise ValueError(f"subtask must be 'ner', 'eae', or 'full', got '{subtask}'")

    return template.format(text=text, schema_line=schema_line)


# ---------------------------------------------------------------------------
# Output parsing
# ---------------------------------------------------------------------------

def parse_extraction_output(raw_output: str) -> dict[str, Any]:
    """Parse a model output string into an Extraction dict.

    Handles JSON parsing (XGrammar guarantees valid JSON, but we still guard),
    field validation, and type coercion for start/end.

    Args:
        raw_output: Raw model completion text.

    Returns:
        Extraction dict with keys entities, relations, events.
    """
    raw = raw_output.strip()
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        # Attempt to extract the first JSON object from the string
        start = raw.find("{")
        end = raw.rfind("}")
        if start != -1 and end != -1 and end > start:
            try:
                data = json.loads(raw[start:end + 1])
            except json.JSONDecodeError:
                return dict(_EMPTY_EXTRACTION)
        else:
            return dict(_EMPTY_EXTRACTION)

    if not isinstance(data, dict):
        return dict(_EMPTY_EXTRACTION)

    entities = _validate_entities(data.get("entities", []))
    relations = _validate_relations(data.get("relations", []))
    events = _validate_events(data.get("events", []))

    return {"entities": entities, "relations": relations, "events": events}


def _validate_entities(raw: Any) -> list[dict]:
    if not isinstance(raw, list):
        return []
    validated = []
    for e in raw:
        if not isinstance(e, dict):
            continue
        try:
            validated.append({
                "text": str(e["text"]),
                "type": str(e["type"]),
                "start": int(e["start"]),
                "end": int(e["end"]),
            })
        except (KeyError, ValueError, TypeError):
            continue
    return validated


def _validate_relations(raw: Any) -> list[dict]:
    if not isinstance(raw, list):
        return []
    validated = []
    for r in raw:
        if not isinstance(r, dict):
            continue
        try:
            validated.append({
                "head": str(r["head"]),
                "tail": str(r["tail"]),
                "type": str(r["type"]),
                "head_start": int(r["head_start"]),
                "head_end": int(r["head_end"]),
                "tail_start": int(r["tail_start"]),
                "tail_end": int(r["tail_end"]),
            })
        except (KeyError, ValueError, TypeError):
            continue
    return validated


def _validate_events(raw: Any) -> list[dict]:
    if not isinstance(raw, list):
        return []
    validated = []
    for ev in raw:
        if not isinstance(ev, dict):
            continue
        trigger_raw = ev.get("trigger")
        if not isinstance(trigger_raw, dict):
            continue
        try:
            trigger = {
                "text": str(trigger_raw["text"]),
                "type": str(trigger_raw["type"]),
                "start": int(trigger_raw["start"]),
                "end": int(trigger_raw["end"]),
            }
        except (KeyError, ValueError, TypeError):
            continue
        arguments = []
        for arg in ev.get("arguments", []):
            if not isinstance(arg, dict):
                continue
            try:
                arguments.append({
                    "text": str(arg["text"]),
                    "role": str(arg["role"]),
                    "start": int(arg["start"]),
                    "end": int(arg["end"]),
                })
            except (KeyError, ValueError, TypeError):
                continue
        validated.append({"trigger": trigger, "arguments": arguments})
    return validated


# ---------------------------------------------------------------------------
# Batch sampling pipeline
# ---------------------------------------------------------------------------

def run_sampling_pipeline(
    sampler: VLLMSampler,
    instances: list[dict],
    n_samples: int = 8,
    temperature: float = 1.0,
    max_tokens: int = 1024,
    subtask: str = "ner",
    schema_hint: str = "",
    use_grammar: bool = True,
    output_path: str | None = None,
) -> list[dict]:
    """Full sampling pipeline: build prompts -> batch sample -> parse -> save.

    Also performs a single greedy decoding pass (temperature=0, n=1) as baseline.

    Args:
        sampler: Initialised VLLMSampler.
        instances: Instance dicts from data_utils (must have "id", "text", and gold fields).
        n_samples: Number of stochastic samples per instance.
        temperature: Sampling temperature for stochastic samples.
        max_tokens: Maximum generated tokens.
        subtask: "ner", "eae", or "full".
        schema_hint: Optional schema description.
        use_grammar: Whether to use XGrammar constrained decoding.
        output_path: If provided, save results to this JSONL path.

    Returns:
        List of SampledInstance dicts.
    """
    prompts = [build_uie_prompt(inst["text"], subtask=subtask, schema_hint=schema_hint)
               for inst in instances]

    # Stochastic sampling
    raw_samples = sampler.sample(
        prompts,
        n_samples=n_samples,
        temperature=temperature,
        max_tokens=max_tokens,
        use_grammar=use_grammar,
    )

    # Greedy decoding
    raw_greedy = sampler.sample(
        prompts,
        n_samples=1,
        temperature=0.0,
        max_tokens=max_tokens,
        use_grammar=use_grammar,
    )

    # Assemble SampledInstance list
    sampled_instances: list[dict] = []
    for idx, inst in enumerate(instances):
        gold = {
            "entities": inst.get("entities", []),
            "relations": inst.get("relations", []),
            "events": inst.get("events", []),
        }
        parsed_samples = [parse_extraction_output(s) for s in raw_samples[idx]]
        parsed_greedy = parse_extraction_output(raw_greedy[idx][0])

        sampled_instances.append({
            "id": inst.get("id", str(idx)),
            "text": inst["text"],
            "gold": gold,
            "samples": parsed_samples,
            "greedy": parsed_greedy,
        })

    if output_path:
        save_sampled_results(sampled_instances, output_path)

    return sampled_instances


# ---------------------------------------------------------------------------
# I/O helpers
# ---------------------------------------------------------------------------

def save_sampled_results(sampled: list[dict], path: str) -> None:
    """Save sampled results as JSONL.

    Args:
        sampled: List of SampledInstance dicts.
        path: Output file path.
    """
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for inst in sampled:
            f.write(json.dumps(inst, ensure_ascii=False) + "\n")


def load_sampled_results(path: str) -> list[dict]:
    """Load sampled results from a JSONL file.

    Args:
        path: Path to a JSONL file of SampledInstance dicts.

    Returns:
        List of SampledInstance dicts.
    """
    instances = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                instances.append(json.loads(line))
    return instances
