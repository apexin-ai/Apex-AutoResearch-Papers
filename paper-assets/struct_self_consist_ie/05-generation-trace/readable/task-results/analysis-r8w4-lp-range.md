# analysis r8w4 lp range

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r8w4_lp_range_20260515T221454_result.json`
- **Structured JSON:** [`4fbfe97f6c8fe8f5abe3.json`](../../sessions/4f/4fbfe97f6c8fe8f5abe3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果：

### LP Range 分析（Cumulative Log Prob）

| Seed | Subtask | N | Median LP Range | IQR | Mean±Std |
|------|---------|---|-----------------|-----|----------|
| 42 | ner | 551 | 8.1946 | [5.76, 11.28] | 8.91±4.58 |
| 123 | ner | 551 | 8.2111 | [6.16, 11.43] | 9.15±4.71 |
| 456 | **joint** | 551 | 8.3672 | [6.00, 11.51] | 9.21±4.78 |
| 456 | ner | 551 | 8.1411 | [5.70, 11.42] | 8.81±4.39 |

### 结论

- Seed 456 (joint) 与 seed 42/123 (ner) 的 LP range **无显著差异**：
  - 相对差异仅 **2.0%**（远低于 10% 阈值）
  - Mann-Whitney U 检验 p = 0.551（不显著）
- Mean LP range 也几乎一致（各 seed 的 median 都在 0.054–0.061 之间）
- 额外对照：seed 456 的 NER-only 重跑版本与 joint 版本 LP range 也基本一致
- Kruskal-Wallis 三组 NER seeds 检验 p = 0.482（三组间无差异）

**Joint decoding 未改变 LP range 分布，种子间可比。**

结果已保存到 `output/review_round8/r8w4_lp_range_analysis.json`。

---
