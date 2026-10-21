# code training rtx5090 adapt

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_training-rtx5090-adapt_20260514T045017_result.json`
- **Structured JSON:** [`4eab0ea17f50fa7c5e77.json`](../../sessions/4e/4eab0ea17f50fa7c5e77.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。我注意到 linter 自动将 `grpo_trainer.py` 头部注释中的多卡示例改成了 `--deepspeed configs/deepspeed_zero3.json --reward_device cpu`，这是合理的（ZeRO-3 场景下 reward 模型放 CPU 也可以），不影响功能。

改动摘要：

**sft_trainer.py**:
- 加了 `--quantize`（默认开启）/ `--no_quantize`，启用时用 `BitsAndBytesConfig` 4-bit NF4 + double quant
- 加了 `--deepspeed` 传入 DeepSpeed 配置路径
- `per_device_batch_size` 默认 1，`gradient_accumulation_steps` 默认 16
- 头部注释更新了多卡启动命令

**grpo_trainer.py**:
- 同样的 QLoRA + DeepSpeed 参数
- 加了 `--reward_device`（默认 `cuda:3`），传给 `CEDRewardWrapper` → `CEDRewardModel`
- `gradient_accumulation_steps` 默认 16
- 头部注释更新

**新建 configs/**:
- `deepspeed_zero2.json` — ZeRO-2 + CPU offload optimizer
- `deepspeed_zero3.json` — ZeRO-3 + CPU offload optimizer & param
- `accelerate_4gpu.yaml` — 4 进程 DeepSpeed bf16 配置

---
