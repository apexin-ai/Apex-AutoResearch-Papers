# analysis full trace seed42 v5

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_full_trace_seed42_v5_20260515T035938_result.json`
- **Structured JSON:** [`ffc2ed588f1a5f0d35e5.json`](../../sessions/ff/ffc2ed588f1a5f0d35e5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

---

## full_trace_seed42_v5 — **SUCCESS**

| Metric | full_trace v5 | no_trace v4 (baseline) | vota v4 | full_trace v2 |
|--------|:---:|:---:|:---:|:---:|
| **Accuracy** | **81.76%** | 75.13% | 95.63% | 28.4% |
| Pass F1 | 0.872 | 0.813 | 0.970 | 0.155 |
| Fail F1 | 0.685 | 0.627 | 0.917 | 0.568 |
| Train loss | 0.042 | 0.180 | 0.046 | 0.037 |
| Eval loss | 0.084 | 0.645 | 0.084 | 0.082 |

**Lift vs no_trace baseline: +6.63pp** (conservative CI: [+4.5pp, +8.8pp], excludes 0)

**Findings:**
1. v5 chat template fix **completely resolved the v2 collapse** (28.4% → 81.8%) — the hypothesis that label truncation from chat template overhead was causing the collapse is confirmed.
2. Full trace provides **significant lift over no_trace** (+6.63pp), passing MVP criteria (≥2pp + CI excludes 0).
3. However, **VOTA still dominates** full trace by a wide margin (95.6% vs 81.8%, ~14pp gap). The full execution trace is too noisy/long compared to VOTA's distilled signal.

---
