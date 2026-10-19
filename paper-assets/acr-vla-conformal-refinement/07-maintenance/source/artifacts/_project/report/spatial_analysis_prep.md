# Spatial Ablation Analysis & Paper Narrative Preparation

> 生成时间: 2026-05-15 | 状态: 分析备忘录（等待全 10 task 完成后裁决）

## 1. 当前数据快照

### Spatial Benchmark（ROADMAP 2026-05-15 03:08 UTC）

| 实验 | Mode | Tasks 完成 | 当前 SR | 来源 |
|------|------|-----------|---------|------|
| VLA baseline (K=1) | vla_only | locked | **30%** | ROADMAP baselines |
| VLA-mean (K=10) | vla_only mean | locked | **31%** | ROADMAP baselines |
| argmin-only | reconvla | 8/10 | **37.5%** | ROADMAP spatial eval |
| perdof CRM | acr_vla, norm=0.1 | 5/10 | **42.0%** | ROADMAP spatial eval (v4-small) |
| obs_only CRM | crm_obs_only, norm=0.1 | 4/10 | **57.5%** | ROADMAP spatial eval (obs-only-r2) |
| scalar CRM | crm_scalar, norm=0.1 | 2/10 | **80%*** | ROADMAP spatial eval (*easy tasks only) |

**注意**: 任务描述中的数字（perdof 42.9%, obs_only 40.0%, scalar 56.7%@3 tasks）与 ROADMAP 不一致。以 ROADMAP 为准，但两者均为中间结果，任何中间排序均可能在剩余 tasks 翻转。

### 关键增量

| 对比 | 增量 | 统计可信度 |
|------|------|-----------|
| CRM (any) vs argmin-only | +4.5pp (perdof) 至 +20pp (obs_only) | 低: 4-5/10 tasks |
| argmin-only vs VLA baseline | +7.5pp | 中: 8/10 tasks |
| 全 pipeline vs VLA baseline | +12pp (perdof) 至 +27.5pp (obs_only) | 低: 不同 task counts |

### 数据可靠性警告
- **obs_only** 仅 4/10 tasks，当前领先可能因 task selection bias 翻转
- **scalar** 仅 2/10 tasks 且均为 easy tasks，80% 完全不可信
- **perdof** 5/10 tasks，D025 已将 D019 "52.5%" claim 标记为失效
- 所有 CRM variant 排序必须等全 10 tasks 完成

---

## 2. 三种 Narrative 分析

### Scenario A: perdof > obs_only（per-DOF story）

**触发条件**: 全 10 task 后 perdof SR > obs_only SR 且差 ≥5pp

**可能性评估**: **低**。当前 obs_only (57.5%@4) 大幅领先 perdof (42.0%@5)。需要剩余 tasks 中 obs_only 大幅下滑且 perdof 追上。训练 loss 也支持 obs_only（val_loss 0.0165 vs perdof 0.0358，见 D020）。

**Narrative**: "Per-DOF conformal features encode dimension-specific uncertainty that observation features cannot capture. Despite worse training loss, conformal features' epistemic signal proves critical under distribution shift in closed-loop deployment."

**各章节影响**:

| 章节 | 内容重点 |
|------|---------|
| **Intro** | 开门见山：scalar UQ 丢失维度信息 → per-DOF conformal features 是解决方案。Problem 聚焦 "information loss in scalar aggregation" |
| **Method** | CGS multivariate CP + per-DOF interval extraction 是核心技术贡献。CRM 架构强调 40D conformal feature vector 的设计。Magnitude control 作为工程发现 |
| **Results** | 主表: 4-way ablation 展示 perdof > obs_only > scalar ≈ argmin。亮点故事: "training loss 预测翻转" (obs_only lower loss but worse eval) = compelling evidence for epistemic value |
| **Discussion** | 强调 conformal features 在 distribution shift 下的 epistemic value 与 in-distribution training loss 的 divergence。与 ReconVLA scalar CP 对比突出信息增益 |

**风险**: 如果 perdof 仅略优于 obs_only (3-5pp)，统计显著性不足，narrative 说服力弱。

---

### Scenario B: perdof ≈ obs_only ≈ scalar（correction-is-key story）

**触发条件**: 全 10 task 后三种 CRM variant 两两差 <5pp

**可能性评估**: **中**。如果 obs_only 在剩余 tasks 下滑，三者可能收敛到 40-50% 区间。

**Narrative**: "Learned uncertainty-conditioned correction (sample-then-refine) significantly outperforms pure sample selection. The correction mechanism is the contribution, not the specific feature representation."

**各章节影响**:

| 章节 | 内容重点 |
|------|---------|
| **Intro** | Problem: 现有方法止步于 sample selection (ReconVLA) 或需 RL 训练 (SC-VLA)。Gap: 缺少 lightweight learned correction。Our angle: CRM 作为 plug-and-play correction module |
| **Method** | CRM 架构设计 + magnitude control 是核心贡献。Per-DOF features 作为 "one valid feature set" 呈现，不强调其必要性。重点放在 correction mechanism 设计原则（bounded residual, norm control） |
| **Results** | 主表: CRM (any variant) vs argmin-only 的增量。Feature ablation 作为次要表 "CRM is robust to feature choice"。Magnitude control study (norm sensitivity) 升级为独立 contribution |
| **Discussion** | "Correction > selection" 作为主要 takeaway。与 residual policy learning 文献 (Silver 2018, PLD, TRANSIC) 建立联系。Per-DOF 保留用于 online monitoring (future work) |

**优势**: 这是最稳健的 narrative——只要 CRM vs argmin-only ≥5pp 即可成立。不依赖特定 feature variant 排序。
**风险**: Contribution novelty 降低——"learned correction helps" 不够新颖。需要用 magnitude control discovery 和 CoRL 实验规模补偿。

---

### Scenario C: obs_only > perdof（simpler-is-better / observation-conditioned story）

**触发条件**: 全 10 task 后 obs_only SR > perdof SR 且差 ≥5pp

**可能性评估**: **较高**。当前数据 (57.5% vs 42.0%) + 训练 loss (0.0165 vs 0.0358) 均支持此方向。D025 已预警此趋势。

**Narrative**: "Observation-conditioned learned residual correction is the key contribution. Conformal features provide no additional value as CRM input over observation features, but remain valuable for sample selection quality and coverage monitoring."

**各章节影响**:

| 章节 | 内容重点 |
|------|---------|
| **Intro** | Problem 保持不变（VLA robustness gap）。Gap: 缺少 inference-time learned correction。Our angle: lightweight observation-conditioned residual correction，不需要额外 UQ features |
| **Method** | CRM 架构 + magnitude control 是核心。CGS/conformal 降为 "sample selection module" 的理论基础，不再是 CRM feature。需要解释 per-DOF features 的 negative result |
| **Results** | 主表: obs_only CRM vs argmin-only vs baselines。Feature ablation 如实呈现——conformal features 不优于 observation features 作为 honest negative result。Per-DOF 在 sample selection 中的角色仍可报告 |
| **Discussion** | 解释可能原因: (1) 观测特征已隐含编码 uncertainty 信息 (2) conformal 特征在小 K 下噪声大 (3) CRM 容量足以从观测中学到校正方向。将 per-DOF 定位为 "future direction: larger K + better calibration" |

**Core Insight 需重写**: "Lightweight learned residual correction on selected VLA samples significantly improves robustness. The correction module only needs observation features; structured uncertainty features are not required."

**优势**: 实际上简化了 method 和 story——不需要解释复杂的 multivariate CP 管线作为 CRM 输入。
**风险**: (1) 论文标题 "ACR-VLA" 中 "conformal" 角色弱化；(2) 与 A2C2 (Sendai 2025) 的差异化缩小——都变成了 "observation-conditioned residual correction"；(3) Reviewer 可能质疑 "你们做了这么复杂的 CP pipeline 结果没用？"

**子情况 C1**: scalar > perdof 但 scalar < obs_only → conformal feature 形式无关紧要，进一步支持 "correction mechanism is key" narrative（hybrid of B+C）

---

## 3. 待完成实验及其对 Narrative 选择的影响

| 实验 | 当前状态 | ETA | 对 narrative 的影响 |
|------|---------|-----|-------------------|
| **Spatial 全 10 task** (bjb1-18228) | 4-8/10 tasks | ~6-9h | **决定性**: 全部排序确认后才能选择 A/B/C |
| **Object benchmark 全 10 task** (bjb1-32546) | 刚开始 | ~数小时 after spatial | **验证性**: cross-benchmark consistency。如果 spatial B 但 object A → narrative 困难 |
| **Magnitude sweep** (norm ∈ {0.03, 0.05, 0.2, 0.3}) | 未开始 | 待 bjb2-28827 部署 | **补充性**: 强化 magnitude control contribution (所有 scenario 均可用) |
| **K sensitivity sweep** (K=5,10,15,20) | 未开始 | 待 GPU 释放 | **补充性**: 回应 Reviewer Q1 (K=10 covariance reliability) |
| **Fisher exact test** | 需全 10 task 数据 | post-eval | **统计性**: 判断增量是否 p<0.05 |

**裁决所需最低数据**: Spatial 全 10 task + Object 全 10 task。两个 benchmark 均显示 CRM vs argmin ≥5pp (p<0.05) 才能安全 claim。

---

## 4. CoRL 8 页单 Claim 论文结构建议

### 推荐结构（CoRL 2026, 8 pages + references）

| 章节 | 页数 | 内容 |
|------|------|------|
| **Abstract** | — | 一句 problem, 一句 method (sample-then-refine + CRM), 一句 headline result |
| **1. Introduction** | 1.0 | Problem (VLA robustness gap) → Existing approaches (selection/RL/MLLM) → Gap (no lightweight learned correction with statistical grounding) → Contribution (CRM + magnitude control + empirical findings) |
| **2. Related Work** | 0.75 | (a) VLA robustness: training-time (RobustVLA, DiG-Flow, SRPO, ACoT) vs inference-time (ReconVLA, SC-VLA, VLA-Pilot, A2C2) (b) CP in robotics (c) Residual policy learning |
| **3. Method** | 2.0 | 3.1 Multi-sample inference + CGS (0.5p) → 3.2 Conformal sample selection (0.5p) → 3.3 CRM architecture + feature variants (0.5p) → 3.4 Magnitude control (0.5p) |
| **4. Experiments** | 2.5 | 4.1 Setup: LIBERO-Plus spatial+object, SmolVLA backbone, baselines (0.5p) → 4.2 Main results: headline table (0.5p) → 4.3 Feature ablation: 4-way comparison (0.5p) → 4.4 Magnitude sensitivity study (0.5p) → 4.5 Analysis: per-task breakdown, failure modes (0.5p) |
| **5. Discussion & Limitations** | 0.75 | Sim-only, K=10 overhead, feature choice insights, future directions |
| **6. Conclusion** | 0.25 | 2-3 sentences |
| **References** | ~1.5 (不计入) | ~30-35 refs |

### 单 Claim 论文的关键策略

1. **Claim 必须够强**: "CRM correction ≥5pp over argmin-only on BOTH benchmarks" 是最低门槛。单 claim 论文缺乏 "至少有一个 claim 成立" 的安全网。

2. **Ablation 表做得像 multi-claim**: 4-way feature ablation + magnitude sweep + K sensitivity = 3 个独立分析维度。即使只有一个 claim，实验深度可以补偿。

3. **Magnitude control 升级为独立 contribution**: norm=1.42 → 0% vs norm=0.1 → 42-57.5% 的发现是 novel empirical insight（来源: D019）。这在所有 scenario 下都成立，可作为论文的 "second punch"。

4. **Negative result 如实呈现**: 如果 per-DOF 不优于 obs_only (Scenario B/C)，Table 中如实展示比隐藏更好——Reviewer 会欣赏 thorough ablation。

5. **与 ReconVLA 的对比是必须的** (paper_framing.md Reviewer Q6)。argmin-only baseline 已经是 ReconVLA 的近似（conformal selection without correction），但需要在论文中明确声明这一对应关系。

### 各 Scenario 下的标题候选

| Scenario | 标题方向 |
|----------|---------|
| A (perdof wins) | "ACR-VLA: Dimension-Selective Action Correction via Per-DOF Conformal Features" |
| B (all similar) | "Sample-then-Refine: Uncertainty-Conditioned Learned Correction for Robust VLA Deployment" |
| C (obs_only wins) | "Learned Residual Correction Improves VLA Robustness: A Conformal Selection + Observation-Conditioned Refinement Pipeline" |

---

## 5. 决策依赖与时间线

```
May 15 (NOW)
  ├── Spatial eval running (ETA ~6-9h)
  ├── Object eval running (ETA ~hours after spatial)
  └── This memo prepared

May 16 (Day 2)
  ├── Spatial 全 10 task 完成 → 初步排序
  ├── Object 初步结果
  └── ★ Narrative 初步选择 (A/B/C)

May 17-19 (Day 3-5)
  ├── Object 全 10 task 完成
  ├── Fisher exact test on both benchmarks
  ├── Magnitude sweep (if GPU available)
  └── ★ Narrative 最终锁定 + paper_framing.md 更新

May 20-24 (Day 6-10)
  ├── Paper writing (8 pages)
  ├── Figures: main results table, ablation, magnitude curve
  └── Per-task breakdown analysis

May 25-26 (Day 11-12)
  ├── Abstract 提交 (May 26 DDL)
  └── Continue full paper for Jun 2 DDL
```

---

## 6. Scenario-Specific 风险矩阵

| 风险 | Scenario A | Scenario B | Scenario C |
|------|-----------|-----------|-----------|
| Novelty 挑战 | 低 (per-DOF is novel) | 中 (correction alone less novel) | 中-高 (需与 A2C2 差异化) |
| Statistical power | 需 perdof-obs_only ≥5pp | 只需 CRM-argmin ≥5pp | 需 obs_only-argmin ≥5pp |
| Reviewer "so what?" | 低 | 中 (加 magnitude control) | 中 (conformal pipeline "wasted"?) |
| 论文完成复杂度 | 高 (需解释 loss-eval 反直觉) | 低 (最直白) | 中 (需优雅处理 negative result) |
| Title/branding 一致性 | 最佳 (ACR = conformal features) | 可接受 | 差 (ACR 中 conformal 角色弱化) |
