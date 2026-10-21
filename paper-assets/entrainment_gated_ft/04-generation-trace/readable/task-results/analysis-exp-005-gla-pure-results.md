# analysis exp 005 gla pure results

**Aggregate Equivalence̸=Behavioral Equivalence: Per-Example Multiplicity in Hybrid Linear Recurrent Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_exp-005-gla-pure-results_20260522T164258_result.json`
- **Structured JSON:** [`30cd9ddcc27490c0b2b9.json`](../../sessions/30/30cd9ddcc27490c0b2b9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

## exp-005-gla-pure 结果

| Task | Metric | GLA pure | GLA h3-1 | Δ |
|------|--------|----------|----------|---|
| lambada_openai | acc | 0.3392 | 0.3819 | -4.27pp |
| lambada_openai | ppl | 32.006 | 23.965 | +8.04 |
| arc_easy | acc | 0.5829 | 0.5673 | +1.56pp |
| arc_easy | acc_norm | 0.5114 | 0.5038 | +0.76pp |

- per-example log_samples: 有（两个 .jsonl），可用于后续 Jaccard 分析
- GLA 与其他三架构（GDN/RetNet/HGRN2）pattern 一致：attention 层选择性提升 LAMBADA（上下文预测），对 ARC-Easy 无正向效果甚至略负
- Registry 已更新为 DONE (success)，memory.md 已追加结果段落

---
