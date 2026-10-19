# fix kill dup deploy goal44

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-dup-deploy-goal44_20260522T205719_result.json`
- **Structured JSON:** [`e33d3c928d64be102b55.json`](../../sessions/e3/e33d3c928d64be102b55.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。

### 产出汇总

**Part 1 — Kill 重复进程**
- PID 121451（较新的 seed43 重复进程）：已 force kill 确认
- PID 100728（原始 seed43）：继续运行，3h58m elapsed

**Part 2 — goal_seed44 部署**
- tmux session: `eval_goal_seed44`
- PID: **205154**
- GPU 5 占用: 11563 MiB
- 状态: rollout 进行中（300 steps/episode × 20 episodes）
- Registry: `eval-smolvla-lerobot-goal-seed44-v3` → RUNNING
- 监控 cron: 每 12 分钟检查一次（job dfd1e0c2）

注意：用户提供的命令中 `--policy.path=lerobot/smolvla_libero` 是相对路径，实际需要 `/root/autodl-tmp/models/smolvla_libero`（与 seed43 一致），已修正。

---
