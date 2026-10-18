# train smart compress m64

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_smart_compress_m64_20260517T173525_result.json`
- **Structured JSON:** [`d86d3d750202ee74fc25.json`](../../sessions/d8/d86d3d750202ee74fc25.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练正常运行。汇总结果：

**训练启动成功**

| 项目 | 值 |
|---|---|
| **PID** | 341605（Python 进程，父 bash PID=341600） |
| **GPU** | cuda:1，占用 2782 MiB / 24564 MiB |
| **总 steps** | 100,000 |
| **每 step 时间** | ~0.24s（sps≈4.0-4.2，稳定后） |
| **预计训练总时长** | ~6.6 小时（100000 / 4.1 / 3600） |
| **Checkpoint 保存间隔** | 每 1000 steps |
| **训练数据** | HuggingFaceVLA/libero（LIBERO 全 130 task demos，与 M=32 相同） |
| **Compressor 参数量** | 22,210,560（22.2M） |
| **总可训练参数** | 122,091,552（122M，占总参数 25.85%） |

**前几个 step 的 loss**（log_every=50）：

| Step | Loss |
|---|---|
| 0 | 2.1065 |
| 50 | 0.5919 |
| 100 | 0.4934 |
| 150 | 0.2990 |
| 200 | 0.5101 |

注意：Compressor 参数量 22.2M 与 M=32 相同——因为 `num_queries` 只影响 learnable query 数量（64×960 vs 32×960 = 30720 参数差异），cross-attention 层参数不变，所以 log 显示的 22.2M 是取整后的同一数字。实际 M=64 比 M=32 多约 30K 参数。

另外注意：wandb 使用 offline 模式（服务器未配置 wandb API key），数据保存在本地 `wandb/offline-run-*` 目录。

---
