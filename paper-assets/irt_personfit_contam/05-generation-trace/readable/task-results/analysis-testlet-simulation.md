# analysis testlet simulation

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_testlet-simulation_20260521T183222_result.json`
- **Structured JSON:** [`28e9210b4fb1e2057c6f.json`](../../sessions/28/28e9210b4fb1e2057c6f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

模拟完成。结果汇总：

```
| σ_testlet | Type I | Mean(clean) | SD(clean) | d(15%) | d(50%) | d_ratio(15%) | d_ratio(50%) |
|-----------|--------|-------------|-----------|--------|--------|--------------|--------------|
| 0.0       | 0.043  |  -0.022     | 0.961     | -3.019 | -5.304 | 1.000        | 1.000        |
| 0.3       | 0.110  |  -0.635     | 1.049     | -3.024 | -5.505 | 1.002        | 1.038        |
| 0.5       | 0.454  |  -1.775     | 1.303     | -2.821 | -5.453 | 0.935        | 1.028        |
| 1.0       | 0.939  |  -5.743     | 2.283     | -2.128 | -5.627 | 0.705        | 1.061        |
```

### 分析

**lz\* 本身在 local dependence 下严重失效**：σ_testlet 增大时，clean condition 的 mean 大幅偏移（0→-5.7），SD 膨胀（0.96→2.28），Type I error 从 0.043 飙升至 0.939。这是预期的——标准 lz\* 假设 local independence，testlet 结构违反该假设，导致 lz\* 的零分布不再是 N(0,1)。

**但差分设计（Δlz\*）对 local dependence 具有鲁棒性**：
- **50% contamination**：d_ratio 在所有 σ_testlet 下都非常稳定（1.00–1.06），说明 testlet 效应对 clean 和 contaminated 条件的影响近似抵消，Δlz\* 的 effect size 几乎不变。
- **15% contamination**：d_ratio 在 σ≤0.5 时稳定（0.93–1.00），σ=1.0 时降至 0.70。极端 local dependence（σ=1.0 远超实际 benchmark 的 testlet 相关性）才导致检测力下降约 30%，但 |d| 仍达 2.13，检测力依然充足。

**结论**：Δlz\* 差分设计天然消除了 testlet random effect 的系统性偏移，在现实范围的 local dependence（σ≤0.5）下完全 robust。仅在极端 σ=1.0 + 低污染（15%）时才出现中等程度的检测力损失。

---
