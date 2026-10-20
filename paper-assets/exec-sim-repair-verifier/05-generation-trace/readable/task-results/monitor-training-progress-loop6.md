# monitor training progress loop6

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training-progress-loop6_20260513T001229_result.json`
- **Structured JSON:** [`123e53079a1a08d7e4e3.json`](../../sessions/12/123e53079a1a08d7e4e3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 训练进度汇总

### CLS v4 (home-1x5090)

| 指标 | 值 |
|------|-----|
| 状态 | **运行中** (PID 2885139, uptime 2h17m) |
| 进度 | step **970/4668** (**20.8%**) |
| 速度 | ~6 it/s |
| 最新 checkpoint | checkpoint-600 |
| 磁盘 | 66% used, 351GB 可用 |
| 预估剩余 | **~8-9 小时** |

> ⚠️ 总步数从之前的 6633 变为 4668，可能训练配置有变。

### CWM v10 (seetacloud-westd-4x5090)

| 指标 | 值 |
|------|-----|
| 状态 | **运行中** (PID 105205, uptime 33m, 从 ckpt-200 恢复) |
| 进度 | step **316/6633** (**4.8%**) |
| eval_loss | **0.3228** @step 300 (vs 上次 loss=4.80，已大幅下降) |
| 速度 | ~8-10 s/step |
| 最新 checkpoint | checkpoint-300 |
| GPU | 仅 GPU2 在用，96% 利用率，21GB/32GB VRAM |
| 预估剩余 | **~15-20 小时**（含 eval 开销，eval 每 100 步一次，每次~12 分钟） |

两个实验均正常运行，无异常。Registry 已更新。

---
