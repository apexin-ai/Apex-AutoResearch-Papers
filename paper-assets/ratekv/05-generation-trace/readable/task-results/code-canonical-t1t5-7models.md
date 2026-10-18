# code canonical t1t5 7models

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_canonical_t1t5_7models_20260515T130817_result.json`
- **Structured JSON:** [`470a57edfd1a725b17a6.json`](../../sessions/47/470a57edfd1a725b17a6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 7 模型表：

| Model | Heads | top5%conc | top1share | t1/t5 | t1/t2 | CV | Gini |
|---|---|---|---|---|---|---|---|
| Qwen2.5-7B | 112 | 0.6104 | 0.3461 | 0.5670 | 3.1741 | 3.8752 | 0.7065 |
| **Qwen2.5-14B** | 384 | 0.3312 | 0.1885 | 0.5693 | 7.7954 | 3.7370 | 0.5626 |
| Llama-3.1-8B | 256 | 0.3387 | 0.2418 | 0.7139 | 21.7098 | 3.8343 | 0.3688 |
| Yi-1.5-9B | 192 | 0.7139 | 0.6434 | 0.9012 | 23.7210 | 8.8759 | 0.7772 |
| Mistral-7B-v0.3 | 256 | 0.2200 | 0.0401 | 0.1820 | 1.8655 | 1.0994 | 0.4941 |
| Gemma-2-9B | 336 | 0.2299 | 0.0404 | 0.1757 | 1.5213 | 1.2344 | 0.5305 |
| **Pythia-1.4B** | 384 | 0.2439 | 0.0289 | 0.1183 | 1.2955 | 1.2157 | 0.5301 |

关键观察：
- **Qwen2.5-14B** (384 KV heads): t1/t5 = 0.57, 与 Qwen-7B 的 0.57 几乎一致，但 top5 concentration 从 0.61 降到 0.33（heads 数量增加稀释了集中度）
- **Pythia-1.4B** (384 heads, MHA): t1/t5 = 0.12, 是所有模型中最低的——delta 分布最均匀，没有显著 outlier head（top1 delta 仅 1.02，且 top3 紧密相邻 1.02/0.78/0.76）
- 三档 shape 清晰：spike-dominated (Yi, Qwen) → moderate (Llama, Qwen-14B) → diffuse (Mistral, Gemma, Pythia)

结果已保存到 `/root/ratekv/shape_metrics.json`。

---
