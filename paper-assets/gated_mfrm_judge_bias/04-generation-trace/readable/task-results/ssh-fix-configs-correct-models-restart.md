# ssh fix configs correct models restart

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_configs_correct_models_restart_20260523T233058_result.json`
- **Structured JSON:** [`16d6cb77548a3ab5d6fc.json`](../../sessions/16/16d6cb77548a3ab5d6fc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部 4 个 judges Total=18000 ✅，从 0 开始，正常运行。

---

## 产出报告

### 1. 18 个模型 response 文件

| 模型 | 行数 | 来源 |
|------|------|------|
| gpt-3.5-turbo-0613 | 500 ✅ | HF 新下载 |
| gpt-4-0613 | 500 ✅ | 已有 |
| gpt-4o-2024-05-13 | 500 ✅ | HF 新下载 |
| gpt-4o-mini-2024-07-18 | 500 ✅ | HF 新下载 |
| gpt-4-turbo-2024-04-09 | 500 ✅ | 已有 |
| llama-3.3-70b-instruct | **491** ⚠️ | 从 llama-3.3-70b 复制（HF 无此模型） |
| llama-3.1-70b-instruct | 500 ✅ | 已有 |
| llama-3-70b-instruct | 500 ✅ | 已有 |
| llama-3-8b-instruct | 500 ✅ | 已有 |
| qwen2.5-72b-instruct | 500 ✅ | HF 新下载 |
| qwen3-8b | 500 ✅ | 已有 |
| gemma-2-9b-it | 500 ✅ | HF 新下载 |
| gemma-2-27b-it | 500 ✅ | 已有 |
| claude-3-5-sonnet-20241022 | 500 ✅ | 已有 |
| claude-3-opus-20240229 | 500 ✅ | 已有 |
| claude-3-haiku-20240307 | 500 ✅ | 已有 |
| mixtral-8x22b-instruct-v0.1 | 500 ✅ | 已有 |
| mistral-large-2407 | 500 ✅ | HF 新下载 |

### 2. Config 修改 ✅
- 4 个 n17 config 全部从 14→18 models
- RPM: sonnet=150, gemini/deepseek/qwen3=100

### 3. 旧错误数据清理 ✅
- 837 行旧 judgment 数据已备份 (`.bak_wrong_models`) 并清空

### 4. API Judges 运行状态

| Judge | PID | Total | 速度 | ETA |
|-------|-----|-------|------|-----|
| sonnet | 485562 | 18000 (17982 实际) | ~1.2/s | ~250 min |
| gemini | 485759 | 18000 (17982 实际) | ~0.5/s | ~650 min |
| deepseek | 485826 | 18000 (17982 实际) | ~0.1/s | ~2145 min |
| qwen3 | 485992 | 18000 (17982 实际) | ~0.2/s | ~1449 min |

实际任务数 17982 = 18000 - 18，因为 llama-3.3-70b-instruct 缺 9 个 item（×2 positions）。

### 5. LLaMA 下载
- PID 480645，已有进程在跑，无需重启
- 进度：29% (5/17 files)，已下载 25GB
- 有超时自动重试，正在继续

---
