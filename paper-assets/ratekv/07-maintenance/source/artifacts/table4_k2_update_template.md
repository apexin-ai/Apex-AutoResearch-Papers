# Table 4 k=2 Update Template

## D063: Replace k=8 downstream eval with per-model optimal k

## Current Table 4 (verbatim LaTeX, lines 92-108 of experiments.tex)

```latex
\begin{table}[t]
\centering
\small
\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\times$ compression. Qwen shows large gains; the remaining models show small degradations or neutrality, tracking PPL results.}
\label{tab:downstream}
\begin{tabular}{lccccc}
\toprule
Model & ARC-C & HS & PIQA & WG & Avg \\
\midrule
Qwen2.5-7B        & $+$3.2 & $+$4.0 & $+$1.3 & $+$2.0 & $+$2.6 \\
Yi-1.5-9B        & $-$3.2 & $-$0.6 & $-$0.3 & $+$1.3 & $-$0.8 \\
Llama-3.1-8B     & $-$2.7 & $-$0.1 & $-$0.7 & $-$0.2 & $-$1.0 \\
Mistral-7B       & $-$1.2 & $-$0.2 & $+$0.4 & $-$1.0 & $-$0.5 \\
Gemma-2-9B       & $-$0.2 & $+$0.3 & $-$0.1 & $+$0.8 & $+$0.1 \\
\bottomrule
\end{tabular}
\end{table}
```

## Updated Table 4 (with k=2 data)

```latex
\begin{table}[t]
\centering
\small
\caption{0-shot accuracy change (Ours $-$ Uniform, pts) at 4$\times$ compression; each model evaluated at its profiling-derived optimal $k$. Qwen shows large gains; the remaining models show small degradations or neutrality, tracking PPL results.}
\label{tab:downstream}
\begin{tabular}{lccccc}
\toprule
Model & ARC-C & HS & PIQA & WG & Avg \\
\midrule
Qwen2.5-7B        & $+$3.2 & $+$4.0 & $+$1.3 & $+$2.0 & $+$2.6 \\
Yi-1.5-9B        & __YI_ARCC__ & __YI_HS__ & __YI_PIQA__ & __YI_WG__ & __YI_AVG__ \\
Llama-3.1-8B     & $-$0.8 & $-$0.0 & $-$0.1 & $+$0.5 & $-$0.1 \\
Mistral-7B       & __MI_ARCC__ & __MI_HS__ & __MI_PIQA__ & __MI_WG__ & __MI_AVG__ \\
Gemma-2-9B       & $-$0.2 & $+$0.3 & $-$0.1 & $+$0.8 & $+$0.1 \\
\bottomrule
\end{tabular}
\end{table}
```

### Llama k=2 values (source: llama_downstream_eval, k=2)

| Task | Baseline | Uniform | MCKP | Delta (MCKP-Uniform) | Rounded |
|------|----------|---------|------|----------------------|---------|
| ARC-C | 51.88 | 52.56 | 51.79 | -0.77 | -0.8 |
| HellaSwag | 60.73 | 60.24 | 60.21 | -0.03 | -0.0 |
| PIQA | 79.22 | 78.73 | 78.67 | -0.06 | -0.1 |
| WinoGrande | 73.88 | 72.61 | 73.09 | +0.48 | +0.5 |
| **Avg** | | | | **-0.10** | **-0.1** |

### Yi-1.5 k=2 values: PENDING (exp: yi15_downstream_eval_k2)

Fill placeholders `__YI_*__` when results arrive.

### Mistral k=2 values: PENDING (exp: mistral_downstream_eval_k2)

Fill placeholders `__MI_*__` when results arrive.

## Prose updates needed (line 111 of experiments.tex)

Current text references old deltas:
> The four non-spread models show minor average degradation (Yi −0.8, Llama −1.0, Mistral −0.5, Gemma-2 +0.1 pts)

Update to:
> The four non-spread models show minor average degradation (Yi __YI_AVG__, Llama −0.1, Mistral __MI_AVG__, Gemma-2 +0.1 pts)

Also line 112 ARC-C sensitivity sentence may need updating if Yi/Mistral ARC-C values change significantly.

## Provenance update checklist

| Claim ID | Current text | Current evidence | Action |
|----------|-------------|-----------------|--------|
| C168 | Yi-1.5 downstream avg delta -0.77 pts | yi15_downstream_eval | Update text + evidence to yi15_downstream_eval_k2 |
| C169 | Llama downstream avg delta -0.99 pts | llama_downstream_eval | Update to: avg delta -0.10 pts, evidence: llama_downstream_eval (k=2) |
| C170 | Mistral downstream avg delta -0.48 pts | mistral_downstream_eval | Update text + evidence to mistral_downstream_eval_k2 |
| C171 | Gemma-2 downstream avg delta +0.14 pts | gemma2_downstream_eval | No change (Gemma-2 uses k=8) |
| C172 | ARC-C most sensitive: Yi -3.24, Llama -2.65 | yi15/llama_downstream_eval | Update Llama to -0.77; Yi pending |

## Change summary vs. old k=8 Llama row

| | k=8 (old) | k=2 (new) | Change |
|---|-----------|-----------|--------|
| ARC-C | -2.7 | -0.8 | improved by 1.9 pts |
| HS | -0.1 | -0.0 | improved by 0.1 pts |
| PIQA | -0.7 | -0.1 | improved by 0.6 pts |
| WG | -0.2 | +0.5 | improved by 0.7 pts |
| Avg | -1.0 | -0.1 | improved by 0.9 pts |

Llama k=2 substantially improves downstream performance vs k=8, consistent with PPL results.
