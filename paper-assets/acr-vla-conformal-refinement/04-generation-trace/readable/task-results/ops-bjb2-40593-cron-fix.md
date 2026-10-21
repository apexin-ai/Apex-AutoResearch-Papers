# ops bjb2 40593 cron fix

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb2-40593-cron-fix_20260515T052900_result.json`
- **Structured JSON:** [`c6a9ed3191eb458b8f46.json`](../../sessions/c6/c6a9ed3191eb458b8f46.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验已重启，正在加载环境。模型和 CRM checkpoint 已加载，10 个 task 正在初始化。

## 汇报

**实际情况**：registry 中的两个条目并非两个独立实验。`eval-mag-obsonly-norm003`（pid 225144）是 `eval-mag-obsonly-norm003-b2`（pid 225139）的子 python 进程。两个 PID 同时启动（etime 均为 08:36），kill 子进程导致父 wrapper 一并退出。

**处理结果**：

| 实验 | 状态 | 说明 |
|------|------|------|
| eval-mag-obsonly-norm003 | DONE / killed | 幻影条目，指向 b2 的子进程 |
| eval-mag-obsonly-norm003-b2 | RUNNING | 已重启，新 wrapper pid **227426**，python pid **227434** |

**当前进度**：刚重启，模型加载完成（SmolVLA + CRM 327K params），正在初始化 10 个 spatial task 的评估环境。尚无 task 完成。

**Cron 监控**：已注册，每小时 :13 检查一次（session-only，job ID `22b5c456`，7天自动过期）。

---
