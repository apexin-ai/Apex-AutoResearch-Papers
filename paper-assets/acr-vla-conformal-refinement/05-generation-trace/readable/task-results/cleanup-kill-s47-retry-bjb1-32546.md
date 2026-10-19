# cleanup kill s47 retry bjb1 32546

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cleanup_kill-s47-retry-bjb1-32546_20260524T113506_result.json`
- **Structured JSON:** [`3d55e19225e0a69138de.json`](../../sessions/3d/3d55e19225e0a69138de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**已 Kill 的进程**（4 个 Object s47 重试，全部释放）：
- `eval-obj-vla-s47-r2` (cuda:0 实际 device 1) — PID 423228
- `eval-obj-crm-s47-r2` (cuda:2) — PID 424705
- `eval-obj-adapt-s47-r2` (cuda:3) — PID 426329
- `eval-obj-k2mean-s47-r2` (cuda:0) — PID 428027

**GPU 状态**：
- cuda:0/1/2/3 全部释放至 2 MiB ✓
- cuda:4 仍有 1932 MiB — Long s47 reconvla 正常运行（PID 316673，已跑 ~5h）
- cuda:5 空闲（2 MiB）

**与任务描述的差异**：
- 任务描述说 Long s47 CRM 在 cuda:5，实际是 Long s47 **reconvla** 在 **cuda:4**（CUDA_VISIBLE_DEVICES=4）。保留无误。
- 任务描述说 cuda:0 有 A1 baseline，实际 cuda:0 跑的是 Object k2mean s47 重试（属于要 kill 的范围，已 kill）。**未发现任何 A1 baseline 进程**。
- 残留：PID 102924 是 5/24 04:11 的旧 `eval-crm-obj-s46` tmux 父进程僵尸（无对应 python 子进程，不占 GPU），未处理。

---
