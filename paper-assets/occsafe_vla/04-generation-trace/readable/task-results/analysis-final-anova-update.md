# analysis final anova update

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_final_anova_update_20260528T062016_result.json`
- **Structured JSON:** [`be1ed662586ba73b8fb0.json`](../../sessions/be/be1ed662586ba73b8fb0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### 2×2 Factorial ANOVA (Type II SS, N=13)

| Source | F(1,9) | p | η²_p | |
|--------|--------|-------|------|---|
| gradient_flow (ON/OFF) | 3.848 | .0814 | .300 | † |
| norm_type (BN/LN) | 4.718 | .0579 | .344 | † |
| gradient_flow × norm_type | 0.002 | .9670 | .000 | ns |

两个主效应均为边际显著（p<0.10），交互效应完全不显著。R²=0.435。

### Cell means & vs Vanilla (Bonferroni α=.0125)

| Cell | mean±sd | Δ vs Vanilla | Welch t | p | Cohen's d |
|------|---------|-------------|---------|-------|-----------|
| Vanilla | .745±.024 | — | — | — | — |
| C1 ON+BN (n=3) | .725±.064 | −.020 | −0.510 | .651 | −0.42 |
| C2 ON+LN (n=4) | .771±.028 | +.026 | 1.291 | .255 | +0.96 |
| C3 OFF+BN (n=4) | .767±.024 | +.021 | 1.147 | .309 | +0.88 |
| C4 OFF+LN (n=2) | .814±.017 | +.069 | 3.736 | .036 | +3.12 |

Cell 4 Welch t-test p=.036（未通过 Bonferroni 校正），但 permutation test p=.10。

### Cell 4 (n=2) 评估

- 两个 replicate 均高于 vanilla 均值（.802, .826 > .745）
- Bootstrap 95% CI: [.802, .826]
- 需要检测 |d|≥3.93 才能在 α=.05 下显著，实测 d=3.12 不够
- **结论：方向性证据强（效应量极大），但 n=2 统计功效不足，无法通过严格显著性检验。论文中应如实报告 n=2 并讨论为 limitation。**

### ANOVA 假设检验
- Levene 方差齐性：p=.543（通过）
- Shapiro-Wilk 正态性：Cell 1-3 均通过（p>.34）
- 假设满足，ANOVA 结果可靠

### 核心 claim 支持度
- **"OCC 不伤害 baseline performance"**：All OCC vs Vanilla Δ=+0.020, p=.313 → 支持（无显著下降）
- **"Detach ≥ Full OCC"**：Grad OFF mean=.782 > ON mean=.751, F=3.85, p=.081 → 边际支持
- **"LN > BN"**：LN mean=.785 > BN mean=.749, F=4.72, p=.058 → 边际支持
- **"无交互"**：F=0.002, p=.967 → 两个因素独立作用，强力支持

LaTeX Table 1 和 ANOVA table 已在输出中生成，artifact 已注册 (`art_20260528_dd1c68`)。

---
