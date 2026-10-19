# code plan004 asv scaffold

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan004-asv-scaffold_20260520T121229_result.json`
- **Structured JSON:** [`7595c4e7e4e9a527be6a.json`](../../sessions/75/7595c4e7e4e9a527be6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部通过。结果总结：

**三个 plim 函数均正常工作：**
- **Confounding** (closed-form): C=I 精确恢复真参数 ✓，C=C₀ 下 τ 偏差 +0.119
- **Mediation** (closed-form, 从 plan_001 移植): C=I 精确恢复 ✓，C=C₀ 下 τ 偏差 +0.174
- **Collider** (precomputed moments, 从 plan_001 移植): C=I 下 τ=0.887 (collider bias 使 τ 从 1.0 缩小)，C=C₀ 下额外 misclass 偏差 +0.063

**compute_asv 框架正常运行：** 三个 DAG 的 ASV 均为 None（对称高精度 C₀ + LinearInterpolation 下 τ 未翻转符号，符合预期——τ 在整个 δ 范围内保持正值）。

**待完成：**
1. C(δ) 参数化方案选定后替换 LinearInterpolation
2. mc_coverage_test / type_error_analysis 实现

---
