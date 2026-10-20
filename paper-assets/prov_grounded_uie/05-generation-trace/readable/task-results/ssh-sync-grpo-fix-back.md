# ssh sync grpo fix back

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_sync-grpo-fix-back_20260512T223513_result.json`
- **Structured JSON:** [`dfc2153c676303e0dfa4.json`](../../sessions/df/dfc2153c676303e0dfa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

同步完成。改动摘要：

### config.py
- **移除** `GRPOArgs` 中 4 个 vLLM 配置字段：
  - `use_vllm` (默认 True)
  - `vllm_mode` (默认 "colocate")
  - `vllm_gpu_memory_utilization` (默认 0.5)
  - `vllm_enable_sleep_mode` (默认 True)

### train_grpo.py
- **移除** `GRPOConfig` 构造中 4 个 vLLM 参数传递及注释：
  - `use_vllm=grpo_args.use_vllm`
  - `vllm_mode=grpo_args.vllm_mode`
  - `vllm_gpu_memory_utilization=grpo_args.vllm_gpu_memory_utilization`
  - `vllm_enable_sleep_mode=grpo_args.vllm_enable_sleep_mode`

修复本质：从 vLLM colocate 模式回退到 TRL 默认的 HF 原生生成，避免 vLLM 在单卡环境下的兼容性问题。

---
