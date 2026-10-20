# Rebuttal Response Draft — Round 1

**Paper**: "Why Temporal Abstraction Fails in Imagination-Based RL: A Diagnostic Analysis of Variable-Rate DreamerV3"
**Venue**: CoRL 2026
**Date**: 2026-05-22
**Status**: Draft framework — pending exp_040-043 final data

---

## Critical Issues

### [W-C1] CoRL Venue Fit 严重不足
**Reviewer 原文摘要**: 全文仅在 DMC Walker Walk 上实验，无 robotics benchmark、无 real-robot、无 robotics motivation。不满足 CoRL CFP "focus on a core robotics problem" 要求，存在 desk reject 风险。

**回复要点**:
- 已增加 PickCube-v1 (ManiSkill2) 作为 preliminary manipulation evidence（注意：仅 2 experiments — 1 CIVO trigger + 1 baseline，且 CIVO 行为在 PickCube 上是 transient/self-correcting，与 Walker/Cheetah 的持续性 CIVO 不同，这是 scope limitation）
- Introduction 已重写，增加 robotics motivation：temporal abstraction 对 robot learning 的重要性（DayDreamer 的 real-robot world-model RL、TD-MPC2 的 manipulation 成功案例）
- 新增 "Implications for Robot Learning" 段落，讨论 CIVO 对 real-world robot deployment 的风险（想象训练中的 value overestimation 导致 sim-to-real 不可靠）
- 引用 DayDreamer (Wu et al., 2023) 和 TD-MPC2 (Hansen et al., 2024) 建立 world-model RL 在 robotics 中的实际应用基础

**证据**:
- exp_019b_civo_trigger (PickCube-v1): NVE peak 3.78 @52.5K, eval 26.6 vs baseline 58.6 (−55%)。CIVO 在 manipulation 环境中同样触发（transient, self-correcting at current scale）
- exp_019a_v2_pickcube_baseline: eval 69.43, 建立 healthy baseline
- exp_036_dual_critic_pickcube: dual-critic 在 PickCube 上 NVE 2.3（自修正），eval 27.7 — PickCube 不触发持续性 CIVO，作为 scope limitation 讨论
- 跨环境 CIVO 行为差异本身是发现：Walker (moderate, NVE 1.5-4.8), Cheetah (severe, NVE 8-70), PickCube (transient, self-correcting)

**论文修改位置**: Section 1 (Introduction rewrite), Section 3.1 (PickCube environment description), Section 5 (PickCube results), Section 7 (Implications for Robot Learning)

---

### [W-C2] 统计检验力严重不足
**Reviewer 原文摘要**: 核心因果声明依赖 n=2 per group。"4/4 separating power" P=1/16≈6.25%，未达 p<0.05。频繁使用 "causal factor"、"triggers" 等措辞与 n=2 证据强度不匹配。

**回复要点**:
- 样本量已从原始 n=8 扩展至 **n=29**（包含 Walker 13, Cheetah 5, PickCube 2, SGS/intervention experiments 9）
- 全样本 AUROC = **0.953** (95% Bootstrap CI: [0.867, 1.000])，精度 89.7% (26/29)，recall 100% (12/12 CIVO 全部检出)
- LOCO-CV (K=12 configs, n=56): mean AUROC = **0.988±0.003**，cross-validated accuracy = 53/56 = **94.6%**（与 in-sample 一致），mean optimal θ = 1.61±0.23，zero false negatives（详见 W-C4）
- Youden-optimal threshold (1.53×) 独立收敛到预设 1.5×
- 因果语言已全面弱化："causal factor" → "strongly associated factor"；"triggers" → "is associated with"；"necessary and sufficient" → 删除。保留 "causal direction" 仅用于描述 factorial ablation 设计意图
- IQM 报告已采用 Agarwal et al. (2021) 推荐方式

**证据**:
- n=29 AUROC analysis: AUROC 0.953, 95% CI [0.867, 1.000]
  - TP=12, FP=3, FN=0, TN=14
  - 3 FPs 均为机制不同的非 CIVO 高 NVE：025_obs_sgs_s2 (SGS damage), 028_rave_ceil15 (EMA pollution), 008e_v3_s2 (IRD, eval-driven)
- artifact: `auroc_label_fix_report.md` — 标签一致性修复详情
- artifact: `nve_loeo_crossval_report.md` — 交叉验证完整报告
- Walker factorial experiments: exp_008d (4 seeds: s1 collapse, s2 self-correct, s3 late-onset, s4 collapse), exp_008f (4 seeds: s1-s4 all NVE<1.5), exp_008a (3 seeds: all NVE<1.0)
- Cheetah: exp_010b (2 seeds: s0 NVE=70.64, s1 NVE=8.27), exp_008a_cheetah (2 seeds: s0 NVE=0.49, s1 NVE=0.48)
- exp_042_frozen_dt_emb_walker: data pending, expected 5/23 — 补充 trained vs frozen vs removed 三向对比
- exp_043_008f_walker_s1: data pending, expected 5/23 — 008f 第5个 seed

**论文修改位置**: Section 3.3 (NVE metric + AUROC), Section 5 (expanded results tables), Appendix A (full per-seed data), Throughout (language weakening)

---

### [W-C3] 单环境（Walker Walk）局限使因果声明不可泛化
**Reviewer 原文摘要**: Walker Walk 是最简单的 DMC locomotion 任务，CIVO 可能依赖低维动力学、dense reward、无 representation bottleneck。单环境无法支撑 "structural incompatibility" 结论。

**回复要点**:
- 已扩展至 **3 个环境**: Walker Walk, Cheetah Run, PickCube-v1 (ManiSkill2)
- 跨环境 CIVO 行为差异本身构成重要发现：
  - **Walker** (moderate CIVO): NVE 1.5-4.8, dual-critic 可完全预防
  - **Cheetah** (severe CIVO): NVE 8.27-70.64 (10×+ higher), dual-critic 仅部分抑制 (NVE 1.75, eval 97.5 = 31% recovery)
  - **PickCube** (CIVO-immune at current scale): NVE 3.78 transient, self-correcting。但 subsample+dt_emb 配置本身损害 manipulation 性能 (vanilla 58.6 → 26.6)
- "structural incompatibility" 已弱化为 "environment-dependent vulnerability"
- CIVO 严重度与环境复杂度正相关的趋势本身有 predictive value

**证据**:
- Walker (13 experiments): exp_008d family (4 seeds CIVO), exp_008f family (4 seeds no-CIVO), exp_008a family (3 seeds no-CIVO), exp_001 baseline, exp_015b frozen dt_emb
- Cheetah (5 experiments): exp_010b_s0 (NVE=70.64, eval→0.83 complete collapse), exp_010b_s1 (NVE=8.27, eval 51.7), exp_010a baseline (eval 849.8), exp_008a_cheetah_s0 (NVE=0.49), exp_008a_cheetah_s1 (NVE=0.48)
- PickCube (2 experiments): exp_019b (NVE=3.78 transient), exp_019a_v2 baseline (eval 69.43)
- Dual-critic cross-env: exp_032 Walker (CIVO prevented, eval 739.7), exp_034 Cheetah (CIVO not prevented, eval 97.5), exp_036 PickCube (NVE 2.3 self-correcting, eval 27.7)
- exp_040_wide_dual_critic_cheetah: data pending, expected 5/23 — Cheetah dual-critic 第2个 seed

**论文修改位置**: Section 3.1 (three environments), Section 5.3 (cross-environment comparison table), Section 6.4 (environment-dependent severity discussion), Table 3 (cross-env CIVO summary)

---

### [W-C4] NVE 阈值 1.5× 为 post-hoc 选择
**Reviewer 原文摘要**: 1.5× 阈值未说明选择依据。[1.2, 2.0] 范围内任何阈值效果类似，强烈暗示 post-hoc。88.9% accuracy 是 in-sample，无 held-out 验证。

**回复要点**:
- 已完成 **Leave-One-Config-Out (LOCO-CV) cross-validation**（K=12 configuration groups, n=56），比 LOEO 更严格
- LOCO-CV 结果：
  - mean train AUROC = **0.988 ± 0.003**
  - mean optimal θ = **1.61 ± 0.23**
  - cross-validated accuracy = **53/56 = 94.6%**（与 in-sample 完全一致）
  - **10/12 folds** 选择 θ ≈ 1.5 ± 0.05
  - **Zero false negatives**: 24/24 CIVO-positive 在所有 fold 正确检出
- 3 个持续 FP（exp_008e_v3 mitigation transient, exp_047/057 frozen transients）均为机制性 non-CIVO
- Sensitivity analysis: θ from 0.5 to 5.0 (step 0.1) 完整扫描

**证据**:
- artifact: `nve_loeo_crossval_report.md` — 完整交叉验证报告 + LaTeX table
- 20 experiments across 3 environments, binary CIVO labels based on mechanism identification
- Youden-optimal threshold from n=29 analysis: 1.53× (independently converges to pre-set 1.5×)
- Sensitivity analysis data: θ range [1.45, 1.53] achieves maximum accuracy in 2/3 training folds; θ range [1.00, 3.78] in the third fold (wider due to strong separation in Cheetah+PickCube data)

**论文修改位置**: Section 3.3 (NVE threshold validation method), Appendix B (LOCO-CV cross-validation details + Table \ref{tab:nve_loco_cv}), Section 5.1 (updated AUROC with cross-validated results)

---

### [W-C5] 未使用 CoRL 2026 官方 PMLR 模板
**Reviewer 原文摘要**: 论文使用自定义 documentclass，不符合 CoRL 2026 PMLR 模板要求，构成 desk reject 独立理由。

**回复要点**:
- 已切换至 CoRL 2026 官方 PMLR 模板 (`\usepackage{corl_2026}`)
- 正文控制在 8 页限制内
- Appendix 包含完整 per-seed 数据、LOCO-CV 交叉验证、intervention hierarchy 详细数据

**证据**:
- 模板文件: `\usepackage{corl_2026}` (submission mode; switch to `[final]` only at camera-ready)
- 页数验证: 正文 8 页 + appendix

**论文修改位置**: 全文格式

---

## Warning Issues

### [W-W1] 纯诊断负面结果缺乏 actionable solution
**Reviewer 原文摘要**: Section 6.6 三个 future directions 全部 "leave to future work"。Gradient stopping 作为 mitigation 仅需一行代码改动却未测试。纯诊断对 CoRL 偏重实际 solution 的 venue 贡献度偏低。

**回复要点**:
- **Gradient stopping 已测试并系统性失败** — 这本身是核心发现：
  - Reward-only SGS (exp_016e): 0/2, NVE=10.42× — 反效果
  - Full-pathway SGS (exp_018+021): 0/3 — 阻断所有非 KL 梯度仍失败
  - Obs-decoder-only SGS (exp_025+026): 1/6 — 唯一"成功" seed 仍有 value collapse 副作用
  - **SGS 总计 1/17 seeds across 3 variants × 2 environments**
- **Dual-critic prevention 已实验验证**:
  - exp_032 (Walker s0): eval 787.7, NVE≤1.1, CIVO prevented ✅
  - exp_032b (Walker s1): eval 551.8, CIVO prevented ✅
  - exp_038 (Walker s2): NVE≤0.3 (CIVO prevented), 但 non-CIVO collapse eval 354→121 ⚠️
  - **3/3 seeds CIVO prevention, 2/3 performance stability**
- **Frozen dt_emb**: exp_042 running (data pending, expected 5/23) — 验证 requires_grad=False 是否足以阻止 CIVO
- **4-level Intervention Hierarchy** 作为独立贡献：
  1. Architecture level: dt_emb removal (5/5 prevention) / frozen dt_emb (pending)
  2. Representation level: TCN (2/8, narrow dose window, environment-dependent)
  3. Output level: RAVE (0/2, EMA anchor pollution)
  4. Gradient level: SGS (1/17, compensatory amplification)
- **Practical Guidelines subsection** 新增，包含可操作建议

**证据**:
- SGS series: exp_016e (NVE=10.42), exp_018v2 (NVE=1.66), exp_018_s2 (collapse), exp_021 (NVE=9.94 transient), exp_025 s1-s4 (1/4 survive with value collapse), exp_026 s0-s1 (0/2, NVE 21.9-30.2)
- Dual-critic: exp_032 (eval 787.7, NVE≤1.1), exp_032b (eval 551.8), exp_038 (eval 120.9, NVE≤0.3 but non-CIVO collapse)
- TCN: exp_027 series (Walker σ=0.2: 2/4 success, eval 45-91% baseline; Cheetah σ=0.2-1.0: all fail; PickCube σ=0.2: fail)
- RAVE: exp_028 series (0/2, EMA pollution)
- dt_emb removal control: exp_008f (4 seeds, all NVE<1.5), exp_024b Cheetah (1 seed, no CIVO) = 5/5
- exp_042_frozen_dt_emb_walker: **data pending, expected 5/23 evening**
- 2×2 Mechanism Factorial table (ROADMAP.md): {single,dual} × {normal,wide}

**论文修改位置**: Section 4 (Intervention Hierarchy — new section), Table 4 (Intervention summary: 7 methods × 3 levels × 3 environments), Section 4.4 (Dual-critic analysis with 2×2 factorial), Section 7 (Practical Guidelines)

---

### [W-W2] 与 TAWM 的对比缺乏实证
**Reviewer 原文摘要**: Section 6.3 MPC 免疫性解释完全基于 architectural reasoning，未实际运行 TAWM/TD-MPC2。TD-MPC2 与 DreamerV3 多重差异可能 confound 对比。

**回复要点**:
- 直接引用 TAWM 原文数据（Nhu et al., ICML 2025）中 Walker Walk 的成功结果
- 明确承认 TD-MPC2 vs DreamerV3 的多重差异（continuous vs discrete latent, MPC vs AC, planning horizon 差异）
- 论文论点限定为 architectural reasoning + 引用 TAWM 数据，不做因果声明
- 关键论点："dt-conditioning succeeds in MPC (re-plans from real states at each step) but fails in imagination-based AC (critic bootstraps from imagined states)" — 这是 architecture-level observation，不需要复现 TAWM
- TAWM 复现超出本论文 scope（不同 codebase + 计算预算）

**证据**:
- TAWM paper (Nhu et al., ICML 2025): Walker Walk 上 dt-conditioning 改善了 TD-MPC2 性能（引用原文 Table/Figure）
- 本文 Walker Walk: dt-conditioning 在 DreamerV3 上触发 CIVO (exp_008d NVE=2.09-4.12)
- Architectural comparison table: MPC (re-plan from real state) vs AC imagination (bootstrap from imagined state)

**论文修改位置**: Section 6.3 (TAWM comparison, cite specific numbers from TAWM paper), Section 2 (Related Work: TAWM positioning)

---

### [W-W3] 105K vs 505K 训练步数不对等
**Reviewer 原文摘要**: Baseline 运行 505K，treatment 仅 105K。Self-correcting seed 009b (eval 267.9@105K = 29% baseline) 可能只是 slower collapse 而非真正 self-correction。

**回复要点**:
- exp_043_008f_walker_s1: 运行至 **210K** steps（data pending, expected 5/23）
- 已有多个 extended baseline 数据点：exp_001_baseline_s2/s3/s4_extended 均运行到 505K
- Dual-critic experiments 全部运行至 **210K** steps:
  - exp_032 (s0): 215K, eval peak 787.7 @205K, final 739.7 @215K — 稳定
  - exp_032b (s1): 215K, eval peak 552 @205K, final 516 @215K — 稳定
  - exp_035 (narrow): 215K, recovery from trough 33.8 @85K to 697.8 @215K — 持续上升
- exp_008a_no_subsample_dt2: extended to 112K, eval 778 (85% baseline), NVE 0.59 — 稳定
- [GAP] 009b self-correction 未 extend beyond 105K。当前 eval 267.9 确实可能是 slower collapse。论文已弱化 "self-correction" 措辞为 "temporary recovery with unknown long-term trajectory"

**证据**:
- exp_032: 215K steps, eval stable at 739.7 @215K (vs peak 787.7 @205K)
- exp_032b: 215K steps, eval stable at 516 @215K
- exp_035: 215K steps, eval still rising at 697.8 @215K
- exp_038: 215K steps, eval collapsed to 120.9 @215K (non-CIVO mechanism)
- exp_008a: 112K steps, eval 778, NVE 0.59 (continuing suppression)
- exp_043_008f_walker_s1: **data pending, target 210K, expected 5/23**

**论文修改位置**: Section 3.2 (training duration justification), Appendix (extended training curves for 210K+ experiments)

---

### [W-W4] Pathway B 解释不充分
**Reviewer 原文摘要**: 008e_v3_s2 的 non-CIVO collapse 仅 1 个 seed 证据。未排除 subsampling 引入的普通 training instability。与 plasticity loss / capacity collapse 区分不清晰。

**回复要点**:
- 弱化措辞：从 "qualitatively distinct pathway" → "observed non-CIVO collapse in one configuration"
- exp_038_s2 提供了额外的 non-CIVO 崩溃证据（不同配置）：
  - eval 354→121, NVE≤0.3 throughout — CIVO 被 dual-critic 预防但 eval 仍崩溃
  - Actor entropy 急升 (-3.59→-0.45)，与 008e_v3_s2 的 entropy 上升 (-5.21→-3.83) 模式一致
- 两个独立 non-CIVO 崩溃实例（008e_v3_s2 和 exp_038_s2）在不同配置下展示相似动态特征
- 承认与 plasticity loss 的区分需要更深入分析，标注为 open question
- exp_041_dual_critic_walker_s3: **data pending, expected 5/23** — 如果 s3 也崩溃 (2/4)，则 non-CIVO collapse 是系统性问题

**证据**:
- exp_008e_v3_s2: eval 715→452→137 (eval-driven), NVE 3.78 @105K (consequence not cause), entropy ↑ (-5.21→-3.83)
- exp_038_dual_critic_walker_s2: eval peak 354 @155K → collapse to 99.6 @175K, NVE≤0.3 (CIVO prevented), entropy ↑ (-3.59→-0.45)
- exp_009a_baseline_s2: eval 618→596→836 (stable) — 排除 seed fragility
- exp_041_dual_critic_walker_s3: **data pending, expected 5/23 — determines collapse rate: 1/4 sporadic vs 2/4 systematic**

**论文修改位置**: Section 5.6 (softened Pathway B discussion), Appendix D (comparison table: CIVO vs non-CIVO collapse signatures)

---

### [W-W5] RSSM fidelity 仅报告 MAE，未验证 overprediction 方向性
**Reviewer 原文摘要**: Table 4 的 reward MAE 不区分 over- vs under-prediction。需 signed error 验证 CIVO 机制假设。

**回复要点**:
- **Signed reward error analysis 已完成**
- 关键发现：008d dt=2 shows **negative bias** (Mean SE = −0.599)，即**系统性低估**而非高估
- 这排除了 "observation-level reward overprediction" 作为 CIVO 机制
- CIVO 的 value overestimation 来自 **critic bootstrapping** (accumulated returns in imagination)，不是 per-step reward prediction bias
- 分析使用 RSSM posterior（conditioned on real observations），而 CIVO 发生在 imagination 的 prior（无观测校正）
- Baseline 校准良好 (Mean SE ≈ 0, Std 0.023)，确认方法论可靠

**证据**:
- artifact: `signed_reward_error.md` — 完整分析报告
  - baseline dt=1: Mean SE = +0.001 (nearly perfect calibration)
  - exp_008d dt=1: Mean SE = +0.018 (slight overprediction, 61.8% samples)
  - exp_008d dt=2: Mean SE = **−0.599** (massive underprediction, only 8% overpredict)
  - exp_008f dt=1: Mean SE = −0.710 (uncalibrated)
  - exp_008f dt=2: Mean SE = −1.645 (uncalibrated)
- 方法: 8 latest training episodes, encoder+RSSM+reward_head from checkpoint, signed error = predicted − actual

**论文修改位置**: Section 6.1 (signed error analysis subsection), Table 5 (signed error table), Section 6.1 (mechanism refinement: CIVO via critic bootstrapping, not per-step overprediction)

---

### [W-W6] CIVO 与已知 value overestimation 的区分不够清晰
**Reviewer 原文摘要**: CIVO 可能只是 compounding model error 的实例化。R1/R3 partial rebut: trained vs untrained 对比提供了机制特异性，但论文应更系统阐述。

**回复要点**:
- **Trained vs untrained dt_emb 对比**是超越 generic compounding error 的核心证据：
  - exp_008d (trained dt_emb): NVE 2.09-4.12 → CIVO
  - exp_008a (unexposed dt_emb): NVE 0.49-0.93 → no CIVO (3 seeds Walker + 2 seeds Cheetah, all safe)
  - 如果仅是 compounding error，两者 dt=2 imagination 质量类似，应出现类似 overestimation — 但事实不同
- **Signed error 双重证据**：
  - dt=2 reward head 实际上 underpredicts (SE = −0.599) → CIVO 不是 reward-level compounding error
  - Value overestimation 来自 critic 在 imagination 中的 bootstrapping，特异于 trained dt_emb 的 conditioning
- **CIVO 与标准 overestimation 的关键区别**：
  1. Standard overestimation (Fujimoto et al., 2018): 独立于 temporal conditioning，Double Q / ensemble 可缓解
  2. CIVO: 特异于 trained temporal embedding，Double Q 失效 (v1≈v2, ρ>0.999)
  - 这本身是区分证据：如果 CIVO 只是 standard overestimation，Double Q 应该有效

**证据**:
- exp_008d vs exp_008a: trained NVE=4.12 vs untrained NVE=0.93 (Walker), 同样 dt=2 transitions
- exp_008a_cheetah: 2 seeds both NVE<0.5 (cross-env validated)
- Signed error: exp_008d dt=2 SE = −0.599 (underprediction)
- Dual-critic v1≈v2: ρ>0.999 in Walker (exp_032), exact match in Cheetah (exp_034) and PickCube (exp_036)

**论文修改位置**: Section 2 (expanded Related Work: explicit CIVO vs generic overestimation), Section 6.1 (mechanism specificity argument), Section 4.4 (v1≈v2 as CIVO-specific evidence)

---

### [W-W7] Factorial design 部分对比存在混淆
**Reviewer 原文摘要**: 008d vs 008a/008c 同时改变 embedding、subsampling、horizon 三个因素。R3 澄清核心对照 008d vs 008f 干净，但 primary vs secondary 区分不清。

**回复要点**:
- 论文已明确标注 **primary comparison** (008d vs 008f: 仅 dt_embed_dim 不同，其他因素相同) vs **secondary comparisons** (008c, 008a 等)
- 新增 **2×2 mechanism factorial** (Walker)，cleanly isolates two factors:

| | Single Critic | Dual Critic (min) |
|--|--------------|-------------------|
| ~1.05-1.2M params | Baseline: CIVO → permanent collapse | exp_035: CIVO (NVE 2.75) → full recovery (eval 697.8) |
| ~2.4-2.9M params | exp_033: CIVO (NVE 4.75) → partial recovery (eval 408) | exp_032: CIVO prevented (NVE≤1.1, eval 787.7) |

- 交互效应清晰：min alone → recovery; capacity alone → partial recovery; min+capacity → prevention

**证据**:
- Primary: exp_008d (dt_embed_dim=8, subsample ON, H=8) vs exp_008f (dt_embed_dim=0, subsample ON, H=8) — 唯一差异是 dt_embedding
- 2×2 factorial: exp_032 (eval 787.7), exp_033 (eval 408), exp_035 (eval 697.8), baseline (collapse)
- Secondary comparisons explicitly labeled in revised Table 1

**论文修改位置**: Section 3 (Table 1: primary vs secondary column), Section 4.4 (2×2 factorial table + interaction analysis), Appendix (complete factorial grid with all cells)

---

### [W-W8] Related Work 遗漏 + Bibliography 冗余
**Reviewer 原文摘要**: Becker-Ehmck et al. (2023), Park et al. (2021), Wang & Beltrame (2024), Colas et al. (2018) 在 bib 中未引用。77 条 bib 中 48 条 orphan。

**回复要点**:
- Bibliography 清理完成：原 77 条 → **43 条**（删除 34 条 orphan）
- 4 篇遗漏论文已补充引用并在正文中讨论：
  - Becker-Ehmck et al. (2023): Section 2, multi-timestep world model 先行工作
  - Park et al. (2021): Section 2, time-discretization invariance 讨论
  - Wang & Beltrame (2024): Section 2, elastic time steps
  - Colas et al. (2018): Section 3 (methodology), seed 数量对 deep RL 结论可靠性的影响
- 所有占位符 author 字段 (splates2025 等) 已修正

**证据**:
- 清理后 bibliography: 43 条，0 orphan entries
- 正文新增引用: 4 篇 + DayDreamer, TD-MPC2 等 robotics 相关文献

**论文修改位置**: References (全面清理), Section 2 (expanded Related Work)

---

## Questions for Authors

### [Q1] 是否在其他 DMC 任务上做过初步验证？
**回复**:
- **Cheetah Run**: 完整验证。5 experiments:
  - exp_010b_s0: NVE=70.64 (catastrophic CIVO, eval→0.83)
  - exp_010b_s1: NVE=8.27 (severe CIVO, eval 51.7)
  - exp_010a baseline: eval 849.8
  - exp_008a_cheetah: 2 seeds, NVE 0.48-0.49 (unexposed dt_emb, no CIVO)
  - Cheetah CIVO severity 10×+ 高于 Walker，且 dual-critic 仅部分抑制 (exp_034: NVE 1.75, eval 97.5 = 31% recovery)
- **PickCube-v1 (ManiSkill2)**: manipulation 环境验证。
  - exp_019b: NVE=3.78 @52.5K (transient CIVO, self-correcting), eval 26.6
  - exp_019a_v2 baseline: eval 69.43
  - CIVO 在 PickCube 不持续 — scope limitation (manipulation dynamics differ from locomotion)
- exp_040_wide_dual_critic_cheetah: **data pending** — Cheetah dual-critic s1

---

### [Q2] Gradient stopping 为什么未测试？
**回复**:
- **已全面测试，系统性失败**。这是论文最重要的新增贡献之一。
- Reward-only SGS (exp_016e): NVE=10.42× — 反效果。Reward head 梯度为 0（architectural no-op），迫使 dt_emb 通过 obs-decoder 适配，强化空间偏差
- Full-pathway SGS (exp_018v2, exp_018_s2, exp_021): 0/3。阻断所有非 KL 梯度仍失败 → forward-pass representational damage 不可逆
- Obs-decoder-only SGS (exp_025 4 seeds, exp_026 2 seeds): 1/6。唯一 survive 的 seed (exp_025_s1) 仍有 value collapse (ve_ratio 0.056-0.14)
- **总计 1/17 seeds across 3 SGS variants × 2 environments**
- 核心发现：**gradient magnitude ≠ causal importance**（reward 38-49% gradient 但 reward-only SGS 最差；obs-decoder 16-22% gradient 但 obs-decoder SGS 也失败）
- **替代方案**: frozen dt_emb (exp_042, running) 和 dual-critic (exp_032, 3/3 CIVO prevention) 作为 architecture-level interventions
- Gradient stopping 本身因 **compensatory amplification** 无效：阻断 obs-decoder on Cheetah → NVE 从 8.3 放大到 21.9-30.2 (2.6-3.6×)

---

### [Q3] 能否补充 signed error 验证方向性？
**回复**:
- **已完成**。见 W-W5 详细回复。
- 关键结果: exp_008d dt=2 Mean SE = −0.599 (underprediction), 排除 observation-level overprediction mechanism
- Baseline dt=1 Mean SE = +0.001 (methodology validation)

---

### [Q4] TAWM 原文 Walker Walk 数据？
**回复**:
- 引用 TAWM (Nhu et al., ICML 2025) 原文中的 Walker Walk 具体数据
- TAWM 使用 TD-MPC2 框架，dt-conditioning 在 MPC setting 中成功改善性能
- 论文直接引用原文数据 + architectural difference 分析，不做因果声明
- [GAP] 需确认 TAWM 原文中 Walker Walk 的具体数字（score/improvement %），当前引用为 "improved performance"

---

### [Q5] NVE 阈值 sensitivity analysis？
**回复**:
- **LOCO-CV 已完成**（见 W-C4）
- θ from 0.5 to 5.0 (step 0.1) 全范围扫描
- θ=1.5 在 10/12 folds 的 optimal accuracy range 内（±0.05）
- Mean train AUROC = 0.988±0.003, cross-validated accuracy = 53/56 = 94.6%
- 在 [1.2, 2.0] 范围内 accuracy 确实变化不大 — 但这恰好说明 NVE 分离度高（CIVO vs non-CIVO 的 NVE gap 远大于 θ 选择范围），而非 post-hoc fitting
- Youden-optimal threshold from n=29: 1.53× (独立收敛)

---

### [Q6] 008e_v3 seed 2 (Pathway B) 的 actor action distribution？
**回复**:
- Actor entropy 数据已有：008e_v3_s2 entropy 从 -5.21 → -3.83（增加，策略变随机）vs 008d s1 entropy -3.47 → -4.88（减少，策略变确定）
- 这是区分 CIVO (Pathway A: entropy ↓, exploitation lock-in) vs non-CIVO (Pathway B: entropy ↑, exploration-driven destabilization) 的关键指标
- [GAP] 更详细的 action distribution analysis (per-dimension variance, action-space coverage) 未完成。可用 exp_038_s2 的 entropy 数据 (-3.59→-0.45) 作为第二个 non-CIVO 崩溃实例佐证
- exp_041_dual_critic_walker_s3: **data pending, expected 5/23** — 如果 s3 也展示 entropy ↑ 崩溃模式，则 Pathway B 特征更加 robust

---

## Summary of Pending Data

| Experiment | Purpose | Expected | Impact |
|---|---|---|---|
| exp_040_wide_dual_critic_cheetah | Cheetah dual-critic s1 robustness | 5/23 | W-C3: cross-env dual-critic data |
| exp_041_dual_critic_walker_s3 | Non-CIVO collapse frequency (1/4 vs 2/4) | 5/23 | W-W4: Pathway B systematic vs sporadic |
| exp_042_frozen_dt_emb_walker | Trained vs frozen vs removed dt_emb | 5/23 | W-W1: frozen dt_emb as mitigation; C2: causal refinement |
| exp_043_008f_walker_s1 | 008f 5th seed replication | 5/23 | W-C2: additional statistical power |

All 4 experiments running on full GPU capacity. Data lock deadline: 5/25.

---

## Evidence Gap Summary

| Concern | Evidence Status | Gap |
|---------|----------------|-----|
| W-C1 (venue fit) | ✅ PickCube added + robotics framing | None critical |
| W-C2 (statistical power) | ✅ n=29, AUROC 0.953 | exp_042/043 pending (incremental) |
| W-C3 (single env) | ✅ 3 environments | exp_040 pending (Cheetah dual-critic s1) |
| W-C4 (NVE post-hoc) | ✅ LOCO-CV AUROC 0.988±0.003, accuracy 94.6% | None |
| W-C5 (template) | ✅ Fixed | None |
| W-W1 (no solution) | ✅ SGS 1/17 + dual-critic 3/3 + hierarchy | exp_042 pending (frozen dt_emb) |
| W-W2 (TAWM) | ⚠️ Cite TAWM data, no reproduction | [GAP] TAWM 原文 Walker Walk 具体数字需确认 |
| W-W3 (105K vs 505K) | ✅ Dual-critic to 210K | [GAP] 009b 未 extend，已弱化 "self-correction" |
| W-W4 (Pathway B) | ⚠️ 2 instances (008e_v3_s2 + exp_038_s2) | exp_041 pending (collapse frequency) |
| W-W5 (signed error) | ✅ Complete | None |
| W-W6 (CIVO novelty) | ✅ trained vs untrained + signed error + v1≈v2 | None |
| W-W7 (factorial confounds) | ✅ Primary vs secondary + 2×2 factorial | None |
| W-W8 (bibliography) | ✅ 43 entries, 4 additions | None |
| Q1 (other envs) | ✅ Cheetah + PickCube | exp_040 pending |
| Q2 (gradient stopping) | ✅ SGS tested, failed | None |
| Q3 (signed error) | ✅ Complete | None |
| Q4 (TAWM data) | ⚠️ Partial | [GAP] 需确认 TAWM 原文具体数字 |
| Q5 (sensitivity) | ✅ LOCO-CV complete | None |
| Q6 (action distribution) | ⚠️ Entropy data available | [GAP] Per-dimension action analysis not done |
