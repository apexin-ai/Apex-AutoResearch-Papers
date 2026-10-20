# eval grid b3 0 b5 0 seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_grid_b3_0_b5_0_seed456_20260515T093346_result.json`
- **Structured JSON:** [`613970f51099fd663f33.json`](../../sessions/61/613970f51099fd663f33.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。两个实验的 post-hoc eval 结果：

| 实验 | eval_ppl | eval_loss | tokens | train_loss (registry) | total_steps |
|------|----------|-----------|--------|-----------------------|-------------|
| **grid_b3_0_seed456** | **17.921** | **2.886** | 4,077,068 | 5.435 | 6,103 |
| **grid_b5_0_seed456** | **17.993** | **2.890** | 4,077,068 | 5.488 | 6,103 |

Registry 已有完整 metrics，status=DONE，conclusion=success，无需额外更新。eval_results.json 已保存到各自的模型目录。

趋势符合预期：随着 b 增大（更激进的下加权），eval_ppl 轻微上升（b3→17.92, b5→17.99），与 b0.5→b2.0 的趋势一致。

---
