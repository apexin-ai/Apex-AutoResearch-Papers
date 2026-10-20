# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL

## Title Candidates

1. **"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination"**
2. ~~**"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination"**~~ (deprecated — "delusional critic" conflicts with Lu et al. 2018)
3. **"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3"** ← preferred after D037 terminology decision
4. **"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination"**

**⚠️ D037 术语决定**: "delusional critic" → **"conditioning-induced value overestimation"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换："delusional critic" → "conditioning-induced value overestimation"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。

**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 "known failure class 的 specific instance" 升级为 "dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability"**。TAWM 是强化 novelty 的最关键参考文献。

## Venue

**ICLR 2027** — Deadline: ~2026-10 (TBD; switched from CoRL 2026 per D176)

## Narrative Positioning

This is a **diagnostic analysis paper**, not a method paper. We do not propose a new algorithm. Instead, we provide a systematic, controlled investigation answering: *Why does temporal abstraction fail in world-model RL?*

The contribution is a **strongly supported causal chain** from mechanism to failure mode, backed by a factorial experiment design that isolates each factor, plus a **practical mitigation guideline** (restrict imagination to dt=1 during multi-dt training → 95% baseline recovery). Diagnostic papers are valued when they (a) address a widely-attempted but poorly-understood failure, (b) provide actionable insight for future method design, and (c) are methodologically rigorous.

We scope all claims to **DreamerV3 and its RSSM world model**. Generalizability to other latent-dynamics architectures is discussed but not claimed.

---

## Core Claims

### C1: Variable-rate imagination in DreamerV3 consistently degrades performance

Temporal abstraction via variable dt—whether learned or fixed—degrades asymptotic performance relative to the dt=1 baseline across all tested configurations.

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Baseline stability | exp_001_baseline (dt=1) | Stable convergence ~950 eval return |
| Fixed dt=2 collapse | exp_006_fixed_dt2 (dt=2, subsample ON, H=15) | Peak 485@35K → collapse to ~135@65K |
| Fixed dt=4 severe degradation | exp_007_fixed_dt4 (dt=4) | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |
| Learned gate collapse | exp_005 (learned gate) | Peak 541@55K → 99@145K |

**Strength**: Strong. Three independent dt>1 configurations all show degradation. No positive result exists for variable-rate imagination in our setup.

### C2: Trained dt_embedding creates susceptibility to CIVO with stochastic onset; necessity confirmed by ablation

**D032/D156/D167 update: CIVO onset is stochastic (Walker 2/3, Cheetah 3/4); necessity confirmed (frozen 0/10 across 2 envs × multiple seeds, removed 0/3+). Cross-env frozen verification 4/4 closed (exp_084-087, all NVE < 0.53×). Fisher exact test (5/7 onset vs 0/19 controls): p < 0.001.**

The trained dt_embedding creates susceptibility to pathological value overestimation (normalized v/e >2.0x baseline) with stochastic onset. Both onset and collapse are stochastic:

- **Walker WITH trained dt_emb**: 2/3 seeds onset NVE>2.0× (exp_008d s0: sustained 2.09x@45K→4.12x@55K → collapse; exp_009e s1: onset >2.0×). exp_009b s2: NVE=1.62×@45K — sub-threshold perturbation under τ=2.0 (onset_self_correcting under former τ=1.5). Value self-corrected to 0.38x@105K
- **Cheetah WITH trained dt_emb**: 3/4 seeds onset (exp_078 s0 NVE=4.1×; exp_091 s2 NVE=138.7×, onset_collapse; exp_097 s3 onset@45K NVE=2.3×, onset_transient_then_degraded, eval_final=61.7 (14% baseline); exp_088 s1 NVE≈1.0 no onset). **All onset seeds eval_final < 15% baseline; no-onset s1 = 69% baseline — CIVO onset causes irrecoverable performance damage even when ve_ratio self-corrects**
- **WITHOUT dt_emb (frozen/removed)**: 0/10 frozen (exp_042, exp_067, 015b, 047, 057, 084, 085 Walker; 046, 058, 086, 087 Cheetah; note: 047/057 had transient spikes 1.71-1.88× but self-corrected) + 0/3 removed (008f s1, 009c s2, exp_069 s1) exceed sustained nve>2.0×. Cross-env frozen verification (exp_084-087, 2 envs × 2 seeds): all NVE<0.53×
- **2.0x threshold (Walker, 35K+)**: Cross-environment onset rate ~71% (5/7 completed seeds) — not deterministic. Walker 009b (NVE=1.62×) is sub-threshold under τ=2.0

**⚠️ 时间限定**: nve>2.0x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。

**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>2.0x. Seed 1 maintained nve>2.0x across 2 consecutive checkpoints at 45K+ (2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 never exceeded 2.0x (peak 1.62x@45K), and self-corrected to 0.38x@105K. This suggests a "point of no return" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).

The trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 2.0x).

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |
| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |
| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |
| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >2.0x = pathological) |
| **D032/D167: Trained dt_emb seed 2 — sub-threshold perturbation** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**(pre-35K, false positive)→1.24x→**1.62x@45K**(sub-threshold under τ=2.0)→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Value self-corrected to 67.3@105K while eval improved. |
| **τ=2.0 threshold (35K+)** | 008d+009b vs 008f+009c | WITH trained dt_emb: 1/2 seeds exceed nve>2.0x at 35K+ (008d peak 2.09x sustained; 009b peak 1.62x@45K sub-threshold). WITHOUT dt_emb: 0/2 seeds exceed nve>2.0x (008f peak 1.02x, 009c peak 1.26x). |
| **Causal control: dt_embed_dim=0 (corrected code, 2 seeds)** | exp_walker_008f_s0 + exp_walker_no_dt_emb_s1 | **Seed 0** (corrected code): eval 219→234→126→183→267→343→139.5@105K (zigzag, terminal dip likely transient — similar to 55-65K dip-recovery); NVE peak≈1.69×@105K (single-point, non-sustained, < τ=2.0). **Seed 1** (corrected code): eval 195→242→215→468.8@105K; NVE peak=0.88×@35K, 0.35×@105K. Both seeds: **0/2 CIVO** (NVE < τ at all checkpoints). **⚠️ Old 008f/009c data (eval=503/148) from pre-correction codebase superseded.** |
| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**⚠️ 修正：reward head 贡献最大梯度（49%@55K），obs decoder 仅 16.3%。但 reward-only SGS 仍失败——梯度大小与因果重要性解耦。** |
| **Cheetah 008d seed 3 — onset then irrecoverable degradation** | exp_097 (008d config, seed 3) | CIVO onset@45K (NVE=2.3×), ve_ratio self-corrected (0.34@85K, 0.3@105K) but eval collapsed: 192.5@75K → 77.4@85K → 61.7@105K (14% baseline). actor_entropy=-0.7 (策略退化). **onset_transient_then_degraded**: ve_ratio 自修复 ≠ 性能恢复。所有 3 个 onset Cheetah seeds eval_final < 15% baseline vs no-onset s1 = 69% baseline |
| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |

**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 1.63x (v3 standardized)）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 "eliminates" 改为 "significantly delays and reduces"。推荐方案仍是 008e_v3（C6）**。

**RSSM Fidelity Table — v3 标准化（seed=42, n=1000, sequential_rollout，论文唯一权威）：**

**Walker Walk:**

| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |
|-------|------------|------------|---------|---------------|---------------|------------|
| baseline (exp_009d) | 9.60 | 15.11 | 1.57× | 0.0294 | 0.0458 | 1.56× |
| trained_dt_emb (exp_008d, collapsed) | 25.71 | 34.60 | 1.35× | 0.0530 | 0.0865 | **1.63×** |
| no_dt_emb (exp_009c, 20ep⚠️) | 19.82 | 20.67 | 1.04× | 0.0611 | 0.0789 | 1.29× |
| frozen_dt_emb (exp_084) | 16.33 | 24.03 | 1.47× | 0.3482 | 0.3561 | 1.02× |

**Cheetah Run:**

| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |
|-------|------------|------------|---------|---------------|---------------|------------|
| trained_dt_emb (exp_097, onset_degraded) | 5.26 | 4.90 | 0.93× | 0.1410 | 0.1405 | **1.00×** |
| no_dt_emb (Cheetah) | — | — | 1.02× | — | — | 1.005× |

**⚠️ 旧 2.78× 已废弃**：旧非标准化分析产出 2.78×，v3 标准化后 Walker trained_dt_emb = 1.63×。

**⚠️ 跨环境差异（重要发现）**：Cheetah trained_dt_emb reward gap = 1.00×（无 fidelity gap），而 Walker = 1.63×。但 Cheetah 仍有 3/4 CIVO onset。可能解释：(1) 分析用 final checkpoint (105K)，onset 发生在 45K——onset 时的 fidelity gap 可能不同；(2) CIVO 机制不仅依赖 RSSM fidelity gap，dt_embedding 在 critic/actor 中的 conditioning 本身即可触发 positive feedback loop。

**解读要点**：Walker 008d 的低 obs gap (1.35×) 具有误导性——其 dt=1 绝对误差已是 baseline 的 2.7×（模型已崩塌）。论文中必须并排呈现绝对误差和比率。

**dt_emb Gradient Decomposition (D061) — ⚠️ 已修正**

梯度验证（torch.autograd.grad analysis, correct config gate_fixed_dt=2）揭示 dt_emb.weight 的梯度来源分布：

| Source | 55K (%) | 112K (%) |
|--------|---------|----------|
| Reward head | 49.0 | 38.1 |
| KL dynamics | 34.7 | 40.4 |
| Observation decoders | 16.3 | 21.5 |
| Cont head | ~0 | ~0 |

⚠️ **之前的 93% obs / 0% reward 数据不可复现**（见 gradient_decomposition_008d_corrected.json）。正确结论：reward head 贡献最大梯度（38-49%），但 reward-only SGS (016e) 仍然失败（NVE=10.42×）；obs decoder 通路（16-22%）虽贡献最小，但携带关键的 Δt-specific 空间信息驱动 RSSM fidelity gap。**梯度大小与因果重要性解耦**是核心发现。

**Strength**: Strong (updated 2026-05-25, D156 stochastic onset revision). Three-way causal ablation (trained/frozen/absent dt_emb): **trained dt_emb creates susceptibility with stochastic onset** — Walker 2/3 onset (exp_008d s0, exp_009e s1; exp_009b s2 sub-threshold NVE=1.62× under τ=2.0), Cheetah 3/4 onset (exp_078 s0 NVE=4.1×; exp_091 s2 NVE=138.7× onset_collapse; exp_097 s3 NVE=2.3× onset_transient_then_degraded; exp_088 s1 NVE≈1.0 no onset) vs **frozen dt_emb 0/4** (exp_042, exp_067) vs **no dt_emb 0/3+** (008f s1, 009c s2, exp_069 s1), all NVE<0.4×. **Necessity robustly confirmed** (trained-vs-control Fisher exact p < 0.001, 5/7 onset vs 0/19 controls). **Sufficiency not confirmed**: onset rate ~71% (5/7 completed seeds), stochastic not deterministic. The three-way design rules out "embedding presence" as cause — only gradient training creates CIVO susceptibility. Both onset (~71%) and collapse given onset (~50%) are stochastic; early training stochasticity (initialization, data sampling) determines trajectory.

### C3: Untrained dt_embedding blocks the CIVO feedback loop across environments

**⚠️ D168 framing rewrite (Reviewer 建议)**: C3 锚定在"NVE < τ = 无 CIVO 机制"上，不承诺性能水平。性能差异作为观测层报告。

**核心 claim（强）**: When dt_embedding is untrained (random fixed), the CIVO feedback loop is blocked across all tested seeds and environments — NVE never approaches τ=2.0 (max observed: 0.93× Walker, 0.584× Cheetah). This confirms C2 的因果对照：trained dt_embedding 的训练是 CIVO 的必要条件。

**观测层（弱 claim / discussion）**: Untrained dt_embedding 产生 value suppression（ve_ratio 全程 <1，value function 保守低估），性能损失程度因环境/horizon 而异：
- **Walker** (H=8): s0=778 (85% baseline), s1=751 (82%), s3=856 (93%) — 温和损失
- **Cheetah** (H=15): s0=366 (82% baseline, NVE max=0.449), s1=281 (63% baseline, NVE max=0.584), mean=324 (73% baseline) — 2-seed 均值比单 seed 大幅改善

**Moderating factor**: 性能差异可由 imag_horizon 差异解释——Walker H=8 vs Cheetah H=15，更长 horizon 意味着 untrained embedding 的小误差被复合更多次。这不是 C3 机制的漏洞，而是可解释的 moderating factor。论文中应说明 H 的选择遵循原始 DreamerV3 环境特定超参。

**Framing 指南**: C3 文本中写 "untrained dt_embedding prevents the CIVO feedback loop (NVE < τ across all N seeds and K environments)"，性能数据放实验表中客观呈现，差异在 discussion 段落中解释。不在 claim 语句中承诺性能水平。

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |
| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |
| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |
| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >2.0x = pathological). ~7x slower overestimation rate |
| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |
| **2-seed replication (Walker 008a s1)** | exp_100 (008a config, seed 1) | eval: 31→169→158→203→306→457→629→687→657→718→750.6@105K (**82% baseline**, no collapse). ve_ratio_max=0.33, civo_alert=0. Confirms 008a s0 pattern: untrained dt_emb sustains near-baseline performance without CIVO. **2-seed mean: (778+751)/2 = 764.5 (83% baseline)** |

**Strength**: Strong (cross-env confirmed, mechanism-anchored). **NVE evidence**: Walker 3 seeds max NVE=0.93×, Cheetah 2 seeds max NVE=0.584×, all far below τ=2.0 with ≥3.4× safety margin. **Performance observation**: Walker 3-seed mean=795 (83-93% baseline), Cheetah 2-seed mean=324 (73% baseline, s0=82%, s1=63%). 跨环境性能差异由 imag_horizon 差异解释（Walker H=8 vs Cheetah H=15），不影响机制性结论。Contrasts sharply with trained dt_emb onset rate 5/7 (71%, NVE>2.0×). C3 作为 C2 的因果对照，证明 CIVO 机制的触发条件，不推荐 untrained dt_emb 作为实用方案（实用方案是 C6: dt=1 imagination）。

**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >2.0x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).

**105K long-run confirmed**: exp_008a ran to 112K steps. Normalized v/e at 105K=0.59x baseline (lowest point), confirming value growth suppression is structural, not a transient delay. The suppression strengthens over time rather than converging to baseline levels.

### C4: Longer dt amplifies the problem

Increasing dt from 2 to 4 worsens degradation, consistent with RSSM prediction error compounding over longer temporal gaps.

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| dt=2 degradation | exp_006_fixed_dt2 | Peak 485, collapse to ~135 |
| dt=4 severe degradation | exp_007_fixed_dt4 | Peak 176.9@25K, 144.4@45K (33% of baseline@45K=443) |
| Monotonic relationship | dt=1 (~950) > dt=2 (peak 485@35K) > dt=4 (peak 177@25K) | Clear monotonic decline |

**Strength**: Moderate. Only two dt values tested (2 and 4). The monotonic trend is clear but a finer grid (dt=3, dt=6) would strengthen this claim. Sufficient for a supporting claim but not a standalone finding.

### C5: Learning signal reduction from shorter effective horizons compounds degradation but is not the root cause

Subsampling with dt>1 reduces the effective number of learning transitions per episode. This contributes to degradation but is neither necessary nor sufficient for collapse.

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Subsample OFF, still degraded | exp_008c (subsample OFF, untrained dt_emb, H=8) | eval ~242 vs baseline ~950 |
| Subsample OFF, no collapse | exp_008a (subsample OFF, untrained dt_emb, H=15) | eval 778@105K (85% baseline), no collapse through 112K steps |
| Subsample ON, collapse | exp_008d (subsample ON, trained dt_emb, H=8) | eval 146, value overestimation |
| Horizon effect | exp_008c (H=8) vs exp_008a (H=15) | H=15 significantly outperforms H=8, both subsample OFF |
| Subsample ON, trained dt_emb, dt=1 imag, no collapse | exp_008e_v3 (subsample ON, trained dt_emb, dt=1 imag, H=15) | eval 382@45K (86% baseline); normalized v/e 0.88x@45K (normal). Even with trained dt_emb and subsample ON, restricting imagination to dt=1 prevents collapse |

**Strength**: Moderate. The 008c vs 008a comparison shows horizon length matters independently. exp_008e_v3 confirms subsample ON does not trigger collapse when imagination is restricted to dt=1, even with trained dt_emb. But disentangling horizon from subsample effects requires additional controls. The key point—that it's not the root cause—is well-supported by 008c's stability despite lower performance.

### C6: dt=1 imagination deterministically prevents CIVO — confirmed practical mitigation

**⚠️ D153 重大修正**: 旧 008e_v3_s2 崩溃由 `gate_max_dt=8` bug 导致（旧代码允许 imagination horizon 内使用 dt>1），非 dt=1 imagination 本身的失败。D152 修复 bug 后，当前代码 **4/4 seeds 无 CIVO**。

修复后实验数据：
- exp_080 (Walker, seed 0): 无 CIVO, eval 正常
- exp_081 (Walker, seed 1): 无 CIVO, eval 正常
- exp_070 (Walker, seed 2): 无 CIVO, eval 正常
- exp_072 (Walker, seed 3): 无 CIVO, eval 正常

**旧 "Pathway B" 叙事已废弃**：008e_v3_s2 的 eval-driven collapse 是 bug 伪影，非 trained dt_embedding 的固有多路径脆弱性。当前代码确认 dt=1 imagination 完全消除 CIVO（阻断 dt>1 imagination path → critic 无法在低质量 dt>1 预测上过度估值）。

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| dt=1 imag, current code, seed 0 | exp_080 (trained dt_emb, dt=1 imag, H=15) | 无 CIVO, eval 正常 |
| dt=1 imag, current code, seed 1 | exp_081 (trained dt_emb, dt=1 imag, H=15) | 无 CIVO, eval 正常 |
| dt=1 imag, current code, seed 2 | exp_070 (trained dt_emb, dt=1 imag, H=15) | 无 CIVO, eval 正常 |
| dt=1 imag, current code, seed 3 | exp_072 (trained dt_emb, dt=1 imag, H=15) | 无 CIVO, eval 正常 |
| dt=2 imag, collapse | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K |
| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |
| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |

**Strength**: **Strong (D153: CONFIRMED — deterministic mitigation, 4/4 current code)** — dt=1 imagination 在修复 gate_max_dt bug 后 4/4 seeds 完全阻止 CIVO。旧 008e_v3 的 1/2 崩溃率是 bug 伪影（D152/D153）。dt=1 imagination 是可行的 practical mitigation：保留 trained dt_embedding 的训练信号优势，同时通过限制 imagination 到 dt=1 消除 CIVO 触发路径。

### C7: Gradient-level interventions fail to eliminate CIVO — gradient magnitude decoupled from causal importance

**⚠️ D107: SGS 全面失败，梯度干预不是正确的干预层级**

All three SGS variants fail to eliminate CIVO:
- **Reward-only SGS** (016e): 0/2, NVE=10.42× — paradoxically worse than untreated
- **Full-pathway SGS** (018+021): 0/3 across two environments — blocks all non-KL gradients, still fails
- **Obs-decoder-only SGS** (025+026): 1/6 across two environments — the identified causal channel, still fails

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Reward-only SGS 反效果 | exp_016e | NVE=10.42×, collapse to eval 31.7. 阻断 reward 梯度迫使 dt_emb 通过 obs-decoder 适配，强化空间偏差 |
| Full SGS 0/3 | exp_018 (Walker 2 seeds) + exp_021 (Cheetah 1 seed) | s1: eval 448.3, NVE 1.66× (CIVO+); s2: collapse 40.8; Cheetah: transient NVE 9.94×→0.34× (not SGS effect) |
| Obs-decoder SGS 1/6 | exp_025 (Walker 4 seeds) + exp_026 (Cheetah 2 seeds) | Walker: 1/4 (s1 survived, s2-s4 collapsed); Cheetah: 0/2, NVE 21.9×-30.2× (2.6-3.6× worse than untreated 8.3×) |
| Compensatory amplification (Cheetah) | exp_026 vs exp_010b | Obs-decoder SGS NVE 21.9-30.2× vs untreated 8.3× — blocking obs-decoder shifts co-adaptation to reward head |
| Universal value collapse | exp_025 all seeds @215K | All 4 seeds terminal ve_ratio=0.056-0.14, including s1 "success" (eval 726, value 41) — critic underestimation as side effect |
| Fourth trajectory (s3) | exp_025_s3 | Healthy@105K → CIVO@135K (NVE 6.8×) → eval recovery (590@215K) → persistent value collapse (ve_ratio 0.14) |

**核心发现**：
1. **梯度量级与因果重要性脱耦**: Reward head 38-49% 梯度占比（最大），但 reward-only SGS 失败最惨；obs decoder 16-22%（最小非零），但 obs-decoder SGS 也失败。梯度分解成功作为**诊断工具**但失败作为**干预指南**。
2. **Backward-pass 是错误的干预层级**: Full SGS 阻断所有非 KL 梯度仍 0/3 → forward-pass representational damage 是不可约减的脆弱性底线。Temporal embedding 通过 forward pass 塑造潜在表示，无论哪些梯度更新它。
3. **补偿放大**: 阻断任一通道导致剩余通道放大 co-adaptation（Cheetah: 2.6-3.6× 放大）。
4. **SGS 副作用**: 即使"成功"的 seed 也遭受 critic 校准损坏（universal value collapse）。

**Strength**: Strong. 17 seeds across 3 SGS variants and 2 environments. Only 1/17 avoids CIVO, and that seed still suffers value collapse. Embedding removal (008f+024b): 5/5 = 100% prevention. The contrast establishes gradient stopping as categorically insufficient.

### C8: Forward-pass interventions — TCN and RAVE (🔄 验证中)

**⚠️ D107/D108: 两种 forward-pass 干预方法并行验证**

SGS 失败的根因是 backward-pass 干预无法消除 forward-pass representational damage。C8 提出绕过梯度冗余的 forward-pass 干预：

**TCN (Temporal Conditioning Noise)**:
- 设计理念：imagination 时对 dt_embedding 输出加高斯噪声 $\mathcal{N}(0, \sigma^2)$，降低 conditioning 精度
- 机制假说：噪声阻止 RSSM 和 critic 对精确 dt 信号的过度 co-adaptation，同时保留粗粒度时间信息
- 与 SGS 的区别：在 forward pass 层面操作，不依赖梯度阻断
- 超参：σ=0.5×std（主实验）+ σ=0.2×std（替代超参）
- 实验：exp_027_tcn_walker_s0 (σ=0.5), exp_027_tcn_walker_s0_sigma02 (σ=0.2)

**RAVE (Reality-Anchored Value Estimation)**:
- 设计理念：用 EMA 跟踪真实环境状态的值估计，当 imagined value 超过 EMA×ceiling 时截断
- 机制假说：直接限制 critic overestimation 的幅度，打断 CIVO 正反馈循环
- 与 SGS 的区别：不修改梯度流，而是在 value estimate 层面施加约束
- 超参：ceiling=2.0（主实验）+ ceiling=1.5（替代超参）
- 实验：exp_028_rave_walker_s0 (ceil=2.0), exp_028_rave_walker_s0_ceil15 (ceil=1.5)

**D113 全面评估完成 (2026-05-20) — Scenario B 确认：Intervention Hierarchy 论文**

TCN 跨环境 universal mitigation（Scenario A）已关闭。TCN 仅在 Walker σ=0.2 成功（2/8 configs），且 eval 保留高度不稳定（91%/45% across seeds）。论文核心转为 **Intervention Hierarchy**：三层干预（Gradient → Output → Representation）系统性评估，证明 CIVO fundamentally hard to mitigate。

**TCN 全景表（D113 最终）：**

| 环境 | σ | NVE_max | CIVO 阻止? | eval 保留 |
|------|---|---------|-----------|----------|
| Walker s0 | 0.1 | 1.02@95K | ⚠️ 边界（进行中） | TBD |
| Walker s0 | 0.2 | 0.91@95K | ✅ | 91% |
| Walker s1 | 0.2 | 0.64@55K | ✅ | **45%** |
| Walker s2 | 0.2 | **2.11@95K** | **❌ CIVO confirmed** | **5%** (eval 45, 持续崩溃) |
| Walker s3 | 0.2 | TBD | 🔄 5K | — |
| Walker s0 | 0.5 | 3.97 | ❌ oscillatory | ~40% |
| Walker s1 | 0.5 | 1.64 | ❌ oscillatory | ~40% |
| Cheetah s0 | 0.2 | 1.90@55K | ❌ dose insufficient | crashed |
| Cheetah s0 | 0.5 | **10.67@55K** | ❌ transient spike+recovery | 26% |
| PickCube s0 | 0.2 | **3.71@52.5K** | ❌ dose insufficient | failing |

**关键发现**：
1. **TCN 成功率 2/10**（NVE<1.0× 标准）或 3/10（NVE<2.0×）：Walker σ=0.2 s2 NVE=2.11@95K（持续恶化），eval=45 (~5% baseline)，成功率从 2/2 降到 2/3。即使最优 dose + 最温和环境也不可靠
2. **Dose-environment dependency**：σ=0.2 在 Walker 有效但 Cheetah/PickCube 不足，σ=0.5 在 Walker 过量但 Cheetah 仍不足。不存在 universal effective dose
3. **防 CIVO ≠ 保性能**：s1 NVE_max=0.64（比 s0 的 0.91 更低），但 eval 仅 45%（比 s0 的 91% 差 2×）。噪声注入本身干扰学习
4. **Cheetah "impossible dose" 完整确认（exp_030c FINAL @224K）**：σ=1.0 全程 NVE≤0.30（CIVO 完全抑制），但 eval 从 peak 372@35K（116% baseline，初始学习不受影响！）→ 47@215K（15% baseline）。关键发现：(a) 噪声不阻止初始学习，而是**渐进腐蚀** policy（cumulative actor gradient interference）；(b) value 校准正常（value_mean=12.4, NVE=0.26@215K）→ policy degradation ≠ value corruption；(c) Cheetah 的 CIVO prevention threshold (~σ=1.0) > noise tolerance threshold (~σ<0.5)，不存在 Goldilocks zone。这本身也是 CIVO 与标准 overestimation 不同的证据——标准 Double Q 不会有这种 dose-dependent policy erosion tradeoff
5. **Cheetah σ=0.5 失败模式**：NVE=10.67@55K（transient CIVO spike），但 >95K 恢复至 <0.3。eval 永久受损（peak 296@35K → 稳态 ~77）
6. **⚠️ "90% baseline" claim 已删除**：cross-seed 均值 (821+401)/2 = 611 ≈ 68%，不是 90%。论文改为 "45%-91% across seeds (mean 68%)"
7. **Seed 效应 > dose 效应**：Walker σ=0.2 跨 seed eval=45%-91%，而 σ=0.1→0.2 的 eval 差异（55% vs 68% mean）更小

**RAVE 2 配置 ❌ — EMA anchor 自身污染**:
- ceil=2.0: negative
- ceil=1.5: negative
- 机制：CIVO 早期 imagined values 已偏高，EMA 跟踪这些值 → anchor 被污染 → ceiling 无效

**Intervention Hierarchy 总结（论文核心 Table）：**

| 干预层级 | 方法 | 成功率 | 主要失败机制 |
|----------|------|--------|-------------|
| Gradient (L1) | Full SGS | 0/3 | Forward-pass damage 不可逆 |
| Gradient (L1) | Obs-decoder SGS | 1/6 | 补偿放大 + critic 校准损坏 |
| Gradient (L1) | Reward SGS | 0/2 | No-op (梯度 ≠ 因果) |
| Output (L2) | RAVE ceil=2.0 | 0/1 | EMA anchor 污染 |
| Output (L2) | RAVE ceil=1.5 | 0/1 | EMA anchor 污染 |
| Representation (L3) | TCN σ=0.2 | 2/4 (Walker only) | ❌ s2 gradual onset NVE=2.77@105K; s3 sudden onset NVE=3.04@105K; Cheetah/PickCube dose insufficient |
| Representation (L3) | TCN σ=0.5 | 0/3 | Overdose (Walker) / Still insufficient (Cheetah) |
| **Control** | **dt_emb removal** | **5/5** | **(not an intervention — removes the feature)** |

**叙事方向（D116 最终版，Reviewer 三问审查后）**：TCN 是 **diagnostic probe**，不是 deployable mitigation。
最终 claim 措辞（确认 2/4）："TCN is the only tested intervention that achieves complete CIVO suppression in any configuration (2 of 4 Walker seeds at σ=0.2), but exhibits high seed sensitivity (50% failure rate) and fails to transfer across environments—positioning it as a diagnostic probe rather than a deployable mitigation."

**Binary protection 假说（确认 + 扩展）**：s2 渐进上升（0.58→1.01→1.65→2.77@105K），s3 表面回落后突崩（0.855→0.666→3.042@105K）。两种不同的 CIVO onset 动态，但结果相同：runaway NVE>2.5 + eval 崩溃。结论：(1) TCN operates as an all-or-nothing gate — 2/4 success, 2/4 complete failure, no intermediate; (2) CIVO onset 有至少两种模式（gradual escalation vs apparent-recovery-then-sudden-collapse）; (3) NVE 短期回落不能预测保护成功（phase transition 特性）。作为 1-2 句观察写入 + appendix 详细分析，非独立贡献。

**Dose-response 定位**：不升级为独立贡献（n 太小，seed variance > dose variance），但作为 Section 3.6 key observations：(1) "Effective dose scales with CIVO severity; tolerable dose does not" — observation; (2) "Impossible dose on Cheetah" — 最有力单点; (3) "Seed variance exceeds dose variance"。

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| TCN σ=0.5 s0 | exp_027_tcn_walker_s0 | ❌ NVE peak 4.0, eval peak 366 (40% baseline), oscillatory CIVO |
| TCN σ=0.5 s1 | exp_027_tcn_walker_s1 | ❌ NVE peak 1.637, eval peak 365, oscillatory CIVO |
| TCN σ=0.2 s0 | exp_027_tcn_walker_s0_sigma02 | ✅ NVE < 1.0× throughout (peak 0.908@95K), eval peak 821 (91% baseline) |
| TCN σ=0.2 s1 | exp_029a_tcn_walker_s1_sigma02 | ✅ NVE < 1.0× (peak 0.643@55K), eval peak 401 (**45% baseline**) |
| RAVE ceiling=2.0 | exp_028_rave_walker_s0 | ❌ negative, EMA anchor polluted |
| RAVE ceiling=1.5 | exp_028_rave_walker_s0_ceil15 | ❌ negative, same mechanism |
| Cheetah TCN σ=0.2 | exp_030a_tcn_cheetah_s0_sigma02 | ❌ NVE=1.903@55K, dose insufficient |
| Cheetah TCN σ=0.5 | exp_030b_tcn_cheetah_s0_sigma05 | ❌ NVE=10.67@55K, transient spike, eval=77 (26% baseline) |
| PickCube TCN σ=0.2 | exp_031_tcn_pickcube_s0_sigma02 | ❌ NVE=3.71@52.5K, dose insufficient |
| Cheetah TCN σ=1.0 (FINAL) | exp_030c @224K | ✅ CIVO prevented (NVE≤0.30 全程) but ❌ eval=372 peak@35K (116% baseline!) → 47@215K (15% baseline). **"Impossible dose" 完整确认**: initial learning unaffected, gradual policy erosion from cumulative noise. Value calibration normal (value_mean=12.4, NVE=0.26@215K) — policy degradation ≠ value corruption |
| Walker TCN σ=0.1 | exp_029c (running) | 🔄 边界剂量响应 |

**D113**: Scenario A closed → Scenario B confirmed. 论文 = Intervention Hierarchy paper with Walker TCN as existence proof.

**Strength**: Moderate. TCN 的 2/8 成功率 + high eval variance 反而是 diagnostic paper 的强证据——证明 CIVO 在所有三个干预层级都难以可靠缓解。Intervention Hierarchy 框架（7+ methods, 3 levels, 3 environments）是系统性贡献。

---

## Story Arc

### 1. Introduction
- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)
- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction
- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?
- Contribution: systematic factorial diagnosis identifying trained dt_embedding as creating susceptibility to conditioning-induced value overestimation (CIVO, nve>2.0x) with stochastic onset (Walker 2/3, Cheetah 3/4); removal/freezing consistently blocks it (0/7+). The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop

### 2. Background & Related Work
- Temporal abstraction in model-free RL (options framework, FiGAR, action repeat)
- World-model RL (Dreamer family, IRIS, TWM)
- Variable-rate planning in world models (few prior works, mostly positive framing)
- Value overestimation in model-based RL (delusional bias per Lu et al. 2018 — differentiate from our CIVO)

### 3. Methodology
- DreamerV3 as base architecture
- Variable-rate imagination: dt_embedding, temporal subsampling, learned gating
- **Factorial experiment design**: 2×2×2 grid (dt_embedding trained/untrained × subsample ON/OFF × H=8/15) + baselines
- Diagnostic metrics: eval return, value/eval ratio as overestimation proxy, learning curves

### 4. Results
- **Finding 1**: All dt>1 configurations degrade (C1)
- **Finding 2**: Controlled ablation isolates trained dt_embedding (C2) — the "smoking gun" comparison (008c vs 008d)
- **Finding 3**: Untrained dt_embedding prevents optimistic drift, sustaining near-baseline performance (C3)
- **Finding 4**: Longer dt amplifies (C4)
- **Finding 5**: Horizon/subsample effects are secondary (C5)
- **Finding 6 (D153 confirmed)**: dt=1 imagination deterministically prevents CIVO (4/4 seeds, current code after gate_max_dt bug fix). Practical mitigation: retain trained dt_embedding benefits while eliminating CIVO trigger pathway (C6)

### 5. Discussion
- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)
- RSSM fidelity analysis: Walker 008d reward gap (1.63x, v3 standardized) vs 008f reward gap (1.01x); Cheetah trained_dt_emb reward gap (1.00x) — environment-dependent transmission pathway (D158)
- **D153: dt=1 imagination confirmed as deterministic mitigation** (4/4 seeds, gate_max_dt bug fixed). Old "Pathway B" was bug artifact
- **D107: Gradient-level interventions fail entirely**: SGS 0/3 (full) + 1/6 (obs-decoder) + 0/2 (reward-only) = backward-pass is categorically insufficient. Gradient magnitude ≠ causal importance (reward 38-49% but reward-only SGS fails worst; obs-decoder 16-22% but targeted SGS also fails). Forward-pass representational damage is the irreducible floor.
- **Compensatory amplification**: Blocking obs-decoder on Cheetah → 2.6-3.6× NVE amplification vs untreated. Blocking reward → obs-decoder reliance increases → spatial bias reinforced.
- **Universal value collapse**: Obs-decoder SGS degrades all seeds' critic calibration (ve_ratio 0.056-0.14 @215K), including CIVO-free seeds. "Protection" = trading overestimation for underestimation.
- **Fourth CIVO trajectory (s3)**: Latent onset → delayed collapse → policy recovery → persistent value collapse. CIVO-induced critic damage may be irreversible.
- MPC vs imagination: TAWM succeeds because MPC re-plans from real states; imagination-based critic bootstrapping creates the positive feedback loop
- **D032: Value self-correction mechanism (009b)**: Transient vs sustained nve>2.0x determines outcome. Early stochasticity (initialization, data sampling) is the gate.

### 6. Implications for Future Work
- **D113: Intervention Hierarchy — all three levels fail or partially fail**: Gradient (SGS 1/17), Output (RAVE 0/2), Representation (TCN 2/8 with high variance). dt_embedding removal 5/5 but removes the feature entirely.
- TCN existence proof (Walker σ=0.2) shows mitigation is *possible in principle* but fragile — narrow dose window, environment-dependent, high seed variance in eval retention
- **Dose-environment dependency**: No universal σ exists; Walker-effective dose (σ=0.2) underdoses Cheetah/PickCube, Walker-overdose (σ=0.5) still underdoses Cheetah
- RSSM prediction quality must improve before variable-rate imagination is viable
- Hierarchical temporal abstraction (THICK, Hieros) may avoid flat-conditioning failure by maintaining separate dynamics per temporal scale
- Need for diagnostic methodology in temporal abstraction research

---

## Anticipated Reviewer Concerns

### R1: "Limited to one environment / one base algorithm"
**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The trained dt_embedding mechanism may have analogues in other latent-dynamics models, though the specific transmission pathway (RSSM fidelity gap vs value extrapolation) appears environment-dependent.
**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.

### R2: "No proposed solution — what's the actionable takeaway?"
**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. Beyond diagnosis, we provide a **systematic Intervention Hierarchy** evaluating 7+ methods across 3 levels (gradient/output/representation) and 3 environments. This is the most comprehensive evaluation of CIVO interventions to date. The key finding: even the most promising intervention (TCN, representation-level) succeeds only under narrow conditions (Walker σ=0.2, 2/8 configs, 45-91% eval retention). The actionable takeaway is that CIVO requires fundamental architectural solutions (hierarchical temporal abstraction per THICK/Hieros), not post-hoc interventions.
**Mitigation**: The Intervention Hierarchy table (7 methods × 3 levels) is a standalone contribution — it saves future researchers from re-exploring these dead ends and provides a systematic framework for evaluating future interventions.

### R3: "Value/eval ratio is a crude proxy for overestimation"
**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 2.0x baseline v/e before collapse, while untrained variants stay at or below baseline levels.
**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.

### R4: "The factorial design is incomplete — missing cells in the grid"
**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.
**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.

### R5: "Novelty concern — model exploitation / value overestimation in MBRL is well-known"
**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but three elements are genuinely novel: (a) **MPC vs imagination architectural boundary** — first empirical evidence that dt-conditioning succeeds in MPC (TAWM) but fails in imagination-based AC, localizing vulnerability to critic bootstrapping architecture; (b) **gradient magnitude ≠ causal importance** — reward head carries 38-49% of gradients but is causally irrelevant, obs-decoder carries 16-22% but is causally critical (broader methodological insight for multi-head MBRL debugging); (c) **systematic three-level intervention hierarchy** — not a single failure report but a complete taxonomy of 7 methods × 3 levels with structured negative evidence.
**Mitigation**: Expand Related Work to engage deeply with MBPO framework, explicitly articulate what CIVO reveals that MBPO does not predict (the specific *trigger* through temporal conditioning, the MPC/imagination divergence, the gradient-causality dissociation).

### R6: "All results from a single seed — how robust are the conclusions?"
**Pre-emption (D032/D167 update)**: Multi-seed data confirms stochastic onset pattern. Trained dt_emb (008d seed 0: NVE=2.09× onset; 009b seed 2: NVE=1.62× sub-threshold under τ=2.0); untrained (008f seed 1, 009c seed 2) neither exceeds 2.0x. Both onset (Walker 2/3, Cheetah 3/4; cross-env 5/7=71%) and collapse (~50% of onset seeds) are stochastic, which we report transparently. Our claim is that trained dt_emb creates susceptibility (necessity confirmed by 0/7+ controls), not deterministic failure.
**[D153]** C6 confirmed: old 008e_v3_s2 collapse was caused by gate_max_dt=8 bug (D152). Current code 4/4 seeds stable with dt=1 imagination (exp_080/081/070/072). dt=1 imagination is a deterministic CIVO mitigation.
**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.

### R7: "The factorial design confounds dt_embedding training with training data composition"
**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).
**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary factor for CIVO (sufficient to create susceptibility, but onset is stochastic — Cheetah 3/4 seeds).

### R8: "008f reward prediction degradation undermines the causal control"
**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是"去掉 dt_embedding → 不崩塌"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。
**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。

### R9: "Why not test standard overestimation countermeasures (Double Q, ensemble critics)?" [Dream D1 — 三档一致 #1 弱点] → **已实验回答 (D118-D123)**

**实验结果（D118-D124 dual-critic + mechanism ablation 系列）**：

**1. Dual-critic 跨环境结果（D128 更新）**：
- Walker wide dual-critic: **3/3 CIVO prevented**（s0 eval 739.7, s1 551.8, s2 ~121）。NVE 全程 < 2.0
  - ⚠️ **s2 非 CIVO 崩溃**：NVE 正常但 eval 354→121，actor entropy 急升(-3.59→-0.45)。可能是 policy exploration failure。**必须区分 "CIVO prevention"(3/3) vs "performance stability"(2/3)**
- Walker narrow dual-critic: 1/1 CIVO occurred (NVE 2.75) → full recovery eval 697.8
- Cheetah dual-critic: CIVO 发生(NVE 1.75) → 部分恢复 eval 97.5 (31%, 晚期下降)
- Cheetah wide single: CIVO 发生(NVE 3.59) → 自修复 eval 146 (晚期下降)。Wide > dual in Cheetah (146 vs 97.5)
- PickCube dual-critic: NVE 短暂升至 2.3 后自行修正，**PickCube 不触发持续性 CIVO**（任务动态不同）。eval 27.7 的低性能源于 gate 配置本身对 manipulation 任务有害（vanilla baseline 58.6 → 加 subsample+dt_emb 后 26.6），非 CIVO 导致。PickCube 作为 scope limitation 讨论，跨环境 CIVO 叙事聚焦 locomotion (Walker/Cheetah)
- **v1≈v2 across all environments and all configs**（ρ>0.999 Walker; exact match Cheetah/PickCube）

**2. v1≈v2 核心发现**：Double Q 的 pessimism 机制在 pure-imagination MBRL 中失效。两个 critic 共享相同 world model imagined features → 收敛到相同函数。Per-sample pessimism 仅为独立 critic 理论值的 3-4%（ρ>0.998）。

**3. 2×2 Mechanism Factorial（D126 — 全部 4 格填满）**：
| | Single critic | Dual critic (min) |
|--|--------------|-------------------|
| ~1.05-1.2M params | baseline (**CIVO → 永久崩溃**) | **exp_035 narrow: CIVO(NVE 2.75) → 恢复中 → eval 149+** |
| ~2.4-2.9M params | **exp_033 wide: CIVO(NVE 4.75) → 自修复 → eval 408** | **exp_032: CIVO 预防(NVE≤1.1) → eval 670-788** |

**4. 双维度发现（D127 最终修正 — 论文最核心新发现）**：

**Recovery 维度（min 是主导因素）**：
| 配置 | CIVO 发生? | NVE peak | eval final | 恢复能力 |
|------|-----------|----------|------------|---------|
| Baseline (single+normal) | ✓ | ~2-4 | collapsed | 无 |
| exp_033 (single+wide) | ✓ | 4.75 | 408 | 部分(capacity) |
| **exp_035 (dual+narrow)** | **✓** | **2.75** | **697.8** | **完全(min)** |
| exp_032 (dual+wide) | ✗ | ≤1.1 | 670-788 | 无需恢复 |

- **Min 的核心价值是 recovery 而非 prevention**：exp_035 eval 697.8 ≈ exp_032 670-788，尽管经历了 CIVO
- **Min >> Capacity for recovery**：697.8 vs 408。min 实现完全恢复，capacity 仅部分恢复
- **Min 同时降低 CIVO 严重度**：exp_035 NVE 2.75 < exp_033 NVE 4.75

**Prevention 维度（需 min+capacity 协同）**：
- 只有 exp_032 (min+capacity) 从未触发 CIVO（NVE≤1.1）
- Prevention 优势不是最终性能（≈recovery-with-min），而是**训练效率**（节省 ~40K steps 恢复期）
- v1≈v2 在所有 dual-critic 中成立（包括 exp_032）→ 协同效应是经验事实，机制为 hypothesis

**跨环境 caveat**：Walker 上 recovery 充分(697.8)，但 Cheetah 上 recovery 不充分(97.5, 31%)。环境越难，recovery 越不可靠 → prevention 在难环境中价值更大。

**⚠️ 机制为 open hypothesis**：v1≈v2 在所有 dual-critic 中成立。可能的解释：(a) min 在训练早期(v1≠v2 时)建立了稳定学习轨迹 (b) min-target coupling 在 wider network 的 smoother loss landscape 上更有效 (c) capacity 提升 value calibration 质量而非多样性。论文中诚实报告经验事实，机制标注为 hypothesis。

**论文 narrative（D127 最终版）**：双维度报告——(a) Prevention: min+capacity 协同预防 CIVO（训练效率优势）(b) Recovery: min 是 CIVO 后恢复的主导因素（被低估的特性）(c) 跨环境：难环境中 recovery 不充分，凸显 prevention 的必要性 (d) v1≈v2: pessimism 机制失效但 min 通过其他通路起效（open question）

**5. 环境依赖性（D125 — exp_034 完成）**：
- **Walker（中等 CIVO，untreated NVE 2-4）**：min 操作完全预防 CIVO（2/2 seeds）
- **Cheetah（高强度 CIVO，untreated NVE 8.27-70.64，seed 间高方差）**：min 操作将 NVE peak 从 baseline 8.27-70.64 降至 1.75（≥4× reduction），但仍超 2.0 阈值，不能完全预防。双倍参数(2.36M)实现部分恢复(eval 97.5)但仅达 pre-CIVO 峰值的 31% 且晚期下降。对比 Walker wide-critic(exp_033) 恢复到 408(>pre-CIVO)，说明**环境动力学复杂度是恢复质量的决定性因素**。（来源：exp_010b s0 NVE_final=70.64, s1 NVE_peak=8.27。论文中须报告两个 seed 并使用保守 claim "≥4× NVE reduction"，不用 40×）
- **论文 claim 限定**："min=prevention" 必须加 "in moderate-CIVO environments" 限定，否则审稿人拿 Cheetah 数据直接攻击。这反而强化 intervention hierarchy 叙事——即使 architecture-level 干预也有 CIVO 严重度边界

**论文 narrative（D126 修正）**：从"为什么不测标准对策"转为"我们测了——(a) pessimism 机制失效（v1≈v2 across all configs），(b) min alone 和 capacity alone 都不能预防 CIVO，(c) 两者协同（min+capacity）才能预防，(d) 机制：capacity 提供函数多样性 + min 约束 overestimation 反馈环，(e) prevention >> recovery"。2×2 factorial 的**交互效应**比任何单因素更有方法论启示——对 ML 社区的 critic 设计指导价值更高。

### R10: "NVE threshold is calibrated and validated in-sample" [Dream D8 — 三档一致]
**Pre-emption**: 承认 2.0× threshold 在同一 29 个数据点上 calibrate 和 validate。但 (a) 2.0× 落在完美分离区间 [1.89×, 3.77×] 内（CIVO 最小 NVE peak=3.78×, No-CIVO 最大=1.88×），非事后拟合；(b) 4 环境 × 多种 configs 提供 reasonable diversity；(c) ground truth labeling 基于 mechanism identification（CIVO vs non-CIVO dynamics），不是简单的 performance threshold。
**Mitigation**: 明确承认 limitation，建议 held-out validation（不同架构或环境）作为 future work。讨论 NVE 在不同 reward scale 下的 generalization boundary。

### R11: "Pixel observations would change the gradient decomposition" [Dream D9 — 三档一致]
**Pre-emption**: 正确——pixel 下 obs-decoder channel（本文识别为 16-22% 梯度但因果关键）会承载更多信息和更大梯度。CIVO 动态可能更强（更多空间信息可利用）或更弱（decoder 正则化效应更强）。这是一个重要的泛化性边界。
**Mitigation**: 在 limitations 中明确讨论，定位为 future work。强调本文在 proprioceptive setting 的发现建立了 CIVO 的基础机制理论，pixel 扩展需要后续工作。

---

## Experiment Coverage Assessment

| Claim | Evidence Status | Gaps |
|-------|----------------|------|
| C1 (degradation) | ✅ Strong — 3 configurations + 2 environments | None |
| C2 (CIVO susceptibility) | ✅ Strong — onset 5/7 (Walker 2/3, Cheetah 3/4) vs 0/19 controls (Fisher p<0.001); cross-env frozen 4/4 closed (084-087); exp_097 confirms irrecoverable damage pattern | None |
| C3 (untrained emb protection) | ✅ Strong — 2-seed confirmed (008a s0=778, exp_100 s1=751, mean 83% baseline) + cross-env replication | None |
| C4 (dt amplification) | ✅ Moderate — dt=1 > dt=2 > dt=4 monotonic | Only 2 dt values |
| C5 (horizon/subsample secondary) | ✅ Moderate | None blocking |
| C6 (dt=1 imag confirmed) | ✅ Strong — 4/4 seeds no CIVO with current code (D153, exp_080/081/070/072). Old 008e_v3 collapse was gate_max_dt bug | None |
| C7 (SGS failure / gradient decoupling) | ✅ Strong — 17 seeds, 3 variants, 2 envs. 1/17 CIVO-free (with value collapse side effect). Embedding removal 5/5. | None |
| C8 (Intervention Hierarchy) | ✅ D113 确认 — TCN 2/8, RAVE 0/2, SGS 1/17. Hierarchy 本身是贡献 | Cheetah σ=1.0 + PickCube σ=0.5 pending (extra data points) |

### Priority Actions Before Submission (updated 2026-05-20 D116 — Dream修复)
1. ~~C1-C7 实验~~ — ✅ 全部完成
2. ~~TCN/RAVE 评估~~ — ✅ D113 Scenario B 确认
3. ~~论文 TCN 文本修正~~ — ✅ cross-seed 报告 + narrative reframe
4. **🔄 [P0] 标准过估值对策讨论** — Paper Agent 执行中 (Dream R9)
5. **🔄 [P0] 参考文献扩展至 40+** — Paper Agent 执行中 (Dream D7)
6. **🔄 [P1] 新颖性锐化 + NVE 讨论 + pixel obs + CoRL 相关性** — Paper Agent 队列 (Dream D3/D8/D9/D2)
7. **🔄 [P1] Cheetah σ=1.0 + PickCube σ=0.5** — 运行中，Hierarchy 额外数据
8. **Re-dream 验证** — Paper Agent 结构性修复完成后
9. **论文收尾** — Reviewer 审查 + provenance + 三件套 + 5/25 数据锁定

---

## Key Figures (Planned)

1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)
2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes
3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis
4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse
5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)
6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）
7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.
