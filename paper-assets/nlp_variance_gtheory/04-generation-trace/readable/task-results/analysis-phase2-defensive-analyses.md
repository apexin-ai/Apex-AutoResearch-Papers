# analysis phase2 defensive analyses

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_phase2_defensive_analyses_20260521T224314_result.json`
- **Structured JSON:** [`1d0497498d5740844041.json`](../../sessions/1d/1d0497498d5740844041.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Results saved to `results/exp004_8model_analysis/defensive_analyses.json` on westd-32570. Summary:

### Part A: Bernoulli Baseline
| Benchmark | Observed Var | Bernoulli Var | Ratio |
|-----------|-------------|---------------|-------|
| MMLU | 0.0973 | 0.0001 | **980x** |
| ARC | 0.0753 | 0.0001 | **987x** |
| HellaSwag | 0.0800 | 0.0001 | **685x** |
| GSM8K | 0.0488 | 0.0001 | **462x** |
| MATH | 0.0647 | 0.0001 | **609x** |

Item difficulty differences are 460-987x larger than Bernoulli sampling noise. Reviewer concern fully addressed.

### Part B: MMLU Subsampling Stability
| n_items | item_id% | G_item |
|---------|----------|--------|
| 50 | 37.59 ± 4.43 | 0.8923 ± 0.0195 |
| 100 | 38.31 ± 2.31 | 0.8976 ± 0.0097 |
| 150 | 37.67 ± 1.53 | 0.8951 ± 0.0065 |
| 200* | 37.88 | 0.8962 |

All subsample sizes recover the 200-item reference within 1 SD. Results are not an artifact of specific item selection.

### Part C: LOBO Stability
Full set: MC mean = 36.0%, FF mean = 21.7%, diff = 14.3pp (MC > FF).

| Dropped | MC mean | FF mean | Diff | Stable |
|---------|---------|---------|------|--------|
| MMLU | 35.04 | 21.67 | 13.38 | Yes |
| ARC | 35.04 | 21.67 | 13.37 | Yes |
| HellaSwag | 37.88 | 21.67 | 16.22 | Yes |
| GSM8K | 35.99 | 26.48 | 9.51 | Yes |
| MATH | 35.99 | 16.86 | 19.13 | Yes |

**All 5/5 drops stable.** Removing HellaSwag (lowest MC) or MATH (highest FF) does not flip the MC > FF conclusion. Minimum gap is 9.5pp when dropping GSM8K.

---
