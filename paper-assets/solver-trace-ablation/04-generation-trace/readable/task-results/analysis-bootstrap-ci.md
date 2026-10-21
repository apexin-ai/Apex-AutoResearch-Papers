# analysis bootstrap ci

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_bootstrap-ci_20260515T070938_result.json`
- **Structured JSON:** [`d44ad627956b3aa0ab37.json`](../../sessions/d4/d44ad627956b3aa0ab37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Script ran successfully. Results saved to `/root/autodl-tmp/outputs/bootstrap_ci_results.json`.

Summary of results:

**Per-experiment bootstrap 95% CIs (on proved samples):**

| Experiment | PR | H7 | H1 | Genuine | ISR* |
|---|---|---|---|---|---|
| exec_only_s42 | .93 [.88,.98] | 0% | 86.0% [78.5,92.5] | 14.0% [7.5,21.5] | .132 [.095,.173] |
| isr_b01_s42 | .81 [.73,.88] | 14.8% [7.4,23.5] | 44.4% [33.3,55.6] | 40.7% [29.6,51.9] | .415 [.349,.482] |
| random_b01_s42 | .79 [.71,.87] | 0% | 63.3% [51.9,73.4] | 36.7% [26.6,48.1] | .131 [.101,.163] |
| isr_b03_s43 | .86 [.79,.92] | 2.3% [0,5.8] | 67.4% [57.0,76.7] | 30.2% [20.9,40.7] | .295 [.246,.345] |
| random_b03_s43 | .92 [.86,.97] | 0% | 58.7% [48.9,68.5] | 41.3% [31.5,51.1] | .180 [.159,.203] |
| exec_only_s44 | .97 [.93,1.0] | 100% | 0% | 0% | .567 [.536,.603] |

**Key comparisons (permutation test):**
- ISR β=0.1 vs Random β=0.1 genuine rate: diff=+0.04, p=0.637 (not significant)
- ISR β=0.1 vs Random β=0.1 H7 rate: diff=+0.148, **p=0.0004**
- Exec-only vs ISR β=0.1 H1 rate: diff=+0.416, **p<0.001**
- ISR β=0.1 vs Random β=0.1 ISR*: diff=+0.284, **p<0.001**
- ISR β=0.3 vs Random β=0.3 genuine: diff=-0.111, p=0.156 (not significant)

**Missing experiments:** SFT baseline (plan009) has no eval file on the server — checkpoint was likely deleted in a prior disk cleanup. The ISR β=0.1 vs Random β=0.1 genuine rate comparison is NOT significant (p=0.637), meaning the genuine rate advantage doesn't survive bootstrap with n=100.

---
