# diag bjb2 28827 gpu0

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_bjb2-28827-gpu0_20260517T225916_result.json`
- **Structured JSON:** [`bb94a6190b0da1974164.json`](../../sessions/bb/bb94a6190b0da1974164.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成，报告已写入 `artifacts/diag_bjb2_28827.md`。

关键发现：
- **GPU 0、5 空闲可用** — GPU 0 的 train-crm-k1-v2 已跑完 50/50 epochs（checkpoint 在 `/root/autodl-tmp/checkpoints/crm_k1/`），GPU 5 的 `mag_perdof_norm02_seed43_r3` 被 SIGKILL 杀死（exit 137）
- **PID 749540 已死亡**，无进程、无 exit file
- **Registry 需更新**：`mag_perdof_norm02_seed43_r3` 实际已 KILLED；`mag_obs_only_norm01_seed47` 和 `mag_obs_only_norm01_seed46` 确认在跑（GPU 1/3）
- GPU 1-4 四个 eval 实验运行中，perdof 两个进度 65-75%，obs_only 两个进度约 30%

---
