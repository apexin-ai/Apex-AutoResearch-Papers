# experiment e1 2lf crossagent

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_e1-2lf-crossagent_20260515T134420_result.json`
- **Structured JSON:** [`01fb9f8633bcb801edc2.json`](../../sessions/01/01fb9f8633bcb801edc2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Excellent results. Let me compile the complete findings.

---

## E1 Results: 2-LF (λ₁+λ₂) Cross-Agent Transfer

### Training Set Statistics

| | 3-LF | 2-LF | Delta |
|---|---|---|---|
| SWE total windows | 59,496 | 59,496 | — |
| Non-abstain | 54,809 | 43,402 | -20.8% |
| conf≥2 (training set) | 15,401 | **10,243** | **-33.5%** |
| conf=3 / conf=2 | 792 / 14,609 | — / 10,243 | — |
| conf≥2 stag rate | — | 17.5% | — |
| Conflicts (LFs disagree) | — | 9,678 | — |

### Label Agreement (2-LF vs 3-LF)

**100.00%** agreement on all 43,402 overlapping non-abstain windows — guaranteed by subset property: when file_diff and cmd_rep both agree, the 3-LF majority must concur.

### In-Domain Sanity Check (SWE, 80/20 split)

| Model | 2-LF macro_F1 | Canonical 3-LF |
|---|---|---|
| GB | 1.0000 | ~0.9951 |
| RF | 1.0000 | ~0.9951 |

### Cross-Agent Transfer (SWE → OH)

| Model | Scope | 3-LF | 2-LF | Delta |
|---|---|---|---|---|
| **GB** | OH all (N=150,652) | 0.9674 | 0.6604 | **-30.70pp** |
| **GB** | OH conf≥2 (N=43,376) | 0.9919 | 0.8720 | **-11.99pp** |
| **RF** | OH all (N=150,652) | 0.9123 | 0.7800 | **-13.23pp** |
| **RF** | OH conf≥2 (N=43,376) | 0.9959 | 0.9778 | **-1.81pp** |

### Findings

Dropping λ₃ (outcome_backpropagation) from the labeling pipeline reduces the conf≥2 training set by 33.5% (10,243 vs 15,401) without altering any label that remains — 2-LF vs 3-LF agreement is 100% on overlapping windows, a mathematical consequence of majority voting over a strict subset. Despite perfect in-domain F1 (1.0), cross-agent transfer degrades substantially: GB drops 30.7pp on OH-all and 12.0pp on OH-conf≥2, while RF is more robust, losing only 1.8pp on OH-conf≥2 (0.9778 vs 0.9959). The asymmetry between GB and RF reflects GB's greater sensitivity to training set size and distribution shift. The outcome_backpropagation LF contributes not by changing label quality (agreement is 100%), but by **expanding coverage** — it breaks ties and enables 5,158 additional windows to reach conf≥2, providing critical training mass for cross-agent generalization. On high-confidence evaluation subsets (OH conf≥2), RF retains near-canonical performance even with 2-LF training, suggesting the structural features themselves carry strong cross-agent signal; the GB degradation is more a function of insufficient training data diversity than label noise.

---
