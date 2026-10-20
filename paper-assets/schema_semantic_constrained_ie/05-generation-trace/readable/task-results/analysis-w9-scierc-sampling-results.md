# analysis w9 scierc sampling results

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_w9_scierc_sampling_results_20260516T203238_result.json`
- **Structured JSON:** [`0cc6737ac95a4e761d88.json`](../../sessions/0c/0cc6737ac95a4e761d88.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。核心结论：

**Constraints 在 sampling 解码下完全 robust。** ET/RV 保持 0%，DR 从 0.93% 微降到 0.75%，CF 不变（~9.9%）。Entity F1 基本持平（+0.30），Relation F1 小幅下降（-0.94）。

注意：v2 checker 计算的 greedy baseline F1（E=30.98, R=8.36）与任务描述中的数值（E=35.38, R=18.59）不一致，可能是之前使用了不同的评估方法。报告中已用同一 checker 做了 apples-to-apples 对比。

---
