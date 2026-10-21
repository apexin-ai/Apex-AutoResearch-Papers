# paper cross model ablation and nli update

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_cross-model-ablation-and-nli-update_20260523T163830_result.json`
- **Structured JSON:** [`6382902707d9c389b683.json`](../../sessions/63/6382902707d9c389b683.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有编辑已完成，验证通过。

**总结：**

1. **solutions.tex — capability-gap paragraph**: 添加了 BART/RoBERTa full cross-generator 表格引用（Tables ref）
2. **solutions.tex — new paragraph**: 在 domain-adapted verifier 之后添加了 "Cross-model voting vs. cross-architecture NLI" 段落，包含 Mistral-7B 弱 voter 降低强 generator 的数据（-9.33, -2.33, -2.67pp）、Qwen2.5-14B 强 voter 在 w=5 也降低 Qwen3（-2.50pp, p=0.006）、DeBERTa NLI 从不降低任何 generator 的对比
3. **appendix.tex — BART table** (`tab:bart-combo-full`): 4 generators × BART-large-mnli，仅 Mistral 显著
4. **appendix.tex — RoBERTa table** (`tab:roberta-combo-full`): 4 generators × RoBERTa-large-mnli，仅 Mistral 显著
5. **appendix.tex — cross-model ablation table** (`tab:cross-model-ablation`): ProofWriter + FOLIO，含 Qwen2.5-14B voter、Mistral-7B voter、DeBERTa NLI 三组对比，共 19 行

**关于 "60 tested conditions" 计数**：不需要更新。60 = 16 main + 27 remediation + 17 analytical，全部在 self-extraction paradigm 内。Cross-model SC ablation 使用外部模型的投票（非 self-extracted constraints），属于 §6 escape mechanism 的控制实验，不在此计数范围内。

---
