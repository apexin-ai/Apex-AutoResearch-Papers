# ops 14b download check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b-download-check_20260522T183226_result.json`
- **Structured JSON:** [`d4907c08cbe96838ce36.json`](../../sessions/d4/d4907c08cbe96838ce36.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full status report:

## 1. Download Progress

**Status: 正常推进中**

- 当前大小: **9.2 GB** (`/dev/shm/Qwen3-14B/._____temp/`)
- 下载进程: ModelScope `snapshot_download` (PID 200698) 仍在运行，CPU 7.5%
- 之前在 02:01 时从 6.0G 回退到 16M 后重新下载，此后稳定增长

下载日志（来自 `cls14b-func-s42.log`）：
```
02:01 → 16M (重置)
02:03 → 499M
02:05 → 1.1G
...
02:31 → 8.8G
02:33 → 9.2G (当前)
```

- **速率**: ~293 MB/min (~4.9 MB/s)，30分钟内从 16M 增长到 8.8G，非常稳定
- **预计总大小**: Qwen3-14B BF16 约 28GB
- **预计剩余时间**: ~(28-9.2)/0.293 ≈ **64 分钟**，约 **03:37** 完成

所有 8 个 shard 文件已在 `._____temp/` 中创建（ModelScope 并行下载），尚未移至最终目录。

## 2. auto_train_14b.sh (GPU 0)

- **GPU 绑定**: `CUDA_VISIBLE_DEVICES=0`
- **进程状态**: 正在运行 (PID 200355)，当前处于 `sleep 120` 轮询循环中
- **触发条件**: 等待所有 8 个 shard 都 ≥1GB 且无 `.aria2` 残留文件
- **训练后自动 eval**: 是，训练完成后会在同一 GPU 上运行 `eval_verifier.py`
- **任务**: `cls` task, QLoRA 4bit, seed 42, batch 1, grad_accum 32, lr 5e-5, epochs 3

## 3. run_14b_eval.sh (GPU 1)

- **GPU 绑定**: `CUDA_VISIBLE_DEVICES=1`
- **进程状态**: 正在运行 (PID 202994)，当前处于 `sleep 60` 轮询循环中
- **触发条件**: 等待 ModelScope 下载进程结束 (`pgrep -f "snapshot_download.*Qwen3-14B"`)
- **eval 任务**: 0-shot 和 3-shot baseline 评估 (`eval_14b_baseline.py`)

## 4. GPU 状态

4x RTX 5090 (32GB each)，**全部空闲**，0% utilization，0 MiB memory used。等待下载完成后 GPU 0 和 GPU 1 将分别启动训练和 eval。

## 5. 执行链完整性

一切正常：
- 下载进程活跃，速率稳定 (~5 MB/s)
- `auto_train_14b.sh` 在 GPU 0 上轮询等待下载完成 → 自动启动训练 → 自动 eval
- `run_14b_eval.sh` 在 GPU 1 上轮询等待下载进程结束 → 自动启动 0-shot + 3-shot baseline eval
- 预计 ~1 小时后下载完成，两个脚本将同时触发

---
