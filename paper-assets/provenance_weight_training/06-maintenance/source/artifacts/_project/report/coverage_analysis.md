# Coverage Analysis — provenance_weight_training
> Generated: 2026-05-15 16:00 UTC
> Deadline: EMNLP ARR May 25 (10 days)
> Overall coverage: **10/34 experiments done (29.4%)**

---

## Per-Claim Coverage Summary

| Claim | Done | Total | Coverage | Running | Critical Gaps |
|-------|------|-------|----------|---------|---------------|
| Claim 1 (dual-constraint necessity) | 3 | 12 | 25.0% | 0 | batch_size ablation, n_min=4/5 |
| Claim 1+2 (shared) | 1 | 6 | 16.7% | 0 | 60% contamination pipeline |
| Claim 2 (adaptive vs grid) | 4 | 10 | 40.0% | 0 | grid_b_low rerun |
| Claim 2+3 (shared) | 1 | 1 | 100% | 0 | — |
| Claim 3 (τ robustness) | 1+1neg | 5 | 20.0% | 4 | τ sweep completion |

---

## Claim 1: Dual-Constraint Necessity (α_eff + ESS)

### Evidence Available ✅
| Experiment | Result | Significance |
|-----------|--------|-------------|
| ess_only_seed42 | PPL=17.730 (vs adaptive 17.650) | **+0.08 PPL gap**: dual > ESS-only (min-intervention > max-intervention) |
| nmin1_seed42 | PPL=17.789 (vs adaptive 17.650) | n_min=1 over-downweights (b_star_mean=7.2, 46.7% batch b*≥2) |
| adaptive_fix ×3 seeds | PPL=17.650/17.643/17.660 | n_min=2 consistently best |
| detector_tfidf_lr | AUC=0.939, ECE=0.048 | Lightweight detector sufficiency established |

### Evidence Missing ❌

**P0 — Must Have:**
1. **p0_nmin_4** (PREPARING) — n_min=batch_size boundary case, should → uniform-equivalent. 完成 n_min sensitivity curve (1,2,3,4)
2. **p0_nmin_5** (planned) — degenerate case, confirms uniform equivalence. 可酌情降优先级（n_min=4 已足够说明）
3. **p0_batchsize_8** (planned) — 证明 n_min knife-edge 是 batch_size=4 的 artifact
4. **p0_batchsize_16** (planned) — 证明 larger batch → ESS 约束放松，b* 更稳定
5. **ESS-only multi-seed** (ess_only_seed123 PREPARING) — 增加 ESS-only 对比的统计可信度

**P1 — Nice to Have:**
- p1_detector_modernbert + p1_detector_ablation_training — AUC→PPL 关系
- p1_baseline_random_reweight — detector signal 的因果性验证
- p1_llama3b_uniform — 3B model baseline

### Assessment
**核心证据到位**: ESS-only baseline 证明 dual > ESS-only (+0.08 PPL)。n_min sensitivity 有 3 个点 (1,2,3)，4 和 5 补完即成 full curve。
**关键缺口**: batch_size ablation 完全空白——reviewer concern "only batch_size=4" 无法回应。

---

## Claim 2: Adaptive b* 免调参匹配 Grid-best ★★★★★

### Evidence Available ✅
| Experiment | Result | Significance |
|-----------|--------|-------------|
| adaptive_fix ×3 seeds | PPL=17.650/17.643/17.660 | 3-seed consistency |
| grid_b ×3 seeds (b=0.5 best) | PPL=17.651/17.638/17.650 | Grid-best established at b=0.5 |
| golden_ratio_seed42 | PPL=17.654 | Oracle baseline, adaptive competitive |
| MVP Path B | Aggregate ratio 88.6% | ✅ PASS |

### Evidence Missing ❌

**P0 — Must Have:**
1. **p0_grid_b_low ×3 seeds** — ⚠️ **CRITICAL**: seed42 FAILED (infra bug)，seed123/456 未开始。若 grid-best 在 b<0.5，当前 Claim 2 数据基础动摇。**必须重跑确认 b=0.5 确是全局最优**
2. **p0_grid_b_low_eval** — 依赖上述完成
3. **p0_contamination_60_grid_b0_5** — 60% 条件下 grid 参考点（依赖 datagen）

**P1:**
- p1_baseline_detect_remove — hard filtering baseline

### Assessment
**MVP 已 PASS，但有致命隐患**: grid_b_low 未完成意味着不确定 b=0.5 是否为 grid 最优。如果 b=0.2 或 b=0.3 更好，adaptive 可能实际劣于 grid-best。**必须在 deadline 前完成 grid_b_low**。

---

## Claim 3: τ Robustness ★★☆☆☆

### Evidence Available ✅
| Experiment | Result | Significance |
|-----------|--------|-------------|
| adaptive_fix_seed42 (τ=0.8) | PPL=17.650 | Baseline |
| tau_06_seed42 (τ=0.6) | PPL=17.681 | ❌ NEGATIVE (+0.031 vs baseline) |
| τ fix validation | τ 独立于 contamination_ratio | Claim 3 前提已验证 |

### Currently Running 🔄
| Experiment | Status |
|-----------|--------|
| tau_05_seed42 | RUNNING |
| tau_07_seed42 | RUNNING |
| tau_09_seed42 | RUNNING |
| tau_095_seed42 | RUNNING |

### Evidence Missing ❌
- τ sweep 结果（等 4 个 running 完成即可）
- p1_cross_generator_datagen/training (P1, 可选)

### Assessment
**核心实验正在跑**，预计数小时内完成。τ=0.6 已 negative（PPL 劣于 baseline），但 delta 仅 0.031。若 τ=0.7/0.9 都在 17.650±0.05 范围内，仍可声称 "τ=0.7-0.9 robust range"。关键是 τ=0.7 和 τ=0.9 的结果。

---

## Cross-Claim: 60% Contamination Pipeline

**状态**: 完全未启动。p0_contamination_60_datagen 是 blocker，下游 3 个 P0 实验全部依赖它。

| Experiment | Claim | Status | GPU Hours |
|-----------|-------|--------|-----------|
| p0_contamination_60_datagen | 1+2 | planned | 4.0 |
| p0_contamination_60_uniform | 1 | planned | 3.6 |
| p0_contamination_60_adaptive | 1+2 | planned | 3.6 |
| p0_contamination_60_grid_b0_5 | 2 | planned | 3.6 |

**总 GPU 时间**: ~14.8h (串行 datagen → 并行 3 training)
**论文价值**: "效应随污染比例放大" 是说服 reviewer "small effect size" concern 的关键证据。

---

## P0 Gap Priority Ranking (Deadline-Critical)

| Priority | Experiment | Claim | Est. Hours | Rationale |
|----------|-----------|-------|------------|-----------|
| **P0-1** | grid_b_low ×3 seeds (rerun) | 2 | 11h×3 | 不确认 grid-best 位置，Claim 2 有翻车风险 |
| **P0-2** | τ sweep (wait) | 3 | already running | 等待即可，无需额外 GPU |
| **P0-3** | 60% contamination pipeline | 1+2 | 14.8h | "small effect size" 主要防御线 |
| **P0-4** | batch_size=8/16 ablation | 1 | 7.2h | 回应 "only bs=4" reviewer concern |
| **P0-5** | n_min=4 (wait) | 1 | PREPARING | 完成 sensitivity curve |
| **P0-6** | ESS-only seed123 (wait) | 1 | PREPARING | 多 seed 增加可信度 |

### GPU Time Budget
- **P0 总需求**: ~33h（grid_b_low 占大头）
- **10 天 deadline, 假设 4 GPU**: 理论上 960 GPU·h，但需留 margin 给重跑和 eval
- **可行性**: 充裕，但 grid_b_low 必须立即启动避免再次 infra 问题

---

## Recommendations

1. **立即启动 grid_b_low 重跑** — Claim 2 的地基，不能等
2. **立即启动 60% datagen** — unblock 整个 contamination pipeline
3. **τ sweep 等待** — 4 个已在跑，预计今天出结果
4. **batch_size ablation 排第二批** — grid_b_low 和 datagen 跑完后启动
5. **n_min=5 可降优先级** — n_min=1/2/3/4 四个点已足够，n_min=5 是 degenerate case（与 n_min=4 行为相同）

### Risk Flags
- ⚠️ **τ=0.6 negative**: 如果 τ=0.5/0.7 也 negative，Claim 3 需收窄为 "τ=0.8-0.9 optimal range"
- ⚠️ **grid_b_low 重跑**: 如果 b=0.3 比 b=0.5 好，Claim 2 的 aggregate ratio 需重算
- ⚠️ **60% pipeline 未启动**: 如果 GPU 被占，可能来不及完成 → Limitations 需说明 "single contamination ratio"
