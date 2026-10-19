# analysis plan006 zero matrix filter v2

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan006_zero_matrix_filter_v2_20260521T021534_result.json`
- **Structured JSON:** [`abe946c863d88bd215e7.json`](../../sessions/ab/abe946c863d88bd215e7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Both files written.

**Key findings**:
- **12 zero-matrix configs dropped** (API-402 artifacts): all civil_comments non-qwen2.5-7b configs (6), all vast qwen3 (3) + vast deepseek few-shot (2), humaid qwen3 few-shot-5 (1).
- **18 valid configs / 126 scenarios** remain (was 30/210).
- **ASV-unsafe (magnitude): 95/126 = 75.4%** — nearly 2× the previously reported 43.8% (old denominator silently included zero-matrix nulls as "safe").
- **Per-K bias**: K=2 mean|bias%|=0.37 / IV=1.17; K=3 = 0.65 / IV=2.53; K=10 = 0.12 / IV=0.30.
- **Sign flips: 0** across all 126 scenarios.
- **VAST 7B vs others**: qwen2.5-7b mean|bias%|=0.735 vs llama4+deepseek=0.593 (ratio 1.24). 7B-vs-235B comparison **infeasible on VAST** (all qwen3 configs zero-matrix).
- **VAST class-2 recall collapsed everywhere** (0.04–0.25), confirming third-class issue is universal across LLM × prompt.

Outputs:
- `artifacts/plan006_full_filtered_stats.json`
- `artifacts/plan006_full_filtered_stats.txt`

---
