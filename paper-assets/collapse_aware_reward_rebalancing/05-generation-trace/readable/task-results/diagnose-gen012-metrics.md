# diagnose gen012 metrics

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_gen012-metrics_20260516T133230_result.json`
- **Structured JSON:** [`61e13ccaa690a14005e8.json`](../../sessions/61/61e13ccaa690a14005e8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
=== QUICK PROBE 03 (single_reward) ===
Status: RUNNING — Gen 2 generating candidates (1216/2000)

| Metric          | Gen 0    | Gen 1    | Gen 2 | Δ Gen1 vs 0 |
|-----------------|----------|----------|-------|-------------|
| mean_quality    | 0.1123   | 0.1138   | —     | +1.4%       |
| vendi_score     | 107.54   | 106.73   | —     | -0.8%       |
| self_bleu       | 0.0059   | 0.0091   | —     | +54.2%      |
| mean_nn_distance| 0.7088   | 0.7065   | —     | -0.3%       |
| perplexity      | 10.60    | 9.73     | —     | -8.2%       |
| complexity_mean | 2.8633   | 2.7944   | —     | -2.4%       |

=== NO-CURATION BASELINE 01 ===
Status: RUNNING (PID 501406, cuda:1)
Current gen: 0 (training done, evaluating — scoring quality in progress)
No metrics yet.
```

要点：Gen 0→1 quality 微升 +1.4%，diversity 指标几乎持平（vendi -0.8%, nn_dist -0.3%），但 self_bleu 涨了 54%（绝对值仍很低 0.006→0.009）。perplexity 下降 8.2% 说明模型对自身输出更"自信"。Gen 2 metrics 预计还需等候生成+评分+训练完成。

---
