# analysis selfbleu distinct metrics

**The Embedding Alignment Gap: Why Diversity-Based Data Selection Accelerates Model Collapse in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_selfbleu_distinct_metrics_20260513T163952_result.json`
- **Structured JSON:** [`ffe0d44153079a1f62f5.json`](../../sessions/ff/ffe0d44153079a1f62f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。4 个方法 × 8 代的多样性指标已保存至 `/root/autodl-tmp/div_cal_verify/diversity_metrics_seed42.csv`。

结果摘要：
- **gen_0 所有方法相同**（因为 gen_0 是同一个初始模型生成的）：self_bleu=0.0125, distinct_1=0.069, distinct_2=0.308, distinct_3=0.528
- **随代数增加，所有方法的多样性均下降**：distinct-n 和 TTR 持续降低，符合 model collapse 预期
- **Self-BLEU 也下降**（句间相似度降低），但这是因为文本整体趋同后每句本身更短/更重复，BLEU 的 precision 反而变低
- **RGDS 后期（gen_6-7）self_bleu 反而升高**（0.0096→0.0107），且 distinct 值最低，说明 RGDS 在后代也出现了显著退化
- **external_only 在 gen_6-7 的 distinct 值略优于其他方法**，distinct_3 从 0.113 到 0.115 有微弱回升

---
