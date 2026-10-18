# ops 14b gpu status check

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b_gpu_status_check_20260519T043631_result.json`
- **Structured JSON:** [`c96656d022bbc4f26776.json`](../../sessions/c9/c96656d022bbc4f26776.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 报告

### nvidia-smi

| GPU | 进程 | PID | 显存 | GPU利用率 | 温度 | 功耗 |
|-----|------|-----|------|-----------|------|------|
| cuda:0 | python | 776616 | 32304 MiB | 100% | 57°C | 298W/600W |
| cuda:0 | python | 776770 | 32302 MiB | | | |
| cuda:1 | (无) | - | 0 MiB | 0% | 32°C | 36W/600W |

### PID 存活状态

- temp09 PID 776596 存活：**YES**（bash wrapper，子进程 python PID=776616）
- topk50 PID 776750 存活：**YES**（bash wrapper，子进程 python PID=776770）

### tmux sessions

- `qwen25_14b_temp09` — created 11:00:03
- `qwen25_14b_topk50` — created 11:00:05

### 日志状态

两个日志都只有 15 行，模型权重加载已完成（100%），当前处于 d0 生成阶段。生成进度未写入日志（tqdm 用 `\r` 覆盖行，日志文件未刷新新进度）。

### 关键问题：两个实验都跑在 cuda:0 上

topk50 的 bash wrapper 设置了 `CUDA_VISIBLE_DEVICES=1`，但日志头打印的是 `CUDA_VISIBLE_DEVICES=0`，nvidia-smi 也确认 PID 776770 在 GPU 0 上。**run script 内部可能覆盖了 CUDA_VISIBLE_DEVICES**，导致两个 14B 模型（共 ~64GB）挤在同一张 GPU 上，cuda:1 完全空闲。

建议检查 `scripts/run_qwen25_14b_topk50.sh` 是否有硬编码 `CUDA_VISIBLE_DEVICES=0`。

---
