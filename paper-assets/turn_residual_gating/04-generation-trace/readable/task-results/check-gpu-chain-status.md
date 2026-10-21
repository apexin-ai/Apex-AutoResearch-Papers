# check gpu chain status

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_chain_status_20260524T022604_result.json`
- **Structured JSON:** [`508bd1a2648c5bbba4af.json`](../../sessions/50/508bd1a2648c5bbba4af.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU Chain Status Report

**GPU**: RTX PRO 6000 (97.9GB), PID 131153 running, 94% util, 31GB VRAM used, 67°C

**Chain progress (steps 1-4 done, step 5 running):**

| Step | Task | Status | Time |
|------|------|--------|------|
| 1/7 | SS s123 eval | Done | completed 01:59 CST |
| 2/7 | SS s456 resume training | Done | completed 08:32 CST |
| 3/7 | SS s456 eval | Done | completed 09:04 CST |
| 4/7 | Qwen-1.5B Phase 1 diag | Done | completed 09:07 CST |
| **5/7** | **Qwen-1.5B TG training** | **Running** | started 09:07 CST |
| 6/7 | Qwen-1.5B eval | Pending | |
| 7/7 | MMLU eval (6 ckpts) | Pending | |

**Step 5 details (Qwen-1.5B TG v7 s42):**
- Currently at **Epoch 1 Step 4600** (3 epochs total, ~8000 total steps → **~57% complete**)
- Epoch 0 completed at ~09:58 CST (51 min), checkpoint saved
- Training healthy: L_NTP ~1.0-1.1, Gate mean ~0.977, Memory 21.8GB
- Interesting gate profile: L3 notably low (~0.71), L5 somewhat low (~0.91), most other layers near 1.0

**ETA:**
- Step 5 remaining: **~1 hour** (epoch 1 finishing + full epoch 2)
- Steps 6-7 after that: ~1.5-2.5 hours
- **Full chain completion: ~2.5-3.5 hours from now** (~13:00-14:00 CST)

**Eval results:** No qwen15b or MMLU eval outputs yet (expected — still in training). Only existing eval results are from v9_pcgrad runs.

**No errors.** Training is stable, no anomalies.

---
