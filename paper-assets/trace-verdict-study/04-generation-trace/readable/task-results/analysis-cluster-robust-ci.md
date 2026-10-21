# analysis cluster robust ci

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cluster-robust-ci_20260516T060250_result.json`
- **Structured JSON:** [`65a37ecd924df86159f5.json`](../../sessions/65/65a37ecd924df86159f5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

24 个条件全部处理完成，结果已保存到 `/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/cluster_robust_ci.json`。

关键发现 — cluster-robust CI vs Wilson CI 对比（宽度差异）：

| 条件 | Sample Acc | Problem Acc | Cluster-robust 95% CI | Wilson 95% CI |
|------|-----------|-------------|----------------------|---------------|
| **ae_only** | 99.92% | 99.92% | [99.75, 100.0] | [99.53, 99.99] |
| **exception_only** | 99.83% | 99.83% | [99.50, 100.0] | [99.39, 99.95] |
| **vota** | 99.41% | 99.41% | [98.32, 100.0] | [98.79, 99.71] |
| **no_trace** | 75.13% | 75.13% | [68.15, 81.60] | [72.59, 77.50] |
| **full_trace** | 81.76% | 81.76% | [75.71, 87.40] | [79.47, 83.86] |
| **loop_only** | 85.63% | 85.63% | [80.08, 90.59] | [83.52, 87.51] |
| **deepseek_vota** | 84.45% | 84.45% | [78.40, 90.08] | [82.28, 86.40] |
| **deepseek_no_trace** | 73.36% | 73.36% | [66.22, 80.00] | [70.78, 75.80] |

符合预期：**cluster-robust CI 普遍比 Wilson CI 更宽**（因为同一 problem 下多个 solution 不独立）。每个 problem 有 10 个 solution（1190 样本 / 119 problems），聚类效应显著。高准确率条件（>99%）两种 CI 差异较小，中等准确率条件差异更明显（宽约 1.5-2x）。

---
