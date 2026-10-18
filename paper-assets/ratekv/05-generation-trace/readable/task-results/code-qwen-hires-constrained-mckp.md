# code qwen hires constrained mckp

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_hires_constrained_mckp_20260514T194934_result.json`
- **Structured JSON:** [`e153806f7daeabe57539.json`](../../sessions/e1/e153806f7daeabe57539.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Job completed successfully. Results:

| Method | WikiText-2 PPL | Delta vs Uniform |
|---|---|---|
| **Baseline (bf16)** | 9.8106 | — |
| **Constrained MCKP (k=8)** | 10.8909 | **+4.5575** |
| **Uniform 4-bit** | 15.4484 | — |

Key metrics:
- **MCKP improvement over uniform**: +4.5575 PPL (**80.8%** gap recovery)
- **Bit distribution**: 8-bit: 4 (Layer 0), 2-bit: 8, 4-bit: 100
- **Compression ratio**: 4x (memory ratio 0.25)
- **Top-5% concentration**: 0.4233
- Layer 0 heads all assigned 8-bit (l0_exclude_2bit=True), 2-bit heads spread across layers 1, 2, 11, 12, 13, 14, 15, 20

Results saved to `/root/ratekv/qwen_hires_constrained_results.json`. The float32 hires profiling data produces a strong result — 80.8% gap recovery vs uniform is substantially better than the previous bf16 data's improvement, confirming the value of higher-precision profiling.

---
