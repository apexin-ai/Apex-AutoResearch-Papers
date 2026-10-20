# GRPO MIA Integration Draft

准备就绪，等 MIA AUC-ROC 数据到齐后填入 [X]/[Y]/[Z] 占位符，Director + Reviewer 确认后写入论文。

## Insertion 1: Appendix Post-RL (appendix.tex, after line 298)

Current text ends with:
> This $N{=}1$ observation requires validation across model families, RL methods, and contamination levels before any conclusions can be drawn.

Insert BEFORE that sentence (after line 297):

```latex
Min-K\% membership inference confirms this dissociation: while SFT yields a weak MIA signal (AUC-ROC${}=0.611$), GRPO training drives AUC to $[X]$ (step 500), $[Y]$ (step 1000), and $[Z]$ (step 1500)---approaching random chance ($0.50$) as RL erases memorization-based features while preserving the response-pattern anomaly that $\ell_z^*$ detects.
```

## Insertion 2: Discussion (discussion.tex, line 21)

Current text:
> $\ell_z^*$ sits below MIA \citep[logits;][]{minkprob2024} and ConStat ... particularly after RL post-training \citep{wang2025fragility}.

Replace with:

```latex
$\ell_z^*$ sits below MIA \citep[logits;][]{minkprob2024} and ConStat \citep[multi-benchmark scores;][]{constat2024} in an information-requirements hierarchy, needing only single-benchmark binary patterns and an external item bank---suited to retrospective audits where logits are unavailable. Our GRPO pilot directly confirms this advantage: Min-K\% AUC degrades from $0.611$ (SFT) to $[Z]$ (post-RL step 1500), while $\ell_z^*$ signal persists (${\sim}3.3$; Figure~\ref{fig:grpo}), demonstrating that response-pattern anomalies survive RL alignment that eliminates memorization-based features \citep{wang2025fragility}.
```

## Data Placeholders

| Placeholder | Source | Expected Value |
|-------------|--------|----------------|
| [X] | GRPO step 500 AUC-ROC | ~0.50-0.55 |
| [Y] | GRPO step 1000 AUC-ROC | ~0.50 |
| [Z] | GRPO step 1500 AUC-ROC | ~0.50 |

## Known Baselines (from registry)
- Base model AUC-ROC: 0.493
- SFT 15% contamination AUC-ROC: 0.611
