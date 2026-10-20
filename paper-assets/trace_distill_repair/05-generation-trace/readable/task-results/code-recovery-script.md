# code recovery script

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_recovery_script_20260515T015437_result.json`
- **Structured JSON:** [`15eb26104802ead4f385.json`](../../sessions/15/15eb26104802ead4f385.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 值 |
|------|-----|
| 总 segments | 3922 |
| 正常 scored | 2256 |
| **error segments** | **1666** |
| 成功恢复 label | **1203** (72.2%) |
| 无法恢复 | 463 (27.8%) |
| 恢复出 keep | 20 |
| 恢复出 drop | 1183 |
| 恢复的平均 confidence | 0.9052 |

**Keep rate 对比：**
- 原始 (仅 ok segments): 38 keep / 2256 total = **1.68%**
- 修正后 (ok + recovered): 58 keep / 3459 total = **1.68%**

关键发现：**之前的 bias 假设不成立。** 恢复的 1203 个截断 segment 中，keep 只有 20 个（1.66%），和原始 keep rate 几乎一致。截断并没有系统性低估 keep rate — drop segment 的 reasoning 同样会被截断。keep rate 极低（~1.7%）是真实的，不是采样偏差。

`recovery_analysis.json` 已保存到 `/root/trace_distill_repair/pipeline_output/recovery_analysis.json`。

---
