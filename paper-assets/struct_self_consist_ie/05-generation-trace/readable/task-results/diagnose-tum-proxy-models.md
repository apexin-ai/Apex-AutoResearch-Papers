# diagnose tum proxy models

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_tum_proxy_models_20260521T052928_result.json`
- **Structured JSON:** [`aa57ffa76accca73ee51.json`](../../sessions/aa/aa57ffa76accca73ee51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

**`/models` 端点**：返回 118 个模型，全部是 OpenAI 系列（GPT / o 系列）。

**实际调用测试**：

| 模型 ID | 状态 | 备注 |
|---------|------|------|
| `claude-sonnet-4-20250514` | ❌ | 不是有效 model ID |
| `anthropic/claude-sonnet-4` | ✅ | 正常 |
| `gemini-2.5-pro` | ✅ | 正常 |
| `google/gemini-2.5-pro` | ✅ | 正常 |
| `deepseek-chat` | ❌ | 歧义，匹配多个模型 |
| `deepseek/deepseek-chat` | ✅ | 正常 |
| `gpt-4o` | ✅ | 正常 |
| `o3` | ❌ | 不支持 `temperature=0`，需用 default |

总结：
- 非 OpenAI 模型需要用 `provider/model` 格式（如 `anthropic/claude-sonnet-4`、`deepseek/deepseek-chat`）
- `o3` 可用但不支持 `temperature=0`，需去掉该参数或换默认值
- `/models` 只列 OpenAI 模型，但实际支持 Claude、Gemini、DeepSeek 等第三方模型（透传代理）

---
