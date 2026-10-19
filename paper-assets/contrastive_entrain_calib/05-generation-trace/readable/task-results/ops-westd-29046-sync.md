# ops westd 29046 sync

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd-29046-sync_20260518T223141_result.json`
- **Structured JSON:** [`990644f42858fc5cac70.json`](../../sessions/99/990644f42858fc5cac70.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All verification passed. Here's the full summary of both steps:

**Step 1 — exp-002 recalibration at step 500:**
- Direction recalibration was **never implemented**. The training code loads d_syc statically from `results/exp001/directions.pt` (shape [36, 2, 4096]) and never updates it during training.
- No `recalib`, `direction_update`, or similar logic exists in any training file.
- R1 oscillation (step 500: -0.23, step 650: -0.50, step 760: +0.21) is not caused by direction recalibration — the directions are fixed throughout training.

**Step 2 — eval file sync to westd-29046:**
- `nli_utils.py` — already matched (2712 bytes both sides), no transfer needed.
- `eval_pipeline.py` — transferred successfully (70585 bytes).
- Verification results:
  - `ls -la`: both files present in `/root/contrastive_entrain_calib/eval/`
  - `from nli_utils import get_entailment_idx` → `nli_utils OK`
  - `import eval_pipeline` → `eval_pipeline OK`
  - `python3 eval_pipeline.py --help` → outputs full CLI usage with all expected flags (`--model-path`, `--lora-path`, `--compare-base`, `--benchmarks`, `--sycon-max-turns`, etc.)

---
