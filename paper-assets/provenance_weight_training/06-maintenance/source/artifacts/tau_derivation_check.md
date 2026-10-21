# τ 推导审计报告

## 论文验证结果

**arXiv 2602.16065** (Wang, Niu, Li 2026) — "Can Generative AI Survive Data Contamination?"

论文中**不存在 τ 参数**。核心参数是 α = m₁/(m₁+m₂)（真实数据比例），作为**已知设计参数**进入收敛定理：

$$d(\hat{P}_t, P_0) \lesssim t^{-\min(p, \alpha)}$$

其中 p 为基线收敛率。论文无 α_eff、importance weighting、adaptive threshold 等概念。

## τ 与 contamination ratio 的关系

| 层面 | 关系 |
|------|------|
| Wang 的理论 | α 是已知输入，收敛 bound 前提是 α 已知 |
| 我们的代码 | `τ = 1.0 - contamination_ratio * 0.5`（pretrain_weighted.py:288），**直接依赖已知比例** |
| 我们的框架 | τ 是 α_eff(b) 的下界阈值：b* = inf{b ≥ 0 : α_eff(b) ≥ τ, ESS ≥ n_min} |

## D025 判断评估

**D025 核心论点**："τ 的理论来源依赖已知比例 → 只能当 empirical HP"

**判断基本正确，但需要细化**：

1. **正确部分**：Wang 的 α 确实是已知参数；代码中 τ 的默认值公式直接使用 contamination_ratio；无法从 Wang 的理论中推导出不依赖比例的 τ 值。

2. **需要修正的部分**：Wang 的论文**根本不定义 τ**。τ 是我们自己的构造，受 α 启发但并非从 α 推导而来。准确表述应为：
   - Wang 的理论提供了**动机**（α 越大收敛越好 → 需要质量阈值保证有效 α 足够大）
   - 但不提供**处方**（具体 τ 取多少）
   - τ 的具体值需要 empirical justification（τ sweep 初步数据：τ=0.6 PPL=17.681, τ=0.8 PPL=17.650，差异仅 0.031；τ=0.5/0.7/0.9/0.95 尚在运行中，待完成后更新完整趋势）

3. **Drayson et al. (EMNLP 2025, 2502.15654) 对照**：使用相同公式 w=(1-q)^b，b 通过验证集 grid search 选取，无任何理论推导。明确声明不假设已知比例。

## 对论文 framing 的影响

D025 采用的方案 A（τ 为 empirical HP with theoretical motivation）是**正确的定位**。建议：

- **保持 D025 结论不变**：τ 是 empirical HP，Wang 理论仅提供 motivation
- **修正叙述精度**：不要说"τ 来源于 2602.16065"，而是"收敛理论 motivates 需要质量阈值，τ 是该阈值的实践实例化"
- **τ sweep 是关键证据（基于部分数据的初步分析，待 τ sweep 完成后更新）**：目前仅 τ=0.6 和 τ=0.8 两个完成数据点（PPL 差 0.031），τ=0.5/0.7/0.9/0.95 四组在跑。若最终确认 PPL 在 [0.5, 0.95] 平坦，则 τ 对精确值不敏感 = 无需已知比例来设定 τ，**强化** Claim 3
- **代码层面**：τ 的默认值公式应改为不依赖 contamination_ratio（如固定 τ=0.8），消除与 Claim 3 的矛盾
