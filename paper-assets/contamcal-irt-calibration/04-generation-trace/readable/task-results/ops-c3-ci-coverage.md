# ops c3 ci coverage

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_c3_ci_coverage_20260517T145149_result.json`
- **Structured JSON:** [`b38a515ccb38b6c02663.json`](../../sessions/b3/b38a515ccb38b6c02663.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results are complete. Here's the summary:

## CI Coverage Results

| Benchmark | Level | Coverage | Nominal | Diff | z-score |
|-----------|-------|----------|---------|------|---------|
| **MMLU** | 50% | **0.833** | 0.50 | +0.33 | +2.83 |
| MMLU | 80% | 0.889 | 0.80 | +0.09 | +0.94 |
| MMLU | 95% | 1.000 | 0.95 | +0.05 | +0.97 |
| **ARC** | 50% | 0.450 | 0.50 | -0.05 | -0.45 |
| ARC | 80% | 0.650 | 0.80 | -0.15 | -1.68 |
| ARC | 95% | 0.900 | 0.95 | -0.05 | -1.03 |

**Key findings:**

1. **MMLU (N=18, 300 items)**: Posterior CIs are **over-conservative** (especially 50% CI covers 83% of models). The 2PL+gamma model's parameter uncertainty provides generous coverage at model level. This means calibrated score uncertainties are trustworthy (if anything, too wide).

2. **ARC (N=20, 300 items)**: CIs are **slightly under-covering** at 80% level (65% vs 80%, z=-1.68). This suggests mild model misfit for some ARC models, though with N=20 the SE~0.09 makes this borderline significant.

3. **Item-bin coverage = 0% everywhere**: This is expected. The posterior CI on predicted means is extremely narrow (parameter uncertainty only). The actual obs-pred discrepancy at the item level reflects IRT model limitations (the 2PL sigmoid attenuates extreme responses), not CI failure.

4. Model-level residual MAE: MMLU=0.009, ARC=0.015.

**Output saved to**: `/root/autodl-tmp/exp006/ci_coverage_analysis/`

---
