# research baseline data consolidation

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_baseline-data-consolidation_20260516T044123_result.json`
- **Structured JSON:** [`ae26e486e2d1f716a51d.json`](../../sessions/ae/ae26e486e2d1f716a51d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/baseline_eval_results.md`。

关键数据：

| Model | Spatial | Object | Goal | Average |
|-------|---------|--------|------|---------|
| SmolVLA (std) | 66.0±8.4 | 67.8±4.2 | 76.4±4.4 | 70.1 |
| SmolVLA+ (plus) | 81.6±6.0 | 88.8±2.6 | 87.8±4.0 | 86.1 |

LIBERO-10 两个模型的 eval_info.json 均未生成，评测仍在进行中。notable 发现：std 的 spatial task_5 成功率为 0%，plus 也仅 32%，是最难的 task。

---
