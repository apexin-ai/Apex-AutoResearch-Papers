# ops d134 random pipeline full sync

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_d134-random-pipeline-full-sync_20260518T174303_result.json`
- **Structured JSON:** [`d6e41ccc6a2bf7b78627.json`](../../sessions/d6/d6e41ccc6a2bf7b78627.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All registry updates complete. Here's the summary:

| seed | train | eval | classify | registry | 关键指标 |
|------|-------|------|----------|----------|---------|
| s47 | 500/500 ✅ | ✅ | ✅ | DONE/success | PR=89%, ISR=0.086, H1=88.8%, H7=0%, H8=4.5%, genuine=6.7% |
| s48 | 25/500 🔄 | — | — | RUNNING (cron registered) | step 25, reward=0, prove_rate=0% (early) |
| s49 | — | — | — | PREPARING | not started |
| s50 | — | — | — | PREPARING | not started |
| s51 | — | — | — | PREPARING | not started |

**GPU**: cuda:0 — PID 121901, 84368 MiB / 97887 MiB, 90% util (s48 training)

**Disk**: 223G / 250G (89%) — 28G free. Each completed seed with model weights takes ~15G. After s48 finishes + eval, disk will be tight for s49-s51. Pipeline should handle cleanup of intermediate checkpoints per C003, but worth monitoring.

**Pipeline**: s48 training at step 25/500, ETA ~1h 7min remaining. The pipeline tmux session (d134-pipeline) is managing sequential execution of s47→s51. s49-s51 will run sequentially after s48 completes its train+eval+classify cycle.

---
