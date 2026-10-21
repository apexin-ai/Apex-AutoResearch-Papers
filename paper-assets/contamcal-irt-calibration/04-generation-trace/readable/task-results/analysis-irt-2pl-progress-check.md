# analysis irt 2pl progress check

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_irt-2pl-progress-check_20260515T043344_result.json`
- **Structured JSON:** [`5e9e27923a4d5f299665.json`](../../sessions/5e/5e9e27923a4d5f299665.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 实验进度汇总

| 实验 | 阶段 | 主 IRT gamma | 当前进度 | 预估剩余 |
|------|------|-------------|----------|---------|
| **oracle-arc-2pl** | 基线 B2 | **-0.6179 [-1.04, -0.20], excludes_zero=True** | 主 IRT 完成; B2 warmup 5% | ~15-20 min |
| **s1only-gsm8k-2pl** | 基线 B3 | 0.1671 [-0.31, 0.64], excludes_zero=False | 主 IRT 完成; B3 warmup 30% | ~10-15 min |
| **oracle-arc-4pl-pooled** | 主 IRT chain 3/4 | 未完成 | chain 3: 2800/6000 (47% sampling), chain 4 未开始 | ~45-55 min |

### 关键结果（已完成的主 IRT）

**oracle-arc-2pl**: gamma 显著为负 (mean=-0.618, CI 不含零), Rhat=1.006, ESS=1512, div=0.00%. 表明受污染模型在 oracle exposure 下表现出**负向** contamination effect（反常）。

**s1only-gsm8k-2pl**: gamma 不显著 (mean=0.167, CI 含零), Rhat=1.002, ESS=1808, div=0.00%. S1 embedding 信号未检测到显著 contamination effect。

三个实验收敛诊断均良好。4PL-pooled 是最慢的（sequential chains + 复杂模型），预计还需约 50 分钟。

---
