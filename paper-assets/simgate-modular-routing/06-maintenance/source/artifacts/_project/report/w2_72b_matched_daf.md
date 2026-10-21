# W2: 72B Matched 10-Task DAF Comparison

**Source**: westb-13313:/root/autodl-tmp/simgate-modular-routing/artifacts/72b_matched_10task_daf.md

## Key Results
- **10 death-prone tasks** compared: 7B (205 eps) vs 72B (235 eps)
- **DAF is scale-independent**: 100% → 97.5% (episode-weighted)
- 8/10 tasks: DAF = 100% at BOTH scales
- 2 sub-100% tasks: identify-life-stages-2 (87.5%), measure-melting-point (90%) — each has only 1 score-driven label

## Death Rates
| Scale | DR Internal | DR Deterministic |
|-------|------------|-----------------|
| 7B | 51.2% | 19.5% |
| 72B | 33.2% | 3.0% |

## Conclusion
Death rates drop substantially with scaling, but the DOMINANCE structure is preserved. No task shifts from death-dominated to performance-dominated at 72B. DAF ≈ 100% at both scales = death dominance is a structural property, not a capacity artifact.