## TY Granger 3-Seed Analysis: alpha=0.25 -- C001 Constraint Evaluation

**Date**: 2026-05-16 | **Data**: alpha=0.25, seeds 42/43/44, T=11 (gen 0..10)

### Per-Seed TY Significance Rates

| Seed | Raw sig | FDR sig | df_resid (entropy) | df_resid (ECE) |
|------|---------|---------|-------|------|
| 42 | 5/8 (62%) | 3/8 (38%) | 7 | 4 |
| 43 | 0/8 (0%) | 0/8 (0%) | 4 | 1 |
| 44 | 0/8 (0%) | 0/8 (0%) | 1 | 4 |

### Cross-Seed Consistency: 3/8 consistent (all none_sig), 5/8 mixed

### C001 Verdict: CANNOT BE MITIGATED — strengthened
- s42=62% sig driven by favorable df_resid=7; s43/s44=0% with df_resid 1-4
- Root cause: ADF integration-order estimation unstable at T=11, causing df_resid to vary 1-7 across seeds
- TY should be labeled "underpowered auxiliary method" in paper