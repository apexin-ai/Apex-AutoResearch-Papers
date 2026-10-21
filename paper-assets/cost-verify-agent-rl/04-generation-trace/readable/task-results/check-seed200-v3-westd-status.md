# check seed200 v3 westd status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_seed200_v3_westd_status_20260522T192647_result.json`
- **Structured JSON:** [`961951584740c3a6c757.json`](../../sessions/96/961951584740c3a6c757.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇报

### seed200 v3 — 正常运行中

| 项目 | 状态 |
|------|------|
| 主进程 PID 129823 (bash) | 存活，24 min |
| Ray session | `session_2026-05-23_03-03-12`，raylet PID 131094 |
| GPU 2,3 进程 | WorkerDict PID 132938/132939（不是 129823 本身，而是 Ray 子进程） |
| GPU 2 | 100% util, 97067/97887 MiB |
| GPU 3 | 100% util, 97067/97887 MiB |
| wandb run | `sy10o3te` (exp029-seed200-episode-level) |
| 当前进度 | **Step 0→1 / 5**，正在执行第一个 iteration 的 rollout + policy update |
| 初始 validation | success = 6.25% (2/32) |
| 最后日志时间 | 03:21:06 — TaskRunner 在跑 AlfworldSG rollout，WorkerDict 在算 compute_policy_loss |

v3 正常。GPU 上的 PID 不是 129823 而是 Ray 派生的 WorkerDict 子进程（132938/132939），这就是 Director 追踪不到的原因。

### seed200 旧 log（seed200_episode_grpo.log）

这是**之前的失败 run**，不是 v3。崩溃原因：`ActorUnavailableError` — raylet 被意外终止（可能 OOM 或 SIGKILL）。与当前 v3 无关。

### seed100 — 正常

| 项目 | 状态 |
|------|------|
| PID 78400 (TaskRunner) | 存活，1h34m |
| PID 72007 (python main) | 存活，1h35m |
| GPU 0,1 | 0% util, ~44GB each（vLLM idle，等待下次 rollout） |

---
