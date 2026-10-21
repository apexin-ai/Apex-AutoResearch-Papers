# code runtime benchmark

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_runtime_benchmark_20260525T063042_result.json`
- **Structured JSON:** [`fd954361056b388d551d.json`](../../sessions/fd/fd954361056b388d551d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Benchmark 完成。结果摘要：

| 方法 | ms/doc (mean±std) | throughput | GPU 内存 |
|------|-------------------|-----------|---------|
| **OBD Pipeline** | 44.3 ± 7.8 | 22.6 docs/s | 3,102 MB |
| Binoculars | 17.0 ± 1.2 | 58.8 docs/s | 5,049 MB |
| DivEye | 14.2 ± 0.2 | 70.3 docs/s | 3,102 MB |
| Neural Probe | 14.6 ± 0.2 | 68.3 docs/s | 3,061 MB |

**OBD pipeline 分解：**
- Scorer forward (GPU): 20.1 ms (45%)
- CPU feature extraction: 23.4 ms (53%) — 瓶颈在 self-BLEU 计算
- LightGBM inference: 0.77 ms (2%)

OBD 比 baselines 慢约 2.6×，主要开销来自 CPU 端的 vocabulary diversity 特征计算（self-BLEU 需对 100 个 reference 文档逐一计算）。但 OBD 用更低的 GPU 内存（vs Binoculars 需双模型 5GB），且提供 15D 可解释特征和 depth ordering 能力，而非仅二分类检测。

结果已保存至 `results/runtime_benchmark/benchmark_results.json` 并注册为 artifact。

---
