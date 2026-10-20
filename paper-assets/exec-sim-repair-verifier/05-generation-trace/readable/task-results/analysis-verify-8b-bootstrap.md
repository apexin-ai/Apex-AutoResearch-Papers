# analysis verify 8b bootstrap

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_verify-8b-bootstrap_20260512T191802_result.json`
- **Structured JSON:** [`63ba803f48b3fc4b6577.json`](../../sessions/63/63ba803f48b3fc4b6577.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 结论

### 1. Bootstrap 分析用了正确值

服务器 `8b_scaling_bootstrap_results.json` 明确记录 seed123 cls_acc = **89.37**（不是 89.52，不是 89.40）。所有 3 个 seed 的值与权威 eval 文件完全一致：

| seed | CLS 8B acc | CWM 8B acc | Gap |
|------|------------|------------|-----|
| 42 | 90.48 | 87.67 | 2.81 |
| 123 | **89.37** | 86.98 | 2.39 |
| 456 | 88.31 | 86.24 | 2.07 |

**无需修正。**

### 2. 正确的 8B 统计量（已验证与服务器一致）

| 指标 | 值 |
|------|------|
| Mean gap | 2.42pp |
| SD | 0.371pp |
| Paired t | 11.31 |
| p (one-sided) | 0.0039 |
| Cohen's d | 6.53 |
| Bootstrap 95% CI | [2.07, 2.81] |
| P(gap > 0) | 1.0000 |

### 3. 两个分析文件的差异说明

本地 `4b_8b_cls_cwm_paired_bootstrap_corrected.json` 中 8B mean gap = 2.26pp（而非 2.42pp），这不是错误——那是 per-instance clustered bootstrap（按 problem_id 聚类后池化），与 seed-level 简单平均方法不同。两者都用了正确的 89.37。

---
