# code oracle exposure pooled

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_oracle-exposure-pooled_20260514T232421_result.json`
- **Structured JSON:** [`373a33b7ef3b74781a4e.json`](../../sessions/37/373a33b7ef3b74781a4e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All results collected. Here's the comparison:

## Oracle Exposure vs RRF v3 — Pooled IRT 4PL+γ

| Metric | ARC Oracle | ARC RRF v3 | GSM8K Oracle | GSM8K RRF v3 |
|--------|-----------|------------|-------------|-------------|
| n_models | 15 | 8 | 15 | 8 |
| **γ_mean** | **-2.83** | -7.62 | **+3.77** | +2.10 |
| γ 95% CI | [-3.72, -1.89] | [-8.79, -6.42] | [2.64, 4.96] | [0.97, 3.30] |
| γ_positive | No | No | **Yes** | Yes |
| **MAE** | **0.047** | 0.115 | 0.089 | **0.079** |
| **coverage_95** | **0.20** | 0.0 | **0.33** | 0.25 |
| PPP | 1.0 | 1.0 | 0.0 | 0.0 |
| pred/obs acc | 0.572/0.540 | 0.711/0.562 | 0.407/0.494 | 0.442/0.509 |
| diagnostics | all_ok | all_ok | **rhat=1.012, ess=345** | all_ok |

**解读：**

1. **ARC γ 仍为负**：oracle exposure (-2.83) 比 RRF v3 (-7.62) 温和很多，但方向仍然错。MAE 大幅改善（0.047 vs 0.115），coverage 从 0 提升到 0.20。pred/obs 差距缩小（0.572/0.540 vs 0.711/0.562）。

2. **GSM8K γ 正且更强**：oracle (3.77) 比 RRF v3 (2.10) 更强，CI 不含零。MAE 略差（0.089 vs 0.079），coverage 提升（0.33 vs 0.25）。但 GSM8K oracle 诊断有 rhat/ess 警告（rhat=1.012, min_ess=345），建议增加 samples。

3. **模型集差异**：oracle 跑了 15 models vs RRF v3 的 8 models，不完全同集合，比较需谨慎。

4. **PPP 模式一致**：ARC 始终 PPP=1.0（过预测），GSM8K 始终 PPP=0.0（欠预测）。

---
