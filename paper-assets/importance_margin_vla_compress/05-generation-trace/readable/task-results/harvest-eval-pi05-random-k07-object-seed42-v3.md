# harvest eval pi05 random k07 object seed42 v3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_harvest_eval_pi05_random_k07_object_seed42_v3_20260523T230117_result.json`
- **Structured JSON:** [`818ce32b6a89216cf0f2.json`](../../sessions/81/818ce32b6a89216cf0f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程仍在运行，并未退出。**

- PID 467663：`python -u eval_pi05_pruning_libero.py --prune_mode random --keep_ratio 0.7 --suite libero_object --seed 42` 在 GPU 2（CUDA_VISIBLE_DEVICES=2）上运行中，占用 ~10245 MiB 显存，CPU 时间 43 分钟。
- 日志只显示到 T0 是因为 nohup `>` 重定向有 buffer 延迟，实际进程一直在跑。

同时还发现 GPU 2 旁边两个同类进程也在跑：
- **GPU 3**：k=0.5 object seed42 v2 (PID 379140)
- **GPU 0**：k=0.9 object seed42 v2 (PID 459609)
- **GPU 1**：另一个进程 (PID 315972)

4 张 GPU 都在使用中，无空闲 GPU。

不应执行收割操作，需要等进程完成。是否需要设置 cron 轮询等待？

---
