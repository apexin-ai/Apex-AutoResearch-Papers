# ops bjb1 c prime crash diagnosis

**Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_bjb1_c_prime_crash_diagnosis_20260522T000104_result.json`
- **Structured JSON:** [`7c108d7392fb908cae69.json`](../../sessions/7c/7c108d7392fb908cae69.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No step 7 metrics were logged — crash happened before metric output. Here's the complete diagnosis.

---

## Diagnosis: exp029_intervention_c_prime crash

### Steps Completed
All 7 training steps ran. Step 7 metrics weren't logged because the checkpoint save crashed before the log flush.

### Per-Step Metrics (from console log)

| Step | train_success | val_success | response_length/mean | pass@8 |
|------|--------------|-------------|---------------------|--------|
| 0 (init val) | — | **9.375%** | — | — |
| 1 | 9.375% | — | — | 50.0% |
| 2 | 7.8% | — | 7,858 | 50.0% |
| 3 | 12.5% | — | 8,809 | 50.0% |
| 4 | **26.6%** | — | 6,165 | 43.8% |
| 5 | 12.5% | **21.875%** | 8,327 | 43.8% |
| 6 | 6.25% | — | 8,198 | 31.3% |
| 7 | *(not logged — crash)* | *(not logged)* | — | — |

W&B run `zndyygbn` has **zero data points** — metrics were never synced.

### Step 5 Checkpoint: INTACT

Path: `/root/autodl-tmp/checkpoints/exp029_intervention_c_prime/global_step_5/actor/`

| File | Size |
|------|------|
| model_world_size_2_rank_0.pt | 4.06 GB |
| model_world_size_2_rank_1.pt | 4.06 GB |
| optim_world_size_2_rank_0.pt | 6.88 GB |
| optim_world_size_2_rank_1.pt | 6.88 GB |
| extra_state (x2) | 15 KB each |
| huggingface/ | config + tokenizer |

Total: **21 GB** — complete, all files present, usable for OOD eval.

### Step 7 Checkpoint: CORRUPT

Path: `global_step_7/actor/` — 16 GB, model files saved but optim files are truncated (4.3GB/4.0GB vs expected 6.9GB), no extra_state, no huggingface dir.

### Crash Root Cause

1. Step 7 training completed, final `_save_checkpoint()` triggered
2. Model files saved OK to data partition (`/root/autodl-tmp/`)
3. `torch.save(optimizer_state_dict, optim_path)` failed with `inline_container.cc:668` enforce failure — zip writer couldn't write expected bytes
4. During Ray atexit cleanup: `OSError: [Errno 28] No space left on device: '/tmp/ray/session_.../ray_spilled_objects_...'`

The **root partition** (30G overlay) was exhausted by Ray object spilling to `/tmp/ray/` during the checkpoint save. The data partition has plenty of space (879G, only 186G used).

### Disk Status Now

| Partition | Size | Used | Avail |
|-----------|------|------|-------|
| Root (overlay, /tmp) | 30G | 8.4G (28%) | **22G free** |
| Data (/root/autodl-tmp) | 879G | 186G | 817G free |
| /tmp/ray/ (6 stale sessions) | 270MB | — | — |

Root has recovered (temp files cleaned on crash), but 6 old Ray sessions remain in `/tmp/ray/`.

### Retry Feasibility

**Retry is possible** after cleanup, but may not be necessary:

- Step 5 checkpoint is intact and usable for OOD eval
- The step 4→5→6 train_success trajectory (26.6% → 12.5% → 6.25%) shows high variance — step 5 val at 21.875% (up from 9.375% baseline) is the reliable signal
- If you do want to retry for a clean step 7 save:
  1. Delete corrupt step 7 dir (`rm -rf /root/autodl-tmp/checkpoints/exp029_intervention_c_prime/global_step_7/`) — frees 16GB
  2. Clean old Ray sessions (`rm -rf /tmp/ray/session_2026-05-21*`) — frees ~230MB on root
  3. Set `RAY_TMPDIR=/root/autodl-tmp/ray_tmp` to spill objects to data partition instead of root overlay

---
