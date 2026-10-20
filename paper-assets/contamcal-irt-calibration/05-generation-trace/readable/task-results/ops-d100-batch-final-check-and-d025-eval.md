# ops d100 batch final check and d025 eval

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d100-batch-final-check-and-d025-eval_20260516T072914_result.json`
- **Structured JSON:** [`5da130e1c2841999f79e.json`](../../sessions/5d/5da130e1c2841999f79e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Done. Here's the summary:

## Part A: d100_s42_a32_batch — RESOLVED ✓

Both aligned and para_aligned evals completed successfully (`.done` markers present):

| Benchmark | Aligned | Para_aligned |
|-----------|---------|--------------|
| MMLU | 0.6364 (8937/14042) | 0.6674 (4402/6596) |
| GSM8K | 0.7036 (928/1319) | 0.5702 (130/228) |
| ARC-Challenge | 0.8208 (962/1172) | 0.8106 (565/697) |
| HumanEval | 26/164 correct | 2/26 correct |

Registry updated: conclusion → success, metrics added, failure_reason → RESOLVED.

## Part B: d025_s42 aligned eval — ALREADY COMPLETE

`Qwen2.5-3B_d025_v3_s42_aligned/` already exists with `.done` marker (completed 2026-05-16 10:33). This is the alpha=32 checkpoint (confirmed lora_alpha=32 in adapter_config.json). Metrics:

| Benchmark | Accuracy |
|-----------|----------|
| MMLU | 0.6242 (8765/14042) |
| GSM8K | 0.6823 (900/1319) |
| ARC-Challenge | 0.8225 (964/1172) |

**No submission needed** — the d025 s42 alpha=32 aligned eval was already completed using the `d025_v3_s42` checkpoint.

Note: The `d025_a32_s42` checkpoint training failed (stalled at 207/3384 steps, lora_adapter empty). But `d025_v3_s42` is the same experiment (alpha=32 retrained) and its eval is done.

---
