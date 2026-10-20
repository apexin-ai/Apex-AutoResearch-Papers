# ssh autodl judge progress

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_autodl_judge_progress_20260522T172831_result.json`
- **Structured JSON:** [`265f60fce8e86301515f.json`](../../sessions/26/265f60fce8e86301515f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All judges have 9 target models × 500 questions × 2 positions = **9000 expected judgments each**。

## 结果

### GPU 状态
**全部空闲** — 0% 利用率，0 MiB 显存。vLLM 进程已全部退出。

### Judgment 进度（期望每 judge 9000 条）

| Judge | 完成数 | 完成度 | 状态 |
|-------|--------|--------|------|
| **gpt-5.5-proxy** | 3437 | 38.2% | 停止 |
| **claude-opus-4.7-proxy** | 3389 | 37.7% | 停止 |
| **claude-sonnet-4.6-proxy** | 2961 | 32.9% | 停止 |
| **qwen3-235b-proxy** | 2091 | 23.2% | 停止 |
| **gemini-2.5-pro-proxy** | 1916 | 21.3% | 停止 |
| **deepseek-v4-pro-proxy** | 1433 | 15.9% | 停止 |
| **llama-3.3-70b** (local) | 1238 | 13.8% | 停止 |
| **qwen2.5-72b** (local) | 915 | 10.2% | 停止 |
| **mistral-large-2** (local) | 583 | 6.5% | 停止 |

### 关键发现
- **所有进程已停止**，包括 3 个本地 vLLM 实例和所有 judge/collector 进程
- 最后一条 judgment 时间戳约 **21:55 (今天)**，文件在 21:55:45 被 collect 脚本收集
- vLLM 日志 (`/tmp/vllm_800*.log`) 已被清理，无法判断是正常退出还是崩溃
- 与上次检查相比（Llama 69%, Qwen 68%, Mistral 46%），当前文件似乎是**重新开始的评估**（config 从 3 个模型扩展到 9 个模型，包括新增的 gemma-2-9b 和 qwen3-8b），所以百分比下降
- 没有发现错误日志

### 需要操作
需要重启 vLLM 实例和 judge 评估进程才能继续。collect.py 支持增量 resume（通过 `load_completed`），重启后可以从断点继续。

---
