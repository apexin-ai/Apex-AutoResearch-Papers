# research asv parameterization

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_asv-parameterization_20260520T121136_result.json`
- **Structured JSON:** [`02f0a4c710e95d89b5f2.json`](../../sessions/02/02f0a4c710e95d89b5f2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存。以下是三方案对比表。

---

## C(δ) 参数化候选方案对比

| 维度 | **A: 线性插值** | **B: 矩阵幂 (CTMC)** | **C: 范数球极值** |
|------|----------------|----------------------|------------------|
| **公式** | C(δ) = (1−δ)I + δC₀ | C(δ) = exp(δ·log C₀) | ASV = inf{δ: sup_{C∈S(δ)} \|bias\| ≥ \|θ̂₀\|} |
| **δ 含义** | 误差率放大倍数 | 误差复合轮次 | 最大单类误差率 |
| **δ=0** | C = I ✓ | C = I ✓ | S={I} ✓ |
| **δ=1** | C = C₀ | C = C₀ | max error rate = 100% |
| **δ 范围** | [0, min_k 1/(1−C₀_{kk})] | [0, ∞) | [0, 1) |
| **δ>1 外推** | 支持，有限 | 无限 | 不需要 |
| **单调性** | 易证（线性） | CTMC 保证 | 平凡（集合包含） |
| **锐度** | 紧（任意 δ 可达） | 弱（约束在 CTMC 路径） | 最紧（worst-case） |
| **需要 C₀** | 是 | 是（且要求 embeddable） | 否（reference-free） |
| **计算** | closed-form | 矩阵对数（数值） | 优化问题 |
| **K=2 退化** | Se/Sp 线性缩放 = VanderWeele & Li | Se/Sp 指数衰减 | 经典 bias analysis |
| **E-value 类比** | ★★★ 最直接 | ★★ 间接 | ★★★ 精神最一致 |
| **可解释性** | ★★★ "LLM 误差是 validation 的 δ 倍" | ★★ "误差复合了 δ 轮" | ★☆ "最大误差率为 δ" |

**推荐**：**方案 A 为主**（简洁、可解释、closed-form、直接类比 E-value），方案 C 可作 appendix 的 robustness 补充。方案 B 理论优雅但实用性不足。

关键文献锚点：
- 方案 A 在 K=2 时精确退化为 VanderWeele & Li (2019) 的 Se/Sp ratio 框架
- E-value 的成功 = 单标量 + 可解释 + 单调 + 可证 sharpness → 方案 A 完全满足
- Brenner (1993) 证实 K>2 时偏差方向不可预测 → 佐证 ASV 的必要性

---
