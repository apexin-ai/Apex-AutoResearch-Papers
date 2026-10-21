# exp review p0b volume matched

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_review-p0b-volume-matched_20260515T134033_result.json`
- **Structured JSON:** [`d08f47f615b59b4a5d64.json`](../../sessions/d0/d08f47f615b59b4a5d64.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

P0-B 完成。结果：

| 条件 | Avg F1 |
|---|---|
| 5-gen LOGO (原始) | 0.8019 |
| 5-gen volume-matched (3 seed 均值) | 0.8024 |
| 6-gen LOGO (excl qwen3-8b) | 0.8102 |

**分解**：
- Volume effect: **+0.05pp**（将 4-gen train 上采样到 5-gen 等量，几乎无影响）
- Total effect: +0.83pp
- Diversity residual: **+0.78pp**（94% 来自 generator diversity）

结论：加入 Qwen3-8B 带来的 per-generator F1 提升几乎完全来自 generator 多样性，而非数据量增加。脚本 `scripts/review_p0b_volume_matched.py`，结果 `results/review_p0b_volume_matched.json`。

---
