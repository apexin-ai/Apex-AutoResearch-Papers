# diag w2 1 7b pilot check

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_w2-1_7b-pilot-check_20260516T111929_result.json`
- **Structured JSON:** [`5c4acdb3a75b085bb3eb.json`](../../sessions/5c/5c4acdb3a75b085bb3eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结果

### 两个实验均正常运行中

| 项目 | w2-qwen3-1.7b-exec-pilot | w2-qwen3-1.7b-isr-pilot |
|------|--------------------------|-------------------------|
| **状态** | 运行中 | 运行中 |
| **当前步数** | 75/500 (15%) | 75/500 (15%) |
| **运行时间** | ~11m27s | ~11m29s |
| **GPU** | GPU 0, 41026 MiB, 70% util | GPU 1, 41026 MiB, 93% util |
| **Checkpoint** | checkpoint-50 已保存 | checkpoint-50 已保存 |
| **错误** | 无 | 无 |

### 关键指标（最近 steps）

- **exec-pilot**: reward 接近 0（step 55-75 大部分为 0.0，偶尔 0.125），prove_rate 极低。训练信号弱。
- **isr-pilot**: reward 明显更高（step 74=0.754, step 75=0.508），prove_rate 达到 50-75%。ISR reward 在发挥作用。

### 其他
- 磁盘：/root/autodl-tmp 199G/250G (80%)，剩余 52G，暂时安全
- 无 error/traceback/OOM
- 预计完成时间：按 ~9s/step 估算，剩余 425 步 ≈ 64 分钟（~20:25 左右完成）

### 问题确认
tmux session name 含 `.` 导致 cron 监控无法匹配，但训练进程本身不受影响，两个实验都在正常推进。

---
