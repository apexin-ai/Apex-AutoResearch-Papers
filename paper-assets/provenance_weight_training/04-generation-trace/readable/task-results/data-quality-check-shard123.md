# data quality check shard123

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_quality-check-shard123_20260513T221536_result.json`
- **Structured JSON:** [`1b3413aafc8a85444fb5.json`](../../sessions/1b/1b3413aafc8a85444fb5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 shard 质量检查全部通过，结果高度一致：

```
Shard          Docs  Corp D3  Mean D3   Degen%   AvgLen   EffLen
--------------------------------------------------------------
shard_0       85248   0.3286   0.7001    0.87%    304.2    173.9
shard_1       85248   0.3291   0.7005    0.92%    304.0    174.1
shard_2       85248   0.3286   0.6992    0.90%    303.8    173.7
shard_3       85248   0.3287   0.7000    0.94%    304.1    174.2
```

- 退化率范围 0.87%–0.94%，远低于 30% 阈值
- corpus distinct-3 ≈ 0.329，mean doc distinct-3 ≈ 0.700，四个 shard 间差异 < 0.002
- 平均文档长度 ~304 tokens，有效长度 ~174 tokens，各 shard 一致
- 不同 seed 未引入质量差异，全部合格

---
