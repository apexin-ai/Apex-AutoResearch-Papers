# ops check training progress

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-training-progress_20260523T171330_result.json`
- **Structured JSON:** [`c25265ab305f61e5945e.json`](../../sessions/c2/c25265ab305f61e5945e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

状态报告已写入 `artifacts/_project/training_status_20260523.md`。

**要点**：
- 8/8 实验全部存活，GPU 利用率 97-100%
- 最快完成的 2 个：t15_a060_s43 和 t15_a050_s43（~1-1.5h 后）
- 最慢的 2 个：t10_a045_s44 和 t15_a075_s43（~4h 后）
- mauve 指标在 t15_a050_s43 上因网络不可达失败（gpt2-large 下载不了），其他实验可能也有同样问题

---
