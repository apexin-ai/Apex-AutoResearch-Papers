# ssh n17 data preparation

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_n17_data_preparation_20260523T134414_result.json`
- **Structured JSON:** [`d0fdad1574c4e001d1d5.json`](../../sessions/d0/d0fdad1574c4e001d1d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

---

## 产出汇总

### 1. 数据下载
从 HuggingFace `lmarena-ai/arena-hard-auto` 下载了 9 个模型的 model_answer 文件（服务器无外网，本地下载后 SCP 传输）。

### 2. 格式转换结果
源格式 `{uid, messages[{content:{answer}}]}` → 目标格式 `{id, response}`。9 个模型每个 500 条，全部成功：

| 模型 | 条数 |
|------|------|
| claude-3-5-sonnet-20241022 | 500 |
| gpt-4-turbo-2024-04-09 | 500 |
| llama-3.1-70b-instruct | 500 |
| gemma-2-27b-it | 500 |
| claude-3-opus-20240229 | 500 |
| llama-3-70b-instruct | 500 |
| mixtral-8x22b-instruct-v0.1 | 500 |
| claude-3-haiku-20240307 | 500 |
| llama-3-8b-instruct | 500 |

### 3. 数据完整性
所有 17 个模型（原 8 + 新 9）的 500 个 question ID 与 `prompts.jsonl` 完全匹配，无缺失。

### 4. Chatbot Arena ELO（2026-05-19 快照）

| Rank | 模型 | ELO |
|------|------|-----|
| 1 | gpt-4o | 1300 |
| 2 | claude-3-5-sonnet-20241022 | 1298 |
| 3 | gpt-4o-mini | 1286 |
| 4 | llama-3.3-70b | 1275 |
| 5 | gpt-4-turbo-2024-04-09 | 1272 |
| 6 | qwen2.5-72b | 1269 |
| 7 | mistral-large-2 | 1266 |
| 8 | claude-3-opus-20240229 | 1262 |
| 9 | llama-3.1-70b-instruct | 1261 |
| 10 | gemma-2-27b-it | 1231 |
| 11 | llama-3-70b-instruct | 1221 |
| 12 | gemma-2-9b | 1207 |
| 13 | gpt-4-0314 | 1206 |
| 14 | claude-3-haiku-20240307 | 1195 |
| 15 | gpt-4-0613 | 1186 |
| 16 | qwen3-8b | 1170* |
| 17 | llama-3-8b-instruct | 1166 |
| 18 | mixtral-8x22b-instruct-v0.1 | 1162 |
| 19 | gpt-3.5-turbo-0125 | 1125 |

*qwen3-8b 不在 Arena 排行榜上，保留 exp003 原有估计值 1170。

**与现有 ARENA_ELO 的偏差**：`exp003/evaluation.py` 的值整体偏低 30-80 分（如 gpt-4o 原 1286→现 1300，llama-3.3-70b 原 1208→现 1275）。最新值已写入 `data/arena_elo_n17.py`。

### 5. Judge 评测配置
创建了 9 个 `*_arena_n17.yaml` 配置文件，每个对应一个 judge，target_models 扩展到 18 个（含 gpt-4-0314 reference）：
- `config_llama_arena_n17.yaml`
- `config_qwen_arena_n17.yaml`
- `config_mistral_arena_n17.yaml`
- `config_gpt-5.5-proxy_arena_n17.yaml`
- `config_claude-opus-4.7-proxy_arena_n17.yaml`
- `config_claude-sonnet-4.6-proxy_arena_n17.yaml`
- `config_deepseek-v4-pro-proxy_arena_n17.yaml`
- `config_qwen3-235b-proxy_arena_n17.yaml`
- `config_gemini-2.5-pro-proxy_arena_n17.yaml`

collect.py 的 resume 机制会跳过已完成的判断，只评测新增的 9 个 target models。

### 6. 无格式不匹配或缺失问题
所有 ID 对齐、字段格式一致、数据完整。

---
