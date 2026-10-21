# check exp029 fresh status

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp029_fresh_status_20260517T031656_result.json`
- **Structured JSON:** [`bb88a0836727c9bd1590.json`](../../sessions/bb/bb88a0836727c9bd1590.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp029_episode_level 状态报告

| 项目 | 状态 |
|------|------|
| **训练存活** | **Y** |
| **原始 PID 902342** | 存活 (wrapper bash) |
| **实际训练进程** | TaskRunner pid=905580, GPU workers pid=905773/905774 |
| **tmux session** | `exp029_episode_level` 存活 (创建于 04:12:30) |
| **日志最后更新** | 2026-05-17 11:14:57 CST (~2 min ago) |

### GPU 占用

| GPU | 显存 | 利用率 | 温度 | 功耗 |
|-----|------|--------|------|------|
| cuda:0 | 47739 / 97887 MiB | 100% | 68°C | 471W/600W |
| cuda:1 | 47741 / 97887 MiB | 100% | 71°C | 440W/600W |

### 最新 metrics (step 12, 已运行 ~5.8h)

| 指标 | 值 |
|------|-----|
| **success** | 23.4% |
| **pass@8** | 62.5% |
| **entropy** | 0.0419 |
| **grad_norm** | 3.01 |
| **ppo_kl** | 0.00886 |
| **pg_loss** | 0.000497 |
| **pg_clipfrac** | 0.0058 |
| **response_length** | 3835 |
| **throughput** | 553.5 tok/s |
| **time/step** | ~22.7 min |

### 趋势 (step 4 → step 12)

- success: 32.8% → 23.4% (下降)
- entropy: 0.0266 → 0.0419 (上升)
- grad_norm: 1.65 → 3.01 (上升)
- ppo_kl: 0.0006 → 0.0089 (上升)

当前正在执行 step 13 的 rollout 阶段 (日志中大量 `anchor_obs` warning 是 rollout 收集的正常输出)。Success rate 从 step 4 到 step 12 有所下降，KL 和 grad_norm 在上升，需关注后续 steps 是否稳定。

---
