# Long Paper Results Summary

所有数字来自 registry 和 paper_framing.md 中标注的权威数据源。主表数据源: plan-012-full (11 tasks / 245 episodes)。

---

## Exp: plan-012 — Death Decomposition (CORE)

**目标**: 量化 death avoidance 在 routing signal 中的占比。

**关键数据**:
- N = 245 episodes, 11 task types
- Δ_full = +29.60, Δ_nd = +2.84, DAF = 90.41%
- Pearson r = 0.9698 (p = 8.12e-07), Spearman ρ = 0.986 (p = 2.4e-08)
- Bootstrap 95% CI for r: [0.952, 0.995]
- LOO range: r ∈ [0.963, 0.980]
- Death rates: internal 42.9%, deterministic 16.3% (2.6× ratio)
- Label distribution: 86 det-preferred / 9 internal-preferred / 150 no-preference
- Death-asymmetry labels: 75/95 non-tie labels (78.9%) — penalty-independent measure
- Exception: find-non-living-thing (n=40, zero deaths, Δ_full = +9.58, all non-death difference)
- Per-task DAF bimodal: find-non-living ≈ 0%, all others > 85%

**结论**: Death avoidance 贡献了约 90% 的 routing signal；非死亡性能差异小但非零 (Δ_nd/Δ_full = 9.6%)。

**支撑 Claim**: **C1** (death avoidance dominates routing signal)

---

## Exp: plan-013 — Labeling Quality Audit

**目标**: 验证 episode-level labels 无 tie-break artifacts。

**关键数据**:
- N = 245 episodes
- Tie rate: 61.2% (both-alive 46.9%, both-died 14.3%)
- 100% genuine labels, 0% tie-break artifacts
- Training labels breakdown: 70 death-asymmetry det + 16 score-comparison det + 5 death-asymmetry int + 4 score-comparison int = 95 total
- Strict retrain (death-asymmetry only) balanced acc: 57.29% (internal recall 75.76%, det recall 38.83%)
- Full retrain (ablation-b) balanced acc: 57.61 ± 0.47%
- Strict vs full: within 1σ, confirming score-comparison labels contribute negligible additional signal
- Step-level tie rate: 97.39% (6094 total steps, 5935 ties; 97.1% of ties are both-zero-delta)

**结论**: 标签管道无 oracle circularity 问题；所有 95 个训练标签均为 genuine。

**支撑 Claim**: **C2** (episode-level counterfactual labeling methodology)

---

## Exp: plan-004 — Explicit vs Implicit Router Ablation

**目标**: 对比 classification head 与 implicit (SFT) router 架构。

**关键数据**:
- Classification head (plan-004-v5, GA=1):
  - Logit-level: accuracy 74.5%, balanced acc 79.1%, internal recall 84.9%
  - Generation-level: accuracy 53.3%, balanced acc 41.5%, internal recall 26.7%
  - **Logit-generation gap**: logit 看似成功，generation 实际失败 — 核心架构问题
  - Thinking mode (on/off/strip) 结果完全一致，非根因
- Implicit router (ablation-b, GA=8, 4-seed):
  - Seed 42: balanced acc 59.27%, internal recall 51.52%
  - Seed 123: balanced acc 57.36%, internal recall 57.58%
  - Seed 456: balanced acc 57.48%, internal recall 75.76%
  - Seed 789: (data truncated in registry)
  - Mean balanced acc: 57–59%, internal recall varies 51.5–81.8%
  - GA fix: GA=1 → degenerate (internal recall 26.7%); GA=8 → non-degenerate (>50%)
- Conclusion: **negative** — 训练可行但 e2e 部署无法超越 always-det

**结论**: Logit-generation gap 暴露了 classification head 的根本架构缺陷；implicit router 非退化但 signal 太薄无法实用。

**支撑 Claim**: **C2** (router as diagnostic probe, not routing system)

---

## Exp: plan-011 — Rule-Based Routing Baseline

**目标**: 测试 keyword heuristic 能否提供 routing signal。

**关键数据**:
- v1 (generic verbs incl. connect/disconnect): match rate 85.8% → degenerate always-det
- v2 (science-only: heat/boil/melt/freeze): match rate 4.9% → degenerate always-internal
- v3 (relaxed): match rate 2.8%, episode accuracy 1.5% → degenerate always-internal
- Root cause: ScienceWorld actions 使用通用交互动词 (connect/move/pick up)，不含 science-specific keywords

**结论**: Keyword heuristic 在 ScienceWorld 上结构性失败；支持 learned/observation-based approaches 的必要性。

**支撑 Claim**: **C1** (支撑论据 — 简单 heuristic 无法替代)

---

## Exp: plan-003 — End-to-End Baselines (245 episodes)

**目标**: 建立 unconditional strategy baselines 和 trained router 对比。

**关键数据**:
- Always-Internal: score = -39.07, 95% CI [-46.40, -32.27], death 42.9%
- Always-Deterministic: score = -9.47, 95% CI [-14.71, -4.29], death 16.3%
- Random: score = -22.38, 95% CI [-28.67, -15.75], death 27.8%
- Oracle: score = -6.58, 95% CI [-11.54, -1.70], death 14.3%, 96.3% decisions = always-det
- Trained Router (4-seed mean): score = -10.70, 95% CI [-16.33, -5.27], death 17.6%
  - sim_ratio = 97.0% (几乎全部路由到 det)
  - fallback_rate = 70.6% (173/245 episodes 无 step data → fallback to det)
  - delta vs always-det = -1.23 (worse, but CI overlapping → not statistically significant)

**结论**: Oracle degeneracy (96.3% = always-det) 表明 episode-level optimal routing ≈ unconditional deterministic。Trained router 未显著超越 always-det。

**支撑 Claim**: **C1** (death avoidance dominance → oracle degeneracy), **C2** (router as diagnostic, not practical system)

---

## Exp: math-negative-contrast — MATH 300-problem Negative Contrast

**目标**: 在无 death penalty 环境中测试 routing signal 是否消失/反转。

**关键数据**:
- N = 300 problems (Level 4: 152, Level 5: 148)
- Internal accuracy: 81.7%, 95% CI [77.3%, 86.0%]
- Code interpreter accuracy: 76.7%, 95% CI [72.0%, 81.3%]
- Diff: +5.0% (internal > code), CI [+0.7%, +9.3%], statistically significant
- Labels: 266 no-preference / 25 internal-preferred / 9 det-preferred
- Contingency: both correct 215, both wrong 40, only-internal 30, only-code 15
- Level 5 gap: +6.1% (internal advantage larger on harder problems)
- Filtered (no code execution): 82 problems

**结论**: Signal reversal — 无 death penalty 时 internal > code interpreter，确认 death avoidance thesis。

**支撑 Claim**: **C3** (cross-domain negative contrast)

---

## Exp: alfworld-counterfactual-full — ALFWorld Exploratory

**目标**: 在另一个 text-based environment 中探索 routing signal。

**关键数据**:
- N = 135 games, 6 task types
- Det success rate: 27.4%, Internal success rate: 3.0%
- Labels: 35 det-preferred (25.9%), 2 internal-preferred (1.5%), 98 no-preference (72.6%)
- Det advantage massive but mechanism differs from ScienceWorld

**结论**: Deterministic advantage 来自 action space pruning (admissible action filtering)，而非 death avoidance。与 ScienceWorld 机制性不同，作为对比案例使用。

**支撑 Claim**: **C3** (cross-domain contrast — different mechanism)

---

## Exp: plan-012-penalty-sensitivity — Penalty Sensitivity Analysis

**目标**: DAF 对 death penalty magnitude P 的敏感性。

**关键数据**:
- N = 245 episodes
- Death count: only-int-dies 70, only-det-dies 5, both-die 35, neither-die 135
- δ (death rate differential) = 0.2653
- Δ_nd = 3.07 (includes both-died in non-death pool)
- Δ_full(P) = δ·P + Δ_nd (linear in P)

| P | Δ_full(P) | DAF(P) |
|---|-----------|--------|
| 10 | 5.72 | 46.4% |
| 25 | 9.70 | 68.4% |
| 50 | 16.33 | 81.2% |
| 100 | 29.60 | 89.6%* |
| 200 | 56.13 | 94.5% |

*Default setting. Note: DAF=89.6% here (both-died included in Δ_nd=3.07) vs 90.41% in main text (strict neither-died filtering, Δ_nd=2.84).

**结论**: DAF 单调递增于 P — 数学性质而非经验发现。Penalty-independent companion metric (78.9% death-asymmetry labels) 更有说服力。

**支撑 Claim**: **C1** (robustness check for DAF)

---

## Summary Table

| Experiment | N | Core Metric | Result | Claim |
|---|---|---|---|---|
| plan-012 (Death Decomp) | 245 eps / 11 tasks | DAF | 90.41% | C1 |
| plan-013 (Labeling Audit) | 245 eps | Genuine label % | 100% | C2 |
| plan-004 (Router Ablation) | 306 val steps | Balanced acc | 57–59% (4-seed) | C2 |
| plan-011 (Rule-Based) | 233 eps | Match rate extremes | 85.8% or <5% | C1 |
| plan-003 (Baselines) | 245 eps | Oracle degeneracy | 96.3% = always-det | C1 |
| math-negative-contrast | 300 problems | Internal − Code | +5.0% (reversed) | C3 |
| alfworld-full | 135 games | Det success rate | 27.4% vs 3.0% | C3 |
| penalty-sensitivity | 245 eps | DAF range | 46.4%–94.5% | C1 |
