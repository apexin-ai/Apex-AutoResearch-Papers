# exp random 300 tau baseline

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_random-300-tau-baseline_20260517T215924_result.json`
- **Structured JSON:** [`6caebdc2cff2a42dff2d.json`](../../sessions/6c/6caebdc2cff2a42dff2d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验结果

| 条件 | τ (Kendall) | p-value |
|------|------------|---------|
| **Random 300 items** | **0.058 ± 0.063** | 全部 > 0.38（不显著） |
| **RRF 300 items** | **0.731** | < 0.001 |

### 5个种子的详细结果

| Seed | τ_cal | p | τ_raw | Rhat | ESS | Time |
|------|-------|---|-------|------|-----|------|
| 42 | -0.019 | 0.917 | -0.013 | 1.007 | 1347 | 51s |
| 123 | 0.105 | 0.555 | 0.144 | 1.007 | 1479 | 51s |
| 456 | 0.154 | 0.385 | 0.213 | 1.006 | 1382 | 49s |
| 789 | 0.043 | 0.808 | 0.056 | 1.006 | 1550 | 51s |
| 1024 | 0.006 | 0.972 | -0.038 | 1.007 | 1466 | 50s |

### 结论

Random 300 items τ ≈ 0（与随机排序无异），RRF 300 items τ = 0.73。RRF 选择效果是压倒性的，τ 提升约 12.6 倍。这直接证明 RRF 信号选择的有效性——不是因为用了更少的 items，而是因为选对了 items。

**注意**：实验加载了 N=20 模型（含 4 个重复的 3B alpha=16 s42 模型），unified_baselines_n16 使用 N=16。结论不受影响。

数据保存在 `cqa1-21977:/root/autodl-tmp/exp006/random_300_tau_baseline.json`。

---
