# verify libero 4gpu status

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_libero_4gpu_status_20260516T155758_result.json`
- **Structured JSON:** [`b90bf80fe0e16ef3badd.json`](../../sessions/b9/b90bf80fe0e16ef3badd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU 利用率:
  cuda:0: 16% / 2.7GB — libero_full_ft_baseline (seed=42) step 24050/100K
  cuda:1:  6% / 2.1GB — libero_lora_baseline (seed=42) step 24250/100K
  cuda:2: 38% / 2.1GB — libero_lora_seed0 (seed=0) step 3850/100K
  cuda:3: 27% / 2.7GB — libero_fullft_seed0 (seed=0) step 3500/100K

Registry 注册: 已完成 (libero_lora_seed0, libero_fullft_seed0 → RUNNING)
```

4 张卡全部在训练。Baseline 对（seed=42）已跑到 ~24K steps，seed=0 对刚启动约 16 分钟（~3.5K steps），速度 ~4 sps，预计各需 ~6.5 小时完成 100K steps。

---
