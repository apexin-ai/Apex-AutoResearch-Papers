# data fix mixed ratio

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_fix-mixed-ratio_20260513T215509_result.json`
- **Structured JSON:** [`98d3acdd754cedadfd8e.json`](../../sessions/98/98d3acdd754cedadfd8e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

### 报告

| 指标 | 值 |
|------|-----|
| **总文档数** | 371,499 |
| **Human 文档** | 164,889 (44.4%) |
| **Synthetic 文档** | 206,610 (55.6%) |
| **Human tokens** | ~120M |
| **Synthetic tokens** | ~80M |
| **总 tokens** | ~200M |
| **Contamination ratio (token)** | **40.00%** |
| **旧文件备份** | `data/mixed_data_old_67pct.jsonl` |

文档数比例 44.4%/55.6% 而 token 比例为 60%/40%，差异是因为 synthetic 文档平均长度比 human 短。token 维度上精确达到了 D004 协议要求的 40% synthetic / 60% human。

---
