# audit westd27271 westd41074 unregistered

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd27271_westd41074_unregistered_20260526T172811_result.json`
- **Structured JSON:** [`1ffb3f9d6fa8186240fc.json`](../../sessions/1f/1ffb3f9d6fa8186240fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
WESTD-27271:
GPU0: 71% util, 16.0/97.9 GB | PID=414927 | l2norm_prune k=0.75 libero_goal seed42
GPU1: 83% util, 16.2/97.9 GB | PID=397225 | attention_prune k=0.5 libero_10 seed42

WESTD-41074:
GPU0: 85% util, 16.0/97.9 GB | PID=682346 | random_prune k=0.85 libero_object seed42
GPU1: 69% util, 16.0/97.9 GB | PID=652888 | attention_prune k=0.5 libero_object seed42
GPU2: 87% util, 16.0/97.9 GB | PID=755986 | attention_prune k=0.75 libero_object seed42
GPU3: 70% util, 16.0/97.9 GB | PID=642262 | l2norm_prune k=0.75 libero_object seed42
```

所有 6 个 GPU 均在跑实验，无空闲 GPU，无未注册进程。全部都是 `eval_openvla_l2norm_libero.py` 的不同配置（mode/k_ratio/suite 组合）。

注意：westd-27271 GPU1 的 PID 397225 确认是 `attention_prune k=0.5 libero_10`（非 `libero_long`，tmux session 名为 `eval_attn_k05_long` 但实际 cmdline 参数是 `libero_10`）。

---
