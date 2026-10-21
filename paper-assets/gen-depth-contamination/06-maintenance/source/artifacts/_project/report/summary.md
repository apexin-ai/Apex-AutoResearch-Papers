# W3: Domain TTR & Vocabulary Entropy Statistics

## Data Sources
| Domain | Experiment | Model | N per depth |
|--------|-----------|-------|-------------|
| C4 | exp_018 | LLaMA-3.1-8B | 5,000 |
| Wikipedia | exp_023 | domain ablation | 5,000 |
| arXiv | exp_024 | Qwen | 2,200 |

## Summary Table (mean ± std)

### TTR
| Depth | Wikipedia | C4 | arXiv |
|-------|-----------|-----|-------|
| 0 | 0.665 ± 0.061 | 0.720 ± 0.105 | **0.755 ± 0.055** |
| 1 | 0.655 ± 0.121 | 0.707 ± 0.149 | **0.732 ± 0.098** |
| 2 | 0.647 ± 0.145 | 0.676 ± 0.159 | **0.677 ± 0.131** |
| 3 | 0.645 ± 0.159 | **0.662 ± 0.164** | 0.635 ± 0.134 |
| 4 | 0.636 ± 0.164 | **0.647 ± 0.169** | 0.621 ± 0.140 |
| 5 | 0.632 ± 0.172 | **0.636 ± 0.175** | 0.618 ± 0.150 |

### Vocabulary Entropy (freq_entropy)
| Depth | Wikipedia | C4 | arXiv |
|-------|-----------|-----|-------|
| 0 | 6.408 ± 0.284 | 6.225 ± 0.706 | **6.853 ± 0.295** |
| 1 | 5.932 ± 0.843 | 5.737 ± 1.189 | **6.113 ± 0.655** |
| 2 | 5.784 ± 0.905 | 5.774 ± 1.139 | **5.998 ± 0.967** |
| 3 | 5.664 ± 1.085 | 5.743 ± 1.161 | **5.964 ± 0.933** |
| 4 | 5.660 ± 1.062 | 5.758 ± 1.167 | **5.898 ± 0.942** |
| 5 | 5.593 ± 1.130 | 5.772 ± 1.141 | **5.816 ± 0.968** |

## Domain Ranking Analysis

### TTR ranking (ascending)
| Depth | Ranking | Matches K* (Wiki < C4 < arXiv)? |
|-------|---------|-------------------------------|
| 0 | Wiki < C4 < arXiv | ✅ Yes |
| 1 | Wiki < C4 < arXiv | ✅ Yes |
| 2 | Wiki < C4 ≈ arXiv | ✅ Yes (marginal) |
| 3 | arXiv < Wiki < C4 | ❌ No (inversion) |
| 4 | arXiv < Wiki < C4 | ❌ No (inversion) |
| 5 | arXiv < Wiki < C4 | ❌ No (inversion) |

### Entropy ranking (ascending)
| Depth | Ranking | Matches K* (Wiki < C4 < arXiv)? |
|-------|---------|-------------------------------|
| 0 | C4 < Wiki < arXiv | ❌ No (C4 and Wiki swapped) |
| 1 | C4 < Wiki < arXiv | ❌ No |
| 2 | C4 < Wiki < arXiv | ❌ No |
| 3 | Wiki < C4 < arXiv | ✅ Yes |
| 4 | Wiki < C4 < arXiv | ✅ Yes |
| 5 | Wiki < C4 < arXiv | ✅ Yes |

### Interpretation
- **TTR at depth 0** follows K* order: arXiv text has the richest vocabulary, Wikipedia the least diverse among these three. This aligns with domain complexity (K*).
- **TTR ranking inverts at depth ≥ 3**: arXiv TTR drops most steeply across depths (Δ = −0.137 from d0 to d5), while C4 and Wiki decay more slowly. This suggests the model collapses arXiv's specialized vocabulary faster.
- **Entropy at depth 0** does NOT follow K*: C4 (6.22) < Wiki (6.41) < arXiv (6.85). Wikipedia's higher entropy than C4 likely reflects its encyclopedic coverage across topics despite lower TTR.
- **Entropy ranking flips to K* order at depth ≥ 3**: as generation depth increases, Wikipedia entropy drops below C4, aligning with K*.

## Cohen's d (Effect Size)

### Depth 0 (original human text)
| Comparison | TTR (d) | Entropy (d) | Interpretation |
|------------|---------|-------------|----------------|
| C4 vs Wiki | +0.65 | −0.34 | C4 has medium-higher TTR; Wiki has slightly higher entropy |
| arXiv vs C4 | +0.37 | +1.03 | arXiv has small-medium higher TTR; large higher entropy |
| arXiv vs Wiki | +1.52 | +1.55 | Both very large effects: arXiv >> Wiki on both metrics |

### Depth-averaged (all depths pooled)
| Comparison | TTR (d) | Entropy (d) | Interpretation |
|------------|---------|-------------|----------------|
| C4 vs Wiki | +0.18 | −0.01 | Negligible after averaging across depths |
| arXiv vs C4 | −0.01 | +0.26 | TTR difference vanishes; small entropy gap remains |
| arXiv vs Wiki | +0.19 | +0.28 | Small effects only when pooling all depths |

### Key takeaway
The large domain differences at depth 0 (d > 1.5 for arXiv vs Wiki) are dramatically attenuated when pooling across depths, because iterative generation homogenizes lexical properties. This convergence itself is a signature of model collapse in the lexical dimension.

## Artifact
- LaTeX table: `domain_ttr_entropy.tex`
