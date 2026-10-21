# ops submit cuda1 next task

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_submit_cuda1_next_task_20260516T123157_result.json`
- **Structured JSON:** [`5ac23efd18d0cc9704ce.json`](../../sessions/5a/5ac23efd18d0cc9704ce.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

启动成功。

**结果：**

| 项目 | 状态 |
|------|------|
| 任务 | **0.5B-Instruct signals**（mmlu × gsm8k × arc_challenge × s1/s2/s4 = 9 tasks） |
| 原因 | 优先级1（1.5B d005_s123）由 cuda:0 batch 覆盖；优先级2（3B d005/d025 s123）信号已完成；3B d100_s123 alpha=16 被 C006 禁止；Instruct eval 是唯一可用回退 |
| PID | **779116** |
| GPU | cuda:1（585 MiB 已占用，正在运行 S1 embedding 编码） |
| 日志 | `/tmp/05B_instruct_signals.log` |
| 进度 | S1 × mmlu 进行中（1017/6250 batches，~45 it/s） |

---
