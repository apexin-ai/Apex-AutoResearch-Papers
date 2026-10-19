# code diag d3 step2

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_diag_d3_step2_20260516T193348_result.json`
- **Structured JSON:** [`60b6975804f5484b5f18.json`](../../sessions/60/60b6975804f5484b5f18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## D3 结果：FAIL

```
Method                 | Step Acc         | Crossing Rate | Lead Mean | Lead Median
-----------------------|------------------|---------------|-----------|------------
Static LR (layer14)    | 0.8172+-0.1631   | 46.51%        | -2.00     | -2.0
Temporal LR (w=5)      | 0.8274+-0.1906   | 65.12%        | -1.18     | -1.5
Temporal LR (w=10)     | 0.8364+-0.1887   | 65.12%        | -0.61     | -1.0
Temporal LR (w=15)     | 0.8478+-0.1736   | 76.74%        | -1.09     | -2.0
```

**判据**：best temporal (w=10) lead_mean=-0.61 vs static lead_mean=-2.00，delta=+1.39 steps。未达 >3 阈值，**FAIL**。

**关键观察**：
- 所有 lead_mean 均为负值，说明 crossing 发生在 commitment point **之后**，probes 整体偏迟
- Temporal window 确实提升了 crossing rate（46%→77%）和 step accuracy（81.7%→84.8%），但 lead time 改善有限
- 209 traces, 24.7% positive rate（类别不平衡明显）

Registry 已更新为 DONE/negative。

---
