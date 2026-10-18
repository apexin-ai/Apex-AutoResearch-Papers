# ops qwen sweep v2 results

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_qwen_sweep_v2_results_20260515T192240_result.json`
- **Structured JSON:** [`5bb78c1d902a96bfeb1d.json`](../../sessions/5b/5bb78c1d902a96bfeb1d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。结果如下：

## Qwen2.5-7B Compounding Sweep v2 (budget=0.25, 112 KV heads)

| k | PPL | n_2bit | mem_ratio | compounding ratio |
|----:|--------:|-------:|----------:|------------------:|
| 0 | 9.8106 | 0 | 1.0000 | 1.00x |
| 2 | 9.8324 | 2 | 0.9844 | 1.00x |
| 4 | 9.8486 | 4 | 0.9688 | 1.00x |
| 8 | 10.0474 | 8 | 0.9375 | 1.02x |
| 16 | 10.3953 | 16 | 0.8750 | 1.06x |
| 32 | 11.6325 | 32 | 0.7500 | 1.19x |
| 64 | 23.2176 | 64 | 0.5000 | 2.37x |
| 128 | 98.7523 | 96 | 0.2500 | 10.07x |
| 256 | 98.7523 | 96 | 0.2500 | 10.07x |

*compounding ratio = PPL(k) / PPL(0)；k=128 和 k=256 均命中 budget 上限 n_2bit=96（86% heads），结果相同。*

## 跨模型对比

| k | Llama (PPL / ratio) | Qwen (PPL / ratio) |
|----:|--------------------:|--------------------:|
| 0 | 8.09 / 1.00x | 9.81 / 1.00x |
| 8 | 8.23 / 1.02x | 10.05 / 1.02x |
| 64 | 11.99 / 1.48x | 23.22 / 2.37x |
| 256 | 1519.19 / 188x | 98.75 / 10.07x |

**总结：** Qwen 的 compounding 效应在中等 k 时（k=64）比 Llama 更严重（2.37x vs 1.48x），但在极端 k 时远不如 Llama 剧烈（10x vs 188x）。不过 k=256 的对比不完全公平——Qwen 因 budget 限制在 n_2bit=96 就触顶（86% heads），而 Llama 可能量化了更高比例的 heads。核心发现：Qwen 的 distortion landscape 更均匀，少数几个 head 没有像 Llama 那样出现灾难性的 compounding 爆炸。

---
