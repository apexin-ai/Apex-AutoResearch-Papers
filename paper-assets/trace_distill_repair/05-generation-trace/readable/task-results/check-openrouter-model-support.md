# check openrouter model support

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_openrouter_model_support_20260515T153120_result.json`
- **Structured JSON:** [`d01165b8feefa912db7f.json`](../../sessions/d0/d01165b8feefa912db7f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

### OpenRouter 代理模型列表（共 73 个模型）

**Claude 系列：**
| 模型 ID | 可用 |
|---------|------|
| `anthropic/claude-sonnet-4` | ✅ 已验证（通过 Amazon Bedrock） |
| `anthropic/claude-sonnet-4.5` | ✅ |
| `anthropic/claude-sonnet-4.6` | ✅ |
| `anthropic/claude-opus-4.5` | ✅ |
| `anthropic/claude-opus-4.6` | ✅ |
| `anthropic/claude-opus-4.7` | ✅ |
| `anthropic/claude-opus-4.7-fast` | ✅ |
| `anthropic/claude-haiku-4.5` | ✅ |
| `claude-haiku-4-5`（无前缀） | ✅ |

**GPT-4o 系列：**
| 模型 ID | 可用 |
|---------|------|
| `openai/gpt-4o-mini` | ✅ |
| `openai/gpt-4o`（完整版） | ❌ 不在列表中 |

### 关键结论
- **Claude Sonnet 4** 可直接调用，用现有 `OPENROUTER_API_KEY` 即可，无需新 key
- **GPT-4o 完整版不可用**，只有 `gpt-4o-mini`。如果强模型消歧实验需要 GPT-4o 作为 judge，需要换成 `gpt-4o-mini` 或其他可用模型

### v2 实验进度
- PID 131777 仍在运行（已运行 2h03m）
- checkpoint 结构是 dict（非 list），包含 **9/14 个 instance**：`black_1, cookiecutter_1/2/3, fastapi_2, httpie_2, luigi_5, sanic_2, scrapy_2`

---
