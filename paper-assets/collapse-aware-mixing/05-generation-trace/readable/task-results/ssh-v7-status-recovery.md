# ssh v7 status recovery

**collapse aware mixing** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_v7-status-recovery_20260513T081752_result.json`
- **Structured JSON:** [`d0a073baf4c8a628ba93.json`](../../sessions/d0/d0a073baf4c8a628ba93.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## v7 训练状态

### 1. 进程存活 ✓
- **PID 60437**，状态 `Rl`（运行中），CPU 105%
- 命令：`python3 pilot_pipeline.py --output_dir /root/autodl-tmp/output_v7 --num_generations 3 --tokens_per_generation 20000000 --checkpoint_interval_tokens 5000000 --holdout_size 5000 --learning_rate 0.000002 --no_wandb --seed 42`
- tmux session `mvp_pilot_v7` 正常，启动于 10:35

### 2. 当前阶段：G0 synth gen
- 进度条：`generate: 62% | 189/306 [4:01:02<2:29:13, 76.53s/it]`
- output_v7 目录下只有 `G0/` 和 `real_data_cache/`，尚未进入 G1

### 3. 剩余时间估算
- G0 synth gen 剩余：117 batches × 76.5s ≈ **2h29m**
- 之后还有 G1 train + G1 eval + G1 synth gen + G2 train + G2 eval
- 按 G0 synth gen 用时 ~6.5h 推算，整个 pipeline（3 generations）预计还需 **12-15h**

### 4. 磁盘空间
- `/root/autodl-tmp/`：250G 用了 183G，剩余 **68G (27%)**
- 当前阶段是生成合成数据，后续训练 checkpoint 会持续占用空间，68G 应该够但偏紧，建议关注

### 5. GPU
- 利用率：**65%**（生成任务，正常）
- 显存：**28.9G / 97.9G**（~30%，A800 96GB）

**结论：v7 进程在服务器重启后存活，正常运行中。当前处于 G0 合成数据生成阶段，约 2.5h 后进入 G1 训练。**

---
