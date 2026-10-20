# ops gpu health check v2

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_gpu_health_check_v2_20260520T092215_result.json`
- **Structured JSON:** [`6c1c1755ac4790ac6805.json`](../../sessions/6c/6c1c1755ac4790ac6805.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总完毕。

---

## GPU 健康度

| 服务器 | GPU | 型号 | 温度 | 显存占用 | 利用率 | 状态 |
|--------|-----|------|------|----------|--------|------|
| bjb1-40020 | GPU 0 | RTX 4090 (24GB) | 37°C | 3564/24564 MiB | 19% | 健康 |
| bjb1-40020 | GPU 1 | RTX 4090 (24GB) | 37°C | 2523/24564 MiB | 20% | 健康 |
| bjb1-45299 | GPU 0 | RTX PRO 6000 Black (96GB) | 29°C | 526/97887 MiB | 0% | 空闲 |
| bjb1-45299 | GPU 1 | RTX PRO 6000 Black (96GB) | 40°C | 2753/97887 MiB | 20% | 健康 |

## 实验进程状态

| 服务器 | GPU | 实验 | PID | 状态 | 当前步数 | 备注 |
|--------|-----|------|-----|------|----------|------|
| bjb1-40020 | 0 | exp_027_tcn_walker_s0_sigma02 | 37873 | **存活** | 160K / 210K | train_return ~615, fps 7.6 |
| bjb1-40020 | 0+1 | exp_029a_tcn_walker_s1_sigma02 | 50924 | **存活** | 28K / 210K | train_return ~155, 刚启动不久，无 .log 文件（仅 metrics.jsonl） |
| bjb1-45299 | — | exp_027_tcn_walker_s0 (σ=0.5) | — | **已退出** | 220K / 210K | EXIT_CODE=0，正常完成 |
| bjb1-45299 | 0+1 | exp_027_tcn_walker_s1 (σ=0.5) | 888926 | **存活** | 112K / 210K | train_return ~309, fps 9.5 |

## 已退出实验详情：exp_027_tcn_walker_s0 (bjb1-45299)

**log 最后 10 行：**
```
[220000] dataset_size 110000.0 / train_return 205.5 / train_length 500.0 / train_episodes 220.0
[220000] dataset_size 110000.0 / train_return 195.4 / train_length 500.0 / train_episodes 220.0
[220000] dataset_size 110000.0 / train_return 182.6 / train_length 500.0 / train_episodes 220.0
[220000] dataset_size 110000.0 / train_return 248.0 / train_length 500.0 / train_episodes 220.0
EXIT_CODE=0
```

**Checkpoint：** 未在对应 logdir 下找到 `latest.pt`（logdir 路径可能为相对路径，需确认实际写入位置）。但该实验已正常完成（EXIT_CODE=0），无需恢复。

## 额外发现

bjb1-40020 上还有 **exp_028_rave_walker_s0_ceil15**，log 停在 16:31（step 136K），nvidia-smi 无对应进程，疑似已退出。最后 train_return ~51，表现较差。

---
