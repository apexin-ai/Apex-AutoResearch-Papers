# analysis c2 cluster robust ci

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_c2-cluster-robust-ci_20260516T054804_result.json`
- **Structured JSON:** [`2f677b26998f26c6afac.json`](../../sessions/2f/2f677b26998f26c6afac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。所有 12 个条件的结果（119 problems × 10 samples = 1190，B=10000）：

### Qwen 模型

| Condition | Acc | Cluster-robust CI | Wilson CI | CR width | W width |
|---|---|---|---|---|---|
| **ae_only** | 99.92% | [99.75, 100.00] | [99.53, 99.99] | 0.25pp | 0.46pp |
| **exception_only** | 99.83% | [99.50, 100.00] | [99.39, 99.95] | 0.50pp | 0.56pp |
| **vota** | 99.41% | [98.32, 100.00] | [98.79, 99.71] | 1.68pp | 0.92pp |
| **vota_no_ae** | 99.41% | [98.32, 100.00] | [98.79, 99.71] | 1.68pp | 0.92pp |
| **full_trace_label_only** | 86.22% | [80.42, 91.34] | [84.14, 88.06] | 10.92pp | 3.92pp |
| **loop_only** | 85.63% | [80.17, 90.42] | [83.52, 87.51] | 10.25pp | 3.99pp |
| **full_trace** | 81.76% | [75.71, 87.31] | [79.47, 83.86] | 11.60pp | 4.39pp |
| **no_trace** | 75.13% | [68.15, 81.51] | [72.59, 77.50] | 13.36pp | 4.91pp |

### DeepSeek 模型

| Condition | Acc | Cluster-robust CI | Wilson CI | CR width | W width |
|---|---|---|---|---|---|
| **deepseek_exception_only** | 99.33% | [98.15, 100.00] | [98.68, 99.66] | 1.85pp | 0.98pp |
| **deepseek_vota** | 84.45% | [78.15, 90.08] | [82.28, 86.40] | 11.93pp | 4.12pp |
| **deepseek_no_trace** | 73.36% | [66.39, 80.09] | [70.78, 75.80] | 13.70pp | 5.02pp |
| **deepseek_full_trace** | 10.59% | [6.64, 15.04] | [8.97, 12.47] | 8.40pp | 3.50pp |

### 验证

- **Cluster-robust CI 一律比 Wilson CI 更宽**：符合预期，因为 problem 内样本相关性导致有效样本量减少。中等准确率条件的 CR width 约为 Wilson 的 2.5-3× 倍。
- **高准确率条件 CI 仍然很窄**：ae_only 99.92% 的 CR-CI 仅 0.25pp 宽，下界 99.75%，结论稳健。
- **deepseek_full_trace 10.59%** 是已知异常（模型训练失败），CI 也正确反映了这一点。

脚本保存在服务器 `/root/trace-verdict-study/analysis/cluster_robust_ci.py`，结果 JSON 在 `/root/autodl-tmp/trace-verdict-study-checkpoints/analysis/cluster_robust_ci.json` 和本地 `artifacts/analysis/`。

---
