# LIBERO Spatial Benchmark — 完整对比分析框架

> 生成日期: 2026-05-14
> 状态: 模板（待实验完成后填入最终数据）

---

## 1. 六路对比总表

| Method | Type | K | Overall SR | 备注 |
|--------|------|---|-----------|------|
| VLA-only (baseline) | Single inference | 1 | **30.0%** (30/100) | 已完成 |
| VLA Mean Action | Multi-sample mean | 10 | **___%** | eval-vla-mean-spatial |
| SampleConsensus (ReconVLA-style) | Scalar Euclidean argmin | 10 | **___%** | eval-reconvla-spatial-v3 |
| Scalar CRM | 3D scalar uncertainty + CRM | 10 | **___%** | eval-scalar-unc-spatial |
| ACR-VLA (K=5) | Per-DOF CRM | 5 | **___%** | eval-k5-spatial |
| ACR-VLA (K=10) | Per-DOF CRM | 10 | **___%** | eval-acr-spatial-v2 |
| **竞品参考** | | | | |
| ACoT-VLA (CVPR'26) | Training-time CoT | - | 98.5% (LIBERO) | 非 LIBERO-Plus; training-time 方法 |
| SRPO | Training-time RL | - | 82.1% (LIBERO-Plus) | 不同 benchmark split |

### Per-Task 详细数据

| Task | Difficulty | VLA K=1 | VLA Mean K=10 | SampleCons K=10 | Scalar CRM K=10 | ACR K=5 | ACR K=10 |
|------|-----------|---------|---------------|-----------------|-----------------|---------|----------|
| bowl_next_ramekin | Easy | 100% | | | | | |
| bowl_next_cookie_box | Easy | 90% | | | | | |
| bowl_between_plate | Easy | 60% | | | | | |
| bowl_cookie_box | Medium | 20% | | | | | |
| bowl_next_plate | Medium | 30% | | | | | |
| bowl_table_center | Hard | 0% | | | | | |
| bowl_top_drawer | Hard | 0% | | | | | |
| bowl_on_ramekin | Hard | 0% | | | | | |
| bowl_on_stove | Hard | 0% | | | | | |
| bowl_wooden_cabinet | Hard | 0% | | | | | |

难度分级: Easy (baseline ≥50%), Medium (20-49%), Hard (baseline <20%)

---

## 2. 关键分析维度

### 2.1 Overall Success Rate Ranking

```
Rank | Method            | SR   | Δ vs baseline
-----|-------------------|------|-------------
  1  |                   |      |
  2  |                   |      |
  3  |                   |      |
  4  |                   |      |
  5  |                   |      |
  6  | VLA-only K=1      | 30%  | —
```

### 2.2 Per-Task Correction 获益/受损分析

**从 correction 获益的 tasks** (method > baseline):
| Task | Baseline | Best Method | Δ | 可能原因 |
|------|----------|-------------|---|---------|
| | | | | |

**被 correction 伤害的 tasks** (method < baseline):
| Task | Baseline | Worst Method | Δ | 可能原因 |
|------|----------|--------------|---|---------|
| | | | | |

关键问题: correction 是否伤害了 easy tasks（过度纠正）而只在 hard tasks 上帮助？

### 2.3 分层分析: Easy / Medium / Hard

| Difficulty | # Tasks | VLA K=1 Avg | VLA Mean K=10 | SampleCons K=10 | Scalar CRM K=10 | ACR K=5 | ACR K=10 |
|-----------|---------|-------------|---------------|-----------------|-----------------|---------|----------|
| Easy (≥50%) | 3 | 83.3% | | | | | |
| Medium (20-49%) | 2 | 25.0% | | | | | |
| Hard (<20%) | 5 | 0.0% | | | | | |

核心观察模板:
- Easy tasks: correction 应保持高性能（不伤害），如果大幅下降说明 CRM 过度校正
- Medium tasks: correction 最有潜力提升的区间
- Hard tasks: baseline 为 0%，任何提升都是 pure gain；但如果仍为 0%，说明问题不在 action noise 而在 task comprehension

### 2.4 Per-DOF vs Scalar 直接对比

| Metric | ACR-VLA (Per-DOF) K=10 | Scalar CRM K=10 | Δ | p-value |
|--------|------------------------|-----------------|---|---------|
| Overall SR | | | | |
| Easy Avg | | | | |
| Medium Avg | | | | |
| Hard Avg | | | | |
| # Tasks improved vs baseline | | | | |
| # Tasks degraded vs baseline | | | | |

如果 Δ < 5%: 参考 paper_framing.md 备选策略 — story 重心从 "per-DOF > scalar" 转向 "structured uncertainty features enable principled correction"。

### 2.5 K Sensitivity (K=5 vs K=10)

| Metric | ACR K=5 | ACR K=10 | Δ |
|--------|---------|----------|---|
| Overall SR | | | |
| Easy Avg | | | |
| Medium Avg | | | |
| Hard Avg | | | |

预期: K=10 > K=5（更多样本 → 更好的 covariance 估计），但 paper_framing 提到 K=10 vs K=5 衰减约 15pp。
如果 K=5 ≈ K=10: 实际效率优势，可强调 "仅需 K=5 即可获得大部分收益"。

### 2.6 Multi-Sampling Contribution Isolation

| | K=1 (no sampling) | Mean K=10 | Best Method K=10 |
|--|-------------------|-----------|------------------|
| Overall SR | 30.0% | | |
| Δ from K=1 | — | | |

分解:
- **Multi-sampling gain** = Mean K=10 - VLA K=1 (纯粹来自多次采样 + 平均)
- **Correction gain** = Best CRM K=10 - Mean K=10 (来自 learned correction 的增量)
- **Selection gain** = SampleConsensus K=10 - Mean K=10 (来自 sample selection 的增量)

如果 multi-sampling gain 占主导: 说明多次采样本身已很有价值，CRM 的增量贡献需要诚实报告。

---

## 3. Claim 验证 Checklist

### Claim 1: Per-DOF > Scalar

> "Per-DOF conformal features enable dimension-selective correction... 比标量 uncertainty 提供显著更好的 action correction"

| 验证项 | 数据源 | 结果 | Pass? |
|--------|--------|------|-------|
| ACR-VLA K=10 > Scalar CRM K=10 (overall) | eval-acr-spatial-v2 vs eval-scalar-unc-spatial | ___% vs ___% | |
| 差距 ≥ 2% (kill criterion from paper_framing) | 同上 | Δ = ___% | |
| Per-task: ACR 在多数 tasks 上优于 scalar | 逐 task 对比 | _/10 tasks | |
| Per-DOF 在 hard tasks 上优势更大 | 分层对比 | | |

Kill criterion: Δ < 2% → Claim 1 不成立，需 reframe。

### Claim 2: ACR-VLA > Baseline

> "ACR-VLA improves base VLA success by X%"

| 验证项 | 数据源 | 结果 | Pass? |
|--------|--------|------|-------|
| ACR-VLA K=10 > VLA K=1 (overall) | eval-acr-spatial-v2 vs baseline | ___% vs 30% | |
| ACR-VLA 不伤害 easy tasks | per-task 对比 | Easy avg: ___% vs 83.3% | |
| ACR-VLA 改善 hard tasks | per-task 对比 | Hard avg: ___% vs 0.0% | |

**中间检查 RED FLAG**: 上次中间结果 ACR-VLA 23.3% < baseline 30%。如果最终结果确认，这是 critical failure。

### Claim 3: Learned CRM > Sample Selection

> "CRM 可以合成更优动作... selection 失效时 CRM 可以合成更好的动作"

| 验证项 | 数据源 | 结果 | Pass? |
|--------|--------|------|-------|
| ACR-VLA K=10 > SampleConsensus K=10 | eval-acr-spatial-v2 vs eval-reconvla-spatial-v3 | ___% vs ___% | |
| Per-task: ACR 在多数 tasks 上优于 SC | 逐 task 对比 | _/10 tasks | |
| Hard tasks: CRM 合成优于 best sample | 分层对比 | | |

**中间检查 RED FLAG**: 上次中间结果 SampleConsensus 42.9% >> ACR-VLA 23.3%。如果确认，Claim 3 完全反转。

---

## 4. 应急 Framing 方案

### 场景 A: ACR-VLA < Baseline (当前中间结果趋势)

**根因假设 (需逐条排查)**:
1. CRM 过拟合训练分布，在 spatial tasks 上产生有害校正
2. Conformal intervals 在 spatial 特定 tasks 上 miscalibrated
3. CGS covariance 估计在某些 DOF 组合上不稳定
4. 训练数据与 spatial benchmark 的分布偏移太大

**Framing 策略**:
- 不能 claim "ACR-VLA improves spatial tasks"
- 转向: "ACR-VLA 的 correction magnitude 需要 task-specific 校准" — 分析 CRM 在哪些 tasks 上帮助/伤害
- 如果 SampleConsensus > all: 论文 narrative 转为 "multi-sample uncertainty 本身有价值，learned correction 是 harder problem than sample selection"
- 如果 VLA Mean > VLA K=1: 至少可以 claim "multi-sampling improves robustness"
- 最坏情况: spatial 作为 "challenging case study"，重心放在其他 benchmarks (LIBERO-Plus)

### 场景 B: Per-DOF ≈ Scalar (Δ < 5%)

参考 paper_framing.md:
- Story 重心从 "per-DOF > scalar" 转向 "structured uncertainty features enable principled correction"
- 强调整体框架（residual + uncertainty + online adaptation）的组合优势
- Per-DOF 作为 "principled design choice" 而非 "empirically dominant"

### 场景 C: SampleConsensus 最高

**这是最棘手的场景** — 直接挑战 "learned correction > sample selection" 的核心 claim。

策略:
1. 分析 SampleConsensus 赢在哪些 tasks — 是否是 "easy tasks 本来就好，selection 不伤害" 的 artifacts?
2. 在 hard tasks 上如果 CRM 仍优于 SC → "CRM 在高难度场景下更优，SC 在简单场景靠不犯错取胜"
3. 检查 SampleConsensus 是否 benefit from multi-sampling (vs Mean K=10) — 如果 SC ≈ Mean，说明 selection 策略本身不重要
4. 最后手段: "在 spatial benchmark 上 sample quality 已足够好，selection 即够用；在更 challenging 的 LIBERO-Plus 上 CRM 的合成能力才显现价值"

### 场景 D: 全部 methods < Baseline

说明 K-sampling + 任何 aggregation 都不如单次推理 → 根本性问题:
- 可能 flow-matching 的最佳样本不在 mean/mode 附近
- 可能 spatial tasks 的 action distribution 高度 multimodal，averaging/correction 都有害
- 这会是 honest negative result，仍有发表价值但需要完全重新 frame

---

## 5. 竞品对比 Context

### LIBERO 标准 benchmark 参考值

| Method | LIBERO (标准) | LIBERO-Plus | 来源 |
|--------|--------------|-------------|------|
| ACoT-VLA | **98.5%** | **84.1%** | arXiv:2601.11404, CVPR'26 |
| SRPO | — | **82.1%** | paper_framing.md |
| SC-VLA | — (ManiSkill 86%) | — | arXiv:2602.21633 |
| VLA-Pilot | — | — (real-world OOD 50%) | arXiv:2511.14178 |
| ReconVLA | — (具体 SR 未公开) | — | arXiv:2604.16677 |

**重要注意**: 
- 竞品数字大多来自不同 benchmark split (LIBERO vs LIBERO-Plus vs LIBERO-Spatial)，不可直接比较
- ACoT-VLA 98.5% 是标准 LIBERO (含 4 个 suite)，我们只跑了 spatial suite (10 tasks)
- 我们的 baseline VLA 本身性能较低 (30% on spatial)，说明 base model 能力是主要瓶颈

### 定位策略

- **vs ACoT-VLA**: "Training-time 方法，与 ACR-VLA 正交互补。ACR-VLA 可叠加在更强的 base VLA 上"
- **vs ReconVLA**: "同为 inference-time CP 方法，但 scalar UQ + selection vs per-DOF UQ + learned correction"
- **vs SC-VLA**: "需要 task-specific RL 训练，我们是 plug-and-play"
- **不要试图在 absolute numbers 上与 ACoT-VLA 98.5% 比较** — base VLA 不同，benchmark split 不同

---

## 6. 数据填写指南

当 5 个 eval 实验完成后:

1. **收集数据**: 从各 eval 目录读取 per-task success rate
2. **填写第 1 节总表和 per-task 表**
3. **计算第 2 节各分析维度**
4. **逐条检查第 3 节 claim checklist** — 每条标注 Pass/Fail
5. **根据第 4 节确定 framing** — 选择匹配的场景
6. **输出最终分析报告** → `artifacts/spatial_final_analysis.md`

---

## Appendix: 实验 ID 映射

| 实验 ID | Method | Config |
|---------|--------|--------|
| eval-acr-spatial-v2 | ACR-VLA per-DOF CRM | K=10 |
| eval-reconvla-spatial-v3 | SampleConsensus | K=10, scalar Euclidean argmin |
| eval-scalar-unc-spatial | Scalar CRM | K=10, 3D uncertainty |
| eval-k5-spatial | ACR-VLA | K=5 |
| eval-vla-mean-spatial | VLA Mean Action | K=10, no conformal |
| eval-spatial-v7-full | VLA-only baseline | K=1 |
