# diagnose check all running bjb1

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_check-all-running-bjb1_20260518T125920_result.json`
- **Structured JSON:** [`7e33c636a25d99948b90.json`](../../sessions/7e/7e33c636a25d99948b90.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 进程状态
| 项目 | 状态 |
|------|------|
| PID 30131 (Ray driver) | **存活**，python 进程，56 线程，State: sleeping |
| PID 33571 (GPU 0 worker) | **存活**，`ray::WorkerDict.actor_rollout_update_actor` |
| PID 33572 (GPU 1 worker) | **存活**，`ray::WorkerDict.actor_rollout_update_actor` |

### GPU 占用
| GPU | 显存 | 利用率 | 温度 |
|-----|------|--------|------|
| 0 (RTX PRO 6000) | 97151 / 97887 MiB (99.2%) | 100% | 66°C |
| 1 (RTX PRO 6000) | 97151 / 97887 MiB (99.2%) | 100% | 63°C |

### RAM
- 已用 117Gi / 总计 1.0Ti，可用 860Gi

### 训练进度
- **当前步数：step 10 / 100**（刚完成 step 9，保存 global_step_10 checkpoint @ 20:53:28）
- 日志文件：`/root/runs/cost-verify-agent-rl/exp029_seed2_100step.log`（6.3MB，持续写入至 20:59:23）
- Checkpoint 路径：`/root/autodl-tmp/checkpoints/exp029-seed2/global_step_10/`
- 每 5 步保存一次 checkpoint（已保存 step 5, step 10）

### Step 9 关键指标
- **success: 7.8%**, pass@8: 50%
- action_is_valid: 65.8%, action_is_effective: 98.2%
- entropy: 0.036, ppo_kl: 0.0056, pg_clipfrac: 0.4%
- grad_norm: 1.79
- response_length mean: 13219 tokens
- **timing: ~818s/step（~13.6 min）**，throughput: 517 tokens/s

### 预计剩余时间
剩 90 步 x ~14 min/step = **约 21 小时**（预计明天 ~18:00 完成）

### 异常
无异常。训练正常进行，当前正在做 step 10 的 AlfWorld rollout（日志中可见 TaskRunner 在执行环境交互）。

---
