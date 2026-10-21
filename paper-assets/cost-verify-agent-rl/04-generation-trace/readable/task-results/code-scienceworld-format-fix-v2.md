# code scienceworld format fix v2

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_scienceworld-format-fix-v2_20260519T122222_result.json`
- **Structured JSON:** [`451b2bc4354dc8fb588d.json`](../../sessions/45/451b2bc4354dc8fb588d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程运行中（PID 51279）。已完成 boil 任务（14 train + 5 val = 19 条），正在处理后续 task。

**总结**：

三处修改已完成并重跑：

| 修改 | 内容 |
|------|------|
| Fix 1 | 第一轮格式从 `Task:\n\nState:\n{obs}` 改为 `State:\nTask: {desc}\n{obs}`（Task 移入 State 内部） |
| Fix 2a | 中间步 reward 从 `{cumulative_score}` (递增分数) 改为 `0.0` (sparse) |
| Fix 2b | 终局步追加 `Reward:\n10.0\n` 用户消息 |

旧进程（23069/23079）已 kill，新进程 51279 运行中。Whitelist 有 26 tasks / 3612 variations。

---
