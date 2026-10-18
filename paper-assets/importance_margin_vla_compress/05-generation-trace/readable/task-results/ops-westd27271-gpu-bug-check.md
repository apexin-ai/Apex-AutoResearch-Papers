# ops westd27271 gpu bug check

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd27271_gpu_bug_check_20260522T080641_result.json`
- **Structured JSON:** [`1a3033176ba376335d73.json`](../../sessions/1a/1a3033176ba376335d73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 1 已成功分配。三个进程状态：

| PID | GPU | 显存 | 实验 |
|-----|-----|------|------|
| 119111 | GPU 0 (61b3...) | 10554 MiB | random_k07_spatial |
| 119449 | GPU 0 (61b3...) | 10554 MiB | l2norm_k07_spatial |
| 212585 | GPU 1 (7c68...) | 10545 MiB | l2norm_k095_object (新) |

## 总结

**GPU 分配 Bug 确认**：`eval_pi05_pruning_libero.py` 第 79 行 `DEVICE = "cuda:0"` 硬编码，`--gpu` 参数（第 47 行）定义了但从未用于设备选择。所有进程无论传什么 `--gpu` 都跑 GPU 0。

**现有实验进度**：
- `random_k07_spatial`：T7/T10 完成，SR=69.8%，已运行 ~84 min
- `l2norm_k07_spatial`：T7 ep40/50，SR~69.4%，已运行 ~72 min
- 两个都过半，让它们在 GPU 0 上跑完

**新实验部署**：`eval_pi05_l2norm_k095_object_seed43` 已通过 `CUDA_VISIBLE_DEVICES=1` 成功部署到 GPU 1，模型已加载完毕开始评估（l2norm pruning, keep 243/256 tokens）。

**修复建议**：将第 79 行改为 `DEVICE = f"cuda:{args.gpu}"` 以正确使用 `--gpu` 参数，避免后续实验再出现 GPU 争抢。

---
