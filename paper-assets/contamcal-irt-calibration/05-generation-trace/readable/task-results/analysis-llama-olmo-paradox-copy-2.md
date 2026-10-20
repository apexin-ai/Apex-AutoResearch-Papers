# analysis llama olmo paradox

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_llama-olmo-paradox_20260522T235708_result.json`
- **Structured JSON:** [`d06013247dba22ef23ea.json`](../../sessions/d0/d06013247dba22ef23ea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析已写入 `artifacts/llama_olmo_paradox_analysis.md`。

**关键修正**（相对前版）：OLMo-2-7B 实际使用 GQA（32 heads / 8 KV heads），与 LLaMA-3.1 完全相同，而非前版写的 MHA。Vocab 也是 ~100K 而非 50K。架构几乎完全一致，排除了 attention capacity 差异作为解释因素。

**核心结论**：最可能的解释是 **pre-training data volume**（15T vs 4T，3.75× gap）驱动的 representation robustness 差异，辅以 OLMo-2 的 **两阶段训练 curriculum**（annealing 保留 plasticity）和 **post-norm 架构**（可能增加 SFT sensitivity）。LLaMA 的极端 over-training 使其表征对 LoRA 微调扰动免疫，而 OLMo-2 的较短训练+annealing 设计使其天然适合 post-hoc adaptation。

---
