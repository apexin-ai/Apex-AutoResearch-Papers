# deploy westd38929 attn k05 goal

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd38929_attn_k05_goal_20260526T161201_result.json`
- **Structured JSON:** [`5ac585e0af3a079fab22.json`](../../sessions/5a/5ac585e0af3a079fab22.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU_OCCUPIED**

cuda:1 上 PID 668245 仍在运行 Random k=0.85 Long：
```
python -u eval_openvla_l2norm_libero.py --mode random_prune --k_ratio 0.85 --suite libero_10 --num_episodes 50 --seed 42 --model_path /root/autodl-tmp/models/openvla-7b-finetuned-libero-10 --unnorm_key libero_10
```

GPU 状态：16188 MiB / 97887 MiB, 65% utilization。四张卡全部占用，无空闲 GPU。

```
DEPLOYED: no
SERVER: westd-38929
GPU: cuda:1
REASON: GPU_OCCUPIED — PID 668245 running Random k=0.85 Long (libero_10), 16169 MiB
ALL_GPUs: 4/4 occupied
```

---
