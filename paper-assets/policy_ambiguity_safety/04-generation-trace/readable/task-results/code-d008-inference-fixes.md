# code d008 inference fixes

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_d008_inference_fixes_20260520T094846_result.json`
- **Structured JSON:** [`052561bff617b8661178.json`](../../sessions/05/052561bff617b8661178.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部修正完成，验证通过。

**config_local.py:**
- 移除了 DeepSeek-V3 和 DeepSeek-V3.1
- Qwen3-32B 改为 AWQ int4 量化版（`Qwen/Qwen3-32B-AWQ`，~18GB VRAM），`vllm_extra_args` 含 `quantization: "awq"`
- 新增 Llama-4-Scout AWQ int4 备选（`meta-llama/Llama-4-Scout-17B-16E-Instruct-AWQ`）
- 新增 `DEFAULT_EXPERIMENT_MODELS = ["Qwen/Qwen3-8B", "Qwen/Qwen3-32B-AWQ"]`

**harness_local.py:**
- `_get_vllm_client` 新增 `_vllm_client_base_url` 跟踪变量，base_url 变化时重新创建 client
- `call_agent_transformers` 从 `async def` 改为 `def`，调用处移除 `await`

**clause_templates.json:**
- `scopal_001`：3→7 条 tool_responses，每个 order 有独立的 `get_order_details` 和 `cancel_pending_order`，按 order_id 精确匹配
- `scopal_025`：3→4 条，补充 ORD-21290 的 `get_order_details`，`args_pattern` 按 order_id 精确匹配
- `scopal_027`：3→4 条，补充 ORD-50280 的 `get_order_details`，同样精确匹配

---
