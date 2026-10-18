# exp kivi baseline qwen7b

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_kivi_baseline_qwen7b_20260515T143618_result.json`
- **Structured JSON:** [`78878762fd8033819ffa.json`](../../sessions/78/78878762fd8033819ffa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验完成，registry 和 artifact 已更新。

**结果汇总**：

| 方法 | PPL (WikiText-2) |
|------|-----------------|
| BF16 baseline | 9.81 |
| **KIVI-4bit** (per-channel K + per-token V, g32, r128) | **9.90** |
| Constrained MCKP (per-head, 4× compression) | 10.91 |
| Uniform 4-bit (per-head) | 15.45 |

KIVI-4bit PPL=9.90，几乎无损（vs BF16 9.81），显著优于 uniform 4-bit (15.45) 和 constrained MCKP (10.91)。这说明 per-channel/per-token 粒度的量化在 4× 压缩下非常有效——但代价是需要更细粒度的 scale/zero-point 存储，且与我们的 per-head MCKP 方法正交（后者优势在于 mixed-precision bit allocation）。

---
