# code qwen bf16 uniform eval

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_bf16_uniform_eval_20260514T061221_result.json`
- **Structured JSON:** [`9b6850818d3b97fe83b7.json`](../../sessions/9b/9b6850818d3b97fe83b7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果：

| 指标 | 值 |
|------|-----|
| **baseline_ppl_bf16** | **8.8191** |
| **uniform_4bit_ppl_bf16** | **63.4134** |
| delta | +54.5942 |

Baseline bf16 = 8.8191，与已知值 8.819 一致。

**注意：uniform 4-bit bf16 PPL = 63.41，远高于 fp16 的 15.45。** 这个差异非常大（63 vs 15），说明 bf16 量化精度下 uniform 4-bit 的 round-trip 误差显著更大。可能原因：`quantize_per_channel` / `quantize_per_token` 在 bf16 下的 rounding 行为不同于 fp16（bf16 mantissa 只有 7 bit vs fp16 的 10 bit），导致 4-bit 量化→反量化的累积误差更大。

这个数字如果要用在 paper 中，需要确认量化函数在 bf16 下的行为是否符合预期——fp16 和 bf16 的 uniform 4-bit 结果差 4 倍，不太正常。

---
