# monitor 009d progress

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_009d-progress_20260516T014011_result.json`
- **Structured JSON:** [`5e322108d1c64310420f.json`](../../sessions/5e/5e322108d1c64310420f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_009d_baseline_walker_s0 训练状态

### 进程
- **PID 149708** 存活，已运行 **13h15m**
- 命令: `python dreamer.py --task dmc_walker_walk --steps 500000 --seed 0 --device cuda:0`

### 进度
| 指标 | 值 |
|------|-----|
| 当前 step | **312,000 / 500,000** (62.4%) |
| FPS | 7.24 |
| 最新 train_return | 972.8 (step 312K) |
| 最新 eval_return | **925.9** (step 308K) |
| metrics 行数 | 411 |

### 预计剩余时间
剩余 188K steps，FPS ~7.2 → **~26,100 秒 ≈ 7.3 小时**

### 最近 5 个 eval checkpoints

| Step | eval_return |
|------|-------------|
| 268K | 704.9 |
| 278K | 802.2 |
| 288K | 845.7 |
| 298K | 913.3 |
| 308K | **925.9** |

### GPU
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 (训练用) | 0% | 4165 / 97887 MiB |
| 1 | 32% | 4690 / 97887 MiB |

### 诊断
- **eval_return 持续上升**，从 268K 的 705 到 308K 的 926，学习曲线健康
- **GPU 0 利用率显示 0%** — 这可能是 `nvidia-smi` 采样瞬间处于 CPU 侧计算（环境交互/数据处理），不一定异常。显存占用 4.1GB 正常，进程存活且 metrics 在更新，FPS 7.2 稳定
- train_return 最新达 972.8，eval 925.9，Walker Walk 的 baseline 表现符合预期（DreamerV3 在 500K 时通常 ~900+）
- **无异常**，预计约 7 小时后完成

---
