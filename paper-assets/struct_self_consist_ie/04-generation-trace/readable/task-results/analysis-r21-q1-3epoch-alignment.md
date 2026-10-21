# analysis r21 q1 3epoch alignment

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r21_q1_3epoch_alignment_20260518T133524_result.json`
- **Structured JSON:** [`446953c82dd11b59f117.json`](../../sessions/44/446953c82dd11b59f117.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results:

| Setting | N_inst | N_rho | N_samp | Median ρ(LP,F1) | Mean ρ | 95% CI | %pos | LP_sel Δ |
|---------|--------|-------|--------|-----------------|--------|--------|------|----------|
| 3-epoch | 529 | 495 | 8 | **0.3192** | 0.2726 | [0.2753, 0.3856] | 76.36% | -1.24pp |
| 5-epoch | 529 | 435 | 8 | **0.2624** | 0.1791 | [0.1956, 0.3637] | 64.14% | +0.64pp |

Key findings:

1. **3-epoch median ρ = 0.32 vs 5-epoch median ρ = 0.26** (diff = +0.057). The 95% CIs overlap substantially ([0.28, 0.39] vs [0.20, 0.36]), confirming alignment is a dataset-intrinsic property, not an epoch artifact.

2. 3-epoch has far fewer constant-F1 (degenerate) instances (34 vs 94), so more instances contribute valid ρ values (495 vs 435). The slightly higher ρ at 3-epoch may partly reflect reduced degeneracy giving cleaner signal.

3. LP selection Δ is negative for 3-epoch (-1.24pp) vs positive for 5-epoch (+0.64pp). This is consistent with the known SciERC pattern where LP is a weak selector, and the 5-epoch model's slightly better LP selection may come from higher degeneracy (more constant-F1 instances inflate the greedy baseline denominator differently).

Script saved at `analysis_r21_q1_alignment.py`, outputs at `output/r21_q1_alignment/{results.json, report.md}`.

---
