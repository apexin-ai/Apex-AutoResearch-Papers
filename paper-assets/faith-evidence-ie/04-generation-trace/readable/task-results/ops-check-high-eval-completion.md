# ops check high eval completion

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-high-eval-completion_20260514T194540_result.json`
- **Structured JSON:** [`654ee538ad5ebce7f90b.json`](../../sessions/65/654ee538ad5ebce7f90b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 完成状态：1/4 checkpoint 完成，进程已挂

| Checkpoint | 状态 |
|-----------|------|
| 60 | ✅ 完成 |
| 70 | ❌ 推理到 8% (5/62 batch) 时进程死亡，目录为空 |
| 80 | ❌ 目录不存在 |
| 90 | ❌ 目录为空 |

进程 81962 已不存在。日志在 checkpoint-70 推理 8% 处中断，无错误信息——可能是 OOM 或被 kill。

### checkpoint-60 metrics

| 指标 | 值 |
|------|-----|
| F1 | 0.1467 |
| Ign-F1 | 0.1467 |
| Precision | 0.1909 |
| Recall | 0.1192 |
| Evi-F1 | 0.5763 |
| EDCR | 0.9062 |
| Predictions | 10041 (gold: 12151) |
| Format OK | 985/985 (100%) |
| Truncated | 16/985 |
| Inference time | 4849s (~81 min) |

### summary.json

只包含之前运行的 checkpoint-50（F1=0.1563, Evi-F1=0.5643, EDCR=0.8858），checkpoint-60 未被写入 summary。

### cuda:3

9503 MiB 占用, 65% 利用率——仍被其他进程占用，未释放。

---
