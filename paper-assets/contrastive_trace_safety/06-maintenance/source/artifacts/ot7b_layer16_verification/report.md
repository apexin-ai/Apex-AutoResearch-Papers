# OT-7B Layer 16 Verification

**Date**: 2026-05-17
**GPU**: cuda:1 (RTX 6000)
**Data**: 228 traces, split train=136 / val=45 / test=47, seed=42

## Layer 16 Temporal Probes (HS)

| W | bal_acc | precision | coverage | pre_cp_fpr | lead_mean |
|---|---------|-----------|----------|------------|-----------|
| 1 | 0.6816 | 0.4284 | 0.5319 | 0.1200 | 16.1 |
| **3** | **0.6876** | **0.4664** | **0.5319** | **0.1004** | **21.6** |
| 5 | 0.6814 | 0.4635 | 0.5319 | 0.0992 | 21.7 |
| 10 | 0.6653 | 0.4685 | 0.4894 | 0.0859 | 25.0 |
| 15 | 0.6644 | 0.4876 | 0.4468 | 0.0773 | 39.6 |
| 20 | 0.6595 | 0.4939 | 0.4894 | 0.0749 | 17.9 |
| 25 | 0.6591 | 0.4889 | 0.5106 | 0.0796 | 28.3 |

Best W = 3 (by bal_acc = 0.6876)

## Text Temporal Probes (all-MiniLM-L6-v2)

| W | bal_acc | precision | coverage | pre_cp_fpr | lead_mean |
|---|---------|-----------|----------|------------|-----------|
| 1 | 0.5810 | 0.2446 | 0.6383 | 0.3449 | 37.1 |
| 3 | 0.5789 | 0.2537 | 0.7447 | 0.2709 | 41.6 |
| 5 | 0.5690 | 0.2474 | 0.7021 | 0.2547 | 50.9 |
| 10 | 0.5826 | 0.2700 | 0.7021 | 0.2223 | 45.6 |
| 15 | 0.5892 | 0.2827 | 0.6596 | 0.2004 | 46.5 |
| 20 | 0.6091 | 0.3162 | 0.6596 | 0.1758 | 39.4 |
| 25 | 0.6141 | 0.3291 | 0.6596 | 0.1605 | 45.5 |

## Bootstrap (Layer 16, W=3)

| Metric | HS | Text | Delta | p-value | Bonferroni (alpha=0.017) |
|--------|------|------|-------|---------|--------------------------|
| bal_acc | 0.7624 | 0.6558 | +0.1067 | 0.000 | **Yes** |
| precision | 0.5648 | 0.3459 | +0.2189 | 0.000 | **Yes** |
| pre_cp_fpr | 0.1004 | 0.2709 | -0.1705 | 0.000 | **Yes** |

Bonferroni pass count: **3/3**

## Layer 0 vs Layer 16 Comparison

| Metric | Layer 0 (W=3) | Layer 16 (W=3) | Delta | Winner |
|--------|---------------|----------------|-------|--------|
| HS bal_acc | 0.672 | 0.688 | +0.016 | L16 |
| HS precision | 0.357 | 0.466 | +0.109 | L16 |
| HS pre_cp_fpr | 0.188 | 0.100 | -0.088 | L16 |
| Bootstrap acc p | 0.001 | 0.000 | - | L16 |
| Bootstrap prec p | 0.056 | 0.000 | - | L16 |
| Bootstrap FPR p | 0.007 | 0.000 | - | L16 |
| Bonferroni pass | 2/3 | **3/3** | +1 | L16 |

## Conclusion

1. **Layer 16 uniformly dominates Layer 0** on all metrics at matched W=3:
   - bal_acc: 0.688 vs 0.672 (+1.6 pp)
   - precision: 0.466 vs 0.357 (+10.9 pp, large improvement)
   - pre_cp_fpr: 0.100 vs 0.188 (-8.8 pp, substantially lower false positive rate)

2. **Statistical significance is stronger**: Layer 16 achieves 3/3 Bonferroni-significant bootstrap tests (all p=0.000), whereas Layer 0 only achieves 2/3 (precision p=0.056, marginal).

3. **Layer 16 is the correct choice for paper reporting**. The original layer selection used `bal_acc * crossing_rate` which favored Layer 0 due to its high crossing rate. With the M001 correction (pure bal_acc as selection criterion), Layer 16 is unambiguously the best layer for OT-7B.

4. **Recommendation**: Replace all OT-7B results in the paper with Layer 16 (W=3). This strengthens the OT-7B case considerably, especially the precision improvement (+10.9 pp) and the clean 3/3 Bonferroni sweep.
