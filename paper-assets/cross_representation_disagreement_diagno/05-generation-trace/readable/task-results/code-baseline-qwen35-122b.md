# code baseline qwen35 122b

**Cross-Representation Disagreement as a Diagnostic Signal for LLM Reasoning Errors** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_baseline_qwen35_122b_20260514T053754_result.json`
- **Structured JSON:** [`e5d8cddeec6f77e4d338.json`](../../sessions/e5/e5d8cddeec6f77e4d338.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

API 返回 **402 Insufficient balance** — 提供的 API Key (`tum_XXB3s...`) 在 `http://47.94.22.126/v1` 上余额不足，所有请求均被拒绝。3 次重试全部失败。

这不是代码问题，代码逻辑和数据加载都正常（204 条数据已就绪）。需要：

1. **充值该 API 账户**，或
2. **提供一个有余额的 API Key**，或
3. **换用其他 API endpoint**（如 OpenRouter 官方 `https://openrouter.ai/api/v1`，但需要对应的 key）

余额恢复后重跑 `python baseline.py --max-examples 3` 即可继续。

---
