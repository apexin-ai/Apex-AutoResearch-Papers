# ops cron registration w41 w27

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cron_registration_w41_w27_20260527T102909_result.json`
- **Structured JSON:** [`cd8bac55349f2ec299d1.json`](../../sessions/cd/cd8bac55349f2ec299d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

### westd-41074

| GPU | PID | 实验 | 状态 | Cron |
|-----|-----|------|------|------|
| 0 | 356361 | pi05 random k=0.9 long seed42 (v2) | RUNNING, Task 3 ep 40/50 | 未注册（不在任务列表） |
| 1 | 356612 | pi05 random k=0.5 long seed42 (v2) | RUNNING, Task 4 ep 30/50 | 未注册（不在任务列表） |
| 2 | 422759 | **pi05 attn k=0.95 long seed42** | RUNNING, tmux 内，无 log 文件 | **已注册** |
| 3 | — | **pi05 l2norm k=0.85 long seed42** | **未启动**，GPU 空闲 | 无法注册 |

### westd-27271

| GPU | PID | 实验 | 状态 |
|-----|-----|------|------|
| 0 | 830286 (wrapper) / 830291 (python) | **eval_openvla_attn_k05_goal_seed42_v4** | **仍在运行**，Task 2/10，GPU 0 **不空闲** |
| 1 | 735728 | eval_openvla_l2norm_k085_object | RUNNING |

### 需要决策

1. **eval_pi05_l2norm_k085_long_seed42_strict_w41** 从未启动，GPU 3 空闲——是否现在启动？
2. **eval_openvla_attn_k05_goal_seed42_v4** 之前标记 DONE(failed) 但实际仍在运行 (Task 2/10)——需要更正 registry 状态。
3. GPU 0/1 上的两个 random 实验也缺少 cron，是否一并注册？

---
