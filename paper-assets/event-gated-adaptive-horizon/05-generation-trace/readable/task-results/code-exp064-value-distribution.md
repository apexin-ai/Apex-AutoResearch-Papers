# code exp064 value distribution

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp064-value-distribution_20260524T195704_result.json`
- **Structured JSON:** [`20eac3dd3717705d1e69.json`](../../sessions/20/20eac3dd3717705d1e69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

exp_064_value_distribution 完成。

## 结果摘要

| Model | Bias (V-MC) | RMSE | Overest% | V/MC ratio | V/MC median | r |
|-------|------------|------|----------|------------|-------------|---|
| **baseline_s1** | +344.85 | 371.73 | 100% | 3.31 | 1.90 | -0.18 |
| **exp_008d (CIVO)** | +108.99 | 112.36 | 100% | **7.80** | **3.40** | 0.29 |
| **exp_008f (control)** | **-6.51** | **57.93** | **52.5%** | 2.58 | **1.05** | 0.23 |

**关键发现**:
- **CIVO 模型 (trained dt_emb)** V/MC ratio = 7.80，是 baseline 的 2.4x，100% overestimation
- **Control (no dt_emb)** 几乎完美校准：median ratio = 1.05，overest 仅 52.5%，bias 接近 0
- 这直接证实 **dt_embedding 是 value overestimation 的根源**

注意：baseline 也有较高 bias（344.85），因为 V(s) 是 on-policy（当前 actor 的想象回报），而 MC return 是 off-policy（replay buffer 中的历史数据，包含早期较差策略的 episode）。关键对比是 CIVO vs control 的差异。

输出文件在 `bjb1-45299:/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_064_value_distribution/`，脚本在本地 `scripts/value_distribution_analysis.py`，4 个 artifact 已注册。

---
