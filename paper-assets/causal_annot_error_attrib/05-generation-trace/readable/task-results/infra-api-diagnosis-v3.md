# infra api diagnosis v3

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_api-diagnosis-v3_20260520T092822_result.json`
- **Structured JSON:** [`4014022bdc899fa1476a.json`](../../sessions/40/4014022bdc899fa1476a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部测试完成。

---

## 完整结果表

| Model ID | Status | Actual Model | Notes |
|----------|--------|-------------|-------|
| `meta-llama/llama-4-maverick` | ✅ OK | (已知可用) | 之前已确认 |
| `qwen/qwen3-235b-a22b` | ✅ OK | qwen3-235b-a22b-04-28 | 验证通过 |
| `deepseek/deepseek-chat` | ✅ OK | deepseek-chat-v3 | 路由到 V3 |
| `deepseek/deepseek-r1` | ✅ OK | deepseek-r1 | 可用 |
| `deepseek/deepseek-r1-0528` | ✅ OK | deepseek-r1-0528 | 可用 |
| `deepseek/deepseek-chat-v3-0324` | ✅ OK | deepseek-chat-v3-0324 | 可用 |
| `deepseek/deepseek-v4` | ❌ ERR | — | not a valid model ID |
| `deepseek/deepseek-v3` | ❌ ERR | — | not a valid model ID |
| `deepseek/deepseek-v4-0324` | ❌ ERR | — | not a valid model ID |
| `qwen/qwen3.5-72b` | ❌ ERR | — | not a valid model ID |
| `qwen/qwen3.5-plus` | ❌ ERR | — | not a valid model ID |
| `qwen/qwen-3.5-plus` | ❌ ERR | — | not a valid model ID |
| `qwen/qwen-3.5-72b` | ❌ ERR | — | not a valid model ID |
| `qwen/qwen3.5-32b` | ❌ ERR | — | not a valid model ID |

## 结论

- **Llama 4 Maverick** → `meta-llama/llama-4-maverick` ✅
- **Qwen 3.5 Plus** → **该 endpoint 不支持任何 Qwen 3.5 变体**。推荐替代：`qwen/qwen3-235b-a22b`（实际路由到 04-28 版本，Qwen3 旗舰 MoE）
- **DeepSeek V4** → **该 endpoint 不支持 DeepSeek V4**。推荐替代：`deepseek/deepseek-chat`（路由到 V3）或 `deepseek/deepseek-chat-v3-0324`（指定版本）；如需推理模型用 `deepseek/deepseek-r1` 或 `deepseek/deepseek-r1-0528`

---
