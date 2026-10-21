# eval acts2 checkpoint inventory

**The Probe Reward Trap: Behavioral Death Before Distributional Collapse in Sycophancy Calibration** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_acts2-checkpoint-inventory_20260522T175645_result.json`
- **Structured JSON:** [`44269f4fa61dc7162afd.json`](../../sessions/44/44269f4fa61dc7162afd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### Checkpoint 列表（按修改时间）

| Checkpoint | 修改时间 |
|-----------|---------|
| checkpoint-2000 | May 22 20:24 *(resume 起点)* |
| checkpoint-3000 | May 22 21:20 |
| checkpoint-2500 | May 22 21:41 |
| checkpoint-3500 | May 22 22:36 |
| checkpoint-4000 | May 22 23:54 |
| checkpoint-4500 | May 23 01:11 |

共 6 个 checkpoint。注意 ckpt-2000 和 ckpt-3000 的时间早于 ckpt-2500，可能是 resume 前遗留的旧 checkpoint，新训练从 ckpt-2500 开始写入。

### 当前训练状态

- **最新日志 step: 4800** (train_log.jsonl 最后一行)
- **进程 PID 494017 仍在运行**，已运行 7h07m，CPU 96%
- **GPU 1** 占用 23270MiB / 97887MiB，但当前 GPU-Util 0%（可能正处于 checkpoint 保存或 log flush 间隙）
- 训练速度：约 **9.1s/step**（从日志推算）

### save_steps 推断

checkpoint 间距为 500（2000→2500→3000→3500→4000→4500），**save_steps = 500**。

### 下一个 checkpoint 预估

- checkpoint-5000 预计在 step 4800 基础上再跑 200 步 ≈ 200 × 9.1s ≈ **30 分钟后**（约 02:27 服务器时间）

### 之前步数不一致的解释

之前报告的 step 3360 可能是另一个 worker 读到了旧日志或未刷新的状态。实际训练已推进到 **step 4800/8000（60%）**，与 ckpt-4500 的存在一致。

### 补充说明

- 命令行写的 `--device cuda:0`，但 nvidia-smi 显示 PID 494017 实际在 **GPU 1** 上
- GPU 0 上另有一个进程 PID 516696（占 38188MiB）

---
