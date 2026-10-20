# analysis d141 task2 task3 combined

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d141_task2_task3_combined_20260518T132400_result.json`
- **Structured JSON:** [`0c50b25faf5d9a57ca24.json`](../../sessions/0c/0c50b25faf5d9a57ca24.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both tasks completed. Here's the summary:

---

## Part A: Conditional Success Decomposition

**Key findings across 3 datasets:**

| Dataset | Favorable (C1+C2) | Cond1-only | Cond2-only | Unfavorable |
|---------|-------------------|------------|------------|-------------|
| **SciERC** (529) | **+2.52pp** [0.03, 0.48] (42.9%) | -0.86pp (39.3%) | -1.80pp (7.0%) | 0.00pp (10.8%) |
| **CoNLL** (2756) | **-2.24pp** [-3.3, -1.3] (34.6%) | -1.91pp (16.9%) | 0.00pp (15.3%) | 0.00pp (33.1%) |
| **FewNERD** (32565) | **+0.47pp** [0.03, 0.07] (47.7%) | **+3.03pp** [2.7, 3.4] (38.5%) | -0.93pp (2.3%) | -0.15pp (11.4%) |

**Interpretation:**
- **SciERC**: LP selection only works when BOTH conditions are met (Favorable). Both conditions are necessary.
- **CoNLL**: LP selection hurts even in the Favorable bucket. High degeneracy (48%) means the two-condition framework can't rescue LP selection here.
- **FewNERD**: Non-degeneracy alone (Cond1) is sufficient for LP selection to help (+3pp), and the effect is actually stronger than in the Favorable bucket (+0.5pp). This suggests LP range isn't a prerequisite when the dataset has low degeneracy.

## Part B: Degeneracy-Capability Scatter Plot

**Spearman rho = 0.61, p = 0.06** (10 data points)

The correlation is primarily **dataset-driven**: CoNLL (F1 > 0.90) has 48-91% degeneracy; FewNERD (F1 ~0.75) has 14-31%; SciERC (F1 ~0.65) has 6-48%.

Within SciERC, the **epoch ablation** is striking: 3ep (6.4%) -> 5ep (17.8%) -> 10ep (47.8%) degeneracy with essentially flat F1 (~0.65). This suggests overfitting to dominant patterns, not capability improvement.

**All outputs on server:**
- Scripts: `analysis_d141_conditional_decomp.py`, `analysis_d141_scatter_plot.py`
- Part A: `output/d141_conditional_decomp/{results.json, report.md}`
- Part B: `output/d141_degeneracy_scatter/{scatter_plot.png, data_points.json, report.md}`

---
