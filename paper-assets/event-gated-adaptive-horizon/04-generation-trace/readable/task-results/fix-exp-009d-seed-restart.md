# fix exp 009d seed restart

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_exp_009d_seed_restart_20260515T121403_result.json`
- **Structured JSON:** [`9e00ffab61032032e92d.json`](../../sessions/9e/9e00ffab61032032e92d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果

### 1. 已有数据的实际 seed
- **exp_009d_baseline_walker_s1**: 有 116K steps 数据和 `latest.pt` checkpoint，但无 config.yaml。目录名暗示 seed=1，checkpoint 内无 seed 字段，无法 100% 确认。
- **exp_009d_baseline_walker_s0**: 刚启动的新目录。

### 2. 策略
**无需操作 — 实验已经在运行。**

PID 145173 已经在 cuda:0 上运行 `exp_009d_baseline_walker_s0`：
```
python dreamer.py --configs defaults dmc_proprio --task dmc_walker_walk \
  --logdir logdir/exp_009d_baseline_walker_s0 --steps 500000 --seed 0 \
  --compile False --device cuda:0
```
进程创建于 20:14:23（约 1 分钟前），当前在 step 5000，已有 8 个 train episode 文件正常生成。

### 3. 训练状态
- nvidia-smi 确认 PID 145173 在 GPU 0 上占用 794MiB
- metrics.jsonl 最后修改时间 20:15:22，活跃写入中
- 当前 step: 5000（刚过 seed episode 收集阶段，进入训练循环）

### 4. Logdir
`/root/autodl-tmp/event-gated-adaptive-horizon/logdir/exp_009d_baseline_walker_s0`

---
