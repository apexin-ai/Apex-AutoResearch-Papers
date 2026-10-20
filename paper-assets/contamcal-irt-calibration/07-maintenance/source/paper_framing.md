# Paper Framing — contamcal-irt-calibration

## Target Venue
- **Primary: EMNLP 2026 ARR May 25** (D006: reinstated per user directive, 12 days)
- Fallback: AAAI 2027 (Jul-Aug 2026) / ICLR 2027 (Sep 2026)
- Track: Machine Learning for NLP / Resources and Evaluation
- Aligns with EMNLP 2026 special theme "New Missions for NLP Research" (explicitly invites contamination/data governance work)

## Core Insight (D149: dose-response profiling + baseline-dependent direction, building on D039/D108/D115)

Benchmark contamination does not have a single effect — controlled SFT injection across 5 independent model families reveals qualitatively different dose-response profiles depending on model baseline capability. Through injection (LoRA r=16, 5 dosage levels d000–d100) on Qwen2.5-7B, Qwen2.5-14B, Phi-4 14.7B, Gemma-2 9B, OLMo-2 7B, we observe:

**4 dose-response patterns (D149→D183→D184, MMLU, cross-seed confirmed)**:
| Pattern | Family | Baseline | s42 Δ(d100) | s123 Δ(d100) | Cross-seed |
|---------|--------|----------|-------------|--------------|------------|
| Immune | Phi-4 14.7B | 76.44% | -0.17pp | +1.83pp | ✅ n=3: s0 +0.52pp, mean +0.73pp, BCa CI [-0.17, +1.39] 含零 |
| Collapse | Qwen-14B | 69.44% | -9.37pp (U-shape) | -12.74pp (monotonic) | ✅ 方向一致，形状不同 |
| V-recovery | Qwen-7B | 66.11% | -1.78pp (V-dip) | ~0pp (V-full) | ✅ 形状+方向一致 |
| Benefit | Gemma-2 9B | 61.86% | +3.76pp | +1.49pp | ✅ 方向一致 |
| Benefit† | OLMo-2 7B | 53.79% | +3.21pp | -0.55pp | ⚠️ seed-sensitive |

⚠️ D184: "U-collapse" 重命名为 "Collapse"——s42 U-shape (d050→d100 回升 +0.6pp) 在 s123 不复现 (d050→d100 继续下沉 -5.1pp)。跨种子稳定的是方向(harm)不是形状(U)。V-recovery 保留 shape-based name 因为它是唯一跨种子形状稳定的 pattern。论文报告 Qwen-14B 跨种子区间 [−12.74, −9.0pp]。

⚠️ **Bootstrap n=2 findings (D186)**: 算法形状分类 2/5 家族一致（Collapse ✅, V-recovery ✅），方向分类 4/5 一致（+Benefit ✅, +Immune ✅）。n=2 t-distribution CI 极宽（df=1, 所有 CI 跨零），统计效力有限——s0 升级到 n=3 BCa 后会显著收窄。
- **Phi-4**: 算法 "Incomplete†"（s42 Immune vs s123 Benefit-sat），但方向层面两个种子都 <2pp → Immune as practical label，等 s0
- **Gemma-2**: 算法 "V-recovery†"（s123 d025 -2.82pp dip 触发 V-dip 检测），但 d100 仍为正 (+1.49pp) → 方向稳定 Benefit，形状变异
- **OLMo-2**: 算法 "Benefit-sat†"，n=3 CI [-0.55, +2.60]，方向 2/3 正向但 s123 负
论文策略：报方向 taxonomy (Immune/Collapse/V-recovery/Benefit) + n=2 bootstrap CI table 作为 conservative bound + 明确写 "shape classification requires ≥3 seeds; direction is more reproducible"。n=3 数据是论文提交前的关键升级。

**Vulnerability gradient (D181, replaces sharp threshold)**: 效应方向不由单一 sharp threshold 决定，而是呈 gradient 分布。Vulnerability（对 contamination 最敏感，表现为 harm）集中在 ~65-70% baseline band（Qwen-7B 66.1%, Qwen-14B 69.4%）。极端 baseline 表现为有限敏感性——低端（OLMo-2 53.8%）benefit 但 magnitude seed-dependent，高端（Phi-4 76.4%）immune。**不可说 "sharp cutoff" 或 "universal threshold"，用 "vulnerability gradient" 和 "observed in our 5-family sample"。**

**Within-family scale finding (Qwen only)**: Within the Qwen family, the 14B model is 3× more fragile than the 7B (-10pp vs -3pp). However, Phi-4 (14.7B) is immune — so this is NOT a general "bigger = more fragile" claim. 正确 framing: "baseline ability, not parameter count alone, determines contamination vulnerability."

**ARC cross-benchmark results (D190, s42 + s123)**:
- s42 ARC: OLMo-2 +3.92pp, Qwen-7B -3.84pp, Qwen-14B -3.41pp, Phi-4 ±0.6pp. Gemma-2 ARC excluded (16pp oscillation artifact).
- s123 ARC: Qwen-14B -3.15pp, Phi-4 +0.86pp, Qwen-7B -2.39pp, OLMo-2 +2.90pp.
- **Cross-benchmark structure (D190→D191 corrected)**: 跨 benchmark 对比必须用 MMLU 多种子均值而非单 seed。修正后 3/4 方向一致：Qwen-14B 双降 ✅, Phi-4 双 Immune ✅, OLMo-2 双正 ✅ (MMLU mean +1.35pp, ARC +2.90pp)。Qwen-7B V-recovery 形状两个 benchmark 都有但恢复幅度 benchmark-specific (MMLU ≈0pp full recovery, ARC -2.39pp partial)。⚠️ D190 原始报告的 OLMo-2 "方向反转"是使用单 seed s123 (-0.55pp) 的伪影——修正为用 bootstrap 均值后双正。
- **论文 framing**: "Cross-benchmark direction is consistent for 3/4 families; only V-recovery shows benchmark-specific modulation in recovery completeness." 不说 "universal consistency"，但也不需要 D190 的"两层结构"——3/4 一致已足够强。
- **方法论教训**: 跨 benchmark 对比使用单 seed 会产生 high-variance 家族的虚假方向反转。论文表格使用 bootstrap 均值。

The primary contribution is the empirical characterization framework — showing that "contamination = inflation" is a gross oversimplification and that model-specific dose-response profiling is necessary for reliable benchmark interpretation. IRT with per-benchmark γ_k provides the statistical machinery for this characterization. Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).

## Core Claims (4 条 — D149 reorder: characterization as primary, D152 Reviewer calibrated)

1. **Characterization Claim (PRIMARY — D149 dose-response profiling)**: Contamination does not uniformly inflate scores — it produces qualitatively different dose-response profiles across model families, with effect direction (benefit vs harm) correlating with baseline ability. Key evidence:
   - **5 families × 5 dosages × 2 benchmarks** (MMLU + ARC) with controlled SFT injection at identical LoRA config
   - **Baseline-dependent direction**: In our 5-family sample, models below ~62-66% MMLU benefited; above were harmed or immune
   - **Effect magnitude heterogeneity**: From -10pp (Qwen-14B) to +3.8pp (Gemma-2) — 14pp range across families at same dosage
   - **Within-family scale effect (Qwen)**: 14B 3× more fragile than 7B, suggesting baseline ability (not just scale) drives vulnerability
   - **Cross-benchmark consistency (D190→D191→D192)**: 5/5 families have ARC data. Using multi-seed means: **4/5 direction-consistent** (Qwen-14B Collapse ✅, Phi-4 Immune ✅, Gemma-2 Benefit ✅, OLMo-2 Benefit ✅). Qwen-7B V-recovery is MMLU-specific — ARC shows persistent -2.65pp (mild Collapse), V-dip shape present but no recovery. Gemma-2 s42 ARC oscillation artifact is seed-specific (s123 clean +2.73pp). ⚠️ 跨 benchmark 表必须用 bootstrap 均值非单 seed。
   ⚠️ **Claim strength gating (D181 updated)**: Cross-seed data (Reviewer 修正): Qwen-7B V-recovery 2/2 seeds 一致 ✅; Gemma-2 Benefit 方向一致 (s42 +3.76pp, s123 +1.49pp) 但形状变异; OLMo-2 方向不稳定 (s42 +3.21pp, s123 -0.55pp, s0 +1.61pp). 4-pattern taxonomy (D184): Immune / Collapse / V-recovery / Benefit, 等 Qwen-14B s123 确认。论文策略：(a) 报 bootstrap CI 而非单点 Δ, (b) 加 seed-sensitivity discussion section, (c) 弱化 "5 distinct patterns" 语言, (d) OLMo-2 caveat about cross-seed instability。Seed-sensitivity 本身作为 methodological contribution: warns community that single-seed contamination studies are unreliable。
   **Domain-level heterogeneity (≤3B Qwen IRT analysis, D108/D115, mechanistic complement)**: Within MMLU, stratification by cognitive domain reveals Simpson's paradox: aggregate γ≈0 masks STEM gradient (Math γ=+0.97, Science γ=+0.84, CS_Eng γ≈0). Non-STEM domains show model misfit (PPP≈1.0). 注意：domain-level 分析在 ≤3B Qwen 上进行，与 7B-14.7B 5-family profiling 是不同 scale。7B-14.7B domain-level 分析列为 future work。
   **Paper claim scope**: 5 profiles based on 5 families × 5 dosages (seed=42; triple-seed in progress). Domain-level from ≤3B Qwen. Bounded by: SFT-route only, ≤14.7B, AUGMENT mode, 2 MCQ benchmarks.

2. **Signal Failure Claim (CO-PRIMARY, headline finding per D039 dream 三档一致)**: Min-K++ exhibits directional reversal at small model scales (Cohen's d = -1.2 to -2.7 at 0.5B d100) — actively misleading, not merely ineffective. S1 embedding similarity is the only reliable signal (AUC>0.95). Multi-signal RRF degrades to S1-only in practice — paper is transparent about this (D039: all 3 dream tiers require honesty here). Training-free RRF remains the principled aggregation design (meta-circularity argument). Must distinguish item-level detection AUC from model-level Cohen's d.
   **C2 contingency**: "Scale-dependent" unverified beyond 0.5B. If 1.5B/3B S2/S4 remain ineffective → downgrade to "method-specific signal effectiveness." Min-K++ reversal remains novel regardless.

3. **Identifiability Claim**: Fisher Information analysis + simulation sweep (20 conditions, 200 runs). Recovery succeeds down to AUC=0.55 (lowest tested) at N≥50; the lower bound remains open. LLM evaluation inherently operates below N≥50 (typically N=8-30), creating a structural domain-method mismatch — this is the real "impossibility," not merely "IRT needs more data." CI width ∝ N^{-0.48} (simulation). Coverage collapse at N<30 confirmed empirically (D036). D039 dream worst-tier caution: frame as domain mismatch insight, not as surprising impossibility.

4. **Conditional Calibration Claim (DEMOTED from old Claim 1 per D039)**: IRT ability estimation provides calibration value (GSM8K: calMAE=0.006 vs raw=0.169, ΔMAE=0.163); the γ parameter provides diagnostic value by revealing domain-differential contamination effects. These are distinct contributions: calibration improvement comes from the IRT framework itself (ability estimation decontaminates via the θ pathway), while γ characterizes where and how contamination manifests. When IRT model complexity matches benchmark structure (2PL for open-ended, 4PL for MCQ) AND signal quality sufficient (validated down to AUC=0.55 at J≥50), calibration produces usable point estimates. Coverage remains below nominal (20-69% at 95%) — present calibrated CIs as directional indicators, not precise credible intervals. Calibration gating criterion: PPP ∈ [0.1, 0.9] AND calibrated MAE < raw MAE. Note: vanilla 2PL ≈ 2PL+γ in MAE across all three benchmarks — γ does not improve calibration accuracy but provides the diagnostic decomposition that is Claim 1's core contribution.

## Contributions (Hierarchical — D149/D152 calibrated)

### Core
1. **Dose-response profiling across 5 model families**: Contamination effects range from -10pp to +3.8pp MMLU depending on model family, with effect direction correlating with baseline ability. No prior work has systematically profiled contamination dose-response across multiple independent families. *(Upgrades to "taxonomy of N discrete patterns" if triple-seed confirms profile stability; conservative framing: 3 profiles — benefit/harm/immune.)*
2. **Domain-dependent contamination characterization** via IRT γ_k (≤3B Qwen): Simpson's paradox within MMLU (aggregate γ≈0 masks STEM gradient: Math +0.97 > Science +0.84 >> CS_Eng ≈0). Mechanistic complement to family-level profiling — contamination heterogeneity operates at multiple granularities.
3. **Signal failure characterization**: Min-K++ directional reversal (Cohen's d = -1.2 to -2.7) — paper's most citation-worthy cautionary finding. Honest reporting that RRF = S1-only in practice.
4. **Fisher Information identifiability analysis**: structural vs practical thresholds with domain-method mismatch insight.

### Supporting
5. ContamCal framework: two-stage pipeline (S1 provenance → contamination-augmented IRT with per-benchmark γ_k). Conditional calibration with gating criterion. ME model as ablation
6. Dual-track validation + 7 baselines + 6 metrics (incl. SBC). Controlled SFT injection across 5 families

## Story Spine
- **Problem**: Benchmark scores are increasingly unreliable due to training data contamination. Rephrased test items inflate MMLU accuracy by 8-15 points while evading n-gram decontamination. RL post-training may further complicate detection (under investigation, exp-009). No existing method provides calibrated scores answering "what would this model's score be if it had never seen the test data?"
- **Existing approaches & gaps**: Detection methods (Min-K%++, ConStat, Self-Critique, KDS) flag contamination but don't calibrate scores. IRT methods (PSN-IRT, Growing Pains, ATLAS, Lalor et al. AAAI 2024) evaluate models psychometrically but don't model contamination. DCR provides adjusted accuracy but lacks uncertainty bounds and RL handling. HiBayES provides Bayesian uncertainty but ignores contamination. Emperor's New Clothes (ICML 2025) demonstrates that all 20 mitigation strategies fail — motivating post-hoc calibration. Dynamic benchmarks (LiveBench) offer an alternative but require continuous curation.
- **Our framing (D149 pivot)**: ContamCal is a diagnostic framework that uses controlled SFT injection and IRT analysis to systematically profile how contamination affects benchmark scores. Through injection across 5 independent model families (7B–14.7B), we discover that contamination produces not one but five distinct dose-response patterns, governed by a baseline ability threshold. The framework establishes both what contamination does (5-pattern taxonomy + domain-level IRT heterogeneity) and under what conditions calibration is feasible (Fisher Information identifiability boundaries). Grounded in educational measurement's item compromise IRT (Eckerly 2017, Sinharay 2017) and explanatory IRT (De Boeck & Wilson 2004).
- **Headline result template (D149, D152 calibrated)**: "Benchmark contamination effects span a 14pp range across model families — from +3.8pp benefit (Gemma-2 9B) to -10pp collapse (Qwen-14B) — with effect direction correlating with baseline ability: lower-baseline models benefit while higher-baseline models are harmed or immune. Within the Qwen family, the 14B model is 3× more fragile than the 7B, suggesting baseline ability rather than parameter count drives vulnerability. Detection signal Min-K++ actively reverses direction at small scales (Cohen's d = -1.2 to -2.7). Fisher Information analysis establishes that reliable parameter recovery requires N≥50 models — conditions rarely met in current LLM evaluation."

## Venue Fit Risks
- **EMNLP (primary)**: Best venue fit — special theme explicitly invites contamination/data governance. Reviewers deeply familiar with NLP contamination literature (advantage: no need to motivate the problem heavily). Risk: reviewers may be less familiar with IRT/psychometric methods (mitigation: add intuitive explanations, visual pipeline overview, and connection to familiar NLP concepts like calibration/confidence estimation). ~~Risk: may expect broader model coverage beyond Qwen2.5~~ — **Resolved by D141**: 4 independent families (Qwen2.5, Phi-4, OLMo-2, Gemma-2) with controlled SFT at ≤14.7B scale.
- **AAAI/ICLR (fallback)**: Strong fit for Bayesian/probabilistic methods. Reviewers may need more contamination context but appreciate methodological rigor.
- **Novelty positioning**: Core method is cross-disciplinary synthesis (detection signals + explanatory IRT + measurement error). NOT positioned as "new algorithm" — positioned as (a) signal effectiveness characterization as empirically novel finding, (b) identifiability bounds with theoretical grounding, (c) first framework bridging detection → calibration with proper UQ. RRF is a principled design choice (meta-circularity argument), not claimed as methodological contribution.
- **RL limitation**: RL models get wide CIs. This is honest — frame as "calibration is only as good as its inputs." Expected regret quantification uses held-out clean benchmark as ground truth (NOT calibrated scores, to avoid circularity).

## Anticipated Reviewer Concerns & Defenses

| # | Concern | Defense | Experiment |
|---|---------|---------|------------|
| 1 | θ and γ identifiable? | Fisher Information analysis + 20-condition simulation sweep (200 runs) + MVP validation | exp-004 |
| 2 | Why not learned aggregation? | Meta-circularity: learned aggregator's training data may itself be contaminated; RRF is design choice, not contribution | exp-003 |
| 3 | SFT injection ≠ real contamination | Dual-track: controlled SFT (internal) + ecological RL (external) + near-zero γ check (specificity). SFT is "best-available proxy", acknowledged as limitation | exp-006, exp-009 |
| 4 | Scale limited to 3B | ≤14.7B controlled SFT across 4 independent families (Qwen2.5 0.5B-14B, Phi-4 14.7B, OLMo-2 7B, Gemma-2 9B; D141). 29 runs total. | D141 scope expansion |
| 5 | Why 4PL not 2PL? | MVP: 2PL γ=0.16 vs 4PL γ=0.34 at N=100; c/d necessary for realistic item modeling | exp-006 |
| 6 | Too few models (N≈15)? | D025 multi-seed strategy: 3 scales × 4+ dosages × 2-3 seeds = 24-36 models pooled. Target N≥30 minimum (N≥50 ideal). Simulation sweep (exp-004) establishes identifiability at actual N. Growing Pains pre-estimation as backup at very low N | exp-004, exp-001 |
| 7 | Noisy exposure scores | Measurement error model (exposure as noisy observation of latent τ) propagates uncertainty into posteriors automatically | exp-005 |
| 8 | No baselines | 7 baselines including DCR (EMNLP 2025) + bootstrap CIs on all comparisons | exp-006 |
| 9 | Single global γ misspecified? | Per-benchmark γ_k is primary (natural in per-benchmark fitting); joint model with shared global γ is ablation. Report both to show contamination effect heterogeneity across benchmarks | exp-006 |
| 10 | Local independence violated? | Discussed explicitly; single model responds to all items → item responses correlated through shared parameters. Empirically test via posterior predictive checks on item-level residual correlations. This is a known IRT limitation when N_examinees is small. | exp-006 |
| 11 | Single model family? | Addressed in main experiments: 4 independent families (Qwen2.5, Phi-4, OLMo-2, Gemma-2) with controlled SFT injection at identical LoRA config (D141). Qwen2.5 provides within-family scaling (0.5B-14B); 3 cross-family models validate generalizability. | D141 scope expansion |
| 12 | RL regret circular? | Ground truth for regret = held-out clean benchmark scores, NOT calibrated scores. Explicitly stated | exp-009 |
| 13 | S2/S4 fail at 0.5B — RRF is just S1? | Scale-dependent: honestly report single-signal regime at 0.5B. Verify S2/S4 at 1.5B/3B. RRF value = principled aggregation when signals ARE available + graceful degradation when not. | exp-008, exp-002 |
| 14 | d100 AUC=0.5 as signal failure? | Labeling artifact: d100 contaminates ALL items → labels lose discriminative power. Must NOT be interpreted as signal degradation. Present only d005/d025 for signal evaluation. | exp-008 |
| 15 | Novelty ceiling — standard IRT synthesis? (D025, all 3 Dream tiers) | Positioned as cross-disciplinary synthesis, NOT new algorithm. Emergent value: (a) per-benchmark γ_k heterogeneity as benchmark property, (b) Min-K++ reversal as cautionary finding, (c) Fisher Info identifiability boundaries. If 4PL vs 2PL gap small → acknowledge honestly but argue c/d params needed for realistic MC modeling. Report oracle-γ ablation to decompose MAE. | exp-006 |
| 16 | Per-benchmark γ_k via separate fits, not hierarchical? (D025, [M][W]) | Per-benchmark separate fits = primary (natural, avoids cross-benchmark correlation). Hierarchical γ_k ~ Normal(μ_γ, σ_γ) as ablation to formally test heterogeneity and share info across benchmarks. Both reported. | exp-006 |
| 17 | Coverage gap — 85% vs 95% nominal? (D025, all 3 tiers) | SBC diagnostic to identify source. Possible causes: local independence violation, insufficient N, model misspecification. Report SBC alongside posterior predictive checks. If gap is from local independence → discuss as known IRT limitation with references. | exp-004, exp-006 |
| 18 | Why not just S1 alone? (D025, [M][W]) | S1-only is a baseline (#2 single-signal 2PL+γ). If RRF ≤ S1-only → present as "S1+IRT calibration with extensible multi-signal architecture for future signals." Meta-circularity argument for training-free aggregation still holds. | exp-003 |
| 19 | Coverage collapse 20-33% even with oracle? (D036) | Far worse than #17 anticipated. PPP extremes (ARC=1.0, GSM8K=0.0) = systematic misspecification. Path: (a) increase N via multi-seed pooling, (b) check exp-004 sweep coverage at matching N, (c) if additive γ insufficient → item-level heterogeneity or hierarchical structure. Fallback: lead with MAE+ranking, present coverage honestly. | exp-006, exp-004 |
| 20 | γ doesn't improve calibration MAE over vanilla 2PL | γ's role is diagnostic (domain-differential characterization), not calibration accuracy improvement. IRT ability estimation itself provides calibration value (GSM8K ΔMAE=0.163). Vanilla 2PL ≈ 2PL+γ confirms γ is orthogonal to calibration performance — it reveals WHERE contamination acts, not HOW MUCH to adjust. | exp-006 |
| 21 | Linear regression nearly as good as IRT (D039, all 3 tiers) | B4 MAE=0.040 vs ContamCal MAE=0.035 on ARC. IRT's value is NOT better MAE — it's interpretable per-item parameters, benchmark-dependent γ_k characterization, and theoretical grounding. Bootstrap CI on MAE gap to show significance (or acknowledge non-significance). | exp-006 |
| 22 | SFT capacity artifact ≠ contamination (D039, all 3 tiers) | 0.5B ARC forgetting (-17pp) may be capacity displacement, not contamination-specific. Need: (a) SFT-on-random-data control at 0.5B to isolate capacity vs contamination, (b) focus on 1.5B/3B where capacity effects are minimal (<2pp). Acknowledge 0.5B forgetting as combined SFT+contamination effect. | exp-001 |
| 23 | N=8/16 contradicts paper's own N≥50 recommendation (D039, all 3 tiers) | Internal contradiction. Path: (a) add N=8 condition to simulation sweep for calibrated expectations, (b) increase N via multi-seed (target N≥30), (c) if N<30 → explicitly position as preliminary with caveats. SBC diagnostic at actual N to decompose coverage gap. | exp-004, exp-006 |
| 24 | GSM8K +10pp is AUGMENT training volume confound, not contamination transfer (D167→D177) | Four-family evidence: (1) Front-loaded saturation in Qwen-7B: d005 (+6.37pp/1.7% steps) vs d100 (+10.13pp/33% steps) — concave, not linear. (2) Phi-4 zero transfer (-0.46pp) from identical AUGMENT setup — immune models unaffected. (3) OLMo-2 +2.09pp (n.s.) — no significant transfer despite same setup. (4) Qwen-14B reversal direction consistent cross-seed (+5.7 to +20.5pp) though magnitude varies. Pattern: only Qwen family shows strong reversal, suggesting latent math capability specific to Qwen training, not universal volume effect. | D177, gsm8k_qwen7b_s42_cqa1, gsm8k_phi4_s123_westd, gsm8k_olmo2_s42_westd, gsm8k_qwen14b_s123_westd |

## Evaluation Protocol (6 Metrics — D025 added SBC)
1. **Calibration error**: MAE between calibrated score and ground-truth clean accuracy, with bootstrap 95% CIs
2. **Interval coverage**: Fraction of true values within 50%/80%/95% credible intervals
3. **Interval sharpness**: Average CI width (tighter is better at fixed coverage)
4. **Ranking preservation**: Kendall's τ between calibrated and ground-truth model rankings
5. **Dose-response monotonicity**: γ effect increases monotonically with contamination dosage
6. **SBC diagnostic** (D025): Simulation-Based Calibration (Talts et al. 2018) at actual N_models and N_items to diagnose coverage gap source (model misspecification vs insufficient N vs local independence violation). CPU-only, parallelize with GPU experiments

## Benchmarks (2 main + 2 contrasts)
1. **MMLU** — knowledge-intensive multiple-choice (14K items, subsampled 1000 for NUTS) — PRIMARY
2. **ARC-Challenge** — science reasoning multiple-choice (~1.2K items) — PRIMARY. ⚠️ D036: gamma consistently negative (forgetting, not inflation). 3 independent evidence chains: s42 raw (-17.5pp), s123 raw (-10.2pp), oracle IRT (γ=-2.83). Scale-dependent: 3B d100 ARC=84% (mild forgetting) vs 0.5B d100 ARC=29-37% (catastrophic). Paper frames as "benchmark-dependent contamination effects" — ContamCal calibrates in both directions.
3. **GSM8K** — mathematical reasoning free-form (~1.3K items) — CROSS-BENCHMARK TRANSFER PROBE (D166→D177: Complete 4-family picture. Three transfer patterns:
   - **Null transfer** — Phi-4: Δ=-0.46pp, immune on both MMLU and GSM8K ✅
   - **Consistent positive** — OLMo-2: mean +2.09pp (n.s.), same direction as MMLU ✅ cross-seed
   - **Directional reversal** — Qwen-7B: mean +10.13pp (s42 +11.07, s123 +9.18, range 1.89pp) ✅ headline; Qwen-14B: +5.69 to +20.47pp range, d100 stable cross-seed (81.3% vs 82.3%) but d000 baseline highly seed-sensitive (s42=60.80% outlier vs s123=76.65%), report as supporting with variance caveat (D177)
   - Gemma-2: ❌ excluded (D175: catastrophic forgetting, d000=11.22%, d100=3.94%)
   Paper frames: "cross-benchmark transfer is family-dependent, with three distinct patterns: null, consistent, and directional reversal — further evidence that contamination effects are model-specific, not universal." Qwen-7B +10.13pp as headline reversal.)
4. **HumanEval** (appendix only) — code generation (N=164). Demoted D009: paraphrase QC 16%.

## Baselines (7)
0. **Raw (no adjustment)** — report original benchmark scores as anchor
1. **Remove-and-rescore** — drop flagged items, rescore on remaining
2. **Single-signal 2PL+γ** — best single detection signal + simpler IRT
3. **Vanilla 4PL** — standard IRT without contamination covariate (γ=0)
4. **Linear exposure regression + bootstrap CI** — simplest post-hoc adjustment (tests if IRT complexity is necessary)
5. **Emperor's mitigation strategies** — rephrasing + option shuffling (2 representative strategies from ICML 2025)
6. **DCR fuzzy inference (EMNLP 2025)** — the only existing method producing adjusted accuracy; direct predecessor, must compare

## Local Independence Discussion
Standard IRT assumes independent examinees. In LLM evaluation, a single model produces all item responses — responses are correlated through shared model parameters. This fundamentally alters local independence. Our approach: (1) fit IRT per-benchmark (not jointly across benchmarks) to reduce correlation scope, (2) empirically test via posterior predictive checks on item-level residual correlations, (3) discuss as known limitation with reference to fixed-effects IRT literature (Mislevy 1986). The coverage gap (if observed) may partly reflect this violation — measurement error model for exposure partially compensates by widening CIs.

## Required Figures (D149 updated)
1. **5-pattern dose-response curves** (MMLU + ARC) — paper's headline figure, already drafted on westd
2. **Baseline vs max effect scatter** — shows ~64% threshold, already drafted on westd
3. Pipeline overview diagram (2-stage: RRF → 4PL+γ IRT)
4. Signal × scale × dosage AUC heatmap (exp-008)
5. Identifiability phase diagram (AUC × N_models → γ recoverability, exp-004)
6. Calibrated-vs-true accuracy scatter with CIs (exp-006)
7. *(Optional)* Per-family IRT γ comparison (bar chart with CIs, shows cross-family heterogeneity)

## Citation Requirements (35+ minimum, expanded per Dream D2)
Must include: Eckerly 2017, Sinharay 2017, De Boeck & Wilson 2004, Adams et al. 1997, San Martín et al. 2009, Maris & Bechger 2009, Cormack et al. 2009 (RRF), Mislevy 1986, Lalor et al. AAAI 2024, LiveBench, TinyBenchmarks (Polo et al. 2024), KDS, CDD, contamination surveys, SBC (Talts et al. 2018), HiBayES, plus all signals/methods cited in IDEA_BRIEF.
Dream D2 additions (all 3 tiers flagged):
- DIF literature: Holland & Wainer 1993, Thissen et al. 1993, Zumbo 1999 (γ_k is essentially DIF between exposure groups)
- ML calibration: Guo et al. 2017, Platt 1999 (disambiguate "calibration" — ours is decontamination, not probability calibration)
- Conformal prediction: Angelopoulos & Bates 2023 (alternative UQ with distribution-free coverage guarantees; discuss why Bayesian IRT preferred)
- Data attribution: Pruthi et al. 2020 (TracIn), Park et al. 2023 (TRAK) — potential additional signals, mention in Future Work
- Multidimensional IRT: Reckase 2009 (acknowledge unidimensional θ for MMLU as simplification in Limitations)
D025 additions (all 3 Dream tiers flagged):
- MIA foundations: Shokri et al. 2017 (membership inference attacks), Carlini et al. 2022 (extracting training data) — contextualize Min-K++ reversal in MIA literature
- Alternative evaluation: HELM (Liang et al. 2023), Chatbot Arena (Zheng et al. 2023) — discuss in Related Work as contamination-bypassing alternatives
- Deeper DCR engagement: Oren et al. 2024 structural comparison
- Burnell et al. 2023: multidimensional IRT for LLMs (relevant to unidimensional θ limitation)

## Discussion Notes

### D045: 0.5B Position Bias and MC Benchmark Exclusion (2026-05-15)
- **Finding**: Qwen2.5-0.5B exhibits severe position bias in logprob-based MC evaluation. MMLU prediction distribution: d000 A=46% → d100 A=98%. SFT contamination amplifies pre-existing position prior rather than encoding knowledge.
- **Decision**: Exclude 0.5B MMLU/ARC data from IRT pooling. Retain 0.5B GSM8K/HumanEval (free-form, unaffected). 1.5B/3B all benchmarks normal.
- **Paper treatment**: Report in Discussion as "capacity threshold for reliable MC evaluation." The 0.5B dosage-accuracy decline (40→23% MMLU) is position bias amplification, not knowledge degradation. This reinforces Concern #22 (SFT capacity artifact) and motivates the 1.5B+ focus in main results.
- **Broader implication**: Logprob-based MC evaluation at small scales may be unreliable across model families — note as limitation and suggest token-level or generation-based alternatives for sub-1B models.

## Scope Expansion: ≤14.7B + 4 Families (D141, 2026-05-18)

### Model Matrix
| Family | Model | Params | Released | Runs | Role |
|--------|-------|--------|----------|------|------|
| Qwen (primary) | Qwen2.5-0.5B/1.5B/3B | 0.5-3B | 2024-09 | existing | Within-family baseline (≤3B) |
| Qwen (primary) | Qwen2.5-7B | 7B | 2024-09 | 10 (5d×2s) | Within-family scale extension |
| Qwen (primary) | Qwen2.5-14B | 14B | 2024-09 | 5 (5d×1s) | Within-family scale frontier |
| Microsoft | Phi-4 | 14.7B | 2024-12 | 5 (5d×1s) | Cross-family, strongest 14B |
| Allen AI | OLMo-2-7B | 7B | 2024-11 | 5 (5d×1s) | Cross-family, fully open |
| Google | Gemma-2-9B | 9B | 2024-06 | 5 (5d×1s) | Cross-family, Google family |

All: bf16 LoRA r=16 α=32 lr=5e-5 (D140: matching ≤3B). SFT AUGMENT mode.

### D149 Narrative: 5-Pattern Taxonomy (supersedes Variant A/B framework)

**[SUPERSEDED]** Variant A (null) / Variant B (scale-dependent transition) 框架已被 D149 实际数据推翻。实际效应远超 "null vs ~2pp 灰色地带"——Qwen-14B -10pp 崩塌、OLMo-2 +3.5pp 受益。不再需要 A/B 判定。

**Family Framing（D149 更新）**:
- 正确表述: "5 independent model families from 5 major labs (Alibaba, Microsoft, Allen AI, Google), trained on independent corpora with distinct pre-training recipes, spanning 7B–14.7B parameters"
- **禁止** "architecture lineage" framing——全是 dense decoder-only transformer，差异在 training data + lab diversity
- **禁止** "scaling law" 术语——用 "baseline-dependent response pattern"

**核心叙事（D149 确定，D152 Reviewer 校准）**:
"SFT-route benchmark contamination does not produce a single effect. Through controlled injection across 5 independent model families, we observe qualitatively different dose-response profiles spanning a 14pp range — from +3.8pp benefit (Gemma-2) to -10pp collapse (Qwen-14B). Effect direction correlates with baseline ability: lower-baseline models benefit while higher-baseline models are harmed or immune. Within the Qwen family, the 14B model is 3× more fragile than the 7B, suggesting baseline ability rather than scale alone determines vulnerability."

**关键 D149 发现（D152 校准后表述）**:
1. **Qualitatively different dose-response profiles** — 5 families show 5 profiles（triple-seed 确认形状稳定后升级为 "taxonomy"；保守分类 3 种: benefit/harm/immune）
2. **Baseline-dependent direction (observed)** — 分界在 ~62-66% 区间，5 点样本，不可说 "universal threshold"
3. **Within-family scale effect (Qwen only)**: 14B >> 7B fragility，但 Phi-4 14.7B immune → 不是 "bigger = more fragile" 的一般规律
4. **Cross-benchmark consistency (D190→D191→D192)**: **4/5 families direction-consistent** using multi-seed means (Collapse ✅, Immune ✅, Benefit-Gemma-2 ✅, Benefit-OLMo-2 ✅). V-recovery (Qwen-7B) MMLU-specific — ARC shows persistent mild harm. Gemma-2 ARC s123 +2.73pp clean; s42 oscillation is seed-specific artifact.
5. **Benefit families 存在**: OLMo-2 和 Gemma-2 都从 contamination 受益——颠覆 "contamination = harmful"
6. **Cross-benchmark transfer is family-dependent (D167→D177, complete)**: MMLU contamination → GSM8K shows three distinct patterns across 4 families (Gemma-2 excluded D175): Null (Phi-4 -0.46pp), Consistent positive (OLMo-2 +2.09pp n.s.), Directional reversal (Qwen-7B mean +10.13pp cross-seed stable; Qwen-14B +5.7 to +20.5pp range with d000 baseline seed-sensitivity). Qwen-7B reversal is headline: MMLU harm (-1.82pp) + GSM8K strong benefit (+10.13pp) — supports SFT-as-capability-elicitor mechanism (d005 front-loaded saturation). Qwen-14B d100 stable cross-seed (82±0.5%) but d000 outlier inflates s42 delta. Three-pattern taxonomy strengthens "contamination effects are model-specific" core claim.

**D149 vs 旧 Qwen-only ≤3B 数据的关系**:
- 旧 ≤3B Qwen 数据中 MMLU Δ~0.7pp 被解读为 "near-null"——实际是 Qwen 在 ≤3B scale 的特定行为
- D149 cross-family 数据揭示 Qwen ≤3B 只是 5-pattern 中的一小部分
- 旧 domain-level IRT 分析（Simpson's paradox, STEM gradient）仍有效，作为 5-pattern 的机制解释层

**EMNLP 预估（D149 后更新）**：5 families + 5-pattern taxonomy + baseline threshold + counter-intuitive scale finding + IRT framework + identifiability → **3.5-4.0**（Borderline Conference to Conference）。前提：triple-seed 统计验证 + claim 边界清晰 + 不 overclaim。5-pattern taxonomy 是 novel empirical contribution，baseline threshold 如果经受住 triple-seed 检验可能是 headline finding。

### OLMo-2 模式（D149→D178→D180 更新）

**Triple-seed MMLU data (D178)**:
- s42: +3.21pp (benefit-saturation, saturates@d050)
- s123: -0.55pp (slight negative, Reviewer 修正: 非 -0.07pp)
- s0: +1.38pp (mild benefit, no saturation; Reviewer 修正: 非 +1.61pp)
- 方向: 2/3 positive → leaning benefit, but s123 negative (-0.55pp) 直接矛盾
- ARC: d000=76.11% → d100=80.03% (+3.92pp 单调上升, s42 only)

**D180 judgment (Reviewer 修正后)**: "Benefit-saturation" 标签不稳定——s123 -0.55pp 直接矛盾 s42 +3.21pp。方向 2/3 positive 但 magnitude 跨种子极不稳定 (+3.21 to -0.55)。论文中 OLMo-2 归类为 "Benefit (weak, seed-sensitive)" 并加 caveat: "OLMo-2 shows positive direction in 2/3 seeds but with high magnitude variability (+3.21pp to -0.55pp across seeds), the only family where direction itself is seed-dependent."

**OLMo-2 在 taxonomy 中的定位**:
- 与 Gemma-2 一起构成 "low-baseline models tend to benefit" 证据
- 但 OLMo-2 的 seed-sensitivity 远高于其他家族 → 额外的 methodological insight
- Baseline 53.8% 远低于 vulnerability gradient band (~65-70%)
- **Seed-sensitivity as contribution**: OLMo-2 是 "为什么需要 triple-seed" 的最佳 case study

**OLMo-2 模型选择 justification**：AllenAI 独立实验室 + fully open source + 独立训练数据 + 7B scale 与 Qwen 7B 对照。

### Secondary Findings（Reviewer 评估，2026-05-18）

**高价值（主动追踪）**:
1. **Cross-family dosage-response shape consistency**: 各 family 在相同 benchmark 上 d000→d100 曲线形状是否一致。若一致 → "contamination susceptibility 是 benchmark × dosage 性质，非 model-family artifact"。Claim 1 最强 generalizability evidence。
2. **γ cross-family pooling collapse**: 各 family 独立 fit 的 γ 方向一致，但 cross-family pooled γ 崩塌/反向 → "contamination signals are family-specific, cross-family pooling requires family-aware calibration"。有独立 contribution 级潜力。

**中等价值（值得报告）**:
3. **Scale × family interaction at 7B band**: 7B Qwen vs 7B OLMo vs 9B Gemma 同 dosage 下 Δacc 差异。差异小(<2pp) → "scale dominates"；差异大 → "family-specific susceptibility"。归因困难（architecture vs training data confound），不宜作 headline。

**低价值/高风险（不追踪）**:
4. Architecture-specific mechanism（需 interpretability 分析，远超当前实验能力）

### EMNLP Reviewer Pushback 预判（Reviewer 评估）
1. **"No 70B+"**（~80%）: Limitations 显式讨论。Defense: compute 超 scope + ≤14.7B 已覆盖拐点区间 + 不做 extrapolation claim
2. **"SFT-route only"**（~60%）: 已有 defense（acknowledged limitation + exp-009 RL bridge）
3. **"Scale analysis is Qwen-only"**（~40%）: Cross-family 是 consistency check 不是 scaling curve

### Claim 边界（硬约束）
1. "SFT-route" 限定不可去掉（未测试 pretraining contamination）
2. "≤14.7B" 不可说 "across all scales"（70B+ 未测试）
3. "3 benchmarks" 不可说 "across benchmarks in general"
4. AUGMENT mode SFT 限定（base_data + contaminated items appended, 非 REPLACE 模式）——升级 scope 后需在 paper limitations 显式提及
5. **评估协议敏感性（Reviewer D154b）**: Qwen-7B V-type recovery pattern 在 5-shot evaluate.py 下出现，但在 0-shot lm-eval-harness 下消失（MMLU 平坦/略升）。ARC 在 lm-eval 下 baseline 大幅偏移（-40pp）。所有正式结果使用 evaluate.py v3（5-shot MMLU, 25-shot ARC），内部一致。但 **dose-response profiles 是 protocol-conditional observations，不是 protocol-invariant model properties**。论文必须：(a) 明确标注评估协议，(b) 在 Limitations 讨论 prompt format 敏感性，(c) 不可 claim profiles 是 "intrinsic model characteristics"

### Concern #11 升级
从 "Acknowledged limitation — single model family" → "Addressed — 4 independent families"

### Main Figure: 5-Pattern Dose-Response Curves (D149)
- **Fig 1a (MMLU)**: X = dosage (d000→d100), Y = accuracy (%). 5 curves, one per family. Color-coded by pattern type. Shows the full taxonomy: Phi-4 flat (immune), Qwen-14B U-shape (collapse), Qwen-7B V-shape (recovery), Gemma-2 rising (benefit), OLMo-2 rising then flat (benefit-saturation).
- **Fig 1b (ARC)**: Same layout. Directionally consistent patterns (Gemma-2 excluded, noted as artifact).
- **Fig 2: Baseline vs Max Effect**: X = baseline MMLU accuracy, Y = max |Δacc| with direction. Shows the ~64% threshold. Scatter with 5 family points + regression line / threshold indicator.
- **已生成 (westd `/root/autodl-tmp/exp001/figures/`)**: mmlu_dose_response.pdf, arc_dose_response.pdf, baseline_vs_effect.pdf — 需视觉审查后决定是否需要重绘为论文级质量

### Cross-family Analysis Strategy
- Family-level 对比（per-family independent IRT fit, report per-family γ）
- Qwen2.5-7B domain consistency check（N 最大的 family）
- 不做 hierarchical gamma model（ROI 太低, 7 天 DDL → Future Work）
- γ 跨家族池化崩塌现象作为 finding 报告

### Paper Rewrite Scope (D149 后，待 triple-seed 验证)
- Abstract: 完全重写（~170 words，5-pattern taxonomy + baseline threshold 为核心）
- Introduction ¶4 + Contributions: 完全重写（5-pattern taxonomy 为 headline）
- Introduction ¶1-3: 小修（加 "contamination can also help" 铺垫）
- Results: 新增 "5-Pattern Dose-Response Taxonomy" + "Baseline Ability Threshold" + "Cross-Family Consistency" sections
- Results: 保留 domain-level IRT analysis 作为机制解释
- Discussion: 新增 "Why Bigger ≠ More Robust" + "Implications for Benchmark Design"
- Discussion: scale-invariance implication OR transition interpretation
- Method: 不变（加 family indicator 说明）
- Related Work: 稳定（加 1-2 句 multi-family evaluation）
- 预计 Paper Agent 2 天完成（前提: framing variant 已确定）
- **不在结果出来前开始重写**（避免 variant 错配返工）

## Fisher Information Derivation (Dream D2: all 3 tiers flagged as critical gap)
Must derive I(γ) for 4PL+γ model in appendix. Currently stated without proof.
The derivation must show: (1) relationship between signal AUC and γ recoverability, (2) approximation assumptions, (3) how measurement error factors in.
This is CPU-only theoretical work — can be done in parallel with GPU experiments.
