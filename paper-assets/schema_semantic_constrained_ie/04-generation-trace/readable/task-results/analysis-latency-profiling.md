# analysis latency profiling

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_latency_profiling_20260516T085245_result.json`
- **Structured JSON:** [`5ddc66bc443abb89eaf4.json`](../../sessions/5d/5ddc66bc443abb89eaf4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Latency Profiling 结果

受控 benchmark（100 SciERC samples，同一模型/GPU/进程，CUDA sync 精确计时）：

| Mode | N | Mean (s) | P50 (s) | P95 (s) | P99 (s) | Overhead | tok/s |
|------|---|----------|---------|---------|---------|----------|-------|
| unconstrained | 100 | 2.594 | 2.359 | 5.985 | 8.194 | — | 57.7 |
| grammar_only | 100 | 2.637 | 2.397 | 6.099 | 8.346 | **+1.7%** | 56.7 |
| semantic_only | 100 | 2.625 | 2.379 | 6.080 | 8.335 | **+1.2%** | 57.0 |
| full_s1 | 100 | 2.655 | 2.416 | 6.162 | 8.449 | **+2.3%** | 56.4 |

所有差异均统计显著 (p < 0.0001, paired t-test)。

**论文可用结论**: Constrained decoding (grammar + semantic) adds only **2.3% latency overhead** (61ms/sample), which is statistically significant but practically negligible. 每个约束层单独贡献 ~1-2%，组合开销低于线性叠加。

---
