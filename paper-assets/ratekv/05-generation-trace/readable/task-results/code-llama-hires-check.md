# code llama hires check

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_llama_hires_check_20260514T052040_result.json`
- **Structured JSON:** [`7ce15a5ce45f2a1d5dea.json`](../../sessions/7c/7ce15a5ce45f2a1d5dea.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新，状态 DONE，结论 **success**。

汇总：

| Method | PPL | Delta vs BF16 |
|--------|-----|---------------|
| Baseline (bf16) | 8.0918 | — |
| Uniform 4-bit | 8.4690 | +0.3772 |
| Lowres MCKP (16×512) | 8.6951 | +0.6033 |
| **Hires MCKP (64×2048)** | **8.4498** | **+0.3581** |

Hires MCKP 以 8.4498 击败 uniform 4-bit 的 8.4690，PPL 退化从 lowres 的 0.6033 降至 0.3581（减少 40.7%）。Llama-3.1-8B 上 hires profiling 有效，与 Qwen 上的结论一致。

---
