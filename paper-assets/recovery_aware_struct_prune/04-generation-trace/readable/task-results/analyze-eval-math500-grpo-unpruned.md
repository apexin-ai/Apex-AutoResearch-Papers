# analyze eval math500 grpo unpruned

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analyze_eval_math500_grpo_unpruned_20260518T045742_result.json`
- **Structured JSON:** [`bb89b9024e5eb2fff721.json`](../../sessions/bb/bb89b9024e5eb2fff721.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结果汇总

**Unpruned post-GRPO MATH-500: 69.0% (345/500) ± 2.07%**

| Model | MATH-500 | GSM8K |
|---|---|---|
| Unpruned pre-GRPO | **73.6%** (368/500) | — |
| Unpruned post-GRPO | **69.0%** (345/500) | 81.27% |
| SFT Standard 20% | 26.0% | — |
| SFT RASP 20% | 24.2% | — |

### Hypothesis 验证：**Negative**

GRPO 在 unpruned 模型上造成了 MATH-500 的 **4.6pp 下降**（73.6% → 69.0%），差异为 23 题。这既不是"保持不变"也不是"提升"，而是第三种意外结果：

1. **GRPO 在 GSM8K 上无变化**（81.27% → 81.27%），但在更难的 MATH-500 上造成退化
2. 这说明 GRPO v2 (step-100) 的 GSM8K reward signal 可能过度特化于 GSM8K 难度级别的问题，导致在更复杂的数学推理上出现 **alignment tax**
3. 17.2% 的回答被截断（86/500），平均回答长度 1768 tokens，说明模型在难题上倾向于生成冗长但未必正确的推理链

对于 pruned 模型的解读：pruned post-GRPO MATH-500 的 baseline 应与 69.0% 而非 73.6% 对比，因为 GRPO 本身就会引入 MATH-500 退化。

---
