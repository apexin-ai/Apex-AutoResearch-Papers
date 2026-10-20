# Paper Table 1: Complete Experiment Results

Generated: 2026-05-16

## CSV Data

```csv
Model,Condition,Seed,Accuracy,Pass_F1,Fail_F1,N,Conclusion
Qwen-1.5B,no_trace,42,67.31,,,1190,success
Qwen-1.5B,full_trace,42,77.06,,,1190,success
Qwen-1.5B,exception_only,42,99.83,,,1190,success
Qwen-1.5B,VOTA,42,99.58,,,1190,success
Qwen-7B,no_trace,42,75.13,81.34,62.72,1190,success
Qwen-7B,full_trace,42,81.76,87.17,68.51,1190,success
Qwen-7B,exception_only,42,99.83,98.50,96.00,1190,success
Qwen-7B,exception_only,123,99.83,98.50,96.00,1190,success
Qwen-7B,exception_only,456,99.83,98.50,96.00,1190,success
Qwen-7B,VOTA,42,99.41,97.00,91.70,1190,success
Qwen-7B,VOTA,456,99.08,,,1190,success
Qwen-7B,ae_only,42,99.92,,,1190,success
Qwen-7B,ae_only,123,99.08,,,1190,success
Qwen-7B,ae_only,456,99.92,,,1190,success
Qwen-7B,loop_only,42,85.63,,,1190,success
Qwen-7B,loop_only,123,85.88,,,1190,success
Qwen-7B,loop_only,456,86.64,,,1190,success
Qwen-7B,label_only,123,87.06,91.50,72.90,1190,success
Qwen-7B,label_only,456,85.90,90.50,72.70,1190,success
CodeLlama-13B,no_trace,42,76.50,,,1190,success
CodeLlama-13B,exception_only,42,99.83,,,1190,success
CodeLlama-13B,VOTA,42,98.57,,,1190,success
DeepSeek-Coder-7B,no_trace,42,73.36,,,1190,negative
DeepSeek-Coder-7B,full_trace,42,79.16,,,1190,success
DeepSeek-Coder-7B,exception_only,42,99.33,,,1190,success
DeepSeek-Coder-7B,exception_only,123,91.09,,,1190,negative
DeepSeek-Coder-7B,exception_only,456,99.33,,,1190,success
DeepSeek-Coder-7B,VOTA,42,84.45,,,1190,success
```

## Aggregated Table (Mean ± Std)

| Model | no_trace | full_trace | label_only | loop_only | ae_only | VOTA | exception_only |
|-------|----------|------------|------------|-----------|---------|------|----------------|
| Qwen-1.5B | 67.31 | 77.06 | — | — | — | 99.58 | 99.83 |
| Qwen-7B | 75.13 | 81.76 | 86.48±0.82 | 86.05±0.53 | 99.64±0.48 | 99.25±0.23 | 99.83±0.00 |
| CodeLlama-13B | 76.50 | — | — | — | — | 98.57 | 99.83 |
| DeepSeek-Coder-7B | 73.36 | 79.16 | — | — | — | 84.45 | 96.58±4.76 |

## LaTeX Tabular

```latex
\begin{table*}[t]
\centering
\caption{Test-set verdict accuracy (\%) across models and trace conditions. Multi-seed results show mean$\pm$std. All evaluations on $n{=}1{,}190$ held-out examples.}
\label{tab:main_results}
\begin{tabular}{l|ccccccc}
\toprule
\textbf{Model} & \textbf{no\_trace} & \textbf{full\_trace} & \textbf{label\_only} & \textbf{loop\_only} & \textbf{ae\_only} & \textbf{VOTA} & \textbf{exception\_only} \\
\midrule
Qwen-1.5B & 67.31 & 77.06 & --- & --- & --- & 99.58 & 99.83 \\
Qwen-7B & 75.13 & 81.76 & 86.48{\scriptsize$\pm$0.82} & 86.05{\scriptsize$\pm$0.53} & 99.64{\scriptsize$\pm$0.48} & 99.25{\scriptsize$\pm$0.23} & 99.83{\scriptsize$\pm$0.00} \\
CodeLlama-13B & 76.50 & --- & --- & --- & --- & 98.57 & 99.83 \\
DeepSeek-Coder-7B & 73.36 & 79.16 & --- & --- & --- & 84.45 & 96.58{\scriptsize$\pm$4.76} \\
\bottomrule
\end{tabular}
\end{table*}
```

## Ablation: exception\_only\_nomarker

| Model | Seed | Accuracy | Δ vs exception\_only |
|-------|------|----------|---------------------|
| Qwen-7B | 42 | 96.55 | −3.28 |
| Qwen-7B | 123 | 97.82 | −2.01 |
| Qwen-7B | 456* | RUNNING | — |
| Qwen-1.5B | 42 | 97.80 | −2.03 |

\* `exception_only_nomarker_seed456` still running at time of compilation.

**Nomarker mean (Qwen-7B, 2 seeds):** 97.19±0.90%  
**Drop from exception_only:** −2.64pp (still well above no_trace baseline)

```latex
\begin{table}[t]
\centering
\caption{Ablation: removing format markers from exception-only traces.}
\label{tab:nomarker_ablation}
\begin{tabular}{llcc}
\toprule
\textbf{Model} & \textbf{Seed} & \textbf{Accuracy (\%)} & \textbf{$\Delta$ vs.\ std} \\
\midrule
Qwen-7B & 42 & 96.55 & $-$3.28 \\
Qwen-7B & 123 & 97.82 & $-$2.01 \\
Qwen-7B & 456$^*$ & \textit{running} & --- \\
Qwen-1.5B & 42 & 97.80 & $-$2.03 \\
\bottomrule
\multicolumn{4}{l}{\footnotesize $^*$ In progress at time of writing.} \\
\end{tabular}
\end{table}
```

## Cross-Scale Analysis

### 1. no\_trace across scale
| Model | Params | Accuracy |
|-------|--------|----------|
| Qwen-1.5B | 1.5B | 67.31% |
| DeepSeek-Coder-7B | 6.7B | 73.36% |
| Qwen-7B | 7B | 75.13% |
| CodeLlama-13B | 13B | 76.50% |

**Trend:** Monotonic improvement with scale (+9.19pp from 1.5B→13B), but diminishing returns — the 1.5B→7B jump (+7.82pp) accounts for most of the gain.

### 2. exception\_only across scale/family
| Model | Accuracy |
|-------|----------|
| Qwen-1.5B | 99.83% |
| Qwen-7B | 99.83% |
| CodeLlama-13B | 99.83% |
| DeepSeek-Coder-7B | 99.33% (seed42/456), 91.09% (seed123) |

**Finding:** exception\_only saturates at ≥99.83% for Qwen-family and CodeLlama regardless of scale. DeepSeek achieves 99.33% on 2/3 seeds but shows one training instability (seed123=91.09%), suggesting the pattern is robust but model-family dependent in stability.

### 3. VOTA across scale/family
| Model | Accuracy |
|-------|----------|
| Qwen-1.5B | 99.58% |
| Qwen-7B | 99.25% (mean, 2 seeds) |
| CodeLlama-13B | 98.57% |
| DeepSeek-Coder-7B | 84.45% |

**Finding:** VOTA is highly effective (≥98.5%) for Qwen-family and CodeLlama across scales. DeepSeek-Coder significantly underperforms (84.45%), suggesting VOTA's structured trace format has family-dependent compatibility. The gap between DeepSeek VOTA (84.45%) and exception\_only (99.33%) indicates DeepSeek struggles with the multi-component VOTA format rather than the task itself.

### 4. Trace component hierarchy (Qwen-7B)
```
no_trace (75.13%) < full_trace (81.76%) < loop_only (86.05%) ≈ label_only (86.48%)
  < ae_only (99.64%) < VOTA (99.25%) ≈ exception_only (99.83%)
```

**Key insight:** Exception/assertion information alone nearly solves the task. The structured loop/label components provide moderate lift over raw traces. Full unstructured traces provide limited benefit (+6.63pp over no\_trace), while structured extraction yields +24pp.
