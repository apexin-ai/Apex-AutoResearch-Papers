# check training status

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_training-status_20260513T045706_result.json`
- **Structured JSON:** [`22103f41243e3f8e30f7.json`](../../sessions/22/22103f41243e3f8e30f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

## 训练进度汇总

| | exp_001_baseline | exp_003_event_gated_v2 |
|---|---|---|
| **PID** | 9409 ✅ 存活 | 18110 ✅ 存活 |
| **运行时间** | 2h54m | 8m |
| **当前步数** | **80,000** / 500K (16%) | **5,000** / 500K (1%) |
| **最新 eval_return** | 596.3 (@ 75K) | 31.0 (@ 5K) |
| **最新 train_return** | 670~846 (@ 80K) | 31~55 (@ 0) |
| **GPU** | cuda:0, 41% util, 4.2/98 GB, 44°C | cuda:1, 21% util, 4.2/98 GB, 42°C |
| **FPS** | ~7.6 | 刚启动，尚无稳定 FPS |

### Baseline eval_return 趋势
| Step | 5K | 15K | 25K | 35K | 45K | 55K | 65K | 75K |
|---|---|---|---|---|---|---|---|---|
| eval_return | 31.8 | 206.6 | 395.3 | 388.5 | 513.8 | 625.7 | 615.9 | 596.3 |

### exp_003 Gate 指标 (@ 5K)

| 指标 | 值 | 判断 |
|---|---|---|
| gate_dt_mean | **1.0** | ✅ Phase 1 curriculum 生效，无 subsampling |
| gate_dt_std | 0.0 | ✅ 所有 dt=1 |
| gate_dt_1_frac | 1.0 | ✅ 100% 步长为 1 |
| gate_scale | 0.0 | ✅ gate loss 未参与训练 |
| gate_empirical_entropy | 0.0 | 符合预期（dt 全为 1，无变异） |
| eval_return | 31.0 | 与 baseline 同期 31.8 **持平** ✅ |
| model_loss | 23.53 | 与 baseline 同期 23.47 **持平** ✅ |

### Phase 1 return 对比判断

**exp_003 @ 5K 与 baseline @ 5K 完全持平。** eval_return (31.0 vs 31.8)、model_loss (23.53 vs 23.47)、value_loss、actor_entropy 等核心指标几乎一致。Subsample curriculum 补丁工作正常——Phase 1 期间 effective_max_dt=1，exp_003 的训练动态与纯 baseline 无显著差异。

exp_003 刚跑了 8 分钟，需要继续观察到 15K-25K 步时 eval_return 是否仍与 baseline 曲线匹配（baseline 15K=206.6, 25K=395.3）。Phase 1 结束点在 25K gate steps，届时 gate 开始 ramp up 是关键观测窗口。

---
