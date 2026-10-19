# check exp029 now

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_now_20260516T132732_result.json`
- **Structured JSON:** [`6678004a4fdcb76d2f88.json`](../../sessions/66/6678004a4fdcb76d2f88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029 状态报告

| 项目 | 状态 |
|------|------|
| **进程** | PID 861524 存活，运行 1h02m44s，状态 Ss+ |
| **GPU** | GPU0: 0% util, 45.5/97.9 GB; GPU1: 0% util, 45.5/97.9 GB |
| **训练进度** | **1/100 steps (1%)**, step 1 耗时 31min, ETA ~51h |
| **错误** | 无 OOM/Traceback/FAILED |
| **W&B** | run `x4bbiddh`, state=running, runtime=3178s |

### Step 0 初始验证指标 (140 episodes)

| 指标 | 值 |
|------|-----|
| val success (pass@1) | **10.7%** (15/140) |
| action_is_valid | 65.4% |
| action_is_effective | 100% |
| avg num_actions | 45.3 |
| best@128 reward | 10 (满分) |
| mean reward @140 | 1.07 |

### 状态判断

训练正常运行中。GPU 利用率为 0% 是因为当前处于环境 rollout 阶段（agent 与 AlfWorld 交互，非 GPU 密集）。Step 1 的 PPO 更新刚完成（日志中有 `compute_policy_loss` 调用），正在进入 step 2 的 rollout。

每 step ~31 分钟，100 步预计总耗时 ~51 小时。W&B 尚未记录 step 1 的 train metrics（仅有 step 0 的初始 val）。

---
