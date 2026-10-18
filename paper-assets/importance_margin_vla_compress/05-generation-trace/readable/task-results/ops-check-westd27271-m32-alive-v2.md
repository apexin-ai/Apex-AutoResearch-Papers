# ops check westd27271 m32 alive v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-westd27271-m32-alive-v2_20260520T211624_result.json`
- **Structured JSON:** [`148561e25df33e02db38.json`](../../sessions/14/148561e25df33e02db38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**状态: ALIVE**

| 项目 | 值 |
|------|-----|
| PID 921279 | **运行中**，CPU 301%，已运行 ~1900 分钟 |
| GPU 1 | 42189MiB / 97887MiB 显存占用，**0% 利用率** |
| tmux session | `train_openvla_sc_m32_seed42`（进程树完整，含 4 个 dataloader worker） |
| 训练命令 | `train_openvla_smart_compress.py --config configs/openvla_smart_compress_m32.yaml --resume checkpoints/openvla_sc_m32_seed42` |

GPU 1 利用率 0% 但显存高占用 + CPU 301%，说明当前正处于 **数据加载/预处理阶段**（或 checkpoint 保存），不是卡死——进程状态为 `Rl+`（running）。

另外 GPU 0 上有一个独立的 eval 任务在跑：`eval_openvla_l2norm_libero.py --k_ratio 0.7 --seed 43 --suite libero_object`，GPU 利用率 67%。

---
