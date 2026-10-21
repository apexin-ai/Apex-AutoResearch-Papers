# analysis exp062 cohens d batch4

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp062_cohens_d_batch4_20260521T161907_result.json`
- **Structured JSON:** [`02ea806df4589e68b1d0.json`](../../sessions/02/02ea806df4589e68b1d0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Combo | entropy_mean | entropy_std | entropy_max | entropy_min | tail_decay | TTR | hapax_ratio | Shape | Drift |
|---|---|---|---|---|---|---|---|---|---|
| llama-3.2-3b topk | 0.77 | 0.21 | 0.08 | 0.03 | 0.20 | 0.73 | 0.71 | YES | YES |
| qwen3-0.6b greedy | 0.82 | 0.72 | 0.09 | 0.02 | 0.03 | 0.51 | **0.46** | YES | **NO** |

qwen3-0.6b greedy 的 hapax_ratio=0.46 差 0.04 没过 drift 阈值，是 greedy 策略下首个 drift 未通过的 combo。两个文件均已更新至 12/16 combos。

---
