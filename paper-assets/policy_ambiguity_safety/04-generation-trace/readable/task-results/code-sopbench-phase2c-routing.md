# code sopbench phase2c routing

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sopbench_phase2c_routing_20260522T163058_result.json`
- **Structured JSON:** [`48a6047e604ca70ccb4b.json`](../../sessions/48/48a6047e604ca70ccb4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes applied and verified:

1. **`swarm/constants.py`** — Added `"gpt-5.4"` to `OPENAI_MODELS`, `AVAILABLE_MODELS["openai"]`, and `FUNCTION_CALLING_MODELS["openai"]`.

2. **`run_full_experiment.py`**:
   - Added `MODEL_ROUTING` dict with 5 entries (gpt-5.4, gpt-4.1 via OpenAI direct; claude-sonnet-4-6, qwen3-235b, deepseek-v3 via OpenRouter)
   - Added `--api-key` and `--base-url` CLI args as overrides
   - Routing logic in `main()`: looks up model in `MODEL_ROUTING`, sets env vars, dynamically registers OpenRouter model IDs in `OPENAI_MODELS`/`FUNCTION_CALLING_MODELS` so the handler uses the OpenAI backend
   - Output directory uses the short `--model` name, handler gets the full `model_id`
   - Timeout: 600s → 300s
   - Retry: max 3 → 2, delay 30s → 10s

---
