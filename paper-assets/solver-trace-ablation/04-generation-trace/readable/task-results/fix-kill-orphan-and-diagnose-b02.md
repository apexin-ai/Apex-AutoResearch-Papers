# fix kill orphan and diagnose b02

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_kill-orphan-and-diagnose-b02_20260516T035942_result.json`
- **Structured JSON:** [`627d4c2424d64904c5e0.json`](../../sessions/62/627d4c2424d64904c5e0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## GPU 0 清理
- PID 604569: **KILLED**
- GPU 0 释放: **yes** (0 MiB, 0%)

## sweep-isr-b02-s42 诊断
- PID 625433: **不存在**（旧 PID）
- **实际 PID 626802: 仍在运行**，etime 6m04s，GPU 1 占用 80068 MiB
- 输出目录: 存在
- checkpoint 数量: **0**（尚未保存）
- reward_log 行数: **34**（最后 step=35, reward=0.57, prove_rate=50%）
- 死因: **未死** — 进程活着，35/500 steps (7%)，~7.6s/step，预计还需 ~59 分钟
- 注意: `--no_wandb` 模式，无 W&B 追踪

## GPU 全局状态
| GPU | 显存 | 利用率 |
|-----|------|--------|
| cuda:0 | 0 MiB | 0% |
| cuda:1 | 80077 MiB | 91% |

- 残留进程: PID 626802 (`python3 train_grpo.py ... sweep_isr_b02_s42`) on GPU 1
- tmux sessions: `sweep-isr-b02-s42` (1 window)
- PID 604563 (旧 sweep-isr-b01-s45 tmux server) 仍在进程表但 session 已不存在，可忽略

**GPU 0 已完全空闲可用。GPU 1 被 sweep-isr-b02-s42 正常占用。**

---
