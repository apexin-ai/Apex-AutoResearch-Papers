# analysis inference efficiency collect

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_inference-efficiency-collect_20260517T112031_result.json`
- **Structured JSON:** [`ac5c5be559f0e72761dc.json`](../../sessions/ac/ac5c5be559f0e72761dc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Benchmark 完成，结果已保存到 `artifacts/efficiency_benchmark.json`。

关键数据（medium input ~475 tokens, batch=1）：

| Metric | CLS (1 token) | TRAJ (~200 tokens) | Ratio |
|--------|--------------|-------------------|-------|
| 单次延迟 | 46.9 ms | 2631.5 ms | 56.1x |
| Func-level (2.3 tests/inst) | 107.9 ms | 2631.5 ms | **CLS 快 24.4x** |
| Repo-level (12.3 tests/inst) | 576.9 ms | 2631.5 ms | **CLS 快 4.6x** |

上一个 Worker 的脚本比任务里给的版本更全面：包含了 short/medium/long 三种输入长度，以及 batch=8/16/32 的吞吐量测试。CLS batch 吞吐约 29-30 samples/sec，TRAJ batch 仅 2.2-4.4 samples/sec。

---
