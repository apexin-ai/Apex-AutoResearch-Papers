# ops check extended experiments

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-extended-experiments_20260519T131054_result.json`
- **Structured JSON:** [`bc8bdc5cb87736f16dda.json`](../../sessions/bc/bc8bdc5cb87736f16dda.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个 checkpoint 都在近期更新，实验都在跑。汇总：

## 实验状态汇报

### GPU 状态
| GPU | 型号 | 显存占用 | 利用率 | 温度 |
|-----|------|---------|--------|------|
| cuda:0 | RTX PRO 6000 Black (98GB) | 4.7GB | 32% | 42°C |
| cuda:1 | RTX PRO 6000 Black (98GB) | 9.5GB (2个进程) | 68% | 47°C |

3个 python 进程运行中：cuda:0 × 1, cuda:1 × 2。

### 实验进度

| 实验 | tmux session | 当前步数 | 进度 | 最新 train_return | 状态 |
|------|-------------|---------|------|-------------------|------|
| Walker baseline s2 | exp_s2_ext | **388K**/505K | 76.8% | 933~985 | 运行中 |
| Walker baseline s3 | exp_s3_ext | **264K**/505K | 52.3% | 888~936 | 运行中 |
| Walker baseline s4 | exp_s4_ext | **236K**/505K | 46.7% | 873~935 | 运行中 |

### 要点
- 三个实验全部正常运行，无异常
- s2 启动最早（12:10），进度领先；s3/s4 同时启动（17:03）
- FPS：s2=8.2, s3=9.6, s4=8.3
- train_return 均在 870~985 区间，表现正常
- 预计完成时间：s2 约 4h 后，s3/s4 约 8-9h 后

---
