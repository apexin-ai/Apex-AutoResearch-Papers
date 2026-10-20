# ops plan 011 eval g8 bf16 ckpt100

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan_011_eval_g8_bf16_ckpt100_20260515T144139_result.json`
- **Structured JSON:** [`f00a24a2eb8a55cc8797.json`](../../sessions/f0/f00a24a2eb8a55cc8797.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Eval 已启动，正在加载模型。关键信息：

- 正确找到 checkpoint-100，使用 `--no-quantize` (bf16)
- 完整 model stack: base_model + sft_adapter + checkpoint-100 adapter
- batch_size=16, split=dev, seed=42
- 输出到 `/root/autodl-tmp/eval_results/grpo_g8_bf16/checkpoint-100/`

预计 ~1.5h 完成。结果出来后对比：
- SFT baseline: rel_f1=0.4057, evi_f1=0.7979
- QLoRA GRPO best: rel_f1=0.217 (catastrophic forgetting)

如果 bf16 GRPO 的 rel_f1 接近或超过 SFT baseline → 量化是 QLoRA 失败根因；如果也 forgetting → GRPO 算法层面不适合结构化 IE。

---
