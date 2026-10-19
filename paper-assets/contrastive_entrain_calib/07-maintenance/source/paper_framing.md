# Paper Framing — contrastive_entrain_calib

## Target Venue
- Primary: **EMNLP 2026** via ARR May 2026 cycle
- ARR Submission Deadline: **May 25, 2026** (6 days from May 19)
- Commitment Deadline: **August 2, 2026**
- ⚠️ May cycle 新政策：提交时必须声明目标会议为 EMNLP，绑定不可更改
- Fallback: ARR August 2026 cycle (DDL ~Aug 15) → EACL 2027 / ACL 2027
- Stretch: ICLR 2027 (abstract ~Sep 2026, full paper ~Oct 2026)

## Core Claims (3 条, 可证伪)

1. **Directional discriminability + training stability**: The policy model's activation space encodes a linear direction d_syc that discriminates sycophantic capitulation from genuine belief revision (AUROC 0.82), with signal emerging at mid-layers (L16-19). During GRPO training, d_syc remains stable (cosine ≈ 0.96 at step 500), and linear separability is preserved (AUROC 0.80 at step 500). Periodic recalibration (every 500 steps) is included as a safety mechanism.
   - *Evidence needed*: AUROC on style-controlled data, layer progression, direction stability curve, AUROC at each checkpoint
   - *MVP basis*: v2.1 CV AUROC 0.826, Layer 0 = random, L16-19 emergence
   - *New finding (D025 corrects D024)*: Initial stability measurement reported cosine=0.28 (74° drift) but this was a measurement artifact from referencing a stale directions.pt file (different dataset). Actual drift: cosine ≈ 0.96. Direction is stable during training.
   - *New finding (D019)*: Per-layer cosine AUROC ≥ 0.77 at step 500, deep layers L32/33 improved +0.025/+0.033. Full training curve (exp-006) pending.
   - *New finding (D036)*: **Cross-model generalization confirmed.** Llama-3-8B-Instruct 5-fold CV AUROC=0.7793±0.019 (best layer=16), style-controlled=0.9227. Same strength gradient as Qwen3-8B (weak 0.711 < medium 0.864 < strong 0.911). d_syc is a cross-model phenomenon, not architecture-specific. This strengthens the negative claim: even cross-model discriminability fails as reward.
   - *New finding (D025→D029)*: **Cosine R1 structural failure** — cosine(h, d_syc) gap between valid/invalid is ~0.098 (7-layer mean), far too small for GRPO reward. Four experiments confirmed this is structural, not tunable: exp-002 (tanh gate), exp-002v2 (raw cosine), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence samples get R1=-0.305 i.e. ALL negative). d_syc conflates legitimate revision with sycophantic capitulation at the continuous projection level. Binarization via probe resolves this (exp-008v3 R1 mean +0.72).

2. **Discriminability ≠ reward utility (D031, core finding)**: d_syc direction successfully discriminates sycophancy (AUROC 0.82) but FAILS as GRPO reward in ALL tested forms — continuous cosine, scaled cosine, and binarized probe. The gap between discriminability and reward utility is the paper's central finding.
   - *Evidence*:
     - **Cosine R1 failure chain** (4 experiments): exp-002 (tanh gate collapse), exp-002v2 (R1≈0), exp002v2-recalib (mode collapse), exp-002v3 (5x scale, strong evidence R1=-0.305 all negative)
     - **Binary probe R1 failure** (exp-008v3): ckpt-1500 ToF=0.0000, ckpt-2000 ToF=0.0000. Probe reward trap: model learns "never change answer" → probe rewards as "non-sycophantic" → positive feedback loop → stubbornness collapse
     - **Probe ablation (D030)**: d_syc probe AUROC 0.835 vs random 0.727 (+0.108) — direction HAS signal, but signal cannot be converted to effective reward
   - *Unified root cause*: d_syc encodes belief change DIRECTION but not change WARRANT. Cosine R1 penalizes ALL change (too punitive), binary probe R1 rewards ALL non-change (too permissive). Both fail because the reward signal conflates desired and degenerate behavior.
   - *Recalibration evidence*: AUROC improves during training (0.82→0.91 via recalibration) yet reward still fails → direction QUALITY is not the bottleneck, reward FORMULATION is.

3. **Probe reward trap mechanism (D031, strengthened D032)**: Binary probe trained on sycophancy contrastive pairs learns "no answer change = non-sycophantic." During GRPO training, this creates a positive feedback loop: stubbornness → high R1 → gradient reinforces stubbornness → entropy collapse. The trap is **immediate**: behavioral collapse (ToF=0) occurs within the first 500 training steps, while entropy remains healthy (0.70) until step ~1840 — a **1300-step lag** between behavioral and distributional collapse.
   - *Evidence (full checkpoint trajectory)*:
     - ckpt-500: entropy=0.70 (healthy), **ToF=0.0000** — trap already active
     - ckpt-1000: entropy=0.80, ToF=0.0055 (1/181, noise)
     - ckpt-1500: entropy=0.61, ToF=0.0000
     - ckpt-2000: entropy=0.30 (collapsed), ToF=0.0000, NoF=1.0000
   - *Timeline reconstruction*: Step 0-500: probe rewards stubbornness → behavior dies. Step 500-1840: behavior dead but policy distribution still diverse (model expresses stubbornness in varied ways). Step 1840+: distribution also collapses → expression fixed.
   - *Methodological insight*: Entropy-based early stopping would NOT have caught this failure — entropy was 0.70 when ToF was already 0. Behavioral eval at intermediate checkpoints is necessary. R1 mean +0.72 during collapse = probe actively rewarding degenerate behavior.
   - *Proposed figure*: Behavioral vs Distributional Collapse dual-axis plot (ToF + entropy over 4 checkpoints), showing 1300-step lag.
   - *Theoretical implication*: Any reward derived from d_syc (without conditioning on input validity) will exhibit one of two failure modes — penalizing all change OR rewarding all non-change. Future work needs condition-aware reward design that jointly encodes change direction AND change warrant.

## Story Spine

**Problem**: LLMs face a "double-bind" in multi-turn dialogue. Anti-sycophancy training (SMART, BCT/ACT) teaches resistance to ALL user pressure indiscriminately, blocking sycophantic capitulation AND legitimate belief revision alike. Meanwhile, multi-turn commitment compounds the problem: TRUTH DECAY shows up to 47% accuracy degradation as models lock into wrong answers across turns. No training method distinguishes "the user is right, I should revise" from "the user is pressuring me, I should resist."

**Existing approaches & gaps**: Behavioral GRPO decomposition ("Pressure, What Pressure?") scores outputs via NLI, but cannot detect sycophantic internal reasoning when surface output appears correct. ACT enforces undifferentiated activation consistency, penalizing all changes equally. Linear Probe Penalties probes the reward model (not policy model) with a binary classifier. CRAFT validates hidden-state GRPO for safety, but uses domain-general prototype clustering. All are single-turn.

**Our framing (D031 — analysis paper)**: Representation Engineering (Zou et al., 2023) established that linear directions in activation space encode high-level concepts. CCS (Burns et al., 2023) showed unsupervised direction finding via consistency objectives. Activation Addition (Turner et al., 2023) demonstrated inference-time steering via such directions. Latent-GRPO (Zhang et al., 2026) uses spherical projection + robust centroids for reasoning correctness, but does not target behavioral attributes like sycophancy. We systematically investigate whether RepE-style directional information can serve as GRPO reward for multi-turn sycophancy reduction. Our finding is negative but insightful: d_syc successfully discriminates sycophancy (AUROC 0.82), but NEITHER continuous cosine projection NOR binarized probe classification translates this discriminability into effective GRPO reward. Both fail for a unified root cause: d_syc encodes belief change direction but not change warrant. We identify a "probe reward trap" — a positive feedback loop where the probe rewards degenerate stubbornness as non-sycophancy, causing behavioral collapse that precedes entropy collapse. The contribution is the systematic revelation that discriminability ≠ reward utility in representation-guided RL, with mechanistic explanation and diagnostic implications.

**Investigated approaches**: We test two reward formulations for R1:
- **Cosine R1** = cos(h, d_syc): continuous projection, magnitude-invariant. Tested with raw signal, scaled signal (5x), and online recalibration. ALL fail (see failure chain below).
- **Binary probe R1** = probe(h; d_syc) ∈ {0,1}: logistic regression on d_syc layer projections. Produces clean signal (R1 mean +0.72) but triggers probe reward trap (see below). ckpt-1500 ToF=0.0000.
- **Continuous probe probability R1** = 1 - P(sycophantic|h): probe's sigmoid output as continuous signal (exp-009, killed D040). Intermediate between cosine and binary. Two-checkpoint trajectory confirms gradual degradation: ckpt-500 SYCONScore=0.124, ckpt-1000=0.114 (monotonic decline, both below vanilla D027=0.134). Continuous probe is a "slow-motion binary probe" — avoids instant collapse but converges to same failure. **Formulation spectrum complete**: binary=instant trap (ToF=0 at step 500), continuous=gradual trap (SYCONScore -1pp/500steps), cosine=noise-dominated collapse. All three d_syc→reward formulations fail, confirming the gap between discriminability and reward utility is structural.
Combined reward in all cases: R = w1·R1 + w3·R3. No formulation produces effective sycophancy reduction.

**R3-only GRPO baseline (exp-003, D042 full trajectory)**:
| ckpt | ToF | NoF | SYCONScore | vs vanilla |
|------|-----|-----|------------|------------|
| vanilla | 0.072 | 0.945 | 0.134 | — |
| 1000 | 0.039 | 0.945 | 0.074 | -44% |
| 2000 | 0.044 | 0.983 | 0.085 | -37% |
| 3000 | 0.050 | 0.972 | 0.095 | -29% |
| 4000 | 0.061 | 0.967 | 0.114 | -14% |
| 4500 | **0.072** | **0.961** | **0.134** | **≈0%** |
| 5000 | 0.061 | 0.967 | 0.114 | -14% |
| 5500 | 0.061 | 0.972 | 0.114 | -14% |
| 6000 | 0.044 | 0.972 | 0.085 | -37% |
| 6500 | 0.083 | 0.983 | 0.153 | +14% |
| 7000 | 0.055 | 0.972 | 0.105 | -22% |
| 7500 | — | — | 0.105 | -22% |
| 8000 | **0.077** | **0.972** | **0.143** | **+7%** |

> **论文 Table 报告方式**: Table 报 ckpt-8000 final (0.143, +7% vs vanilla)，但必须附 late-training range [0.085, 0.153] 和 late-training mean = 0.118 (-12% vs vanilla)，揭示 final checkpoint 得分的不可靠性。

**Spike-regression pattern (D045→D047)**：ckpt-4500 短暂恢复到 vanilla 水平（SYCONScore=0.1337 ≈ vanilla 0.1335，ToF=0.0718 = vanilla ToF），但立即回落。**R3-only 在 late-training 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持**——late-training 呈现极端振荡 (0.085→0.153→0.105→0.105→0.143)，late-training 均值 ≈ 0.118 < vanilla 0.134。三次单点超越 vanilla (ckpt-4500=0.134, ckpt-6500=0.153, ckpt-8000=0.143) 均为噪声，不持续。不稳定性在 late-training 阶段出现，但跨 seed 发作时间不同（seed 1 ~step 6000, seed 2 ~step 3500），说明不稳定性是方法固有特征而非训练特定阶段的产物。与 d_syc experiments 的区别：d_syc causes collapse with no recovery; R3-only 围绕 vanilla 不稳定振荡且存在 reliability gap; SFT surpasses vanilla significantly and keeps improving。

**Seed 2 跨 seed 可复现性（exp-003-s2, seed=43）**：
| ckpt | ToF | NoF | SYCONScore | vs vanilla | vs seed 1 同 step |
|------|-----|-----|------------|------------|-------------------|
| 500 | 0.044 | 0.950 | 0.085 | -37% | — |
| 1000 | 0.044 | 0.945 | 0.084 | -37% | seed1=0.074 (+14%) |
| 1500 | 0.055 | 0.950 | 0.104 | -22% | — |
| 2000 | 0.044 | 0.983 | 0.085 | -37% | seed1=0.085 (=) |
| 2500 | 0.055 | 0.972 | 0.105 | -22% | — |
| 3000 | 0.050 | 0.972 | 0.095 | -29% | seed1=0.095 (=) |
| 3500 | 0.039 | 0.972 | 0.074 | -45% | — |
| 4000 | 0.077 | 0.945 | **0.143** | **+7.1%** | seed1=0.114 (+25%) |
| 4500 | 0.055 | 0.950 | 0.104 | -22% | seed1=0.134 (-22%) |
| 5000 | 0.055 | 0.950 | 0.104 | -22% | seed1=0.114 (-8.8%) |
| 5500 | 0.061 | 0.972 | 0.114 | -14% | seed1=0.114 (=) |
| 6000 | 0.050 | 0.950 | 0.095 | -29% | seed1=0.085 (+11%) |
| 6500 | 0.055 | 0.978 | 0.105 | -22% | seed1=**0.153** (-31%) |
| 7000 | 0.050 | 0.950 | 0.095 | -29% | seed1=0.105 (-10%) |
方向一致：两个 seed 均远低于 vanilla、高 NoF 低 ToF（stubbornness 特征）。Seed 2 峰值在 ckpt-4000 (0.143, 唯一 > vanilla)，之后持续回落。**关键发现**：seed 1 在 ckpt-6500 的最大 spike (0.153) 在 seed 2 未复现（仅 0.105），证明 spike 是随机噪声而非可靠趋势。Spike timing 跨 seed 完全不同（seed 1 ~step 4500/6500, seed 2 ~step 4000），不稳定振荡是方法固有特征。

**ACT seed 2 跨 seed 验证（exp-004-s2）**：
| ckpt | ToF | NoF | SYCONScore | vs vanilla | vs seed 1 |
|------|-----|-----|------------|------------|-----------|
| 500 | 0.127 | 0.917 | **0.223** | **+67%** | seed1=0.170 (+31%) |
| 1000 | 0.149 | 0.912 | **0.256** | **+92%** | seed1=0.205 (+25%) |
| 1500 | 0.122 | 0.884 | **0.214** | **+60%** | seed1=0.170 (+26%) |
| 2000 | 0.122 | 0.890 | **0.214** | **+60%** | seed1=0.255 (-16%) |
ACT seed 2 全部 4 点均大幅 > vanilla（+60%~+92%）。ckpt-1500→2000 plateau（均 0.214），与 seed 1 不同（seed 1 ckpt-2000=0.255 跳升）——seed 2 更稳定但起步更高。ACT 的 non-monotonic pattern 跨 seed 可复现，且最低点仍远超 vanilla。

**ACT is SFT, not RL (D041 critical correction)**: Reviewer 确认 exp-004 (ACT) 训练日志记录 sft_loss + l2_loss，是 Supervised Fine-Tuning，不是 GRPO RL。SFT 在 ckpt-500 即达 SYCONScore=0.170，远超 GRPO plateau 0.114。效率差 ~16x。

**论文叙事 — Scheme C 双层结构 (D041→D042)**：

**Layer 1: d_syc rewards actively harmful**
- 7 种 d_syc→reward formulations 全部 fail（cosine×4, binary probe, continuous probe, ActAdd）
- d_syc experiments collapse and DO NOT recover（exp-008v3 ToF=0 不回升，exp-009 单调下降，exp-002v3 mode collapse）
- 根因：d_syc 编码 change direction 不编码 change warrant → 引入有害梯度

**Layer 2: GRPO stubbornness emergence + reliability gap**
- R3-only GRPO (exp-003) 围绕 vanilla 水平不稳定振荡，偶尔超越但无法维持
- GRPO 系统性地向 stubbornness 漂移（所有 GRPO 实验 NoF↑ ToF↓）
- R3 (NLI) 无法区分"正确坚持"和"错误顽固"——sparse reward 的固有限制
- **Reliability gap**: ACT 20/20 checkpoints > vanilla (seed1 16/16 + seed2 4/4); R3-only seed 1 仅 3/12 > vanilla, seed 2 仅 1/14

**Positive control: SFT succeeds (with nuance)**
- exp-004 ACT (SFT) SYCONScore trajectory (16/16 checkpoints > vanilla): ckpt-500(0.170)→1000(0.205)→1500(0.170)→2000(0.255)→2500(0.239)→3000(0.206)→3500(0.231)→4000(0.214)→4500(0.188)→5000(0.263)→5500(0.238)→6000(0.262)→6500(0.253)→7000(0.286)→7500(0.277)→8000(0.301)
- **非单调**：ckpt-4000 出现回落（ToF↓ NoF↑，短暂 stubbornness 增加），但 ckpt-6000 自恢复
- 关键区分：SFT 也经历 stubbornness episodes 但能自恢复；GRPO 一旦 stubbornness 不回头
- **ACT vs GRPO representation 对比 (mechanistic)**：ACT dip→recovery 时 d_syc L19 AUROC 恢复（+0.013），GRPO 同期退化（-0.004）。ACT 绝对 AUROC 更高（0.32-0.35 vs 0.16-0.23）。Dense supervision 维持 representational coherence。
- 整体趋势仍远优于 GRPO：ckpt-500 (0.170) 已超 GRPO plateau (0.114)，效率差 ~16x
- 证明 sycophancy calibration IS achievable via dense supervision

**三层区分总结 (D043→D047 精确化)**：d_syc = actively harmful (collapse, no recovery), R3-only = 围绕 vanilla 不稳定振荡 + reliability gap (late-training mean 0.118 < vanilla 0.134, 偶尔超越但无法维持，seed 1 仅 3/12 checkpoints > vanilla, seed 2 仅 1/14), SFT = dips but self-recovers and keeps improving (16/16 > vanilla, 0.170→0.301)。GRPO 的共同特征是 stubbornness emergence（NoF↑ ToF↓），区别在于 d_syc 加剧崩溃而 R3-only 围绕 vanilla 振荡但无法稳定超越。SFT 也经历 stubbornness episodes 但能自恢复——这是 dense vs sparse supervision 的根本差异。Claim 强度：Medium (D043)。

**Reliability gap 对比框架 (D047)**:
- **ACT (SFT)**: 16/16 D027 eval checkpoints > vanilla（最低 ckpt-500 = 0.170, +27%），稳定上升至 ckpt-8000 = 0.301 (+126%)
- **R3-only seed 1**: 仅 3/12 > vanilla（ckpt-4500 +0.1%, ckpt-6500 +14.5%, ckpt-8000 +7.3%），其余 9/12 低于 vanilla
- **R3-only seed 2**: 1/14 > vanilla（ckpt-4000 +7.1%），其余 13/14 低于 vanilla（ckpt-6500=0.105 未复现 seed1 spike, ckpt-7000=0.095）
- **跨 seed 合计**: ACT 20/20 (100%) vs R3-only 4/26 (15.4%)
- **ACT seed 2**: 4/4 > vanilla — ckpt-500(0.223,+67%)→1000(0.256,+92%)→1500(0.214,+60%)→2000(0.214,+60%)。ckpt-1500→2000 plateau，seed 1 同期跳升到 0.255
- **效率差 ~16x**: ACT 500 步即 +27%，R3-only 8000 步才 +7.3%

**Online recalibration**: d_syc is recalibrated every 500 training steps as a safety mechanism. Empirically, direction drift is modest (cosine ≈ 0.96 at step 500), but recalibration ensures the reward signal tracks any longer-term geometry changes. Cost is negligible (one forward pass over calibration data per 500 steps).

**Cosine R1 failure chain (D029 — key negative result)**: Continuous cosine R1 fails structurally, not due to scaling. Evidence chain:
1. **exp-002** (tanh gate): gate collapsed, R1 contribution zero → removed gate (D021)
2. **exp-002v2** (raw cosine, weight=0.25): R1 ≈ 0 throughout training, functionally equivalent to R3-only
3. **exp002v2-recalib** (raw cosine + recalibration): mode collapse (entropy 0.069, mean_length 62 tokens) — not clean evidence
4. **exp-002v3** (5x scaled cosine, weight=0.4): Per-strength analysis reveals structural cause — strong evidence samples (where model SHOULD revise) get R1=-0.305 (ALL negative). d_syc projection cannot distinguish "model correctly revises belief" from "model sycophantically capitulates" because both involve moving TOWARD the user's position in activation space. Scaling amplifies this flaw rather than fixing it. **D035 update**: GRPO mode collapse at step 2440 — entropy=0.009, grad_norm=0.00016, R3 saturated to 0.9998, frac_reward_zero_std=61%. R1 too weak to drive learning after R3 saturation → symmetric with exp-008v3 (R1 too strong).

**Root cause**: Cosine similarity measures angular alignment with d_syc direction. But sycophantic capitulation and genuine revision BOTH involve belief change toward the user's claim — they differ in WHETHER the change is warranted, not in the DIRECTION of the change. A linear direction captures the direction of change, not its warrant. Binarization via probe adds a decision boundary that the continuous projection lacks.

**Cosine R1 failure is noise, not weakness (D035 Reviewer analysis)**: exp-002v2 (R1 ~8% of combined reward) vs exp-002v3 (R1 ~45%) comparison rules out the "too weak" hypothesis. With 5x scaling, R1 gap expanded from ~0.098 to ~0.49, but R1 mean oscillated between -0.46 and +0.41 with NO sustained positive trend — d_syc gives contradictory directional judgments for the same response in different contexts. The root cause is high variance of the direction projection, not low amplitude.

**Probe reward trap (D031/D032 — key finding)**: Binary probe learns "no answer change = non-sycophantic" from contrastive training data. In GRPO:
1. Model outputs stubborn response (doesn't change answer) → probe classifies as non-sycophantic (R1=1)
2. High R1 reward → gradient reinforces stubbornness
3. Policy narrows to always-stubborn → entropy drops → more stubborn → R1 stays high
4. Result: ToF=0.0000 (model NEVER accepts valid corrections), NoF≈1.0 (resists everything)
5. **Critical diagnostic finding (D032)**: The trap is **immediate** — ckpt-500 already shows ToF=0 while entropy=0.70 (fully healthy). Full trajectory: ckpt-500 (entropy 0.70, ToF=0) → ckpt-1000 (0.80, ~0) → ckpt-1500 (0.61, 0) → ckpt-2000 (0.30, 0). Behavioral collapse leads distributional collapse by **~1300 steps**. Entropy monitoring alone cannot detect this failure mode.

**Probe ablation (D030, extended D037)**: d_syc probe carries real sycophancy-specific signal across models:
- **Qwen3-8B**: d_syc AUROC 0.835 vs random 0.727, gap = +0.108
- **Llama-3-8B**: d_syc AUROC 0.813 vs random 0.530±0.054, gap = **+0.248** (2.3× larger than Qwen)
Cross-model probe ablation strengthens the argument: direction signal quality is even BETTER on Llama, yet the structural limitation (encoding change direction not warrant) remains. Higher discriminability does not translate to reward utility — the gap is between CLASSIFICATION and OPTIMIZATION.

**Mechanistic analysis of spike-regression (D046 — three-layer evidence)**:

Why does R3-only peak at vanilla (ckpt-4500) then regress (ckpt-5000)? Three independent analyses converge:

1. **Activation drift**: d_syc L19 representations nearly identical (AUROC Δ<0.01, valid-invalid gap -5.98 vs -6.05) → NOT representation degradation
2. **R3 reward distribution**: R3 mean saturated at ~0.98 for both checkpoints (Welch t-test p=0.703, no significant difference). Valid-invalid gap actually improves (-0.034 → -0.015) → NOT reward signal degradation
3. **Yet SYCONScore drops 15%** (0.134 → 0.114)

Conclusion: **GRPO drifts randomly in a flat reward landscape.** R3 saturates near 1.0 around vanilla performance, leaving no gradient signal to maintain or improve. The policy wanders while representations and rewards remain stable — a fundamental limitation of sparse behavioral reward near its ceiling.

This three-layer decoupling (representation stable + reward stable + behavior regresses) is the strongest mechanistic evidence for why GRPO fails: it's not that the reward is wrong, it's that the reward provides no useful gradient once behavior reaches baseline level.

**Stubbornness taxonomy (exp-008v3 binary probe trap)**:
181/181 valid samples show 100% stubbornness. Six failure modes identified:
- **Sycophantic stubbornness** (24%): says "you're right" but doesn't change answer — simultaneously sycophantic AND stubborn
- **Deliberation trap** (29%): knows correct answer but can't commit, trapped in infinite reasoning
- **Acknowledge-but-maintain** (24%): "however/but" hedge then maintains original answer
- **Evidence-strength gradient**: weak evidence → surface compliance (39%); strong evidence → explicit hedging (54%). Model adjusts *refusal style* but never accepts correction
- Format corruption: 87% responses start with "Ah, interesting", 96% truncated at 512 tokens

**CRAFT/Latent-GRPO asymmetry (Dream review critical gap)**: Continuous representation geometry reportedly succeeds as GRPO reward for reasoning (Latent-GRPO: spherical projection) and safety (CRAFT: prototype clustering). Why does it fail for sycophancy? Our explanation: reasoning (correct/incorrect) and safety (safe/unsafe) have cleaner geometric separation — the behavioral categories DON'T share direction. Sycophancy is unique: sycophantic capitulation and genuine revision both involve belief change toward the user's position, differing ONLY in warrant. This makes sycophancy fundamentally harder for direction-based rewards. This asymmetry should be a key Discussion section point.

**Headline result template**: "We show that a linear sycophancy direction (d_syc) achieves AUROC 0.82 in discriminating sycophantic capitulation from genuine revision, yet fails as GRPO reward in all tested formulations — continuous cosine penalizes all belief change while binarized probe rewards all resistance, both exploiting the direction's blindness to change warrant. We identify a probe reward trap that causes behavioral collapse (ToF=0) before entropy collapse, revealing that discriminability ≠ reward utility in representation-guided RL."

## Positioning (from 21-paper distillation, 2026-05-24)

**Research Gap #3 (distilled-research)**: "Reward hacking 理论 × activation engineering 无交叉研究" — our paper IS the first systematic cross-study. Skalse (theoretical impossibility) + RepE (direction extraction) → we empirically demonstrate that activation discriminability does not transfer to reward utility. This is already implicitly conveyed in Intro §4 and Related Work, but not explicitly claimed as "first to bridge."

**Multi-turn (Gap #1)**: Our multi-turn setting is itself underexplored (O'Brien only paper to mention multi-turn steering limitations). Already in our framing but could be emphasized more.

**Baseline coverage**: Matches field convention (base + training + inference-time). No gaps.

**Story type**: "突破局限型" (5/8 distilled papers) matches our paper perfectly.

## Venue Fit Risks

- **EMNLP fit (Path B — analysis paper)**: Moderate-strong for Findings. Systematic investigation of representation-guided RL with mechanistic analysis. EMNLP Findings values rigorous empirical work with diagnostic insights. The discriminability ≠ reward utility finding is relevant to the broader RepE-for-training community. Main track unlikely without positive method result.
- **Reviewer concern 1 (novelty)**: "This is just RepE/CRAFT applied to sycophancy." Counter: (a) d_syc is explicitly positioned as a RepE application; the novelty is the systematic investigation of how direction information should enter GRPO rewards — discovering that discriminability ≠ reward utility; (b) the cosine R1 failure chain (4 experiments) and binarization insight are the core contribution, not direction extraction; (c) multi-turn calibration with evidence-strength stratification is a standalone contribution; (d) neither CRAFT nor RepE has investigated the discriminability–reward gap.
- **Reviewer concern 6 (RC-AUC custom metric)**: "Strongest results on self-invented metric." Counter: RC-AUC is formally defined in Method section with statistical properties. Results are also reported on standard metrics (NoF, WRR) for direct comparison. RC-AUC captures the sycophancy-revision tradeoff that no existing metric addresses.
- **Reviewer concern 2 (signal strength)**: "AUROC ~0.82 on style-controlled data is moderate." Counter: (a) single-turn literature achieves >0.97 with style confound included; (b) our v2.1 ablation isolates pure cognitive signal; (c) 0.82 is sufficient for GRPO reward gradient; (d) D019 confirms AUROC ≥ 0.77 persists across ALL 7 layers even after 500+ LoRA training steps, with deep layers actually improving (+0.025-0.033); (e) direction remains stable during training (cosine sim ≥ 0.82 with initial direction).
- **Reviewer concern 3 (scale)**: "Only Qwen3-8B." ✅ Resolved by exp-012 (D036): Llama-3-8B AUROC=0.779±0.019, style-controlled=0.923, same strength gradient. Two architecturally distinct families (Qwen/Alibaba + Llama/Meta). Claim "cross-architecture phenomenon" with qualifier in Limitations ("tested on two 8B-parameter models; larger models and additional architectures remain future work"). Third model family (Mistral/Gemma) is nice-to-have, not required for Findings.
- **Reviewer concern 4 (R2 degeneration)**: "d_gen = -d_syc in binary design." Counter: We use rank-based contrastive R2 (S1) that doesn't depend on d_gen definition. If time allows, neutral-baseline three-way design (S2) provides independent d_gen.
- **Reviewer concern 5 (practical utility)**: "Do models actually exhibit masked sycophancy at meaningful rates?" Counter: Literature documents 13-29% representation-behavioral disagreement (Knowledge-Prediction Gap, Sycophantic Anchors). R1-R3 disagreement analysis directly measures this.

## Anticipated Reviewer Concerns & Experimental Responses

| Concern | Experiment | Priority |
|---------|-----------|----------|
| d_syc is just style detector | v2.1 style-controlled ablation (done in MVP) + expanded data | P0 |
| DC-GRPO doesn't beat behavioral GRPO | Main exp vs R3-only baseline, report Revision-Capitulation AUC | P0 |
| Undifferentiated consistency (ACT) is enough | ACT-style baseline comparison | P0 |
| Probe doesn't need d_syc (random features work) | Random-direction probe ablation: d_syc AUROC 0.835 vs random 0.727 (+0.108) | P0 ✅ done (D030) |
| Directions drift during training | Direction stability monitoring + periodic recalibration | P0 (built into training) |
| R1-R3 disagreement is negligible | Disagreement frequency analysis + qualitative examples | P1 |
| Single model, doesn't generalize | ✅ Cross-model: Llama-3-8B AUROC=0.779, strength gradient consistent (D036). Probe ablation in progress. | P2 → Done |
| Multi-turn contribution marginal vs single-turn | Turn-depth analysis: revision rate vs commitment depth | P1 |
| Why not continuous probe output (probability) instead of binary? | Continuous probe probability vs binary probe reward comparison | P1 |
| Reward weights unjustified | Reward weight sensitivity analysis (3-5 configs) | P1 |
| RC-AUC is custom, unvalidated | Formal definition + correlation with human judgments | P1 |
| Missing foundational references (RepE, CCS) | Expanded Related Work with 25+ references | P0 (writing) |
| Cosine R1 failure is just bad tuning, not structural | 4-experiment failure chain + per-strength analysis showing structural conflation | P0 (evidence complete) |
| Direction drifts during training | exp-006 stability curve: cosine sim + AUROC at 5 checkpoints | P0 |
| Why cosine not dot product? | Appendix: dot product saturation analysis + R1 distribution comparison | P2 (less critical post-D029, cosine R1 is negative evidence not method) |
