# ops urgent harvest both codellama

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_urgent_harvest_both_codellama_20260518T060214_result.json`
- **Structured JSON:** [`2ee46ca259a6925b42de.json`](../../sessions/2e/2ee46ca259a6925b42de.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

### GPU 状态
| GPU | 型号 | 显存占用 | GPU-Util |
|-----|------|----------|----------|
| 0 | RTX PRO 6000 | 49175/97887 MiB | **0%** (空闲) |
| 1 | RTX PRO 6000 | 36535/97887 MiB | **100%** (活跃) |

只有 GPU 1 上有进程 (PID 405141)。

---

### 实验 1: `codellama13b_full_trace_tail1024_seed42_v2` (cuda:0)

| 项目 | 状态 |
|------|------|
| tmux session | **不存在**（已退出） |
| 训练进度 | **已完成** — 444/444 steps, 3 epochs, 耗时 2h27m |
| train_loss | 0.0937 |
| eval_loss | 0.1859 |
| eval_mean_token_accuracy | **0.9612** |
| eval_entropy | 0.0708 |
| 模型保存 | `/root/autodl-tmp/trace-verdict-study-checkpoints/codellama13b_full_trace_tail1024_seed42_v2/final` |
| EXIT_CODE | 0 |
| eval_results.json | **不存在**（eval 指标在训练日志末尾输出，未单独写 JSON） |

---

### 实验 2: `codellama13b_full_trace_tail2048_seed42_v2` (cuda:1)

| 项目 | 状态 |
|------|------|
| tmux session | **存活** |
| 训练进度 | **进行中** — 263/444 steps (59%), ~28.4s/it |
| 预计剩余 | ~1h26m |
| eval_results.json | 不存在（训练未完成） |

---

**总结**: tail1024 已完成（token accuracy 96.1%），tail2048 还在跑，约 59%，预计还需 ~1.5 小时。

---
