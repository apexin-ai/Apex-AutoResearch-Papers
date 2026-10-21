# monitor exp 001b urgent

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_exp_001b_urgent_20260513T192646_result.json`
- **Structured JSON:** [`e3dd8798418967e041be.json`](../../sessions/e3/e3dd8798418967e041be.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_001b 状态报告

### 训练状态：**在跑**
- 进程 PID 93794，启动于 03:15（约 12 分钟前）
- 当前 step 4/50（8%），每 step 约 120-270 秒
- GPU 0/1 各占用 ~59GB，利用率瞬时 0%（正在 rollout/collapse 阶段）

### Step 1 关键指标（目前唯一有完整 metrics 的训练 step）

| 指标 | 值 | 判定 |
|------|-----|------|
| `critic/advantages/mean` | **0.005** | 技术上非零，但极小 |
| `critic/advantages/max` | 1.50 | 有差异信号 |
| `critic/advantages/min` | -0.50 | 有差异信号 |
| `actor/pg_loss` | **-1.73e-7** | 约等于 0 |
| `actor/ppo_kl` | **0.0** | 策略无变化 |
| `actor/pg_clipfrac` | **0.0** | 无 clip |
| `train/AlfworldSG/success` | **0%** | 全失败 |
| `manager_invalid_action` | **95.6%** | bootstrap 问题仍在 |
| `action_is_valid` | **0.6%** | 几乎全部格式错误 |
| `critic/rewards/mean` | -0.956 | 接近最低 -1.0 |

### 分析

advantages 均值 0.005（非字面 0），但 **pg_loss ≈ 0、KL = 0、clipfrac = 0** — 策略实际没有任何更新。95.6% invalid action 表明模型仍然无法输出正确格式，bootstrap 问题未解决。max_model_len 修复没有帮助。

### 建议：**Kill**

虽然 advantages 不是严格全零，但训练实质无效：
- 策略梯度为零，模型不在学习
- 95.6% invalid action，和 exp_001 同一问题
- 继续跑 46 步只是浪费 GPU 时间

需要先解决 bootstrap 问题（如 SFT warmstart 或 prompt engineering 让 base model 输出正确格式）再重启训练。

**是否执行 kill？** 请确认。

---
