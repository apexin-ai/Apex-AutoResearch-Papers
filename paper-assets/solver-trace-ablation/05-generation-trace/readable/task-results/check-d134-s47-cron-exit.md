# check d134 s47 cron exit

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_d134-s47-cron-exit_20260518T115141_result.json`
- **Structured JSON:** [`b3890af895188191bada.json`](../../sessions/b3/b3890af895188191bada.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正常 pipeline 推进，不是崩溃。

```
Pipeline: ALIVE
s47 status: COMPLETE (eval + classify done at 11:51:27 UTC)
s47 eval results:
  - PR: 97% (97/100)
  - ISR*: n/a (see classify breakdown)
  - Hacking modes: H1=1, H7=83 (all H7a), H8=10, H9=0
  - Content-independent: 8
  - Genuine: 3 (3.1%)
  - Total proofs evaluated: 100

Current run: s48 at step 4/500 (~10.4s/it, ETA ~86 min)
GPU: RTX PRO 6000, 81.4G/97.9G used, 91% util
Disk: 223G/250G (89%)
```

s47 结果很差——97 个 proved 中 83 个是 H7（conclusion in premise），10 个 H8（conjunction collapse），只有 3 个 genuine。s48 刚启动正常训练中。

---
