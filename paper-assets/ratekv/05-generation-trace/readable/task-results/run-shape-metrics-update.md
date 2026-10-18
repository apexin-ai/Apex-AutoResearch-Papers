# run shape metrics update

**When Does Non-Uniform KV Cache Quantization Help? Cardinality Constraints and a Heterogeneity Diagnostic** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_run_shape_metrics_update_20260515T142520_result.json`
- **Structured JSON:** [`8adfa6e4d6ef2f4a6431.json`](../../sessions/8a/8adfa6e4d6ef2f4a6431.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果汇总：

## 7 模型 Shape Metrics 完整表格

| Model | Heads | top5%conc | top1share | t1/t5 | t1/t2 | CV | Gini |
|-------|-------|-----------|-----------|-------|-------|----|------|
| Qwen2.5-7B | 112 | 0.6104 | 0.3461 | 0.5670 | 3.1741 | 3.8752 | 0.7065 |
| Qwen2.5-14B | 384 | 0.3312 | 0.1885 | 0.5693 | 7.7954 | 3.7370 | 0.5626 |
| **Llama-3.1-8B** | **256** | **0.5749** | **0.4867** | **0.8466** | **34.7909** | **7.7511** | **0.6695** |
| Yi-1.5-9B | 192 | 0.7139 | 0.6434 | 0.9012 | 23.7210 | 8.8759 | 0.7772 |
| Mistral-7B-v0.3 | 256 | 0.2200 | 0.0401 | 0.1820 | 1.8655 | 1.0994 | 0.4941 |
| Gemma-2-9B | 336 | 0.2299 | 0.0404 | 0.1757 | 1.5213 | 1.2344 | 0.5305 |
| Pythia-1.4B | 384 | 0.2439 | 0.0289 | 0.1183 | 1.2955 | 1.2157 | 0.5301 |

## Llama 确认

- **t1/t5 = 0.8466**（Director 估算 0.85，实际略低）
- **t1/t2 = 34.79** — 所有模型中最极端的 top1 vs top2 比值，说明 L2H5 独大
- top3 deltas: [15.26, 0.44, 0.33] — L2H5 的 delta 是第二名的 **35 倍**

## 其他 6 模型对比

全部与之前一致，无变化（conc 和 t1/t5 精确匹配）。

## Llama Top 5 Head Deltas

| Head | Delta |
|------|-------|
| L2H5 | 15.2636 |
| L3H1 | 0.4387 |
| L0H0 | 0.3263 |
| L3H2 | 0.2631 |
| L3H6 | 0.2585 |

Llama 是典型的 "single-head dominant" 分布：L2H5 一个 head 贡献了全部 delta 总和 (31.36) 的 48.7%。

---
