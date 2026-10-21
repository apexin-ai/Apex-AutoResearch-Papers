# diag eval vla only object seed48

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_eval-vla-only-object-seed48_20260519T234612_result.json`
- **Structured JSON:** [`144e3491bdb99d826450.json`](../../sessions/14/144e3491bdb99d826450.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断报告

### 结论：实验实际已成功完成，不是真正的失败

日志和输出文件均显示实验已正常跑完全部 10 个任务 × 10 rollouts = 100 次评估。

**根因：监控系统误判。** 实验进程在监控系统检测窗口外正常退出（进程完成后自然消失），被误判为"process dead"。没有 sentinel 文件或 W&B 上报，因此监控系统在 5 次检测不到进程后自动标记为失败。

### 关键证据

- **输出文件** `logs/eval_object_vla_only_seed48.json` 存在（1485字节，时间戳 May 20 07:36）
- **日志文件** `logs/eval_object_vla_only_seed48.log` 完整，末尾打印了最终结果：`Overall success rate (vla_only): 10.0% (10/100)` 并显示 `Results saved to logs/eval_object_vla_only_seed48.json`
- **无报错**，无 OOM、无 CUDA error、无 crash traceback

### 实验结果
- 模式: vla_only, benchmark: object, seed: 48, K=1
- 总体成功率: **10.0%** (10/100)
- 各任务成功率范围: 0%–30%

### 服务器当前状态
- **磁盘**: 根分区 30G 中已用 8.9G（30%），可用 22G — 磁盘充足，之前报告的 89% 已不适用
- **GPU**: RTX 4090D, 0MiB 占用, 0% 利用率 — 空闲
- **进程**: 无 Python 实验进程残留

### 是否需要重试
**不需要。** 实验已成功完成，结果已保存。需要做的是将此实验的状态从"failed"更正为"completed"，并采集已有结果。

---
