# check d134 post restart

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-post-restart_20260518T125831_result.json`
- **Structured JSON:** [`ef196bb3d9c7da37f5ed.json`](../../sessions/ef/ef196bb3d9c7da37f5ed.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status:

```
Pipeline tmux: ALIVE (d134-pipeline, created Mon May 18 18:52:28)
Cleaner tmux: ALIVE (d134-cleaner, created Mon May 18 20:02:21)

Completed runs: 2/10
  1. d134_4b_isr_b01_s47 — COMPLETE (train+eval+classify, 16G, model kept)
  2. d134_4b_isr_b01_s48 — COMPLETE (train+eval+classify, 17M, model cleaned)

Current run: d134_4b_isr_b01_s49 — step 92/500 (~18%, ~50 min remaining @ ~7.5s/step)

Pending: ISR s50, s51, Random s47–s51 (7 runs)

GPU: GPU 0 — 84220/97887 MiB, 93% util, PID 41453
Disk: 223G/250G (89%) ⚠️

Per-run eval results:
- s47 ISR: PR=97/100, H7=83, H1=1, H8=10, genuine=3 (3.1%), ISR≈0.55
- s48 ISR: PR=66/100, H7=66, H1=0, H8=0, genuine=0 (0.0%), ISR≈0.49
```

Key observations:
- **s48 recovered**: previously marked failed at step 199, but the pipeline successfully retrained and completed it this time (though PR dropped to 66% with 100% H7 rate among proved samples — all 66 proved samples are H7 shortcut proofs)
- **Disk at 89%** is concerning — with 7 more runs, the cleaner needs to keep up. Each run generates ~16G of model files before cleanup
- **s48 results are degenerate**: 100% H7 rate, 0 genuine — the model collapsed into pure shortcut mode on this seed. s47 is better (3 genuine) but still 85.6% H7
- **ETA for full pipeline**: at ~1h per train + ~6min eval + ~5min classify per run ≈ ~8h for remaining 8 runs (s49 finishes in ~50min)

---
