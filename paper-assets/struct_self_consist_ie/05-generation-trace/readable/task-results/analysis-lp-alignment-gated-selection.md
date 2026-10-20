# analysis lp alignment gated selection

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_lp_alignment_gated_selection_20260519T011937_result.json`
- **Structured JSON:** [`46341889de36ba4498ea.json`](../../sessions/46/46341889de36ba4498ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Experiment complete. Here are the results:

## LP-Alignment-Gated Selection Results

### Core Finding: Adjusted Score = mean_rho × valid_ratio

Raw `mean_rho` fails on CoNLL (0.32 passes threshold despite LP being harmful) because only 51.6% of instances have computable rho (high degeneracy). Multiplying by `valid_ratio` fixes this.

### Summary (adjusted score, threshold=0.3) — all 3 datasets correct

| Dataset | mean_rho | Valid% | adj_score | Decision | Greedy | LP | Gated |
|---------|----------|--------|-----------|----------|--------|----|-------|
| SciERC  | 0.178    | 88.5%  | 0.158     | greedy   | 64.42  | 64.65 | 64.42 |
| CoNLL   | 0.322    | 51.6%  | 0.166     | greedy   | **90.70** | 89.60 | **90.70** |
| FewNERD | 0.503    | 92.9%  | 0.468     | LP       | 74.78  | **76.66** | **76.66** |

### Threshold Robustness (adjusted score)
- **thr=0.2, 0.3, 0.4**: all 3 datasets correct
- thr=0.1: SciERC/CoNLL incorrectly pick LP
- thr=0.5: FewNERD incorrectly picks greedy

### Probe Size Sensitivity (threshold=0.3, adjusted)
100% consistency across 10 random seeds for all probe sizes (50–all), all 3 datasets. Even 50 probes suffice for a stable decision.

### Key Insight
CoNLL's high degeneracy rate (48.4% of instances have constant F1 across all 16 samples) inflates raw rho by only averaging over the non-degenerate half. The adjusted score naturally down-weights this, making it a reliable gating signal.

### Outputs
- Script: `/root/autodl-tmp/struct_self_consist_ie/code/lp_alignment_gated_selection.py`
- Results JSON: `/root/autodl-tmp/struct_self_consist_ie/output/prescriptive_analysis/lp_alignment_gated.json`
- LaTeX table included in the log output

---
