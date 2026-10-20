# train p0 nmin 5

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_p0_nmin_5_20260524T160125_result.json`
- **Structured JSON:** [`e441578c9c9b7751a2a0.json`](../../sessions/e4/e441578c9c9b7751a2a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`p0_nmin_5` 已在 cuda:1 上启动，registry 已更新为 RUNNING。

当前状态：step 12/6103，ETA ~3.5h，n_min=5 的 ESS 被钳在 4（= batch_size），weighting 暂未生效（b=0, weighted_loss = unweighted_loss），符合预期——n_min 过高导致约束过紧。

---
