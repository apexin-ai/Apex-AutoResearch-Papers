# analysis ckpt50 eval results

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ckpt50-eval-results_20260514T181437_result.json`
- **Structured JSON:** [`ce8b6e78b78beaea1326.json`](../../sessions/ce/ce8b6e78b78beaea1326.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 eval 都还在跑，结果尚未写入磁盘：

| Checkpoint | 进度 | 开始时间 | 预计剩余 |
|-----------|------|---------|---------|
| **ckpt-50** | 50/62 batches (81%) | 01:10 | ~15 min |
| **ckpt-10** | 23/62 batches (37%) | 01:43 | ~55 min |
| **ckpt-100** | 4/62 batches (6%) | 02:09 | ~80 min |

checkpoint-50 最快，大约还需 15 分钟完成。结果文件会在 inference 全部跑完后才写入 `eval_metrics.json`。需要等完成后再读取。

---
