# experiment plan 006 qwen3 1 7b sft bf16

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_plan_006_qwen3_1_7b_sft_bf16_20260516T063412_result.json`
- **Structured JSON:** [`eae00d28d8c5527cc7a0.json`](../../sessions/ea/eae00d28d8c5527cc7a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。

**训练已在 cuda:3 启动**（PID 310381）：
- 模型：Qwen3-1.7B，bf16 LoRA（无量化），`--no-quantize`
- LoRA：rank=64, alpha=128, 69.7M trainable / 1.79B total (3.89%)
- 数据：3027 samples, 3 epochs, batch=1×16 accumulation, lr=2e-4, seed=42
- 输出：`/root/autodl-tmp/sft_output_qwen3_1_7b_bf16/`
- 日志：`~/runs/faith-evidence-ie/plan_006_qwen3_1_7b_sft_bf16.log`
- Registry：`plan_006_qwen3_1_7b_sft_bf16` → RUNNING，spec.quantize="none (bf16 LoRA)"

---
