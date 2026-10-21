# analysis testlet simulation ext

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_testlet-simulation-ext_20260521T183540_result.json`
- **Structured JSON:** [`11419e48702e4490f010.json`](../../sessions/11/11419e48702e4490f010.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

5 条件 × 1000 reps 全部完成。结果汇总：

## 结果表格

| σ_testlet | σ_mem | contam% | Power | Mean(Δlz*) | SD(Δlz*) | Cohen's d |
|-----------|-------|---------|-------|-------------|-----------|-----------|
| 0.5 | 0.0 | 0% | 0.000 | 0.000 | 0.000 | 0.000 |
| 0.5 | 0.5 | 15% | 0.987 | −6.960 | 3.303 | −2.107 |
| 0.5 | 1.0 | 15% | 0.993 | −6.716 | 3.192 | −2.104 |
| 0.5 | 0.5 | 50% | 0.991 | −20.034 | 8.574 | −2.337 |
| 0.5 | 1.0 | 50% | 0.985 | −20.685 | 13.033 | −1.587 |

## 分析

**非对称 LD 下 lz\* 仍能有效检测污染，power 均 ≥ 98.5%。** 具体发现：

1. **memory factor 对 power 影响微弱**：σ_mem 从 0.5 增到 1.0 时，15% contam 的 power 从 0.987 略升至 0.993，50% contam 反而从 0.991 微降至 0.985。Mean(Δlz*) 变化也很小。这说明 memorization floor（P≥0.95）是 Δlz* 信号的主要驱动力，额外的 memory factor 只是叠加了噪声。

2. **σ_mem=1.0 增大了 SD(Δlz*)，降低了 Cohen's d**：50% contam 时，σ_mem=1.0 的 SD 达到 13.03（vs σ_mem=0.5 的 8.57），Cohen's d 从 −2.34 降到 −1.59。大的 memory factor 方差让信号更不稳定，虽然均值信号差不多，但个体差异更大。

3. **power 是升还是降？** 与无 memory factor 的对照相比——场景 2 的 clean baseline 本身 lz\*_clean ≈ −1.82（因 testlet LD 导致 misfit），这个 baseline 偏移使得 contaminated 条件的绝对 lz\* 更极端，但 Δlz\*（paired difference）仍然由 memorization floor 主导。memory factor 本质上是在已经很强的信号上加噪声，power 基本持平（~98-99%）。

**结论：非对称 LD（seen items 共享 memory factor）不会削弱 lz\* 对污染的检测能力。** Memorization floor 效应远大于 LD 结构带来的噪声。

---
