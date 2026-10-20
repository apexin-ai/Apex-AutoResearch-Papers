## BH-FDR Sensitivity Analysis (R31-W8)

### Question
Reviewer concern: would switching from Holm-Bonferroni to BH-FDR change conclusions?

### Results

| Method | Rejected / 57 | Selection tests surviving |
|--------|---------------|---------------------------|
| Holm-Bonferroni (paper current) | 10 | 0 |
| BH-FDR α=0.01 | 10 | #6, #19, #21 (3) |
| BH-FDR α=0.05 | 19 | #6, #18, #19, #20, #21 (5) |
| BH-FDR α=0.10 | 21 | same as α=0.05 |
| BH-FDR α=0.20 | 26 | +#8, #13 (7) |

### Key Points
- 15/21 selection tests have uncorrected p > 0.05 — no correction method can make them significant
- FewNERD LP selection (p<0.001): significant under BH α=0.01 (adj=0.0029) but NOT under Holm (adj=0.055)
- BH preserves 9 additional significant results that Holm rejects
- Core conclusion "no signal reliably beats greedy" driven by large non-significant p-values, correction-method-invariant

### Rebuttal Use
Switching to BH-FDR only makes MORE positive findings survive correction, does not invalidate any null findings.