# ops r3 grpo batch check

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_r3_grpo_batch_check_20260524T234149_result.json`
- **Structured JSON:** [`01bde289dfdde1c49640.json`](../../sessions/01/01bde289dfdde1c49640.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Now I have all the data. Here's the summary:

## Effective Batch Size 对比

| 实验 | batch_size | GA | num_gen | effective_batch | quantization |
|------|-----------|----|---------|-----------------| -------------|
| **QLoRA G=4** (所有 GRPO QLoRA runs) | 1 | **16** | 4 | **16** | QLoRA 4-bit |
| **plan_011 bf16 G=8** | 1 | **1** | 8 | **1** | bf16 LoRA |
| **r3_grpo_bf16_g4** | 1 | **1** | 4 | **1** | bf16 LoRA |

## 结论

**存在 batch size confound，但方向与预期相反。** QLoRA G=4 的 GA=16（effective batch=16），而所有 bf16 实验（plan_011 和 r3_grpo_bf16_g4）GA=1（effective batch=1）。

不过这个 confound 对论文 claim 的影响需要仔细分析：
- 论文的核心 claim 是 QLoRA GRPO collapse，bf16 GRPO 不 collapse
- QLoRA 有**更大**的 batch（16 vs 1），理论上更大 batch 应该**更稳定**而非更不稳定
- 所以 batch size 差异实际上**强化**了 claim——在更有利的训练条件下（更大 batch），QLoRA 仍然 collapse

**r3_grpo_bf16_g4 已完成**（100/100 steps，685s）。无需 kill。

**建议**：batch size confound 存在但**不需要重跑**——它是一个对 claim 有利的 confound（QLoRA 在更大 batch 下仍 fail），reviewer 如果追问可以用这一点反驳。如果 Director 仍想要一个完全匹配的控制实验（bf16 GA=16 G=4），可以补跑，但优先级不高。

---
