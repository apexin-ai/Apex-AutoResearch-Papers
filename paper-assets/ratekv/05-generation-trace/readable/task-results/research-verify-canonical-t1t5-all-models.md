# research verify canonical t1t5 all models

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_verify_canonical_t1t5_all_models_20260515T130038_result.json`
- **Structured JSON:** [`46aacb5cbc2ac5610259.json`](../../sessions/46/46aacb5cbc2ac5610259.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Sanity check 通过：Qwen-7B concentration=0.5992 ≈ 0.61，shape=Spread。

结果汇总：

| Model | concentration | t1_t5 | shape | top1_head | 变化? |
|-------|-------------|-------|-------|-----------|------|
| Qwen-7B | 0.5992 | 0.6406 | Spread | L0H0 | no (sanity check) |
| Llama-3.1-8B | 0.3360 | 0.7315 | Spike | L2H5 | no |
| **Yi-1.5-9B** | **0.5264** | **0.6980** | **Spread** | L4H3 | **YES (was Spike)** |
| Mistral-7B | 0.2200 | 0.1820 | Flat | L2H5 | no |
| Gemma-2-9B | 0.2592 | 0.1800 | Flat | L29H7 | no |

**Yi-1.5-9B 分类变了**：从 Spike → Spread。用 canonical 公式（concentration 比值而非 raw delta 比值）计算后，Yi 的 concentration=0.5264 (≥0.50) 且 t1_t5=0.6980 (≤0.70)，符合 Spread 条件。不过两个指标都紧贴边界（concentration 仅超 0.50 约 5%，t1_t5 距 0.70 仅差 0.002），属于边界案例。

其余三个模型（Llama=Spike, Mistral=Flat, Gemma-2=Flat）分类不变。

---
