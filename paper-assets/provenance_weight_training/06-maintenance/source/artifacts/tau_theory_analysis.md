# τ 理论推导分析：arXiv 2602.16065 中 α 是否依赖已知 contamination ratio

> 分析日期: 2026-05-15
> 论文: Wang, Niu & Li (2026). "Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training." arXiv:2602.16065

## 结论

**τ 的理论来源（收敛定理中的 α）直接依赖已知 contamination ratio。** α = m₁/(m₁+m₂) 是已知设计参数，不是从数据中估计的。但这对 Claim 3 的影响可控——τ 应定位为 empirical hyperparameter with theoretical motivation，而非 proportion-free 的理论推导结果。

---

## 1. 论文中 α 的定义与角色

Wang et al. (2602.16065) 研究 contaminated recursive training (CRT)：每一轮训练使用 m₁ 个真实样本 + m₂ 个前代模型生成的合成样本。核心参数：

$$\alpha := \frac{m_1}{m_1 + m_2} \in (0, 1)$$

α 是 **real-data fraction**——真实数据在混合训练集中的比例。

**关键性质：α 是已知的设计参数 (design parameter)**。论文将 α 视为实践者在每轮训练中主动设定的值（因为 m₁ 和 m₂ 都是训练者控制的）。论文中没有任何关于 α 未知或需要估计的讨论。

## 2. 收敛定理对 α 的依赖

**Theorem 3.4 (主定理)**：设 {ℙ̂ₜ} 为 CRT 序列，在 Assumptions A1 (多项式基准收敛率 p) 和 A2 (凸距离度量) 下：

```
d(ℙ̂ₜ, ℙ₀) ≲ t^{-min{p, α}}
```

其中 p 为未受污染模型的基准收敛率。

**α 的角色是 rate limiter**：收敛速率由 p 和 α 的最小值决定。当 α < p 时，real-data fraction 成为瓶颈；当 α > p 时，模型能力成为瓶颈。

**Theorem 4.3 (有偏设定 BCRT)**：扩展到采样偏差场景：

```
d(ℙ̂ₜ, ℙ₀) ≲ t^{-min{p, q, α}}
```

其中 q 为偏差衰减率。三个因子中的最小值决定收敛。

**结论：α 在定理中是一个需要已知确切值的参数，推导过程直接依赖 α 的具体数值。**

## 3. 对项目 τ 的影响分析

### 3.1 项目中 τ 与论文 α 的关系

项目的 dual-constrained adaptive b* 方法中，τ 是 α_eff(b) 的质量阈值：

```
b* = inf{b ≥ 0 : α_eff(b) ≥ τ}  s.t.  ESS(b) ≥ n_min
```

τ 的理论 motivation 来自 Wang et al. 的收敛定理：α 越高，收敛越快。因此设定 α_eff ≥ τ 确保加权后有效真实率达到足够高的水平。

### 3.2 依赖程度：直接依赖

这是**直接依赖**而非间接依赖：

- 收敛定理的 bound 中 α 直接出现在指数位置（t^{-α}）
- α 的定义 m₁/(m₁+m₂) 就是 contamination ratio 的互补量（contamination ratio = 1-α = m₂/(m₁+m₂)）
- 论文假设 α 是已知设计参数，没有提供 α 未知时的任何理论保证

### 3.3 对 Claim 3 的影响与 Framing

**Claim 3 核心仍然成立，但 τ 的叙事需要调整：**

| 方面 | 不能说 | 应该说 |
|------|--------|--------|
| τ 理论基础 | "τ 有 proportion-free 的理论推导" | "收敛理论解释了为什么需要质量阈值（α 越高收敛越快），τ 的具体值由经验确定" |
| τ 的定位 | "理论最优阈值" | "empirical hyperparameter with theoretical motivation" |
| 方法的 proportion-free 性质 | "τ 理论上不需要已知比例" | "b* 的推导不需要已知比例——ESS 和 α_eff 从 batch 统计量计算；τ 是一个不敏感的经验默认值" |

**合理的 framing**：

> 收敛理论 (Wang et al. 2026) 证明 contaminated recursive training 的收敛速率由 real-data fraction α 决定（Theorem 3.4: rate ≲ t^{-min{p,α}}）。这为设定质量阈值提供了理论 motivation——α_eff(b) ≥ τ 确保 reweighting 后数据的有效真实率足够支撑收敛。然而，收敛定理中的 α 是已知设计参数，不能直接推出特定 τ 值。τ 作为 empirical hyperparameter，其鲁棒性由 τ sweep 实验支撑：τ ∈ [0.6, 0.9] 均能正常工作，无需 per-dataset 调优。这类似于 learning rate warmup steps——有理论 motivation 但具体值凭经验确定。

## 4. τ 的理论基础总结

**第一段：收敛理论的核心结果。** Wang, Niu & Li (2026) 建立了 contaminated recursive training 的一般性收敛理论。在对数据分布无参数假设、生成模型为通用逼近器的框架下，他们证明混合训练仍然收敛，但收敛速率被 real-data fraction α = m₁/(m₁+m₂) 限制在 t^{-min{p,α}}。这是第一个不依赖高斯/离散分布假设的正面理论结果，为 contaminated training 的可行性提供了理论保证。

**第二段：α 作为已知参数的假设。** 定理的关键假设是 α 已知且由实践者控制。在论文的 recursive training 设定中这是自然的——每轮训练时 m₁ 和 m₂ 由实践者决定。但在 web-scale pretraining 的真实场景中，合成数据的比例本质不可知（来源混杂、标注缺失），α 退化为需要估计的量。论文本身不讨论 α 未知的情况，也不提供这一场景下的理论保证。

**第三段：从理论到实践的桥梁。** 项目中 τ 借用了"α 越高收敛越好"的定性洞察，但不依赖 α 的精确值。τ 的作用是为 adaptive b* 提供质量下界——"至少要 reweight 到这个清洁程度"。τ 的具体值（如 0.8）由经验设定，τ sweep 实验将证明方法在宽泛 τ 范围内鲁棒。方法运行时不访问 contamination ratio：b* 从每个 batch 的 q-score 统计量实时计算，ESS 和 α_eff 均为 batch-local 量。因此 Claim 3（方法无需已知污染比例）的核心论点不受影响——需要调整的仅是 τ 的叙事定位，从"理论推导"降级为"有理论 motivation 的经验超参数"。

---

## Sources

- [Wang, Niu & Li (2026). arXiv:2602.16065](https://arxiv.org/abs/2602.16065)
- [HTML full text](https://arxiv.org/html/2602.16065)
