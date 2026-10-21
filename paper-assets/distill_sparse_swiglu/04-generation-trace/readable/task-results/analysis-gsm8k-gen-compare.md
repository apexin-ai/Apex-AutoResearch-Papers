# analysis gsm8k gen compare

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_gsm8k_gen_compare_20260516T003648_result.json`
- **Structured JSON:** [`51594217e946f58664df.json`](../../sessions/51/51594217e946f58664df.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结论已写入 registry (exp_id: gsm8k_gen_compare, status: DONE)。

---

## 结论

**退化模式：(A) 推理丧失 — degenerate repetition loops**

10/10 个 GSM8K 样本中，KL sparse 50% 模型表现一致：
- 开头 1-3 个短语看似合理，随后立刻陷入**句子级重复循环**
- **从未产生任何算术运算或最终答案**
- 偶见拼写退化 (crabs→crbs, skein→skeen)
- Sample 7 最接近成功：正确算出 9×2=18，但无法完成 "+3" 这步

对比 dense 模型（推理链完整，4/10 答对），50% sparsity 彻底摧毁了 autoregressive generation 能力。GSM8K exact_match 从 0.5004→0.0121 不是"算错数"，是"完全无法推理"。

---
