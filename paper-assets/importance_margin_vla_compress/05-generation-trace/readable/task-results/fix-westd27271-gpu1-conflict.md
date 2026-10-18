# fix westd27271 gpu1 conflict

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_westd27271_gpu1_conflict_20260526T160422_result.json`
- **Structured JSON:** [`c4d5b01271adaae5110f.json`](../../sessions/c4/c4d5b01271adaae5110f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 冲突已解决，397225 独占 GPU 1 正常运行。

```
WESTD-27271:
  PID_357375: killed
  PID_397225_STATUS: correct_params (auto-mapped suite=libero_10 -> model_path + unnorm_key)
  ATTN_K05_LONG: running (PID=397225, verified)
  ACTUAL_CMDLINE: python -u eval_openvla_l2norm_libero.py --mode attention_prune --k_ratio 0.5 --suite libero_10 --seed 42 --gpu 0
    (auto-mapped: model_path=/root/autodl-tmp/openvla-7b-finetuned-libero-10, unnorm_key=libero_10)
  GPU1_MEM: 16169 MiB (单进程，357375 已释放)

WESTD-41074:
  GPU0: PID 682346 - random_prune k=0.85 object seed42 (15961 MiB)
  GPU1: PID 652888 - attention_prune k=0.5 object seed42 (15961 MiB)
  GPU3: PID 642262 - l2norm k=0.75 object seed42 (15965 MiB)
  GPU2_STATUS: idle (无 Random k=0.5 Object 进程，tmux session eval_openvla_random_k05_object_seed42_v2 存在但进程已结束)
```

---
