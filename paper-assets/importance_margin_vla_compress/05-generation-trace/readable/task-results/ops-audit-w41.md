# ops audit w41

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_audit-w41_20260527T171317_result.json`
- **Structured JSON:** [`6ef938b29dfbd1fb05b5.json`](../../sessions/6e/6ef938b29dfbd1fb05b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
GPU0: [运行中] PID=781014 eval_pi05_l2norm_k075_long — Task 7完成(76.0%), 累计78.2%, 进入Task 8
GPU1: [完成]   PID=756250 eval_pi05_attn_k095_long — SR=77.2%, EXIT_CODE=0 (17:13 UTC完成)
GPU2: [运行中] PID=840142 eval_pi05_random_k075_long — Task 4进行中(ep30=77%), 累计68.0%
GPU3: [运行中] PID=821246 eval_pi05_l2norm_k07_long — Task 4进行中(ep40=55%), 累计74.5%
```

**注意**: GPU 3 上额外跑了 PID 816713（cascade_gpu3.sh 启动的 `l2norm k=0.95 libero_10`），两个进程共享 GPU 3 显存（共 21.7GB）。

**GPU 1 最终结果**: `libero_10 prune=attention keep=0.95 SR=77.2%`，结果已保存到 `eval_results/pi05_attention_k0.95_libero_10_seed43.json`。

---
