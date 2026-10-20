# code openrouter adaptation

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_openrouter_adaptation_20260520T074600_result.json`
- **Structured JSON:** [`384762d0d6bae2a349d1.json`](../../sessions/38/384762d0d6bae2a349d1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。修改摘要：

| 文件 | 改动 |
|---|---|
| **config.py** | 新增 `OPENROUTER_BASE_URL`、`API_KEY_ENV`；移除 `provider` 字段；模型 ID 改为 OpenRouter 格式 |
| **harness.py** | 删除 `_get_anthropic_client()`、`_call_anthropic()`；合并为单一 `_get_client()` + `call_agent()` 走 OpenAI SDK；`run_episode` 中移除 Anthropic tool result 格式分支 |
| **judge.py** | 同理删除 Anthropic 代码，`call_judge()` 统一走 OpenAI SDK |
| **requirements.txt** | 移除 `anthropic` |

三个 CLI 的参数接口保持不变，`analyze.py` 未修改。模型端点不可达，模型 ID 使用了 OpenRouter 常见格式并加了注释提示确认。

---
