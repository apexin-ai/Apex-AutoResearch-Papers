# Coverage Matrix Analysis — EMNLP 2026 ARR May 25

> 生成时间: 2026-05-15 09:30 UTC | Deadline: 2026-05-25 (10 天)

## 1. Core Claims → 实验覆盖矩阵

### Claim 1 (Primary): Dual-Constrained Adaptive b* — Minimum Intervention Principle

| 证据需求 | 实验 | 状态 | 结论 |
|----------|------|------|------|
| α_eff binding 比例统计 | Q1 micro-batch analysis | ✅ DONE | 40.1% α_eff binding, b*=1.67 vs ESS-only 4.15 |
| b* 轨迹分析 | adaptive_fix_seed42/123/456 step_metrics | ✅ DONE | b* 分布: mean 1.4, median 0.87, range [0, 20] |
| **ESS-only baseline head-to-head** | **ess_only_seed42** | **❌ QUEUED** | **CRITICAL GAP — 无法证明 min > max intervention** |
| ESS-only 多 seed 验证 | ess_only_seed123/456 | ❌ NOT PLANNED | 至少需要 1 seed, 3 seeds 更优 |

**覆盖率: 2/4 (50%)** — ESS-only baseline 是 Claim 1 最大漏洞。

### Claim 2 (Primary): Adaptive b* 免调参匹配 Grid-best

| 证据需求 | 实验 | 状态 | 结论 |
|----------|------|------|------|
| Adaptive ×3 seeds | adaptive_fix_seed42/123/456 | ✅ DONE | PPL: 17.65 / 17.643 / 17.66 |
| Grid-best ×3 seeds (b=0.5) | grid_b0_5_seed42/123/456 | ✅ DONE | PPL: 17.651 / 17.638 / 17.65 |
| Uniform ×3 seeds | uniform_seed42/123/456 | ✅ DONE | PPL: 17.69 / 17.69 / 17.70 |
| Grid landscape (all b × 3 seeds) | grid_b{0.5-5.0}_seed{42,123,456} | 🟡 RUNNING | seed42 全部 ✅; seed123 全部 ✅; seed456 b=2/3/5 RUNNING |
| Grid b<0.5 (确认 0.5 为 best) | grid_b_low_seed42 (b=0.1/0.2/0.3) | 🟡 RUNNING | ETA ~May 16 |

**覆盖率: 4/5 (80%)** — MVP PASS (D019, aggregate 88.6%). seed456 高 b 值即将完成，但 b=0.5 已确认为 best-b，不影响核心结论。

**主结果表 (已有数据)**:

| Method | seed42 | seed123 | seed456 | Mean |
|--------|--------|---------|---------|------|
| Uniform | 17.690 | 17.690 | 17.700 | 17.693 |
| Grid-best (b=0.5) | 17.651 | 17.638 | 17.650 | 17.646 |
| Adaptive (ours) | 17.650 | 17.643 | 17.660 | 17.651 |
| Δ(Adaptive vs Uniform) | -0.040 | -0.047 | -0.040 | -0.042 |
| Ratio (Adaptive/Grid-best) | 102.6% | 90.4% | 80.0% | 88.6% |

### Claim 3 (Setting): Unknown Contamination Proportion

| 证据需求 | 实验 | 状态 | 结论 |
|----------|------|------|------|
| τ 代码独立于 contamination_ratio | τ fix (D021) | ✅ DONE | τ=0.8 固定 CLI 参数, Reviewer PASS |
| **τ sensitivity sweep (0.5-0.9)** | **p0_tau_sweep** | **❌ NOT STARTED** | **需要证明 τ 不敏感** |
| 理论审计 (arXiv 2602.16065) | D025 | ✅ DONE | τ 降级为 empirical hyperparameter |

**覆盖率: 2/3 (67%)** — τ sweep 缺失削弱 "any reasonable τ works" 的论点。

### Ancillary: Lightweight Detector Sufficiency

| 证据需求 | 实验 | 状态 | 结论 |
|----------|------|------|------|
| TF-IDF+LR 可用 | detector_tfidf_lr | ✅ DONE | AUC=0.939, ECE=0.048 |
| Detector quality ablation | p1_detector_ablation | ❌ P1 (NOT STARTED) | 需不同 detector 强度对比 |

**覆盖率: 1/2 (50%)** — 缺 ablation 无法升级为 co-primary, 但作为 ancillary finding 可接受。

### n_min / batch_size Robustness (Reviewer Concerns)

| 证据需求 | 实验 | 状态 | 结论 |
|----------|------|------|------|
| n_min=2 vs 3 | adaptive vs adaptive_fix | ✅ DONE | n_min=3 clamped ESS, n_min=2 works |
| **n_min=1** | **nmin1_seed42** | **❌ QUEUED** | 测试过松 ESS 约束 |
| n_min=4 | p0_nmin4 | ❌ NOT STARTED | — |
| **batch_size=8** | **p0_batchsize_8** | **❌ NOT STARTED** | **证明方法不限于 bs=4** |
| **batch_size=16** | **p0_batchsize_16** | **❌ NOT STARTED** | **证明方法不限于 bs=4** |

**覆盖率: 1/5 (20%)** — batch_size 消融是审稿人最可能追问的点（当前 bs=4 + n_min=2, ESS 范围仅 [2,4]）。

### Positioning Baselines

| Baseline | 实验 | 状态 |
|----------|------|------|
| Uniform | ✅ 3 seeds DONE | — |
| Grid-b (6 values) | ✅ seed42 DONE, seed123 DONE, seed456 🟡 RUNNING | — |
| **Golden Ratio oracle** | **golden_ratio_seed42** | **❌ QUEUED** |
| **ESS-only adaptive** | **ess_only_seed42** | **❌ QUEUED** |
| Detect-and-remove | ❌ NOT PLANNED | P2 |
| DoReMi / DSIR | ❌ NOT PLANNED | P2 (domain-level, 不直接可比) |

---

## 2. Gap 清单（按优先级排序）

### 🔴 CRITICAL — 缺失将导致 reject

| # | Gap | 影响的 Claim | 预估 GPU 时间 | 预估 Wall 时间 |
|---|-----|-------------|-------------|--------------|
| G1 | **ESS-only baseline (≥1 seed)** | Claim 1 (核心) | ~3.5h | ~4h |
| G2 | **τ sweep (≥3 values: 0.6, 0.7, 0.8, 0.9)** | Claim 3 | ~14h (4 runs) | ~4h (并行) |

**没有 ESS-only baseline，Claim 1 "最小干预优于最大干预" 完全无证据。** 这是全文最关键的差异化论点。

**没有 τ sweep，Claim 3 的 "τ 不敏感" 只是断言，reviewer 可直接否定。**

### 🟡 HIGH — 缺失将导致 major revision / weak accept → reject

| # | Gap | 影响 | 预估 GPU 时间 |
|---|-----|------|-------------|
| G3 | **Golden Ratio oracle baseline** | Positioning (缺 oracle upper bound) | ~3.5h |
| G4 | **batch_size=8 或 16 (≥1)** | Robustness (bs=4 artifact concern) | ~3.5h |
| G5 | **n_min=1 和 n_min=4** | Robustness (hyperparameter sensitivity) | ~7h |

### 🟢 NICE-TO-HAVE — 加分但非必须

| # | Gap | 影响 | 预估 GPU 时间 |
|---|-----|------|-------------|
| G6 | 60% 污染比例 | Effect size amplification | ~7h |
| G7 | Detector quality ablation | Ancillary → co-primary | ~10h |
| G8 | Llama-3B | Model scale generalization | ~25h (D024 descoped) |
| G9 | Domain-skewed injection | Ecological validity | ~7h |
| G10 | ESS-only ×3 seeds | Statistical rigor for Claim 1 | ~7h |

---

## 3. 当前实验库统计

| 状态 | 数量 | 说明 |
|------|------|------|
| DONE (success) | 21 | 含 uniform×3, adaptive_old×3, adaptive_fix×3, grid-b seed42×6, grid-b seed123×6, grid-b seed456×3, detector×2, datagen |
| RUNNING | 4 | grid_b2/3/5_seed456 + grid_b_low_seed42 |
| QUEUED | 3 | golden_ratio, ess_only, nmin1 (all seed42) |
| KILLED | 4 | adaptive_v2×3 + diagnostic |
| **Total** | **32** | — |

---

## 4. 论文所需实验最小集 vs 当前状态

### 论文必须包含的表/图:

| 表/图 | 所需实验 | 状态 | 缺失 |
|-------|---------|------|------|
| **Table 1: Main Results** (uniform / grid-best / adaptive) | uniform×3, grid_b0_5×3, adaptive_fix×3 | ✅ 全部 DONE | — |
| **Table 2: Grid Search Landscape** (all b × 3 seeds) | grid_b{0.5-5.0}×3 seeds | 🟡 seed456 b=2/3/5 RUNNING | 数小时内完成 |
| **Table 3: Baselines** (+ Golden Ratio, ESS-only) | golden_ratio, ess_only | ❌ QUEUED | **G1, G3** |
| **Figure 1: α_eff / ESS dual constraint** | adaptive_fix step_metrics | ✅ 可从现有数据生成 | — |
| **Figure 2: b* trajectory** | adaptive_fix step_metrics | ✅ 可从现有数据生成 | — |
| **Figure 3: τ sensitivity** | τ sweep | ❌ NOT STARTED | **G2** |
| **Figure 4: n_min sensitivity** | n_min=1/2/3/4 | 🟡 2/3 done, 1/4 missing | **G5** |
| **Figure 5: batch_size ablation** | bs=4/8/16 | ❌ 仅 bs=4 | **G4** |

---

## 5. 时间评估：10 天是否足够

### GPU 资源
- 4× RTX 6000 Pro 96GB
- 剩余预算: ~85h (D024)
- P0 需求: ~82h

### 时间线估算

**Phase 1: 当前 RUNNING 完成 (May 15-16)**
- grid_b2/3/5_seed456: 已接近完成 (timestamps 显示 07:46 finished)
- grid_b_low_seed42: ETA May 16 ~05:00
- 释放 4 GPUs

**Phase 2: CRITICAL gaps (May 16-17, ~1 day)**
- GPU 0: Golden Ratio seed42 (~4h)
- GPU 1: ESS-only seed42 (~4h)
- GPU 2: τ=0.6 sweep (~4h)
- GPU 3: τ=0.7 sweep (~4h)
- → 释放后: τ=0.9 sweep + n_min=1 + n_min=4 + batchsize=8

**Phase 3: HIGH gaps (May 17-18, ~1 day)**
- n_min=1, n_min=4, batchsize=8 或 16
- ESS-only seed123 (如果 seed42 结果显著)

**Phase 4: 论文写作 (May 18-24, ~6 days)**
- 实验分析 + 图表生成: 1 day
- 论文初稿: 3 days
- 内部 review + 修改: 2 days

### 结论

**10 天足够完成 P0 实验 + 论文，但余量很紧。**

- ✅ CRITICAL gaps (G1, G2) 需 ~18h GPU + ~8h wall → **1 天可完成**
- ✅ HIGH gaps (G3-G5) 需 ~14h GPU + ~4h wall → **与 Phase 2 部分并行**
- ⚠️ 论文写作 6 天是最低估计，假设实验结果顺利
- ⚠️ 如果 ESS-only baseline ≈ dual-constraint (Key Risk #1)，需要 reframe，额外消耗 1-2 天

### 关键风险
1. **ESS-only 结果不利**: 如果 ESS-only ≈ dual，Claim 1 核心差异化消失，需 reframe 为 empirical study
2. **τ sweep 显示敏感**: 如果 τ 敏感，Claim 3 "dataset-agnostic default" 不成立
3. **GPU 故障/超时**: 当前已有多次超时/重跑经历，预留缓冲

---

## 6. 建议：投稿前必须完成的实验

### Must-Do (无这些不应提交):
1. **ess_only_seed42** — Claim 1 的唯一证据缺口
2. **τ sweep (至少 3 values)** — Claim 3 的唯一证据缺口
3. **golden_ratio_seed42** — Positioning 必需的 oracle baseline

### Should-Do (强烈建议):
4. **batch_size=8** — 回应 "bs=4 artifact" 质疑
5. **n_min=1 + n_min=4** — 超参数敏感性完整图

### 可跳过 (接受 limitation):
6. Llama-3B (D024 已 descoped)
7. Detector ablation (保持 ancillary)
8. 60% 污染 (nice-to-have)
9. Domain-skewed (P2)

---

## 7. 总体覆盖率

| Claim | 覆盖率 | 投稿风险 |
|-------|--------|---------|
| Claim 1 (Dual-constraint) | 50% | 🔴 HIGH — 缺 ESS-only baseline |
| Claim 2 (Match grid-best) | 80% | 🟢 LOW — MVP PASS |
| Claim 3 (Unknown proportion) | 67% | 🟡 MEDIUM — 缺 τ sweep |
| Ancillary (Detector) | 50% | 🟢 LOW — ancillary 可接受 |
| Robustness (n_min/bs) | 20% | 🟡 MEDIUM — 审稿人可能追问 |
| **Overall** | **~55%** | **⚠️ 需完成 G1-G3 才达到可投稿水平** |

完成 G1 (ESS-only) + G2 (τ sweep) + G3 (Golden Ratio) 后，overall 升至 ~75%，达到 EMNLP 可投稿门槛。
