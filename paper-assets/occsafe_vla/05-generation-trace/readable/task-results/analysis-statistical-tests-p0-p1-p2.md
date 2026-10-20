# analysis statistical tests p0 p1 p2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_statistical_tests_p0_p1_p2_20260527T185337_result.json`
- **Structured JSON:** [`5dfd435090f1c70ab657.json`](../../sessions/5d/5dfd435090f1c70ab657.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。以下是完整结果和解读。

---

## 统计分析结果汇报

### Cell Means (Bootstrap 95% CI)

| Cell | Condition | Mean CAR | 95% CI | n | SD |
|------|-----------|----------|--------|---|-----|
| Cell 1 | Full OCC BN (Grad ON + BN) | **0.763** | [0.720, 0.804] | 5 | 0.053 |
| Cell 2 | Full OCC LN (Grad ON + LN) | **0.777** | [0.740, 0.798] | 3 | 0.032 |
| Cell 3 | Detach BN (Grad OFF + BN) | **0.754** | [0.741, 0.775] | 5 | 0.023 |
| Cell 4 | Detach LN (Grad OFF + LN) | **0.826** | — | 1 | — |
| Vanilla | Baseline | **0.745** | [0.720, 0.768] | 3 | 0.024 |

### P0: Permutation Tests — 无显著效应

| 对比 | Delta | p-value | 判定 |
|------|-------|---------|------|
| **Gradient flow 主效应** (ON - OFF) | +0.002 | 0.921 | n.s. |
| **Norm type 主效应** (BN - LN) | -0.030 | 0.205 | n.s. |
| Cell1 vs Cell3 (Full vs Detach, BN) | +0.009 | 0.714 | n.s. |
| Cell1 vs Vanilla | +0.018 | 0.571 | n.s. |
| Cell3 vs Vanilla | +0.009 | 0.643 | n.s. |
| Cell2 vs Vanilla | +0.031 | 0.300 | n.s. |
| All OCC vs Vanilla | +0.022 | 0.371 | n.s. |

**结论**: gradient flow 主效应几乎为零 (Delta=+0.002, p=0.92)。norm type 也不显著 (p=0.20)。所有 pairwise 对比均不显著。

### P1: Effect Sizes

| 对比 | Cohen's d | 量级 | Hedges' g | Bootstrap Delta [95% CI] |
|------|-----------|------|-----------|--------------------------|
| Cell1 vs Cell3 (Full vs Detach BN) | +0.23 | small | +0.21 | +0.010 [-0.036, +0.053] |
| Cell1 vs Vanilla | +0.40 | small | +0.35 | +0.018 [-0.030, +0.064] |
| Cell3 vs Vanilla | +0.37 | small | +0.33 | +0.009 [-0.018, +0.037] |
| **Cell2 vs Vanilla** | **+1.11** | **large** | **+0.89** | +0.031 [-0.005, +0.067] |
| Grad ON vs OFF (main) | +0.06 | negligible | +0.06 | +0.002 [-0.037, +0.039] |

**结论**: gradient flow 主效应 d=0.06，可忽略。Cell2 (Full OCC LN) vs Vanilla 效应量最大 (d=1.11, large)，但 bootstrap CI 跨零。Full vs Detach (BN固定) 效应小 (d=0.23)。

### P2: Per-task 分析

**Gradient flow 敏感度 (Detach BN - Full OCC BN):**

| Task | Full OCC BN | Detach BN | Delta | 方向 |
|------|-------------|-----------|-------|------|
| **T3** | 0.440 | 0.236 | **-0.204** | Full OCC 大幅优于 Detach |
| **T5** | 0.147 | 0.064 | **-0.083** | Full OCC 优于 Detach |
| T6 | 0.547 | 0.552 | +0.005 | 基本持平 |
| T0-T2, T4, T7-T9 | ~high | ~high | <0.04 | 差异可忽略 |

**OCC vs Vanilla (Full OCC BN - Vanilla):**

| Task | Full OCC BN | Vanilla | Delta | 方向 |
|------|-------------|---------|-------|------|
| **T6** | 0.547 | 0.387 | **+0.160** | OCC 最大收益 |
| **T5** | 0.147 | 0.040 | **+0.107** | OCC 收益 |
| **T3** | 0.440 | 0.340 | **+0.100** | OCC 收益 |
| T1, T2 | ~0.92 | ~0.94 | -0.013 | 略负（噪声范围） |

**交互效应**: BN-LN|Full = -0.013, BN-LN|Detach = -0.072, interaction = +0.059。方向上 BN 在 Full OCC 下比 Detach 下更有优势，但 Cell 4 仅 n=1 不可靠。

### 综合解读

1. **Gradient flow 效应不显著**：Grad ON vs OFF 的 Delta 仅 +0.002 (p=0.92, d=0.06)。在 overall CAR 层面，是否让梯度回传到 backbone 对安全性能无影响。

2. **Per-task 差异集中在困难 task**：T3 和 T5（最难的两个 task，baseline CAR<0.5）是 gradient flow 最敏感的 task。Full OCC 在 T3 上比 Detach 高 +0.20——这是唯一有实际意义的差距，但因 T3 本身方差极大（Cell 1 的三个 seed: 0.80, 0.02, 0.50），不足以驱动 overall 显著性。

3. **OCC 对比 Vanilla 不显著但方向一致**：所有 OCC variant 均高于 Vanilla (mean 0.767 vs 0.745, +0.022)，且收益集中在 T5/T6/T3 困难 task。Cell 2 (Full OCC LN) vs Vanilla 的 Cohen's d=1.11 是唯一 large 效应量，但因 n=3 bootstrap CI 跨零。

4. **T3 是最大不确定性来源**：Cell 1 的 T3 CAR 在 [0.02, 0.80] 之间剧烈波动（SD 极高），直接拉高了 Cell 1 的方差，是所有对比不显著的主要原因之一。

---
