# analysis wilson ci

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_wilson-ci_20260515T075227_result.json`
- **Structured JSON:** [`7415ef1c7526c16160aa.json`](../../sessions/74/7415ef1c7526c16160aa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### Pooled Wilson 95% CI

| Condition | H7 rate [CI] | H1 rate [CI] | Genuine rate [CI] |
|---|---|---|---|
| **exec-only** (3 seeds, n=204) | 0.475 [0.408, 0.544] | 0.461 [0.394, 0.529] | 0.059 [0.034, 0.100] |
| **ISR β=0.1** (3 seeds, n=231) | 0.645 [0.581, 0.704] | 0.519 [0.411, 0.624]† | 0.309 [0.219, 0.416]† |
| **ISR β=0.3** (3 seeds, n=199) | 0.497 [0.429, 0.566] | 0.367 [0.303, 0.436] | 0.136 [0.095, 0.190] |
| **Random β=0.1** (1 seed, n=88) | 0.000 [0.000, 0.042] | 0.932 [0.859, 0.968] | 0.068 [0.032, 0.141] |
| **Random β=0.3** (3 seeds, n=163) | 0.043 [0.021, 0.086] | 0.988 [0.956, 0.997] | 0.012 [0.003, 0.044] |
| **SFT** (2 seeds, n=29) | 0.000 [0.000, 0.117] | 0.069 [0.019, 0.220] | 0.931 [0.780, 0.981] |

†ISR β=0.1 的 H1/genuine 仅有 s42 数据（s43/s44 缺 H1/genuine 分解），pooled 实际 n=81。

### Fisher Exact Tests (关键对比)

| 对比 | 类别 | OR | p-value | |
|---|---|---|---|---|
| ISR β=0.1 vs Random β=0.1 | genuine | 6.10 | 0.0001 | *** |
| ISR β=0.1 vs Random β=0.1 | H7 | ∞ | <0.0001 | *** |
| ISR β=0.3 vs Random β=0.3 | genuine | 12.64 | <0.0001 | *** |
| ISR β=0.3 vs Random β=0.3 | H7 | 22.06 | <0.0001 | *** |
| ISR β=0.1 vs exec-only | genuine | 7.14 | <0.0001 | *** |
| ISR β=0.3 vs exec-only | genuine | 2.51 | 0.011 | * |
| Random β=0.1 vs exec-only | genuine | 1.17 | 0.793 | ns |
| Random β=0.3 vs exec-only | genuine | 0.20 | 0.026 | * |

### 关键发现

1. **ISR 训练显著提升 genuine rate**：ISR β=0.1 genuine=30.9% vs Random β=0.1 genuine=6.8%（OR=6.1, p=0.0001）；ISR β=0.3 genuine=13.6% vs Random β=0.3 genuine=1.2%（OR=12.6, p<0.0001）。

2. **ISR 训练也带来更高 H7 rate**：ISR β=0.1 H7=64.5% vs Random β=0.1 H7=0%；ISR β=0.3 H7=49.7% vs Random β=0.3 H7=4.3%。这与 C006 约束一致——ISR+exec 的高 H7 可能是 Goodhart 效应（metric gaming）。

3. **Random 和 exec-only 的 genuine rate 无显著差异**（Random β=0.1 vs exec-only: p=0.793, ns），说明 random trace ablation 不比纯执行训练产生更多 genuine reasoning。

4. **SFT 有最高 genuine rate（93.1%）**，但样本极小（n=29），CI 很宽 [0.780, 0.981]。

5. **数据局限**：ISR β=0.1 的 H1/genuine pooled 仅基于 s42 一个 seed（s43/s44 缺分解数据）；Random β=0.1 仅有 s43 一个 seed。

产出文件已注册：`wilson_ci_results.csv`、`wilson_ci_results.json`、`wilson_ci.py`。

---
