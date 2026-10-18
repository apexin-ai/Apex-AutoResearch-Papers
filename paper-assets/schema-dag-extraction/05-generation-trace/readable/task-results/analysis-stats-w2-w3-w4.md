# analysis stats w2 w3 w4

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_stats_w2_w3_w4_20260516T032244_result.json`
- **Structured JSON:** [`74480a77f1d42c4ec0a1.json`](../../sessions/74/74480a77f1d42c4ec0a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项分析全部完成。结果保存在 `/root/schema-dag-extraction/artifacts/round2_statistical_analyses.json`。

---

## 结果汇总

### W3: Type-level Cluster Bootstrap

| Dataset | r (paper) | Naive CI | Cluster CI (B=10000) | Significant |
|---------|-----------|----------|---------------------|-------------|
| Few-NERD | 0.112 | [0.076, 0.156] | **[0.069, 0.219]** | **Yes** |
| MAVEN | 0.129 | [0.104, 0.156] | **[0.081, 0.185]** | **Yes** |

Cluster CI 如预期更宽（有效样本从 pair 数降到 type 数），但两个 CI 均不含 0 → **cluster-robust inference 确认相关性显著**。

### W4: count=22 vs count=44 Recall CI

| Count | Pooled Recall | 95% Bootstrap CI |
|-------|--------------|------------------|
| 22 | 0.527 | [0.484, 0.569] |
| 44 | 0.551 | [0.525, 0.570] |

两个 CI **大幅重叠** → delta=+0.024pp 在 sampling variability 范围内，non-monotonicity **不显著**。每个 count 仅 5 batches，CI 宽度合理。

### W2: Realistic Practical Effect

| Setting | Slope | BCS IQR | Typical Gap (Q1→Q3) | 1-SD Gap | Extreme |
|---------|-------|---------|---------------------|----------|---------|
| 16-rel pool | -0.449 | 0.110 | **4.9pp** | **3.0pp** | 31.2pp |
| 80-pool 16-sub | -0.401 | 0.066 | **2.6pp** | **1.8pp** | — |

31.2pp 是极端 batch 对比。典型用户体验中 BCS 变动对应 **2.6–4.9pp accuracy gap**（IQR 范围）或 **1.8–3.0pp**（1-SD）。

### 推荐叙事

- **W3**: "Cluster-robust CIs (resampling types rather than pairs) are wider as expected but still exclude zero for both datasets, confirming significance."
- **W4**: "Bootstrap CIs overlap substantially; the +2.4pp non-monotonicity is within sampling variability (5 batches per level)."
- **W2**: "The 31.2pp gap is for extreme batches. For typical batch compositions (IQR), the predicted gap is ~5pp (16-rel) or ~2.6pp (80-pool), representing a meaningful but not dramatic practical effect."

---
