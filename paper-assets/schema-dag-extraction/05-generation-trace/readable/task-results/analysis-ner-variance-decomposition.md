# analysis ner variance decomposition

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ner-variance-decomposition_20260517T053347_result.json`
- **Structured JSON:** [`c59e35c367988571e72e.json`](../../sessions/c5/c59e35c367988571e72e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

编译成功（warnings 仅为跨文件 reference，正常）。

**Few-NERD Variance Decomposition:**

| Count | Batch SD | Seed SD | Ratio |
|------:|--------:|--------:|------:|
| 2 | 0.1782 | 0.0557 | 10.2 |
| 6 | 0.1233 | 0.0160 | 59.2 |
| 12 | 0.1063 | 0.0297 | 12.8 |
| 22 | 0.0954 | 0.0096 | 99.2 |
| 44 | 0.1214 | 0.0143 | 72.4 |
| 66 | 0.0016 | 0.0002 | 46.3 |

**Mean ratio (counts 2--44):** 50.8x  
**Range:** 10.2--99.2x  
**编译:** 成功，PDF 已生成。

---
