# diagnose llama 8k result extract

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_llama_8k_result_extract_20260515T141033_result.json`
- **Structured JSON:** [`0a49cdb8b644e270ee50.json`](../../sessions/0a/0a49cdb8b644e270ee50.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果汇总：

### Llama-3.1-8B 8K Spot-check 结果

| 指标 | BF16 Baseline | Constrained MCKP | Uniform 4-bit |
|------|--------------|-------------------|---------------|
| **8K PPL** | **5.5958** | **6.0537** | **6.0364** |
| 2K PPL (参考) | 8.0922 | 8.5042 | 8.4701 |

**MCKP vs Uniform 4-bit @ 8K**: -0.0174 (**-3.94%**，MCKP 略差于 uniform）

**Attention 特征**: Spike 型，concentration=0.5749，t1/t5=0.71
**Bit 分配**: 2-bit×2, 4-bit×253, 8-bit×1（几乎全4-bit）

**关键发现**: Llama-3.1-8B 在 8K 上 MCKP 仍然略逊于 uniform 4-bit（-3.94%），与 2K 结果一致（-9.01%）。Spike 型 attention 分布下 MCKP 无优势，与 Qwen-7B Spread 型形成鲜明对比。

---
