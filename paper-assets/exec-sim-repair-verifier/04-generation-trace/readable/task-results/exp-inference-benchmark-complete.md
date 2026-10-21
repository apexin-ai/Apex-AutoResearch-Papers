# exp inference benchmark complete

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_inference-benchmark-complete_20260516T100612_result.json`
- **Structured JSON:** [`930cf0fb9e7e32d9dffd.json`](../../sessions/93/930cf0fb9e7e32d9dffd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完整 benchmark 结果汇总：

## Inference Benchmark — RTX 5090 (32GB), 100 samples

| Level | Model | Avg (ms) | Median (ms) | P95 (ms) | Throughput (samples/min) | Avg Output Tokens |
|-------|-------|----------|-------------|----------|--------------------------|-------------------|
| **Func** | CLS | 40.6 | 42.9 | 55.5 | 1,478 | 1 |
| **Func** | CWM | 189.1 | 184.5 | 210.4 | 317 | 7.2 |
| **Func** | **Speedup** | | | | **4.7x** | |
| **Repo** | CLS | 70.3 | 48.1 | 116.8 | 853 | 1 |
| **Repo** | CWM | 15,307.7 | 16,299.9 | 16,704.0 | 3.9 | 477.1 |
| **Repo** | **Speedup** | | | | **217.8x** | |

关键发现：
- **Repo-level speedup 极其 dramatic (217.8x)**：CWM 平均生成 477.1 tokens，每样本 15.3 秒；CLS 只做 1 次 forward pass，70ms
- **Func-level speedup 温和 (4.7x)**：CWM 实际只生成 7.2 tokens（func-level 执行结果短），所以 generation 开销不大
- 这正好支持审稿人关注的 repo-level throughput 论点——输入越长、输出越多，CLS 的效率优势越明显

结果已保存至 `artifacts/inference_benchmark_results.json`。

---
