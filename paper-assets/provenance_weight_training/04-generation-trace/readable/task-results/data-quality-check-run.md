# data quality check run

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_quality-check-run_20260513T215114_result.json`
- **Structured JSON:** [`1d3e82998c0462a6cc4f.json`](../../sessions/1d/1d3e82998c0462a6cc4f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Shard_0 合成数据质量报告

| 指标 | 值 |
|------|-----|
| 文档数 | 85,248 |
| Corpus distinct-3 | 0.3286 |
| Mean document distinct-3 | 0.7001 |
| 退化样本数 | 742 / 85,248 (**0.87%**) |
| 平均文档长度 | 304.2 tokens |
| 平均有效（非重复）长度 | 173.9 tokens (57.2%) |
| **是否超过 30% 退化阈值** | **否，远低于阈值** |

### 退化样本示例（distinct-3 < 0.1）

1. **idx=79** (d3=0.031): `2 RV Sites, 1 Tent Site, 2 RV Sites, 1 Tent Site, 2 RV Sites, 1 Tent Site, 2 RV Sites, 1 Tent Site...`

2. **idx=146** (d3=0.016): `Events Calendar\nEvents Calendar\nEvents Calendar\nEvents Calendar\nEvents Calendar...`

3. **idx=409** (d3=0.056): `No 8 Do Duc Duc Road Me Tri, Tu Liem DistrictOutstanding 100%\nNo 8 Do Duc Duc Road Me Tri...`

### 结论

退化率 0.87%，远低于 30% 阈值，无需抽查 shard_1。退化样本主要来自源文档本身就是结构化重复内容（表格、列表、日历），不是生成模型退化。数据质量合格，不阻塞 MVP。

---
