# data qwen14b table1 extract

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_qwen14b_table1_extract_20260515T144133_result.json`
- **Structured JSON:** [`910379c76c9ff5818d04.json`](../../sessions/91/910379c76c9ff5818d04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。Qwen2.5-14B constrained pipeline 完整 PPL 数据（Table 1 用）：

| Metric | Value |
|--------|-------|
| BF16 baseline | 6.8654 |
| Uniform 4-bit | 7.2020 |
| Constrained MCKP | 7.2206 |
| Unconstrained MCKP | 7.6923 |
| Δ constrained vs uniform | **−0.019** (−5.5%) |
| Δ unconstrained vs uniform | −0.490 |

**Bit distribution (constrained)**: 374×4bit + 8×2bit + 1×8bit + 1×16bit
**Shape**: Flat (conc=0.33, t1/t5=0.68, top1=22.6%, top5=33.0%)

符合预期：Flat profile 下 constrained MCKP ≈ uniform，几乎无非均匀分配收益。

---
