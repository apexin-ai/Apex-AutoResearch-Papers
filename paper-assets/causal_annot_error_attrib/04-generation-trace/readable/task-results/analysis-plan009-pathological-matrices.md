# analysis plan009 pathological matrices

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan009_pathological_matrices_20260520T185124_result.json`
- **Structured JSON:** [`8d2c912bee40d52c7268.json`](../../sessions/8d/8d2c912bee40d52c7268.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。报告已写入 `artifacts/plan009/plan009_analysis.md` 并注册。

核心结论：

**7 个拓扑分为 3 个风险层级：**
- **低风险** (mbias)：即使最病态的 C，bias < 0.04
- **中风险** (confounding/mediation/collider/frontdoor)：bias 有界（0.1–0.31），catastrophic fraction = 0%，矩阵特征可预测 bias（R² = 0.70–0.77）
- **高风险** (exposure/IV)：无论 C 质量如何都灾难性——exposure 的 |bias| ≈ τ（结构性识别失败），IV 的 Wald 估计器爆炸（near-perm ε=0.01 时 cat=61–73%，rank-deficient 时 bias 达百万级）

**关于 4 个假设：**
1. 病态 C 产生可预测的灾难性偏差 → **部分成立**，风险等级由拓扑决定而非 C 特征
2. 矩阵特征是强预测因子 → **拓扑依赖**，5/7 拓扑 R² > 0.6，exposure/IV 失败
3. 存在安全/灾难阈值 → **不成立**，分界由拓扑决定，不存在 C 特征上的阈值
4. 特征可作为诊断指标 → **部分成立**，condition_number 是最一致的预测因子（5/5 拓扑显著），但需要拓扑特定的诊断标准

---
