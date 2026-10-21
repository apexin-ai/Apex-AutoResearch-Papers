# evidence 14b appendix table

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_evidence_14b_appendix_table_20260525T080724_result.json`
- **Structured JSON:** [`9973e18e67a95732b952.json`](../../sessions/99/9973e18e67a95732b952.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

JSON artifact 已生成并注册。以下是 LaTeX 表格预览：

```latex
\begin{table}[h]
\centering
\caption{Pythia-1.4B phase diagram: PermG forward detection across contamination levels ($\alpha$) and observation windows ($T$). Fwd/Rev: FDR-significant forward/reverse pairs; $K{\geq}3$: multi-method consensus pairs. $\dagger$ marks bidirectional confounding (reverse $>0$). Denominator is 8 (canonical pairs) unless marked $^{*}$ (6-pair basis, MAUVE unavailable).}
\label{tab:14b_phase_diagram}
\begin{tabular}{@{}llcccl@{}}
\toprule
$T$ & $\alpha$ & Seed & Fwd & Rev & $K{\geq}3$ \\
\midrule
\multirow{12}{*}{10}
 & \multirow{3}{*}{0.45} & 42 & 0/8 & 0/8 & 0/8 \\
 &                       & 43 & 1/8 & 0/8 & 2/8 \\
 &                       & 44 & 0/6$^{*}$ & 0/6$^{*}$ & 0/6$^{*}$ \\
\cmidrule(l){2-6}
 & \multirow{3}{*}{0.50} & 42 & 4/8 & 2/8$^{\dagger}$ & 3/8 \\
 &                       & 43 & 6/6$^{*}$ & 0/6$^{*}$ & 1/6$^{*}$ \\
 &                       & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 0/6$^{*}$ \\
\cmidrule(l){2-6}
 & \multirow{3}{*}{0.60} & 42 & 4/8 & 0/8 & 3/8 \\
 &                       & 43 & 4/8 & 6/8$^{\dagger}$ & 3/8 \\
 &                       & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 5/6$^{*}$ \\
\cmidrule(l){2-6}
 & \multirow{3}{*}{0.75} & 42 & 5/8 & 0/8 & 5/8 \\
 &                       & 43 & 6/8 & 5/8$^{\dagger}$ & 5/8 \\
 &                       & 44 & 6/6$^{*}$ & 0/6$^{*}$ & 6/6$^{*}$ \\
\midrule
\multirow{8}{*}{15}
 & \multirow{2}{*}{0.45} & 42 & 3/8 & 0/8 & 4/8 \\
 &                       & 43 & 5/6$^{*}$ & 3/6$^{*\dagger}$ & 3/6$^{*}$ \\
\cmidrule(l){2-6}
 & \multirow{2}{*}{0.50} & 42 & 3/8 & 0/8 & 2/8 \\
 &                       & 43 & 3/6$^{*}$ & 0/6$^{*}$ & 3/6$^{*}$ \\
\cmidrule(l){2-6}
 & \multirow{2}{*}{0.60} & 42 & 6/8 & 0/8 & 6/8 \\
 &                       & 43 & 6/6$^{*}$ & 3/6$^{*\dagger}$ & 6/6$^{*}$ \\
\cmidrule(l){2-6}
 & \multirow{2}{*}{0.75} & 42 & 6/8 & 0/8 & 6/8 \\
 &                       & 43 & 6/6$^{*}$ & 0/6$^{*}$ & 6/6$^{*}$ \\
\bottomrule
\end{tabular}
\end{table}
```

关键发现：
- **T=10 α=0.45** 是盲区：3 seed 的 PermG fwd 均 ≤1，K≥3=0
- **T=10 α≥0.50** 开始出现信号，但 s43 的 α=0.60/0.75 有双向混杂（rev=5-6/8）
- **T=15** 整体灵敏度提高：α=0.45 已有 3-5 fwd；α≥0.60 达到 6/6-6/8 饱和
- 4 个实验出现 bidirectional confounding（†标注），均在 s43，提示 seed-specific artifact

---
