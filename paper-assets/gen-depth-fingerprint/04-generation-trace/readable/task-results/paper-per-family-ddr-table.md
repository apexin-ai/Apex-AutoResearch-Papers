# paper per family ddr table

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_per-family-ddr-table_20260523T093718_result.json`
- **Structured JSON:** [`48f064669d09bf08ba5c.json`](../../sessions/48/48f064669d09bf08ba5c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### LaTeX 表格（Spearman |ρ|）

```latex
\begin{table}[t]
\centering
\caption{Intra-family consistency of DDR patterns...}
\label{tab:family_ddr_consistency}
\small
\setlength{\tabcolsep}{3.5pt}
\begin{tabular}{l c ccc c ccc}
\toprule
 & & \multicolumn{3}{c}{\textsc{Drifting}} & \textsc{Int.} & \multicolumn{3}{c}{\textsc{Near-Stationary}} \\
\cmidrule(lr){3-5} \cmidrule(lr){6-6} \cmidrule(lr){7-9}
Family & $n$ & $H_{\mathrm{mean}}$ & TTR & Hapax & $H_{\mathrm{std}}$ & $H_{\mathrm{max}}$ & $H_{\mathrm{min}}$ & $\beta_{\mathrm{tail}}$ \\
\midrule
Pythia  & 2 & 0.69±0.03 & 0.65±0.02 & 0.66±0.01 & 0.20±0.06 & 0.02±0.02 & 0.49±0.02 & 0.08±0.02 \\
OLMo   & 1 & 0.64      & 0.70      & 0.71      & 0.30      & 0.07      & 0.39      & 0.14      \\
Qwen   & 3 & 0.55±0.07 & 0.60±0.06 & 0.62±0.06 & 0.16±0.08 & 0.09±0.00 & 0.36±0.05 & 0.08±0.01 \\
Llama  & 1 & 0.63      & 0.69      & 0.70      & 0.16      & 0.09      & 0.40      & 0.06      \\
Mistral& 1 & 0.54      & 0.60      & 0.61      & 0.06      & 0.09      & 0.40      & 0.03      \\
\midrule
All 8  & 8 & 0.60±0.08 & 0.63±0.05 & 0.65±0.05 & 0.18±0.08 & 0.07±0.03 & 0.40±0.06 & 0.08±0.03 \\
\bottomrule
\end{tabular}
\end{table}
```

### 关键发现

1. **Drifting 特征 family 内部高度一致**：Pythia CV=2-4%，Qwen CV=9-12%，所有 family 的 drifting |ρ| 均 > 0.5。

2. **Near-stationary 特征同样一致**：entropy_max（0.02-0.09）和 tail_decay（0.03-0.14）跨所有 family 保持低 |ρ|。

3. **Qwen 变异最大**（CV ~9-12% vs Pythia 2-4%），可能因为 model size 跨度大（0.6B → 8B）。

4. **entropy_min 是异常项**：|ρ| = 0.36-0.49，介于 drifting 和 stationary 之间，可能需要重新归类为 intermediate。

5. **跨 family 一致性也很强**：All 8 gen. 行的 SD 仅 0.05-0.08（drifting），说明 DDR pattern 是 generator-agnostic 的。

### 产出文件
- 服务器脚本：`/root/gen-depth-fingerprint/per_family_ddr_analysis.py`
- Spearman |ρ| 表：`artifacts/_project/paper/per_family_ddr_table.tex`
- Cohen's d 表：`artifacts/_project/paper/per_family_cohens_d_table.tex`

---
