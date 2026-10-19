# check corr 8b progress

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_corr-8b-progress_20260512T135254_result.json`
- **Structured JSON:** [`0cdaf046763678d08be5.json`](../../sessions/0c/0cdaf046763678d08be5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`screen -ls` 被 read-only 白名单拦截，但 GPU 状态已足够判断。

**corr_8b (correction feasibility test on cuda:1):**
- cuda:1 有两个进程在跑（PID 116110, 116400），各占 7754 MiB — 模型已加载，正在运行
- 刚启动不久：完成 **1/100 episodes**（~21:53 完成第一个）
- 第一个 episode: task=25, look_at_obj, reward=False, 40 steps, 耗时 88.5s
- 日志仅 22 行，处于极早期阶段
- 按 ~90s/episode 估算，100 episodes 约需 **2.5 小时**

**轨迹收集 (cuda:0):**
- `train_part0.jsonl`: **52 条**轨迹已收集

---
