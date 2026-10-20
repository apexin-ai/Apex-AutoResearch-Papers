# ssh rtx6000 judge api health

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_rtx6000_judge_api_health_20260522T163611_result.json`
- **Structured JSON:** [`5b3ead33a1ad619ecd0d.json`](../../sessions/5b/5b3ead33a1ad619ecd0d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部信息已收集完毕。

---

## 健康状况报告

### 1. PID 247295（死亡进程）
是 `generate_vllm_online.py` v5 run，生成 3 个本地 vLLM 模型（llama-3.3-70b, qwen2.5-72b, mistral-large-2）的 responses。在 summary 阶段因 `unsupported operand type(s) for +: 'int' and 'list'` 崩溃，但 **3 个模型的 responses 均已写入完毕（500/500）**。**无需重启。**

### 2. 9 个 Judge 收集器 — 全部存活

| Judge | PID | Workers | Judgments | %（/9000） | ETA | 状态 |
|-------|-----|---------|-----------|-----------|-----|------|
| claude-opus-4.7-proxy | 332552 | 4 | 5,150 | 57.2% | ~7.8h | ✅ |
| gpt-5.5-proxy | 332533 | 4 | 4,900 | 54.4% | ~8.6h | ✅ |
| claude-sonnet-4.6-proxy | 332567 | 4 | 4,673 | 51.9% | ~8.6h | ✅ |
| qwen3-235b-proxy | 332616 | 4 | 3,309 | 36.8% | ~13h | ✅ |
| gemini-2.5-pro-proxy | 332599 | 4 | 2,961 | 32.9% | — | ✅ log空但文件 9s 前更新 |
| deepseek-v4-pro-proxy | 332582 | 4 | 2,320 | 25.8% | — | ✅ log空但文件 3s 前更新 |
| llama-3.3-70b | 332474 | 8 | 2,074 | 23.0% | — | ✅ log空但文件 36s 前更新 |
| qwen2.5-72b | 332493 | 8 | 1,974 | 21.9% | ~30h | ⚠️ 有 connection errors，在 retry |
| mistral-large-2 | 332512 | 8 | 1,337 | 14.9% | ~34h | ⚠️ 部分 prompt 超 8192 token 限制 |

3 个 log 为空（llama/deepseek/gemini）仅是 Python stdout 缓冲，judgment 文件实际在持续写入。

### 3. API Response 生成

| Model | Responses | 完成? |
|-------|-----------|-------|
| gpt-3.5-turbo-0125 | 500 | ✅ |
| gpt-4-0314 | 500 | ✅ |
| gpt-4-0613 | 500 | ✅ |
| gpt-4o | 500 | ✅ |
| gpt-4o-mini | 500 | ✅ |
| llama-3.3-70b | 500 | ✅ |
| qwen2.5-72b | 500 | ✅ |
| mistral-large-2 | 500 | ✅ |
| claude-opus-4.7 | 500 | ✅ |
| gpt-5.5 | 500 | ✅ |
| gemma-2-9b | 500 | ✅ |
| qwen3-8b | 500 | ✅ |
| **claude-sonnet-4.6** | **255** | **❌ 51%** |

`generate_responses.py --group proxy_nocredit`（PID 273489）正在运行，log 暂无输出（可能在处理 claude-sonnet-4.6 剩余 245 条）。

### 4. exp-009
**159/200**（79.5%），ETA ~4h，PID 112923 运行 15h31m，正常。

### 需要关注的问题

1. **mistral judge 的 8192 token 上限** — 部分长 prompt 会永久失败，可能需要调大 max_tokens 或跳过这些 item
2. **qwen judge 连接错误** — vLLM port 8002 可能不稳定，retry 中但速率只有 0.1 items/s（ETA 30h）
3. **claude-sonnet-4.6 responses 只有 255/500** — 是当前唯一未完成的 response 生成任务

---
