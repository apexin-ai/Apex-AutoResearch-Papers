# diag exp034 status cron

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_exp034-status-cron_20260519T042929_result.json`
- **Structured JSON:** [`5b3ac53dd1486658da7b.json`](../../sessions/5b/5b3ac53dd1486658da7b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇报：

**exp-034 状态：正常运行中**
- 进度：**562/600** (93.7%)，剩余 39 题
- ETA：~45 分钟（avg 68.6s/prob）
- tmux session：`exp034_run`，VLLM PID=68846，cuda:1，port 8001
- Cron 监控：**已注册**（120s 间隔）
- Registry 状态：仍为 DEPLOYED（状态机不允许 DEPLOYED→RUNNING 转换），notes 已更新为实际运行状态
- 早期 93 题 partial metrics：SICA=77.42% vs SC=74.19%, delta=+3.23pp（待全量完成后更新）

---
