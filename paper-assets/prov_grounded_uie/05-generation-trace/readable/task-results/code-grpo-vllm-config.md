# code grpo vllm config

**prov grounded uie** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_grpo-vllm-config_20260512T203447_result.json`
- **Structured JSON:** [`fac101ab22ee508ccb0a.json`](../../sessions/fa/fac101ab22ee508ccb0a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

改动完成。摘要：

### train_grpo.py
- **移除** `AutoModelForCausalLM.from_pretrained()` 显式模型加载 — colocate 模式下 GRPOTrainer 内部管理 HF 模型和 vLLM 引擎
- **`model` 参数**：从模型对象改为传 `grpo_args.sft_checkpoint` 路径字符串
- **`model_kwargs`** 通过 `GRPOConfig.model_init_kwargs` 传递（控制 HF 模型加载的 dtype、flash attention 等）
- **GRPOConfig** 新增 4 个 vLLM 参数：`use_vllm`, `vllm_mode`, `vllm_gpu_memory_utilization`, `vllm_enable_sleep_mode`
- 移除未使用的 `AutoModelForCausalLM` import

### config.py
- **GRPOArgs** 新增 4 个字段，默认值：`use_vllm=True`, `vllm_mode="colocate"`, `vllm_gpu_memory_utilization=0.5`, `vllm_enable_sleep_mode=True`，均可通过 CLI `--use_vllm False` 等覆盖

---
