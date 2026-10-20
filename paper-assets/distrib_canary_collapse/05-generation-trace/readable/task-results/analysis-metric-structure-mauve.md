# analysis metric structure mauve

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_metric-structure-mauve_20260522T115912_result.json`
- **Structured JSON:** [`81578115e3f6b26f33ae.json`](../../sessions/81/81578115e3f6b26f33ae.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All artifacts registered. PDF also generated alongside the PNG.

---

## 结果汇总

### Part 1: Mauve Pair 归因

Registry 中 3 个有 `non_robust_pairs` 数据的实验，**100% 的 non-robust pairs 涉及 mauve 作为 downstream**：
- 仅出现 2 种 pair：`token_entropy<mauve` 和 `ece<mauve`（consensus 0–2/5）
- 6 个 diversity pairs（`*<distinct_1/2/3`）全部通过 K≥3 consensus
- Wiki 域：PermG_fwd=6/8 + K3=6（mauve pairs 失败）
- C4 域：可达 PermG_fwd=8/8 + K3=8（mauve pairs 在 C4 可通过）
- 无例外

### Part 2: Shape Comparison

**形状指标**（核心判别器）：

| 模型 | 中间态 cells (0.1–0.7) / 25 |
|------|----------------------------|
| H0 linear | 12 (48%) |
| H0' concave | 13 (52%) |
| H1 step | 4 (16%) |
| **Observed** | **2 (8%)** |

H0/H0' 预测近半数 cells 处于中间检测率——平滑过渡。Observed 数据是二值的：23/25 cells 为 0.0 或 ≥0.625。

**RMSE**：H0=0.315, H0'=0.287, H1=0.371。H1 的 RMSE 偏高源于 T=10 阈值误判（H1 在 T=10 不预测检测但 observed 已有 0.75）及 α=0.60 异常，而非形状错误。

**图表**：4-panel figure 清晰展示 H0/H0' 平滑曲线 vs observed 二值点的对比。

---
