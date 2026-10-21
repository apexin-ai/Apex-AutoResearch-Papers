# Convergence Pattern Deep Analysis — Summary Report

## Analysis 1: Attractor Pattern
- **Dominant direction**: PERMISSIVE (77.0%)
- Binomial test p = 0.0 (H0: p=1/3)
- **STRONG FINDING**: >60% convergence to single direction

## Analysis 2: Type × Convergence Rate

| Type | Convergent Rate | Unanimous Rate |
|------|----------------|----------------|
| auth_scope | 0.44 | 0.1 |
| cond_prec | 0.36 | 0.06 |
| coreferential | 0.3 | 0.06 |
| incompleteness | 0.62 | 0.24 |
| lexical | 0.38 | 0.16 |
| scopal | 0.38 | 0.16 |

### Incompleteness vs Others (Fisher's exact, unanimous rate)
- incompleteness vs auth_scope: OR=2.842, p=0.1084
- incompleteness vs cond_prec: OR=4.947, p=**0.0226**
- incompleteness vs coreferential: OR=4.947, p=**0.0226**
- incompleteness vs lexical: OR=1.658, p=0.4539
- incompleteness vs scopal: OR=1.658, p=0.4539

### Mechanism Group Comparison
- Structural (scopal, cond_prec, coreferential): 0.347 (52/150)
- Gap-filling (incompleteness, lexical): 0.5 (50/100)
- Boundary (auth_scope): 0.44 (22/50)
- χ²(2) = 5.993, p = 0.05

## Analysis 3: Non-Convergent Characteristics
- 92 divergent clauses (1-2/5 models violating)
- Type distribution χ² p = 0.3652 (consistent with uniform — divergence is not type-specific)
- Clause length: divergent median = 48.5 words, convergent = 46.0 words (p = 0.1642, not significant)
- Model uniformity in divergent violations: χ² p = 0.0017 (**significant**)
  - deepseek-v3 (43) and qwen3-235b (28) disproportionately represented in solo violations
  - gpt-4.1 (18) and claude-sonnet-4-6 (16) most robust to divergent-trigger clauses

---

## Paper Integration Suggestions

### §6.3 Extension (2-3 sentences)
"Classifying the interpretation direction of convergent violations reveals a strong permissive attractor: 77.0% of violation traces in majority-convergent clauses reflect permissive policy interpretation (binomial test against H0: p=1/3, p < 0.001). This directional bias holds across five of six ambiguity types (>75% permissive in each), with the exception of conditional precedence, where violations split nearly evenly between permissive (51.5%) and restrictive (47.1%) directions—suggesting that when-then rule conflicts induce bidirectional errors rather than the unidirectional permissive attractor observed elsewhere."

### Type-specific patterns
- auth_scope: near-universal permissive attractor (98.8%)—models consistently grant unauthorized latitude
- cond_prec: bidirectional split (51.5% PERM / 47.1% REST)—conflicting conditional rules produce both over-permissive and over-restrictive outcomes
- coreferential: highest LITERAL rate (16.1%)—models fail to resolve coreference chains
- incompleteness/lexical/scopal: strong permissive attractor (76-78%)

### Appendix Draft
See attractor_pattern.md for full per-type and per-convergence-level breakdowns suitable for appendix inclusion.

### Abstract/Intro Adjustment
Consider adding: "...with convergent violations showing a systematic permissive bias (77%)"
