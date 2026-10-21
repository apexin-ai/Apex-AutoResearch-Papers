# ops m64 50k eval gate

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_m64-50k-eval-gate_20260521T023450_result.json`
- **Structured JSON:** [`aa3ad2865f383524ab43.json`](../../sessions/aa/aa3ad2865f383524ab43.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Summary:**

| | Status | Detail |
|--|--------|--------|
| **M64** | **Crashed** at step 50000 | Disk full → checkpoint corrupted, no valid checkpoints (save_every=50000). **Must restart from step 0.** |
| **M96** | Running, step 40400 | save_every=50000, will crash in **~5.3 hours** when it tries to save unless disk is freed |

**Disk: `/root/autodl-tmp` 250G/250G (100% full)**

Cleanup candidates:

| Path | Size | Notes |
|------|------|-------|
| `checkpoints/openvla_sc_m64_seed42/` (corrupted) | 14G | Safe to delete — file is corrupted |
| `.hf_cache/` | 99G | Likely has unused model downloads |
| `checkpoints/openvla_sc_m128/` | 38G | checkpoint.pt + checkpoint_step20000.pt |
| `openvla-7b-finetuned-libero-{spatial,goal,10}` | 45G | 3 finetuned model dirs, 15G each |
| `openvla-oft-libero-object` | 15G | |
| `pi05_libero_finetuned` | 7G | |

**Immediate needs:**
1. Delete the corrupted M64 checkpoint (14G) — no value, saves nothing
2. Free at least ~30G more so both M64 restart and M96's upcoming save have headroom
3. Restart M64 training with an earlier `save_every` (e.g. 10000) to avoid losing 50K steps again if something goes wrong

Which items should I clean up? And should I modify `save_every` to 10000 before restarting M64?

---
