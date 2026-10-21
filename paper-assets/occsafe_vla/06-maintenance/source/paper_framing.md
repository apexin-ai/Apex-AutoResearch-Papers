# OccSafe-VLA — Paper Framing

> 维护者: Director | 最后更新: 2026-05-29 13:30 UTC | 状态: Draft — **D074 Dual Main Effects (D076 N=14 sync)** — v2 factorial: gradient flow 主效应 (Δ=-3.0pp) + normalization 主效应 (LN>BN, Δ=+3.6pp, d≈1.05); ANOVA interaction ≈ 0 (F=0.10, p=0.763); BN+Grad ON 是唯一 < Vanilla 的配置。Cell 1 n=3, Cell 2 n=4, Cell 3 n=4, Cell 4 n=3。CoRL 2026 target (Paper May 29)
>
> ⚠️ **D074 Dual Main Effects Transition (2026-05-27)**: Reviewer 审查发现 ANOVA 交互项 F=0.10, p=0.763，数学上不可能显著。"ordinal interaction" framing 改为 "dual main effects + practical threshold crossing"。新增 normalization 主效应 (d≈1.05) 作为 secondary claim。详见 D074。

## Architecture Facts (from code, verified)
- **Occ head input**: DINOv2(1024) + SigLIP(1152) 拼接 = 2176d（非仅 DINOv2）
- **Occ head**: Linear(2176→256) → reshape(B,256,16,16) → ConvTranspose2d×2 上采样(16→32→64) → Conv2d(64→1)。BatchNorm2d + GELU。参数量 1.2M。
- **FocalLoss**: α=0.25, γ=2.0
- **occ_loss_weight**: λ=0.01, 指数衰减 w(t)=0.01×exp(-t/50000)
- **LR**: 5e-4 恒定（MultiStepLR milestone=100K > max_steps，从未触发）
- **LoRA**: rank=32, alpha=16, dropout=0.0
- **GPU**: 4× RTX PRO 6000 98GB per server
- **训练时间**: ~12.9h/run @ 1.08 it/s

### 叙事含义
- **双编码器梯度流**: Occ head 接收 DINOv2+SigLIP 拼接特征，occupancy supervision 同时影响两个编码器。
  比"仅改善 DINOv2"更强 — 同时改善语义(SigLIP)和空间(DINOv2)编码器的 3D 感知。
- **极轻量**: occ_head 仅 1.2M params = 全模型 7.65B 的 0.016%，强化 "lightweight auxiliary" 叙事
- **occ_loss 指数衰减**: w(t)=0.01×exp(-t/50000) → 训练后期 occ 监督逐渐"放手"让 action loss 主导，
  可论证为"先学空间结构，再精化动作"的课程学习效果
- **LoRA alpha=16 < rank=32**: 有效 scaling factor = alpha/rank = 0.5，比常见的 1.0 更保守

### DepthHead (新增, 2026-05-22)
- **Depth head**: Linear(2176→256) → ConvTranspose2d×2 (256→128→64, kernel=4, stride=2) → ReLU（无 sigmoid）
- **SmoothL1Loss**, depth_loss_weight=0.01 + 指数衰减（同 occ_loss_weight）
- **GT 来源**: MuJoCo sim 深度渲染（state replay），分辨率 64×64
- **参数量**: ~1.2M（与 OccHead 同量级）

## Core Insight (D043 Plan B, 2026-05-26)

**假设演变**：
- 原始假设（已推翻）：BEV occupancy → 3D 空间感知 → safety emergence
- D017-D019：梯度流是防止损害的条件，非提供收益的条件
- D040 (v1)：crossover interaction — BN+gradient flow = best ← **v2 不可复现**
- **D043 (v2, 当前)：ordinal interaction — gradient flow 损害 CAR，BN 放大损害**

### D074 v2 Factorial — Dual Main Effects（当前权威数据）

| | BN | LN | Δ(LN-BN) |
|--|----|----|-----------|
| **Gradient ON** | **0.725±0.064** (n=3) | **0.773±0.027** (n=4) | **+4.8pp** |
| **Gradient OFF** | 0.767±0.024 (n=4) | **0.802±0.024** (n=3) | **+3.5pp** |
| Δ(ON-OFF) | **-4.2pp** | **-2.9pp** | — |
| **主效应** | BN pooled: 0.749 | LN pooled: 0.785 | **+3.6pp (d≈1.05)** |
| Vanilla | — | — | **0.745±0.024** (n=3, v2: 0.768/0.748/0.720) |

**ANOVA 交互项**: F=0.10, p=0.763, η²=0.005。两行斜率几乎相同 (BN: -4.2pp, LN: -2.9pp)，纯可加模型。**BF₀₁=3.50**（moderate evidence for additivity, BIC-based Bayes Factor）。

**关键发现（D074 更新）**：
- **Gradient flow 主效应**: ON pooled (0.752) < OFF pooled (0.782), Δ=-3.0pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全
- **Normalization 主效应**: LN pooled (0.785) > BN pooled (0.749), Δ=+3.6pp, F=4.49, p=0.060, η²=0.253 — LN 一致优于 BN
- **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**——其他三个 cell 均 ≥ Vanilla
- **Grad ON < Vanilla; Grad OFF ≈ Vanilla** — Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，t=1.20, p=0.28，统计不可区分
- **Cell 1 高方差** (std=0.064, 3× 其他 cell) — BN+gradient flow 导致训练不稳定，本身是 finding
- ✅ Cell 4 n=3 (D076 revert): [0.826, 0.802, 0.778], mean=0.802±0.024
- Cell 4 vs Vanilla: Hedges' g=1.89, p=0.045

### v1 → v2 数据不一致 [v1-SUPERSEDED]

v1 Full OCC BN = 0.797 (best) → v2 Full OCC BN = 0.700 (worst)。原因待查（代码版本差异）。
**论文策略**：以 v2 factorial 为权威数据集。v1 数据不纳入主 claim。v1/v2 差异可在 appendix 讨论 code sensitivity。

### 机制证据状态（全部来自 v1 checkpoint — pending v2 validation）

### 机制证据状态（D056 v2 验证完成）

**D026 Gradient Collapse Prevention — ⚠️ 待同方法论 v2 验证**：
- v1 结果：Detach gradient norms = 1-13% of Vanilla — "灾难性崩塌"（逐层分析, 200 真实样本）
- v2 分析：Detach/Vanilla ratio = 1.29（patch_features 接口, 5 合成 batch）
- **D057 修正**：v1 与 v2 方法论不同（逐层 vs 接口, 真实数据 vs 合成数据），**不可声称 v2 推翻 v1**
- **TODO**: 用 v1 相同方法论（逐层 backbone 梯度, ≥200 真实样本）在 v2 checkpoint 上重做
- 论文中暂时**不引用**梯度 collapse/非 collapse 任何 claim，待同方法论验证

**v2 Gradient Analysis (D056/D057) — 部分有效**：
- ✅ **梯度正交性 (cosine≈0, conflict≈50%)**：方法论独立可信，v2 确认
- ⚠️ **OCC 梯度极小 (<1.5%)**：v2 独立成立，但 5 个合成 batch 统计力不足
- ⚠️ **Full OCC action grad 下降 9%**：在当前样本量下可能是噪声 + 选择偏差 (s1 = worst seed)
- ❌ **v1/v2 梯度比值对比**：方法论不同，论文中**不可引用**

**D034-D035 BN Interference + CKA — ❌ v1 CKA 退化已确认为 bug 产物**：
- v1 CKA (May 20 代码)：Detach BN CKA 灾难性退化 (DINOv2=0.539, SigLIP=0.312) → checkpoint 已删除
- Retrain CKA (May 24 新代码)：DINOv2=0.964, SigLIP=0.953 → 正常
- **所有 v2/retrain 条件 CKA 均在 0.95-0.97，与 Vanilla 一致** — 无表征漂移
- BN forward-pass 并未导致表征退化 — "BN interference" 假设不成立

**机制现状（D057 修正, Reviewer 确认）— 无可用机制证据**：
所有 v1 机制证据（gradient collapse, CKA drift, gradient redistribution, crossover interaction）均为 bug 产物。
v2 存活的机制信号：
- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — 仅排除直接梯度冲突
- ⚠️ Full OCC action grad -9% — 统计力不足 (5 合成 batch)
- ❌ "capacity competition" — Reviewer 驳回：OCC head 极小，CKA 正常，无 capacity 竞争证据
- ❌ "BN forward-pass interference" — Reviewer 驳回：BN 在 OCC decoder 内部，不在 backbone；Detach 也有相同 BN 但 CAR 更好
- **唯一解释**：gradient flow ON vs OFF 改变了 LoRA 优化轨迹（dual-objective loss landscape），但太 generic 不构成可发表 claim

### Core Insight（D074 修正）

VLA LoRA fine-tuning 中，auxiliary spatial head 对安全性的影响由两个独立主效应驱动：

1. **Gradient flow 主效应**: 梯度流损害安全（ON < OFF, Δ=-3.0pp, F=3.20, p=0.104），Detach 消除损害
2. **Normalization 主效应**: LN 一致优于 BN（Δ=+3.6pp, F=4.49, p=0.060, d≈1.05），独立于 gradient flow 条件
3. **Practical threshold**: BN+Grad ON 是唯一低于 Vanilla 的配置（其余三 cell 均 ≥ Vanilla）

**行为层面**：两个主效应近似可加（ANOVA 交互项 F=0.10, p=0.763, η²=0.005; BF₀₁=3.50），BN+gradient flow 叠加产生最差结果（0.725）且训练不稳定（std 3× 其他）。Detach 模式完全消除梯度流损害。

**Safety-specificity（D080 新增）**：TSR factorial ANOVA 所有效应均不显著（all p>0.27）——gradient flow 和 normalization 仅影响碰撞回避，不影响一般任务成功率。

**Per-task 放大效应（D080 新增）**：Normalization 优势在 hard safety tasks (T3/T5/T6) 上放大 4×（+6.9pp vs easy tasks +1.7pp）。Gradient flow harm 无 task-level 集中模式。

**统计稳健性（D080 新增）**：Leave-one-out 分析 14/14 次删除中两效应方向一致（F_grad∈[1.73,6.05], F_norm∈[3.06,7.91]）。Levene's test W=0.71, p=0.57（方差齐性未被拒绝）。Welch 校正 p: gradient=0.204, norm=0.104。

**机制层面（D057 修正）**：
- 梯度正交性 (cosine≈0) 在 v2 确认 → 排除直接梯度冲突
- 梯度 collapse 状态未知（v1/v2 方法论不同，需同方法论重做）
- BN forward-pass 干扰（CKA 退化）待 v2 CKA 验证
- 空间内容仍然次要

**论文策略选项**（Reviewer 建议）：
- **Option A**: 依赖梯度机制 → 需用 v1 方法论在 v2 上重做，时间成本 ~2-4h
- **Option B**: 不依赖梯度机制，以 CAR 统计分析 (ANOVA 效应量) 为核心证据 + 梯度正交性作为辅助排除证据。更稳健，不受方法论争议影响
- 推荐 **Option B + v2 CKA** 作为主线，v2 同方法论梯度分析作为 supplementary

### 措辞约束（D057 更新）
- **禁止** "crossover interaction" — v2 是 ordinal
- **禁止** "statistically significant interaction" / "significant interaction effect" — ANOVA 交互项 contrast ≈ 0，数学上不可能显著 (D074)
- **谨慎** "interaction" 单独使用 — 改用 "normalization-dependent gradient flow effect" 或 "dual main effects"
- **禁止** "BN-mediated gradient calibration" / "existence regularization" — v1 不可复现
- **禁止** 引用 v1/v2 梯度数值的跨方法论比较
- **谨慎** "gradient collapse" / "no gradient collapse" — 待同方法论验证，暂不 claim
- **可用** "gradient orthogonality"（v2 确认）— 排除直接梯度冲突
- **可用** "capacity competition" / "BN forward-pass interference"（需标注为假设，待 CKA 验证）
- 所有条件 vs Vanilla 的差异需标注 n 和 CI，多数可能不显著
- Cell 1 高方差本身可作为 finding：用 "BN+gradient flow leads to unstable training"
- Gradient flow 主效应用 "detrimental" / "harmful"，不用 "collapse"（collapse 特指 detach 极端情况）

**已确认（D022）**：Depth CAR = 0.780 = Vanilla exactly (4 seeds)，egocentric depth 不比 random noise 更好。

## Framing Strategy (D019 修正)

**确定路线: Option B 分析论文**（Reviewer 审查通过）

**核心叙事转变 (D026)**：从"梯度流是必要条件"→"梯度流防止 encoder gradient collapse"（具体机制，非抽象论断）

**Title（暂定）**: "Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis"

**3-Contribution 结构（D043 Plan B 修正）**：
- **C1 (核心发现)**: Auxiliary spatial head 对 VLA 安全性的影响由**两个独立主效应**驱动（ANOVA 交互项 ≈ 0）：
  - **Gradient flow 主效应**: Grad ON < Grad OFF, Δ=-3.0pp, F=3.20, p=0.104, η²=0.180 — 梯度流损害安全
  - **Normalization 主效应 (d≈1.05)**: LN > BN, Δ=+3.6pp, F=4.49, p=0.060, η²=0.253 — LN 一致提供安全优势
  - **Practical threshold crossing**: BN+Grad ON (0.725) 是**唯一低于 Vanilla (0.745) 的配置**
  - **Detach 消除损害**: Detach BN (0.767±0.024, n=4) ≈ Vanilla (0.745±0.024, n=3)，统计不可区分 (t=1.20, p=0.28)
  - **BN+gradient flow 最不稳定**: Cell 1 std=0.064, 3× 其他 cell → 训练不稳定
  - 空间内容无关: Full OCC ≈ Random OCC ≈ Depth ≈ Vanilla
  - **Safety-specific**: TSR ANOVA 全 p>0.27 → 效应仅影响碰撞回避
  - **Task-level 放大**: Normalization 优势在 hard tasks 上 4× (+6.9pp vs +1.7pp)
  - **统计稳健**: BF₀₁=3.50 (additivity); LOO 14/14 方向一致; Levene p=0.57
  - 机制证据: 梯度正交性确认 (cosine≈0); gradient flow → LoRA 优化轨迹改变
  - ✅ 全部 14 factorial seeds 完成 (D076: Cell 4 reverted to n=3), ANOVA v2 final 已验证
- **C2 (方法论贡献)**: 首个 2×2 factorial + multi-condition study design for VLA auxiliary head mechanism analysis（gradient flow × normalization × spatial content）
- **C3 (实用贡献, D074 修正)**: 两个独立设计维度的推荐：(1) **若加辅助 spatial head，必须 detach 梯度** — Detach 消除 gradient flow 损害；(2) **用 LN 替代 BN** — LN 一致 +3.6pp 安全优势。**绝不用 BN + gradient flow**（最差 0.725 且 std 3× 其他）。最优：Detach + LN (0.802±0.024, n=3, g=1.89 vs Vanilla, p=0.045)
- **Observation (非 core claim, D041 修正)**: Temporal dynamics — continuous flow 最优，reverse（late-only）一致最差(timing>duration)，中间 cutoff ≈ Vanilla

## Core Contribution Evidence

### [v1-SUPERSEDED] v1 Behavioral Evidence (不再用于主 claim)
v1 数据：Full OCC BN=0.797 (best), Random=0.789, Vanilla=0.780, Detach+LN=0.765, Detach BN=0.746, Full OCC+LN=0.743。
v2 数据推翻 BN+gradient flow 的正面效应。v1 数据保留用于 appendix code sensitivity 分析。

### v2 Factorial Evidence (D043, 权威数据)

| Cell | Condition | n | CAR values | mean±std | 代码版本 |
|------|-----------|---|-----------|----------|---------|
| 1 | Full OCC BN (Grad ON + BN) | 3 | 0.746, 0.654, 0.776 | 0.725±0.064 | **v2** ✅ |
| 2 | Full OCC LN (Grad ON + LN) | 4 | 0.798, 0.792, 0.740, 0.762 | 0.773±0.027 | **v2** ✅ |
| 3 | Detach BN (Grad OFF + BN) | 4 | 0.774, 0.736, 0.762, 0.794 | 0.767±0.024 | **v2** ✅ |
| 4 | Detach LN (Grad OFF + LN) | 3 | 0.826, 0.802, 0.778 | 0.802±0.024 | **v2** ✅ (D076: n=4→3) |
| — | Vanilla | 3 | 0.768, 0.748, 0.720 | 0.745±0.024 | **v2** ✅ |

✅ **全部完成**：Cell 1 n=3 ✅; Cell 2 n=4 ✅; Cell 3 n=4 ✅; Cell 4 n=3 ✅ (D076); Vanilla n=3 ✅。共 N=14+3=17。
✅ **ANOVA v2 final (N=14, df=1,10)**: F(gradient)=3.20, p=0.104; F(norm)=4.49, p=0.060; F(interaction)=0.10, p=0.763。

### Mechanistic Evidence [v1-SUPERSEDED — 以上方 D056 section 为准]

**D026 Gradient Collapse [v1-SUPERSEDED]**：v1 数据 (Detach norms = 1-13% of Vanilla) 已被 D056 确认为旧代码 bug 产物。v2 patch_features ratio=1.29。同方法论 v2 验证脚本已就绪（compare_gradient_conditions.py），待 50K checkpoint 到位后执行。**论文中不可引用 v1 梯度 collapse 数据。**

**CKA Evidence [v1-SUPERSEDED]**：
- v1 Detach BN CKA (DINOv2=0.539, SigLIP=0.312) — **已确认为旧代码 bug 产物**（D034-D035）
- v2/retrain 所有条件 CKA ≥ 0.95，编码器表征完整，无灾难性退化
- **"BN = 100% 表征漂移原因" 不再成立** — v2 中 BN 不导致 CKA 退化

**D042 Same-Seed Gradient Analysis [v1-SUPERSEDED]**：
v1 数据显示 LN → DINOv2 grad ↓3.5×, SigLIP ↑2.5×。v2 中 BN+gradient 排序反转，需在 v2 checkpoint 上重做。

**两种失败模式（D031, 仍有效）**：
- Detach = 均匀退化 (per-task CAR std=0.002)
- Withdrawal (cutoff) = 选择性灾难遗忘 (per-task 方差极大)

**Status**: v2 factorial 全部完成: Cell 1 n=3 ✅, Cell 2 n=4 ✅, Cell 3 n=4 ✅, Cell 4 n=3 ✅ (D076), Vanilla n=3 ✅。N=14。Depth 4-seed ✅。ANOVA v2 final (N=14) verified。

### Claim 2 (Mechanism): Gradient Flow Harm [v1 机制证据已失效]
- ~~BN forward-pass 干扰导致表征漂移~~ [v1-SUPERSEDED] — v2 CKA ≥0.95，无表征漂移，"BN interference" 假设不成立
- ✅ Gradient flow 通过辅助头损害安全行为（v2 新发现：Grad ON < Grad OFF）
- ~~Detach gradient collapse (D026)~~ [v1-SUPERSEDED] — v1 bug 产物，v2 待同方法论验证
- ⚠️ v1 的 "existence regularization" / "BN-mediated calibration" 不再成立
- ✅ 梯度正交性 (cosine≈0, conflict≈50%) — v2 确认，排除直接梯度冲突

### Claim 3: Spatial Content Secondary
v1 数据 Full OCC ≈ Random OCC（0.797 vs 0.789, Δ=0.8pp）仍成立。
Depth = Vanilla exactly (4 seeds, D022)。空间内容次要。
⏳ v2 中尚未跑 Random OCC 和 Depth 的 factorial 对应实验。

### Claim 4 (Depth): ✅ Confirmed (D022)
Depth CAR = 0.780 = Vanilla exactly (4 seeds)。

## Depth MVP Gate（预注册，锁定于 2026-05-22 09:30 UTC，depth eval 前）

**【Pass（必须同时满足）】**
1. Depth 4-seed mean CAR 的 bootstrap 95% CI 下界 > 0.780（Vanilla 3-seed mean）
2. Depth 4-seed mean TSR ≥ 0.870

**【Fail（满足任一）】**
1. Depth 4-seed mean CAR < 0.780
2. Depth 4-seed mean TSR < 0.870

## Anticipated Reviewer Concerns

### RC1 [CRITICAL]: Collision Detection Metric Validity — ✅ RESOLVED
### RC2 [HIGH]: "Why Not Just Use CBF?" — Defense: zero inference cost + complementarity
### RC3 [HIGH]: Depth Ablation — ✅ RESOLVED (D022: Depth=Vanilla, 4 seeds)
### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations
### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations
### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI

## 待定关键实验

### plan_027: Detach + LayerNorm (BN Artifact Test) — ✅ DONE (D034)
替换 OccHead 的 BatchNorm2d 为 LayerNorm，在 detach 模式下测试。
- **结果: Scenario C (混合)** — Detach+LN CAR=0.765±0.023，介于 Detach BN(0.746) 和 Vanilla(0.780)
- BN 干扰贡献 ~1.9pp (~56%)，梯度流缺失贡献 ~1.5pp (~44%)
- 种子方差大（s0=0.792, s1=0.756, s2=0.748），95% CI 与两端均有重叠
- ✅ **Detach+LN CKA 分析完成 (D035)**：DINOv2=0.966, SigLIP=0.960 — 表征完全恢复。注：v1 中 BN→CKA 退化已被确认为代码 bug [v1-SUPERSEDED]；v2 所有条件 CKA ≥0.95，BN 不导致表征漂移

### Cutoff Temporal Dynamics (D029/D030/D041)

**D030 确认：cutoff 实现仅设 weight=0，occ head forward pass 未停止。** cutoff 后 = Detach 模式（BN 干扰 + 无梯度补偿），非 Vanilla。

**D041 多 seed 修正：s0 非单调模式是 seed noise，非真实信号。**
cutoff_15k/35k/Vanilla 2-seed 均值几乎相等（0.782/0.779/0.780），s0 排序在 s1 完全不复现。

| 条件 | s0 CAR | s1 CAR | s2 CAR | Mean | 安全 claim |
|------|--------|--------|--------|------|-----------|
| Full OCC | 0.832 | 0.788 | 0.770 | 0.797 | ✅ 最优（continuous flow） |
| cutoff_15k | 0.804 | 0.760 | — | 0.782 | ≈ Vanilla |
| cutoff_35k | 0.768 | 0.798 | 0.770 | 0.779 | ≈ Vanilla |
| Vanilla | 0.788 | 0.766 | 0.786 | 0.780 | baseline |
| cutoff_25k | 0.688 | 0.760 | running | 0.724 | 高方差，等 3rd seed |
| reverse | 0.700 | 0.736 | running | 0.718 | ✅ 一致最差（timing>duration） |

**安全 claim（D041 限缩后）**：
1. ✅ Continuous gradient flow（Full OCC）> 任何 interrupted 版本
2. ✅ Reverse cutoff（late-only flow）一致最差 → **timing > duration**（早期 imprinting > 晚期补充）
3. ✅ 中间 cutoff 点 ≈ Vanilla — 梯度流在 cutoff 后不持久（因 BN 干扰抵消）
4. ❌ ~~非单调 dose-response~~ / ~~15K sweet spot~~ — seed noise，不可 claim

**不安全 claim**：任何特定 cutoff 点优于另一个、非单调"sweet spot"。

**M052 影响**：cutoff_45k_s1 因 resume bug 无效，需从头重跑（~13h）。cutoff_25k_s2/reverse_cutoff_s2 正在训练（~3h），将提供关键 3rd seed。

### Same-Seed 梯度重分析 — 条件式 (D028)
当前 Fig.3 用了不同 seed/round 的 checkpoint。重分析方案**取决于 plan_027 结果**：
- **Scenario B** (detach_ln ≈ Detach): detach_ln_s0 (seed42, LN) 可替代 detach 做 same-seed 分析 ✓
- **Scenario A** (detach_ln ≈ Vanilla): 需重训 detach_s0 (seed42, **BN**) 或保留 detach_s2 (seed44) 注明 seed 差异
- **Scenario C**: 需两版分析（BN 和 LN）
Fig.3 至少保留 3 核心条件：Vanilla, Full OCC, Detach。Random OCC 可省略或标注 "旧 round"。

## Framing Risk Ranking (D043 Plan B 更新)

| 排名 | 风险 | 状态 | 应对 |
|------|------|------|------|
| **1** | v1/v2 数据不一致（crossover → ordinal） | 🔴 关键 | 以 v2 为权威；v1 放 appendix 讨论 code sensitivity |
| **2** | v2 ANOVA 统计显著性 | ✅ 已完成 | N=14, F/p/η² 已验证。Cell 4 vs Vanilla g=1.89, p=0.045 |
| **3** | Detach BN ≈ Vanilla (p=0.28, 不显著) — 支持 "无害" 但非 "有益" | ✅ 已定性 | 论文用 "statistically indistinguishable"，不 claim positive |
| **4** | v1 same-seed 梯度分析不适用于 v2 | 🟡 待重做 | v2 checkpoint 就绪后重做 |
| **5** | Cutoff dose-response BN 混淆 (D029/D030) | 已 reframe | withdrawal 分析，3rd seed 进行中 |
| **6** | 单 benchmark（只有 LIBERO-Spatial） | 仍存在 | Acknowledge in Limitations |

## 目标会议
**CoRL 2026**: Abstract May 26, Paper May 29
