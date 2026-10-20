# FDR Gradient at α=0.45: Complete fdr_p Values

## 8 Pairs × 2 Seeds

| Canary | Downstream | s42 fdr_p | s42 raw_p | s43 fdr_p | s43 raw_p |
|--------|-----------|-----------|-----------|-----------|-----------|
| token_entropy | distinct_1 | 0.0936 | 0.0702 | 0.0589 | 0.0308 |
| token_entropy | distinct_2 | 0.0912 | 0.0342 | 0.0589 | 0.0398 |
| token_entropy | distinct_3 | 0.0912 | 0.0312 | 0.0589 | 0.0442 |
| token_entropy | mauve | 0.2112 | 0.2112 | 0.0990 | 0.0866 |
| ece | distinct_1 | 0.0936 | 0.0640 | 0.0589 | 0.0234 |
| ece | distinct_2 | 0.0936 | 0.0522 | 0.0589 | 0.0346 |
| ece | distinct_3 | 0.0912 | 0.0306 | 0.0589 | 0.0220 |
| ece | mauve | 0.2112 | 0.1990 | 0.1050 | 0.1050 |

## Interpretation

At α=0.45, no pair reaches FDR-corrected significance (all fdr_p > 0.05) in either seed, yet the fdr_p values monotonically decrease relative to lower-α conditions, consistent with continuous signal growth approaching onset. The 6 core distinct-metric pairs cluster tightly (s42: 0.091–0.094; s43: 0.059), while mauve pairs lag behind at ~0.10–0.21, indicating weaker or delayed coupling for distribution-level metrics at this α.

## Cross-Seed Stability

The min fdr_p differs substantially between seeds: s42 = 0.091 vs s43 = 0.059 (ratio ≈ 1.55×). This cross-seed gap means the proximity to the significance boundary is seed-dependent — s43 is marginally closer to the 0.05 threshold than s42. The rank ordering of pairs is broadly preserved across seeds (mauve pairs weakest in both), but the absolute fdr_p magnitudes show non-trivial variability. This level of cross-seed instability is expected given T=11 time points and n_perm=5000, and cautions against interpreting the exact distance to threshold as a stable quantity.
