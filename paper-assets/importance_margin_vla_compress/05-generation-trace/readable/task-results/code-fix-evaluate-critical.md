# code fix evaluate critical

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-evaluate-critical_20260515T165023_result.json`
- **Structured JSON:** [`ff80ab83026c7aaa203f.json`](../../sessions/ff/ff80ab83026c7aaa203f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Baseline dry-run completed successfully. All 8 conditions evaluated:

| Condition | action_loss |
|-----------|-------------|
| eps0.0_pruneFalse | 0.0490 |
| eps0.0_pruneTrue | 0.0168 |
| eps0.01_pruneFalse | 0.0042 |
| eps0.01_pruneTrue | 0.0064 |
| eps0.02_pruneFalse | 0.0067 |
| eps0.02_pruneTrue | 0.0229 |
| eps0.05_pruneFalse | 0.0144 |
| eps0.05_pruneTrue | 0.0180 |

**Summary of all changes:**

1. **`imm/smolvla_wrapper.py`** — `compute_importance_scores()` now accepts optional `noise`/`time` parameters. If not provided, samples fresh (backward compatible). When provided, uses them deterministically so clean vs perturbed comparisons share identical noise.

2. **`evaluate.py`** — 5 changes:
   - Helper `compute_importance_scores()` passes `noise`/`time` through to wrapper
   - `evaluate_full` accepts `tokenizer` param
   - Batch preprocessing via `preprocess_batch` (tokenizes language, moves to device)
   - Baseline path uses `baseline_forward` from train.py (bypasses action_is_pad masking)
   - IMM path generates `det_noise`/`det_time` once per batch, reuses for both clean and perturbed scores

3. **Dry-run**: Baseline step_5000 — **PASS** (all 8 conditions). No IMM checkpoints yet to test.

---
