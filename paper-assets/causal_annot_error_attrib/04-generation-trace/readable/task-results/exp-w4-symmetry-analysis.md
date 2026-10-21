# exp w4 symmetry analysis

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_exp_w4_symmetry_analysis_20260523T190010_result.json`
- **Structured JSON:** [`87d050d82b388b0c09a0.json`](../../sessions/87/87d050d82b388b0c09a0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**Summary (25 matrices, dedup across 4 files):**

| 指标 | 值 |
|------|-----|
| d_rel min | 0.0147 |
| d_rel median | 0.1604 |
| d_rel mean | 0.1858 |
| d_rel max | 0.3809 |
| near-symmetric (d_rel < 5%) | 6/25 |
| near-symmetric (d_rel < 10%) | 9/25 |
| diag_mean range | [0.4533, 0.8086] |

**按 dataset 分层的规律很清晰：**

- **CivilComments (K=2):** 全部 7 个矩阵 d_rel ∈ [0.015, 0.065]，高度近似对称，Theorem 2 的 symmetric C₀ 假设成立
- **HumAID (K=10):** 8 个矩阵 d_rel ∈ [0.095, 0.170]，中等偏离，DeepSeek 系列更接近对称
- **VAST (K=3):** 全部 10 个矩阵 d_rel ∈ [0.295, 0.381]，显著不对称，Theorem 2 的对称假设不适用

结论：Theorem 2 (symmetric C₀) 对 K=2 二分类任务高度适用（6/7 < 5%），对多分类任务（尤其 VAST 三分类）偏离显著，需要 Theorem 1 的一般形式。

---
