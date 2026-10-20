# Panel Granger Analysis 可行性评估

**日期**: 2026-05-15  
**项目**: distrib_canary_collapse / plan_002 Phase 2

## 当前数据

| α | Seeds | T (generations) |
|---|-------|-----------------|
| 0.00 | 1 (seed=42) | 11 (gen 0–10) |
| 0.25 | 1 (seed=42) | 11 |
| 0.50 | 1 (seed=42) | 11 |
| 0.75 | 1 (seed=42) | ~5 (进行中) |
| 1.00 | 4 (seed=42–45) | 11 |

---

## 1. Panel Granger (DH 2012) 最小样本要求

Dumitrescu-Hurlin (2012) 检验的统计量 $\bar{W}_{N,T}^{Hnc}$ 是 N 个 unit-specific Wald 统计量的均值，标准化后的 $\tilde{Z}_{N,T}^{Hnc}$ 在 T→∞（N 固定）下渐近正态。

**关键约束：**

- **每个 unit 的自由度**：lag=1 时，每个 unit 回归需估计 3 个参数（截距 + y_{t-1} + x_{t-1}）。T=11 经差分/滞后后有效观测约 9 个，自由度仅 6。个体 Wald 统计量的 F 分布近似在 df=6 时极不稳定。
- **DH Monte Carlo 结果**：他们的模拟显示 T=10, N=5 是 size 控制勉强合理的下限（实际 size 约 7–8% at nominal 5%），但 **power 极低**（约 15–25% 在中等效应下）。
- **N 对标准化的影响**：$\tilde{Z}$ 的标准化依赖 Wald 统计量的理论矩（前两阶矩），N=4–5 时均值的 CLT 近似很粗糙。

**结论：N=4–5, T=11 处于 DH 检验适用性的绝对下限，power 不足以支撑发表级结论。**

---

## 2. 单 Seed 的根本问题

这是比样本量更严重的问题。

### 2.1 不可交换性 (Non-exchangeability)

Panel 模型（无论 pooled 还是 heterogeneous）假设 cross-sectional units 来自某种可比较的总体。不同 α 值代表**本质不同的训练 regime**：

- α=0.0（纯合成数据）与 α=1.0（纯真实数据）的 training dynamics 在质上不同
- 不同 α 下的 canary metric 时间序列不是同一数据生成过程的独立实现
- DH 检验允许异质斜率，但其零假设（"所有 unit 均无 Granger 因果"）的拒绝只在 units 有某种可比性时才有意义

### 2.2 无法分离 α-effect 与 seed noise

α=0.00/0.25/0.50 各 1 seed 时：

- 观测到的时间序列 pattern 可能是 seed=42 的特殊性质，而非该 α regime 的固有特征
- 无 within-α 方差估计 → 无法构造任何关于 α-specific effect 的置信区间
- 一个 seed 的 Granger 检验本质上是 n=1 的 case study，不是统计推断

### 2.3 α=1.0 的 4 seeds 不对称性

将 (α, seed) 对作为 panel unit（N=8）的方案：

- α=1.0 贡献 4/8 = 50% 的 Wald 统计量，严重偏向单一 regime
- DH 检验的均值统计量会主要反映 α=1.0 的 Granger 关系
- 结论无法推广到 "across α regimes" 的一般性陈述
- 本质上是在做 α=1.0 的 multi-seed Granger 检验并掺入噪声

---

## 3. 替代方案评估

### 3.1 Fixed-Effects Panel Regression

$$y_{i,t} = \alpha_i + \beta \cdot x_{i,t-1} + \gamma \cdot y_{i,t-1} + \varepsilon_{i,t}$$

- N=5, T=11: 总观测 ~45，估计 5 个 fixed effects + 2–3 个斜率 = 7–8 参数
- 残差自由度 ~37–38，技术上可行
- **问题**：fixed effects 假设 α 之间只有截距不同、斜率相同。这个假设对不同 training regime 几乎必然不成立。加 interaction terms 则自由度不够。
- **评级：不推荐。假设太强，样本太小无法检验假设是否成立。**

### 3.2 Meta-Analytic Pooling（per-α Granger → pool p-values）

已有 per-α differenced permutation Granger 结果，可用 Fisher's method 合并：

$$-2\sum_{i=1}^{k} \ln(p_i) \sim \chi^2_{2k}$$

- **优点**：不要求 cross-sectional exchangeability；每个 α 独立检验，然后问"整体上有无 Granger 信号"
- **缺点**：各个 per-α 检验本身 power 极低（T=11, permutation test），合并弱信号仍然是弱信号
- **评级：方法论上最干净，但 power 不足以得出强结论。可作为 suggestive/preliminary evidence。**

### 3.3 Descriptive Cross-α Comparison（推荐的 preliminary 方案）

不做正式的 panel 检验，而是：

1. 报告每个 α 的 per-α Granger p-value 和 effect size（已有）
2. 绘制 effect size vs. α 的 trend plot（是否随 α 变化单调递增/递减）
3. 用 α=1.0 的 4 seeds 展示 within-α variability 作为 benchmark
4. 用 bootstrap CI 或 permutation distribution 可视化每个 α 下 Granger 统计量的不确定性

**优点**：不依赖 panel 假设，诚实展示数据现状  
**缺点**：不是正式的 panel 因果检验  
**评级：当前数据下最合理的选择。**

### 3.4 等 Multi-Seed Balanced Panel（推荐的正式方案）

| 设计 | N | T | DH Power (中等效应, lag=1) |
|------|---|---|--------------------------|
| 3 seeds × 5 α | 15 | 11 | ~50–60% |
| 4 seeds × 5 α | 20 | 11 | ~65–75% |
| 5 seeds × 5 α | 25 | 11 | ~75–85% |

- **最低要求：3 seeds × 5 α = N=15, T=11**
  - DH 检验的 size 控制在 N≥10 时明显改善
  - 可估计 within-α variance，separating regime effect from seed noise
  - Balanced design 避免单一 α 主导
- **推荐：4 seeds × 5 α = N=20**
  - Power 进入合理区间
  - 允许做 leave-one-seed-out robustness check

---

## 4. 结论

### 现在做 panel analysis 是否有学术价值？

**不成立作为正式统计结论。** 三个致命问题：

1. N=4–5, T=11 在 DH 检验的 power floor 之下
2. 单 seed/α 无法分离 regime effect 与 seed noise——这不是样本量问题，而是实验设计缺陷
3. Cross-sectional units (不同 α) 不满足 panel 模型的可比性假设

### 推荐方案

**现在（Phase 2 preliminary）：**
- 做 §3.3 的 descriptive cross-α comparison
- 用 Fisher's method pool 已有的 per-α Granger p-values 作为 supplementary evidence
- 论文中定位为 "preliminary evidence suggesting cross-regime pattern, pending multi-seed confirmation"
- 这些可以写进论文作为 motivation，但不能作为 main claim 的支撑

**等 D026 multi-seed 完成后（Phase 2 formal）：**
- 最低 3 seeds × 5 α (N=15, T=11)
- 推荐 4 seeds × 5 α (N=20, T=11)
- 使用 DH 检验 + fixed-effects 回归作为 robustness check
- 此时可作为论文 main result

### Multi-seed 优先级

如果计算资源有限，优先跑 α=0.00 和 α=0.50 的额外 seeds（极端值 + 中间值），因为：
- α=0.00 vs α=1.00 的对比是 main story（纯合成 vs 纯真实）
- α=0.50 是 mixing regime 的代表
- α=0.25/0.75 是 interpolation，优先级较低
