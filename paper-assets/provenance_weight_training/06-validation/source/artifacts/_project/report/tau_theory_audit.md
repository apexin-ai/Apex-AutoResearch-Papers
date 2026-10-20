# τ 理论来源审计：arXiv 2602.16065

## 论文信息

- **标题**: Can Generative Artificial Intelligence Survive Data Contamination? Theoretical Guarantees under Contaminated Recursive Training
- **作者**: Kevin Wang, Hongqian Niu, Didong Li (UNC Chapel Hill)
- **arXiv**: 2602.16065 (2026-02-17)

## 论文摘要

研究生成式 AI 在递归训练（训练数据混合真实数据和前代模型生成的合成数据）下的收敛性。在最小假设框架下证明：即使训练数据被合成数据污染，递归训练仍然收敛，收敛速率等于基线模型收敛速率与真实数据比例的最小值。

## 核心收敛 Bound

**Theorem 3.4**:

$$d(\widehat{\mathbb{P}}_t, \mathbb{P}_0) \lesssim t^{-\min\{p, \alpha\}}$$

三种 regime：
- p > α: 速率为 t^{-α}（受数据比例限制）
- p = α: 速率为 t^{-α} log t
- p < α: 速率为 t^{-p}（受模型能力限制）

## α 的定义

**α 是真实数据比例（fraction of real data），不是分布的固有属性。**

$$\alpha := \frac{m_1}{m_1 + m_2} \in (0,1)$$

其中：
- m₁ = 每轮新采样的真实数据量
- m₂ = 每轮新采样的合成数据量

α 是实验者主动设定的设计参数（design choice），不是需要从数据中估计的未知量。

## 是否依赖已知污染比例

**YES — α 的定义本身就是已知的污染比例。**

论文框架假设实验者控制每轮的真实/合成数据混合比，因此 α 是已知的。这与"不需要知道污染比例"的 claim 直接矛盾。

## 对 Claim 3 的影响

**Claim 3 ("works without known contamination proportion") 无法从该论文获得完整理论支撑。**

具体影响：
1. 论文中的 α 不能直接作为我们 τ 的 principled 来源——它们语义不同。α 是已知的数据混合比例，τ 是质量阈值
2. 收敛 bound 的推导前提就是 α 已知，因此不能用该 bound 来论证"无需知道污染比例"
3. 如果我们的 τ 声称源自该论文的 α，逻辑链断裂：论文要求知道比例 → 我们声称不需要知道比例

## 建议的论文表述

### 方案 A：降级 τ 的叙述（推荐）

将 τ 定位为 **empirical hyperparameter with theoretical motivation**，而非 theoretically principled threshold：

> "Our threshold τ is motivated by the convergence analysis of Wang et al. (2026), who show that recursive training converges at rate t^{−min{p,α}} where α is the real-data fraction. While their α assumes known contamination proportions, our τ serves as an analogous quality gate that can be set empirically without explicit knowledge of contamination ratios — trading theoretical guarantees for practical applicability."

### 方案 B：修正 Claim 3

加 caveat，明确理论 bound 的前提：

> "The theoretical convergence guarantee (Theorem X) holds when the contamination proportion is known. In practice, we show that setting τ via cross-validation on a small clean holdout set achieves comparable performance without requiring explicit knowledge of the contamination ratio (Section Y, Table Z)."

### 方案 C：寻找替代理论支撑

搜索是否有其他工作提供 contamination-proportion-free 的收敛 bound，作为 τ 的替代理论来源。候选方向：
- Robust statistics 中的 breakdown point 理论（不需要已知污染比例）
- Influence function 方法
- DRO (distributionally robust optimization) 框架
