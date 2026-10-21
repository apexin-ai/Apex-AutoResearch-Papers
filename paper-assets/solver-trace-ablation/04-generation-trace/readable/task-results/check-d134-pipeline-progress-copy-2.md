# check d134 pipeline progress

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-pipeline-progress_20260518T115041_result.json`
- **Structured JSON:** [`6c7ce9a057bba0bbfe8b.json`](../../sessions/6c/6c7ce9a057bba0bbfe8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
Pipeline status: ALIVE
Session: d134-pipeline (created Mon May 18 18:52:28 local / 10:52 UTC)
Completed runs: 1/10
Current run: d134_4b_isr_b01_s48 at step ~8/500
Current UTC: ~11:52

Run order: ISR s47→s48→s49→s50→s51, Random s47→s48→s49→s50→s51

Per-run results (completed only):
- d134_4b_isr_b01_s47:
    PR=97%, ISR*(train-final)=0.359
    H7=83, H1=1, H8=10, Genuine=3 (3.1%), CntIndep=8

Timing:
  s47 training: 57 min (500 steps @ ~6.8s/step)
  s47 eval+classify: ~2 min
  Total per run: ~59 min
  9 remaining × 59 min ≈ 8.9h
  ETA: ~20:45 UTC (May 18) — significantly earlier than the original 05/19 05:00 estimate

GPU: RTX PRO 6000 Black, 16299/97887 MiB, 69% util (PID 20893)
Disk: 223G/250G used (89%) — 28G free, ~15G per checkpoint, tight for 9 more runs
```

Disk is the main concern: 28G free with 9 runs to go. The pipeline script preserves weights only for seed 47 and deletes others (optimizer + global_step removed), but each full model is ~15G. If all 10 checkpoints are kept, that's 150G which won't fit. Check whether the cleanup logic in the script is aggressive enough — currently it only preserves s47 weights and strips the rest down to just model files, but even stripped that's still ~15G per run.

---
