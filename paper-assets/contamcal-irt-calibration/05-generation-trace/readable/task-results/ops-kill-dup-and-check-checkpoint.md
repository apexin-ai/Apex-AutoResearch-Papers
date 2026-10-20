# ops kill dup and check checkpoint

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill-dup-and-check-checkpoint_20260518T172801_result.json`
- **Structured JSON:** [`e829d93c793be6f91f53.json`](../../sessions/e8/e829d93c793be6f91f53.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

匹配到的是 pgrep 命令自身（PID 46821）。d100_s123 无活跃进程。

---

**汇总：**

| 检查项 | 结果 |
|--------|------|
| PID 45613 终止 | **已终止** |
| d025_s123 checkpoint | **安全** — `lora_adapter/` 目录存在但为空（训练未到 save 阶段），无腐败风险。PID 42743 在 cuda:1 正常运行中 |
| cuda:3 状态 | **已空闲** — 0MiB 显存，0% 利用率 |
| d100_s123 目标目录 | **无活跃进程，安全启动** |

四项检查全部通过，cuda:3 可用于 d100_s123 任务。

---
