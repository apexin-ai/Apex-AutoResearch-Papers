# analysis bootstrap run

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-run_20260520T140722_result.json`
- **Structured JSON:** [`7069d1fa748903729ead.json`](../../sessions/70/7069d1fa748903729ead.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整结果

### 1. 数据覆盖率

42/75 cells。只有 OLMo-2-7B 有全部 3 seeds (s42/s123/s0)，Gemma-2-9B 有 2 seeds (s42/s123)，其余仅 s42。

### 2. Delta(d100-d000) — 各家族

| Family | n_seeds | Baseline | mean Δ(d100) | 95% CI | p(Δ=0) |
|--------|---------|----------|-------------|--------|--------|
| Phi-4 | 1 | 76.44% | -0.17pp | [-0.17, -0.17] | --- |
| Qwen2.5-14B | 1 | 69.05% | -9.37pp | [-9.37, -9.37] | --- |
| Qwen2.5-7B | 1 | 66.11% | -1.78pp | [-1.78, -1.78] | --- |
| Gemma-2-9B | 2 | 63.85% | +2.62pp | [+1.49, +2.62] | 0.000 |
| OLMo-2-7B | 3 | 54.93% | +1.35pp | [-0.55, +2.60] | 0.039 |

n=1 的家族无法计算 CI 和 p-value（degenerate，CI 就是点估计本身）。

### 3. Pattern Classification Consistency

| Family | s42 | s123 | s0 | Consistent? |
|--------|-----|------|----|-------------|
| Phi-4 | Immune | --- | --- | Yes |
| Qwen2.5-14B | U-collapse | Incomplete | --- | **No** |
| Qwen2.5-7B | V-recovery | --- | --- | Yes |
| Gemma-2-9B | Benefit-sat | V-recovery | --- | **No** |
| OLMo-2-7B | Benefit-sat | Immune | Benefit-sat | **No** |

3/5 家族跨种子 pattern 不一致（但 Phi-4/Qwen7B 仅有 1 seed，"consistent" 是 trivially true）。真正有多 seed 的 3 个家族全部不一致。

### 4. Spearman ρ（dose-response curve shape correlation across seeds）

| Family | n_pairs | rho_mean | rho_min | rho_max |
|--------|---------|----------|---------|---------|
| Phi-4 | --- | --- | --- | --- |
| Qwen2.5-14B | --- | --- | --- | --- |
| Qwen2.5-7B | --- | --- | --- | --- |
| Gemma-2-9B | 1 | 0.300 | 0.300 | 0.300 |
| OLMo-2-7B | 3 | 0.033 | -0.100 | 0.300 |

跨种子 dose-response 曲线形状相关极低。OLMo 平均 ρ=0.033（几乎无相关），Gemma ρ=0.300（弱相关）。

### 5. bootstrap_table.tex 完整内容

```latex
\begin{table}[t]
\centering
\caption{Triple-seed bootstrap analysis of MMLU dose-response patterns.}
\label{tab:bootstrap-mmlu}
\small
\begin{tabular}{lccccc}
\toprule
Family & Baseline (\%) & $\Delta$(d100) & 95\% CI & Pattern & $\bar{\rho}$ \\
\midrule
Phi-4 & 76.44 & -0.17 & [-0.17, -0.17] & Immune & --- \\
Qwen2.5-14B & 69.05 & -9.37 & [-9.37, -9.37] & Incomplete$^\dagger$ & --- \\
Qwen2.5-7B & 66.11 & -1.78 & [-1.78, -1.78] & V-recovery & --- \\
Gemma-2-9B & 63.85 & +2.62 & [+1.49, +2.62] & Benefit-sat$^\dagger$ & 0.30 \\
OLMo-2-7B & 54.93 & +1.35 & [-0.55, +2.60] & Benefit-sat$^\dagger$ & 0.03 \\
\bottomrule
\end{tabular}
\vspace{1mm}
\raggedright\footnotesize
$\Delta$(d100) = acc(d100) $-$ acc(d000) in percentage points. CI via BCa bootstrap (10{,}000 resamples). $\bar{\rho}$: mean pairwise Spearman $\rho$ across seeds. $^\dagger$Pattern inconsistent across seeds.
\end{table}
```

### 6. bootstrap_results.txt 完整内容

即上面第 2-4 节的四个表格的原始输出，已在上文完整列出（与 stdout 一致）。

**注意**: 输出目录是 `analysis/analysis/`（双层），因为脚本从 `analysis/` 目录运行时 `--output-dir analysis/` 变成了 `analysis/analysis/`。如果需要输出到 `analysis/`，可以加 `--output-dir .`。

---
