# code plan 009 oracle comparison

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan_009_oracle_comparison_20260514T110435_result.json`
- **Structured JSON:** [`fd31eca2b648cc626431.json`](../../sessions/fd/fd31eca2b648cc626431.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成。结果：

| Layer | MCKP combo | Oracle combo | Gap (PPL) |
|-------|-----------|-------------|-----------|
| 0 | (8,8,8,8) | (8,8,8,8) | 0.0000 |
| 1 | (2,4,2,4) | **(2,4,4,2)** | **0.0183** |
| 2 | (4,4,2,4) | (4,4,2,4) | 0.0000 |
| 4 | (4,4,2,4) | **(4,4,4,2)** | 0.0045 |
| 5 | (4,2,4,4) | (4,2,4,4) | 0.0000 |
| 6 | (4,4,2,4) | (4,4,2,4) | 0.0000 |
| 10 | (4,2,4,4) | (4,2,4,4) | 0.0000 |
| 11 | (4,4,2,4) | **(2,4,4,4)** | 0.0136 |

**结论**：
- MCKP PPL = 10.9131
- **Max gap = 0.0183 PPL**，avg gap = 0.0046 PPL
- 5/8 有替代方案的层 MCKP 完全最优（gap=0）
- 3 个层有微小改进，都是 2-bit head 在层内换位置（不改变总 bit 数），说明 additive distortion assumption 在同 bit 预算内基本成立
- 54 次 real eval，21.3 分钟完成

---
