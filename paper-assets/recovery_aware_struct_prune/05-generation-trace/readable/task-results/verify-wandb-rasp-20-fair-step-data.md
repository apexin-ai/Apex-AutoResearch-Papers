# verify wandb rasp 20 fair step data

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_wandb_rasp_20_fair_step_data_20260518T045034_result.json`
- **Structured JSON:** [`72569b71c0585a5de6d7.json`](../../sessions/72/72569b71c0585a5de6d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

数据完整获取。以下是权威结果：

## Run 元信息

| 字段 | 值 |
|------|-----|
| Run ID | `s5zf5akl` |
| Run Name | `grpo_rasp_20_fair` |
| 创建时间 | 2026-05-17T23:50:31Z |
| 状态 | finished |
| 总 training steps | 100 |
| 运行时间 | 3791s (~63 min) |
| Config | beta=0.01, T=0.4, rep_penalty=1.15, lr=1e-6, loss=dapo, max_steps=100 |

## Step-Level Metrics (W&B 权威数据)

| Step | train/reward | train/frac_reward_zero_std | train/grad_norm | train/loss |
|------|-------------|---------------------------|-----------------|------------|
| 10   | 0.016875    | 0.850                     | 0.012207        | 0.006536   |
| 20   | 0.020625    | 0.850                     | 0.014282        | 0.000010   |
| 30   | 0.022500    | 0.800                     | 2.437500        | 0.024982   |
| 40   | 0.021250    | 0.850                     | 0.021240        | 0.029009   |
| **50** | **0.061250** | 0.725                  | 0.018188        | 0.032384   |
| 60   | 0.053125    | 0.750                     | 0.014099        | 0.011078   |
| **70** | 0.055625  | **0.675**                 | 1.296875        | 0.017321   |
| 80   | 0.030000    | 0.775                     | 0.535156        | 0.031667   |
| 90   | 0.015000    | 0.900                     | 0.006989        | 0.012074   |
| 100  | 0.010000    | 0.850                     | 0.882812        | 0.014751   |

## 数据校验结论

- **Peak reward = 0.061 at step 50** (不是 step 20)
- **Mean reward = 0.031** (所有 10 步均值: (0.0169+0.0206+0.0225+0.0213+0.0613+0.0531+0.0556+0.0300+0.0150+0.0100)/10 = 0.0306)
- **Min frac_zero_std = 0.675 at step 70**
- 轨迹模式：steps 10-40 低位徘徊 → step 50 peak → steps 60-70 短暂维持 → steps 80-100 collapse

论文中 **"peak step 50, mean 0.031"** 版本与 W&B 数据一致；**"peak step 20, mean 0.019"** 版本是错误的。

---
