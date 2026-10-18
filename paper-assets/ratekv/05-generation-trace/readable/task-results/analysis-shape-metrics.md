# analysis shape metrics

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_shape_metrics_20260514T201915_result.json`
- **Structured JSON:** [`a4fcc98a4e15b29e34c6.json`](../../sessions/a4/a4fcc98a4e15b29e34c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果汇总：

| Model | Heads | top5%conc | top1share | t1/t5 | t1/t2 | CV | Gini |
|---|---|---|---|---|---|---|---|
| **Yi-1.5-9B** | 192 | 0.7139 | **0.6434** | **0.9012** | **23.72** | 8.88 | 0.78 |
| **Llama-3.1-8B** | 256 | 0.3387 | 0.2418 | 0.7139 | 21.71 | 3.83 | 0.37 |
| **Qwen2.5-7B** | 112 | 0.6104 | 0.3461 | 0.5670 | 3.17 | 3.88 | 0.71 |
| **Mistral-7B-v0.3** | 256 | 0.2200 | 0.0401 | 0.1820 | 1.87 | 1.10 | 0.49 |
| **Gemma-2-9B** | 336 | 0.2299 | 0.0404 | 0.1757 | 1.52 | 1.23 | 0.53 |

**Spike vs Spread 分类清晰：**

- **Spike 型**：Yi-1.5（t1/t5=0.90, t1/t2=23.7）和 Llama-3.1（t1/t5=0.71, t1/t2=21.7）——单个 head delta 远超其余，top-1 几乎等于 top-5% 总和
- **Spread 型**：Mistral（t1/t5=0.18, t1/t2=1.87）和 Gemma-2（t1/t5=0.18, t1/t2=1.52）——delta 分散在多个 head 上
- **中间型**：Qwen（t1/t5=0.57, t1/t2=3.17）——有明显的 top head 但不像 Yi 那样极端集中

Yi-1.5 的 top-1 delta (13.12) 是第二大 (0.55) 的 **23.7 倍**，确认是极端 spike。Qwen 的 top-1 (6.74) 是 top-2 (2.12) 的 3.2 倍，属于 moderate concentration。

数据已保存在服务器 `/root/ratekv/shape_metrics.json` 和本地 `artifacts/shape_metrics.json`。

---
