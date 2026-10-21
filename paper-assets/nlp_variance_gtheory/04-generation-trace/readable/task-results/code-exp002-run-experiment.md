# code exp002 run experiment

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp002_run_experiment_20260521T080403_result.json`
- **Structured JSON:** [`b90259a4f57b5c58b7ca.json`](../../sessions/b9/b90259a4f57b5c58b7ca.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**79/79 tests passed.** All changes deployed and verified:

### What was done

1. **`src/inference/benchmark_utils.py`** (NEW) — Prompt templates (6 variants each), answer extractors, and scorers for GSM8K, ARC-Challenge, HellaSwag:
   - GSM8K: extracts `#### N` or last number, float comparison scoring, 512 max_tokens for CoT
   - ARC: variable-choice MC with label mapping, letter extraction
   - HellaSwag: 4-choice sentence completion, idx→letter gold mapping

2. **`src/inference/vllm_runner.py`** (MODIFIED) — `generate()` now accepts `max_tokens` parameter (default 16, backward compatible)

3. **`src/inference/run_experiment.py`** (REWRITTEN) — Multi-benchmark support via `--benchmark` flag:
   - `_build_prompt()` routes to correct prompt builder per benchmark
   - `_extract_and_score()` routes to correct extraction/scoring
   - `--items` auto-selects per benchmark if omitted; `--few-shot` only used for MMLU
   - Output adds `benchmark` and `text_exact_match` fields
   - Default `mmlu` — existing exp-001 CLI invocations unchanged

4. **`scripts/dry_run_exp002.py`** (NEW) — CPU-only test covering all extraction/scoring/prompt logic

---
