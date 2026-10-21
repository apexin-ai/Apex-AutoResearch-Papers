# analysis dstudy single condition

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_dstudy_single_condition_20260521T132403_result.json`
- **Structured JSON:** [`a9b09099e9ccbbd5725c.json`](../../sessions/a9/a9b09099e9ccbbd5725c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。关键结果：

| 指标 | 值 |
|------|-----|
| **单条件 G @ 200 items** | 0.559 |
| **单条件 G @ 116 items (IRT推荐)** | 0.424 |
| **单条件 G≥0.80 所需 items** | 631 |
| **Multi-facet G @ 72 items** | 0.802 (验证通过) |
| **Multi-facet G @ 200 items** | 0.918 (验证通过) |
| **Delta 比值 (single/multi)** | 8.86× |

所有检查通过：
- G 单调递增 ✓
- 单条件 delta (0.089) 远大于 multi-facet delta (0.010) ✓
- 单条件 G@200 (0.559) 远低于 multi-facet G@200 (0.918) ✓

单条件下 residual 独占 53.5% 的误差方差（因为不再被 1296 个条件平均掉），precision×item 贡献 14%、seed×item 12.6%、prompt×item 12.2%。这意味着 IRT 的单条件假设下，即使 200 items 也只有 G=0.56——需要 631 items 才能达到 G≥0.80，是 multi-facet 的 8.8 倍。

输出文件：`results/exp001_analysis/dstudy_single_condition.json`

---
