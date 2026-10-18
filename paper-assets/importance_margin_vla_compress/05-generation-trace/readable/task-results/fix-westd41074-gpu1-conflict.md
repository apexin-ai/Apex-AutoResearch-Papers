# fix westd41074 gpu1 conflict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd41074_gpu1_conflict_20260526T135356_result.json`
- **Structured JSON:** [`9943867f3ae54165e6f1.json`](../../sessions/99/9943867f3ae54165e6f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

westd-41074 每个 GPU 各一个进程，PID 652888 独占 GPU 1。

```
KILL: PID 657544 on westd-41074 — done
REDEPLOY: eval_openvla_l2norm_k05_long_seed42 on westd-38929 cuda:0 — done
NEW_PID: 623613
VERIFY_41074: GPU1 single process (PID 652888) — yes
VERIFY_38929: GPU0 single process (PID 623613) — yes
```

---
