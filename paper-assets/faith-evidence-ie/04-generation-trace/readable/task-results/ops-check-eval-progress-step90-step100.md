# ops check eval progress step90 step100

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-progress-step90-step100_20260514T184613_result.json`
- **Structured JSON:** [`1509f173bbcee1e79830.json`](../../sessions/15/1509f173bbcee1e79830.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 进度

| GPU | Eval | PID | 存活 | 进度 (batches) | 预计剩余 |
|-----|------|-----|------|---------------|---------|
| cuda:0 | step-100 | 80789 | Y | 26/62 | ~50 min |
| cuda:1 | step-90 | 83207 | Y | 9/62 | ~72 min |
| cuda:2 | multi | 78857 | Y | 45/62 | ~21 min |
| cuda:3 | high | 81962 | Y | 22/62 | ~51 min |

4 个 GPU 全部在跑，利用率 69-83%，每个 ~9-10 GB 显存。

**已完成的 checkpoint 结果**: 无。checkpoint-90 和 checkpoint-100 的输出目录已创建但为空（inference 尚未完成）。

**预计完成时间**:
- multi (cuda:2) 最先完成，约 21 min 后
- step-100 (cuda:0) 约 50 min 后
- high (cuda:3) 约 51 min 后
- step-90 (cuda:1) 最晚，约 72 min 后（刚启动 ~14 min）

---
