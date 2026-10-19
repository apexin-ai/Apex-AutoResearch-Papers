# check replay running

**error diag dpo recovery** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_replay-running_20260512T140313_result.json`
- **Structured JSON:** [`20db192606487dc4f757.json`](../../sessions/20/20db192606487dc4f757.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总：

**1. GPU 状态**
- GPU 1 上有进程 PID 117225，占用 7754 MiB — **replay 版本正在运行**

**2. Replay 日志 (`feasibility_8b_replay.log`)**
- 已完成 **6/10 episodes**（Attempt 1，共 10 个 target），仍在运行中
- 日志**有** `replay` 和 `corr` 字段（如 `replay=21 corr=19`），但字段名是 `replay` 和 `corr`，不是 `replay_steps` / `correction_steps`
- 所有 episode 的 `replay_ok=False` — replay 阶段本身就失败了
- **0 个成功 episode**，全部 FAILED，sr=0/6
- 尚无 `feasibility_8b_replay.json` 输出文件（未完成）

**3. 原版日志 (`feasibility_8b.log`)**
- 也在运行中，4/100 episodes 完成，同样 sr=0/4，全部 reward=False

**4. 目录内容**
- `feasibility_14b.json` + `.log` — 已完成
- `feasibility_8b.json` + `.log` — 进行中
- `feasibility_8b_replay.log` — 进行中，无 json 输出

**关键结论**：replay 版本在跑，但所有 episode 的 replay 阶段就已失败（`replay_ok=False`），意味着模型在 replay 原始轨迹时就偏离了，correction 阶段虽然执行了（corr 步数 19-35），但起点已经不对，全部失败。

---
