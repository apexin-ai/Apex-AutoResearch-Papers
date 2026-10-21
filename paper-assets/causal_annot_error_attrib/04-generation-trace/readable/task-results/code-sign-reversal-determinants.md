# code sign reversal determinants

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sign_reversal_determinants_20260523T145155_result.json`
- **Structured JSON:** [`0f4ef66bccae2f8b6f80.json`](../../sessions/0f/0f4ef66bccae2f8b6f80.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

脚本运行完成，结果已写入 JSON。

**关键发现**：

- **23 个矩阵**，default beta `[0, 1.0, -0.5, ...]` 下 **14/23 发生 sign reversal**（61%）
- **最佳单特征规则**：`det < 0.0137` — 准确率 91.3%，specificity 100%（无假阳），sensitivity 85.7%
- **最佳双特征规则**：`(min_diag < 0.5523) AND (mean_entropy > 0.3986)` — 准确率 95.7%，sensitivity 100%（无遗漏），specificity 88.9%
- **跨 beta 鲁棒性**：det 规则在 scale_0p3 和 scale_3p0 上同样 91.3%，但在 uniform_pos（全正 beta）下完全失效（47.8%），因为 uniform_pos 下 0/23 矩阵产生 sign reversal
- `uniform_pos` 配置 0 个 sign flip，说明方向相同的 beta 不会被混淆矩阵翻转符号

---
