# code fix llama eval script

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_llama_eval_script_20260521T020209_result.json`
- **Structured JSON:** [`97fc540f1dbc0218b50c.json`](../../sessions/97/97fc540f1dbc0218b50c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Correctly picks `epoch_1` (highest complete checkpoint). When training finishes and `epoch_2` appears, it'll pick that instead.

All 3 fixes applied:

**P1 — TG checkpoint path**: Replaced hardcoded `epoch_2/1/0` loop with dynamic `ls | sort -rn` that finds the highest completed epoch with both `gate_params.pt` and `lora/`. Currently resolves to `epoch_1`, will auto-pick `epoch_2` when training completes.

**P2 — Autoregressive eval**: Already present (steps were in the script). Verified the mechanism: omitting `--conversations-path` triggers `build_conversation()` which generates responses via `model.generate()`. GAR is then measured with gating active. This correctly captures the TF-AR gap for C5.

**P3 — LoRA-only guard**: Added 4 LoRA-only eval steps (TF ours/dongre + AR ours/dongre) with `--gate-type none --checkpoint-dir $LO_CKPT`. All wrapped in `if [ -n "$LO_CKPT" ]` — prints WARNING and skips when checkpoint doesn't exist (current state). Auto-detects from `runs/phase2_llama_lo_s42/epoch_*/lora/`.

**Script structure** (12 steps, 4 guarded):
| Part | Steps | Commands |
|------|-------|----------|
| TF | Base ours/dongre | 2 |
| TF | LO ours/dongre (guarded) | 2 |
| TF | TG ours/dongre | 2 |
| AR | Base ours/dongre | 2 |
| AR | LO ours/dongre (guarded) | 2 |
| AR | TG ours/dongre | 2 |

---
