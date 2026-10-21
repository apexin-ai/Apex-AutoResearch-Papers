# analysis push a v2 capability gap 7point

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_push-a-v2-capability-gap-7point_20260520T214934_result.json`
- **Structured JSON:** [`5d9de8487ba2ab4d2637.json`](../../sessions/5d/5d9de8487ba2ab4d2637.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。输出在 `/root/symb_invariant_consensus/results/push_a_v2_capability_gap_7point/`。

**统计摘要（7 data points）：**

| Metric | Value |
|--------|-------|
| Spearman ρ | **0.955**, p = 0.0008 |
| Linear R² | 0.822, RMSE = 1.43 pp, p = 0.005 |
| Linear slope | 0.143 (95% CI: [0.066, 0.219]) |
| Sigmoid R² | 0.893, RMSE = 1.11 pp |
| Isotonic R² | 0.983, RMSE = 0.45 pp |
| Break-even (linear) | Δ* ≈ −43.2 pp |

新增 Qwen2.5-14B 数据点（gap=−18.5, gain=+1.83）落在 sigmoid 曲线上符合预期——强 generator 时 verifier 增益有限但仍为正。相比 Push A 的 5 点，7 点的 Spearman ρ 从 0.90→0.955 且 p 值从 0.037→0.0008，统计显著性大幅增强。

图中新数据点用红色菱形标注，与其他点区分。PDF/PNG 均为 300 DPI 学术风格。`latex_stats.txt` 底部有可直接粘贴到论文的 inline summary 模板。

---
