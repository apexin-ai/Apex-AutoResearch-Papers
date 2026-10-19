# ops v9d urgent status check

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_v9d_urgent_status_check_20260520T075223_result.json`
- **Structured JSON:** [`1d5f9c89c824357e3ecf.json`](../../sessions/1d/1d5f9c89c824357e3ecf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v9d 状态报告

**结论：v9d 正在正常运行，GPU 利用率 0% 是因为当前处于 PPO 训练阶段（非 inference），属正常现象。**

| 项目 | 状态 |
|------|------|
| **PID 549487** | 存活，运行时间 2h22m54s，状态 `SNl`（sleeping，正常） |
| **GPU 进程** | 4 张 GPU 全部有进程（PID 550057-550060），显存占用 25-28 GB/卡 |
| **GPU 利用率** | 4 卡均 0%——日志显示刚完成 step 10 的 rollout（大量 AlfworldSG warning），正在进入 PPO update 的 `compute_policy_loss` 阶段。利用率瞬间为 0% 是 rollout→training 切换间隙的正常现象 |
| **训练进度** | **37% (11/30 steps)**，已跑 2h13m，预估剩余 ~7h12m |
| **Checkpoint** | step 10 已保存（`latest_checkpointed_iteration.txt` = 10），只含 actor |
| **磁盘** | `/root/autodl-tmp` 176G/250G 使用，剩余 75G (71%)，充足 |
| **verl_logs** | `/root/cost-verify-agent-rl/RAGEN/verl_logs/` 不存在（日志直接写在 `/root/runs/` 下） |

**关键日志**：最后一行是 `Training Progress: 37%|███▋ | 11/30 [2:13:33<7:12:05, 1364.52s/it]`，以及 `compute_policy_loss` 的 FutureWarning（不影响运行）。

Director 看到的 GPU-Util 0% 是采样时正好在 CPU-bound 的 PPO 计算阶段，不是故障。

---
