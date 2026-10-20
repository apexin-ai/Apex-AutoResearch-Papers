# verify d103 seq8192 v2 confirm

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_verify_d103-seq8192-v2-confirm_20260515T174628_result.json`
- **Structured JSON:** [`a75de192beeacd2ce79f.json`](../../sessions/a7/a75de192beeacd2ce79f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D103 验证结果

| 项目 | 状态 |
|------|------|
| **PID** | 398981 存活，已运行 4m11s |
| **GPU 占用** | GPU0: 18,477/32,607 MiB (79%) — 进程绑定 `CUDA_VISIBLE_DEVICES=0` |
| **PYTORCH_ALLOC_CONF** | `expandable_segments:True` ✓ |
| **max_seq_length** | 8192 ✓ |
| **batch_size** | 1 ✓ |

**当前进度：**
- Checkpoint: **checkpoint-1800**（第 1/21 个）
- Samples: **1,430 / 9,335**
- running_acc: **87.6%**

**ETA 估算：**
- 推理速率：从 01:42:49→01:46:48 处理 1,420 samples = **~5.94 samples/sec（356 samples/min）**
- 总工作量：21 × 9,335 = **196,035 samples**
- 已完成：1,430 samples（0.7%）
- 剩余：~194,605 samples → **~32,760 sec ≈ 9.1 小时**（含 21 次模型加载 ~3 min 额外开销）
- 预估完成：**服务器时间 ~10:55**（当前服务器时间 ~01:47）

> 注：GPU1 (27,313 MiB, 97%) 和 GPU3 (22,527 MiB, 88%) 有其他任务占用，GPU2 空闲。

---
