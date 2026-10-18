# code prepare m128 train script

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_prepare_m128_train_script_20260518T013452_result.json`
- **Structured JSON:** [`77004e4ff9e465019e9a.json`](../../sessions/77/77004e4ff9e465019e9a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。创建了两个文件：

**`configs/smart_compress_m128.yaml`** — 继承 `smart_compress.yaml`，仅覆盖 `num_queries: 128` 和 `output_dir`

**`run_train_m128.sh`** — 启动脚本，格式与 M=96/M=16 的运行方式完全一致：
- `CUDA_VISIBLE_DEVICES=X`（待分配）
- `HF_HOME=/root/autodl-tmp/.hf_cache HF_HUB_OFFLINE=1 WANDB_MODE=offline`
- `--config configs/smart_compress_m128.yaml --wandb_run smart_compress_m128`
- 输出到 `train_M128.log`

**完整参数（继承自 smart_compress.yaml）：**

| 参数 | 值 |
|---|---|
| num_queries | **128**（control，不压缩） |
| num_heads | 12 |
| num_layers | 2 |
| total_steps | 100,000 |
| batch_size | 4 |
| lr | 1e-4 |
| warmup_steps | 1,000 |
| decay_lr | 2.5e-6 |
| grad_clip | 10.0 |
| seed | 42 |
| weight_decay | 1e-10 |

**显存预估：** M=96 当前占用 ~2.6GB（进程 RSS），M=128 的 cross-attention query 多 33%，预计 ~2.8-3.0GB，不会成为瓶颈。

GPU 编号留 `X`，未启动，等 Director 分配。

---
