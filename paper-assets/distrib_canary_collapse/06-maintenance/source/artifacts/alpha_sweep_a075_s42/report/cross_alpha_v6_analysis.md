Cross-alpha 5-point v6 FDR Analysis Summary

α=0.75 Permutation Granger FDR:
- ECE→d1: p_fdr=0.046 (SIG)
- ECE→d2: p_fdr=0.046 (SIG)
- entropy→d2: p_fdr=0.048 (SIG)
- entropy→d1: p_fdr=0.054 (borderline, NOT SIG)
- All 4 reverse directions: p>0.39, NOT SIG

5-point FDR summary: Raw-sig 14/40 → FDR-sig 6/40
FDR-sig concentrated at α=0.75 and α=1.0

Consensus framework:
α=0.00: 0/16 robust
α=0.25: 1/16 robust
α=0.50: 0/16 robust
α=0.75: 11/16 robust (single-seed method-agreement)
α=1.00: 6/16 robust (4-seed full consensus, stricter)

Conclusion: α=0.75 substantially passes. Claim 1 scope → "α ≥ 0.75" with single-seed caveat (C001).

Server files: results/analysis/cross_alpha_v6.json, results/analysis/cross_alpha_v6_report.md