# code v72 contrastive gradient fix

**action cond info bottleneck** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_v72-contrastive-gradient-fix_20260517T083634_result.json`
- **Structured JSON:** [`6426e8c0880b4d1c52bc.json`](../../sessions/64/6426e8c0880b4d1c52bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes complete. Summary of modifications on the server (`/root/acib`):

**1. `acib/config.py`** — Added `lambda_drift: float = 0.1`

**2. `acib/acib_policy.py`** — Three changes:
- `_connector_hook`: conditional detach — keeps gradient path alive in `connector_scorer` mode (`output` without `.detach()`), detaches in all other modes
- `__init__`: saves `_connector_ref_params` (frozen weight snapshot) when `freeze_mode == "connector_scorer"`
- `_compute_connector_drift_loss()`: L2 drift penalty against reference weights
- `forward()`: adds `lambda_drift * drift_loss` to total loss, logs as `"connector_drift"`

**3. `scripts/train_acib.py`** — Added `--lambda_drift` CLI arg (default 0.1), passed to `ACIBConfig`, logged to wandb

**4. `scripts/run_v7.2_connector_scorer.sh`** — Added `--lambda_drift 0.1`

Verification passed: config instantiation and module import both succeed.

---
