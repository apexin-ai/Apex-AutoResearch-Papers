# check exp 005 health

**Why Temporal Abstraction Can Fail in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp_005_health_20260513T164322_result.json`
- **Structured JSON:** [`3f5e312d687990d0b74b.json`](../../sessions/3f/3f5e312d687990d0b74b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp_005 健康状态报告

### 进程状态
| 实验 | PID | 状态 | 运行时间 | CPU% |
|------|-----|------|---------|------|
| exp_005 (event_gated_v4) | 51721 | **ALIVE** | 35m32s | 0.0% (瞬时值，正常) |
| exp_001 (baseline) | 9409 | **ALIVE** | 14h40m | 1128% (多线程env采集) |

### GPU 状态
| GPU | 型号 | 利用率 | 显存占用 |
|-----|------|--------|---------|
| cuda:0 (baseline) | RTX PRO 6000 | 2% | 4165/97887 MiB |
| cuda:1 (exp_005) | RTX PRO 6000 | 28% | 4173/97887 MiB |

GPU 利用率 2%-28% + 显存 ~4GB：DreamerV3 是 CPU-bound（env step + replay buffer），GPU 只在 world model 更新时短暂使用，这是正常行为，不是问题。

### 训练进度 (exp_005)
- **当前 step: ~16000**，dataset_size=8000，16 episodes 已收集
- **eval_return@5K: 31.0** → **eval_return@15K: 153.9**（5x 提升，学习曲线健康）
- **train_return@16K: 115~169**（持续上升）
- model_loss: 23.5→7.6（下降正常），value_loss: 9.5→3.3（下降正常）
- **gate_dt_mean=1.0, gate_dt_1_frac=1.0**：gate 尚未激活（全部选 dt=1），gate_loss=0, gate_scale=0 — warmup 阶段 gate 被冻结，符合预期
- FPS: ~7.3（DreamerV3 on single GPU 正常范围）

### 结论
**exp_005 健康。** 进程存活，reward 稳步上升（eval 31→154），losses 正常下降，gate 处于 warmup 冻结期（全 dt=1）符合设计。两个实验均正常运行。

---
