# analysis paper outline ab variants

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_paper_outline_ab_variants_20260517T035337_result.json`
- **Structured JSON:** [`2236fe2870cd55fc55cf.json`](../../sessions/22/2236fe2870cd55fc55cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已写入 `artifacts/paper_outline_ab.md`。

两套 outline 的核心区别：

- **Outline A** (纯 negative result): 贡献靠方法论 rigor + collapse 源头 taxonomy + LoRA artifact，故事是 "the field is solving a non-problem in this regime"，风险是 reviewer 觉得 scope 太小、insight 不够
- **Outline B** (boundary finding): 故事更强，有 actionable threshold (K=16 / 6.25% retention)，贡献是正面的 practical guideline + failure mode characterization，但依赖 K=16 实验确实触发 collapse

建议等 K=16 结果出来再决定走哪条线。如果 K=16 触发了 collapse，Outline B 明显更有竞争力（positive framing + actionable）。

---
