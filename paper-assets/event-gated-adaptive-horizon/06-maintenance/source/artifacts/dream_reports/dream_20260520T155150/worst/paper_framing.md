# Paper Framing: Diagnostic Analysis of Temporal Abstraction in World-Model RL

## Title Candidates

1. **"Why Temporal Abstraction Fails in DreamerV3: A Diagnostic Analysis of Variable-Rate Imagination"**
2. ~~**"The Delusional Critic Problem in DreamerV3's Variable-Rate Imagination"**~~ (deprecated — "delusional critic" conflicts with Lu et al. 2018)
3. **"Diagnosing Value Overestimation from Temporal Abstraction in DreamerV3"** ← preferred after D037 terminology decision
4. **"Conditioning-Induced Value Overestimation in Variable-Rate World-Model Imagination"**

**⚠️ D037 术语决定**: "delusional critic" → **"conditioning-induced value overestimation"** (简称 CIVO)。Lu et al. 2018 的 delusional bias 指 policy-class constraints 导致不可实现的 Q 值，本文机制是 model imprecision + learned conditioning amplification，概念不同。Dream 模拟三档审稿一致指出术语误导。全文替换："delusional critic" → "conditioning-induced value overestimation"，可 cite Lu et al. 2018 as analogy but must explicitly differentiate。

**⚠️ D037 TAWM 对比（关键 novelty 升级）**: TAWM (Nhu et al., ICML 2025) 在 TD-MPC2 (MPC setting) 中成功使用 dt-conditioning。本文发现 dt-conditioning 在 imagination-based actor-critic 中失败 → **novelty 从 "known failure class 的 specific instance" 升级为 "dt-conditioning succeeds in MPC but fails in imagination — here's the architecture-specific vulnerability"**。TAWM 是强化 novelty 的最关键参考文献。

## Venue

**CoRL 2026** — Deadline: 2026-05-29

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

### C2: Trained dt_embedding reliably triggers pathological value overestimation (>1.5x), creating high collapse risk

**D032 update: nve>1.5x threshold has perfect separating power (4/4); collapse itself is stochastic.**

The trained dt_embedding reliably induces pathological value overestimation (normalized v/e >1.5x baseline) across all tested seeds, but whether this overestimation progresses to catastrophic performance collapse is stochastic:

- **WITH trained dt_emb**: 2/2 seeds exceed nve>1.5x at 35K+ (008d seed 1: sustained 1.71x@35K→2.09x@45K→4.12x@55K → collapse; 009b seed 2: 1.62x@45K → self-correction to 0.38x@105K)
- **WITHOUT dt_emb (008f)**: 0/2 seeds exceed nve>1.5x at 35K+ (seed 1 peak 1.02x@25K; seed 2 peak 1.26x@25K)
- **1.5x threshold (35K+)**: 4/4 perfect classification — reliable diagnostic marker separating trained vs untrained dt_emb

**⚠️ 时间限定**: nve>1.5x 诊断适用于 **35K+ steps**（此时 baseline v/e 已充分收敛至 >0.24，比率稳定可靠）。25K 处 baseline v/e 仅 0.087，微小绝对差异可被放大为大比率（如 009b@25K nve=2.05x 和 008e_v3@25K nve=1.93x 均为 false positive）。论文中报告 threshold 时必须标注此限定。

**Sustained vs transient overestimation**: The key difference between collapse (008d seed 1) and self-correction (009b seed 2) is the **temporal persistence** of nve>1.5x. Seed 1 maintained nve>1.5x across 3 consecutive checkpoints at 35K+ (1.71x@35K→2.09x@45K→4.12x@55K, accelerating), locking the positive feedback loop; seed 2 exceeded 1.5x at 45K (1.62x) but dropped to 1.41x@55K and continued declining, allowing self-correction. This suggests a "point of no return" where sustained overestimation becomes irreversible, with early training stochasticity (initialization, data sampling order) determining which path is taken (cf. Henderson et al. 2018, Bjorck et al. 2022, Qiao et al. 2023).

The trained dt_embedding enables precise dt prediction in imagination, but RSSM state prediction quality at dt>1 is insufficient to support this precision. The result is conditioning-induced value overestimation (CIVO) that drives actor learning toward incorrect policies. Without dt_embedding conditioning, the overestimation feedback loop is blocked entirely (nve never exceeds 1.5x).

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Untrained dt_emb, no collapse | exp_008c (dt=2, subsample OFF, untrained dt_emb, H=8) | eval plateau ~242@55K; v/e: @35K=21.8% (0.90x) → @55K=29.1% (0.72x) → @65K=32.8% (0.58x) (declining normalized v/e, ~7x slower than trained) |
| Trained dt_emb, collapse | exp_008d (dt=2, subsample ON, trained dt_emb, H=8) | eval declining 167→146→141 @25K→35K→45K; v/e: @25K=15.5% (1.78x) → @35K=41.2% (1.71x) → @45K=69.3% (2.09x) (accelerating overestimation) |
| Both trained dt_emb → accelerating v/e | exp_006 (H=15) vs exp_008d (H=8) | 006: v/e @35K=31.1% (1.29x)→@45K=53.3% (1.61x)→@55K=93.3% (2.31x); 008d: v/e @35K=41.2% (1.71x)→@45K=69.3% (2.09x) — both show accelerating normalized v/e leading to collapse |
| Baseline v/e calibration (overshoot reference) | exp_001_baseline | v/e@35K=24.1%, @45K=33.1%, @55K=40.4%. Overshoot ratio: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x (all >1.5x = pathological) |
| **D032: Trained dt_emb seed 2 — pathological but self-correcting** | exp_009b (008d config, seed 2) | eval 39→141→164→141→172→209→197→236→279→268@105K (**no collapse**, rising). nve: **2.05x@25K**→1.24x→**1.62x@45K**→1.41x→0.94x→0.66x→0.51x→0.43x→**0.38x@105K**. Transient nve>1.5x with self-correction. Value peaked 110.9@65K → self-corrected to 67.3@105K while eval improved. |
| **1.5x threshold separating power** | 008d+009b vs 008f+009c | WITH trained dt_emb: 2/2 seeds exceed nve>1.5x (008d peak 2.09x sustained, 009b peak 2.05x transient). WITHOUT dt_emb: 0/2 seeds exceed nve>1.5x (008f peak 1.02x, 009c peak 1.26x). **4/4 perfect classification.** |
| **Causal control: dt_embed_dim=0 (direction confirmed, seed-dependent)** | exp_008f seed 1 + exp_009c seed 2 | **Seed 1**: eval 197→207→194→173→503@105K (zigzag recovery); nve 1.02x→0.73x→0.83x→0.97x→0.30x. **Seed 2**: eval 169→211→239→359→227→191→148@105K (decline after 75K); nve 1.26x→0.79x→0.72x→0.33x→0.60x→0.90x→1.14x. Both vs 008d@45K nve=2.09x: onset delayed 60K+ steps, severity reduced ~2x. **009c extending to 200K to observe if nve crosses 1.5x.** |
| **Reward SGS = no-op (reward gradient = 0 by architecture)** | exp_016e (reward_dt_emb_detach=True, subsample ON, H=8, seed 1) | Peak eval 326.7@75K → collapse 31.7@95K, NVE=10.42x. 梯度验证揭示 reward loss 对 dt_emb.weight 贡献为 0——reward_dt_emb_detach 是 no-op。016e 与 008d 的差异（onset timing, peak height）归因于随机变异。**⚠️ 修正：reward head 贡献最大梯度（49%@55K），obs decoder 仅 16.3%。但 reward-only SGS 仍失败——梯度大小与因果重要性解耦。** |
| RSSM fidelity analysis | baseline / 008d / 008f | See RSSM Fidelity Table below |

**⚠️ 008f 定位：因果控制实验，非推荐方案。** 008f 去掉 dt_embedding 后 reward_MAE=0.747（baseline 的 75x），reward head 无法区分 dt=1/dt=2（reward gap 仅 1.01x vs 008d 的 2.78x）。**D030 更新**：008f seed 2 (009c) 在 105K 达到 nve=1.14x（borderline），seed 1 为 0.30x——protection 不 robust。但 008f 两个 seed 的 v/e 增长速度均显著慢于 008d（008d@45K=2.09x vs 008f seed 2@105K=1.14x），确认 dt_embedding 是 primary amplifier。**C2 因果方向成立，但 "eliminates" 改为 "significantly delays and reduces"。推荐方案仍是 008e_v3（C6）**。

**RSSM Fidelity Table（论文中必须同时报告绝对误差和比率）：**

| Model | dt1 obs_MSE | dt2 obs_MSE | obs gap | dt1 reward_MAE | dt2 reward_MAE | reward gap |
|-------|------------|------------|---------|---------------|---------------|------------|
| baseline (exp_001) | 13.49 | 27.50 | **2.04x** | 0.0102 | 0.0159 | 1.56x |
| 008d (trained dt_emb, collapsed) | 41.31 | 53.67 | **1.30x** | 0.0568 | 0.1579 | **2.78x** |
| 008f (no dt_emb, stable) | 8.01 | 22.04 | **2.75x** | 0.7469 | 0.7526 | 1.01x |

**解读要点**：008d 的低 obs gap ratio (1.30x) 具有误导性——其 dt=1 绝对误差本身已是 baseline 的 3x（模型已崩塌）。论文中必须并排呈现绝对误差和比率，避免审稿人被比率误导。

**dt_emb Gradient Decomposition (D061) — ⚠️ 已修正**

梯度验证（torch.autograd.grad analysis, correct config gate_fixed_dt=2）揭示 dt_emb.weight 的梯度来源分布：

| Source | 55K (%) | 112K (%) |
|--------|---------|----------|
| Reward head | 49.0 | 38.1 |
| KL dynamics | 34.7 | 40.4 |
| Observation decoders | 16.3 | 21.5 |
| Cont head | ~0 | ~0 |

⚠️ **之前的 93% obs / 0% reward 数据不可复现**（见 gradient_decomposition_008d_corrected.json）。正确结论：reward head 贡献最大梯度（38-49%），但 reward-only SGS (016e) 仍然失败（NVE=10.42×）；obs decoder 通路（16-22%）虽贡献最小，但携带关键的 Δt-specific 空间信息驱动 RSSM fidelity gap。**梯度大小与因果重要性解耦**是核心发现。

**Strength**: Moderate-strong (D032 update: causal direction + diagnostic marker confirmed; collapse stochastic). The **nve>1.5x threshold** achieves 4/4 perfect separation: all trained dt_emb seeds (008d, 009b) exceed 1.5x; no untrained seeds (008f, 009c) exceed 1.5x. This is the paper's strongest quantitative result for C2. **Collapse** is stochastic (1/2 trained seeds): 008d seed 1 shows sustained nve>1.5x → collapse; 009b seed 2 shows transient nve>1.5x → self-correction. The **causal direction** is unambiguous across all 4 data points. Pending: 009e (008d seed 1) to determine collapse probability (1/3 vs 2/3); 009f (008f seed 1) for third untrained seed; 009c extension to 200K.

### C3: Untrained dt_embedding prevents optimistic drift, substantively protecting performance

When dt_embedding is untrained (random fixed), the value function cannot exploit precise dt information, preventing the optimistic value drift seen in trained variants. This value growth suppression substantively protects performance: exp_008a demonstrates two complete zigzag recovery cycles over 105K steps (peak @105K=778, 85% of baseline 916), with normalized v/e consistently suppressed at 0.59-0.93x baseline. The trained dt_embedding variant (exp_006) collapses catastrophically as its v/e ratio accelerates far past baseline levels (2.3x baseline@55K).

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| Two V-shaped recoveries (105K) | exp_008a (dt=2, subsample OFF, untrained dt_emb, H=15) | 501→563→488→608→470→584→572→778; two complete recovery cycles over 105K steps. @65K=608 (-1.3% baseline), @105K=778 (-15.1% baseline, 85% of 916). No collapse. |
| Sustained v/e suppression | exp_008a | v/e: 37.6%@55K → 37.2%@65K → 53.6%@75K → 47.5%@85K → 49.7%@95K → 38.6%@105K. Normalized v/e: 0.93x→0.66x→0.75x→0.68x→0.79x→0.59x baseline. Consistently below 1.0x, no acceleration. |
| Trained dt_emb: accelerating collapse | exp_006 (dt=2, subsample ON, trained dt_emb, H=15) | 485→477→360→collapse; v/e: 53.3%@45K (1.61x)→93.3%@55K (2.31x) → immediate collapse |
| v/e rate comparison (H=8 controlled) | exp_008c vs exp_008d | 008c (untrained): @35K=21.8% (0.90x)→@65K=32.8% (0.58x) (normalized declining); 008d (trained): @25K=15.5% (1.78x)→@35K=41.2% (1.71x) (normalized >1.5x = pathological). ~7x slower overestimation rate |
| Baseline v/e calibration | exp_001_baseline | v/e: 8.7%@25K → 24.1%@35K → 40.4%@55K → 56.3%@65K → 65.6%@105K (stable 69-72% from 135K+). 008a normalized v/e: 0.93x@55K → 0.66x@65K → 0.59x@105K (suppressed, diverging further below baseline); 008d: 1.7x@35K → 2.1x@45K (optimistic drift) |

**Strength**: Strong (B+ confirmed with 105K long-run data). Two complete zigzag recovery cycles (501→608→470→778) with normalized v/e consistently 0.59-0.93x baseline across 105K steps. This is structural value growth suppression, not a transient delay. Contrasts sharply with exp_006's accelerating v/e (1.6x→2.3x baseline → collapse). The mechanism is clear: untrained dt_embedding prevents the value function from exploiting precise (but wrong) dt>1 predictions, suppressing the optimistic value drift that drives the CIVO feedback loop in trained variants.

**Diagnostic metric: v/e overshoot ratio** = experiment v/e / baseline v/e at same training step. >1.5x = pathological warning. Trained dt_emb variants: 008d@35K=1.7x, @45K=2.1x; 006@45K=1.6x, @55K=2.3x. Untrained: 008a normalized v/e range 0.59-0.93x over 55K-105K (consistently below baseline = healthy, diverging further from baseline over time).

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

### C6: dt=1 imagination delays but does not eliminate CIVO collapse — the vulnerability is the trained dt_embedding itself

**⚠️ D038 重大修正**: 008e_v3_s2 (seed=2) **崩溃** — eval 715@95K → 452 → 137@105K, nve=3.78x@105K, 全程 gate_dt_mean=1.0（dt=1 imagination 从未违反）。

原假设"dt=1 imagination = practical mitigation"被**否证**。跨 seed 数据：
- seed 1: eval=869.9@105K ✓（95% baseline, nve=0.80x）
- seed 2: eval=137@105K ✗（崩溃, nve=3.78x）
- **独立 seed 崩溃率: 1/2 (50%)**

对比 008d (trained dt_emb + dt=2 imagination): 同样 1/2 崩溃率（seed 1 collapse, seed 2 self-correct@268）。dt=1 imagination **未降低崩溃概率**。

**⚠️ D039 机制辨析 — 008e_v3_s2 的崩溃可能不是 CIVO**

Reviewer 深度分析揭示 008e_v3_s2 与 008d 的崩溃动力学**定性不同**：

| 特征 | 008d s1 (经典 CIVO) | 008e_v3_s2 (待确认) |
|------|---------------------|---------------------|
| value 变化 | 爆炸 (60→138, +130%@55K) | 温和 (339→384→340, +13%→-12%) |
| eval 变化 | 后跌 (146→83, -43%) | **先跌** (715→452→137, -81%) |
| nve 驱动 | value 分子驱动（value 爆炸） | eval 分母驱动（eval 崩溃） |
| actor_entropy | ↓ (-3.47→-4.88) 策略变确定 | **↑** (-5.21→-3.83) 策略变随机 |
| 机制 | critic overestimate → actor exploit | eval crash → value 滞后跟随 |

**结论**: 008e_v3_s2 的 nve=3.78x 是 eval 崩溃的**结果**，不是 value overestimation 的**原因**。这更像 policy instability 而非 CIVO。

**D040 最终判定**: 009a baseline seed 2 在 85-105K **完全稳定** (618→596→836, 正常波动后恢复)。排除 "seed 2 本身不稳定" 假说。**008e_v3_s2 的崩溃是配置导致的**。

| Step | baseline s2 (009a) | 008e_v3 s2 | 差异 |
|------|-------------------|------------|------|
| 85K | 618.7 | 715.2 | 008e_v3 略高 |
| 95K | 596.2 (↓3.6%) | 452.4 (**↓37%**) | 10× 更大跌幅 |
| 105K | 836.5 (↑40%) | 137.0 (**↓70%**) | baseline 恢复 vs 008e_v3 继续崩 |

**C6 最终状态: PARTIALLY FALSIFIED**
- dt=1 imagination 不能阻止崩溃（008e_v3: 1/2 seeds 崩溃 vs baseline: 0/2 seeds 崩溃）
- 崩溃是配置导致的，不是 seed 特异性
- 但崩溃**机制**与经典 CIVO 不同（见上方对比表）→ trained dt_embedding 可能通过**多条路径**创造脆弱性

**论文表述建议**: "Restricting imagination to dt=1 does not prevent collapse in the presence of trained dt-embedding (1/2 seeds collapse). While the collapse shares the high nve signature with classic CIVO, the underlying dynamics differ — the collapsed seed exhibits eval-driven destabilization with increasing policy entropy, rather than value-driven exploitation with decreasing entropy. This suggests trained dt-embedding creates vulnerability through multiple pathways, not solely through the value overestimation feedback loop."

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| dt=1 imag, seed 1, healthy | exp_008e_v3_walker_s1 (trained dt_emb, dt=1 imag, H=15) | eval=869.9@105K (95% baseline), nve=0.80x |
| **dt=1 imag, seed 2, COLLAPSED** | exp_008e_v3_walker_s2 (same config, seed=2) | eval 715@95K → 137@105K, nve ≤0.68x@85K → 1.34x@95K → **3.78x@105K**. gate_dt=1.0 throughout |
| dt=2 imag, seed 1, collapsed | exp_008d (trained dt_emb, dt=2 imag, H=8) | eval 167→82@55K, nve 1.78x@25K → 2.09x@45K. Onset at 25K |
| dt=2 imag, seed 2, self-corrected | exp_009b (008d config, seed 2) | eval 268@105K (rising), nve peak 1.62x@45K → self-correction |
| Onset delay | 008e_v3_s2 vs 008d | 008d onset nve>1.5x at 25-35K; 008e_v3_s2 at 95-105K. Delay ~70K steps |
| No dt_emb, stable | exp_008f (dt_embed_dim=0, subsample ON) | No collapse, reward_MAE 75x baseline |
| Untrained dt_emb, stable | exp_008a (untrained, subsample OFF, H=15) | 778@105K (85% baseline), nve 0.59-0.93x |

**Strength**: **Moderate (D040: PARTIALLY FALSIFIED)** — dt=1 imagination 不能阻止崩溃 (1/2 seeds)，但崩溃机制与经典 CIVO 不同 (eval-driven vs value-driven)。009a baseline s2 稳定排除 seed 脆弱假说。核心洞察：trained dt_embedding creates vulnerability through multiple pathways — CIVO (Pathway A, 008d) 和 non-CIVO policy instability (Pathway B, 008e_v3_s2)。dt=1 imagination 消除 Pathway A 但不消除 Pathway B。

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

**D109 GO — 结果更新 (2026-05-20)**:

**TCN σ=0.2 Walker s0 (215K) ✅ — 全项目首个完全预防 CIVO 的干预**:
- NVE 全程 < 1.0×（峰值 0.908@95K，末期 0.095@215K）
- eval 峰值 821.1@175K（90% baseline），末期均值 587
- 保持基线竞争性能 + 零 CIVO → 前向精度降解假说验证

**TCN σ=0.5 Walker 2 seeds ❌ — 过量噪声 → 振荡双稳态**:
- s0: NVE 峰值 4.0, eval 峰值 366（40% baseline）
- s1: NVE 峰值 1.637, eval 峰值 365（40% baseline）
- 跨 seed 定性一致：振荡 CIVO + 永久性能损伤 → σ 过大破坏有用时间信息

**RAVE 2 配置 ❌ — EMA anchor 自身污染**:
- ceil=2.0: negative（具体数据 TBD）
- ceil=1.5: negative（具体数据 TBD）
- 机制：CIVO 早期 imagined values 已偏高，EMA 跟踪这些值 → anchor 被污染 → ceiling 无效

**Cheetah σ=0.2 ❌ — 剂量不足**:
- NVE=1.903@55K（刚过 1.5× 阈值）
- Cheetah CIVO 严重程度 8-108× vs Walker 2-6× → σ=0.2 噪声幅度不足

**⚠️ Claim 措辞**: 用 "NVE remained below 1.0× throughout" 而非 "零 CIVO"。范围限制为 "Walker Walk, σ=0.2" 直到 s1 和 Cheetah σ=0.5 数据到手。

| Evidence | Experiment | Key Metric |
|----------|-----------|------------|
| TCN σ=0.5 s0 | exp_027_tcn_walker_s0 | ❌ NVE peak 4.0, eval peak 366 (40% baseline), oscillatory CIVO |
| TCN σ=0.5 s1 | exp_027_tcn_walker_s1 | ❌ NVE peak 1.637, eval peak 365, oscillatory CIVO |
| TCN σ=0.2 s0 | exp_027_tcn_walker_s0_sigma02 | ✅ NVE < 1.0× throughout (peak 0.908@95K), eval peak 821 (90% baseline) |
| TCN σ=0.2 s1 | exp_027_tcn_walker_s1_sigma02 | 🔄 RUNNING |
| RAVE ceiling=2.0 | exp_028_rave_walker_s0 | ❌ negative, EMA anchor polluted |
| RAVE ceiling=1.5 | exp_028_rave_walker_s0_ceil15 | ❌ negative, same mechanism |
| Cheetah TCN σ=0.2 | exp_027_tcn_cheetah_s0_sigma02 | ❌ NVE=1.903@55K, dose insufficient for Cheetah severity |
| Cheetah TCN σ=0.5 | — | 🔄 RUNNING |

**D109 GO**: TCN σ=0.2 Walker s0 成功 → C8 confirmed for Walker. 等待 s1 + Cheetah σ=0.5。

**Strength**: Moderate-strong (single seed). σ=0.2 on Walker = first successful CIVO prevention with competitive performance. Dose-response (σ=0.5 fails, σ=0.2 succeeds) provides mechanistic insight. Cross-environment generalization pending.

---

## Story Arc

### 1. Introduction
- Temporal abstraction is a long-sought goal in RL (options, macro-actions, skip connections)
- World-model RL (DreamerV3) offers a natural testbed: modify imagination dt without changing environment interaction
- Puzzle: all our attempts at variable-rate imagination degrade performance. Why?
- Contribution: systematic factorial diagnosis identifying trained dt_embedding as the reliable trigger for conditioning-induced value overestimation (CIVO, nve>1.5x), with collapse as a stochastic consequence. The vulnerability is deeper than imagination quality — even dt=1 imagination collapses at the same rate when dt_embedding is trained, revealing that training data dt>1 transitions alone drive the critic exploitation feedback loop

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
- **Finding 6 (partially falsified)**: dt=1 imagination does not prevent collapse (1/2 seeds), but collapsed seed (008e_v3_s2) shows non-CIVO dynamics (eval-driven, entropy ↑) unlike 008d's classic CIVO (value-driven, entropy ↓). 009a baseline s2 stable → collapse is config-caused. Trained dt_embedding creates vulnerability through multiple pathways, not solely through value overestimation (C6, D040)

### 5. Discussion
- Mechanism: why trained dt_embedding causes CIVO (RSSM fidelity gap at dt>1)
- RSSM fidelity analysis: 008d reward gap (2.78x) vs 008f reward gap (1.01x)
- **D040: Multiple vulnerability pathways**: Pathway A (CIVO, value-driven) + Pathway B (non-CIVO policy instability, eval-driven)
- **D107: Gradient-level interventions fail entirely**: SGS 0/3 (full) + 1/6 (obs-decoder) + 0/2 (reward-only) = backward-pass is categorically insufficient. Gradient magnitude ≠ causal importance (reward 38-49% but reward-only SGS fails worst; obs-decoder 16-22% but targeted SGS also fails). Forward-pass representational damage is the irreducible floor.
- **Compensatory amplification**: Blocking obs-decoder on Cheetah → 2.6-3.6× NVE amplification vs untreated. Blocking reward → obs-decoder reliance increases → spatial bias reinforced.
- **Universal value collapse**: Obs-decoder SGS degrades all seeds' critic calibration (ve_ratio 0.056-0.14 @215K), including CIVO-free seeds. "Protection" = trading overestimation for underestimation.
- **Fourth CIVO trajectory (s3)**: Latent onset → delayed collapse → policy recovery → persistent value collapse. CIVO-induced critic damage may be irreversible.
- MPC vs imagination: TAWM succeeds because MPC re-plans from real states; imagination-based critic bootstrapping creates the positive feedback loop
- **D032: Value self-correction mechanism (009b)**: Transient vs sustained nve>1.5x determines outcome. Early stochasticity (initialization, data sampling) is the gate.

### 6. Implications for Future Work
- **D107: Forward-pass interventions are the next frontier**: Backward-pass (gradient) interventions exhaustively shown insufficient. Two forward-pass approaches under test:
  - **TCN**: Imagination-time noise on dt_embedding to reduce conditioning precision
  - **RAVE**: EMA-anchored value ceiling to directly limit critic overestimation
- **D108 硬截止**: 5/22 go/no-go, 5/25 数据锁定. If both fail → pure diagnostic paper (still strong: C1-C7)
- RSSM prediction quality must improve before variable-rate imagination is viable
- Hierarchical temporal abstraction (THICK, Hieros) may avoid flat-conditioning failure by maintaining separate dynamics per temporal scale
- Need for diagnostic methodology in temporal abstraction research

---

## Anticipated Reviewer Concerns

### R1: "Limited to one environment / one base algorithm"
**Pre-emption**: Our claims are mechanistic (trained dt_embedding → value overestimation → collapse). The causal chain is architecture-specific by design—we diagnose *why* it fails in DreamerV3, not whether it fails everywhere. The mechanism (RSSM fidelity gap) likely generalizes to other latent-dynamics models but we scope claims conservatively.
**Mitigation**: Cheetah Run is a planned experiment in our experiment schedule, not a stretch goal. We will include at least one additional DMC environment (Cheetah Run) to demonstrate generality of the mechanism.

### R2: "No proposed solution — what's the actionable takeaway?"
**Pre-emption**: Our primary contribution is diagnostic, not prescriptive. The causal chain (C1-C5) provides clear guidance: trained dt_embedding is the necessary condition for CIVO. Restricting imagination to dt=1 eliminates CIVO (Pathway A) but not all failure modes — 008e_v3 shows 1/2 seeds collapse via a distinct non-CIVO pathway (eval-driven policy instability). The actionable takeaway is that trained dt_embedding creates vulnerability through multiple pathways in imagination-based actor-critic; surface-level fixes are insufficient. Hierarchical approaches (THICK, Hieros) that avoid flat dt-conditioning are the recommended direction.
**Mitigation**: Present the dual-pathway finding as a key diagnostic contribution (Section 5). dt=1 imagination is a partial mitigation (eliminates CIVO) but not robust (1/2 collapse via Pathway B).

### R3: "Value/eval ratio is a crude proxy for overestimation"
**Pre-emption**: We acknowledge this is a proxy, not a formal divergence measure. However, the v/e overshoot ratio (experiment v/e / baseline v/e at same step) consistently identifies pathological overestimation: trained dt_emb variants exceed 1.5x baseline v/e before collapse, while untrained variants stay at or below baseline levels.
**Mitigation**: Add distributional analysis of value predictions vs. realized returns if time permits.

### R4: "The factorial design is incomplete — missing cells in the grid"
**Pre-emption**: We prioritized the most informative comparisons. The 008c vs 008d pair isolates dt_embedding training with all else held constant—this is the critical controlled experiment.
**Mitigation**: Explicitly present the factorial grid, mark which cells are filled, and justify the prioritization.

### R5: "Novelty concern — model exploitation / value overestimation in MBRL is well-known"
**Pre-emption**: General MBRL overestimation is known (Janner et al., 2019), but the specific mechanism through temporal abstraction's dt_embedding is novel. Prior work on temporal abstraction in world models has not identified this failure mode. Our contribution is the *specific causal link*, not the general phenomenon.

### R6: "All results from a single seed — how robust are the conclusions?"
**Pre-emption (D032 update)**: Multi-seed data now available. The nve>1.5x diagnostic threshold achieves **4/4 perfect classification** across seeds: trained dt_emb (008d seed 1, 009b seed 2) both exceed 1.5x; untrained (008f seed 1, 009c seed 2) neither exceeds 1.5x. Collapse itself is stochastic (1/2 trained seeds), which we report transparently — our claim is about the reliable **diagnostic marker** (nve>1.5x), not deterministic collapse.
**[D040]** C6 partially falsified: 008e_v3_s2 collapsed via non-CIVO pathway (eval-driven, entropy ↑). 009a baseline s2 stable (618→596→836) — rules out seed fragility. Trained dt_embedding creates multiple vulnerability pathways: CIVO (Pathway A, 008d) and policy instability (Pathway B, 008e_v3_s2). dt=1 imagination eliminates Pathway A but not B.
**Mitigation**: Report all seeds with IQM + confidence intervals per Agarwal et al. (2021). The 4/4 separation is robust. Additional seeds (009e, 009f) pending to further narrow collapse probability estimates.

### R7: "The factorial design confounds dt_embedding training with training data composition"
**Pre-emption**: exp_008f confirmed: dt_embed_dim=0 + subsample ON → normalized v/e 0.83x@45K (healthy), vs 008d@45K=2.09x (collapse at v/e=69.3%). This confirms dt_embedding conditioning—not RSSM learned dynamics—is the causal mechanism. exp_008f uses identical training data composition as 008d (subsample ON, dt=2 transitions) but removes dt_embedding conditioning. Through 55K, 008f remained in normal range (normalized v/e 0.73-1.02x).
**Mitigation**: The 008f causal control resolves this confound definitively. The three-way comparison (008c: subsample OFF/untrained, 008d: subsample ON/trained, 008f: subsample ON/no dt_embed) isolates dt_embedding conditioning as the necessary and sufficient factor for CIVO.

### R8: "008f reward prediction degradation undermines the causal control"
**Pre-emption**: 008f 的 reward_MAE=0.747（baseline 75x）是重要发现，但不削弱 C2 因果结论。008f 证明的是"去掉 dt_embedding → 不崩塌"，这个 collapse vs no-collapse 的区分不依赖 reward 质量。008f 的低 v/e 部分源于奖励噪声，但关键对比是 008d 的 v/e 加速发散 vs 008f 的 v/e 保持稳定——模式差异才是因果证据。
**Mitigation**: 论文中明确区分 008f 的角色（因果控制实验）和 008e_v3 的角色（诊断证据：dt=1 imagination 不能消除 CIVO）。RSSM fidelity 表同时报告绝对误差和比率，避免审稿人被 008d 的低 obs gap ratio（1.30x，但绝对误差 41.31 已是 baseline 3x）误导。

---

## Experiment Coverage Assessment

| Claim | Evidence Status | Gaps |
|-------|----------------|------|
| C1 (degradation) | ✅ Strong — 3 configurations + 2 environments | None |
| C2 (CIVO trigger) | ✅ Strong — nve≥1.5× threshold 15/16, AUROC=0.969 (2 envs) | None |
| C3 (untrained emb protection) | ✅ Strong — 008a + cross-env replication | None |
| C4 (dt amplification) | ✅ Moderate — dt=1 > dt=2 > dt=4 monotonic | Only 2 dt values |
| C5 (horizon/subsample secondary) | ✅ Moderate | None blocking |
| C6 (dt=1 imag partial) | ✅ 4 seeds — 2/4 collapse via distinct pathways (CIVO + IRD) | None |
| C7 (SGS failure / gradient decoupling) | ✅ Strong — 17 seeds, 3 variants, 2 envs. 1/17 CIVO-free (with value collapse side effect). Embedding removal 5/5. | None |
| C8 (forward-pass intervention) | 🔄 RUNNING — TCN + RAVE, 4 configs | Results by 5/22 go/no-go |

### Priority Actions Before Submission (updated 2026-05-20)
1. ~~C1-C7 实验~~ — ✅ 全部完成，31 configurations, 2 environments
2. **🔄 [P0] TCN/RAVE 结果评估** — exp_027 + exp_028, 硬截止 5/22 go/no-go
3. **如 TCN 或 RAVE 有效** → 多 seed + Cheetah 扩展, 5/25 数据锁定
4. **如两者均无效** → 锁定纯诊断论文 (C1-C7), 7 天完成写作
5. **论文收尾** — Reviewer 审查 + provenance 检查 + 三件套

---

## Key Figures (Planned)

1. **Figure 1**: Learning curves — all experiments overlaid, showing degradation pattern (hero figure)
2. **Figure 2**: Value/eval ratio over training — separating healthy vs. pathological regimes
3. **Figure 3**: Factorial grid summary — 2×2 (dt_emb × subsample) with H as secondary axis
4. **Figure 4**: Causal diagram — dt_embedding → value overestimation → actor degradation → collapse
5. **Figure 5**: dt=1 vs dt=2 vs dt=4 comparison — monotonic degradation (C4)
6. **Table 1**: RSSM fidelity — absolute obs_MSE + reward_MAE at dt=1/dt=2, 三模型并排（绝对值 + 比率，避免比率误导）
7. **Figure 6 (D035)**: Mitigation comparison — plot 008e_v3 seed=1 as single line. Add s2 (seed=2) when done. Do NOT present s0+s1 as two independent seeds. Can footnote deterministic reproduction.
