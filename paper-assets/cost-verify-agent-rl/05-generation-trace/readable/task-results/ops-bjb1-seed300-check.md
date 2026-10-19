# ops bjb1 seed300 check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_seed300_check_20260522T170826_result.json`
- **Structured JSON:** [`244015d51874210ca146.json`](../../sessions/24/244015d51874210ca146.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**seed300 进程存活，正在训练。**

| 项目 | 状态 |
|------|------|
| **进程** | `exp029_seed300_episode` 在 tmux session 中运行，PID 433097 (`ray::TaskRunner.run`, CPU 80.1%)，两个 `ray::WorkerDict` (PID 433306/433307, 各 ~58% CPU) |
| **GPU** | cuda:0 — 45179 MiB used, 0% util; cuda:1 — 45351 MiB used, 0% util（显存占满，GPU util 瞬时为 0 说明当前在 CPU-bound 阶段如 rollout 收集） |
| **训练进度** | **3/5 steps (60%)**, 已跑 1h26m, 预估剩余 ~57min |
| **日志** | 最新时间戳 `2026-05-23 00:41:17`，大量 `Skipping non-numeric metric 'anchor_obs'` 警告（正常，ALFWorld 环境的文本观测被 metric logger 跳过） |
| **wandb** | wandb-core (PID 433602) 在线 |

---
