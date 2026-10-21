# deploy bjb1 18228 pi05 table2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb1-18228-pi05-table2_20260526T104814_result.json`
- **Structured JSON:** [`85280fe87c7ef140ab04.json`](../../sessions/85/85280fe87c7ef140ab04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

bjb1-18228 上 4 张 GPU **都不空闲**，每张都有 python 进程占用 10-14GB。Registry 中有 6 个 `pi05-crm-k2-{goal,object}-s{42,43,44}-bjb1-r2` 状态为 RUNNING（最近更新于 2026-05-26 09:52~09:53），很可能就是这些进程。

PIDs：
- GPU 0: PID 2558 (10190 MiB)
- GPU 1: PID 2916 (10190 MiB)
- GPU 2: PID 81928 (13947 MiB)
- GPU 3: PID 3764 (10154 MiB)

需要确认下一步如何处理：
1. **GPU 实际上正在跑前一批 r2 实验**——直接提交会撞 GPU；
2. 你说"全部空闲"可能基于过时信息。

要不要我先检查这 4 个进程对应的 tmux 会话（ssh_execute 调用 `tmux ls`），确认它们就是 r2 实验还是孤儿进程？确认后再决定：等它们结束 / kill 掉 / 改用别的服务器。

---
