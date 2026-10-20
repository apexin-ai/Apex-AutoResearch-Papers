# e_ij vs b_j Empirical Correlation Check (B2)

## Data Sources

- **τ_j (per-item exposure propensity)**: RRF aggregated scores from `/root/autodl-tmp/exp003/rrf_full_3scales/exposure_aggregated.json`. These are the per-item RRF composite of S1 (embedding), S2 (Min-K++), S4 (self-critique) signals averaged across 3 model scales (0.5B, 1.5B, 3B).
- **b_j (item difficulty proxy)**: `difficulty_baseline` from `analysis/irt_data/{bench}/item_metadata.csv` — mean p(correct) across d000 (clean) respondents. Also transformed to b_proxy = −logit(p) for IRT-scale difficulty.
- **IRT model exposure matrix**: `exposure[i,j] = (dosage_i / max_dosage) × τ_j`, so per-item variation in e_ij is entirely determined by τ_j.

## Results: τ_j vs b_j Correlation

### All Items

| Benchmark | N items | Pearson r | p-value | Spearman ρ | p-value |
|-----------|---------|-----------|---------|------------|---------|
| MMLU | 14042 | 0.0106 | 2.07e-01 | −0.0178 | 3.46e-02 |
| ARC | 1172 | 0.0599 | 4.02e-02 | 0.0534 | 6.78e-02 |
| GSM8K | 1319 | 0.0671 | 1.47e-02 | 0.0604 | 2.82e-02 |

(Pearson between τ_j and p(correct); negative sign = higher exposure items are harder)

### Top-300 RRF Items (IRT fitting subset)

| Benchmark | Pearson r | p-value | Spearman ρ | p-value | mean p(correct) top300 | mean p(correct) all |
|-----------|-----------|---------|------------|---------|------------------------|---------------------|
| MMLU | 0.1181 | 4.10e-02 | 0.0759 | 1.90e-01 | 0.5592 | 0.5171 |
| ARC | 0.1003 | 8.29e-02 | 0.0683 | 2.38e-01 | 0.7287 | 0.7125 |
| GSM8K | 0.0140 | 8.09e-01 | 0.0012 | 9.84e-01 | 0.3708 | 0.3391 |

### τ_j vs b_proxy (−logit(p)) — Top-300

| Benchmark | Pearson r | p-value | Spearman ρ | p-value |
|-----------|-----------|---------|------------|---------|
| MMLU | −0.1249 | 3.05e-02 | −0.0759 | 1.90e-01 |
| ARC | −0.0658 | 2.56e-01 | −0.0683 | 2.38e-01 |
| GSM8K | −0.0395 | 4.95e-01 | −0.0012 | 9.84e-01 |

## Per-Model RRF Exposure Variation

| Benchmark | N base models | Cross-model τ corr (mean) | Cross-model τ corr (range) | Within-item τ std |
|-----------|---------------|---------------------------|----------------------------|-------------------|
| MMLU | 30 | 0.1804 | [−0.044, 1.000] | 0.0535 |
| ARC | 29 | 0.2267 | [−0.160, 1.000] | 0.1352 |
| GSM8K | 29 | 0.2170 | [−0.177, 1.000] | 0.1235 |

## Conclusion

**Correlation strength: negligible.** All Pearson |r| < 0.13 across all benchmarks and item subsets. The strongest observed correlation (MMLU top-300, r=0.12) corresponds to R²=0.014 — exposure explains 1.4% of difficulty variance.

**Direction**: Slight positive correlation between τ_j and p(correct) (easier items tend to have marginally higher exposure scores). This is expected: commonly encountered benchmark items (e.g., textbook-style questions) may be both easier and more likely to appear in training data.

**Impact on γ identifiability**: **Minimal.** Two arguments:

1. **Empirical orthogonality**: τ_j and b_j are near-orthogonal (|r| < 0.13), so the γ×τ and a×b terms in the IRT likelihood occupy largely independent dimensions of the data. The model can reliably separate contamination effects from difficulty effects.

2. **Structural identification from dosage variation**: Even if τ_j and b_j were correlated, γ is identified from cross-respondent dosage variation. At dosage=0, the γ term vanishes (exposure[i,j]=0), so b_j is identified from clean respondents. γ is identified from the *change* in accuracy as dosage increases from 0→5→25→100, not from the absolute level. This within-respondent variation provides identification regardless of τ-b correlation.

**Selection bias check**: Top-300 RRF items have slightly higher mean p(correct) than the full set (e.g., MMLU: 0.559 vs 0.517), but the difference is small (+0.04 pp). The RRF selection does not preferentially select easy or hard items.
