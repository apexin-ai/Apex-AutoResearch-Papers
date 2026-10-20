# check d134 s49 metrics s50

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-s49-metrics-s50_20260518T140130_result.json`
- **Structured JSON:** [`9820492f311a6049b0a0.json`](../../sessions/98/9820492f311a6049b0a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
s49 metrics:
  PR: 86/100
  H7: 73 (rate 84.88%)
  H1: 6 (strict)
  H8: 6 (rate 6.98%)
  genuine: 1 (rate 1.16%)
  CI (conclusion_in_premise): 79 (rate 91.86%)
  content_independent: 0
  isr_1: 5 (rate 5.81%)

s50 status: RUNNING step 97/500 (~19%), ~28min remaining
  GPU: 90% util, 84845 MiB used
  checkpoint-50 already saved

Disk: 223G/250G (89%, 28G free)
```

s49 genuine 只有 1 个，H7 严重主导（73/86）。磁盘 28G 剩余，s50 完成后可能偏紧，留意清理。

---
