# debug mistral mckp constraint

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_mistral_mckp_constraint_20260514T070410_result.json`
- **Structured JSON:** [`efe520210bb501206cdc.json`](../../sessions/ef/efe520210bb501206cdc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

| Method | PPL | Delta vs Baseline |
|--------|-----|------------------|
| Baseline (bf16) | 7.0351 | --- |
| Uniform 4-bit | 7.1314 | +0.0962 |
| MCKP max_2bit=18 (原始) | 7.3231 | +0.2880 |
| **MCKP max_2bit=16 (修正)** | **7.3106** | **+0.2755** |

修正约束后 PPL 改善了 **-0.0125**（7.3231→7.3106）。虽然改善不大，但方向正确——减少 2-bit heads 确实降低了 compounding error。

不过 MCKP 仍然劣于 uniform 4-bit（7.31 vs 7.13），Mistral 在 4x 压缩率下的 negative result 不变。

需要更新 registry 吗？或者还有其他操作？

---
