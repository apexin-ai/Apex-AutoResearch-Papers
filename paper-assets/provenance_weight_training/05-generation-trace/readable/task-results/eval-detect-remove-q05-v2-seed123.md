# eval detect remove q05 v2 seed123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_detect_remove_q05_v2_seed123_20260521T233914_result.json`
- **Structured JSON:** [`b44ee0af3205e29f431d.json`](../../sessions/b4/b44ee0af3205e29f431d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry already fully updated. A previous worker completed the evals and wrote all fields:

| Dataset | Loss | PPL |
|---------|------|-----|
| Holdout | 2.8545 | 17.366 |
| OWT | 2.9013 | 18.198 |
| Wiki | 2.7234 | 15.232 |

- **status**: DONE
- **conclusion**: success
- **checkpoint_path**: `/root/autodl-tmp/provenance_weight_training/output/models/detect_remove_q05_v2_seed123/final`
- **log_path**: `~/runs/provenance_weight_training/detect_remove_q05_v2_seed123.log`

Holdout PPL 17.366 vs seed42's 17.285 — consistent across seeds as expected for full D&R. No action needed.

---
