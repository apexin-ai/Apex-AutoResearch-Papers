# exp-005: Temperature Sensitivity Analysis (T=0.7 vs T=1.0)

## 1. Signal Comparison by Temperature

### NER (full set, n=529)

| Signal | T=1.0 ρ | T=0.7 ρ | Δρ | T=1.0 τ | T=1.0 AUROC |
|--------|---------|---------|-----|---------|-------------|
| soft_jaccard | 0.3825 | 0.3875 | +0.0050 | 0.2658 | 0.6892 |
| fleiss_kappa | 0.259 | 0.3211 | +0.0621 | 0.2027 | 0.6292 |
| mean_logprob | 0.1396 | — | — | 0.1006 | 0.5907 |
| exact_match | 0.2941 | — | — | 0.2181 | 0.6398 |
| voting_conf | 0.3915 | — | — | 0.2906 | 0.7039 |

### RE (full set, n=397)

| Signal | T=1.0 ρ | T=0.7 ρ | Δρ | T=1.0 τ | T=1.0 AUROC |
|--------|---------|---------|-----|---------|-------------|
| soft_jaccard | 0.2441 | 0.2343 | -0.0098 | 0.1619 | 0.5916 |
| fleiss_kappa | 0.2782 | 0.1835 | -0.0947 | 0.1967 | 0.6262 |
| mean_logprob | 0.2467 | — | — | 0.1808 | 0.6186 |
| exact_match | 0.1562 | — | — | 0.1185 | 0.5863 |
| voting_conf | 0.3403 | — | — | 0.256 | 0.6668 |

## 2. Signal-Noise Tradeoff

| Metric | NER T=1.0 | NER T=0.7 | NER Δ | RE T=1.0 | RE T=0.7 | RE Δ |
|--------|-----------|-----------|-------|----------|----------|------|
| Oracle headroom | 0.1085 | 0.0966 | -0.0119 | 0.1674 | 0.1313 | -0.0361 |
| Diversity (1-SJ) | 0.2992 | 0.2243 | -0.0749 | 0.3886 | 0.313 | -0.0756 |
| Mean sample F1 | 0.6084 | 0.6243 | +0.0159 | 0.3612 | 0.3782 | +0.0170 |
| Sample F1 std | 0.3174 | 0.3131 | -0.0043 | 0.383 | 0.3845 | +0.0015 |
| % zero F1 | 12.19 | 11.2 | -0.9900 | 44.3 | 42.4 | -1.9000 |

**Key finding**: T=0.7 reduces oracle headroom (NER: -0.012, RE: -0.036) and diversity (NER: -0.075, RE: -0.076), confirming the expected narrowing. Despite less headroom, SJ ρ is marginally preserved (+0.005 NER, -0.010 RE), suggesting the signal-to-noise ratio stays roughly constant.

## 3. Conditional vs Full ρ by Temperature

### NER

| Signal | T=1.0 full ρ | T=1.0 cond ρ | Δ | T=0.7 full ρ | T=0.7 cond ρ | Δ |
|--------|-------------|-------------|---|-------------|-------------|---|
| soft_jaccard | 0.3825 | 0.3762 | -0.0063 | 0.3875 | 0.3868 | -0.0007 |
| fleiss_kappa | 0.259 | 0.2352 | -0.0238 | 0.3211 | 0.305 | -0.0161 |
| mean_logprob | 0.1396 | 0.1627 | +0.0231 | — | — | — |

### RE

| Signal | T=1.0 full ρ | T=1.0 cond ρ | Δ | T=0.7 full ρ | T=0.7 cond ρ | Δ |
|--------|-------------|-------------|---|-------------|-------------|---|
| soft_jaccard | 0.2441 | 0.3161 | +0.0720 | 0.2343 | 0.3716 | +0.1373 |
| fleiss_kappa | 0.2782 | 0.3067 | +0.0285 | 0.1835 | 0.2533 | +0.0698 |
| mean_logprob | 0.2467 | 0.1457 | -0.1010 | — | — | — |

## 4. Best Temperature per Signal

| Signal | Best T for NER | Best T for RE | Rationale |
|--------|---------------|--------------|-----------|
| SJ | T=0.7 (ρ=.388) | T=1.0 (ρ=.244) | NER: marginal gain; RE: negligible diff (.244→.234) but T=1.0 has more headroom |
| FK | T=0.7 (ρ=.321) | T=1.0 (ρ=.278) | FK improves at T=0.7 for NER (+0.062); RE: T=1.0 FK slightly better |
| logprob | T=1.0 only | T=1.0 only | No T=0.7 data; weakest signal overall |
| exact_match | T=1.0 only | T=1.0 only | No T=0.7 data; mid-tier NER, weak RE |
| voting_conf | T=1.0 only | T=1.0 only | No T=0.7 data; strongest single signal at T=1.0 |

## 5. Summary

### Temperature has minimal impact on SJ correlation quality
- NER SJ ρ: 0.383 (T=1.0) → 0.388 (T=0.7), Δ = +0.005
- RE SJ ρ: 0.244 (T=1.0) → 0.234 (T=0.7), Δ = -0.010
- The signal quality is stable across temperatures despite significant diversity changes.

### Lower temperature compresses the usable range
- Oracle headroom drops: NER -1.2pp, RE -3.6pp
- Diversity (1-SJ) drops: NER 0.299→0.224, RE 0.389→0.313
- This means less room for sample selection to improve over greedy.

### FK benefits more from T=0.7 than SJ
- NER FK ρ jumps +0.062 (0.259→0.321), while SJ gains only +0.005
- RE FK drops -0.095 (0.278→0.184), but SJ only drops -0.010
- FK is more temperature-sensitive; SJ is more robust.

### Conditional filtering matters more than temperature
- RE SJ: cond ρ at T=1.0 = 0.316, at T=0.7 = 0.372 — both far above full ρ (~0.24)
- The full→cond lift (+0.07 to +0.14) dwarfs the temperature effect (±0.01).

### Recommendation: T=1.0 with conditional filtering
- T=1.0 preserves more headroom and diversity while signal quality is nearly identical.
- Conditional filtering provides a much larger boost than temperature tuning.
- For voting_conf (strongest signal), T=1.0 is the only option with data.

### Data gaps
- logprob, exact_match, voting_conf only computed at T=1.0 (from pilot_004).
- tau and AUROC not available for T=0.7 (pilot_005 only stored ρ).
- To fully resolve, would need to re-run exp_012/013/014 on pilot_005 data.