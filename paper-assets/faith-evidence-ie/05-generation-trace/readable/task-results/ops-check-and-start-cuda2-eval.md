# ops check and start cuda2 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-and-start-cuda2-eval_20260514T180256_result.json`
- **Structured JSON:** [`07b2653be60e2ed854e3.json`](../../sessions/07/07b2653be60e2ed854e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

summary.json 为空。目前状态清楚了：

## 状态报告

**进程状态**: ALIVE
- PID 78850 (bash wrapper) — 运行 20h01m
- PID 78857 (python inference) — 运行 20h01m, cuda:2 占用 9400 MiB

**当前评估**: checkpoint-10, inference 进度 **14/62 batches (23%)**，约每 batch 80s，预计还需 ~64 分钟完成当前 checkpoint

**Checkpoint 进度**:

| Checkpoint | 状态 |
|---|---|
| 10 | **进行中** (23%) |
| 20 | PENDING |
| 30 | PENDING |
| 40 | PENDING |
| 50 | 目录已存在但空（前次可能失败） |
| 60 | PENDING |
| 70 | PENDING |
| 80 | PENDING |

**注意**: 20 小时只跑到 checkpoint-10 的 23%，速度异常慢。从日志看 01:43 才开始加载 checkpoint-10（距提交约 19h），之前可能卡在排队或 checkpoint-50 的失败尝试上。按当前速度（~80s/batch, 62 batches/checkpoint），单个 checkpoint inference 约 83 分钟，7 个 checkpoint 还需 ~9-10 小时（不含 scoring 时间）。

---
