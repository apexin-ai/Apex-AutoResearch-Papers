# ops check cell a progress

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-cell-a-progress_20260519T104531_result.json`
- **Structured JSON:** [`452d8d95a4af3bdc3e54.json`](../../sessions/45/452d8d95a4af3bdc3e54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

日志数据完整提取到了。汇报如下：

---

## 8B Cell A (7b_cell_a_h2) 训练状态

### 进程 & GPU
- **PID 849089**: 活着
- **GPU**: 4 卡全部 100% 利用率，显存 60-65 GB

### 当前进度
- **已完成**: Step 0 (val_before_train) + Step 1 (train)
- **当前**: Step 2 rollout 阶段（日志被 anchor_obs warning 刷屏，时间戳 17:37）
- **总步数**: 15

### Step 0 (val baseline)
| 指标 | 值 |
|---|---|
| val/success | **28.1%** |
| val/num_actions | 30.7 |

### Step 1 (train metrics)
| 指标 | 值 | 判断 |
|---|---|---|
| train/success | **12.5%** | 腰斩（28.1% → 12.5%） |
| entropy | **0.115** | 接近崩溃 |
| ppo_kl | **1.917** | 严重偏离 reference |
| grad_norm | 2.29 | 正常范围 |
| num_actions | **47.7/50** | 几乎全部 max out |
| pass@8 | 0.5 | |
| pg_clipfrac | 10.9% | |
| response_length | 567.5 | |

### 时间估算
- Step 1 耗时 **5076 秒（~85 分钟）**
- 剩余 13 步，乐观估计 **~18.4 小时**
- 但 entropy collapse 会导致后续 rollout 更慢（degenerate loops 生成 max-length episodes）

### 诊断：**训练已 collapse，建议 kill**

三个 collapse 信号全部确认：
1. **Success 腰斩** 28.1% → 12.5%
2. **Entropy 0.115** ≈ 模型输出退化为重复 token（日志中大量 "Nothing happens" 和反复 visit 同一物品）
3. **num_actions 47.7/50** = 每个 episode 都跑满最大步数，无法完成任务

Entropy 在 step 1 就已经 0.115，继续训练只会更低。模型不会自行恢复。剩余 ~18 小时 GPU 时间将全部浪费。

**建议**: kill 进程，调整超参（增大 entropy_coeff、降低 lr 或 kl_loss_coef）后重启。

---
