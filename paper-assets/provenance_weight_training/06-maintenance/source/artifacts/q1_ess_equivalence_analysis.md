# Q1: α_eff(b) 是否等价于 ESS 阈值法？

## 结论

**不等价。** Reviewer 的论断基于对优化目标的误读。α_eff 方法求的是 min b（最小干预），而非 max α_eff（最大质量）。在实际训练中，约 40% 的 reweighted batches 中 α_eff 是 binding constraint，此时 b* 远小于 ESS 上界，产生实质不同的权重。

---

## 数学推导

### 核心公式

- **权重**: w_i = (1−q_i)^b
- **有效真实率**: α_eff(b) = Σ(1−q_i)^{b+1} / Σ(1−q_i)^b （w-加权的 (1−q_i) 均值）
- **有效样本量**: ESS(b) = (Σw_i)² / Σw_i²
- **优化目标**: b* = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b) ≥ n_min

### α_eff(b) 单调性证明

α_eff(b) 是 (1−q_i) 关于权重 w_i = (1−q_i)^b 的加权均值。设 x_i = 1−q_i ∈ [0,1]：

α_eff(b) = Σ x_i^{b+1} / Σ x_i^b = E_w[x]

其中权重分布 w_i ∝ x_i^b。随 b 增大，权重向大 x_i 倾斜，加权均值 E_w[x] 非递减。

形式化：令 f(b) = Σ x_i^{b+1} / Σ x_i^b，取导数（用 log-sum-exp 技巧）：

f'(b) = [Σ x_i^b · (Σ x_i^{b+1} ln x_i · Σ x_i^b − Σ x_i^{b+1} · Σ x_i^b ln x_i)] / (Σ x_i^b)²

化简得 f'(b) = Cov_w(x, ln x)，其中协方差在权重分布下计算。由于 x 和 ln x 同序（x > 0 时 ln 单调），Chebyshev 排序不等式保证 Cov_w(x, ln x) ≥ 0。

**结论: α_eff(b) 对 b 单调非递减。** ✓

### Reviewer 论断的错误

Reviewer 的推理链：
> α_eff(b) 单调非减 → 最优化 b* 总会推到 ESS 边界 → 等价于 ESS 阈值法

**错误在第二步。** 这隐含假设优化目标是 max_b α_eff(b) s.t. ESS(b) ≥ n_min。如果目标是最大化 α_eff，那确实总是推到 ESS 边界。

但实际优化目标是 **inf{b : α_eff(b) ≥ τ}**——最小的满足质量阈值的 b。这是一个 min-intervention 准则：

| 约束 | 作用方向 | 含义 |
|------|---------|------|
| α_eff(b) ≥ τ | b 的**下界** b ≥ b_τ | 至少要足够的 downweighting 以达到质量阈值 |
| ESS(b) ≥ n_min | b 的**上界** b ≤ b_ESS | 不能太激进以至于丧失有效样本 |

三种情形：

1. **α_eff(0) ≥ τ** → b* = 0（batch 已足够干净，无需干预）
2. **b_τ ≤ b_ESS** → b* = b_τ（**α_eff binding**，ESS 有余量）
3. **b_τ > b_ESS** → b* = b_ESS（**ESS binding**，α_eff 达不到 τ，取最优可行解）

情形 2 是关键区分：α_eff 方法选择 b_τ < b_ESS，比 ESS-only 方法更保守，保留更多有效样本。

### 何时 α_eff 约束更紧？

当 τ 适中且 batch 内 q-score 方差较大时：
- 高方差 → ESS 随 b 衰减慢（权重不均匀度本来就不大）→ b_ESS 大
- τ 适中 → b_τ 不需要很大就能达到 → b_τ < b_ESS

反之，当 τ 接近 1 或 q-score 高度集中时，α_eff 爬升慢，b_τ 大，更易碰到 ESS 边界。

---

## 实证数据

### 训练日志分析 (adaptive_fix_seed42)

- 配置: τ=0.8, n_min=2, batch_size=4
- 总 micro-batches: 51,913

| 类别 | 数量 | 占比 |
|------|------|------|
| Clean (b=0, α_eff(0) ≥ τ) | 25,922 | 49.9% |
| α_eff binding (α_eff ≈ τ=0.8) | 10,473 | 20.2% |
| ESS binding (α_eff < τ) | 15,580 | 30.0% |

**在需要 reweighting 的 batch 中**（n=25,991）：
- 40.1% α_eff 是 binding（α_eff 精确等于 0.8，ESS > n_min）
- 59.9% ESS 是 binding（α_eff < 0.8，ESS ≈ 2.0）

### Monte Carlo 对比 (2000 synthetic batches)

| 指标 | 值 |
|------|-----|
| α_eff binding 比例 | 38.6% |
| ESS binding 比例 | 61.4% |
| 两种方法完全一致 (\|Δb\|<0.01) | 33.5% |
| 两种方法近似一致 (\|Δb\|<0.1) | 62.0% |
| Mean \|Δb\| | 0.947 |
| Pearson r | 0.638 |
| Spearman ρ | 0.458 |

**当两种方法不同时** (n=760)：
- α_eff 方法 b*: mean=1.67
- ESS-only 方法 b*: mean=4.15
- **比值 A/B = 0.45** — α_eff 方法只用了 ESS-only 方法 45% 的 downweighting 强度
- α_eff 方法的 ESS: mean=2.60（vs n_min=2.0，有 30% 余量）

---

## 对论文 framing 的影响

### Reviewer 关切可以这样回应：

1. **单调性成立，但优化方向不是 max**。α_eff(b) 对 b 单调非减是正确的，但这恰恰是框架设计的一部分——它保证了 b_τ = inf{b : α_eff(b) ≥ τ} 的存在性和唯一性。

2. **核心差异是 min-intervention vs max-intervention**。ESS 阈值法（找最大 b 使 ESS ≥ n_min）是 max-intervention 准则——尽可能多地 downweight。α_eff 方法是 min-intervention 准则——只做恰好足够的 downweighting 以达到收敛保证所需的质量阈值。

3. **实证上两者产生不同的 b***。在 40% 的 reweighted batch 中，α_eff 约束是 binding 的，此时 b* 仅为 ESS 上界的 45%，保留了显著更多的有效样本。

4. **理论贡献不在于选择 b 的算法，而在于 τ 的理论基础**。α_eff ≥ τ 的阈值来自收敛界的推导（arXiv 2602.16065），给出了有理论保证的质量门槛。ESS 阈值法没有这个——n_min 是人工设定的 heuristic，没有理论指导应该设多大。

### 建议论文修改

- 在方法论部分强调 b* 的 inf（最小化）语义，而非 argmax 语义
- 加一个 figure：对同一批次画 α_eff(b) 和 ESS(b) 的双轴图，标注 b_τ 和 b_ESS 两个点，可视化两个约束的不同角色
- 在消融实验中加 ESS-only baseline 的对比，展示 min-intervention 比 max-intervention 更优的训练结果
