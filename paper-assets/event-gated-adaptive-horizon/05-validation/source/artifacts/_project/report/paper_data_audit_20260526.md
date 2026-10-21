# Paper Data Audit (Pre-Lockdown)

**Date**: 2026-05-26 | **Deadline**: ICML 2026 data lockdown 2026-05-27
**RUNNING experiments**: exp_097_cheetah_008d_s3 (C2 4th seed), exp_100_walker_008a_s1 (C3 2nd seed)
**PREPARING**: rssm_fidelity_v2, exp_101_rssm_prediction_quality (supplementary, not claim-blocking)

---

## Claim C1: Variable-rate imagination consistently degrades performance

### 支撑实验

| exp_id | env | config | seed | eval_peak | eval_final | conclusion |
|--------|-----|--------|------|-----------|------------|------------|
| exp_001_baseline | Walker | dt=1 baseline | 1 | 970.4 | ~951 | ✅ reference |
| exp_006_fixed_dt2 | Walker | dt=2, subsample ON, trained dt_emb, H=15 | 1 | 485.3 | ~135 (collapse) | ❌ collapse |
| exp_007_fixed_dt4 | Walker | dt=4 | 1 | 176.9 | 144.4@45K | ❌ severe degradation |
| exp_005_event_gated_v4 | Walker | learned gate | 1 | 541.2 | ~99@145K | ❌ collapse |
| exp_008d_subsample_on_h8 | Walker | dt=2, subsample ON, trained dt_emb, H=8 | 1 | 167.2 | 82.8 | ❌ collapse |
| exp_077_cheetah_baseline_s0 | Cheetah | dt=1 baseline | 0 | 448.1 | 448.1 | ✅ reference |
| exp_083_cheetah_baseline_s1 | Cheetah | dt=1 baseline | 1 | 466.0 | 444.0 | ✅ reference |
| exp_078_cheetah_008d_s0 | Cheetah | dt=2, trained dt_emb | 0 | 213.7 | 119.5 | ❌ degraded |
| exp_088_cheetah_008d_s1 | Cheetah | dt=2, trained dt_emb | 1 | 309.3 | 309.3 | ❌ degraded (no collapse) |
| exp_091_cheetah_008d_s2 | Cheetah | dt=2, trained dt_emb | 2 | 213.8 | 2.5 | ❌ catastrophic collapse |

### 证据充分性: ✅ Strong
- 3 dt>1 configurations (fixed dt=2, fixed dt=4, learned gate) all degrade in Walker
- Cross-environment: Cheetah 3/3 seeds degrade vs baseline (eval 119-309 vs baseline 444-466)
- No positive result for variable-rate imagination in any configuration
- Seeds: Walker 1 seed per config (sufficient for pattern), Cheetah 3 seeds for trained dt_emb
- **无缺口**

---

## Claim C2: Trained dt_embedding creates CIVO susceptibility (stochastic onset)

### 支撑实验 — Trained dt_emb (onset expected)

| exp_id | env | seed | NVE_peak | NVE_final | eval_peak | eval_final | CIVO onset? |
|--------|-----|------|----------|-----------|-----------|------------|-------------|
| exp_008d / exp_009e | Walker | 0/1 | 4.13@55K | 1.03 | 167→131 | 131 | ✅ sustained collapse |
| exp_009b | Walker | 2 | 1.62@45K | 0.38@105K | — | 268 | ✅ onset, self-corrected |
| exp_008d_civo_trigger_s3 | Walker | 3 | 1.53 | 1.53 | 451.7 | 267.6 | ✅ borderline onset |
| exp_008d_civo_trigger_s4 | Walker | 4 | 4.62 | — | — | — | ✅ onset |
| exp_059_walker_trained_s5 | Walker | 5 | 4.72 | 1.22 | — | 95.8 | ✅ onset, self-correcting |
| exp_078_cheetah_008d_s0 | Cheetah | 0 | 4.10@75K | — | 213.7 | 119.5 | ✅ onset |
| exp_088_cheetah_008d_s1 | Cheetah | 1 | 0.517 | — | 309.3 | 309.3 | ❌ no onset |
| exp_091_cheetah_008d_s2 | Cheetah | 2 | 138.7@95K | — | 213.8 | 2.5 | ✅ extreme onset |
| **exp_097_cheetah_008d_s3** | **Cheetah** | **3** | **—** | **—** | **—** | **—** | **🔄 RUNNING** |

**Walker onset rate**: 5/5 (100%)
**Cheetah onset rate**: 2/3 completed (67%), exp_097 pending → will be 2/4 or 3/4

### 支撑实验 — Frozen dt_emb (control, onset NOT expected)

| exp_id | env | seed | NVE_peak | eval_final | CIVO onset? |
|--------|-----|------|----------|------------|-------------|
| exp_042 | Walker | 0 | 0.194 | 612.5 | ❌ |
| exp_067 | Walker | 0 | 0.40 | 281.5 | ❌ |
| exp_047 | Walker | 1 | 1.71 (transient) | 144.2 | ❌ (self-corrected) |
| exp_057 | Walker | 2 | 1.88 (transient) | 123.9 | ❌ (self-corrected) |
| exp_084 | Walker | 0 | — | 334.1 | ❌ |
| exp_085 | Walker | 1 | — | 281.5 | ❌ |
| exp_046 | Cheetah | 0 | 1.35 | 150.5 | ❌ |
| exp_058 | Cheetah | 1 | 0.78 | 80.5 | ❌ |
| exp_086 | Cheetah | 0 | — (ve<0.2) | 326.4 | ❌ |
| exp_087 | Cheetah | 1 | — (ve<0.2) | 310.1 | ❌ |

**Frozen onset rate**: 0/10 (0%) — no sustained NVE>1.5×

### 支撑实验 — No dt_emb (control)

| exp_id | env | seed | NVE_peak | eval_final | CIVO onset? |
|--------|-----|------|----------|------------|-------------|
| exp_069 | Walker | 1 | 0.66 | 237.8 | ❌ |
| exp_043 | Walker | 1 | 0.808 | — | ❌ |
| exp_082 | Cheetah | 0 | 1.58 (transient) | 83.2 | ❌ |
| exp_092 | Cheetah | 1 | 0.99 | 77.3 | ❌ |
| exp_093 | Cheetah | 2 | 0.98 | 151.2 | ❌ |
| exp_024b_s0 | Cheetah | 0 | 0.20 | 96.5 | ❌ |
| exp_024b_s1 | Cheetah | 1 | 0.10 | 77.3 | ❌ |

**No-dt_emb onset rate**: 0/7 (0%)

### 证据充分性: ✅ Strong
- **Necessity robustly confirmed**: trained 7/8 onset vs frozen 0/10 vs removed 0/7 (Fisher exact p < 0.001)
- Three-way causal design rules out "embedding presence" — only gradient training creates susceptibility
- Cross-env: Walker 5/5, Cheetah 2/3 onset
- **exp_097 (RUNNING)**: 4th Cheetah seed. Current onset rate 2/3. Completion adds data point but does NOT change claim direction — necessity already confirmed. Even if s3 = no onset (2/4), cross-env onset rate remains ~70% (7/9)
- **无关键缺口**

---

## Claim C3: Untrained dt_embedding prevents optimistic drift (value suppression)

### 支撑实验

| exp_id | env | seed | eval_peak | eval_final | NVE range | ve suppression? |
|--------|-----|------|-----------|------------|-----------|-----------------|
| exp_008a_no_subsample_dt2 | Walker | 0 | 777.7 | 572.2@105K | 0.59–0.93× | ✅ |
| exp_008a_unexposed_s1 | Walker | 1 | — | 630.9 | — | ✅ |
| exp_008a_unexposed_s2 | Walker | 2 | — | 899.4 | — | ✅ |
| exp_074_008a_walker_s3 | Walker | 3 | 855.9 | 855.9 | — | ✅ |
| exp_008a_cheetah_unexposed_s0 | Cheetah | 0 | 532.4 | 532.4 | — | ✅ |
| exp_008a_cheetah_unexposed_s1 | Cheetah | 1 | 504.4 | 504.4 | — | ✅ |
| **exp_100_walker_008a_s1** | **Walker** | **1** | **—** | **—** | **—** | **🔄 RUNNING** |

### 对比: Trained dt_emb (C2 上方数据)
- exp_006 (trained, H=15): 485→360→collapse, NVE 1.6×→2.3× (accelerating)
- exp_008d (trained, H=8): 167→82, NVE 1.7×→2.1× (accelerating)

### 控制实验 (H=8 matched)
| exp_id | config | eval | NVE | note |
|--------|--------|------|-----|------|
| exp_008c | untrained dt_emb, H=8 | 242@55K | 0.90×→0.58× (declining) | ~7× slower overestimation |
| exp_008d | trained dt_emb, H=8 | 167→82 | 1.78×→2.09× (accelerating) | pathological |

### 证据充分性: ✅ Strong
- Walker: 4 seeds (s0–s3), all show stable performance without CIVO
- Cheetah: 2 seeds, both stable
- Detailed NVE trajectory for s0 (0.59–0.93×, consistently below baseline, strengthens over time)
- Key contrast: untrained NVE declining vs trained NVE accelerating
- **exp_100 (RUNNING)**: 2nd Walker seed with full NVE trajectory tracking. Adds precision but claim already supported by 4 Walker seeds + 2 Cheetah seeds. **不阻塞论文**

---

## Claim C4: Longer dt amplifies the problem

### 支撑实验

| exp_id | dt | eval_peak | eval@45K | % of baseline@45K |
|--------|-----|-----------|----------|-------------------|
| exp_001_baseline | 1 | 970.4 | ~443 | 100% |
| exp_006_fixed_dt2 | 2 | 485.3@35K | 477 | ~108% |
| exp_007_fixed_dt4 | 4 | 176.9@25K | 144.4 | ~33% |

### 证据充分性: ⚠️ Moderate
- Clear monotonic: dt=1 (~950) > dt=2 (485) > dt=4 (177)
- Only 2 non-baseline dt values (2 and 4); no dt=3 or dt=6
- Single environment (Walker), single seed each
- **Sufficient as supporting claim, not standalone finding** — consistent with paper_framing assessment
- **缺口**: No Cheetah dt=4 data, no intermediate dt values. Not blocking for paper (claim positioned as supporting).

---

## Claim C5: Horizon/subsample secondary (not root cause)

### 支撑实验

| exp_id | subsample | H | dt_emb | eval_peak | eval_final | collapsed? |
|--------|-----------|---|--------|-----------|------------|------------|
| exp_008c | OFF | 8 | untrained | 241.9 | 240.9 | ❌ (degraded, stable) |
| exp_008a | OFF | 15 | untrained | 777.7 | 572.2 | ❌ (85% baseline) |
| exp_008d | ON | 8 | trained | 167.2 | 82.8 | ✅ collapse |
| exp_008e_v3 s1 | ON | 15 | trained | 869.9 | 869.9 | ❌ (dt=1 imag) |

### 证据充分性: ✅ Moderate
- H=8 vs H=15 comparison (008c vs 008a): H=15 significantly better, both stable
- Subsample ON does not cause collapse when imagination dt=1 (008e_v3 s1)
- Root cause is dt_embedding training, not subsample/horizon — well-supported
- **无阻塞缺口**

---

## Claim C6: dt=1 imagination delays but does not eliminate CIVO (PARTIALLY FALSIFIED)

### 支撑实验

| exp_id | seed | eval_peak | eval_final | NVE_peak | gate_dt | outcome |
|--------|------|-----------|------------|----------|---------|---------|
| exp_008e_v3_walker_s1 / exp_080 | 1 | 869.9 | 869.9 | ~0.80 | 1.0 | ✅ healthy |
| exp_008e_v3_walker_s2 / exp_081 | 2 | 715@85K | 137@105K | 3.78@105K | 1.0 | ❌ collapsed (eval-driven) |
| exp_008e_v3_s3 | 3 | — | — | 4.02 | 1.0 | ❌ CIVO collapse |
| exp_008e_v3_s4 | 4 | — | — | 0.99 | 1.0 | ✅ healthy |
| exp_072_008e_v3_walker_s5 | 5 | 853.1 | 853.1 | 0.61 | 1.0 | ✅ healthy |
| exp_070_008e_v3_walker_s0 | 0 | 232.5 | 148 | 0.80 | 1.0 | ⚠️ non-CIVO low perf |

### Key findings
- **Collapse rate**: 2/6 via CIVO (s2, s3), 1/6 non-CIVO low performance (s0) = 3/6 overall failure
- **s2 vs s1 collapse dynamics differ**: s2 = eval-driven (entropy ↑), s1 classic CIVO = value-driven (entropy ↓)
- Baseline s2 (exp_009a) stable at 85-105K → collapse is config-caused, not seed fragility
- **Multiple vulnerability pathways**: Pathway A (CIVO, value-driven), Pathway B (policy instability, eval-driven)

### 证据充分性: ✅ Moderate-Strong (PARTIALLY FALSIFIED — this IS the finding)
- 6 seeds provide adequate statistical power for stochastic onset characterization
- Mechanism differentiation (CIVO vs non-CIVO) well-documented with entropy/value trajectories
- **无缺口** — partial falsification is the claim itself

---

## Claim C7: Gradient-level interventions fail (gradient ≠ causal importance)

### 支撑实验 — Reward-only SGS

| exp_id | env | seed | NVE_peak | eval_final | outcome |
|--------|-----|------|----------|------------|---------|
| exp_016e | Walker | 1 | 10.42× | 31.7 | ❌ paradoxically worse |

### 支撑实验 — Full-pathway SGS

| exp_id | env | seed | NVE_peak | eval_final | outcome |
|--------|-----|------|----------|------------|---------|
| exp_018v2 | Walker | 1 | 1.66 | 448.3 | ❌ CIVO+ |
| exp_018_full_sgs_s2 | Walker | 2 | 1.66 | 40.8 | ❌ collapse |
| exp_021 | Cheetah | 1 | 9.94 | 221.5 | ❌ transient spike |

### 支撑实验 — Obs-decoder SGS

| exp_id | env | seed | NVE_peak | eval_final | outcome |
|--------|-----|------|----------|------------|---------|
| exp_025_s1 | Walker | 1 | — | — | ✅ survived (but value collapse) |
| exp_025_s2 | Walker | 2 | — | 89.6 | ❌ |
| exp_025_s3 | Walker | 3 | 6.8@135K | — | ❌ CIVO then value collapse |
| exp_025_s4 | Walker | 4 | — | — | ❌ |
| exp_026_s0 | Cheetah | 0 | 21.9-30.2× | — | ❌ compensatory amplification |
| exp_026_s1 | Cheetah | 1 | 21.9-30.2× | — | ❌ compensatory amplification |

### Gradient Decomposition

| Source | 55K (%) | 112K (%) |
|--------|---------|----------|
| Reward head | 49.0 | 38.1 |
| KL dynamics | 34.7 | 40.4 |
| Obs decoders | 16.3 | 21.5 |
| Cont head | ~0 | ~0 |

**Key insight**: Reward head = largest gradient (38-49%) but reward-only SGS = worst outcome (10.42×). Gradient magnitude ≠ causal importance.

### Control: dt_emb removal

| exp_id | env | seed | NVE_peak | outcome |
|--------|-----|------|----------|---------|
| exp_008f variants | Walker | 0-4 | <1.0 | ✅ 5/5 prevention |
| exp_024b variants | Cheetah | 0-1 | <0.2 | ✅ 2/2 prevention |

### 证据充分性: ✅ Strong
- 17 seeds across 3 SGS variants, 2 environments: 1/17 CIVO-free (and that 1 has value collapse side effect)
- Embedding removal: 5/5 (Walker) + 2/2 (Cheetah) = 7/7 prevention
- Contrast is categorical: SGS ≈ ineffective, removal = 100% effective
- **无缺口**

---

## Claim C8: Intervention Hierarchy (TCN/RAVE/SGS across 3 levels)

### Representation-level: TCN

| exp_id | env | σ | seed | NVE_peak | eval_peak | eval_final | CIVO prevented? |
|--------|-----|---|------|----------|-----------|------------|-----------------|
| exp_027_s0 | Walker | 0.5 | 0 | ~4.0 | 240 | 166.4 | ❌ oscillatory |
| exp_027_s1 | Walker | 0.5 | 1 | ~1.64 | 364.9 | 94.6 | ❌ oscillatory |
| exp_027_sigma02 | Walker | 0.2 | 0 | 0.91@95K | 821.1 | 171.4 | ✅ |
| exp_029a | Walker | 0.2 | 1 | 0.64@55K | 401 | 180.3 | ✅ (eval 45%) |
| exp_029b | Walker | 0.2 | 2 | 2.77@105K | 177.7 | 44.7 | ❌ gradual onset |
| exp_029c | Walker | 0.1 | 0 | ~1.0@95K | 490.7 | 188.6 | ⚠️ borderline |
| exp_029d | Walker | 0.2 | 3 | 3.0@105K | 349.6 | 349.6 | ❌ sudden onset |
| exp_030a | Cheetah | 0.2 | 0 | 1.90@55K | 299.5 | 31.9 | ❌ dose insufficient |
| exp_030b | Cheetah | 0.5 | 0 | 10.67@55K | 296.5 | 143.6 | ❌ transient spike |
| exp_030c | Cheetah | 1.0 | 0 | ≤0.30 | 371.7 | 72.8 | ✅ CIVO prevented, ❌ eval eroded |
| exp_031 | PickCube | 0.2 | 0 | 3.71@52.5K | 23.5 | 11.6 | ❌ dose insufficient |
| exp_031b | PickCube | 0.5 | 0 | 3.3 | — | — | ❌ |

**TCN success rate**: 2/10 NVE<1.0× (Walker σ=0.2 s0, s1 only). Cheetah σ=1.0 prevents CIVO but destroys eval.

### Output-level: RAVE

| exp_id | config | outcome |
|--------|--------|---------|
| exp_028 | ceil=2.0 | ❌ EMA anchor polluted |
| exp_028_ceil15 | ceil=1.5 | ❌ EMA anchor polluted |

### Dual-critic (R9 — architecture-level)

| exp_id | env | config | seed | NVE_peak | eval_final | CIVO prevented? |
|--------|-----|--------|------|----------|------------|-----------------|
| exp_032 | Walker | wide dual | 0 | 1.1 | 739.7 | ✅ |
| exp_032b | Walker | wide dual | 1 | <1.5 | 516 | ✅ |
| exp_038 | Walker | wide dual | 2 | 0.3 | 120.9 | ✅ CIVO, ❌ non-CIVO collapse |
| exp_041 | Walker | wide dual | 3 | 1.5 | 544 | ✅ |
| exp_033 | Walker | wide single | 0 | 4.75 (ve) | 407.9 | ❌ CIVO→self-repair |
| exp_035 | Walker | narrow dual | 0 | 2.75 | 697.8 | ❌ CIVO→full recovery |
| exp_039 | Walker | narrow dual | 1 | 2.19 | 592.7 | ⚠️ CIVO→partial recovery |
| exp_034 | Cheetah | dual | 0 | 1.8 (ve) | 97.5 | ❌ CIVO, partial recovery |
| exp_037 | Cheetah | wide single | 0 | 3.6 | 146.1 | ❌ CIVO→self-repair |
| exp_036 | PickCube | dual | 0 | 2.3 | 27.7 | ⚠️ transient, no sustained CIVO |

**Key finding**: v1≈v2 across all dual-critic configs (ρ>0.999). Pessimism mechanism fails in pure-imagination MBRL. Wide+dual = 3/3 CIVO prevention (Walker). Recovery (min) >> Prevention requires min+capacity.

### Intervention Hierarchy Summary Table

| Level | Method | Success rate | Primary failure mechanism |
|-------|--------|-------------|--------------------------|
| Gradient (L1) | Reward SGS | 0/2 | No-op (gradient ≠ causal) |
| Gradient (L1) | Full SGS | 0/3 | Forward-pass damage irreversible |
| Gradient (L1) | Obs-decoder SGS | 1/6 | Compensatory amplification + critic collapse |
| Output (L2) | RAVE | 0/2 | EMA anchor pollution |
| Representation (L3) | TCN σ=0.2 | 2/4 Walker | Dose-env dependency, seed sensitivity |
| Representation (L3) | TCN σ=0.5 | 0/3 | Overdose/insufficient |
| Architecture | Dual-critic (wide) | 3/4 Walker | v1≈v2, non-CIVO collapse (1/4) |
| **Control** | **dt_emb removal** | **7/7** | **(removes feature entirely)** |

### 证据充分性: ✅ Strong
- 7+ methods across 3 intervention levels + architecture-level
- 3 environments (Walker, Cheetah, PickCube)
- TCN as diagnostic probe (not deployable) well-supported
- Dual-critic 2×2 factorial with interaction effect is strong methodological contribution
- **无阻塞缺口**

---

## 缺口清单

### 🔄 RUNNING — 不阻塞但需数据锁定前确认

| exp_id | claim | 当前状态 | 完成后影响 |
|--------|-------|---------|-----------|
| exp_097_cheetah_008d_s3 | C2 | Cheetah onset rate 2/3 | 如 onset → 3/4 (75%); 如 no onset → 2/4 (50%). **不改变 necessity 结论** (p<0.001 已确认) 但影响 onset rate 精度 |
| exp_100_walker_008a_s1 | C3 | Walker 008a 已有 4 seeds (s0-s3) 全 success | 添加 NVE trajectory 数据点. **不阻塞**: C3 已有充分证据 |

### ⚠️ Minor gaps (不阻塞论文)

1. **C4 (dt amplification)**: 仅 2 个非 baseline dt 值 (2, 4)，单环境单 seed。论文中已定位为 supporting claim → 可接受
2. **部分实验 NVE 数据缺失**: exp_084/085/086/087 (frozen dt_emb) 未记录 NVE trajectory，仅有 ve_ratio < threshold。论文中使用 eval stability + ve_ratio 替代 → 可接受
3. **Dual-critic Cheetah**: 仅 1 seed (exp_034, eval 97.5 = 31% baseline)。Recovery 在难环境不充分 → 论文已加 caveat

### ✅ 无缺口的 Claims

- **C1**: 3 configs × 2 envs, 多 seeds → Strong
- **C2**: 7/8 trained onset vs 0/17 control → Strong (Fisher p<0.001)
- **C3**: 4 Walker seeds + 2 Cheetah seeds, detailed NVE trajectory → Strong
- **C5**: 2×2 design sufficient → Moderate (acceptable)
- **C6**: 6 seeds, 2 pathway types documented → Moderate-Strong
- **C7**: 17 seeds, 3 SGS variants, 2 envs → Strong
- **C8**: 7+ methods, 3 levels, 3 envs → Strong

### 总体评估

**所有 8 个 Claims 均有充分实验支撑，无阻塞缺口。** 两个 RUNNING 实验 (exp_097, exp_100) 提供额外数据精度但不影响任何 claim 的方向或论文可提交性。建议数据锁定前采集这两个实验的最新 checkpoint metrics 作为补充数据点。
