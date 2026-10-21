# analysis exp004 incremental v2

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp004-incremental-v2_20260514T100341_result.json`
- **Structured JSON:** [`2fe14539ea1ed327a0b5.json`](../../sessions/2f/2fe14539ea1ed327a0b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 分析摘要

**5 条件, 46 runs** (auc0.55×{20,50,100}, auc0.8×{20,50}):

**核心结论（均确认）：**
- **CI宽度膨胀**: AUC=0.80 的 CI 宽度是 AUC=0.55 的 **1.87–1.95×**，且该比率跨 N 稳定（无交互效应）
- **1/√N 缩放**: 每步偏差 <5%，累积 n20→n100 偏差 +8.4%（微小的 prior 方差底限）
- **100% power**: 46/46 runs 的 CI 均排除 0
- **零 divergence**, 所有 R̂ < 1.01

**修正/新发现：**
- **Bias 方向反转降级**: AUC=0.55 高估 vs AUC=0.80 低估仅在 N=20 出现，t 检验不显著（t=1.72 / 0.59）。随 N 增大，两者均趋近无偏。结论：采样噪声，非系统性偏差
- **覆盖率偏低**: N=20 时 95% CI 覆盖率仅 80-90%（低于 nominal 95%），N≥50 恢复正常。建议论文中推荐 N≥50
- **AUC=0.8_n50 更新**: 从 6 seeds 增至 9 seeds，bias 从 +0.005 微调至 +0.009，CI 宽度 0.163 稳定

**无异常**。报告已写入 `artifacts/exp004_incremental_analysis.md` (v3)。

---
