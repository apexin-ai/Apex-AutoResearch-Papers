# eval mistral s4s7 theta fixed

**What Can IRT Person-Fit Statistics Reveal About SFT-Stage Benchmark Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_mistral-s4s7-theta-fixed_20260521T170408_result.json`
- **Structured JSON:** [`e768b3270b11ce86b345.json`](../../sessions/e7/e768b3270b11ce86b345.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Checkpoint 不存在，任务停止。**

35694 上 `/root/autodl-tmp/ctrl_contam_mistral/checkpoints/` 只有：
- clean, clean_s2, clean_s3, clean_s8, clean_s9, clean_s10, contam_15, contam_50

缺少 **clean_s4, clean_s5, clean_s6, clean_s7** — 这 4 个 checkpoint 在已释放的 19912 上，未迁移到 35694。无法重跑 eval。

---
