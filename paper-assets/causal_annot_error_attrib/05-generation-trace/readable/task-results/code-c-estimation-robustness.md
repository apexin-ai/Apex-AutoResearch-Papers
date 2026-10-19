# code c estimation robustness

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_c_estimation_robustness_20260523T145144_result.json`
- **Structured JSON:** [`5cd829c9f276445b5795.json`](../../sessions/5c/5cd829c9f276445b5795.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行成功，结果已写入 JSON。

**结果摘要：**

| n_gold | Partition 稳定率 | Spearman ρ (mean) | Spearman ρ (median) |
|--------|-----------------|-------------------|---------------------|
| 50     | 50.4%           | 0.857             | 0.991               |
| 100    | 82.0%           | 0.993             | 1.000               |
| 200    | 85.6%           | 0.995             | 1.000               |
| 500    | 88.5%           | 0.996             | 1.000               |

所有 8 个源矩阵的 truth partition 都匹配 canonical fragile set {exposure, iv}。n_gold=50 时 partition 稳定率较低主要是 llama4 两个矩阵拖累（0%），但这两个矩阵在 n_gold=100 时跳至 99.5-100%。ASV 排名相关性（ρ）从 n_gold≥100 起即达 >0.99，说明有限 gold set 下 Ĉ 估计对 safe/fragile 划分是鲁棒的。

---
