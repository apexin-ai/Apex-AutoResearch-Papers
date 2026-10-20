# check c1 regen v2 completion

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_c1_regen_v2_completion_20260517T102428_result.json`
- **Structured JSON:** [`3b26daef8a8b4794ac54.json`](../../sessions/3b/3b26daef8a8b4794ac54.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**c1-regen-v2 实验成功完成。** Registry 已更新为 DONE/success。Cron 不存在（可能已被手动清除或从未创建）。

## 结果摘要

| Metric | Gen 0 | Gen 1 | Gen 2 | 趋势 |
|--------|-------|-------|-------|------|
| mean_quality | 0.1133 | 0.1132 | **0.1142** | 稳定微升 |
| vendi_score | 107.21 | 106.87 | **108.42** | 无 collapse |
| self_bleu | 0.00597 | 0.00623 | **0.0047** | 下降（多样性提升） |
| perplexity | 9.854 | 8.618 | 9.399 | 稳定 |
| mean_nn_distance | 0.7058 | 0.7026 | **0.7126** | 微升 |

关键结论：3 代迭代训练后 vendi_score 不降反升（107.21→108.42），self_bleu 下降，无 mode collapse 迹象。Hypothesis 得到验证。

---
