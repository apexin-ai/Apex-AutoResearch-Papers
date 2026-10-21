# paper appendix update

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_appendix_update_20260525T135051_result.json`
- **Structured JSON:** [`df62f2d4f63da9bfbe31.json`](../../sessions/df/df62f2d4f63da9bfbe31.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes verified. Summary of modifications to `docs/paper/sections/appendix.tex`:

**Complete results table — 7 new rows + 1 update:**
- Line 35: **068** (Factorial repro s1) — eval 39.1, NVE 4.12×, Full collapse (shaded)
- Line 37: **008f s4** updated — eval 306.5→289.3, NVE 1.41→0.76 (per exp_073)
- Line 42: **008a_s3** — eval 855.9, Healthy
- Line 48: **067** (Frozen emb s0) — eval 281.5, NVE 0.19×, Healthy
- Line 58: **008e_v3 s5** — eval 853.1, NVE 0.61×, Healthy
- Lines 84-87: **060/061/062** (Cartpole Swingup baseline/trigger/control, 3 seeds each)

exp_071 (008f s3, eval 311.9) skipped — already present as "009c s3" with identical eval.

**Cross-domain table:** Added Cartpole Swingup row (0/3 trained, 0/3 control, No CIVO — single-joint).

**Cartpole paragraph:** Added after cross-domain table, confirming CIVO requires multi-joint dynamics.

**ROC caption:** n=30→56, AUROC=0.957→0.990, FPR=0.18→0.09, added accuracy=53/56 and F1=0.941, updated false positive descriptions to match n=56 analysis.

**Supporting text:** Updated n=30 references at lines 249 and 293 for consistency.

---
