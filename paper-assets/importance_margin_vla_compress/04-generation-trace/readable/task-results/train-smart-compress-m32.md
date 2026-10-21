# train smart compress m32

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_smart_compress_m32_20260517T173516_result.json`
- **Structured JSON:** [`67510c4bdbe7b9cf82cf.json`](../../sessions/67/67510c4bdbe7b9cf82cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练稳定运行。汇报如下：

---

## Smart Compress M=32 训练启动报告

| 项目 | 值 |
|---|---|
| **服务器** | cqa1-33015, GPU 0 (RTX 4090 D) |
| **PID** | 342374 (python 进程) |
| **总 steps** | 100,000 |
| **每 step 时间** | ~0.22s (稳定 sps ≈ 4.5) |
| **预计训练时长** | **~6.2 小时** (100000 / 4.5 / 3600) |
| **Checkpoint 间隔** | 每 1,000 steps（已从 10000 修改） |
| **GPU 显存占用** | 2,866 MiB / 24,564 MiB |
| **训练数据** | `HuggingFaceVLA/libero` (本地缓存 `/root/autodl-tmp/.hf_cache/lerobot/hub/datasets--HuggingFaceVLA--libero`) |
| **可训练参数** | 122M / 472M (25.85%), 其中 Compressor 22M, Expert+Projection 100M |
| **W&B** | offline 模式 |

### Loss 变化（log_every=50）

| Step | Loss | Grad Norm |
|---|---|---|
| 0 | 1.0367 | 51.78 |
| 50 | 3.2804 | 40.22 |
| 100 | 0.7217 | 11.42 |
| 150 | 0.4781 | 5.79 |
| 200 | 0.4456 | 5.45 |
| 250 | 0.3565 | 8.10 |
| 300 | 0.4607 | 3.46 |

Loss 从 1.04 快速下降到 ~0.4 附近，grad norm 从 51.78 降至 3-8 范围，训练收敛正常。

> 注：log 间隔为 50 步，无法获取逐 step 的前 10 步 loss。step 50 的 loss 异常高 (3.28) 可能是 warmup 初期学习率调整导致的正常波动。

---
