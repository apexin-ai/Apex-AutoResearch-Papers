# eval llama31 random s0 injected

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_llama31-random-s0-injected_20260516T115621_result.json`
- **Structured JSON:** [`3e0727f214cf7c45f4f0.json`](../../sessions/3e/3e0727f214cf7c45f4f0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

任务完成。Registry `llama31-random-s0-eval` 已更新为 DONE。

**总结：**

LLaMA Random s0 injected eval 已于今天早些时候完成，结果：
- **Recovery: 74.5%** | **Detection: 25.5%**
- 对比 s42 (recovery 76.6%, detection 29.8%)，s0 略低但整体一致
- 两个 seed 的 Random baseline 均显著低于 s42 的 TaxEI（74.5%），验证了 Random 训练无显著注入恢复增强

---
