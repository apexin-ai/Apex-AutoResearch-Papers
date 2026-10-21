# Analysis: eval_xvla_random_k085_long_seed42

## Experiment Parameters
- **Model**: X-VLA-Libero (BART connector, 879.5M params)
- **Suite**: libero_10 (Long)
- **Pruning**: Random, keep_ratio=0.85 (42/50 vision tokens)
- **Episodes**: 50 per task × 10 tasks = 500 total
- **Seed**: 42
- **Server**: westd-38929
- **Runtime**: 106.7 min

## Results

**Overall SR: 35.0% (175/500), 95% Wilson CI: [30.9%, 39.3%]**

| Task | SR | Description |
|------|-----|-------------|
| T0 | 54% | put both the alphabet soup and the tomato sauce in the basket |
| T1 | 10% | put both the cream cheese box and the butter in the basket |
| T2 | 16% | turn on the stove and put the moka pot on it |
| T3 | 88% | put the black bowl in the bottom drawer of the cabinet and close it |
| T4 | 2% | put the white mug on the left plate and put the yellow and white mug on the right plate |
| T5 | 98% | pick up the book and place it in the back compartment of the caddy |
| T6 | 0% | put the white mug on the plate and put the chocolate pudding to the right of the plate |
| T7 | 48% | put both the alphabet soup and the cream cheese box in the basket |
| T8 | 16% | put both moka pots on the stove |
| T9 | 18% | put the yellow and white mug in the microwave and close it |

Extreme bimodal distribution: T5 (98%) and T3 (88%) near-perfect, while T6 (0%), T4 (2%), T1 (10%) near-zero.

## Cross-Suite Comparison (X-VLA Random k=0.85)

| Suite | SR | 
|-------|-----|
| Spatial | 68.2% |
| Object | 65.0% |
| Goal | 60.4% |
| **Long** | **35.0%** |

Long shows by far the worst performance at k=0.85, with a 25-33pp gap below the other suites. The Long suite's multi-step, multi-object tasks are most vulnerable to the disruption effect.

## Non-Monotonic Behavior on Long

| keep_ratio | Long SR | Tokens kept |
|------------|---------|-------------|
| k=0.5 | 61.6% | 25/50 |
| k=0.85 | **35.0%** | 42/50 |

Keeping MORE tokens (k=0.85) yields 26.6pp WORSE performance than keeping fewer (k=0.5). This is the strongest non-monotonic effect observed across all X-VLA suite × k combinations, confirming the disruption peak is amplified by task complexity.

For comparison, the disruption peak magnitude across suites:
- Long: k=0.85 (35%) vs k=0.5 (61.6%) → -26.6pp non-monotonic gap
- Object: k=0.85 (65%) — moderate, need k=0.5 (70.6%) for comparison → -5.6pp
- Spatial: k=0.85 (68.2%) vs k=0.5 (71.4%) → -3.2pp  
- Goal: k=0.85 (60.4%) vs k=0.5 (67.2%) → -6.8pp

## RoPE Disruption Hypothesis (D196) Verification

The disruption peak at k=0.85 is confirmed on Long and is the most severe across all suites. Key observations:

1. **X-VLA uses BART connector (no RoPE)**, yet still shows a disruption peak. This means the disruption is NOT exclusively a RoPE phenomenon — it's a more general positional/structural sensitivity in vision-language connectors.

2. **Task complexity amplifies the disruption**: Long (most complex, multi-step) shows 26.6pp non-monotonic gap, while simpler suites show 3-7pp gaps.

3. **Per-task variance is extreme on Long**: T5 (single object pick-place) is unaffected (98%), while T6 (two-object spatial arrangement) collapses to 0%. The disruption selectively destroys tasks requiring precise spatial reasoning with multiple objects.

## Conclusion

**SUCCESS** — The experiment completes the k=0.85 Random cross-suite profile for X-VLA and reveals that the disruption peak is dramatically amplified on Long (35.0%), the most complex suite. This is the strongest non-monotonic effect observed (-26.6pp vs k=0.5) and provides evidence that the disruption mechanism disproportionately affects multi-step, multi-object tasks regardless of connector architecture (BART vs MLP+RoPE).
