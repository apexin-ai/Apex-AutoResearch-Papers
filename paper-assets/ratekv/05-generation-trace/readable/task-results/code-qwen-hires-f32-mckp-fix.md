# code qwen hires f32 mckp fix

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_qwen_hires_f32_mckp_fix_20260514T200644_result.json`
- **Structured JSON:** [`5b088a2e7fd34248fea7.json`](../../sessions/5b/5b088a2e7fd34248fea7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果汇总：

| Method | WikiText-2 PPL | Delta vs Uniform |
|---|---|---|
| Baseline (bf16) | **9.8106** | — |
| Constrained MCKP (k=8) | **10.8921** | **+4.5563** |
| Uniform 4-bit | **15.4484** | — |

- **MCKP improvement**: +80.8% of gap recovered vs uniform 4-bit
- **Bit distribution**: 8-bit: 4, 4-bit: 100, 2-bit: 8
- **top5_concentration**: 0.6156（接近 D048 verified 0.6104，差异来自 `enforce_monotonicity` 调整）
- **Baseline PPL**: 9.8106（符合预期 ~9.81）
- **结果文件**: `westd-37397:/root/ratekv/qwen_hires_f32_constrained_results.json`

值得注意：MCKP PPL=10.89 与之前用 lowres profiles 的结果几乎一致，说明 lowres 和 hires profiling 在 Qwen 上给出了非常相似的 MCKP allocation，但 uniform 4-bit PPL 从之前的值变为 15.45，使 MCKP 的相对优势更大（80.8%）。

---
