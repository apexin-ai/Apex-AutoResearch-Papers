# code plan007 correction framework

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan007-correction-framework_20260520T181451_result.json`
- **Structured JSON:** [`31e168e8cd16d7459f73.json`](../../sessions/31/31e168e8cd16d7459f73.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`plan_007_correction_guidance.py` 已完成全部验证，三阶段测试均通过：

**验证结果汇总：**
- `--help` — CLI 正常
- `--dry-run` — 单组合 × 10 sims 通过
- 多方法测试（5 methods × 2 topos × 2 C structures × 10 sims）— 全部 0% failure

**关键理论发现：** naive_plugin 和 MLA 对 T 系数（confounding/mediation/collider/mbias 拓扑）的 bias reduction 为 0%。这不是 bug，而是 Frisch-Waugh 定理的直接推论：C⁻¹ 对 dummy 矩阵的线性变换不改变 [intercept, D*] 的列空间，因此 T 系数的 OLS 估计不变。只有当 `tau_idx` 指向 dummy 系数时（exposure/iv/frontdoor），correction 才有效。这是论文的一个重要发现点。

**各方法表现概览（10-sim 预览）：**
| Method | Bias Reduction Range | 备注 |
|--------|---------------------|------|
| PPI++ | 95–99% | 最优，利用 gold labels 直接校正 |
| DSL (EM) | 60–72% | 中等，联合估计 β 和 C |
| MC-SIMEX | 30–91% | 波动大，依赖外推质量 |
| naive_plugin | 0% (T系数) / 负值 (dummy系数) | 列空间不变性；dummy 系数 overcorrect |
| MLA | 0% (T系数) / 变化 (dummy系数) | 同上；仅对称 C 无偏 |

全量运行（1000 sims × 7 topos × 6 C × 5 methods = 210,000 组合）等你审批后启动。

---
