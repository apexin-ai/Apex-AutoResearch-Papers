# Communication Function Analysis and Pruning in Multi-Agent LLM Systems

This repository contains the code, taxonomy, and sample data for reproducing the
experiments in "When the Most Disruptive Messages Are Safe to Prune in Aggregate:
Functional Analysis of Communication Pruning in Two-Agent LLM Systems."

## Overview

We provide a five-class taxonomy of communication functions in LLM-based
multi-agent systems and an empirical pruning validation pipeline. The taxonomy
classifies inter-agent messages into: **acknowledgment**, **information_provision**,
**reasoning_guidance**, **verification**, and **coordination**. The pipeline
evaluates whether messages of a given type can be safely removed without
degrading task accuracy, using McNemar's exact test, TOST equivalence testing,
and non-inferiority confidence intervals.

## Repository Structure

```
code_release/
├── README.md                              # This file
├── taxonomy/
│   ├── schema.json                        # 5-class taxonomy definition with examples and decision rules
│   └── annotation_prompt.txt              # Full GPT-4o annotation prompt (math domain)
├── pipeline/
│   ├── functional_annotation.py           # LLM-based message annotation pipeline
│   └── pruning_validation.py              # Core pruning evaluation (offline simulation + online)
├── statistics/
│   └── statistical_tests.py               # McNemar, TOST, non-inferiority, BH correction, power analysis
├── configs/
│   └── experiment_config.yaml             # Example experiment configuration
└── data/
    └── sample_traces/
        └── gsm8k_qwen_20.json            # 20 annotated GSM8K traces (Qwen2.5-7B, oracle labels)
```

## Dependencies

- Python >= 3.10
- Core: `numpy`, `scipy >= 1.10`, `pyyaml`
- Annotation pipeline: `openai >= 1.0` (OpenAI-compatible API client)
- Online pruning: `openai >= 1.0` + running vLLM instance with backbone model
- Optional: `ag2 >= 0.8` (for AG2-based end-to-end experiments), `datasets` (for loading benchmarks)

Install:
```bash
pip install numpy scipy pyyaml openai
```

## Quick Start

### 1. Functional Annotation

Annotate inter-agent messages with the 5-class taxonomy:

```bash
# Using GPT-4o (recommended for reproducing paper results)
python pipeline/functional_annotation.py \
    --traces data/traces.jsonl \
    --output annotations.jsonl \
    --model gpt-4o \
    --task-domain math

# Cross-model annotation for inter-annotator agreement
python pipeline/functional_annotation.py \
    --traces data/traces.jsonl \
    --output annotations.jsonl \
    --model gpt-4o \
    --cross-model \
    --model-b-base http://localhost:8001/v1 \
    --model-b-name Qwen/Qwen2.5-7B-Instruct
```

**Input format** (traces JSONL): each line is a JSON object:
```json
{
    "task_id": "gsm8k_0000",
    "question": "...",
    "ground_truth": "42",
    "messages": [
        {"sender": "solver", "receiver": "checker", "content": "...", "round": 0},
        {"sender": "checker", "receiver": "solver", "content": "...", "round": 1}
    ]
}
```

**Output format** (annotations JSONL): each line contains the classification:
```json
{
    "task_id": "gsm8k_0000",
    "message_index": 0,
    "annotation": {"type": "acknowledgment", "confidence": 0.9, "reasoning": "..."}
}
```

### 2. Offline Pruning Simulation

Evaluate pruning safety by removing messages from pre-recorded traces:

```bash
python pipeline/pruning_validation.py simulate \
    --traces data/traces.jsonl \
    --annotations annotations.jsonl \
    --output results.json \
    --domain gsm8k \
    --random-trials 10
```

This removes messages of each function type and re-extracts answers from the
remaining messages. Compares against a random pruning baseline at matched
suppression rate.

### 3. Statistical Tests

Run the full test battery on pruning results:

```bash
python statistics/statistical_tests.py \
    --results outputs/oracle_results.json \
    --equivalence-margin 1.0 \
    --non-inferiority-delta -3.0 \
    --output stats.json
```

**Programmatic usage:**

```python
from statistics.statistical_tests import compute_all_tests, benjamini_hochberg

baseline = [True, True, False, True, ...]   # per-task correctness
pruned = [True, True, True, True, ...]

results = compute_all_tests(baseline, pruned, label="ack_pruning")
print(f"McNemar p={results['mcnemar']['p_value']}")
print(f"TOST p={results['tost']['p_tost']}")
print(f"95% CI: {results['ci_95_pp']}")

# Multiple comparison correction
p_values = [0.34, 0.013, 0.50, 0.007]
adjusted = benjamini_hochberg(p_values, alpha=0.05)
```

### 4. Sample Data

`data/sample_traces/gsm8k_qwen_20.json` contains 20 GSM8K tasks with
oracle pruning results from Qwen2.5-7B-Instruct. Each trace includes
per-round oracle decisions with binary ack labels, confidence scores,
and 5-class function types.

## Online Pruning (GPU Required)

Online pruning requires:
1. A running vLLM server serving the backbone model (e.g., Qwen2.5-7B-Instruct)
2. An OpenAI API key for oracle classification (GPT-4o)

```bash
# Start vLLM server
vllm serve Qwen/Qwen2.5-7B-Instruct --port 8000

# Run online pruning (see pruning_validation.py for the API)
```

The online pipeline generates each agent response via the LLM, classifies it
in real-time using the oracle, and withholds detected acknowledgments from
the conversation context before the next agent generates its response.

## Reproducing Paper Results

The paper's primary results use:
- **Backbones**: Qwen2.5-7B-Instruct, Llama-3.1-8B-Instruct
- **Oracle**: GPT-4o (temperature=0) for 5-class functional annotation
- **Benchmarks**: GSM8K (N=500), StrategyQA (N=500), ARC-Challenge (N=250)
- **Decoding**: Greedy (temperature=0, top_p=1.0)
- **Topology**: Two-agent round-robin, 5 rounds per task
- **Statistical tests**: McNemar exact (primary), TOST at +/-1pp, non-inferiority at -3pp

## License

Code is released under the MIT License. GSM8K is MIT-licensed.
Model weights are subject to their respective licenses.
