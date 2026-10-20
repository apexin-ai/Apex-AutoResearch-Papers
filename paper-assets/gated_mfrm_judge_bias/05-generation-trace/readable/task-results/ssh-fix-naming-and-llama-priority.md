# ssh fix naming and llama priority

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix_naming_and_llama_priority_20260522T063705_result.json`
- **Structured JSON:** [`3c6552208126a151e903.json`](../../sessions/3c/3c6552208126a151e903.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总报告：

---

### 1. Mistral 命名修复 ✓

**模型确认**: 部署的是 `Mistral-Large-Instruct-2407-AWQ`（Mistral Large **2**），vLLM served name `mistral-large-instruct`

**修改了 5 处**:
| 文件 | 变更 |
|------|------|
| `data/arena_hard/responses/mistral-large-3.jsonl` | → `mistral-large-2.jsonl` |
| `exp001/generate_vllm_online.py:23` | `mistral-large-3` → `mistral-large-2` |
| `exp001/generate_vllm_batch.py:34` | `mistral-large-3` → `mistral-large-2` |
| `exp001/config.yaml:46` | `mistral-large-3` → `mistral-large-2` |
| `exp001/generate_responses.py:44` | `mistral-large-3` → `mistral-large-2` |

`exp001/results/mistral-large-2/` 本来就是正确命名，无需改。全项目已无 `mistral-large-3` 残留。

注意：`Mistral-Large-Instruct-2411-AWQ`（真正的 Large 3）正在下载中（2 个 hf download 进程）。

### 2. Llama response 生成 — 无需干预

`generate_vllm_online.py` 进程**已自然结束**（不在进程列表中）。Llama vLLM 当前仅服务 judge 收集，无双重负载。

### 3. Response 生成进度

| Model | 进度 |
|-------|------|
| gpt-3.5-turbo-0125 | **500/500** ✓ |
| gpt-4-0314 | **500/500** ✓ |
| gpt-4-0613 | **500/500** ✓ |
| gpt-4o | 377/500 (openai group 在跑) |
| qwen2.5-72b | 395/500 |
| mistral-large-2 | 395/500 |
| llama-3.3-70b | **9/500** (需后续单独补) |

### 4. Judge 收集进度（目标 3000 each）

| Judge | 进度 | 状态 |
|-------|------|------|
| gpt-5.5-proxy | 835 | 运行中 (0.1/s, ETA ~6h) |
| claude-opus-4.7-proxy | 467 | — |
| claude-sonnet-4.6-proxy | 431 | — |
| gemini-2.5-pro-proxy | 360 | — |
| qwen3-235b-proxy | 252 | — |
| deepseek-v4-pro-proxy | 243 | — |
| llama-3.3-70b | 217 | 运行中 (极慢, 40/2827) |
| qwen2.5-72b | 130 | 运行中 (30/2907) |
| mistral-large-2 | 58 | 运行中 (10/2979, 极慢) |

### 5. exp-009

**仍在运行**。PID 112923，已运行 5h32m，GPU 0 上，CPU 105%。

### 6. GPU 状态

| GPU | 显存 | 利用率 |
|-----|------|--------|
| 0 | 74/98 GB | 61% (exp-009) |
| 1 | 88/98 GB | 100% (Qwen vLLM) |
| 2 | 90/98 GB | 100% (Llama vLLM) |
| 3 | 88/98 GB | 100% (Mistral vLLM) |

---
