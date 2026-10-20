# ssh theta crit sweep

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_theta_crit_sweep_20260522T082613_result.json`
- **Structured JSON:** [`d0757be3590c674448c7.json`](../../sessions/d0/d0757be3590c674448c7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results saved. Here's the summary:

**θ_crit = 0.70 is robust.** The sweep across θ ∈ {0.60, 0.65, 0.70, 0.75, 0.80} shows:

- **Only CoNLL configs are sensitive** — they cluster at D = 0.63–0.70, so lowering θ to 0.60 reclassifies them as FAIL. SciERC (D ≈ 0.12–0.21) and FewNERD (D ≈ 0.12–0.46) are always classified as "pass" across the entire sweep range.

- **No conclusion changes**: α ≈ 0.068 (signal alignment) is the binding constraint, not degeneracy. The bound is loose by a factor of 8–33×. Whether θ is 0.60 or 0.80, the same methods fail for the same reasons.

- **Entity construction is independent of θ_crit**: It operates at entity-level (frequency threshold θ = 2/N = 0.25), not sample-level. FewNERD: +1.40pp, SciERC: +0.32pp, CoNLL: −0.39pp — none change with θ_crit.

Script: `code/theta_crit_sweep.py`
Output: `output/theta_crit_sweep_results.txt`

---
