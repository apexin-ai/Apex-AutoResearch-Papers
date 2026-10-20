# exp-016: Weighted Self-Consistency Baselines

## Summary

Tested whether simple trace-level weighting can match SICA's performance. Result: **No weighted SC variant significantly outperforms standard SC.** All differences are n.s. (McNemar p > 0.05).

## Methods

| # | Method | Weight per trace | Hypothesis |
|---|--------|-----------------|------------|
| 1 | Uniform (= SC) | 1.0 | Baseline |
| 2 | Length-weighted | trace_len (chars) | Longer reasoning = more reliable |
| 3 | Inverse-length | 1/trace_len | Shorter = more confident |
| 4 | Constraint-count | trace_len (proxy)† | More constraints = more evidence |

† Per-trace constraint counts were not stored in exp-001. trace_len used as proxy (constraint extraction is proportional to trace length). This makes method 4 identical to method 2.

## Results (804 problems, K=12, Qwen2.5-14B-Instruct)

| Method | Accuracy | n_correct | vs SC (p) | vs SICA (p) |
|--------|----------|-----------|-----------|-------------|
| **SICA** (reference) | **76.49%** | 615 | — | — |
| **SC / Uniform** | **76.24%** | 613 | — | 0.855 |
| Inv-length-weighted | 76.74% | 617 | 0.453 | 0.864 |
| Length-weighted | 75.25% | 605 | 0.153 | 0.066 |
| Constraint-count (=length) | 75.25% | 605 | 0.153 | 0.066 |

### Per-dataset Breakdown

| Method | ProofWriter (n=600) | FOLIO (n=204) |
|--------|--------------------:|----:|
| SICA | 75.50% | 79.41% |
| SC / Uniform | 75.17% | 79.41% |
| Inv-length | 75.67% | 79.90% |
| Length-weighted | 73.83% | 79.41% |

## Key Findings

1. **Uniform = SC verified** (76.24%, exact match with stored SC baseline).

2. **Length-weighting HURTS** (−1.0pp vs SC, n.s.): Longer traces are slightly less reliable, not more. This aligns with the intuition that LLMs that "overthink" on easy problems produce long but error-prone chains.

3. **Inverse-length slightly helps** (+0.5pp vs SC, n.s.): Concise traces marginally more accurate, but the effect is tiny and not significant.

4. **No weighted method matches SICA**: Even the best weighted variant (inv-length, 76.74%) merely matches SICA (76.49%) — and neither significantly improves over SC.

5. **Length vs inv-length**: chi2=3.03, p=0.082 (not significant, but trending). Directionally confirms that shorter traces are slightly better predictors.

## Flip Analysis (vs SC/Uniform)

| Method | Total flips | Flipped to correct | Flipped to wrong |
|--------|------------|-------------------|------------------|
| Length-weighted | 26 | 8 | 18 |
| Inv-length | 17 | 10 | 7 |

Length-weighting causes more flips and predominantly flips to wrong answers. Inverse-length causes fewer flips, slightly net positive.

## Trace Length Statistics

- N traces: 9,648 (804 × 12)
- Min: 204, P25: 1294, Median: 1700, P75: 2097, Max: 3993
- Mean: 1721.8 chars

## Conclusion

Simple per-trace weighting by length or its inverse does not meaningfully improve over standard majority vote. This is consistent with exp-013's finding that the MaxSAT component of SICA provides no additional value over counting — the entire SICA pipeline (constraint extraction + MaxSAT + weighted voting) collapses to performance equivalent to SC.

The Taubenfeld et al. (2024) style weighted SC baseline does not help on this task domain (logical reasoning with discrete True/False/Unknown answers). This may differ on tasks with more diverse answer distributions.

## Artifacts

- Script: `scripts/weighted_sc_baseline.py`
- Results: `results/weighted_sc_results.json`
- Report: this file
