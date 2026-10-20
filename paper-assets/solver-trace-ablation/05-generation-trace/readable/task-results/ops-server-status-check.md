# ops server status check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_server-status-check_20260513T233559_result.json`
- **Structured JSON:** [`5543a0ec02d7db5138da.json`](../../sessions/55/5543a0ec02d7db5138da.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态汇总

### plan001-exec-only-s42-r2 (cuda:0)
- **状态**: 运行中，PID 84901，已运行 ~56 分钟
- **进度**: 434/500 步 (87%)
- **最新 metrics** (step 434): reward_mean=0.75, prove_rate=0.75, parse_rate=1.0
- **趋势**: 大部分步骤 reward_mean=1.0，偶尔降到 0.625-0.875，模型已收敛
- **Checkpoints**: checkpoint-350, checkpoint-400
- **预计**: 约 10-15 分钟完成

### plan005-sta-low-s42 (cuda:1)
- **状态**: 运行中，PID 85795（实际训练进程），已运行 ~54 分钟
- **进度**: 369/500 步 (74%)
- **最新 metrics** (step 369): reward_mean=0.92, prove_rate=1.0, isr_mean=0.19, parse_rate=1.0
- **趋势**: prove_rate 多在 0.5-1.0 间波动，reward 因 STA 组件 (isr_mean) 较低而低于 plan001
- **Checkpoints**: checkpoint-300, checkpoint-350
- **预计**: 约 20-25 分钟完成

### GPU
| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 82% | 80.3/97.9 GB |
| 1 | 91% | 80.4/97.9 GB |

### 僵尸进程
6 个 swipl 相关进程（PID 95932-96445）已全部 kill，释放了 2 核 CPU。

### tmux sessions
- `plan001-exec-only-s42-r2` — 运行中
- `plan005-sta-low-s42` — 运行中

### 异常
无异常。两个实验稳定推进中，预计 plan001 先完成。

---
