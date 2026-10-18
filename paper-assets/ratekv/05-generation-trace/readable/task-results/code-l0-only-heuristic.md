# code l0 only heuristic

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_l0_only_heuristic_20260514T061550_result.json`
- **Structured JSON:** [`82969d9795497a6f19aa.json`](../../sessions/82/82969d9795497a6f19aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job running — Qwen2.5-7B is loaded and evaluation is in progress. The script will:

1. **Qwen2.5-7B** (112 heads): baseline → uniform 4-bit → L0-A (ratio=0.2589) → L0-B (ratio=0.2500)
2. **Llama-3.1-8B** (256 heads): same 4 evals
3. **Mistral-7B-v0.3** (256 heads): same 4 evals

Each model takes ~50s per eval × 4 evals = ~3.5min, total ~12min for all 3 models. Results will be saved to `l0_heuristic_results.json`.

Key comparisons this run produces:
- **Variant A** (L0@8bit, rest@4bit) — budget-relaxed — vs MCKP hires numbers
- **Variant B** (L0@8bit, deepest@2bit, rest@4bit) — budget-matched at 0.25 — the apples-to-apples comparison against MCKP

---
