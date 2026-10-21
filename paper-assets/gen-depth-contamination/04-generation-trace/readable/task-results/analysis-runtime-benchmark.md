# analysis runtime benchmark

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_runtime-benchmark_20260523T130755_result.json`
- **Structured JSON:** [`429fe9d644048fc492a7.json`](../../sessions/42/429fe9d644048fc492a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Benchmark 完成。结果：

| Stage | Mean (ms/doc) | 占比 |
|-------|--------------|------|
| Scorer log-prob (GPU) | 20.6 ± 1.9 | 46.1% |
| CPU 特征提取 | 23.4 ± 6.1 | 52.3% |
| LightGBM 推理 | 0.74 ± 0.10 | 1.6% |
| **Total** | **44.7 ± 7.7** | |

**Throughput: 22.4 docs/sec**（单文档无 batch，RTX PRO 6000 Blackwell）。

结果已保存到服务器 `results/runtime_benchmark/` 和本地 artifact `runtime_benchmark_results.md`。

---
