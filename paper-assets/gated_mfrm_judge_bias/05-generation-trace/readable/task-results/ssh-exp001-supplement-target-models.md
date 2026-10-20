# ssh exp001 supplement target models

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp001_supplement_target_models_20260522T053513_result.json`
- **Structured JSON:** [`3ea2f5bb15a05cc83cba.json`](../../sessions/3e/3ea2f5bb15a05cc83cba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

llama 确实在跑但吞吐只有 5 tok/s（AWQ 单卡）。所有 3 个 vLLM 服务都在并行生成。

下面汇总当前状态和完整计划。

---

## 当前状态

### 正在生成（后台进行中）

| 模型 | 来源 | 进度 | 预估完成 |
|------|------|------|---------|
| gpt-4o | Proxy API | 69/500 | ~1h |
| gpt-4o-mini | Proxy API (排队中) | 0/500 | gpt-4o 完成后 ~1h |
| gpt-5.5 | Proxy API (排队中) | 0/500 | gpt-4o-mini 后 ~1.5h |
| llama-3.3-70b | vLLM :8001 | 1/500 | ~3-4h (AWQ 慢) |
| qwen2.5-72b | vLLM :8002 | 26/500 | ~2h |
| mistral-large-3 | vLLM :8003 | 26/500 | ~2h |

### 已完成（原有）

| 模型 | 数量 |
|------|------|
| gpt-3.5-turbo-0125 | 500 ✓ |
| gpt-4-0314 | 500 ✓ |
| gpt-4-0613 | 500 ✓ |

### 需要 GPU 时间窗（等现有 vLLM 服务释放后用离线批推理，每模型 ~10-30min）

| 模型 | 大小 | GPU 需求 |
|------|------|---------|
| llama-3.1-8b | 8B | 1 GPU |
| qwen2.5-7b | 7B | 1 GPU |
| gemma-2-9b | 9B | 1 GPU |
| mistral-7b-v0.3 | 7B | 1 GPU |
| qwen2.5-14b | 14B | 1 GPU |
| phi-4 | 14B | 1 GPU |
| gemma-2-27b | 27B | 1 GPU |
| llama-3.1-70b | 70B | 2 GPU |
| qwen3-235b-a22b | 235B MoE | 4 GPU + FP8 |

### 需要额外 API 余额（Proxy 402 余额不足）

| 模型 | 状态 |
|------|------|
| claude-opus-4.7 | 需充值/替代 API |
| claude-sonnet-4.6 | 需充值/替代 API |
| gemini-2.5-pro | 需充值/替代 API |
| gemini-2.5-flash | 需充值/替代 API |
| deepseek-v4-pro | 需充值/替代 API |
| mistral-medium-3.5 | 需充值/替代 API |
| deepseek-v3 | 671B MoE，本地装不下，需 API |

---

### 接下来需要你决定的

1. **7 个 proprietary 模型**的 API 问题：proxy (`47.94.22.126`) 对非 OpenAI 模型余额不足 (402)。是否有其他 API key 可用？或者需要充值？
2. **GPU 调度**：等 vLLM 在线生成（llama/qwen/mistral）完成后，是否可以暂停 vLLM 服务来跑小模型的离线批推理？还是 exp009 和 judge 评估也在用这些服务？
3. **deepseek-v3**（671B MoE）本地跑不下，是否可以从 target list 中去掉或替换为 deepseek-v2.5？

---
