# ops latency benchmark p0

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_latency-benchmark-p0_20260516T140521_result.json`
- **Structured JSON:** [`93bc70ab34d45104ced0.json`](../../sessions/93/93bc70ab34d45104ced0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完整结果

| Method | Sparsity | tokens/s | ms/token | speedup vs dense |
|--------|----------|----------|----------|------------------|
| Dense | 0% | 17018.0 | 0.0588 | 1.000x |
| KL predictor-only | 30% | 16069.9 | 0.0622 | 0.944x |
| KL predictor-only | 50% | 16062.3 | 0.0623 | 0.944x |
| Predictor+compensation | 30% | 15681.4 | 0.0638 | 0.921x |
| Predictor+compensation | 50% | 15731.4 | 0.0636 | 0.924x |

**Breakdown:**
- Predictor overhead (32 layers): **3.16 ms** (2.6% of dense forward)
- Per-layer predictor: 0.099 ms
- Dense FFN per layer: 2.424 ± 0.035 ms
- Sparse FFN+predictor per layer: 2.686 ± 0.009 ms
- Compensation additional overhead: ~3.16 ms

**关键结论：**
- 当前实现用 element-wise mask（非结构化稀疏），所以 30% 和 50% latency 几乎相同——dense matmul 大小不变
- Predictor 开销仅 **5.9%**，compensation 再加 **2.6%**，合计 overhead < 8.5%
- 若利用结构化稀疏内核（如 Triton block-sparse），50% sparsity 理论可将 FFN 计算减半，净 speedup = 50% FFN 节省 - 5.9% predictor 开销 ≈ 显著正收益

脚本已保存在 `/root/distill_sparse_swiglu/src/latency_benchmark.py`。

---
