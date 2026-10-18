# check cqa1 all gpu 20260519

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_cqa1_all_gpu_20260519_20260519T005428_result.json`
- **Structured JSON:** [`8cec3712f0239a1942eb.json`](../../sessions/8c/8cec3712f0239a1942eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个实验已完成，GPU 全部空闲。结果汇总：

```
GPU 0 (m32_goal):    完成 | SR=56.4% | per-task=[60,94,62,52,32,28,28,100,78,30]%
GPU 1 (m64_seed43):  完成 | SR=60.0% | per-task=[58,56,46,50,48,58,80,60,86,58]%  (libero_object)
GPU 2 (m32_spatial): 完成 | SR=53.2% | per-task=[58,62,52,82,28,18,82,70,56,24]%
GPU 3 (m32_seed43):  完成 | SR=59.2% | per-task=[72,38,68,36,68,48,86,44,96,36]%  (libero_object)
```

补充说明：
- **GPU 2 (m32_spatial)** task 9 完成后总 SR=53.2%，之前 partial task 0-8 数据完全吻合
- **GPU 3 (m32_seed43)** task 0-5 partial 也完全吻合之前记录，最终 SR=59.2%
- **GPU 1 (m64_seed43)** 跑的是 libero_object，注意这是 n_queries=64 的配置，SR=60.0%
- **GPU 3 (m32_seed43)** 也是 libero_object，n_queries=32，SR=59.2%（m32 vs m64 差距仅 0.8%）

---
