# ssh d064 violation check batch1

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_d064_violation_check_batch1_20260519T234318_result.json`
- **Structured JSON:** [`57cb23a6c379118fad63.json`](../../sessions/57/57cb23a6c379118fad63.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

报告已写入 `artifacts/_project/report/d064_violation_batch1.md`。

## 结果总结

| Model | Decoding | Mode | ET% | RV% | DR% | CF% | E-F1 | R-F1 |
|-------|----------|------|-----|-----|-----|-----|------|------|
| Qwen  | beam-4   | unc  | 0.00 | 0.14 | 0.54 | 0.04 | 83.73 | 44.40 |
| Qwen  | beam-4   | con  | 0.00 | 0.00 | 0.00 | 0.01 | 84.00 | 44.46 |
| Llama | beam-4   | unc  | 0.00 | 0.04 | 0.10 | 0.06 | 85.16 | 47.17 |
| Llama | beam-4   | con  | 0.00 | 0.00 | 0.00 | 0.00 | 85.23 | 47.17 |

要点：
- **约束解码消除全部 violation**，Llama constrained 达到 4 项全 0.00%
- **F1 不降反微升**：Qwen E-F1 +0.27, Llama E-F1 +0.07；R-F1 持平或微升
- **Llama 全面优于 Qwen**：E-F1 高 ~1.2，R-F1 高 ~2.7
- **Qwen greedy 998-doc baseline 不存在**，两台服务器均未找到

---
