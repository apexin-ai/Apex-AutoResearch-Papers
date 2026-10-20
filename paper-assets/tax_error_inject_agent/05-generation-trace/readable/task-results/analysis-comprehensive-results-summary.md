# analysis comprehensive results summary

**When Does Unpaired Error Injection Help LLM Agents? Hypotheses from a Failed Transfer to Embodied Planning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_comprehensive-results-summary_20260515T002159_result.json`
- **Structured JSON:** [`c2fceee688334a006afa.json`](../../sessions/c2/c2fceee688334a006afa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。汇总文档保存并注册为 artifact `art_20260515_aa47ed`。

文档包含 8 个维度：
- **Multi-seed clean eval**: Vanilla 65.3%±3.3, TaxEI 56.7%±8.6, Random 60.7%±7.6 (2-seed)
- **Recovery eval**: Vanilla 61.7%, TaxEI 59.6%, Random 63.8%，detection rate 全部 0%
- **Dose-response**: 10% injection 无影响, 25% injection −12.8pp
- **Training metrics**: 6 个训练 + 2 个 fixed-size ablation
- **Statistical tests**: McNemar p=0.375, cross-seed variance analysis
- **Pilot/early experiments** 和 **still running** (`v4-random-seed123-eval`)
- **Key takeaways**: 6 条 negative result 结论

---
