# ops check eval step100 step90 progress

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-eval-step100-step90-progress_20260514T193424_result.json`
- **Structured JSON:** [`555401351450d464b5fe.json`](../../sessions/55/555401351450d464b5fe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Eval 状态汇报

### Step-100 eval (PID 80789, cuda:0)
- **状态**: 运行中，elapsed 1h26m
- **进度**: **98%** (61/62 batches)，正在处理最后 1 个 batch
- **预计剩余**: ~1-2 分钟完成 inference，之后还有 metrics 计算
- 输出目录 `checkpoint-100/` 目前为空（inference 完成后才写入）

### Step-90 eval (PID 83207, cuda:1)
- **状态**: 运行中，elapsed 1h02m
- **进度**: **73%** (45/62 batches)
- **预计剩余**: ~22 分钟完成 inference + metrics 计算
- 输出目录 `checkpoint-90/` 目前为空

### GPU 使用情况

| GPU | 显存占用 | 利用率 |
|-----|---------|--------|
| 0 | 11,243 / 32,607 MiB (34%) | 55% |
| 1 | 10,005 / 32,607 MiB (31%) | 68% |
| 2 | 8,773 / 32,607 MiB (27%) | 56% |
| 3 | 11,157 / 32,607 MiB (34%) | 74% |

GPU 2/3 也有显存占用和计算负载，可能有其他任务在跑。两个 eval 均正常推进中，step-100 即将完成。

---
