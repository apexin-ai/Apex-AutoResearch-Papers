# exp_003: MMLU Item Alignment Gap Analysis

## Summary

Comprehensive analysis of MMLU item-level correctness differences between aligned (original) and para_aligned (paraphrased) evaluations across 20 model pairs (3 sizes × 4 contamination levels × 2 seeds).

## Key Findings

### 1. Aggregate Gap: Para Consistently Easier (-2.24pp)

| Metric | Value |
|--------|-------|
| N pairs | 20 |
| N common items | 6,596 |
| Mean gap (aligned - para) | **-2.243 pp** |
| Std | 0.671 pp |
| Max |gap| | 3.73 pp |
| Median | -2.259 pp |
| All pairs > 0.3pp | 20/20 (100%) |
| All pairs > 1.0pp | 19/20 (95%) |

The paraphrased versions are **systematically easier** across all models and contamination levels.

### 2. Per-Item Distribution

| Category | Count | % |
|----------|-------|---|
| Neutral (|gap| ≤ 0.3) | 5,593 | 84.8% |
| Para easier (gap < -0.3) | 568 | 8.6% |
| Aligned easier (gap > +0.3) | 435 | 6.6% |
| High disagreement (>50%) | 426 | 6.5% |

**Median per-item gap = 0.00** — most individual items show no systematic difference. The aggregate -2.24pp gap is driven by an asymmetric tail: more items become easier when paraphrased (8.6%) than become harder (6.6%).

### 3. The "Alignment Correction < 0.3pp" Claim — VALIDATED

The claim refers to the difference between:
- **Misaligned comparison**: comparing raw accuracy on 14042 items (aligned) vs 6596 items (para) without item-ID matching
- **Aligned comparison**: matching by item_id on the 6596 common items

This correction is indeed < 0.3pp (confirmed: 0.29pp for 1.5B, -0.04pp for 3B). The claim is about the **methodology correction**, not the total gap magnitude.

### 4. By Model Size

| Size | Mean Gap | Std | N |
|------|----------|-----|---|
| 0.5B | -2.259 pp | 1.238 | 4 |
| 1.5B | -2.452 pp | 0.310 | 8 |
| 3B | -2.026 pp | 0.415 | 8 |

Gap is relatively stable across sizes (0.5B has higher variance due to fewer pairs).

### 5. By Contamination Level

| Level | Mean Gap | N |
|-------|----------|---|
| d000 | -2.292 pp | 5 |
| d005 | -2.181 pp | 6 |
| d025 | -1.913 pp | 5 |
| d100 | -2.687 pp | 4 |

Variation across contamination levels is ~0.8pp. d100 shows slightly larger gap, suggesting contaminated models may benefit more from paraphrasing.

### 6. Flagged Items for IRT

426 items (6.5%) have >50% disagreement rate across models. Top examples:
- mmlu_8490, mmlu_10268: 100% disagreement, all models wrong on original, correct on para
- mmlu_10737, mmlu_194: 100% disagreement, strong para bias

These items should be considered for exclusion or differential treatment in IRT fitting.

## RRF Impact Assessment

For contamination detection via RRF:
1. **The -2.24pp systematic bias partially cancels** in differential analysis (aligned_exposure - para_exposure), since it affects all contamination levels similarly.
2. **Residual confound ~0.8pp** from d000→d100 variation in the gap. This is small relative to contamination effects (which are typically 5-15pp).
3. **426 flagged items** should be reviewed — if their disagreement is correlated with contamination, they could bias IRT estimates.

## Conclusion

- Per-item alignment correction is minimal (<0.3pp) — the methodology is sound
- But para versions are systematically easier (-2.24pp) — they cannot be treated as difficulty-equivalent to originals
- For RRF contamination detection, the bias is approximately constant across contamination levels, so differential analysis remains valid
- 426 items flagged for potential IRT exclusion
