# analysis did parallel trends

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_did-parallel-trends_20260522T231708_result.json`
- **Structured JSON:** [`d27a79e44f31a275d669.json`](../../sessions/d2/d27a79e44f31a275d669.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Balance check 完成。

**结果**：pre-treatment balance 在所有维度上都成立，parallel trends 假设有良好支撑：

| 维度 | p-value | 效应量 |
|------|---------|--------|
| Accuracy | 0.391 | d = 0.017 |
| Difficulty quintile | 0.194 | V = 0.018 |
| Domain | 0.263 | V = 0.017 |
| Subject (57个) | 0.290 | V = 0.066 |
| KS 分布检验 | 0.639 | D = 0.014 |

Treated 和 untreated 组在 baseline accuracy（差异仅 +0.6pp）、难度分布、领域组成和科目组成上均无显著差异，所有效应量均可忽略。这与 25% 随机抽样机制一致。

输出已写入 `artifacts/did_parallel_trends_balance.md`。

---
