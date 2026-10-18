# audit westd38929 gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_westd38929_gpu_status_20260526T172754_result.json`
- **Structured JSON:** [`efbfe0b828268326fa89.json`](../../sessions/ef/efbfe0b828268326fa89.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
WESTD-38929 GPU STATUS:
GPU0: busy | PID=623613 | eval_openvla_l2norm_libero.py --mode l2norm_prune --k_ratio 0.5 --suite libero_10 (seed42) | MEM=15880/97887 MiB
GPU1: busy | PID=668245 | eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.85 --suite libero_10 (seed42) | MEM=15780/97887 MiB
GPU2: idle  | PID=- | - | MEM=1/97887 MiB
GPU3: busy | PID=514356 | eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.85 --suite libero_10 (seed42) | MEM=16118/97887 MiB

TMUX_SESSIONS:
  eval_openvla_attn_k085_long_seed42_v3 (created May 26 19:09)
  eval_openvla_random_k085_long_seed42_v3 (created May 26 23:23)

IDLE_GPUS: 2
```

3 个 OpenVLA LIBERO-10 评估实验在跑，全部用 openvla-7b-finetuned-libero-10 模型、50 episodes、seed 42。GPU2 空闲可用。

---
