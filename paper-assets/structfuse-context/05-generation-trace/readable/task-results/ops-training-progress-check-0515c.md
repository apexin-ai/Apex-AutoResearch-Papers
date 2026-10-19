# ops training progress check 0515c

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_training-progress-check-0515c_20260515T130214_result.json`
- **Structured JSON:** [`f6c2a97e61e362309b93.json`](../../sessions/f6/f6c2a97e61e362309b93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the summary:

---

## M2 Training Status — bjb1-42106 @ 2026-05-15 21:02 CST

**GPU utilization**: Both at 100%, GPU0 50.6/97.9 GB, GPU1 53.9/97.9 GB

| | Qwen M2 (cuda:0) | StarCoder M2 (cuda:1) |
|---|---|---|
| **PID** | 337267 (alive, 1d 1h38m) | 519791 (alive, 19h) |
| **Chain** | s43plus (9 subruns) | s43plus (seeds 43,44) |
| **Current subrun** | `embedding_distance_s44` (4/9) | `random_s44` (after random_s42,s43) |
| **Progress** | step 1600/2816 (57%) | step 900/2816 (32%) |
| **Latest eval** | @1500: R@1=0.5473, R@5=0.9421, val_loss=0.5256 | @500: R@1=0.4848, R@5=0.8952, val_loss=0.5913 |
| **Best R@1 (this subrun)** | **0.5942** @500 | **0.4848** @500 |
| **Best val_loss (this subrun)** | **0.4341** @1000 | **0.5913** @500 |
| **Early stopping** | val_loss patience 1/2 (may stop at eval@2000) | not triggered yet |
| **ETA (this subrun)** | ~4-5h (if not early stopped) | ~9-10h |

### Completed subruns so far

**Qwen**: random_s42 (R@1≈0.5503), random_s43, random_s44, embedding_distance_s43 — 4 done, current is #4/9 in s43plus chain (plus random_s42 done separately = 5 total done)

**StarCoder**: random_s42, random_s43 (best R@1=0.4912, early stopped @2500) — 2 done, on #3 overall

### Qwen embedding_distance_s44 trend
R@1 is declining: 0.5942 → 0.5813 → 0.5473. val_loss improved at step 1000 (0.4341) but spiked at step 1500 (0.5256). Likely to early stop at eval@2000 if val_loss doesn't recover.

### m1_reextract_v2
`all.jsonl`: **44,173 lines**. No active reextract process detected from log inspection.

---
