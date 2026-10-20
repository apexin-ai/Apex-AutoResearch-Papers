# code exp natural experiment

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp-natural-experiment_20260520T125039_result.json`
- **Structured JSON:** [`8987f41e3c2ea1982daf.json`](../../sessions/89/8987f41e3c2ea1982daf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's a summary of the results:

## Natural Experiment Results

**Setup**: 21 base/chat pairs × 4 benchmarks (MMLU, HellaSwag, ARC-Challenge, GSM8K), 63 models for IRT fitting, 61 valid (pair, benchmark) data points. 9/21 pairs had all 4 benchmarks (gaps due to missing HF data for `huggyllama/llama-7b`, `mosaicml/mpt-30b`, `meta-llama/Llama-2-7b-hf`).

**Two benchmarks show significant systematic Δlz* deviations** (one-sample t-test on within-pair deviation from pair mean):

| Benchmark | Mean Δlz* | Mean Deviation | t | p |
|---|---|---|---|---|
| MMLU | -1.32 ± 5.12 | +1.17 | +1.52 | 0.150 |
| **HellaSwag** | -6.82 ± 5.56 | **-3.40** | **-3.97** | **0.001** |
| ARC-Challenge | -3.87 ± 2.45 | -0.46 | -0.91 | 0.378 |
| **GSM8K** | +0.43 ± 1.20 | **+3.92** | **+3.35** | **0.009** |

**Key findings**:
1. **HellaSwag** shows the largest lz* drop after instruction-tuning (mean Δlz*=-6.82), significantly more negative than the pair average. This likely reflects that alignment changes response patterns on sentence-completion tasks in ways IRT models flag as aberrant.
2. **GSM8K** shows the opposite — lz* barely changes (mean Δlz*=+0.43), with deviation significantly above pair mean. Chat models' GSM8K improvements are more IRT-consistent, possibly because CoT reasoning produces "legitimate" performance gains.
3. **No individual pair outliers** detected (|z| > 1.5 within pairs), suggesting benchmark-level systematic effects rather than pair-specific contamination.
4. The **deviation heatmap** clearly shows the HellaSwag column systematically blue (negative) and GSM8K column systematically red (positive).

**Outputs**: `artifacts/natural_experiment/` — `pairs_data.csv`, `deviation_analysis.csv`, 4 plots, `natural_experiment_summary.json`, `natural_experiment_report.md`, `natural_experiment.py`.

---
