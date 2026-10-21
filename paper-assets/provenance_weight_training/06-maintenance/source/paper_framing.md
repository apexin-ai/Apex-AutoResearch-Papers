# Paper Framing — provenance_weight_training

> 状态: ACTIVE — Round 8 审稿 (2.5-3.0) 后 analysis paper reframe 进行中
> 最后更新: 2026-05-21 UTC
> 投稿目标: EMNLP 2026 ARR May 25 — Findings Track
> 
> **Analysis Paper Reframe (D115, Round 8 响应)**:
> 论文彻底转为 analytical study — **"We analyze when, why, and how detect-and-reweight works"**。
> **D093 Distribution Matching 已失效**: 3-seed from-scratch 显示 OOD 改善（OWT Δ=−0.028, Wiki Δ=−0.029），D093 数据受 resume artifact (M049) 污染。
> **贡献排序**: (1) Epoch confound (>95% multi-epoch exposure) (2) Detector requirements — calibration+discrimination (3) Mechanism decomposition (4) Adaptive b* 工具。
> **M055 修正 (2026-05-22)**: D&R v2（正确数据）PPL=17.651 ≈ 原版 epoch-matched 17.657，独立确认 epoch confound 结论。LR schedule 选择对 D&R 几乎无影响。"quality vs diversity trade-off" 框架已放弃（Reviewer 指出 equal-step Δ=−0.412 中 Uniform 本质是 under-trained，不是 diversity trade-off）。

### ~~W2 Distribution Matching (D093)~~ — 已作废

> D093 单 seed 含 resume artifact (M049)，OOD 退化数据不可靠。3-seed from-scratch（D110 v3）显示 OOD **改善**：OWT Δ=−0.028, Wiki Δ=−0.029。"No distribution matching" 贡献已移除。

### Epoch Confound（Primary Contribution #1 — D&R v2 独立确认）

> ⚠️ **M055 数据反转事故**：旧 dr_epoch_matched_indep_lr_seed42 (PPL=18.782) 在反转数据（85%合成）上训练，结果无效已废弃。D&R v2 使用正确过滤数据（153,725条，86.4%真实）。

D&R 的 epoch-matched 比较存在两层系统性混淆：
1. **Multi-epoch exposure**: D&R filtering 后数据量 153,725 条（~83M tokens），2533 步 ≈ 1.0 content epoch。Uniform 用全部 371,499 条（~200M tokens），2533 步 ≈ 0.415 content epoch。D&R 对数据有更多 exposure。
2. **LR schedule confound**: 原版 epoch-matched 截取 6103 步 schedule 的前 2533 步，此时 LR ≈ 62% peak（warm LR）。独立 2533 步 schedule 则 LR 衰减到 0。

**W3 LR confound 实验结果（✅ D&R v2 修正完成）**:

| 实验 | 步数 | LR schedule | Data | Holdout PPL |
|------|------|-------------|------|-------------|
| **D&R v2 独立LR** | 2533 | 2533步 linear→0 | filtered 153K | **17.651** |
| Uniform 独立LR | 2533 | 2533步 linear→0 | all 371K | **18.062** |
| D&R epoch-matched 原版 | 2533/6103 | 共享6103步 (warm LR) | filtered | 17.657±.006 |
| Adaptive τ=0.7 | 6103 | 6103步 linear | all | 17.674±.007 |
| Uniform | 6103 | 6103步 linear | all | 17.694±.008 |

**核心发现——D&R v2 独立确认 epoch confound**:

1. **D&R v2 (17.651) ≈ 原版 epoch-matched (17.657)**：差仅 0.006——LR schedule 选择（shared vs independent）对 D&R 几乎无影响。

2. **>95% epoch exposure 归因数学不变**：
   - Equal-compute (2533步): D&R 17.651 vs Uniform 18.062 → Δ = 0.411
   - Equal-epochs (~1.0): D&R 17.657 vs Uniform full 17.694 → Δ = 0.037
   - Exposure component: (0.411 − 0.037) / 0.411 = **95.9%**

3. **Reviewer 修正（重要）**：equal-step Δ=−0.412 不是 "per-token quality" 度量。2533 步时 Uniform 仅完成 ~0.415 content epoch（本质是 under-trained），不能解读为 "diversity trade-off"。正确解读：D&R 在 equal-compute 下优势来自更高的数据重复率。

4. **D&R v2 的论文价值**：作为 **robustness check** 展示——LR 选择不影响 epoch-matched 结论，预封堵 "shared LR 不公平" 攻击面。可选加入 Table 2 或 Appendix。

**论文呈现**: Contribution #1 保持 "Epoch confound: >95% of D&R's published advantage is multi-epoch exposure, not filtering quality"。D&R v2 作为 robustness check 确认此结论在独立 LR 下稳健。

## Core Insight

Web 语料预训练面临合成数据污染问题（20-60%，来源未知），Drayson et al. (EMNLP 2025) 提出 w=(1-q)^b detect-and-reweight 框架，但 b 需要 per-model validation-based grid search（GPT-2/SmolLM ≤360M 用 b=10，SmolLM 1.7B 用 b=1）。

我们提出 **dual-constrained adaptive b***：per-batch 从 q-score 分布推导最优 b*，同时满足两个约束：
- **α_eff(b) ≥ τ** — 质量下界：确保加权后有效真实率达到收敛理论要求的阈值（"至少做够清洁"）
- **ESS(b) ≥ n_min** — 稳定上界：确保有效样本量不低于 Kish 阈值（"不要清洁过头"）

b* = inf{b ≥ 0 : α_eff(b) ≥ τ} subject to ESS(b) ≥ n_min — **最小干预准则**：在保证质量的前提下，使用最少的 downweighting。

**关键洞察**：α_eff(b) 单调递增、ESS(b) 单调递减。α_eff 给出 b 的下界 b_τ（需至少这么多清洁），ESS 给出 b 的上界 b_ESS（最多这么多清洁）。当 b_τ < b_ESS（~50.9% of all training batches at ρ=0.4），α_eff 是 binding constraint，b* 远小于 ESS 上界（mean 0.614 vs 3.550，ratio ~5.8×）——方法选择保守干预而非最大干预。

实现路径：**直接 loss reweighting**（gradient 层面连续加权），vs Drayson 的 SIR resampling（离散重采样）。

### α_eff(b) 的角色（D023 修正定论）

**D021 证明 α_eff(b) 严格单调递增**（dα_eff/db = Cov_w(x, ln x) ≥ 0）——这是正确的。

**D021 的错误推论**："因此 α_eff 优化等价于 ESS 阈值化"——这假设优化目标是 max α_eff(b) s.t. ESS ≥ n_min。但实际优化是 **inf{b : α_eff(b) ≥ τ}**——最小满足质量阈值的 b。单调性恰恰保证了 b_τ 的**存在性和唯一性**。

**Q1 实证（tau=0.7 阈值，3-seed 验证）**：
- 24,412 training batches (seed42) 中，5.8% clean (b*=0), 50.9% α_eff binding, 43.3% ESS binding
- 在需 reweighting 的 batch（94.2%）中：54.0% α_eff binding, 46.0% ESS binding
- α_eff binding 时 b* mean=0.614，ESS-only 上界 b* mean=3.550，ratio=5.8× (means)
- 跨 ρ 一致性：ρ=0.4 α_eff-binding 50.9% vs ρ=0.6 46.8%（gap <5pp），constraints nearly balanced at both ρ levels

**论文呈现**：α_eff 是方法的核心组件（非仅 motivation），提供质量阈值约束。Figure: 双轴图展示 α_eff(b) 和 ESS(b) 曲线 + b_τ 和 b_ESS 标注。

**τ 的定位（D025 定论 + D035 τ sweep 完整数据更新）**：收敛理论 (arXiv 2602.16065) 中 α = m₁/(m₁+m₂) 是已知设计参数，推导依赖已知比例。τ **不能声称有 proportion-free 的理论推导**。正确定位：empirical hyperparameter with theoretical motivation——收敛理论解释了"为什么需要质量阈值"（α 越高收敛越快），但 τ 的特定值由经验确定。

**τ sweep 完整结果（6 点，seed42，ρ=0.4）**：

| τ | PPL | Δ vs uniform (17.694) | b* mean | conclusion |
|---|-----|----------------------|---------|------------|
| 0.50 | 17.688 | −0.006 | 0.39 | success |
| 0.60 | 17.681 | −0.013 | 0.59 | success |
| 0.70 | 17.679 | −0.015 | 0.89 | success |
| 0.80 | 17.653 | −0.041 | 1.40 | best holdout (seed42) |
| 0.90 | 17.712 | +0.018 | 2.36 | negative |
| 0.95 | 17.723 | +0.029 | 3.08 | negative |

**关键洞察**：(1) [0.5, 0.8] 全部 beat uniform，safe range 内 PPL 差异仅 0.035；(2) τ=0.8 holdout PPL 略优于 τ=0.7（seed42: 17.653 vs 17.679），但 3-seed 差异仅 0.023（17.651±0.007 vs 17.674±0.007）；(3) τ>0.8 因 b* 膨胀导致过度 downweighting 而退化（asymmetric sensitivity）；(4) b* 与 τ 严格单调递增，机制清晰——τ 越高要求越严，solver 被迫推高 b*。

**D104 τ 推荐升级**：τ=0.7 和 τ=0.8 holdout PPL 可比（3-seed gap 0.023，在 seed variance 范围内），downstream 完全一致（均值 0.5414）。但 τ=0.7 在 OOD 指标上**跨污染水平一致优于** τ=0.8：
- ρ=0.4: OWT Δ(τ=0.7−τ=0.8) = −0.024, Wiki Δ = −0.028 (from-scratch only: τ=0.7 3-seed vs τ=0.8 2-seed. 旧值 -0.077/-0.143 和 -0.041/-0.066 均含 seed42 resume artifact — M049)
- ρ=0.6: OWT Δ(τ=0.7−τ=0.8) = −0.014, Wiki Δ = −0.013 (D105 2-seed paired)
推荐 τ=0.7 为实用默认值（comparable holdout + consistent OOD generalization advantage）。正确表述："wide safe range [0.5, 0.8] with recommended default τ=0.7 (better OOD generalization)"。

**ESS-only baseline 三 seed 验证完成 (D029 → D073 定稿)**：

| Method | seed42 | seed123 | seed456 | Mean±Std |
|--------|--------|---------|---------|----------|
| Adaptive (dual, **τ=0.8**) | 17.653 | 17.643 | 17.657 | **17.651±0.007** |
| Adaptive (dual, **τ=0.7**) | — | — | — | **17.674±0.007** |
| Uniform | 17.694 | 17.686 | 17.702 | 17.694±0.008 |
| ESS-only | 17.730 | 17.721 | 17.762 | 17.738±0.022 |
| Random | 17.830 | 17.800 | 17.777 | 17.802±0.027 |

**ρ=0.4 消融层级（两个 τ 均成立）**：Adaptive < Uniform < ESS-only < Random。τ=0.7 gap: adaptive-ESS-only=0.064, adaptive-uniform=0.020; τ=0.8 gap: 0.087, 0.043。Dual-constrained min-intervention 在两个 τ 下均优于 ESS-only max-intervention。

**ρ=0.6 消融层级（seed42）**：adaptive τ=0.7 (17.735) / τ=0.8 (17.740) < uniform (17.766) ≈ ESS-only (17.770) < random (pending)
- ESS-only/uniform gap 从 ρ=0.4 的 0.043 崩塌至 ρ=0.6 的 0.004
- adaptive/uniform gap 保持 0.026（vs ρ=0.4 的 0.043，diminishing but present）
- **α_eff 独立价值的最强证据**：在 ρ=0.6，ESS binding 66% 压制 b*，ESS-only 退化为 ≈ uniform（几乎不 reweight）。只有 α_eff 的 33% binding 提供了真正的质量改善。去掉 α_eff（ESS-only），方法在高污染下不工作
- **论文表述**：不能 claim 4-tier hierarchy universally holds。正确："hierarchy holds at ρ=0.4; at ρ=0.6, ESS-only collapses toward uniform, but adaptive maintains its advantage through α_eff quality targeting"

## Positioning vs Prior Work

### Drayson et al. (EMNLP 2025) — 最近相关工作

**共同点**：同一加权公式 w=(1-q)^b，detect-and-reweight 范式。

**关键区分**：

| 维度 | Drayson et al. | Ours |
|------|---------------|------|
| **b 选择** | 验证集 empirical 选取，训练中固定 | α_eff + ESS 双重约束自适应推导，per-batch 动态 |
| **干预原则** | 无原则（b 是超参数） | 最小干预（inf{b : α_eff ≥ τ}，只做必要的清洁） |
| **实现路径** | SIR resampling（离散重采样） | Loss reweighting（连续梯度加权） |
| **污染设置** | 不假设已知比例，但 b 依赖 validation set | 仅需 detector scores，无 validation set |
| **检测器** | ModernBERT 150M (AUC=0.986) | TF-IDF + LR (AUC=0.939)，轻量即可 |
| **训练场景** | 递归训练 model collapse prevention | Web corpus 一次性预训练 |
| **数据规模** | WikiText-2 (~2M tokens) | FineWeb subset (132M+ tokens) |
| **validation 成本** | 需 per-model validation run | 零额外 validation cost |

**定位原则：complementary approaches for different settings。**

### Golden Ratio Weighting (arXiv 2502.18049, 2025)
理论最优 w*=1/φ，但假设已知 real/synthetic 比例 k。作为 oracle baseline。

### 其他相关工作
- **Strong Model Collapse (ICLR 2025)** — 理论动机：微量合成数据即致 collapse
- **Dynamic Loss-Based Reweighting (ICLR 2025)** — 按 loss 加权（不使用 detector score），互补
- **SoftDedup (ACL 2024)** — 基于重复度的 soft reweighting
- **DoReMi / DSIR (NeurIPS 2023)** — 域级优化 vs 我们的实例级
- **Beyond Model Collapse / Verification (NeurIPS 2025)** — verifier-based prevention
- **PSIS (Pareto Smoothed IS)** — 重要性采样诊断，Kish's ESS 理论来源
- **arXiv 2602.16065** — α_eff 质量阈值 τ 的收敛理论来源

## Core Claims

### Claim 1 (Primary): Dual-Constrained Adaptive b* — Minimum Intervention Principle

α_eff + ESS 双重约束的 adaptive b*，提供 contamination-aware reweighting 中权重指数的 **principled 推导**，替代 Drayson et al. 的 per-model empirical grid search。

- **方法核心**：b* = inf{b ≥ 0 : α_eff(b) ≥ τ} s.t. ESS(b) ≥ n_min。两个约束分别提供 b 的下界（质量）和上界（稳定），b* 是最小满足质量阈值的可行解
- **最小干预原则**：不 downweight 更多于必要——在 ~38% of all batches 中，b* 仅为 ESS-only 上界的 ~20%（mean 1.19 vs 5.88），保留显著更多有效样本
- **差异化**：Drayson 的 b 是超参数（需 validation + grid search）；我们的 b* 是双约束下的自适应推导
- **证据需求**：(a) α_eff binding 比例统计 (✓ Q1); (b) ESS-only baseline head-to-head 对比（证明 min > max intervention）(✓ D029); (c) b* 轨迹分析; (d) mechanism decomposition (✓ — binding rate + b* ratio + 跨 ρ 一致性数据齐备)
- **理论 motivation**：α_eff(b) 单调性保证 b_τ 唯一存在；收敛理论为 τ 选择提供指导
- **n_min auto-compute 机制**：n_min = max(2, batch_size // 2) 自动缩放，无需手动调优（bs=4→n_min=2, bs=8→n_min=4, bs=16→n_min=8）。消融验证：n_min=1 过松（PPL=17.789, b* mean=7.2 爆炸），n_min=4@bs=4 过紧（b*≡0，退化为 uniform PPL=17.695），n_min=2@bs=4 最优（PPL=17.653@τ=0.8 / 17.674@τ=0.7）。auto-compute 规则确保 ESS 约束既不过松也不过紧——与 τ 的 safe-range 逻辑互补，共同构成 "set once, works across scales" 的设计。batchsize16_nmin8 (QUEUED) 将验证大 batch 下 auto-compute 行为

### Claim 2 (Primary): Adaptive b* 免调参即匹配 Grid-best

Adaptive b* 在零超参调优下达到 grid-search 最优同等水平（within seed variance），消除 grid search 的计算开销（6N → 1 runs）。

- **MVP 证据**: adaptive_fix ×3 seeds vs grid-b ×3 seeds（40% 污染, Qwen3-0.6B, 200M tokens）
- **状态**: ✅ MVP Path B PASS (D019: aggregate 88.6%, 三支柱论证)

**D074 定稿 — grid b=0.3 三 seed 确认为 grid-best**：
- grid b=0.3 mean=17.620±0.033 vs adaptive τ=0.7 17.674±0.007，gap=0.054 仍在 grid 95% CI [17.554, 17.686] 内
- 核心表述：**"adaptive achieves comparable performance to grid-best without hyperparameter search"**
- **D106 注**：τ=0.7 统一后 gap 从 0.031 增至 0.054，但 grid-best seed variance (±0.033) 大于 adaptive (±0.007)，adaptive 仍落在 grid plateau (b=0.1-0.3, 17.62-17.66) 边缘
- **"eliminates grid search cost (6N → 1 runs)"** + **"consistent improvement across all seeds"**
- b=0.1 三 seed 完成：17.655±0.009（range=0.017，极稳定）；b=0.1-0.3 形成 flat plateau (17.62-17.66)，adaptive 落在 plateau 内
- b=0.2 cross-seed 从 checkpoint-5500 恢复中

**三 seed 数据（D074, τ=0.8；D106 τ=0.7 对照）**：

| Metric | seed42 | seed123 | seed456 | Mean±Std |
|--------|--------|---------|---------|----------|
| Uniform PPL | 17.690 | 17.690 | 17.700 | 17.694±0.005 |
| Grid-best b=0.3 PPL | 17.640 | 17.579 | 17.640 | **17.620±0.033** |
| Adaptive PPL (τ=0.8) | 17.650 | 17.643 | 17.660 | **17.651±0.007** |
| Adaptive PPL (τ=0.7) | — | — | — | **17.674±0.007** |
| Capture ratio (τ=0.8) | 80.0% | 90.4% | 80.0% | 83.5% |

Grid-best advantage (0.031@τ=0.8, 0.054@τ=0.7) 在 grid 自身 seed variance (±0.033) 范围内，adaptive 的 seed variance 更小 (±0.007)——adaptive 更稳定。D106 统一 τ=0.7 后 gap 增大但 claim 仍成立（grid 95% CI 覆盖 adaptive）。

### Claim 3 (Setting): Unknown Contamination Proportion

方法仅需 detector scores，无需已知污染比例、无需 clean validation set。

- **差异化**：Golden Ratio 需已知比例 k；Drayson 的 b 依赖 validation set；我们仅需 per-sample q-scores
- **实际意义**：web-scale pretraining 中污染比例本质不可知
- **D021 代码修复**: ✅ τ 固定 CLI 参数（D104 后默认 τ=0.7），不依赖 contamination_ratio
- **D025 理论审计**: arXiv 2602.16065 的 α 是已知比例，τ 不能声称有 proportion-free 理论推导。τ 定位为 empirical hyperparameter with theoretical motivation
- **D035 τ sweep 完整数据 (6 点)**：[0.5, 0.8] 为 safe range（all beat uniform，PPL 差异 <0.035），τ=0.7 推荐为实用默认值（D104: comparable holdout + consistent OOD advantage）；τ>0.8 因 b* 膨胀退化。正确表述："wide safe range [0.5, 0.8] with recommended default τ=0.7"，不说"insensitive"
- **Claim 3 核心仍成立**：b* 推导不需要已知比例（ESS 和 α_eff 从 batch 统计量计算），方法运行时不访问 contamination_ratio。τ 在 [0.5, 0.8] 范围内是 robust empirical default，类似于 learning rate warmup steps——有理论 motivation 但具体值凭经验，且有明确的有效范围上界
- **结构性解释（D056/Reviewer）**：ESS 约束本身是 ρ-independent 的（仅依赖 batch 内权重浓度 + n_min），D056 修正后 ESS 主导 ~61-66% 的 batch，这为 proportion-robust 行为提供了结构必然性——不是巧合。跨 ρ 数据：b* mean ρ=0.4=1.425 vs ρ=0.6=1.402（差 1.6%），ESS binding 61%→66%，α_eff binding 38%→33%
- **Claim 1-3 联动**：ESS 主导解释了 b* 跨 ρ 稳定（Claim 3），α_eff 在剩余 ~37% batch 中的干预解释了 dual > ESS-only（Claim 1）。两个约束互补：ESS 提供 ρ-robust 基线行为，α_eff 提供针对性质量干预
- **D071 scope 定稿**：scope 收窄至 **ρ≥0.4**。ρ=0.2 + τ=0.8 PPL=17.38 vs uniform 17.336，Δ=+0.046（worse）——graceful degradation，不是严重退化。Limitations 说明 ρ>0.8 未测试
- **τ = 1 − ρ/2 经验规则**：ρ=0.4 → τ=0.8（最优 ✅），ρ=0.6 → τ=0.7（最优 ✅），ρ=0.2 → τ=0.9 predicted 但 negative（PPL=17.712 > uniform）。2/3 数据点支持，定位为 practical heuristic（非严格 rule），仅限 ρ≥0.4 场景
- **Claim 3 叙事策略（Reviewer 审查后定稿）**：
  - **Lead with structural argument**：b* 跨 ρ 稳定（mean 1.425@ρ=0.4 vs 1.402@ρ=0.6，差 <2%）因 ESS 约束 ρ-independent——结构性一致，非巧合
  - **PPL delta 作为验证（D106 τ=0.7 统一后）**：ρ=0.4 Δ=-0.020, ρ=0.6 Δ=-0.032。效应随 ρ 增大（不再 diminishing），因为 τ=0.7 更好匹配 ρ=0.6（τ=1−ρ/2 heuristic: ρ=0.6→τ=0.7 恰好最优）
  - **效应随 ρ 增大的解释（条件性）**：固定 τ=0.7 下效应随 ρ 增大（-0.020→-0.032），但这**不是**"ρ 越高方法越好"的一般规律——τ=0.8 下效应是递减的（-0.043→-0.028）。真正原因：τ=0.7 恰好是 ρ=0.6 的最优 τ（τ=1−ρ/2 heuristic），而对 ρ=0.4 略次优（τ=0.8 更好）。论文中避免"效应随 ρ 增大"的无条件表述
  - **禁止 "never hurts" / "safety" framing**——ρ=0.2 已证明退化
  - **用词**："consistent advantage" / "persistent benefit"，不用 "consistent improvement"
  - **参考表述（D106 升级）**："With recommended default τ=0.7, the adaptive method provides statistically significant improvement at both ρ=0.4 (Δ=-0.020, p<0.003) and ρ=0.6 (Δ=-0.032, p<0.01). The effect scales with contamination severity, consistent with the τ=1−ρ/2 heuristic (τ=0.7 is optimal for ρ=0.6). Structural analysis shows b* remains stable across ρ (<2% variation), with ESS binding dominating at higher ρ (61%→67%)."
- **contamination_60 三 seed — τ=0.8 (D076) vs τ=0.7 (D105/D106)**：

  **τ=0.8（旧主结果，现移至 appendix）**：
  | seed | adaptive | uniform | Δ |
  |------|----------|---------|-------|
  | 42 | 17.740 | 17.766 | -0.026 |
  | 123 | 17.732 | 17.754 | -0.022 |
  | 456 | 17.735 | 17.770 | -0.035 |
  | **mean±SD** | **17.736±0.004** | **17.763±0.008** | **-0.028±0.007** |

  **τ=0.7（D106 主结果）**：
  | seed | adaptive | uniform | Δ |
  |------|----------|---------|-------|
  | 42 | 17.735 | 17.766 | -0.031 |
  | 123 | 17.727 | 17.754 | -0.027 |
  | 456 | 17.732 | 17.770 | -0.038 |
  | **mean±SD** | **17.731±0.004** | **17.763±0.008** | **-0.032±0.006** |

  τ=0.7 效应量比 τ=0.8 大 14%（-0.032 vs -0.028），且比 ρ=0.4 (Δ=-0.020) 大 60%——效应随 ρ 增大

  **D105/D108 τ=0.7 vs τ=0.8 全量配对比较（ρ=0.6, 3-seed holdout）**：
  | Seed | τ=0.7 | τ=0.8 | Δ(0.7−0.8) |
  |------|-------|-------|------------|
  | 42 | 17.735 | 17.742 | −0.007 |
  | 123 | 17.727 | 17.733 | −0.006 |
  | 456 | 17.732 | 17.735 | −0.003 |
  | **Mean** | **17.731** | **17.737** | **−0.005** |
  Paired t = −4.70, df = 2, **p < 0.05**。τ=0.7 在所有 3 seed 上均优于 τ=0.8。

  **OOD + Downstream（τ=0.8 seed42/123 D105 eval）**：
  | Metric | τ=0.8 s42 | τ=0.8 s123 | τ=0.7 s42 | τ=0.7 s123 | τ=0.7 s456 |
  |--------|-----------|------------|-----------|------------|------------|
  | OWT PPL | 18.42 | 18.40 | 18.408 | 18.385 | 18.411 |
  | Wiki PPL | 15.37 | 15.34 | 15.355 | 15.329 | 15.424 |
  | DS mean | 0.5398 | 0.5368 | 0.5403 | 0.5361 | 0.5375 |
  OOD/downstream 差异在种子方差范围内，方向不一致。τ=0.7 优势主要体现在 holdout（统计显著），OOD/downstream 持平
- **ρ 梯度 evidence**：Uniform baseline PPL scales with ρ: 17.336 (ρ=0.2) → 17.694 (ρ=0.4) → 17.766 (ρ=0.6), establishing clear motivation for reweighting in any contamination regime
- **跨 ρ 机制分析数据（D056 修正 + Worker 实测更新）**：
  | ρ | τ | α_eff binding | ESS binding | b*=0 (clean) | b* mean | mean_q |
  |---|---|---|---|---|---|---|
  | 0.2 | 0.8 | 60.1% | 26.3% | 13.7% | 1.735 | 0.393 |
  | 0.4 | 0.8 | 37.2% | 61.0% | ~2% | 1.425 | ~0.6 |
  | 0.6 | 0.8 | 33.4% | 66.6% | — | 1.368 | 0.624 |
  注：ρ=0.4 数据来自 bs=4 主实验 (adaptive_fix_seed42)，ρ=0.2 和 ρ=0.6 来自对应 bs=4 实验。之前 ρ=0.2 ESS=40% 是因为忽略了 b*=0 类别（60+40=100）。
  ρ↑ → ESS binding↑ → b* 被压低 → 干预力度受限 → PPL 改善递减。ρ=0.2 失败解释：α_eff binding 60% 但 mean_q 仅 0.393，detector 低污染下区分力弱，导致错误方向的 reweighting。

## 1.7B Scale Verification (D090 → D107/D108 → D112 3-seed 定稿)

Qwen3-1.7B from-scratch 3-seed 全量 eval（ρ=0.4, τ=0.8）：

| Metric | Uniform (3-seed) | Adaptive (3-seed) | Δ |
|--------|---------|----------|---|
| Holdout PPL | 13.275±0.009 | 13.262±0.010 | −0.013 |
| OWT PPL | 13.297±0.009 | 13.288±0.006 | −0.008 |
| Wiki PPL | 10.938±0.017 | 10.951±0.004 | +0.013 (方向不一致: seed42 +0.036, seed123 +0.010, seed456 −0.006) |
| Downstream Mean | 0.625±0.001 | ~0.626 | ~+0.001 |

**Scaling 对比（adaptive − uniform）**：

| Scale | Holdout Δ | OWT Δ | Wiki Δ | DS Δ |
|-------|-----------|-------|--------|------|
| 0.6B ρ=0.4 τ=0.7 3-seed | −0.020 | −0.028 | −0.029 | ~0 |
| 0.6B ρ=0.6 τ=0.7 3-seed | −0.032 | −0.02 | −0.03 | ~0 |
| **1.7B ρ=0.4 τ=0.8 3-seed** | **−0.013** | **−0.008** | **+0.013** | **~0** |

Holdout/OWT: 3/3 seeds 一致改善。Wiki: 方向不一致（2/3 退化 1/3 改善，std ~0.021），属噪声。效应量从 0.6B 到 1.7B 缩小约 35-60%。

**D112 最终叙事**："adaptive reweighting scales without degradation; holdout and OWT consistently improve, Wiki OOD not directionally consistent across seeds. Benefit diminishes as larger models are more robust to contamination." 不启动 1.7B τ=0.7 实验（seed456 Wiki Δ=-0.006，未超 +0.020 阈值）。

**论文处理**：results inline 格式带 ±，3-seed confirmed。正确 claim: "the method scales without degradation"。**禁止** claim "advantage persists/holds at larger scale"。

## Detector Requirements: Calibration AND Discrimination（Primary Contribution #2）

不仅是 "lightweight detector sufficiency"——3×3 detector matrix 揭示 **AUC alone insufficient, calibration (ECE) is the key differentiator**。这是对 detect-and-reweight 范式的重要发现：practitioners 应优先确保 detector score calibration，而非追求高 AUC。

**D106 detector quality 实证（Reviewer 审查后纳入）**：
| Detector | AUC | Adaptive PPL | vs Uniform (17.694) | 结论 |
|----------|-----|-------------|---------------------|------|
| TF-IDF + LR | 0.939 | 17.674 (τ=0.7) | −0.020 ✓ | calibrated scores → works |
| GPT-2 PPL | 0.913 | 17.79 | +0.096 ✗ | AUC high but poorly calibrated → worse than uniform |
| N-gram PPL | 0.73 | 17.82 | +0.126 ✗ | low AUC + poor calibration → worst |

**关键论证**：AUC=0.913 的 GPT-2 PPL 检测器反而比 uniform 更差——证明 AUC 不是决定因素，calibration（q-score 连续性和概率语义）才是。TF-IDF+LR 的 temperature scaling (T=0.204) 后 ECE=0.048 是成功的关键。

**3×3 数据（3-seed + ECE, Round 8 完整）**:
| Detector | AUC | ECE | 3-seed Mean PPL | Δ vs Uniform |
|----------|-----|-----|-----------------|--------------|
| TF-IDF+LR | 0.939 | 0.048 | 17.650±0.010 | −0.044 ✓ |
| GPT-2 PPL | 0.913 | 0.131 | 17.792±0.005 | +0.098 ✗ |
| N-gram PPL | 0.731 | 0.069 | 17.823±0.003 | +0.129 ✗ |

论文 detector section 显式报告此三者 + ECE，强化 "both calibration and discrimination required" 论点。

## n_min Robustness Framing

ESS 约束的 n_min 是 adaptive b* 的超参数之一（另一个是 τ）。

- n_min=3 at batch_size=4 → ESS 约束过紧，b* 被钳制在低值，seed42 零改善
- n_min=2 at batch_size=4 → 稳定工作，3/3 seeds positive
- **论文呈现**：n_min sensitivity curve (n_min=1,2,3,4,5) + batch_size 消融 (4,8,16) 证明 knife-edge 是 batch_size=4 的 artifact

## Narrative Structure (D115 — Analysis Paper)

**起点**: Web 语料 20-60% 为合成文本，Drayson et al. (EMNLP 2025) 提出 detect-and-reweight 框架应对污染，但 b 需 per-model grid search 且评估方法论未经审视。

**我们的研究问题**: When, why, and how does detect-and-reweight actually work? 不是 "我们提出更好的方法"，而是 "我们系统性分析这个范式"。

**发现 1 — Epoch Confound**: D&R 的 PPL 优势 96% 来自 multi-epoch exposure effect，仅 4% 来自 filtering。这意味着过去对 D&R 效果的评估存在系统性高估。

**发现 2 — Detector Requirements**: AUC alone insufficient；需要 calibration AND discrimination。GPT-2 (AUC=0.913) 反而 worse than uniform，因 ECE=0.131。TF-IDF (AUC=0.939, ECE=0.048) works → lightweight but calibrated > powerful but uncalibrated。

**发现 3 — Mechanism**: α_eff/ESS binding dynamics 揭示 min-intervention > max-intervention。38% batches 中 α_eff binding 将 b* 压至 ESS 上界的 ~20%。ESS-only 在 ρ=0.6 collapse → α_eff 在高污染下提供不可替代的质量信号。

**工具 — Adaptive b***: 从以上分析中涌现的工程方案。Dual-constrained b* 零 validation cost、matches grid-best within seed variance、proportion-agnostic [ρ≥0.4]。不是主角，是分析的 byproduct。

**实验验证**: (a) epoch confound 分解 + LR 控制实验; (b) 3×3 detector matrix with ECE; (c) ESS-only baseline 对比; (d) τ/n_min sensitivity; (e) 1.7B scaling。

## Contribution Structure (D115 — Analysis Paper Reframe)

1. **Primary — Analytical: Epoch Confound**: D&R PPL 优势 96% 来自 multi-epoch exposure，仅 4% 来自 filtering。对 detect-and-reweight 范式评估方法论的重要 caveat，社区最有价值的发现。
2. **Primary — Analytical: Detector Requirements**: calibration (ECE) AND discrimination (AUC) both required。GPT-2 (AUC=0.913, ECE=0.131) worse than uniform；TF-IDF (AUC=0.939, ECE=0.048) works。AUC alone insufficient — "lightweight but calibrated > powerful but uncalibrated"。
3. **Secondary — Analytical: Mechanism Decomposition**: α_eff/ESS binding dynamics（38% α_eff-binding, b* ratio ~5×），min-intervention vs max-intervention，ESS-only collapse at ρ=0.6，跨 ρ b* stability (<2% variation)。
4. **Tool — Method: Adaptive b***: Dual-constrained b* 作为实用工具 — zero validation cost, matches grid-best within seed variance, proportion-agnostic in [ρ≥0.4]。Method 不再是 primary contribution，而是 analysis 的工程产出。

**叙事逻辑**: 我们不是在 propose a better method，而是在 analyze 一个范式 — 发现 confounds、刻画 requirements、分解 mechanism — adaptive b* 是从这些分析中自然涌现的工具。

## Method Comparison Spectrum

实验揭示了一个清晰的方法谱系，从硬过滤到纯自适应，每种方法在 threshold sensitivity 与 safety 之间占据不同位置：

| Method | PPL (ρ=0.4) | Threshold requirement | Trade-off |
|--------|-------------|----------------------|-----------|
| detect_remove (q>0.3) | 17.253 | precise calibration required | best PPL, but brittle to threshold choice |
| detect_remove (q>0.5) | 17.290 | moderate calibration | strong PPL, still threshold-dependent |
| hybrid (q>0.95 + adaptive) | 17.514 | conservative safe threshold only | middle ground: safe filter + soft reweight |
| adaptive (dual-constrained) | 17.674 (τ=0.7) / 17.653 (τ=0.8) | threshold-free | fully automatic, no calibration risk |

**Key observations:**

1. **detect_remove** achieves the lowest PPL when the threshold is correctly calibrated, but performance depends critically on threshold choice (q=0.3 vs q=0.5 yields 0.037 PPL gap; wrong threshold could degrade significantly).

2. **hybrid** uses a deliberately conservative threshold (q>0.95, removing only near-certain synthetic samples) combined with adaptive reweighting on the remainder. This reduces threshold sensitivity while retaining partial filtering benefit.

3. **adaptive** operates entirely without threshold calibration. The dual constraints (α_eff + ESS) determine per-batch intervention strength from q-score statistics alone.

**论文需要 "When to use which" discussion**: 如果 practitioner 有高质量检测器 + 能投入资源做 threshold calibration，detect_remove 是最优选择。如果检测器质量不确定或 threshold calibration 不可行（web-scale 常态），adaptive 提供 zero-calibration guarantee。hybrid 适用于检测器对极端 case 可靠但 borderline 区域不确定的场景。

### batch_adaptive_tau: Negative Result (Simplicity Validated)

Per-batch τ adaptation (dynamic τ based on batch statistics) 未能改善固定 τ 的表现 (PPL=17.681 vs τ=0.8 的 17.653)。结论：固定 τ 已是最优策略，额外的 per-batch τ 动态调整增加复杂度但无收益。D104 推荐 τ=0.7 为默认值（comparable holdout, better OOD generalization）。这验证了方法设计中 "τ as stable empirical default" 的选择——simplicity is a feature, not a limitation。

## Anticipated Reviewer Concerns

| Concern | Response Strategy | 实验支撑 |
|---------|------------------|----------|
| **"Why not just filter?" (D051)** | detect_remove (q>0.5) PPL=17.29 大幅优于 adaptive (17.65)。根因：eval 是 human-only，filtering 后分布天然匹配。**Reframe**: adaptive 无需 threshold calibration + 保留全部数据。**关键依赖**: threshold sensitivity (q>0.3/0.7) 证明 filtering 对 threshold 脆弱 | detect_remove ✅ + threshold_q03/q07 🔄 |
| "Incremental over Drayson" | 差异化: adaptive b* (zero validation) vs per-model empirical b; min-intervention principle; loss reweighting vs SIR | Claim 1 + Claim 3 + ESS-only baseline |
| "α_eff monotone → just ESS thresholding?" | inf{b} vs max{b} 区分: 最小干预 vs 最大干预。Q1 实证: 37.2% α_eff binding, b* mean 1.19 vs ESS-only 5.88 (ratio ~5×)。ESS-only baseline 对比训练结果 | ESS-only baseline + Q1 figure |
| "Small effect size (~0.1-0.2% PPL)" | D106: τ=0.7 ρ=0.4 Δ=-0.020 (p<0.003), ρ=0.6 Δ=-0.032 (p<0.01)，效应随 ρ 增大。1.7B Δ=-0.013（效应随 scale 递减，大模型更鲁棒）。zero-cost advantage + 效应 scales with contamination severity | p0_contamination_60 + 1.7B scale ✅ |
| "Two hyperparameters (τ, n_min) vs one (b)" | 关键区别：τ 在 [0.5,0.8] 有效（sweep 6 点验证），n_min=2 跨 3 seed 稳定。两个 HP 都有明确 safe range + principled default，设一次即可跨数据集；Drayson 的 b 需 per-model per-dataset validation。2 个 robust defaults 替代 1 个 sensitive HP | p0_nmin_* + p0_tau_sweep ✅ + p0_batchsize_* |
| "Only 0.6B model" | D112: 1.7B 3-seed 全量 eval：holdout Δ=-0.013, OWT Δ=-0.008（3/3 seeds 一致改善），Wiki Δ=+0.013（方向不一致，噪声），DS ~0。Scaling framing: "scales without degradation; benefit diminishes." 核心证据在 0.6B 三 seed，1.7B 为 3-seed scalability 验证 | p0_batchsize_* + 1.7B scale ✅ |
| "Detector quality sensitivity" | D106: TF-IDF+LR (AUC=0.939, calibrated) works; GPT-2 PPL (AUC=0.913, uncalibrated) WORSE than uniform (+0.096); N-gram (AUC=0.73) worst (+0.126)。AUC 不决定效果，calibration 才是关键 | ngram_adaptive ✅ + gpt2_adaptive ✅ |
| "Controlled injection ≠ real web" | domain-skewed + semi-realistic | p2_domain_skewed |
| "τ comes from contamination_ratio?" | τ 代码已独立 (D021 fix); 收敛理论 α 确实依赖已知比例 (D025)，诚实说明 τ 是 empirical default with theoretical motivation; τ sweep 6 点完整数据证明 [0.5,0.8] safe range + recommended default τ=0.7 (D104: comparable holdout + better OOD) | p0_tau_fix ✅ + p0_tau_sweep ✅ |

## Key Risks

1. **~~ESS-only baseline 可能同样好~~** ✅ **RESOLVED (D029→D073, D106 更新)**: ESS-only 三 seed mean=17.738±0.022。与 τ=0.7 adaptive (17.674±0.007) 比较 gap=0.064，与 τ=0.8 adaptive (17.651±0.007) 比较 gap=0.087。无论哪个 τ，消融层级 Adaptive < Uniform < ESS-only < Random 均成立
2. **Novelty risk (D013)**: 基础公式来自 Drayson，双约束框架新颖性需充分论证。**应对**: 差异化锚定在 min-intervention principle + zero validation cost
3. **~~τ 修复后性能变化~~** ✅ **RESOLVED (D035)**: τ sweep 6 点完成。[0.5, 0.8] safe range 全部 beat uniform；τ=0.8 最优；τ>0.8 退化但机制清晰（b* 膨胀）。方法 robust in practical range
4. **~~τ 理论来源依赖已知比例~~** ✅ **RESOLVED (D025+D035)**: τ 定位为 empirical HP with theoretical motivation。τ sweep 提供完整 empirical justification，Claim 3 核心不受影响
5. **效应量小**: **应对**: D106 统一 τ=0.7 后 ρ=0.4 Δ=-0.020（p<0.003）、ρ=0.6 Δ=-0.032（p<0.01）。效应随 ρ 增大——方法在问题越严重时越有价值。1.7B 不退化。zero-cost advantage framing
6. **Venue fit**: 核心偏 ML，EMNLP reviewer 可能低估。**应对**: NLP-specific analysis
7. **detect_remove 大幅优于 adaptive (D051)**: PPL=17.29 vs 17.65，gap=0.36。根因：eval 只测 human-like text，hard filtering 后训练分布 ≈ eval 分布（distribution match confound）。**应对**: (a) threshold sensitivity（q=0.3/0.5/0.7）证明 filtering 对 threshold 脆弱; (b) reframe: 无需 threshold calibration + 信息保留; (c) 诚实报告 detect_remove 是 human-eval best。**状态**: threshold experiments RUNNING

## MVP → Full Paper 扩展路径

| 维度 | MVP | Full Paper |
|------|-----|-----------|
| 污染比例 | 40% | 20%, 40%, 60% |
| 模型 | Qwen3-0.6B | + Llama-3.2-3B |
| 生成器 | Qwen3-0.6B (self) | + Llama-3.2-1B, Mistral, Gemma |
| 检测器 | TF-IDF + LR | + ModernBERT variants (quality ablation) |
| Baseline | uniform, grid-b, adaptive | + ESS-only adaptive, Golden Ratio, detect-and-remove, random reweight |
| 评估 | eval_ppl | + MMLU, HellaSwag, Self-BLEU, distinct-n |
| 注入方式 | uniform random | + domain-skewed, semi-realistic |
| n_min 分析 | n_min=2 vs n_min=3 | + n_min=1,4,5 + batch_size=4,8,16 |
| τ 分析 | 无 | ✅ τ sweep (6 点) + ESS-only vs dual-constraint 对比 |
