# check exp002 completion status

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_exp002_completion_status_20260521T134117_result.json`
- **Structured JSON:** [`a32ad5bc1c0722db0b8a.json`](../../sessions/a3/a32ad5bc1c0722db0b8a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## exp-002 状态汇总

### 1. 核心 16 文件（4 models × 4 benchmarks）

| 文件 | 行数 | 状态 |
|------|------|------|
| llama_{mmlu,arc,hellaswag,gsm8k} | 57,600 × 4 | OK |
| qwen_{mmlu,arc,hellaswag,gsm8k} | 57,600 × 4 | OK |
| gemma_{mmlu,arc,hellaswag,gsm8k} | 57,600 × 4 | OK |
| mistral_{mmlu,arc,hellaswag,gsm8k} | 57,600 × 4 | OK |

**判断：exp-002 核心实验 SUCCESS** — 全部 16 文件 × 57,600 行完整。

### 2. MATH 接力推理（进行中）

| 文件 | 行数 | 进度 | 启动时间 | PID |
|------|------|------|----------|-----|
| llama_math | 16,400 | 28.5% | 20:45 | 162292 |
| mistral_math | 13,600 | 23.6% | 20:58 | 163851 |
| qwen_math | 2,200 | 3.8% | 21:33 | 166536 |
| gemma_math | 600 | 1.0% | 21:37 | 167468 |

GSM8K→MATH 自动切换已成功执行，monitor 在 21:37 确认全部 3 个模型（mistral/qwen/gemma）切换完毕后退出。llama_math 在 20:45 单独启动。

### 3. GPU 状态

| GPU | 利用率 | 显存 |
|-----|--------|------|
| 0 | 86% | 87.9 / 97.9 GiB |
| 1 | 81% | 88.0 / 97.9 GiB |
| 2 | 89% | 87.1 / 97.9 GiB |
| 3 | 80% | 88.5 / 97.9 GiB |

4 GPU 全满载跑 MATH 推理。

### 4. MATH 预计完成时间

按 llama/mistral 的稳定速率（~300 lines/min），4 个 MATH 文件预计还需 **~3-3.5 小时**（约 01:00 CST 前后完成）。

---
