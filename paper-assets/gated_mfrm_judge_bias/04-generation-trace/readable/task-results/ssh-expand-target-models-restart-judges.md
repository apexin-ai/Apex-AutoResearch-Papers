# ssh expand target models restart judges

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_expand_target_models_restart_judges_20260522T102710_result.json`
- **Structured JSON:** [`d9fbc5026894ed349bee.json`](../../sessions/d9/d9fbc5026894ed349bee.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

### 确认的 7 个 target models
| Model | Responses |
|-------|-----------|
| gpt-3.5-turbo-0125 | 500 |
| gpt-4-0314 | 500 |
| gpt-4-0613 | 500 |
| gpt-4o | 500 |
| gpt-4o-mini | 500 |
| llama-3.3-70b | 500 |
| qwen2.5-72b | 496 |

### 更新的 config 文件（全部 9 个）
`config_llama_arena.yaml`, `config_qwen_arena.yaml`, `config_mistral_arena.yaml`, `config_claude-opus-4.7-proxy_arena.yaml`, `config_claude-sonnet-4.6-proxy_arena.yaml`, `config_deepseek-v4-pro-proxy_arena.yaml`, `config_gemini-2.5-pro-proxy_arena.yaml`, `config_gpt-5.5-proxy_arena.yaml`, `config_qwen3-235b-proxy_arena.yaml`

### 重启的 judge sessions（全部 9 个）
- Local (--workers 8): `judge-llama`, `judge-qwen`, `judge-mistral`
- API (--workers 4): `judge-gpt55`, `judge-opus`, `judge-sonnet`, `judge-deepseek`, `judge-gemini`, `judge-qwen3`

### 验证结果
新 target model 的 judgment 已开始出现：

| Judge | 总条目 | 新模型条目 |
|-------|--------|-----------|
| claude-opus-4.7-proxy | 1663 | 16 |
| claude-sonnet-4.6-proxy | 1251 | 16 |
| gpt-5.5-proxy | 1926 | 16 |
| deepseek-v4-pro-proxy | 654 | 5 |
| gemini-2.5-pro-proxy | 879 | 9 |
| qwen3-235b-proxy | 866 | 9 |
| llama-3.3-70b | 252 | 已在写入 |
| qwen2.5-72b | 145 | 已在写入 |
| mistral-large-2 | 70 | 2 |

`auto-restart` session 已 kill，不再需要。所有 judge 正常运行，`load_completed()` 保证存量不丢失。

---
