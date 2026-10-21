# eval d014 baseline gate

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_d014_baseline_gate_20260515T210432_result.json`
- **Structured JSON:** [`b66598720c7239c46d9b.json`](../../sessions/b6/b66598720c7239c46d9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 3 baseline evaluations and registry update complete. Here's the summary:

---

## D014 Baseline Eval Results

### Task 1: Final eval (500 batches) — `eval_results/eval_baseline_v5_final.json`
**Checkpoint:** `checkpoints/baseline/step_029999`

| Condition | action_loss | margin_median | preservation_rate | LED_median |
|---|---|---|---|---|
| `eps0.0_pruneFalse` | 0.004077 | 0.01002 | 1.0000 | 0.0 |
| `eps0.0_pruneTrue` | 0.11897 | 0.01092 | 1.0000 | 0.0 |
| `eps0.01_pruneFalse` | 0.004579 | 0.01033 | 0.3352 | 0.0 |
| `eps0.01_pruneTrue` | 0.11898 | 0.01041 | 0.3375 | 0.0 |
| `eps0.02_pruneFalse` | 0.005580 | 0.01063 | 0.3362 | 0.0 |
| `eps0.02_pruneTrue` | 0.12176 | 0.01072 | 0.3356 | 0.0 |
| `eps0.05_pruneFalse` | 0.018037 | 0.01094 | 0.3381 | 0.0 |
| `eps0.05_pruneTrue` | 0.13948 | 0.01114 | 0.3362 | 0.0 |

**Meta:** `lipschitz_empirical=0.0`, `lipschitz_spectral=0.0`

### Task 2: Mid-checkpoint (50 batches) — `eval_results/eval_baseline_v5_step5000.json`
**Checkpoint:** `checkpoints/baseline/step_005000`
- `clean_action_loss`: 0.01891 | `clean_margin_median`: 0.01002

### Task 3: Mid-checkpoint (50 batches) — `eval_results/eval_baseline_v5_step10000.json`
**Checkpoint:** `checkpoints/baseline/step_010000`
- `clean_action_loss`: 0.00974 | `clean_margin_median`: 0.01002

### Key D014 Gate-relevant observations (baseline reference)
- **Baseline clean_action_loss (G3 denominator):** 0.004077
- **Baseline margin_median (G1 denominator for 2x):** 0.01002
- **Baseline preservation_rate @ eps0.01 (G2 baseline):** 0.3352
- **All LED ratios = 0** (baseline has no ACIS/Lipschitz estimation)
- **Training trajectory:** action_loss dropped from 0.01891 (step 5k) → 0.00974 (step 10k) → 0.004077 (step 30k)

Registry `mvp_baseline_v5.metrics` updated with all three eval datasets.

---
