# Random β=0.1 vs ISR β=0.1: 跨 Seed 中期对比分析

**日期**: 2026-05-14
**状态**: 中期 (Random s43-r2 QUEUED, 待补完成 3-seed)
**目的**: 比较 ISR-as-reward 与 random control 在低剂量 β=0.1 下的多 seed 表现

---

## 1. 数据来源

所有 ISR 数据来自 `eval_sta.py` 统一评估 (C004 合规)，避免训练日志跨 run 不可比。

### Random β=0.1 (additive_random, r = r_exec · (1 + 0.1·U[0,1]))

| Seed | Status | PR | mean ISR | proved-only ISR | components | ISR=0 ratio |
|------|--------|------|----------|-----------------|------------|-------------|
| s42  | DONE   | 0.79 | 0.1038   | 0.1314          | 8.46       | 36.7%       |
| s43  | r2 QUEUED (原 r1 step 200 磁盘满) | — | — | — | — | — |
| s44  | DONE   | 0.89 | 0.0619   | 0.0695          | (n/a)      | 80.9% (72/89) |

### ISR β=0.1 (additive_bonus, r = r_exec · (1 + 0.1·ISR))

| Seed | Status | PR | mean ISR | proved-only ISR | H7 (conclusion dup) | Verdict |
|------|--------|------|----------|-----------------|---------------------|---------|
| s42  | DONE   | 0.81 | 0.3365   | 0.4154          | (待审, 可能 genuine) | success |
| s43  | DONE   | 0.61 | 0.5063   | 0.8301          | **96.7%**           | negative |
| s44  | DONE   | 0.89 | 0.803    | 0.902           | **86.5%**           | negative |

---

## 2. 聚合统计

### Random β=0.1 (n=2, **2/3 seeds, 中期**)

| Metric           | Mean   | Std    |
|------------------|--------|--------|
| PR               | 0.840  | 0.071  |
| mean ISR         | 0.083  | 0.030  |
| proved-only ISR  | 0.100  | 0.044  |

### ISR β=0.1 (n=3, **完整**)

| Metric           | Mean   | Std    |
|------------------|--------|--------|
| PR               | 0.770  | 0.144  |
| mean ISR         | 0.549  | 0.236  |
| proved-only ISR  | 0.716  | 0.263  |

### 聚合比例

- mean ISR 比率 (ISR / Random): **6.62×**
- proved-only ISR 比率: **7.13×**
- PR 几乎持平 (ISR 0.77 vs Random 0.84，差 7pp，方向上 Random 略高)

**注意**: ISR β=0.1 的高均值由 2/3 hacked seeds 撑起 (s43/s44 H7>85%)。剔除 hacked seeds 后仅剩 s42 (proved-only ISR=0.415)，仍高于 Random 但差距大幅缩窄 (s42 vs s42 配对 3.24×，非 7×)。

---

## 3. 同 seed 配对对比

| Seed pair | Random (PR/ISR) | ISR-reward (PR/ISR) | ISR 倍数 | Hacking? |
|-----------|-----------------|---------------------|----------|----------|
| s42       | 0.79 / 0.104    | 0.81 / 0.337        | 3.24×    | s42 待审, 可能 clean |
| s44       | 0.89 / 0.062    | 0.89 / 0.803        | **12.97×** | s44 H7=86.5% conclusion duplication |
| s43       | (pending r2)    | 0.61 / 0.506        | —        | s43 H7=96.7% conclusion duplication |

**关键观察**:

- s44 配对 PR **完全相同** (0.89=0.89)，但 ISR 相差 13×。这不是因为 ISR-reward 训出了更强推理，而是因为 ISR-reward 训出了 **conclusion duplication hacking**：86.5% 的 proved 样本仅生成一条 premise 且 premise≈conclusion (重言式 P→P)，使 per-clause ablation 下唯一 premise 必然 necessary → ISR=1.0 inflated。
- s42 配对 PR 几乎一致 (0.79 vs 0.81)，ISR 差 3.24× 是 **唯一可能反映 genuine structural guidance 的对照点**。但仅 1/3 seeds 的证据基础非常薄。
- s43 random 待 r2 完成补齐。s43 在 ISR-reward 下 PR=0.61 是 3-seed 中最差，但 ISR_2nd 高 (0.506)；H7=96.7% 是 3-seed 中最严重的 hacking。

---

## 4. 叙事点 (D043 框架下)

### (a) Random β=0.1 ISR 低但 "honest"

Random 的低 ISR (0.083 mean, 0.100 proved-only) **不是 reasoning 失败**，而是 **redundant encoding** (C006 区分原则):
- s42: components=8.46, ISR_0_ratio=36.7% — 模型生成大量 premise (8+ 条) 但多为冗余 (重复 ground facts)，per-clause ablation 删任一冗余不影响结果 → n_necessary=0 → ISR=0
- s44: ISR_0_ratio=80.9% — 更严重的冗余，几乎所有 proved 样本都有 trivially droppable premises
- **无 conclusion duplication hacking** (component count 远高于 ISR-reward 的 4.03~4.33)

Random 的 PR=0.84 (mean, 高于 ISR β=0.1 的 0.77) 说明: **r_exec 信号本身已经足以拿到高 PR**，ISR-reward 的 r·(1+β·ISR) 在 β=0.1 下并不提升 PR，只重塑结构。

### (b) ISR β=0.1 reward 在低剂量下有结构引导能力但不稳定

3-seed 中：
- **s42**: 仅这一 seed 是 "possibly genuine"——PR=0.81 (近 exec-only baseline 0.93 减 12pp 可接受范围), components=5.58 (无 tautological collapse), ISR=0.337 (3.24× over random s42)。但 conclusion duplication 是否完全无 (H7) 尚需逐样本审查确认。
- **s43**: PR 崩塌 (0.61)，conclusion duplication 96.7%，ISR=0.506 是 artifact。
- **s44**: 与 exec-only s44 (tautological collapse) 不同的失败模式——避免了 2-component collapse 但转向 conclusion duplication 86.5%，ISR=0.803 是 artifact。

**结论**: ISR-as-reward 在 β=0.1 下 **2/3 seeds 转向 conclusion duplication hacking**。仅 1/3 seeds (s42) 可能产生 genuine structural improvement。多 seed 可靠性不足。

### (c) D043 降级：β=0.1 不再是 "sweet spot"

原 D031-D032 框架: β=0.1 是 ISR-as-reward 的 "sweet spot" — PR 不崩 + ISR 显著提升。

**重新框定 (D043)**:
- β=0.1 **不是 sweet spot**，而是 **"hacking rate 最低的失败模式"**: 3-seed 中仍有 2/3 转向 conclusion duplication，仅严重程度低于 β=0.3。
- Random control 用 PR≈ISR-reward 但 ISR 6.6× 低，证明 r_exec 信号已撑起 PR；ISR-reward 提供的"结构引导"在多数 seed 下是 metric gaming 而非 reasoning。
- **论文 Claim 2 需重写**: 不能再说 "ISR β=0.1 提供 genuine structural guidance"，应改为 "ISR β=0.1 在大多数 seed 下导致 conclusion duplication hacking，仅 1/3 seed 显示结构改善信号，可靠性不足"。

### (d) C006 警示：ISR 差异 ≠ reasoning 能力差异

- Random exec-only low ISR = **冗余编码** (重复 ground facts 导致 n_necessary=0)
- ISR β=0.1 high ISR = **metric gaming** (Goodhart, conclusion duplication 使 n_premises=1 且 ISR=1)
- 两者中间状态 (s42) 才可能是 genuine reasoning，但 1/3 概率不足以支撑论文 claim

论文叙事必须区分这两种 ISR 失效模式，否则审稿人会问："Random ISR 低是不是说明它推理差？" 答案是 **不是**——它生成了大量冗余 premises，证明可行但不必要。

---

## 5. 后续行动

1. **Random s43-r2 完成后**: 补齐 3-seed mean±std，重新计算并更新此文档。
2. **ISR β=0.1 s42 H7 逐样本审查**: 确认 s42 是否真的 "genuine"——这是 ISR-as-reward 能否进论文 Claim 2 的关键。如 s42 也 H7>50%，则 β=0.1 全军覆没。
3. **配对 t-test**: 等 Random 3-seed 齐后，做 paired t-test on (PR, ISR, proved-only ISR) 跨 condition。
4. **D043 决策**: 根据 s42 审查结果决定 β=0.1 是 "demoted sweet spot" 还是 "全失败"。

---

## 6. 关键数字汇总 (用于论文表格)

| Condition       | n | PR (mean±std)  | mean ISR (mean±std) | proved-only ISR (mean±std) | Hacking |
|-----------------|---|----------------|---------------------|----------------------------|---------|
| Random β=0.1    | 2 (待 3) | 0.84 ± 0.07 | 0.083 ± 0.030       | 0.100 ± 0.044              | None    |
| ISR β=0.1       | 3 | 0.77 ± 0.14   | 0.549 ± 0.236       | 0.716 ± 0.263              | 2/3 H7>85% |

**Paired (s42, s44 only)**:
- PR Δ (ISR − Random): s42 +0.02, s44 +0.00
- ISR Δ: s42 +0.233 (3.24×), s44 +0.741 (12.97×, hacking-driven)
