# ops restart 14b 17855 batch

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_restart-14b-17855-batch_20260522T094618_result.json`
- **Structured JSON:** [`a33886bee16ca4daa987.json`](../../sessions/a3/a33886bee16ca4daa987.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both experiments launched and verified. Final state on 17855:

| GPU | PID | Experiment | Status |
|-----|-----|-----------|--------|
| 0 | 661775 | **t10_a050_s42_fp32_14b** (NEW) | Gen 0, 10.3GB, fixed code |
| 1 | 662119 | **t15_a050_s42_fp32_14b v3** | Resumed gen 2, 10.3GB, fixed code |
| 2 | 655764 | t10_a075_14b v2 | 29GB, old code |
| 3 | 655841 | t10_a060_14b v2 | 29GB, old code |
| 4 | 577241 | t25_a045_s43 410M | 14.5GB, since 08:19 |
| 5 | 603938 | t20_a075_s43 410M | 14.5GB, since 12:10 |

New PIDs: **661775** (cuda:0, t10_a050) and **662119** (cuda:1, t15_a050_v3). Both loaded post-MAUVE-fix code. GPU memory at 10.3GB indicates model loaded, will grow to ~29GB during training steps.

Note: GPUs 2-3 still run v2 experiments with pre-fix code — Director only requested restart for cuda:0/cuda:1.

---
