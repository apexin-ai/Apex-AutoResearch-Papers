# ssh 008d status check

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_008d_status_check_20260514T041821_result.json`
- **Structured JSON:** [`1b6dcbe94ec50bd4da38.json`](../../sessions/1b/1b6dcbe94ec50bd4da38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 008d (subsample_on_h8) — cuda:? | 进程存活

| 项目 | 值 |
|------|------|
| **当前 step** | **45000** (已到目标！) |
| **45K eval** | **尚未完成** — 只写了 marker，eval 正在跑 |
| **最新完整 eval (35K)** | eval_return=**146.3**, value_mean=**60.2**, ratio=**0.41** |
| **25K eval** | eval_return=167.2, value_mean=25.9, ratio=0.15 |
| **趋势** | eval_return 从 167→146 下降，value_mean 26→60 大幅追赶 |
| **gate** | dt=2 锁死（100% dt_2_frac），零 entropy，gate 没有探索 |
| **fps** | ~6.0 |

> 45K eval 应该几分钟内就能出来（eval 10 episodes 通常 2-3 分钟）。

### 008a (fixed_dt2_no_subsample) — cuda:0 | 进程存活

| 项目 | 值 |
|------|------|
| **当前 step** | **68000** (已超过 65K 目标) |
| **65K eval** ✅ | 见下方详细指标 |
| **55K eval** | eval_return=487.9, value_mean=183.5, ratio=0.376 |
| **趋势** | eval_return 488→**608** (+24.6%)，稳步上升 |
| **gate** | dt=2 锁死，零 entropy |
| **fps** | ~6.67 |
| **ETA 到 105K** | (105K-68K)/6.67 ≈ **1.5 小时** |

**008a @65K 完整指标：**

| 指标 | 值 |
|------|------|
| eval_return | **607.98** |
| value_mean | **226.10** |
| value/eval ratio | **0.372** |
| actor_loss | -0.058 |
| actor_entropy | -5.23 |
| value_loss | 0.898 |
| model_loss | 3.918 |
| imag_reward_mean | 0.946 |
| target_mean | 227.40 |
| EMA_005 / EMA_095 | 211.8 / 233.4 |
| kl | 4.51 |

### 008e (subsample_on_fixed_dt1_h15) — cuda:1 | 进程存活

| 项目 | 值 |
|------|------|
| **当前 step** | **5000** (刚起步) |
| **5K eval** | eval_return=31.0, value_mean≈0 |
| **gate** | dt=1 锁死 |

### 关键发现

1. **008d 45K eval 即将出来**，再等几分钟就可以拿到数据做决策。
2. **008a 65K 数据已到**：eval_return 608 表现不错，value/eval ratio 0.37 相比 55K 基本持平，value 追踪稳定。
3. **两个实验的 gate 都锁死在固定 dt**，没有任何自适应行为。

---
