# analysis param perturbation

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_param-perturbation_20260521T183252_result.json`
- **Structured JSON:** [`4789e5dadd3fe5519f9a.json`](../../sessions/47/4789e5dadd3fe5519f9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

### 验收

| 项目 | 状态 |
|------|------|
| 原始 d 值与 registry 一致 | d_15=-6.5746, d_50=-1.8966 ✓ |
| 2×100 trials 完成 | ✓ |
| 表格 + JSON 已输出 | ✓ |

### 结果表

| σ_rel | d_15 mean | d_15 SD | d_15 %bias | d_50 mean | d_50 SD | d_50 %bias |
|-------|-----------|---------|------------|-----------|---------|------------|
| 0% (orig) | -6.575 | — | — | -1.897 | — | — |
| 5% | -6.010 | 0.178 | 8.6% | -0.925 | 0.133 | 51.2% |
| 10% | -5.433 | 0.369 | 17.4% | -0.014 | 0.271 | 99.3% |

### 分析

**contam_15 (d_15)**: 鲁棒。即使 10% 噪声，d 仍为 -5.43（最差 trial=-4.74），远超常规阈值 |d|>0.8。检测结论不变。

**contam_50 (d_50)**: 脆弱。5% 噪声下 d 从 -1.90 衰减至 -0.92（仍可检测），但 10% 噪声下 d 均值趋近 0（中位数 -0.004），检测能力完全丧失。原因：contam_50 的 lz* 本身就落在 clean 分布边缘（原始 d=-1.90 只是 medium-large effect），参数扰动引入的方差足以淹没信号。

**结论**：4PL 参数**不是** contam_15 检测的 single point of failure——强污染信号对参数误差有充分容忍度。但对弱污染信号（contam_50），参数精度确实是瓶颈。论文中可据此论证：(1) 高污染率场景下结论 robust；(2) 低污染率场景需配合参数校准质量保证。

---
