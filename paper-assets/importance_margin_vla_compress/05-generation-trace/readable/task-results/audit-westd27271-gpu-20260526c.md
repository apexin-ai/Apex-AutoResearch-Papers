# audit westd27271 gpu 20260526c

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd27271-gpu-20260526c_20260526T200726_result.json`
- **Structured JSON:** [`43029a953b0603381cea.json`](../../sessions/43/43029a953b0603381cea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 0: BUSY  PID=414927  L2norm k=0.75 Goal seed42 v2  VRAM=15964MiB  Util=69%
  — Task 10/10 Ep 40/50, 即将完成

GPU 1: BUSY  PID=397225  Attn k=0.5 Long (libero_10) seed42  VRAM=16358MiB  Util=68%
  — Task 5/10 Ep 20/50, 约一半进度

已完成实验：
- eval_attn_k09_goal_s43: SR=73.20% (366/500), 来源=log ✓

异常：
- eval_spatial_baseline_s42: 停在 Task 8/10，无 Overall SR，日志停更于 May 26 17:12，无对应进程 — 疑似 crash
```

---
