# analysis table3 llama L16

**English-Chinese Knowledge Conflict Signals Are Consistent With General Cross-Lingual Asymmetries** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_table3-llama-L16_20260523T120142_result.json`
- **Structured JSON:** [`a0d2a0cd5ea05e3de2d7.json`](../../sessions/a0/a0d2a0cd5ea05e3de2d7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

现有 Table 3 完整内容（`artifacts/_project/paper/experiments.tex` L142-164）：

```latex
%% Table 3: Steering results
\begin{table}[t]
\centering
\caption{Representation steering results (Llama-3.1-8B). Flip rate: fraction of test samples switching answer category. Control: random-direction perturbation of equal magnitude. Significant results ($p < 0.05$) in bold.$^{\dagger}$}
\label{tab:steering}
\small
\begin{tabular}{lcrrrrl}
\toprule
Layer & Depth & $\alpha$ & Steer (\%) & Ctrl (\%) & Fisher $p$ & Dir. \\
\midrule
\textbf{L13} & \textbf{41\%} & $\mathbf{+5}$ & \textbf{19.9} & \textbf{6.6} & $\mathbf{0.002}$ & \textbf{4 p$\to$c} \\
\textbf{L13} & \textbf{41\%} & $\mathbf{-20}$ & \textbf{36.0} & \textbf{17.6} & $\mathbf{<0.001}$ & \textbf{5 c$\to$p} \\
L18 & 56\% & $+2$ & 3.7 & 1.5 & 0.447 & \\
L28 & 88\% & $-20$ & 14.7 & 16.9 & 0.740 & \\
L28 (all) & 88\% & $-20$ & 11.8 & 11.8 & 0.370 & \\
\midrule
\multicolumn{7}{l}{\textit{Qwen3-8B L13: \textbf{[PLACEHOLDER]}}} \\
\bottomrule
\end{tabular}
```

---

## 分析

**格式规范：**
- 百分比：1 位小数（19.9, 6.6）
- p 值：3 位小数（0.002, 0.447），极小值用 `<0.001`
- 显著行（p < 0.05）：全行 `\textbf{}`
- Dir. 列：仅显著行填写翻转方向，非显著行留空
- 行按 layer 编号排序

**L16 数据换算：**
| α | Steer | Ctrl | Steer % | Ctrl % | p |
|---|-------|------|---------|--------|---|
| +5 | 12/136 | 11/136 | 8.8 | 8.1 | 1.000 |
| +10 | 25/136 | 15/136 | 18.4 | 11.0 | 0.123 |
| +20 | 31/136 | 33/136 | 22.8 | 24.3 | 0.886 |

L16 depth = 16/32 = 50%。全部不显著，不加粗，Dir. 留空。

---

## Diff 方案

**在 L153（L13 α=-20 行）之后、L154（L18 行）之前，插入 3 行：**

```diff
 \textbf{L13} & \textbf{41\%} & $\mathbf{-20}$ & \textbf{36.0} & \textbf{17.6} & $\mathbf{<0.001}$ & \textbf{5 c$\to$p} \\
+L16 & 50\% & $+5$ & 8.8 & 8.1 & 1.000 & \\
+L16 & 50\% & $+10$ & 18.4 & 11.0 & 0.123 & \\
+L16 & 50\% & $+20$ & 22.8 & 24.3 & 0.886 & \\
 L18 & 56\% & $+2$ & 3.7 & 1.5 & 0.447 & \\
```

**建议行排列顺序（按 layer → α）：**

| # | Layer | α |
|---|-------|---|
| 1 | L13 | +5 (sig) |
| 2 | L13 | -20 (sig) |
| 3 | **L16** | **+5** |
| 4 | **L16** | **+10** |
| 5 | **L16** | **+20** |
| 6 | L18 | +2 |
| 7 | L28 | -20 |
| 8 | L28 (all) | -20 |

L16 三行全部 p > 0.1，与 L13 的 p=0.002 和 p<0.001 形成鲜明对比，支持"因果窗口极窄（仅 3 层即失效）"的叙事。

---
