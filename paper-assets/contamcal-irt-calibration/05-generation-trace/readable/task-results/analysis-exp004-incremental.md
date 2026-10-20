# analysis exp004 incremental

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004_incremental_20260514T041612_result.json`
- **Structured JSON:** [`364d44ef4bf148bf7af1.json`](../../sessions/36/364d44ef4bf148bf7af1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果摘要

**进度**: 4/12 条件已启动，27/120 runs 完成 (22.5%)，进程仍在运行。

**核心发现**:

| 条件 | Seeds | γ Bias | CI95 宽度 | Coverage | 0∉CI |
|------|-------|--------|----------|----------|------|
| AUC=0.55, N=20 | 10 | +0.020 | 13.3pp | 80% | 100% |
| AUC=0.55, N=50 | 10 | +0.015 | 8.7pp | 90% | 100% |
| AUC=0.55, N=100 | 6 | −0.003 | 6.5pp | 100% | 100% |
| AUC=0.80, N=50 | 1* | +0.008 | 16.2pp | 100% | 100% |

**关键结论**:

1. **γ 在 AUC=0.55 就能识别** — 即使 exposure signal 接近随机，bias ≤ 0.02，RMSE ≤ 0.04，100% power。可辨识边界可能低于 AUC=0.55。

2. **N_models 主导精度** — CI 宽度 ≈ 1/√N 缩放（N=20→100: 13.3pp→6.5pp，比值 2.04 vs 理论 2.24）。

3. **AUC=0.80 CI 反而更宽 (16.2pp)** — 仅 1 seed，可能是噪声，但也可能是 exposure-ability collinearity 导致。需更多 seeds 确认。

4. **MCMC 质量完美** — 0 divergences，Rhat 全部 < 1.011。

5. **AUC threshold 暂无法确定** — 需要 AUC=0.65/0.90 数据。当前看 N≥50 时 15pp 阈值在 AUC=0.55 以下就已满足。

**预计剩余时间**: 93 runs，约 30-50 小时。

---
