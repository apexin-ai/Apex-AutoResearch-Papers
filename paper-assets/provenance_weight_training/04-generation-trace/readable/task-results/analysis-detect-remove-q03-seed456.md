# analysis detect remove q03 seed456

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_detect_remove_q03_seed456_20260519T014009_result.json`
- **Structured JSON:** [`6fb6e7aa3f330e3f357c.json`](../../sessions/6f/6fb6e7aa3f330e3f357c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**结果**: seed456 的 eval_ppl_holdout = **17.2509**, eval_loss_holdout = **2.8479**，与 seed42 (PPL=17.25, loss=2.848) 几乎完全一致（PPL delta = +0.0009）。

**2-seed 统计**: mean PPL = 17.2505, std = 0.0006。D&R q03 阈值的结果跨 seed 高度稳定，不是随机波动。

Registry 已更新为 DONE/success。seed123 仍在运行，完成后可计算 3-seed 统计。

---
