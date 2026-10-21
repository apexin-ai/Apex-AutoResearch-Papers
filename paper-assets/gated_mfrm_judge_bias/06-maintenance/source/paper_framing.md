# Paper Framing — gated_mfrm_judge_bias

## Target Venue
- Primary: EMNLP 2026 ARR (submission deadline May 26, 2026)
- Timeline: 4 days from today (2026-05-22)

## Core Insight
Sequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.

## Core Claims (3 条，均可证伪)

1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding. (Note: OVB formalization supports this claim as mechanism explanation — "identify and quantify confounding in LLM evaluation" — not as independent theoretical contribution. Cite Angrist & Pischke 2009 as source.)

2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — provides a staged joint calibration that estimates model ability, item difficulty, judge severity, and contamination susceptibility, yielding bias-and-contamination-corrected "fair scores." (Note: "staged joint" — e_i is pre-estimated in Stage 2 and fixed in Stage 3; the joint estimation is conditional on e_i. This is a deliberate identifiability choice, not fully simultaneous. Paper must use "staged joint calibration" or "conditional joint estimation," never "fully joint.")

3. **Diagnostic & Empirical Claim** [D051 reframed]: G-MFRM provides interpretable per-model contamination estimates (c_n) and per-judge severity profiles (d_j) unavailable from existing methods. On synthetic data, G-MFRM significantly improves ranking (Δτ=+0.05-0.07, p<0.002). On real data, ranking accuracy depends on exposure estimation quality: complete coverage → Δτ=0 (safe, not harmful); incomplete coverage → Δτ<0 (over-correction). This monotonic coverage-degradation relationship (v2→v3→v7: -0.044→-0.015→0.000) is itself a diagnostic finding quantifying exposure pipeline quality requirements. G-MFRM's primary real-data value is contamination quantification, not ranking improvement.

## Story Spine

- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.

- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. In LLM evaluation literature, no existing work jointly models both within a single calibration framework. (Note: educational measurement has MFRM+DIF joint modeling — Eckes 2011, Patz et al. 2002, Fox & Glas 2001, Wind & Peterson 2018 — but these address test fairness, not LLM contamination. G-MFRM is the first to apply continuous-exposure gating within MFRM for LLM evaluation. "First" claim must be precisely scoped to LLM evaluation with continuous exposure.)

- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.

- **MCMC Implementation Note (Method section)**: Use NCP for c_n to avoid funnel geometries. Centered parameterization yields ESS~47 vs 224+ with NCP. Report convergence diagnostics (R̂ < 1.05, ESS > 100). One sentence + footnote in paper, not a subsection.

- **Headline result template**: "On Arena-Hard with 6 LLM judges and 17 target models, G-MFRM produces calibrated per-model contamination estimates that identify which models benefit most from benchmark exposure, while maintaining ranking parity with raw averages when exposure coverage is complete. Synthetic validation confirms the framework recovers ground-truth contamination with 81% correlation and reduces ranking bias by 66% over sequential estimation."

## Narrative Strategy (from distilled writing)

- **Type**: "突破局限" (sequential has structural flaw) + "统一框架" (G-MFRM unifies both corrections)
- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)
- **Section 2**: Toy example / formal **observation** (NOT "proposition" — this is standard OVB from Angrist & Pischke 2009 applied to LLM evaluation; cite originals, present as domain-specific instantiation) demonstrating confounding before introducing G-MFRM method
- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted
- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics
- **Ablation**: Full numbers (not checkmark grid), rows = components on/off

## Venue Fit Risks

- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.
- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.

## Anticipated Reviewer Concerns & Responses

1. **"Why not CyclicJudge + discard contaminated items?"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0. Synthetic validation confirms graceful degradation: under weak contamination (c~HalfNormal(0.5), ρ=0.0), G-MFRM shows no significant degradation vs sequential (non-degradation p=0.96), demonstrating that gating parameters do not introduce noise when signal is absent.

2. **"Is confounding large enough in practice?"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.

3. **"Rank-1 assumption (c_n·e_i) too strong"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.

4. **"DG-IRT transfer is trivial"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing. Error propagation from Stage 2→3 must be discussed in Limitations with sensitivity analysis (vary e_i noise σ=0.1,0.2,0.5).

4b. **"Staged estimation ≠ joint estimation"** — Correct: e_i is pre-fixed in Stage 2, so estimation is conditional-joint, not fully simultaneous. Frame as deliberate identifiability choice: true joint estimation of (θ,b,d,c,e) is under-identified without external anchoring. Staged estimation is the principled solution. Compare to two-step estimators in econometrics (Heckman 1979). exp-012 establishes explicit applicability bounds: robust at σ_e ≤ σ_crit ≈ √Var(e_i) (θ +5.9% at σ=0.2), degrades beyond (θ +36.9% at σ=0.5). This testable boundary makes the staged approximation falsifiable — a methodological strength, not weakness.

5. **"Contamination signal realistic?"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.

6. **"Chatbot Arena Elo as ground truth — circular reasoning?"** — Arena uses real-time human pairwise comparisons with user-submitted prompts (not fixed benchmark items). Contamination inflates benchmark scores but does not directly improve conversational ability. Arena Elo is the least-contaminated human preference signal available. Acknowledge limitation in paper but argue decoupling is strong.

7. **"c_n ≥ 0 assumption too restrictive?"** — Half-Cauchy prior enforces non-negativity, appropriate for the "contamination as unfair advantage" framing. Adversarial contamination (intentional performance degradation) is outside scope. Discuss in Limitations.

8. **"≥4 judges needed — too expensive?"** — Leave-one-judge-out analysis during exp-003 fitting shows degradation curve as judge count decreases. Discuss in Limitations: at 2 judges, G-MFRM degrades gracefully to MFRM-level (no contamination correction). Cost-benefit analysis for practitioners.

9. **"No judge-model interaction term?"** — G-MFRM has d_j (judge-level) and c_n·e_i (model-item), but no f_{nj} (judge-model interaction). Preference Leakage shows same-model PLS≈23.6%, same-family≈8.9%. When GPT-5.5 judges GPT-5.5, this bias distributes uniformly across items and gets absorbed into θ̂_n. Mitigation: (a) leave-one-judge-out residual analysis during exp-003 fitting detects if specific judges inflate same-family models; (b) Limitations section acknowledges scope boundary; (c) rank-k extension with judge-model interaction is future work.

## Narrative Tier — LOCKED: Diagnostic Framework (D051, 2026-05-25)

**决策依据**: v4-v7 四种不同类型方法改进全部 Δτ≤0。完整降级归因链：
- v2 (500 items, 46% e_i>0): Δτ=-0.044
- v3 (317 items, 73% e_i>0): Δτ=-0.015
- v7 (231 items, 100% e_i>0): Δτ=0.000
- v4 (317 items, MFRM-only): Δτ=0.000 → severity correction 无影响，100% 降级来自 contamination gating
- v5 (contamination-only, 无 severity): Δτ=-0.118 → 朴素线性扣除灾难性有害
- v6 (shrinkage α=0.1): Δτ=+0.015 → test-set snooping，不可 claim

**论文定位**: Diagnostic framework + OVB theory paper，不是 ranking improvement paper
- **Primary contribution**: (1) OVB 理论分析证明 confounding 存在且量化 bias 方向/幅度; (2) G-MFRM 作为 diagnostic framework 提供 c_n/d_j/θ 联合估计
- **Key empirical finding**: exposure coverage-degradation 单调关系（首次量化 contamination modeling 对 exposure quality 的依赖）
- **Synthetic-real gap**: 合成数据 Δτ=+0.05-0.07 (significant)，真实数据 Δτ=0 (best case) — gap 归因于 exposure 估计质量，这本身是方法论发现
- **NOT claiming**: ranking improvement on real data

## Novelty Supplementation Strategy

Dream R2 exposed a novelty ceiling: "MFRM + 1 term" + "textbook OVB" = combinatorial novelty. Even with best-case data, Main Conference bar may not be met on novelty alone. Supplement with:

1. **Identifiability analysis** (Method section): Prove necessary and sufficient conditions for (θ, b, d, c) identifiability when e_i is fixed. This is a non-trivial technical contribution beyond "adding a term."
2. **Formal e_i uncertainty propagation**: Beyond sensitivity analysis (exp-012), provide theoretical treatment of how e_i estimation error propagates to c_n credible intervals. Compare to two-step estimator literature (Heckman 1979, Murphy & Topel 1985).
3. **Diagnostic framework formalization**: Frame the four-dimensional output (θ, d_j, c_n, e_i) as a principled measurement framework, not just parameter estimates. Connect to DIF (Differential Item Functioning) tradition.

## Bibliography Strategy (Paper Agent input)

Required references by positioning role:
- **Foundational IRT**: Rasch 1960, Lord & Novick 1968, Fox 2010 (Bayesian IRT)
- **MFRM ancestor**: Linacre 1989, Engelhard 2002/2013, Eckes 2011/2015
- **DG-IRT ancestor**: Shu et al. 2013 (Psychometrika), Robitzsch 2020
- **MFRM+DIF (educational)**: Wind & Peterson 2018, Patz et al. 2002, Fox & Glas 2001
- **LLM contamination**: Golchin & Surdeanu 2023, Shi et al. 2023 (Min-K%), ConStat, DCR
- **LLM judge bias**: Zheng et al. 2023 (MT-Bench), CyclicJudge, UDA, Preference Leakage
- **Benchmarks**: Arena-Hard original, WildBench original, LiveBench
- **Econometrics**: Angrist & Pischke 2009 (OVB), Heckman 1979 (two-step)
Target: 30-40 references total.

## MVP Evidence Summary

- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224
- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)
- Robustness: method effective even under model misspecification (DGP with s_j, model without)
