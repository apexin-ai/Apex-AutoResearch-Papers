# check step 25k

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_step-25k_20260513T061613_result.json`
- **Structured JSON:** [`fa406744d4935994f5a3.json`](../../sessions/fa/fa406744d4935994f5a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 汇总

### 1. 进程状态

| 实验 | PID | 运行时间 | CPU% | 当前 step | 状态 |
|---|---|---|---|---|---|
| exp_003_event_gated_v2 | 18110 | 1h27m | 1136% | ~40K (train) / 35K (eval) | 运行中 |
| exp_001_baseline | 9409 | 4h13m | 1165% | ~116K (train) / 115K (eval) | 运行中 |

### 2. exp_003 已过 25K — 但 Phase 2 未激活

step 25K 和 35K 的 gate 指标完全一致，**gate 没有开启**：

| 指标 | step 25K | step 35K |
|---|---|---|
| **gate_scale** | **0.0** | **0.0** |
| **gate_loss** | **0.0** | **0.0** |
| gate_dt_mean | 1.0 | 1.0 |
| gate_dt_std | 0.0 | 0.0 |
| gate_dt_1_frac | 1.0 | 1.0 |
| gate_empirical_entropy | 0.0 | 0.0 |
| gate_entropy_ratio | 0.0 | 0.0 |
| gate_entropy_bonus | 0.098 | 0.097 |

**gate_scale=0.0 说明 Phase 2 的 gate loss 权重从未生效。** gate 网络没有参与训练，dt 分布退化为全 1（固定步长）。

可能原因：`gate_curriculum_phase1` 的阈值单位可能是 `update_count` 而非 `step`。step 35K 时 update_count=7599，离 25000 updates 还很远（约需 step ~170K）。需要检查代码中 gate curriculum 的判断逻辑。

### 3. eval_return 对比

| Step | exp_003 | baseline | ratio | 判定 |
|---|---|---|---|---|
| 5K | 31.0 | 31.8 | 0.976 | 通过 |
| 15K | 153.9 | 206.6 | 0.745 | **需关注** |
| 25K | 254.2 | 395.3 | 0.643 | **需关注** |
| 35K | 290.8 | 388.5 | 0.749 | **需关注** |

exp_003 在 15K 后持续落后 baseline 25-36%，ratio 均 < 0.8。

### 4. Baseline 最新状态

| Step | eval_return |
|---|---|
| 85K | 713.9 |
| 95K | 871.1 |
| 105K | 915.7 |
| 115K | 919.8 |

Baseline 在 85K-115K 区间表现强劲，已趋近收敛（919.8）。

### 5. 关键问题

1. **Phase 2 未激活是最大问题。** gate_scale 始终为 0，gate 网络完全冻结。需要检查 `gate_curriculum_phase1=25000` 的判断单位是 environment step 还是 update count。
2. **即使 gate 未激活，exp_003 也比 baseline 慢 25%+。** 这可能因为 gate 网络参数增加了模型容量但未参与有效训练，拖累了整体学习效率。
3. 建议：检查代码中 gate curriculum 的触发条件，确认是按 `step` 还是 `update_count` 计数。如果是后者，Phase 2 要到 ~step 170K 才会激活。

---
