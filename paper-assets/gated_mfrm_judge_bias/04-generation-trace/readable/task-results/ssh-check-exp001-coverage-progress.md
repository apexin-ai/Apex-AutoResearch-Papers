# ssh check exp001 coverage progress

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check_exp001_coverage_progress_20260522T103640_result.json`
- **Structured JSON:** [`87b8feb2ebf55910d13b.json`](../../sessions/87/87b8feb2ebf55910d13b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总所有结果。

---

## exp-001 Judge 收集进度

### Per-Judge 统计（9 judges 全部在线运行中）

| Judge | Items | Workers | 类型 |
|---|---|---|---|
| gpt-5.5-proxy | **1,962** | 4 | API |
| claude-opus-4.7-proxy | **1,701** | 4 | API |
| claude-sonnet-4.6-proxy | **1,284** | 4 | API |
| gemini-2.5-pro-proxy | **908** | 4 | API |
| qwen3-235b-proxy | **895** | 4 | API |
| deepseek-v4-pro-proxy | **676** | 4 | API |
| llama-3.3-70b | **278** | 8 | Local |
| qwen2.5-72b | **166** | 8 | Local |
| mistral-large-2 | **83** | 8 | Local |

**总计: 7,953 items across 9 judges**

### Coverage Matrix (model_a vs gpt-4-0314 baseline, 7 target models)

| Judge | gpt-3.5-turbo | gpt-4-0314 (self) | gpt-4-0613 | gpt-4o | gpt-4o-mini | llama-3.3-70b | qwen2.5-72b |
|---|---|---|---|---|---|---|---|
| gpt-5.5-proxy | 638 | 636 | 637 | 14 | 13 | ~13 | ~11 |
| claude-opus-4.7 | 550 | 545 | 552 | 14 | 14 | ~13 | ~13 |
| claude-sonnet-4.6 | 412 | 412 | 411 | 13 | 12 | ~12 | ~12 |
| gemini-2.5-pro | 298 | 280 | 293 | 10 | 10 | ~9 | ~8 |
| qwen3-235b | 285 | 286 | 286 | 10 | 10 | ~9 | ~9 |
| deepseek-v4-pro | 224 | 203 | 222 | 8 | ~7 | 7 | ~5 |
| llama-3.3-70b | 81 | 82 | 80 | 10 | 9 | ~8 | ~8 |
| qwen2.5-72b | 48 | 48 | 48 | 6 | 6 | ~5 | ~5 |
| mistral-large-2 | 24 | 23 | 21 | 4 | ~4 | 4 | ~3 |

**前 3 个 target model（gpt-3.5-turbo, gpt-4-0314, gpt-4-0613）覆盖充足**；后 4 个（gpt-4o, gpt-4o-mini, llama, qwen）还在 ramp up（<15 items/cell）。

### 运行进程
**9 个 collect.py 进程**，全部于 18:30 启动。日志文件均为 0 bytes（尚未 flush）。

---

## exp-009 进度

| 指标 | 值 |
|---|---|
| PID | 112923 |
| 已运行 | **9h 31m** |
| 当前进度 | **[99/200] rho=0.3 seed=48** |
| 完成率 | **~49.5%** |
| ETA | **~9.7 小时** (~35000s) |
| 警告 | MCMC chains 串行执行（仅 1 GPU/CPU device，期望 4） |

---

## 磁盘

| 分区 | 总量 | 已用 | 可用 | 使用率 |
|---|---|---|---|---|
| / (overlay) | 30G | 10G | 21G | **34%** |

---
