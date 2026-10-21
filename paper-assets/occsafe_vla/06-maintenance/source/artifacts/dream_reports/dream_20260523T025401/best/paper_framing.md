# OccSafe-VLA — Paper Framing

> 维护者: Director | 最后更新: 2026-05-22 22:15 UTC | 状态: Draft (3-seed ablation complete, depth 4-seed complete, Path B confirmed (D022))

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

## Core Insight (D019 修正, 2026-05-22)

**原始假设（已部分推翻）**：BEV occupancy 迫使 vision encoder 发展 3D 空间感知 → safety emergence。

**D017 发现**：辅助任务的梯度流提供正则化效应。

**D019 修正后的 Core Insight**：VLA fine-tuning 中，辅助任务的**梯度流**是**必要条件**——
缺少梯度流（Detach）不仅无法提供正则化收益，反而**主动损害**模型的 collision avoidance（-3.4pp）
和 task execution 稳定性（TSR σ=0.163 vs <0.050）。梯度流条件（Full OCC, Random OCC）
保持与 Vanilla 可比的 CAR（差异 0.9-1.7pp，在 seed variance 内），
但不提供显著的正向收益。**梯度流是"防止损害"的必要条件，非"提供收益"的充分条件。**

BEV 空间内容仅有边际贡献（Full OCC 0.797 vs Random OCC 0.789，差异 0.8pp，在 σ≈0.031 内）。

**待验证**：Depth（egocentric, 与操作视角对齐）是否比 BEV（allocentric）和 Random 提供更有效的空间信号？

## Framing Strategy (D019 修正)

**确定路线: Option B 分析论文**（Reviewer 审查通过）

**核心叙事转变 (D019)**：从"梯度流提供正则化收益"→"梯度流是防止辅助 head 损害的必要条件"

**Title（暂定）**: "Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Mechanism Analysis"

**3-Contribution 结构（D019 修正）**：
- **C1 (核心发现)**: Auxiliary gradient flow 是防止 VLA safety 退化的必要条件
  - 正面证据: Full OCC/Random OCC ≈ Vanilla（梯度流不损害）
  - 反面证据: Detach < Vanilla（-3.4pp CAR, TSR σ=0.163 不稳定）
  - 空间内容次要: Full OCC ≈ Random OCC（0.8pp 差异，3 seeds each）
- **C2 (方法论贡献)**: 首个 5+ condition factorial study design for VLA safety mechanism analysis
- **C3 (实用贡献)**: 如果附加辅助 head，必须保留梯度流，否则会损害模型

## Core Contribution Evidence (D019 修正, 3-seed 数据)

### C1: Auxiliary Gradient Flow = Necessary Condition (Not Sufficient)

**Evidence (4 conditions @50K, 50r, all 3 seeds)**:
| 条件 | Seeds | TSR | CAR | vs Vanilla CAR |
|------|-------|-----|-----|---------------|
| Full OCC | 3 | 0.894±0.050 | **0.797**±0.032 | **+1.7pp** |
| Random OCC | 3 | 0.869±0.029 | 0.789±0.031 | **+0.9pp** |
| Vanilla | 3 | 0.907±0.009 | 0.780±0.012 | baseline |
| Detach OCC | 3 | 0.812±0.163 | 0.746±0.002 | **-3.4pp** |

**关键变化（D019 vs D017）**：
- Random OCC 3-seed 均值从 0.806 (2-seed) 降至 0.789 (3-seed)，s2 CAR=0.754 拉低
- Detach OCC 3-seed 暴露 TSR 不稳定性（s2 TSR=0.624，全面崩溃）
- Full OCC > Random OCC（翻转！2-seed 时 Random>Full，3-seed 后 Full>Random）
- 梯度流条件与 Vanilla 的差距缩小（0.9-1.7pp vs 之前 1.7-2.6pp），不再显著

**Detach 系统性弱点（per-task 分析，3 seeds）**：
- T3 CAR: 0.200, 0.140, 0.000 — 三 seed 均低，系统性失败
- T5 TSR: 0.340, 0.360, 0.160; CAR: 0.060, 0.040, 0.040 — 三 seed 均低
- s2 TSR 全面崩溃（10/10 tasks 均退化），但 CAR 不变（0.748 vs 0.746/0.744）

**Status**: ✅ 4 conditions 3-seed 数据齐全。Depth 4-seed complete, Path B confirmed (D022)。Cutoff eval 进行中。

### Claim 2 (Mechanism): Gradient Flow is Necessary
梯度流是辅助任务不损害 safety 的必要条件。Detach(0.746) < Vanilla(0.780) → 切断梯度流有害。
**新增**: Detach TSR 不稳定性（σ=0.163）进一步证实梯度流必要性。

### Claim 3: Spatial Content Secondary to Gradient Flow Presence
Full OCC (0.797) 和 Random OCC (0.789) 差异仅 0.8pp（3 seeds each），
远小于 Detach 退化（-3.4pp）。梯度流的存在/缺失是主要因素，空间内容次要。
**注意**: 3-seed 数据中 Full OCC > Random OCC（D017 时 Random > Full），
但差异太小不改变结论。

### Claim 4 (Depth Comparison): ✅ Confirmed (D022)
Depth CAR = 0.780 = Vanilla exactly (4 seeds), confirms spatial content is secondary to gradient flow.
Path B confirmed: egocentric depth supervision offers no advantage over no auxiliary supervision at all.

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
### RC3 [HIGH]: Depth Ablation — Pending results
### RC4 [MEDIUM]: Single VLA Architecture — Acknowledge in Limitations
### RC5 [MEDIUM]: Single Benchmark — Acknowledge in Limitations
### RC6 [LOW]: n=3 Statistical Power — Report Cohen's d and bootstrap CI

## Framing Risk Ranking (D019 更新)

| 排名 | 风险 | 概率 | 应对 |
|------|------|------|------|
| **1** | Depth ≈ Random ≈ OCC（空间内容完全无用） | 40-50% | 论文已转为"必要条件"分析，此结果强化叙事 |
| **2** | 高 seed 方差致条件间差异不显著 | 25-30% | Detach 退化是稳健发现；gradient-flow vs Vanilla 差异确实不显著 |
| **3** | Depth 结果异常 | 15-20% | Path C framing |
