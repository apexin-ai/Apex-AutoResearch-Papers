# analysis theta fixed param perturbation

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_theta-fixed-param-perturbation_20260521T185533_result.json`
- **Structured JSON:** [`e77a4c567124f4113c17.json`](../../sessions/e7/e77a4c567124f4113c17.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### 验收

| 项目 | 状态 |
|------|------|
| Baseline 验证: d_fixed(15%) = 4.77, d_fixed(50%) = 14.52 | ✓ |
| 2 × 100 trials 完成 | ✓ |
| JSON 输出 | ✓ `/root/autodl-tmp/param_perturbation_theta_fixed_results.json` |

### 结果表

| σ_rel | d_15 mean | d_15 SD | %bias_15 | d_50 mean | d_50 SD | %bias_50 |
|-------|-----------|---------|----------|-----------|---------|----------|
| 0% (orig) | 4.77 | — | — | 14.52 | — | — |
| 5% | 5.07 | 0.24 | 6.3% | 14.76 | 0.44 | 1.6% |
| 10% | 4.95 | 0.43 | 3.7% | 14.45 | 0.85 | 0.5% |

**Percentiles:**
- 5% noise d_15: [4.54, 4.87, 5.06, 5.23, 5.68]
- 5% noise d_50: [13.74, 14.45, 14.74, 15.06, 15.78]
- 10% noise d_15: [3.73, 4.73, 4.95, 5.26, 5.93]
- 10% noise d_50: [12.20, 13.93, 14.37, 15.02, 16.47]

### 分析

θ-fixed 路径在参数扰动下极其 robust。即使 10% noise，d_fixed(50%) 最小值仍为 12.20（远超任何常规检测阈值），d_fixed(15%) 最小值 3.73 仍然是极大的效应量。%bias 均 <7%，且 d_50 的 bias 不到 1%。

与 free-θ 形成鲜明对比：free-θ 在 10% noise 下 contam_50 的 d 崩到 ≈0，而 θ-fixed 的 d 始终维持在 12+。这直接支持论文的核心论点——θ-fixed 方法对参数误设更 robust，因为固定 θ 消除了参数噪声通过 θ 估计传递到 lz* 的间接路径。

---
