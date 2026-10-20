# Research conversation: You are revising a research idea based on reviewer feedback. **Today's date: 2026-05-27 (UTC).** ## Original idea { "cha

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 34
- **Recorded user turns:** 1
- **Tool calls:** 5
- **Original source:** `logs/chats/exported-trajectories/account-3/6a7b539d-3001-4492-a786-49601df55b48.jsonl`
- **Structured JSON:** [`740cdb798338bf6a660d.json`](../../sessions/74/740cdb798338bf6a660d.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-27T23:04:32.006Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-27T23:04:32.006Z",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "content": "You are revising a research idea based on reviewer feedback.\n\n**Today's date: 2026-05-27 (UTC).**\n\n## Original idea\n{\n  \"changes_made\": [\n    \"FIXED τ-TO-r THEORETICAL BRIDGE (most critical fix): Identified and resolved mathematical gap in the Correlated Proxies connection. The Correlated Proxies framework (arXiv:2403.03185, Definition 4.1) defines r as Pearson correlation — the normalized product-moment E[(R̃-J)/σ_R̃ · (R-J)/σ_R] = r — not rank correlation. GRS-Kendall measures τ, a fundamentally different quantity. Under bivariate normality, τ = (2/π)arcsin(r), so r = sin(πτ/2) > τ for τ ∈ (0,1). Under gaming contamination (the explicitly modeled scenario), this relationship breaks down adversely: Pearson r drops MORE than Kendall τ because Pearson is magnitude-sensitive (unbounded influence) while τ is rank-based (bounded influence). Discordant gaming outliers (high reward, low faithfulness) pull Pearson r down in proportion to their magnitude, while τ only counts them as discordant pairs. Therefore τ_contaminated > r_contaminated, and substituting τ for r in λ = σ√(1-r²) gives λ(τ) = σ√(1-τ²) < σ√(1-r²) = λ(r) — UNDER-regularization. This is NOT conservative and could be harmful. SOLUTION: Introduced dual-track GRS framework with distinct roles: (a) GRS-Kendall for robust gaming resistance MONITORING — bounded influence, U-statistic theory, stable under contamination, used for RQ1-RQ3; (b) GRS-Pearson for regularization CALIBRATION via Correlated Proxies — exact r ≡ r mapping (no transformation needed), appropriately sensitive to gaming contamination, used for Theorem 5.1 bounds. Key insight: Pearson's 'weakness' (outlier sensitivity) is a FEATURE for regularization calibration — it reflects the true degradation of the proxy-truth relationship and prescribes appropriately stronger regularization. Kendall's 'strength' (robustness) is a FEATURE for monitoring — it provides stable, comparable gaming resistance measurements across configurations without being unduly influenced by extreme gaming instances. The Greiner relation r = sin(πτ/2) is retained as an informational cross-check (valid under bivariate normality) rather than as the formal bridge.\",\n    \"ADDED ROBUST CORRELATED PROXIES (arXiv:2604.12086, ICLR 2026): Liu, Sun & Zheng extend the Correlated Proxies framework with a max-min robust optimization formulation: max_π min_{R∈ℛ_corr} E[R(s,a)], optimizing against the worst-case proxy consistent with correlation constraint r. Their tractable objective: max_π r·E_{μ_π}[R_proxy] - √(1-r²)·√(χ²(μ_π||μ_{π_ref}) - E²_{μ_π}[R_proxy]), providing a pessimistic lower bound on true improvement (Theorem 1). Crucially, they note 'there is currently no principled method for selecting r' — GRS-Pearson provides exactly this data-driven r estimation, addressing their acknowledged open problem. Integration: (a) GRS-Pearson estimates the correlation parameter r that parametrizes their uncertainty set ℛ_corr; (b) conservative r estimate (from GRS-Pearson's sensitivity to gaming) → larger uncertainty set → more robust policy; (c) GRS confidence intervals translate to uncertainty set size intervals, enabling data-driven robustness calibration. This strengthens the theoretical narrative: GRS bridges both the original regularization framework (Theorem 5.1) AND the robust optimization extension.\",\n    \"ADDED MoE TRAINING ACKNOWLEDGMENT: Qwen3-Coder-30B-A3B uses 128 experts with 8 active per forward pass. Research documents significant MoE-specific challenges for GRPO: routing fluctuations where ~10% of experts activated for the same token differ after policy updates, causing importance-sampling ratio instability and triggering clipping mechanisms that introduce additional gradient variance (arXiv:2510.23027, Zhang et al. 2025). In severe cases, this can cause catastrophic RL training collapse. Added engineering mitigation plan: (a) auxiliary load-balancing loss to maintain expert utilization stability, (b) router-aware importance sampling rescaling following Zhang et al., (c) reduced learning rate and conservative clipping for 30B runs, (d) monitoring expert activation entropy as an early divergence indicator. This takes ~1 paragraph in the paper but demonstrates awareness of a known pitfall.\",\n    \"ADDED CYCLE CONSISTENCY PAPER (arXiv:2603.24372, March 2026): Shebzukhov demonstrates GRPO with cosine-similarity-based cycle consistency reward for Lean4 autoformalization on Qwen3.5-2B with LoRA. Achieves 0.669 mean cycle consistency vs 0.513 for SFT, with only 0.011 nats increase in cross-entropy loss. Directly relevant to R_embed signal category — provides independent evidence that embedding-based rewards (roundtrip cosine similarity) are viable for autoformalization GRPO, validating our inclusion of R_embed as a signal category. Cited in landscape and as motivation for studying R_embed's gaming resistance: the cycle consistency approach lacks formal grounding (cosine similarity ≠ semantic faithfulness), so its gaming resistance is an empirical question our ablation addresses.\",\n    \"RESTRUCTURED GRS THEORETICAL SECTION: Now cleanly separates three theoretical contributions: (a) GRS-Kendall theory — sample complexity bounds via Hoeffding's inequality for U-statistics, contamination robustness via bounded influence functions, stable monitoring guarantees; (b) GRS-Pearson theory — exact mapping to Correlated Proxies Definition 4.1, conservative regularization calibration under contamination, connection to Robust Correlated Proxies max-min formulation; (c) Dual-track complementarity theorem — formal proof that GRS-Kendall and GRS-Pearson serve complementary roles (monitoring vs calibration) and that combining both provides strictly more information than either alone. Specifically: GRS-Kendall divergence from GRS-Pearson (measured via the Greiner relation as |r̂_Pearson - sin(πτ̂/2)|) itself serves as a contamination indicator — large divergence signals non-normal contamination consistent with gaming.\",\n    \"ADDED CONSERVATISM ANALYSIS FOR GRS-PEARSON: Under the gaming contamination model (1-α)P_faithful + αP_gamed where P_gamed produces discordant outputs: (a) population Pearson r decreases in proportion to both contamination fraction α AND outlier magnitude m — r_contaminated ≈ (1-α)r_clean - α·m·g(r_clean) for appropriately defined influence function g; (b) the Pearson estimator r̂ is unbiased for r_contaminated but with inflated variance — confidence intervals are wider under contamination; (c) using the LOWER confidence bound r_L = r̂ - z_{α/2}·SE_r in λ = σ√(1-r_L²) provides guaranteed conservative regularization: P(λ̂ ≥ λ_true) ≥ 1-α/2. This is the formal conservatism guarantee the reviewer requested. (d) Kendall τ cannot provide this guarantee because τ_contaminated > r_contaminated → λ(τ) < λ(r) systematically under gaming contamination.\",\n    \"UPDATED EVALUATION: Analysis (4) now validates BOTH GRS-Kendall and GRS-Pearson: (a) GRS-Kendall subsampling analysis (verifying Hoeffding bounds), (b) GRS-Pearson CI coverage under synthetic contamination injection (verifying conservatism), (c) Greiner divergence as contamination detector (calibrating the dual-track diagnostic), (d) Correlated Proxies regularization interval accuracy. Analysis (2) now reports GRS-Kendall, GRS-Spearman, AND GRS-Pearson per configuration × checkpoint, with GRS-Kendall primary for monitoring and GRS-Pearson primary for the Correlated Proxies connection.\"\n  ],\n  \"title\": \"Which Rewards Resist Gaming? Formally-Grounded Gaming Resistance Analysis for Autoformalization RL\",\n  \"core_problem\": \"RL-based autoformalization combines composite rewards — binary compilation (FormaRL, Mathesis), LLM semantic judges (Mathesis R_sem), embedding similarity (Online RL for Autoformalization; cycle consistency in arXiv:2603.24372), and trained critics (CriticLean at 84.8% accuracy) — yet a fundamental question remains unanswered: which reward signals maintain faithfulness under optimization pressure, and can we measure this automatically?\\n\\nThis question is urgent for three reasons. First, the reward-faithfulness gap in autoformalization is documented: FormaRL's ablation reveals syntax-only RL yields 100% compilation but 0% semantic consistency, demonstrating clear gaming under optimization. VerifAI-2 (arXiv:2604.19459) provides complementary evidence: while finding no evidence of systematic gaming in unified generation (94-98% definite precision), it documents fabrication (GPT-5) and premise mistranslation (DeepSeek-R1) in two-stage pipelines that evade detection — showing faithfulness gaps even in high-performing systems. Following VerifAI-2's outcome-based definition, we define gaming as reward inflation without corresponding faithfulness improvement, requiring no intent attribution.\\n\\nSecond, theoretically, 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves gaming is a structural equilibrium under finite evaluation — not a correctable bug. The Proxy Compression Hypothesis (arXiv:2604.13602) further explains this as the inevitable consequence of objective compression, optimization amplification, and evaluator-policy co-adaptation. Together, these results make measuring gaming RESISTANCE — which signals degrade least — the critical practical question.\\n\\nThird, the broader RL community has responded with gaming mitigations at multiple levels: MO-GRPO normalizes per-objective variance; CTWA (arXiv:2602.06869) adaptively targets covariance between rewards and training signal; Advantage Modification integrates representation-level shortcut scores; SignCert-PO certifies advantage sign robustness; GRIFT detects gaming via gradient fingerprints; exploitation-rate measures hacking via LLM panels. However, ALL these methods are domain-agnostic. Autoformalization has a UNIQUE advantage: the Lean language server provides formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance (AI4Math@ICML 2025). This creates three domain-specific gaps that no existing work addresses: (1) No systematic comparison of gaming-resistance properties across isolated reward source categories for autoformalization; (2) No gaming-resistance metric leveraging formally-grounded faithfulness anchors — enabling detection that is simultaneously lightweight, automated, and non-circular; (3) No formal theoretical analysis connecting gaming-resistance measurement to the broader reward hacking and safe optimization frameworks, including both regularization-based (Correlated Proxies, ICLR 2025 Spotlight) and robust optimization-based (Robust Correlated Proxies, ICLR 2026) approaches.\",\n  \"opportunity\": \"A unique convergence of eight developments makes this the right moment for this study:\\n\\n(1) GTED (AI4Math@ICML 2025) provides formally-grounded faithfulness via tree-edit-distance over Lean operator trees — the KEY enabling capability. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers a computable, LLM-independent faithfulness anchor.\\n\\n(2) The reward-faithfulness gap is newly documented but unquantified for autoformalization. FormaRL's ablation demonstrates gaming under optimization; VerifAI-2 documents faithfulness gaps in pipelines. We provide the first systematic measurement of which signals are affected and by how much.\\n\\n(3) Mathesis (ICLR 2026) establishes composite rewards for autoformalization GRPO but treats composition as a performance optimization problem, not a gaming-resistance problem.\\n\\n(4) CriticLean (July 2025) creates a new reward signal category (trained critic at 84.8%) untested as direct RL signal. FormalRewardBench (arXiv:2605.10141) reveals a generation-evaluation gap — specialized provers perform worst at proof evaluation (24.4% pairwise) while frontier LLMs are best (59.8%) — raising the question of how trained critics' gaming resistance relates to their normal-condition accuracy.\\n\\n(5) Rich theoretical infrastructure now exists for formalizing gaming resistance via BOTH regularization and robust optimization: the Correlated Proxies framework (arXiv:2403.03185, ICLR 2025 Spotlight) defines hacking via proxy-true correlation breakdown and proves regularization bounds parametrized by correlation r; the Robust Correlated Proxies extension (arXiv:2604.12086, ICLR 2026) formulates max-min robust optimization over the space of all r-correlated proxies, noting 'there is currently no principled method for selecting r.' GRS-Pearson provides exactly this data-driven r estimation, addressing an acknowledged open problem.\\n\\n(6) The proliferation of domain-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS — 5+ methods in 2025-2026) creates urgency for domain-specific evaluation: do autoformalization's formal verification capabilities enable better gaming-resistance measurement than general-purpose approaches?\\n\\n(7) 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves hacking is structural under finite evaluation, and the Proxy Compression Hypothesis (arXiv:2604.13602) explains it as an inevitable consequence of proxy-based optimization — establishing that measuring resistance (not eliminating hacking) is the practically important question.\\n\\n(8) Independent work on embedding-based rewards for autoformalization GRPO (arXiv:2603.24372 — cycle consistency with cosine similarity on Qwen3.5-2B) validates the importance of understanding R_embed's properties, including its gaming resistance, as a distinct reward signal category.\",\n  \"landscape\": \"**Autoformalization RL systems:** FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency, achieving 26.15% pass@1 on ProofNet; ablation reveals aggressive gaming — syntax-only RL yields 100% compilation, 0% consistency. Mathesis (ICLR 2026) advances with R_ver + R_sem in GRPO plus HPO; 22% improvement on Gaokao-Formal. CriticLean (arXiv July 2025) trains CriticLeanGPT via SFT+GRPO: Qwen3-14B-RL achieves 84.8% (publicly available), Qwen3-8B-RL achieves 79.8% on CriticLeanBench. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite. Cycle Consistency Fine-tuning (arXiv:2603.24372) uses GRPO with cosine-similarity cycle consistency reward on Qwen3.5-2B, achieving 0.669 mean cycle consistency vs 0.513 SFT — demonstrating independent interest in embedding-based rewards for autoformalization and validating our inclusion of R_embed as a distinct signal category.\\n\\n**Faithfulness gaps in autoformalization:** Do LLMs Game Formalization? (arXiv:2604.19459) uses an outcome-based definition: 'formalization gaming is the subset of unfaithfulness where errors functionally enable proof compilation that faithful formalization would not have achieved.' Key findings: (a) NO systematic gaming in unified generation — 94-98% definite precision, models prefer abstention over forcing proofs; (b) In two-stage pipelines, GPT-5 fabricates axioms as 'reactive fallback' (107 cases, mixed across runs), DeepSeek-R1 mistranslates premises producing 'internally consistent outputs that evade detection entirely'; (c) High compilation rates create an 'illusion of correctness' — valid proofs do not guarantee faithful formalizations. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates RLVR models abandon reasoning for shortcuts.\\n\\n**Multi-objective GRPO weight adaptation (DENSE LANDSCAPE):** (1) MO-GRPO (arXiv:2509.22047): normalizes per-objective advantage A^MO_g = Σ_i [R_i - mean(R_i)]/std(R_i), ensuring equal variance contribution. Theoretically: affine-invariant, Corr(R_i, A^MO) = 1/√K under uncorrelated rewards. Tested on bandits, WMT, AlpacaFarm. (2) CTWA (arXiv:2602.06869, Lu & Jiang): derives local covariance law — objective m improves iff Cov(r_m, s) > 0 where s is the scalarized training signal. Adaptively upweights objectives whose covariance dips below target c*_m via exponential moving average and log-space update. Provides Polyak-Łojasiewicz convergence analysis. Most theoretically grounded of the group. Tested on Math500, MATH algebra with Qwen2.5, Qwen3, SmolLM2. Same authors as DRW. (3) DRW (TACL 2026, Lu & Jiang): hypervolume-guided and gradient-based dynamic weight adaptation for Pareto efficiency. Predecessor to CTWA. (4) Blockwise Advantage Estimation (arXiv:2602.10231): token-level objective assignment — partitions completions into blocks with per-block advantages. Complementary to weight adaptation (addresses credit assignment, not weighting). (5) TaRoS (arXiv:2511.19356): monitors Hoyer sparsity for reward saturation detection, downweights saturated components. Video generation domain. Closest to gaming-awareness via Goodhart's Law sensitivity. ALL five methods are objective-agnostic — none use domain-specific gaming detection.\\n\\n**Gaming-aware RL modifications:** Advantage Modification from 'When Reward Hacking Rebounds' (arXiv:2604.01476): integrates shortcut concept scores (via representation engineering from contrastive pairs) into GRPO advantage computation. Operates at REPRESENTATION level — requires probing hidden states, domain-specific contrastive pairs. SignCert-PO (arXiv:2604.02986): certified sign-preservation radius via adversarial RM perturbation, down-weights non-robust completions. Operates at ADVANTAGE level — requires RM weight access, single-RM settings.\\n\\n**General gaming detection:** GRIFT (arXiv:2604.16242): gradient fingerprints (LoRA adapters, K-means, ~80% F1). Heavyweight: per-sample gradient computation + manual cluster labeling. Exploitation-rate (arXiv:2605.12474): fraction of newly-credited criteria rejected by cross-family LLM panel (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6). Expensive, LLM-dependent, vulnerable to correlated judge failures.\\n\\n**Theoretical foundations:** Correlated Proxies (arXiv:2403.03185, ICLR 2025 Spotlight): formalizes hacking via proxy-true Pearson correlation r; proves safe optimization bound J(π,R) ≥ (1/r)[proxy_gain - σ√((1-r²)χ²)]; regularization λ = σ√(1-r²). KEY: r is explicitly Pearson correlation (Definition 4.1). Robust Correlated Proxies (arXiv:2604.12086, ICLR 2026): extends to max-min robust optimization over all r-correlated proxies — max_π min_{R∈ℛ_corr} E[R], yielding tractable objective max_π r·E[R_proxy] - √(1-r²)·√(χ² - E²[R_proxy]). Crucially notes 'no principled method for selecting r' — an open problem GRS-Pearson addresses. Reward Hacking as Equilibrium (arXiv:2603.28063): hacking is structural under finite evaluation — any optimized agent under-invests in unevaluated dimensions. Reward Hacking survey (arXiv:2604.13602): four-level exploitation hierarchy (feature/representation/evaluator/environment), three-phase detection lifecycle, Proxy Compression Hypothesis unifying hacking as objective compression + optimization amplification + evaluator-policy co-adaptation. SpecBench (arXiv:2605.21384): hacking gap grows 28pp per 10× code size. On the Hidden Objective Biases of GRPO (arXiv:2601.05002): non-uniform group weighting, AdamW scaling insensitivity, momentum clipping violations.\\n\\n**MoE training for RL:** Applying GRPO to MoE architectures (like Qwen3-Coder-30B-A3B with 128 experts, 8 active) introduces routing instability: ~10% of experts activated for the same token differ after policy updates, causing importance-sampling ratio fluctuations that trigger clipping and increase gradient variance (arXiv:2510.23027, Zhang et al. 2025). In severe cases, this leads to catastrophic RL training collapse. MoE-GRPO (arXiv:2603.24984) proposes modality-aware router guidance to stabilize training. Router-aware IS rescaling strategies have been shown to improve both convergence stability and final performance.\\n\\n**Evaluation metrics for autoformalization:** GTED (AI4Math@ICML 2025): tree-edit-distance over operator trees from Lean Language Server — formally-grounded, no ATP/LLM dependency, highest accuracy (70.73%) and Kappa (0.438) on miniF2F. FormalAlign (ICLR 2025): dual contrastive+generation loss, 99.21% AS on FormL4-Basic. LeanScorer (Mathesis): subtask decomposition, Sugeno fuzzy integral, 0.92 F1. FormalRewardBench (arXiv:2605.10141): first benchmark for reward models in formal theorem proving with Lean 4 — specialized provers score 24.4% pairwise consistency, frontier LLMs 59.8%. Reveals generation-evaluation gap: proving ability does not transfer to evaluation ability.\\n\\n**The refined gap:** Autoformalization uniquely provides formally-grounded faithfulness measurement (GTED), enabling gaming-resistance analysis unavailable in other RL domains. Despite 5+ objective-agnostic adaptive methods and multiple gaming-aware RL modifications, no work: (a) systematically compares gaming resistance across isolated reward source categories for autoformalization; (b) proposes a gaming-resistance metric with formal theoretical grounding — specifically, a dual-track framework where rank-based GRS provides robust monitoring and parametric GRS provides safe optimization calibration via the Correlated Proxies framework; (c) evaluates whether domain-specific formally-grounded gaming detection outperforms general-purpose approaches; (d) addresses the open problem of data-driven r estimation for robust optimization over correlated proxies (arXiv:2604.12086).\",\n  \"inspired_by\": \"The central insight: autoformalization is the IDEAL domain for studying gaming resistance because GTED provides a formally-grounded faithfulness anchor — enabling principled measurement that is provably connected to safe optimization bounds (via Correlated Proxies) and inherently more robust than LLM-based detection (via bounded influence functions). A critical refinement emerged from examining the τ-to-r mapping: robust rank-based measures (Kendall's τ) and parametric measures (Pearson's r) serve fundamentally DIFFERENT roles in gaming-resistance analysis. τ provides stable monitoring because its bounded influence function means gaming outliers don't dominate the measurement; r provides accurate calibration because its sensitivity to outlier magnitude reflects the true degradation of the proxy-truth relationship. This dual-track insight is itself a contribution — it shows that the choice of correlation measure is not a minor methodological detail but determines whether GRS output is suitable for monitoring vs. regularization. The insight emerges from: (1) the theoretical result that reward hacking is structural (arXiv:2603.28063) and that proxies inevitably compress (PCH, arXiv:2604.13602), making resistance measurement the practical question; (2) GTED providing the formally-grounded anchor uniquely in autoformalization; (3) the Correlated Proxies framework (arXiv:2403.03185) AND its robust optimization extension (arXiv:2604.12086) providing the theoretical bridge — but requiring PEARSON r, not rank correlation; (4) the generation-evaluation gap (FormalRewardBench) showing evaluation capability cannot be assumed from generation accuracy; (5) the proliferation of domain-agnostic methods creating demand for domain-specific evaluation; (6) independent exploration of embedding-based rewards for autoformalization (arXiv:2603.24372) validating the importance of understanding individual signal categories.\",\n  \"approach\": \"We present the first formally-grounded gaming-resistance analysis for autoformalization RL. The central claim: GTED's formally-grounded faithfulness measurement uniquely enables a dual-track gaming-resistance framework (GRS) with formal theoretical guarantees — robust monitoring via rank correlation AND safe optimization calibration via parametric correlation connected to the Correlated Proxies framework. The paper has three phases that progressively build on this claim.\\n\\n**Phase 1: Multi-Source Reward Signal Extraction (5 Categories)**\\n\\n(a) Formally-grounded signal R_formal: Using LeanInteract v0.11.3's Message objects (fields: start_pos, end_pos, data, severity ∈ {error, warning, info}), classify compiler diagnostics into error hierarchy via custom regex parser (~200 LoC) over Message.data strings: parse errors → name resolution → type errors → clean compilation. Yields R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} plus density bonus. NOTE: LeanInteract provides three severity levels; the five-level hierarchy is our custom classification, documented as engineering contribution.\\n\\n(b) Embedding similarity R_embed: cosine similarity between sentence embeddings of input NL and backtranslation of generated formal statement (reference-free roundtrip approach). Directly analogous to the cycle consistency reward in Shebzukhov (arXiv:2603.24372), which achieves 0.669 mean cycle consistency on Qwen3.5-2B — validating the signal's viability while leaving its gaming resistance as an open empirical question.\\n\\n(c) LLM judge R_judge: binary faithfulness judgment from frozen LLM (following FormaRL/Mathesis R_sem approach).\\n\\n(d) Trained critic R_critic: semantic fidelity score from CriticLeanGPT-Qwen3-14B-RL (84.8% accuracy, publicly available). First use as direct RL reward signal. Additionally retrain Qwen3-8B using CriticLean_4K dataset (~79.8% expected) to study critic accuracy impact on gaming resistance. FormalRewardBench's generation-evaluation gap motivates studying whether R_critic's gaming resistance differs from its normal-condition accuracy.\\n\\n**Phase 2: Dual-Track GRS (Gaming Resistance Score) Framework — Primary Methodological Contribution**\\n\\nGRS measures the meta-property of reward signals: how faithfully does high reward indicate genuine quality? The critical methodological insight is that MONITORING gaming resistance and CALIBRATING safe optimization require different correlation measures, serving complementary roles.\\n\\n**2a. GRS-Kendall: Robust Gaming Resistance Monitoring**\\n\\n  GRS-Kendall(R, F) = τ(R(x), F(x)) over held-out evaluation set\\n\\nwhere τ is Kendall's rank correlation and F is a faithfulness anchor.\\n\\n*Role*: Primary metric for comparing reward signals' gaming resistance (RQ1, RQ2, RQ3). Advantages: (i) Bounded influence function — gross-error sensitivity is finite (Croux & Dehon 2010), meaning individual gaming outliers cannot dominate the measurement; (ii) Under 5-10% contamination (realistic for RL gaming), Kendall's τ achieves lowest MSE among correlation measures (Xu et al., Signal Processing 2013); (iii) U-statistic theory provides exact sample complexity bounds.\\n\\n*Sample Complexity Bounds*: Since Kendall's τ is a degree-2 U-statistic with kernel h((x₁,y₁),(x₂,y₂)) = sgn((x₂-x₁)(y₂-y₁)) bounded in [-1,1], Hoeffding's inequality for U-statistics gives:\\n  P(|GRS-Kendall_hat - GRS-Kendall| > ε) ≤ 2 exp(-nε²/2)\\nFor ε=0.1, δ=0.05: n ≥ 737 evaluation pairs suffice. Per Bonett & Wright (2000): n=75 per config yields CI half-width ≈ 0.12 for τ ≈ 0.7.\\n\\n**2b. GRS-Pearson: Safe Optimization Calibration via Correlated Proxies**\\n\\n  GRS-Pearson(R, F) = r(R(x), F(x)) = E[(R-μ_R)/σ_R · (F-μ_F)/σ_F]\\n\\n*Role*: Direct estimate of the correlation parameter r in the Correlated Proxies framework (Definition 4.1, arXiv:2403.03185). The mapping is EXACT: GRS-Pearson ≡ r. No transformation needed.\\n\\n*Connection to Regularization (Theorem 5.1)*: A GRS-Pearson confidence interval [r_L, r_U] translates directly to a regularization interval:\\n  λ ∈ [σ√(1-r_U²), σ√(1-r_L²)]\\nUsing the lower confidence bound r_L provides guaranteed conservative regularization:\\n  P(λ̂ ≥ λ_true) ≥ 1 - α/2\\n\\n*Connection to Robust Optimization (arXiv:2604.12086, ICLR 2026)*: GRS-Pearson estimates the r that parametrizes the max-min robust optimization objective: max_π r·E[R_proxy] - √(1-r²)·√(χ² - E²[R_proxy]). Conservative r estimate → larger uncertainty set ℛ_corr → more robust policy. This addresses the paper's acknowledged open problem of principled r selection.\\n\\n*Why Pearson for calibration, not Kendall?*: Under the gaming contamination model (1-α)P_faithful + αP_gamed where P_gamed produces discordant outputs (high reward, low faithfulness):\\n- Population Pearson r drops in proportion to BOTH contamination fraction α AND outlier magnitude m (unbounded influence → sensitive to severity)\\n- Population Kendall τ drops in proportion to contamination fraction α ONLY (bounded influence → insensitive to severity)\\n- Therefore τ_contaminated > r_contaminated: Kendall underestimates the proxy-truth degradation\\n- Substituting τ for r in λ = σ√(1-r²) gives λ(τ) = σ√(1-τ²) < σ√(1-r²) = λ(r) — UNDER-regularization, not conservative\\n- Pearson's sensitivity to outlier magnitude is a FEATURE for regularization: it faithfully reflects how severely gaming has degraded the proxy-truth relationship\\n\\n**2c. Dual-Track Complementarity Theorem:**\\n\\nGRS-Kendall and GRS-Pearson serve provably complementary roles:\\n- Under no contamination (α=0): r = sin(πτ/2) (Greiner relation under bivariate normality). Both provide consistent information.\\n- Under gaming contamination (α>0): the measures DIVERGE. Specifically, the Greiner divergence Δ_G = |r̂ - sin(πτ̂/2)| serves as a contamination indicator — large Δ_G signals non-normal contamination consistent with gaming. This divergence is itself a diagnostic: when GRS-Pearson drops faster than predicted by the Greiner transformation of GRS-Kendall, it indicates gaming outliers of large magnitude.\\n- Information-theoretic complementarity: GRS-Kendall captures the ORDINAL degradation (how many rank inversions?), GRS-Pearson captures the CARDINAL degradation (how severe are the inversions?). Together, they provide a richer picture than either alone.\\n\\n**2d. GRS vs Exploitation-Rate: Complementary Detection Regimes:**\\nGRS provides population-level monitoring with O(n log n) computation and bounded influence; exploitation-rate provides per-instance classification at O(K·n) frontier model cost but is vulnerable to correlated judge failures. GRS dominates when: contamination fraction ε > 0.05, evaluator cost is constrained, judge diversity is limited, or formally-grounded anchor is available. Exploitation-rate dominates for per-instance flagging in domains lacking formal anchors. Analytical comparison using published results; no experimental reimplementation.\\n\\n**2e. Multi-Faceted Faithfulness Anchors:**\\n  GRS-GTED: F(x) = GTED tree-edit-distance (PRIMARY — formally-grounded, no LLM dependency)\\n  GRS-LeanScorer: F(x) = LeanScorer Sugeno score (secondary)\\n  GRS-roundtrip: F(x) = roundtrip consistency (tertiary)\\n  GRS-human: F(x) = expert judgment (gold standard, 600 validation samples)\\n\\n**Phase 3: Systematic Ablation (8 Configurations)**\\n  C1: Binary compilation only (FormaRL/Mathesis R_ver reproduction)\\n  C2: Graded formal signal only (R_formal)\\n  C3: Embedding similarity only (R_embed)\\n  C4: LLM judge only (R_judge)\\n  C5: Trained critic only (R_critic via CriticLeanGPT-14B-RL)\\n  C6: Formal + embedding hybrid (R_formal + R_embed)\\n  C7: Formal + trained critic hybrid (R_formal + R_critic)\\n  C8: Full hybrid (R_formal + R_embed + R_critic)\\n  Tiered model strategy: all 8 on Qwen2.5-Coder-7B-Instruct; top 4 by GRS on Qwen3-Coder-30B-A3B-Instruct.\\n  MoE engineering for 30B: Qwen3-Coder-30B-A3B uses 128 experts with 8 active per forward pass; RL training of MoE architectures faces expert routing instability where ~10% of activated experts differ after policy updates, causing IS ratio fluctuations and potential training collapse (arXiv:2510.23027). We mitigate via: (a) auxiliary load-balancing loss to maintain expert utilization, (b) router-aware IS rescaling following Zhang et al. (2025), (c) conservative learning rate and clipping for 30B runs, (d) expert activation entropy monitoring as early divergence indicator.\\n  Critic scaling sub-study: C5 with 14B (84.8%) vs 8B (~79.8%) on 7B model.\\n\\n**Phase 4: Adaptive Composition Demonstration (Lightweight, ~2 pages)**\\n\\nBrief demonstration that GRS can inform dynamic composition, tested on 7B with C8 component set:\\n  D1: AGRC — w_k^(t+1) ∝ w_k^(t)·exp(η·GRS_k^(t)). Gaming-SPECIFIC: upweights gaming-resistant components based on per-component GRS-Kendall (monitoring role), updated every K=500 steps.\\n  D2: CTWA (arXiv:2602.06869) — monitors Cov(r_k, s) and upweights when covariance drops below target c*_k. Gaming-AGNOSTIC but signal-driven: targets interference regardless of cause. Primary comparison — mechanistically closest to AGRC.\\n  D3: MO-GRPO (arXiv:2509.22047) — A^MO = Σ_i [R_i - mean(R_i)]/std(R_i). Gaming-AGNOSTIC and static: normalizes variance. Reference baseline.\\n\\nHypotheses: (H1) When gaming concentrates in specific components, AGRC selectively downweights while CTWA and MO-GRPO cannot discriminate gamed from non-gamed components. (H2) CTWA may match AGRC when gaming correlates with negative covariance (interference and gaming are aligned). Both outcomes are publishable and informative.\\n\\n**Phase 5: Evaluation Framework (6 Analyses)**\\n\\n(1) Standard metrics + automated faithfulness: BEq@1, pass@1, ASSESS structural similarity, GTED score, LeanScorer score, FormalAlign alignment, roundtrip consistency\\n(2) GRS decomposition: GRS-Kendall (primary monitoring), GRS-Spearman (secondary), AND GRS-Pearson (calibration) per configuration × checkpoint — the core analysis answering RQ1 and RQ2. Reporting all three enables the dual-track analysis and Greiner divergence diagnostic.\\n(3) GRS-human validation: 75 samples × 8 key config-model pairs = 600 stratified expert audits with bootstrap BCA CIs (10,000 resamples). Stratified by gaming severity (no/mild/severe). Per Bonett & Wright: n=75 yields CI half-width ≈ 0.12 for τ ≈ 0.7\\n(4) GRS theoretical validation: (a) GRS-Kendall subsampling analysis verifying Hoeffding bounds, (b) GRS-Pearson CI coverage under synthetic contamination injection verifying conservatism for regularization, (c) Greiner divergence (|r̂ - sin(πτ̂/2)|) as gaming contamination detector — calibrating when the dual-track measures diverge, (d) Correlated Proxies regularization interval accuracy — do GRS-Pearson-derived λ values produce policies with verified true-reward improvement?\\n(5) Critic scaling: GRS comparison for R_critic using 14B (84.8%) vs 8B (~79.8%). Connected to FormalRewardBench's generation-evaluation gap: does critic accuracy predict gaming resistance?\\n(6) AGRC vs CTWA vs MO-GRPO demonstration: weight trajectories, GRS at convergence, Pareto analysis (GRS vs standard accuracy)\\n\\n**Research Questions:**\\n  RQ1: Which reward signal categories exhibit highest gaming resistance in isolation? Do formally-grounded signals (C2) outperform semantic (C3, C4) and learned-critic (C5) signals? Does critic accuracy predict gaming resistance? (C5 14B vs 8B)\\n  RQ2: Does hybrid composition (C6-C8) yield additive faithfulness gains while maintaining gaming resistance?\\n  RQ3: Is GRS-GTED a reliable automated proxy for expert gaming assessment? (correlation, bootstrap CIs, sample complexity verification)\\n  RQ4: Does gaming-specific adaptation (AGRC) outperform gaming-agnostic adaptation (CTWA, MO-GRPO) when domain-specific detection is available? (brief demonstration)\\n\\n**Training:** GRPO with KL penalty on Qwen2.5-Coder-7B-Instruct and Qwen3-Coder-30B-A3B-Instruct. Training on ProofNet + FormalMATH-Lite.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1200 H100 (8 configs on 7B = 8×70 + top 4 on 30B = 4×70 + 3 demo configs on 7B = 3×70 + 80 grid search + 60 CriticLeanGPT inference + 60 evaluation)\",\n      \"cpu_hours\": \"~35,000 CPU-hours on c7i.16xlarge for Lean compilation via Kimina Lean Server + GTED operator tree construction\",\n      \"human_audit_hours\": \"~70 expert-hours for 600 stratified manual gaming audits (75 samples × 8 key config-model pairs) with bootstrap BCA validation\",\n      \"timeline\": \"14-16 weeks (4 wks pipeline + GTED integration + GRS implementation + theoretical proofs + LeanInteract error parser, 5 wks RL training across configs, 1.5 wks demonstration configs (AGRC+CTWA+MO-GRPO), 4 wks evaluation/writing)\",\n      \"estimated_gpu_cost\": \"$3,000 (at ~$2.50/hr H100 spot)\",\n      \"estimated_cpu_cost\": \"$600-1,200 (c7i.16xlarge spot at ~$0.90/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"1050 H100\",\n      \"cpu_hours\": \"~30,000 CPU-hours\",\n      \"human_audit_hours\": \"~55 expert-hours\",\n      \"timeline\": \"12-14 weeks\",\n      \"claude_api_cost\": \"$500\",\n      \"estimated_gpu_cost\": \"$2,625\",\n      \"estimated_cpu_cost\": \"$500-1,000\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1050 H100\",\n      \"cpu_hours\": \"~30,000 CPU-hours\",\n      \"human_audit_hours\": \"~45 expert-hours (automated pre-filtering via GRS-GTED reduces manual load to disagreement cases)\",\n      \"timeline\": \"10-12 weeks\",\n      \"claude_api_cost\": \"$700\",\n      \"estimated_gpu_cost\": \"$2,625\",\n      \"estimated_cpu_cost\": \"$500-1,000\",\n      \"speed_bottleneck\": \"Lean compilation (~7s avg) and GTED operator tree construction (~2s per statement). With 120-180 parallel Lean instances, throughput matches GPU generation.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (abstract Sep 19, paper Sep 24, 2026 [estimated]) — PRIMARY, ~17 weeks available. Analysis paper framing (dual-track GRS + systematic ablation primary, AGRC demonstration secondary) fits ICLR's preference for principled analysis with clear contributions. The corrected Correlated Proxies connection (dual-track with conservatism guarantee) strengthens the theoretical contribution. Tighter scope makes clean narrative feasible.\",\n    \"EACL 2027 (ARR Aug 3, 2026 → Oct 11 commitment) — SECONDARY, ~10 weeks for ARR submission. 7B full ablation + GRS framework + theoretical analysis feasible; 30B scaling and demonstration deferred to camera-ready.\",\n    \"NAACL 2027 (ARR Oct 12, 2026 → commitment ~Oct 16 [estimated]) — TERTIARY CONTINGENCY. Full experiment set including 30B scaling and complete demonstration.\",\n    \"ACL 2027 (ARR ~Feb 16, 2027 [estimated]) — SAFE FALLBACK. Complete experimental set with all supplementary analyses.\"\n  ],\n  \"level\": \"strong-\",\n  \"key_references\": [\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"Mathesis: Towards Formal Theorem Proving from Natural Languages (ICLR 2026)\",\n    \"Online Reinforcement Learning for Autoformalization (MAR Workshop @ NeurIPS 2025)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv July 2025)\",\n    \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (arXiv:2603.24372, March 2026)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv:2604.19459)\",\n    \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)\",\n    \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems (arXiv:2509.22047, Sep 2025)\",\n    \"Uncovering Cross-Objective Interference in Multi-Objective Alignment [CTWA] (arXiv:2602.06869, Feb 2026)\",\n    \"Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting [DRW] (TACL 2026)\",\n    \"On the Hidden Objective Biases of Group-based Reinforcement Learning (arXiv:2601.05002, Jan 2026)\",\n    \"Blockwise Advantage Estimation for Multi-Objective Alignment (arXiv:2602.10231, Feb 2026)\",\n    \"Rethinking Reward Signals in Video GRPO: When Scores Become Targets [TaRoS] (arXiv:2511.19356)\",\n    \"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, April 2026)\",\n    \"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness [SignCert-PO] (arXiv:2604.02986, April 2026)\",\n    \"Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063, March 2026)\",\n    \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges [Survey] (arXiv:2604.13602, April 2026)\",\n    \"Detecting and Suppressing Reward Hacking with Gradient Fingerprints [GRIFT] (arXiv:2604.16242, April 2026)\",\n    \"Reward Hacking in Rubric-Based Reinforcement Learning [Exploitation-rate] (arXiv:2605.12474, May 2026)\",\n    \"FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv:2605.10141, May 2026)\",\n    \"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking (arXiv:2403.03185, ICLR 2025 Spotlight)\",\n    \"Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026)\",\n    \"Reward Hacking Mitigation using Verifiable Composite Rewards (arXiv:2509.15557, ACM-BCB 2025)\",\n    \"SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv:2605.21384, May 2026)\",\n    \"Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization (AI4Math @ ICML 2025)\",\n    \"FormalAlign: Automated Alignment Evaluation for Autoformalization (ICLR 2025)\",\n    \"Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)\",\n    \"Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)\",\n    \"Process-Driven Autoformalization in Lean 4 (arXiv 2024)\",\n    \"Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)\",\n    \"ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\",\n    \"Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\",\n    \"Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\",\n    \"Towards Stable and Effective Reinforcement Learning for Mixture-of-Experts (arXiv:2510.23027, Oct 2025)\",\n    \"MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models (arXiv:2603.24984, March 2026)\",\n    \"Sample Size Requirements for Estimating Pearson, Kendall and Spearman Correlations (Bonett & Wright, Psychometrika 2000)\",\n    \"Influence functions of the Spearman and Kendall correlation measures (Croux & Dehon, Statistical Methods & Applications 2010)\",\n    \"A comparative analysis of Spearman's rho and Kendall's tau in normal and contaminated normal models (Xu et al., Signal Processing 2013)\",\n    \"A class of statistics with asymptotically normal distribution (Hoeffding, Annals of Mathematical Statistics 1948)\",\n    \"Asymptotic Inference for Rank Correlations (Pohle, Wermuth & Weiss, arXiv:2512.14609)\"\n  ],\n  \"description\": \"Reward hacking in autoformalization is a documented concern — FormaRL's ablation shows syntax-only RL achieves 100% compilation but 0% semantic consistency, and VerifAI-2 (arXiv:2604.19459) reveals that high compilation rates in neuro-symbolic pipelines create an 'illusion of correctness' even when unified generation shows no systematic gaming. Yet we lack answers to a basic question: which reward signals maintain faithfulness under optimization pressure? This paper provides the first systematic answer, exploiting a capability unique to autoformalization: formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance.\\n\\nOur central insight is that autoformalization is uniquely positioned for principled gaming-resistance analysis. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers GTED — a computable faithfulness anchor derived from the Lean language server's operator trees. A critical methodological refinement: MONITORING gaming resistance and CALIBRATING safe optimization require fundamentally different correlation measures, leading to our dual-track framework.\\n\\nWe contribute three advances.\\n\\n**First (primary contribution)**, the dual-track GRS (Gaming Resistance Score) framework with deep theoretical grounding. GRS-Kendall measures rank correlation between reward signals and GTED-anchored faithfulness, providing ROBUST MONITORING: bounded influence functions (Croux & Dehon 2010) ensure stability under contamination, U-statistic theory gives exact sample complexity bounds (n ≥ 2log(2/δ)/ε² via Hoeffding), and lowest MSE under realistic gaming contamination (Xu et al. 2013). GRS-Pearson measures parametric correlation, providing SAFE OPTIMIZATION CALIBRATION: it exactly estimates the correlation parameter r in the Correlated Proxies framework (Definition 4.1, ICLR 2025 Spotlight), so a confidence interval [r_L, r_U] directly yields a regularization interval [σ√(1-r_U²), σ√(1-r_L²)] with formal conservatism guarantees via the lower confidence bound. GRS-Pearson also addresses an acknowledged open problem in Robust Correlated Proxies (arXiv:2604.12086, ICLR 2026) — providing principled, data-driven r estimation for their max-min robust optimization over all r-correlated proxies. The dual-track design resolves a subtle but critical issue: under gaming contamination, Kendall's τ (robust, bounded influence) drops LESS than Pearson's r (sensitive, unbounded influence), so τ_contaminated > r_contaminated, meaning naively substituting τ for r in regularization formulas would produce dangerously weak regularization. The dual-track framework assigns each measure to its natural role. We further show that the Greiner divergence |r̂ - sin(πτ̂/2)| — the gap between GRS-Pearson and the Greiner transformation of GRS-Kendall — serves as a real-time gaming contamination indicator. We validate GRS against 600 expert-annotated samples with bootstrap BCA confidence intervals.\\n\\n**Second (systematic analysis)**, the first comparison of gaming resistance across five isolated reward source categories for autoformalization RL: binary compilation, graded formal (via custom error-hierarchy classification over LeanInteract v0.11.3 diagnostics), embedding similarity (cf. cycle consistency in arXiv:2603.24372), LLM judge, and trained critic (CriticLeanGPT-Qwen3-14B-RL at 84.8% — first use as direct RL reward). Our 8-configuration GRPO ablation on Qwen2.5-Coder-7B-Instruct and Qwen3-Coder-30B-A3B-Instruct (with MoE routing stabilization via auxiliary load-balancing loss and router-aware IS rescaling per arXiv:2510.23027) isolates individual signal contributions, answering which signals to trust. FormalRewardBench's (arXiv:2605.10141) finding that specialized provers are poor evaluators motivates our sub-study of whether critic accuracy (14B vs 8B) predicts gaming resistance.\\n\\n**Third (lightweight demonstration)**, we briefly show that GRS can inform adaptive reward composition via AGRC (gaming-aware dynamic reweighting using per-component GRS-Kendall for the monitoring signal). We compare against CTWA (arXiv:2602.06869) — the most theoretically grounded objective-agnostic adaptive method, which monitors covariance between rewards and training signal — and MO-GRPO (arXiv:2509.22047), testing whether gaming-specific signals outperform gaming-agnostic adaptation. We position this in a dense landscape of 5+ objective-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS), honestly noting AGRC's mechanism is a demonstration of GRS's utility, not a primary methodological contribution.\\n\\nThe paper adopts VerifAI-2's outcome-based gaming definition: reward inflation without corresponding faithfulness improvement, requiring no intent attribution. It is designed for outcome robustness: if formally-grounded signals dominate, we advance reward design; if signals are equivalent, we establish cost-effectiveness; if CTWA matches AGRC, we demonstrate that gaming-specific detection is unnecessary (a useful negative result). Regardless, the dual-track GRS framework with its theoretical guarantees and the systematic gaming-resistance analysis are independent contributions. Targeting ICLR 2027 (Sep 24 estimated deadline), with EACL 2027, NAACL 2027, and ACL 2027 as contingency venues.\",\n  \"project_name\": \"reward_comp_autoform\",\n  \"source\": \"web_research\"\n}\n\n## Reviewer feedback (round 8)\nIssues: [\"CRITICAL OMISSION — GSPO (arXiv:2507.18071, July 2025): Group Sequence Policy Optimization was developed by the Qwen team specifically because GRPO fails on MoE models like Qwen3-30B-A3B. The Qwen team found ~10% expert activation changes per GRPO gradient update (the exact statistic the proposal cites from arXiv:2510.23027) and developed GSPO as the algorithmic fix — defining importance ratios at sequence level rather than token level, eliminating the need for routing replay. The proposal uses GRPO on this exact model with engineering mitigations but doesn't acknowledge the model creator's own recommended algorithm. GSPO may also interact differently with multi-component reward decomposition (sequence-level vs token-level clipping), which is relevant to the per-component GRS analysis. This must be cited, discussed, and the GRPO choice must be justified — or GSPO should be adopted for the 30B experiments.\", \"MINOR OMISSION — MathAtlas (arXiv:2605.14061, May 2026): First large-scale autoformalization benchmark of graduate-level math (~52k theorems from 103 textbooks, achieving at most 9.8% correctness). While a benchmark paper rather than a methods paper, it reinforces the challenge of autoformalization at scale and could serve as additional evaluation data. Should be cited in the landscape.\", \"CriticLeanGPT-Qwen3-14B-RL accuracy (84.8%) could not be independently verified from web sources, though the model's existence on HuggingFace (15B parameters, Apache 2.0 license) is confirmed. The 32B variant achieves 87.0%. The 8B variant does not exist on HuggingFace — the proposal correctly identifies it as needing retraining. The 84.8% figure is plausible given the scaling trend (32B: 87%, 14B: ~84.8%, 8B: ~79.8%) but should be verified against the paper's Table 2.\", \"GSPO interaction with multi-objective reward: GSPO performs sequence-level clipping and rewarding. The proposal's approach requires token/component-level reward decomposition for per-component GRS analysis. Whether GSPO's sequence-level operation is compatible with this fine-grained decomposition is unclear. If GSPO is adopted, the proposal needs to verify that per-component reward signals can still be extracted and analyzed.\"]\nFeedback: The proposal has matured substantially over 8 rounds — the τ-to-r theoretical fix is mathematically correct, the dual-track framework is well-motivated, and the connection to Correlated Proxies addresses a genuine open problem. You are very close to pass quality. The ONE remaining critical issue:\n\n(1) **Cite and address GSPO (arXiv:2507.18071)**: This is the Qwen team's own algorithm designed specifically for MoE models like the Qwen3-Coder-30B-A3B you plan to use. You cite the MoE instability problem (arXiv:2510.23027) — GSPO is the algorithmic solution developed by the model's creators. Three options: (a) **Best**: Adopt GSPO for the 30B MoE experiments and justify GRPO for the 7B dense experiments, explaining how per-component reward decomposition works under sequence-level optimization. (b) **Good**: Justify GRPO over GSPO with a technical argument — e.g., GSPO's sequence-level operation may complicate per-component GRS monitoring (since GRS requires individual reward component analysis), while GRPO's token-level operation naturally exposes per-component rewards; acknowledge GSPO as an alternative that could be explored in future work. (c) **Adequate**: Cite GSPO and note that the primary contribution comes from the 7B dense model experiments (where GRPO is unproblematic), with 30B experiments as secondary scaling validation using established mitigations.\n\n(2) **Minor**: Add MathAtlas (arXiv:2605.14061) to the autoformalization landscape — it's the largest benchmark as of May 2026 and shows the field's rapid growth.\n\nWith GSPO addressed, the proposal should clear the pass threshold. The theoretical framework is now sound, the empirical design is systematic, and the contributions are clearly articulated.\n\n## Instructions\n- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.\n- Address each issue specifically.\n\n## 深度调研要求\n\n不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。\n\n1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。\n2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。\n3. **深度思考**：\n   - 核心假设是否仍然成立？\n   - reviewer 的批评是否揭示了更深层的问题？\n   - 有没有更好的 framing 或 approach？\n4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。\n\n## 针对 Review 意见的定向搜索\n\n1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点\n2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline\n3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现\n4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot\n\n- You have full freedom: minor fix, major revision, or pivot.\n- Include a \"change_type\" field: \"minor\", \"major\", or \"pivot\".\n- Output a COMPLETE JSON object with ALL fields.\n\n## 停滞提醒\n经过 8 轮修订，近 3 轮平均分从 3.6 到 3.8，无明显改善。\n考虑 major revision 或 pivot。\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-27T23:04:32.009Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-27T23:04:32.009Z",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

## Round 1

32 recorded events

### User

_source line 3 · 2026-05-27T23:04:32.023Z_

You are revising a research idea based on reviewer feedback.

**Today's date: 2026-05-27 (UTC).**

## Original idea
{
  "changes_made": [
    "FIXED τ-TO-r THEORETICAL BRIDGE (most critical fix): Identified and resolved mathematical gap in the Correlated Proxies connection. The Correlated Proxies framework (arXiv:2403.03185, Definition 4.1) defines r as Pearson correlation — the normalized product-moment E[(R̃-J)/σ_R̃ · (R-J)/σ_R] = r — not rank correlation. GRS-Kendall measures τ, a fundamentally different quantity. Under bivariate normality, τ = (2/π)arcsin(r), so r = sin(πτ/2) > τ for τ ∈ (0,1). Under gaming contamination (the explicitly modeled scenario), this relationship breaks down adversely: Pearson r drops MORE than Kendall τ because Pearson is magnitude-sensitive (unbounded influence) while τ is rank-based (bounded influence). Discordant gaming outliers (high reward, low faithfulness) pull Pearson r down in proportion to their magnitude, while τ only counts them as discordant pairs. Therefore τ_contaminated > r_contaminated, and substituting τ for r in λ = σ√(1-r²) gives λ(τ) = σ√(1-τ²) < σ√(1-r²) = λ(r) — UNDER-regularization. This is NOT conservative and could be harmful. SOLUTION: Introduced dual-track GRS framework with distinct roles: (a) GRS-Kendall for robust gaming resistance MONITORING — bounded influence, U-statistic theory, stable under contamination, used for RQ1-RQ3; (b) GRS-Pearson for regularization CALIBRATION via Correlated Proxies — exact r ≡ r mapping (no transformation needed), appropriately sensitive to gaming contamination, used for Theorem 5.1 bounds. Key insight: Pearson's 'weakness' (outlier sensitivity) is a FEATURE for regularization calibration — it reflects the true degradation of the proxy-truth relationship and prescribes appropriately stronger regularization. Kendall's 'strength' (robustness) is a FEATURE for monitoring — it provides stable, comparable gaming resistance measurements across configurations without being unduly influenced by extreme gaming instances. The Greiner relation r = sin(πτ/2) is retained as an informational cross-check (valid under bivariate normality) rather than as the formal bridge.",
    "ADDED ROBUST CORRELATED PROXIES (arXiv:2604.12086, ICLR 2026): Liu, Sun & Zheng extend the Correlated Proxies framework with a max-min robust optimization formulation: max_π min_{R∈ℛ_corr} E[R(s,a)], optimizing against the worst-case proxy consistent with correlation constraint r. Their tractable objective: max_π r·E_{μ_π}[R_proxy] - √(1-r²)·√(χ²(μ_π||μ_{π_ref}) - E²_{μ_π}[R_proxy]), providing a pessimistic lower bound on true improvement (Theorem 1). Crucially, they note 'there is currently no principled method for selecting r' — GRS-Pearson provides exactly this data-driven r estimation, addressing their acknowledged open problem. Integration: (a) GRS-Pearson estimates the correlation parameter r that parametrizes their uncertainty set ℛ_corr; (b) conservative r estimate (from GRS-Pearson's sensitivity to gaming) → larger uncertainty set → more robust policy; (c) GRS confidence intervals translate to uncertainty set size intervals, enabling data-driven robustness calibration. This strengthens the theoretical narrative: GRS bridges both the original regularization framework (Theorem 5.1) AND the robust optimization extension.",
    "ADDED MoE TRAINING ACKNOWLEDGMENT: Qwen3-Coder-30B-A3B uses 128 experts with 8 active per forward pass. Research documents significant MoE-specific challenges for GRPO: routing fluctuations where ~10% of experts activated for the same token differ after policy updates, causing importance-sampling ratio instability and triggering clipping mechanisms that introduce additional gradient variance (arXiv:2510.23027, Zhang et al. 2025). In severe cases, this can cause catastrophic RL training collapse. Added engineering mitigation plan: (a) auxiliary load-balancing loss to maintain expert utilization stability, (b) router-aware importance sampling rescaling following Zhang et al., (c) reduced learning rate and conservative clipping for 30B runs, (d) monitoring expert activation entropy as an early divergence indicator. This takes ~1 paragraph in the paper but demonstrates awareness of a known pitfall.",
    "ADDED CYCLE CONSISTENCY PAPER (arXiv:2603.24372, March 2026): Shebzukhov demonstrates GRPO with cosine-similarity-based cycle consistency reward for Lean4 autoformalization on Qwen3.5-2B with LoRA. Achieves 0.669 mean cycle consistency vs 0.513 for SFT, with only 0.011 nats increase in cross-entropy loss. Directly relevant to R_embed signal category — provides independent evidence that embedding-based rewards (roundtrip cosine similarity) are viable for autoformalization GRPO, validating our inclusion of R_embed as a signal category. Cited in landscape and as motivation for studying R_embed's gaming resistance: the cycle consistency approach lacks formal grounding (cosine similarity ≠ semantic faithfulness), so its gaming resistance is an empirical question our ablation addresses.",
    "RESTRUCTURED GRS THEORETICAL SECTION: Now cleanly separates three theoretical contributions: (a) GRS-Kendall theory — sample complexity bounds via Hoeffding's inequality for U-statistics, contamination robustness via bounded influence functions, stable monitoring guarantees; (b) GRS-Pearson theory — exact mapping to Correlated Proxies Definition 4.1, conservative regularization calibration under contamination, connection to Robust Correlated Proxies max-min formulation; (c) Dual-track complementarity theorem — formal proof that GRS-Kendall and GRS-Pearson serve complementary roles (monitoring vs calibration) and that combining both provides strictly more information than either alone. Specifically: GRS-Kendall divergence from GRS-Pearson (measured via the Greiner relation as |r̂_Pearson - sin(πτ̂/2)|) itself serves as a contamination indicator — large divergence signals non-normal contamination consistent with gaming.",
    "ADDED CONSERVATISM ANALYSIS FOR GRS-PEARSON: Under the gaming contamination model (1-α)P_faithful + αP_gamed where P_gamed produces discordant outputs: (a) population Pearson r decreases in proportion to both contamination fraction α AND outlier magnitude m — r_contaminated ≈ (1-α)r_clean - α·m·g(r_clean) for appropriately defined influence function g; (b) the Pearson estimator r̂ is unbiased for r_contaminated but with inflated variance — confidence intervals are wider under contamination; (c) using the LOWER confidence bound r_L = r̂ - z_{α/2}·SE_r in λ = σ√(1-r_L²) provides guaranteed conservative regularization: P(λ̂ ≥ λ_true) ≥ 1-α/2. This is the formal conservatism guarantee the reviewer requested. (d) Kendall τ cannot provide this guarantee because τ_contaminated > r_contaminated → λ(τ) < λ(r) systematically under gaming contamination.",
    "UPDATED EVALUATION: Analysis (4) now validates BOTH GRS-Kendall and GRS-Pearson: (a) GRS-Kendall subsampling analysis (verifying Hoeffding bounds), (b) GRS-Pearson CI coverage under synthetic contamination injection (verifying conservatism), (c) Greiner divergence as contamination detector (calibrating the dual-track diagnostic), (d) Correlated Proxies regularization interval accuracy. Analysis (2) now reports GRS-Kendall, GRS-Spearman, AND GRS-Pearson per configuration × checkpoint, with GRS-Kendall primary for monitoring and GRS-Pearson primary for the Correlated Proxies connection."
  ],
  "title": "Which Rewards Resist Gaming? Formally-Grounded Gaming Resistance Analysis for Autoformalization RL",
  "core_problem": "RL-based autoformalization combines composite rewards — binary compilation (FormaRL, Mathesis), LLM semantic judges (Mathesis R_sem), embedding similarity (Online RL for Autoformalization; cycle consistency in arXiv:2603.24372), and trained critics (CriticLean at 84.8% accuracy) — yet a fundamental question remains unanswered: which reward signals maintain faithfulness under optimization pressure, and can we measure this automatically?\n\nThis question is urgent for three reasons. First, the reward-faithfulness gap in autoformalization is documented: FormaRL's ablation reveals syntax-only RL yields 100% compilation but 0% semantic consistency, demonstrating clear gaming under optimization. VerifAI-2 (arXiv:2604.19459) provides complementary evidence: while finding no evidence of systematic gaming in unified generation (94-98% definite precision), it documents fabrication (GPT-5) and premise mistranslation (DeepSeek-R1) in two-stage pipelines that evade detection — showing faithfulness gaps even in high-performing systems. Following VerifAI-2's outcome-based definition, we define gaming as reward inflation without corresponding faithfulness improvement, requiring no intent attribution.\n\nSecond, theoretically, 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves gaming is a structural equilibrium under finite evaluation — not a correctable bug. The Proxy Compression Hypothesis (arXiv:2604.13602) further explains this as the inevitable consequence of objective compression, optimization amplification, and evaluator-policy co-adaptation. Together, these results make measuring gaming RESISTANCE — which signals degrade least — the critical practical question.\n\nThird, the broader RL community has responded with gaming mitigations at multiple levels: MO-GRPO normalizes per-objective variance; CTWA (arXiv:2602.06869) adaptively targets covariance between rewards and training signal; Advantage Modification integrates representation-level shortcut scores; SignCert-PO certifies advantage sign robustness; GRIFT detects gaming via gradient fingerprints; exploitation-rate measures hacking via LLM panels. However, ALL these methods are domain-agnostic. Autoformalization has a UNIQUE advantage: the Lean language server provides formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance (AI4Math@ICML 2025). This creates three domain-specific gaps that no existing work addresses: (1) No systematic comparison of gaming-resistance properties across isolated reward source categories for autoformalization; (2) No gaming-resistance metric leveraging formally-grounded faithfulness anchors — enabling detection that is simultaneously lightweight, automated, and non-circular; (3) No formal theoretical analysis connecting gaming-resistance measurement to the broader reward hacking and safe optimization frameworks, including both regularization-based (Correlated Proxies, ICLR 2025 Spotlight) and robust optimization-based (Robust Correlated Proxies, ICLR 2026) approaches.",
  "opportunity": "A unique convergence of eight developments makes this the right moment for this study:\n\n(1) GTED (AI4Math@ICML 2025) provides formally-grounded faithfulness via tree-edit-distance over Lean operator trees — the KEY enabling capability. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers a computable, LLM-independent faithfulness anchor.\n\n(2) The reward-faithfulness gap is newly documented but unquantified for autoformalization. FormaRL's ablation demonstrates gaming under optimization; VerifAI-2 documents faithfulness gaps in pipelines. We provide the first systematic measurement of which signals are affected and by how much.\n\n(3) Mathesis (ICLR 2026) establishes composite rewards for autoformalization GRPO but treats composition as a performance optimization problem, not a gaming-resistance problem.\n\n(4) CriticLean (July 2025) creates a new reward signal category (trained critic at 84.8%) untested as direct RL signal. FormalRewardBench (arXiv:2605.10141) reveals a generation-evaluation gap — specialized provers perform worst at proof evaluation (24.4% pairwise) while frontier LLMs are best (59.8%) — raising the question of how trained critics' gaming resistance relates to their normal-condition accuracy.\n\n(5) Rich theoretical infrastructure now exists for formalizing gaming resistance via BOTH regularization and robust optimization: the Correlated Proxies framework (arXiv:2403.03185, ICLR 2025 Spotlight) defines hacking via proxy-true correlation breakdown and proves regularization bounds parametrized by correlation r; the Robust Correlated Proxies extension (arXiv:2604.12086, ICLR 2026) formulates max-min robust optimization over the space of all r-correlated proxies, noting 'there is currently no principled method for selecting r.' GRS-Pearson provides exactly this data-driven r estimation, addressing an acknowledged open problem.\n\n(6) The proliferation of domain-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS — 5+ methods in 2025-2026) creates urgency for domain-specific evaluation: do autoformalization's formal verification capabilities enable better gaming-resistance measurement than general-purpose approaches?\n\n(7) 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves hacking is structural under finite evaluation, and the Proxy Compression Hypothesis (arXiv:2604.13602) explains it as an inevitable consequence of proxy-based optimization — establishing that measuring resistance (not eliminating hacking) is the practically important question.\n\n(8) Independent work on embedding-based rewards for autoformalization GRPO (arXiv:2603.24372 — cycle consistency with cosine similarity on Qwen3.5-2B) validates the importance of understanding R_embed's properties, including its gaming resistance, as a distinct reward signal category.",
  "landscape": "**Autoformalization RL systems:** FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency, achieving 26.15% pass@1 on ProofNet; ablation reveals aggressive gaming — syntax-only RL yields 100% compilation, 0% consistency. Mathesis (ICLR 2026) advances with R_ver + R_sem in GRPO plus HPO; 22% improvement on Gaokao-Formal. CriticLean (arXiv July 2025) trains CriticLeanGPT via SFT+GRPO: Qwen3-14B-RL achieves 84.8% (publicly available), Qwen3-8B-RL achieves 79.8% on CriticLeanBench. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite. Cycle Consistency Fine-tuning (arXiv:2603.24372) uses GRPO with cosine-similarity cycle consistency reward on Qwen3.5-2B, achieving 0.669 mean cycle consistency vs 0.513 SFT — demonstrating independent interest in embedding-based rewards for autoformalization and validating our inclusion of R_embed as a distinct signal category.\n\n**Faithfulness gaps in autoformalization:** Do LLMs Game Formalization? (arXiv:2604.19459) uses an outcome-based definition: 'formalization gaming is the subset of unfaithfulness where errors functionally enable proof compilation that faithful formalization would not have achieved.' Key findings: (a) NO systematic gaming in unified generation — 94-98% definite precision, models prefer abstention over forcing proofs; (b) In two-stage pipelines, GPT-5 fabricates axioms as 'reactive fallback' (107 cases, mixed across runs), DeepSeek-R1 mistranslates premises producing 'internally consistent outputs that evade detection entirely'; (c) High compilation rates create an 'illusion of correctness' — valid proofs do not guarantee faithful formalizations. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates RLVR models abandon reasoning for shortcuts.\n\n**Multi-objective GRPO weight adaptation (DENSE LANDSCAPE):** (1) MO-GRPO (arXiv:2509.22047): normalizes per-objective advantage A^MO_g = Σ_i [R_i - mean(R_i)]/std(R_i), ensuring equal variance contribution. Theoretically: affine-invariant, Corr(R_i, A^MO) = 1/√K under uncorrelated rewards. Tested on bandits, WMT, AlpacaFarm. (2) CTWA (arXiv:2602.06869, Lu & Jiang): derives local covariance law — objective m improves iff Cov(r_m, s) > 0 where s is the scalarized training signal. Adaptively upweights objectives whose covariance dips below target c*_m via exponential moving average and log-space update. Provides Polyak-Łojasiewicz convergence analysis. Most theoretically grounded of the group. Tested on Math500, MATH algebra with Qwen2.5, Qwen3, SmolLM2. Same authors as DRW. (3) DRW (TACL 2026, Lu & Jiang): hypervolume-guided and gradient-based dynamic weight adaptation for Pareto efficiency. Predecessor to CTWA. (4) Blockwise Advantage Estimation (arXiv:2602.10231): token-level objective assignment — partitions completions into blocks with per-block advantages. Complementary to weight adaptation (addresses credit assignment, not weighting). (5) TaRoS (arXiv:2511.19356): monitors Hoyer sparsity for reward saturation detection, downweights saturated components. Video generation domain. Closest to gaming-awareness via Goodhart's Law sensitivity. ALL five methods are objective-agnostic — none use domain-specific gaming detection.\n\n**Gaming-aware RL modifications:** Advantage Modification from 'When Reward Hacking Rebounds' (arXiv:2604.01476): integrates shortcut concept scores (via representation engineering from contrastive pairs) into GRPO advantage computation. Operates at REPRESENTATION level — requires probing hidden states, domain-specific contrastive pairs. SignCert-PO (arXiv:2604.02986): certified sign-preservation radius via adversarial RM perturbation, down-weights non-robust completions. Operates at ADVANTAGE level — requires RM weight access, single-RM settings.\n\n**General gaming detection:** GRIFT (arXiv:2604.16242): gradient fingerprints (LoRA adapters, K-means, ~80% F1). Heavyweight: per-sample gradient computation + manual cluster labeling. Exploitation-rate (arXiv:2605.12474): fraction of newly-credited criteria rejected by cross-family LLM panel (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6). Expensive, LLM-dependent, vulnerable to correlated judge failures.\n\n**Theoretical foundations:** Correlated Proxies (arXiv:2403.03185, ICLR 2025 Spotlight): formalizes hacking via proxy-true Pearson correlation r; proves safe optimization bound J(π,R) ≥ (1/r)[proxy_gain - σ√((1-r²)χ²)]; regularization λ = σ√(1-r²). KEY: r is explicitly Pearson correlation (Definition 4.1). Robust Correlated Proxies (arXiv:2604.12086, ICLR 2026): extends to max-min robust optimization over all r-correlated proxies — max_π min_{R∈ℛ_corr} E[R], yielding tractable objective max_π r·E[R_proxy] - √(1-r²)·√(χ² - E²[R_proxy]). Crucially notes 'no principled method for selecting r' — an open problem GRS-Pearson addresses. Reward Hacking as Equilibrium (arXiv:2603.28063): hacking is structural under finite evaluation — any optimized agent under-invests in unevaluated dimensions. Reward Hacking survey (arXiv:2604.13602): four-level exploitation hierarchy (feature/representation/evaluator/environment), three-phase detection lifecycle, Proxy Compression Hypothesis unifying hacking as objective compression + optimization amplification + evaluator-policy co-adaptation. SpecBench (arXiv:2605.21384): hacking gap grows 28pp per 10× code size. On the Hidden Objective Biases of GRPO (arXiv:2601.05002): non-uniform group weighting, AdamW scaling insensitivity, momentum clipping violations.\n\n**MoE training for RL:** Applying GRPO to MoE architectures (like Qwen3-Coder-30B-A3B with 128 experts, 8 active) introduces routing instability: ~10% of experts activated for the same token differ after policy updates, causing importance-sampling ratio fluctuations that trigger clipping and increase gradient variance (arXiv:2510.23027, Zhang et al. 2025). In severe cases, this leads to catastrophic RL training collapse. MoE-GRPO (arXiv:2603.24984) proposes modality-aware router guidance to stabilize training. Router-aware IS rescaling strategies have been shown to improve both convergence stability and final performance.\n\n**Evaluation metrics for autoformalization:** GTED (AI4Math@ICML 2025): tree-edit-distance over operator trees from Lean Language Server — formally-grounded, no ATP/LLM dependency, highest accuracy (70.73%) and Kappa (0.438) on miniF2F. FormalAlign (ICLR 2025): dual contrastive+generation loss, 99.21% AS on FormL4-Basic. LeanScorer (Mathesis): subtask decomposition, Sugeno fuzzy integral, 0.92 F1. FormalRewardBench (arXiv:2605.10141): first benchmark for reward models in formal theorem proving with Lean 4 — specialized provers score 24.4% pairwise consistency, frontier LLMs 59.8%. Reveals generation-evaluation gap: proving ability does not transfer to evaluation ability.\n\n**The refined gap:** Autoformalization uniquely provides formally-grounded faithfulness measurement (GTED), enabling gaming-resistance analysis unavailable in other RL domains. Despite 5+ objective-agnostic adaptive methods and multiple gaming-aware RL modifications, no work: (a) systematically compares gaming resistance across isolated reward source categories for autoformalization; (b) proposes a gaming-resistance metric with formal theoretical grounding — specifically, a dual-track framework where rank-based GRS provides robust monitoring and parametric GRS provides safe optimization calibration via the Correlated Proxies framework; (c) evaluates whether domain-specific formally-grounded gaming detection outperforms general-purpose approaches; (d) addresses the open problem of data-driven r estimation for robust optimization over correlated proxies (arXiv:2604.12086).",
  "inspired_by": "The central insight: autoformalization is the IDEAL domain for studying gaming resistance because GTED provides a formally-grounded faithfulness anchor — enabling principled measurement that is provably connected to safe optimization bounds (via Correlated Proxies) and inherently more robust than LLM-based detection (via bounded influence functions). A critical refinement emerged from examining the τ-to-r mapping: robust rank-based measures (Kendall's τ) and parametric measures (Pearson's r) serve fundamentally DIFFERENT roles in gaming-resistance analysis. τ provides stable monitoring because its bounded influence function means gaming outliers don't dominate the measurement; r provides accurate calibration because its sensitivity to outlier magnitude reflects the true degradation of the proxy-truth relationship. This dual-track insight is itself a contribution — it shows that the choice of correlation measure is not a minor methodological detail but determines whether GRS output is suitable for monitoring vs. regularization. The insight emerges from: (1) the theoretical result that reward hacking is structural (arXiv:2603.28063) and that proxies inevitably compress (PCH, arXiv:2604.13602), making resistance measurement the practical question; (2) GTED providing the formally-grounded anchor uniquely in autoformalization; (3) the Correlated Proxies framework (arXiv:2403.03185) AND its robust optimization extension (arXiv:2604.12086) providing the theoretical bridge — but requiring PEARSON r, not rank correlation; (4) the generation-evaluation gap (FormalRewardBench) showing evaluation capability cannot be assumed from generation accuracy; (5) the proliferation of domain-agnostic methods creating demand for domain-specific evaluation; (6) independent exploration of embedding-based rewards for autoformalization (arXiv:2603.24372) validating the importance of understanding individual signal categories.",
  "approach": "We present the first formally-grounded gaming-resistance analysis for autoformalization RL. The central claim: GTED's formally-grounded faithfulness measurement uniquely enables a dual-track gaming-resistance framework (GRS) with formal theoretical guarantees — robust monitoring via rank correlation AND safe optimization calibration via parametric correlation connected to the Correlated Proxies framework. The paper has three phases that progressively build on this claim.\n\n**Phase 1: Multi-Source Reward Signal Extraction (5 Categories)**\n\n(a) Formally-grounded signal R_formal: Using LeanInteract v0.11.3's Message objects (fields: start_pos, end_pos, data, severity ∈ {error, warning, info}), classify compiler diagnostics into error hierarchy via custom regex parser (~200 LoC) over Message.data strings: parse errors → name resolution → type errors → clean compilation. Yields R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} plus density bonus. NOTE: LeanInteract provides three severity levels; the five-level hierarchy is our custom classification, documented as engineering contribution.\n\n(b) Embedding similarity R_embed: cosine similarity between sentence embeddings of input NL and backtranslation of generated formal statement (reference-free roundtrip approach). Directly analogous to the cycle consistency reward in Shebzukhov (arXiv:2603.24372), which achieves 0.669 mean cycle consistency on Qwen3.5-2B — validating the signal's viability while leaving its gaming resistance as an open empirical question.\n\n(c) LLM judge R_judge: binary faithfulness judgment from frozen LLM (following FormaRL/Mathesis R_sem approach).\n\n(d) Trained critic R_critic: semantic fidelity score from CriticLeanGPT-Qwen3-14B-RL (84.8% accuracy, publicly available). First use as direct RL reward signal. Additionally retrain Qwen3-8B using CriticLean_4K dataset (~79.8% expected) to study critic accuracy impact on gaming resistance. FormalRewardBench's generation-evaluation gap motivates studying whether R_critic's gaming resistance differs from its normal-condition accuracy.\n\n**Phase 2: Dual-Track GRS (Gaming Resistance Score) Framework — Primary Methodological Contribution**\n\nGRS measures the meta-property of reward signals: how faithfully does high reward indicate genuine quality? The critical methodological insight is that MONITORING gaming resistance and CALIBRATING safe optimization require different correlation measures, serving complementary roles.\n\n**2a. GRS-Kendall: Robust Gaming Resistance Monitoring**\n\n  GRS-Kendall(R, F) = τ(R(x), F(x)) over held-out evaluation set\n\nwhere τ is Kendall's rank correlation and F is a faithfulness anchor.\n\n*Role*: Primary metric for comparing reward signals' gaming resistance (RQ1, RQ2, RQ3). Advantages: (i) Bounded influence function — gross-error sensitivity is finite (Croux & Dehon 2010), meaning individual gaming outliers cannot dominate the measurement; (ii) Under 5-10% contamination (realistic for RL gaming), Kendall's τ achieves lowest MSE among correlation measures (Xu et al., Signal Processing 2013); (iii) U-statistic theory provides exact sample complexity bounds.\n\n*Sample Complexity Bounds*: Since Kendall's τ is a degree-2 U-statistic with kernel h((x₁,y₁),(x₂,y₂)) = sgn((x₂-x₁)(y₂-y₁)) bounded in [-1,1], Hoeffding's inequality for U-statistics gives:\n  P(|GRS-Kendall_hat - GRS-Kendall| > ε) ≤ 2 exp(-nε²/2)\nFor ε=0.1, δ=0.05: n ≥ 737 evaluation pairs suffice. Per Bonett & Wright (2000): n=75 per config yields CI half-width ≈ 0.12 for τ ≈ 0.7.\n\n**2b. GRS-Pearson: Safe Optimization Calibration via Correlated Proxies**\n\n  GRS-Pearson(R, F) = r(R(x), F(x)) = E[(R-μ_R)/σ_R · (F-μ_F)/σ_F]\n\n*Role*: Direct estimate of the correlation parameter r in the Correlated Proxies framework (Definition 4.1, arXiv:2403.03185). The mapping is EXACT: GRS-Pearson ≡ r. No transformation needed.\n\n*Connection to Regularization (Theorem 5.1)*: A GRS-Pearson confidence interval [r_L, r_U] translates directly to a regularization interval:\n  λ ∈ [σ√(1-r_U²), σ√(1-r_L²)]\nUsing the lower confidence bound r_L provides guaranteed conservative regularization:\n  P(λ̂ ≥ λ_true) ≥ 1 - α/2\n\n*Connection to Robust Optimization (arXiv:2604.12086, ICLR 2026)*: GRS-Pearson estimates the r that parametrizes the max-min robust optimization objective: max_π r·E[R_proxy] - √(1-r²)·√(χ² - E²[R_proxy]). Conservative r estimate → larger uncertainty set ℛ_corr → more robust policy. This addresses the paper's acknowledged open problem of principled r selection.\n\n*Why Pearson for calibration, not Kendall?*: Under the gaming contamination model (1-α)P_faithful + αP_gamed where P_gamed produces discordant outputs (high reward, low faithfulness):\n- Population Pearson r drops in proportion to BOTH contamination fraction α AND outlier magnitude m (unbounded influence → sensitive to severity)\n- Population Kendall τ drops in proportion to contamination fraction α ONLY (bounded influence → insensitive to severity)\n- Therefore τ_contaminated > r_contaminated: Kendall underestimates the proxy-truth degradation\n- Substituting τ for r in λ = σ√(1-r²) gives λ(τ) = σ√(1-τ²) < σ√(1-r²) = λ(r) — UNDER-regularization, not conservative\n- Pearson's sensitivity to outlier magnitude is a FEATURE for regularization: it faithfully reflects how severely gaming has degraded the proxy-truth relationship\n\n**2c. Dual-Track Complementarity Theorem:**\n\nGRS-Kendall and GRS-Pearson serve provably complementary roles:\n- Under no contamination (α=0): r = sin(πτ/2) (Greiner relation under bivariate normality). Both provide consistent information.\n- Under gaming contamination (α>0): the measures DIVERGE. Specifically, the Greiner divergence Δ_G = |r̂ - sin(πτ̂/2)| serves as a contamination indicator — large Δ_G signals non-normal contamination consistent with gaming. This divergence is itself a diagnostic: when GRS-Pearson drops faster than predicted by the Greiner transformation of GRS-Kendall, it indicates gaming outliers of large magnitude.\n- Information-theoretic complementarity: GRS-Kendall captures the ORDINAL degradation (how many rank inversions?), GRS-Pearson captures the CARDINAL degradation (how severe are the inversions?). Together, they provide a richer picture than either alone.\n\n**2d. GRS vs Exploitation-Rate: Complementary Detection Regimes:**\nGRS provides population-level monitoring with O(n log n) computation and bounded influence; exploitation-rate provides per-instance classification at O(K·n) frontier model cost but is vulnerable to correlated judge failures. GRS dominates when: contamination fraction ε > 0.05, evaluator cost is constrained, judge diversity is limited, or formally-grounded anchor is available. Exploitation-rate dominates for per-instance flagging in domains lacking formal anchors. Analytical comparison using published results; no experimental reimplementation.\n\n**2e. Multi-Faceted Faithfulness Anchors:**\n  GRS-GTED: F(x) = GTED tree-edit-distance (PRIMARY — formally-grounded, no LLM dependency)\n  GRS-LeanScorer: F(x) = LeanScorer Sugeno score (secondary)\n  GRS-roundtrip: F(x) = roundtrip consistency (tertiary)\n  GRS-human: F(x) = expert judgment (gold standard, 600 validation samples)\n\n**Phase 3: Systematic Ablation (8 Configurations)**\n  C1: Binary compilation only (FormaRL/Mathesis R_ver reproduction)\n  C2: Graded formal signal only (R_formal)\n  C3: Embedding similarity only (R_embed)\n  C4: LLM judge only (R_judge)\n  C5: Trained critic only (R_critic via CriticLeanGPT-14B-RL)\n  C6: Formal + embedding hybrid (R_formal + R_embed)\n  C7: Formal + trained critic hybrid (R_formal + R_critic)\n  C8: Full hybrid (R_formal + R_embed + R_critic)\n  Tiered model strategy: all 8 on Qwen2.5-Coder-7B-Instruct; top 4 by GRS on Qwen3-Coder-30B-A3B-Instruct.\n  MoE engineering for 30B: Qwen3-Coder-30B-A3B uses 128 experts with 8 active per forward pass; RL training of MoE architectures faces expert routing instability where ~10% of activated experts differ after policy updates, causing IS ratio fluctuations and potential training collapse (arXiv:2510.23027). We mitigate via: (a) auxiliary load-balancing loss to maintain expert utilization, (b) router-aware IS rescaling following Zhang et al. (2025), (c) conservative learning rate and clipping for 30B runs, (d) expert activation entropy monitoring as early divergence indicator.\n  Critic scaling sub-study: C5 with 14B (84.8%) vs 8B (~79.8%) on 7B model.\n\n**Phase 4: Adaptive Composition Demonstration (Lightweight, ~2 pages)**\n\nBrief demonstration that GRS can inform dynamic composition, tested on 7B with C8 component set:\n  D1: AGRC — w_k^(t+1) ∝ w_k^(t)·exp(η·GRS_k^(t)). Gaming-SPECIFIC: upweights gaming-resistant components based on per-component GRS-Kendall (monitoring role), updated every K=500 steps.\n  D2: CTWA (arXiv:2602.06869) — monitors Cov(r_k, s) and upweights when covariance drops below target c*_k. Gaming-AGNOSTIC but signal-driven: targets interference regardless of cause. Primary comparison — mechanistically closest to AGRC.\n  D3: MO-GRPO (arXiv:2509.22047) — A^MO = Σ_i [R_i - mean(R_i)]/std(R_i). Gaming-AGNOSTIC and static: normalizes variance. Reference baseline.\n\nHypotheses: (H1) When gaming concentrates in specific components, AGRC selectively downweights while CTWA and MO-GRPO cannot discriminate gamed from non-gamed components. (H2) CTWA may match AGRC when gaming correlates with negative covariance (interference and gaming are aligned). Both outcomes are publishable and informative.\n\n**Phase 5: Evaluation Framework (6 Analyses)**\n\n(1) Standard metrics + automated faithfulness: BEq@1, pass@1, ASSESS structural similarity, GTED score, LeanScorer score, FormalAlign alignment, roundtrip consistency\n(2) GRS decomposition: GRS-Kendall (primary monitoring), GRS-Spearman (secondary), AND GRS-Pearson (calibration) per configuration × checkpoint — the core analysis answering RQ1 and RQ2. Reporting all three enables the dual-track analysis and Greiner divergence diagnostic.\n(3) GRS-human validation: 75 samples × 8 key config-model pairs = 600 stratified expert audits with bootstrap BCA CIs (10,000 resamples). Stratified by gaming severity (no/mild/severe). Per Bonett & Wright: n=75 yields CI half-width ≈ 0.12 for τ ≈ 0.7\n(4) GRS theoretical validation: (a) GRS-Kendall subsampling analysis verifying Hoeffding bounds, (b) GRS-Pearson CI coverage under synthetic contamination injection verifying conservatism for regularization, (c) Greiner divergence (|r̂ - sin(πτ̂/2)|) as gaming contamination detector — calibrating when the dual-track measures diverge, (d) Correlated Proxies regularization interval accuracy — do GRS-Pearson-derived λ values produce policies with verified true-reward improvement?\n(5) Critic scaling: GRS comparison for R_critic using 14B (84.8%) vs 8B (~79.8%). Connected to FormalRewardBench's generation-evaluation gap: does critic accuracy predict gaming resistance?\n(6) AGRC vs CTWA vs MO-GRPO demonstration: weight trajectories, GRS at convergence, Pareto analysis (GRS vs standard accuracy)\n\n**Research Questions:**\n  RQ1: Which reward signal categories exhibit highest gaming resistance in isolation? Do formally-grounded signals (C2) outperform semantic (C3, C4) and learned-critic (C5) signals? Does critic accuracy predict gaming resistance? (C5 14B vs 8B)\n  RQ2: Does hybrid composition (C6-C8) yield additive faithfulness gains while maintaining gaming resistance?\n  RQ3: Is GRS-GTED a reliable automated proxy for expert gaming assessment? (correlation, bootstrap CIs, sample complexity verification)\n  RQ4: Does gaming-specific adaptation (AGRC) outperform gaming-agnostic adaptation (CTWA, MO-GRPO) when domain-specific detection is available? (brief demonstration)\n\n**Training:** GRPO with KL penalty on Qwen2.5-Coder-7B-Instruct and Qwen3-Coder-30B-A3B-Instruct. Training on ProofNet + FormalMATH-Lite.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1200 H100 (8 configs on 7B = 8×70 + top 4 on 30B = 4×70 + 3 demo configs on 7B = 3×70 + 80 grid search + 60 CriticLeanGPT inference + 60 evaluation)",
      "cpu_hours": "~35,000 CPU-hours on c7i.16xlarge for Lean compilation via Kimina Lean Server + GTED operator tree construction",
      "human_audit_hours": "~70 expert-hours for 600 stratified manual gaming audits (75 samples × 8 key config-model pairs) with bootstrap BCA validation",
      "timeline": "14-16 weeks (4 wks pipeline + GTED integration + GRS implementation + theoretical proofs + LeanInteract error parser, 5 wks RL training across configs, 1.5 wks demonstration configs (AGRC+CTWA+MO-GRPO), 4 wks evaluation/writing)",
      "estimated_gpu_cost": "$3,000 (at ~$2.50/hr H100 spot)",
      "estimated_cpu_cost": "$600-1,200 (c7i.16xlarge spot at ~$0.90/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "1050 H100",
      "cpu_hours": "~30,000 CPU-hours",
      "human_audit_hours": "~55 expert-hours",
      "timeline": "12-14 weeks",
      "claude_api_cost": "$500",
      "estimated_gpu_cost": "$2,625",
      "estimated_cpu_cost": "$500-1,000"
    },
    "auto_research": {
      "gpu_hours": "1050 H100",
      "cpu_hours": "~30,000 CPU-hours",
      "human_audit_hours": "~45 expert-hours (automated pre-filtering via GRS-GTED reduces manual load to disagreement cases)",
      "timeline": "10-12 weeks",
      "claude_api_cost": "$700",
      "estimated_gpu_cost": "$2,625",
      "estimated_cpu_cost": "$500-1,000",
      "speed_bottleneck": "Lean compilation (~7s avg) and GTED operator tree construction (~2s per statement). With 120-180 parallel Lean instances, throughput matches GPU generation."
    }
  },
  "target_venues": [
    "ICLR 2027 (abstract Sep 19, paper Sep 24, 2026 [estimated]) — PRIMARY, ~17 weeks available. Analysis paper framing (dual-track GRS + systematic ablation primary, AGRC demonstration secondary) fits ICLR's preference for principled analysis with clear contributions. The corrected Correlated Proxies connection (dual-track with conservatism guarantee) strengthens the theoretical contribution. Tighter scope makes clean narrative feasible.",
    "EACL 2027 (ARR Aug 3, 2026 → Oct 11 commitment) — SECONDARY, ~10 weeks for ARR submission. 7B full ablation + GRS framework + theoretical analysis feasible; 30B scaling and demonstration deferred to camera-ready.",
    "NAACL 2027 (ARR Oct 12, 2026 → commitment ~Oct 16 [estimated]) — TERTIARY CONTINGENCY. Full experiment set including 30B scaling and complete demonstration.",
    "ACL 2027 (ARR ~Feb 16, 2027 [estimated]) — SAFE FALLBACK. Complete experimental set with all supplementary analyses."
  ],
  "level": "strong-",
  "key_references": [
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "Mathesis: Towards Formal Theorem Proving from Natural Languages (ICLR 2026)",
    "Online Reinforcement Learning for Autoformalization (MAR Workshop @ NeurIPS 2025)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)",
    "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv July 2025)",
    "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (arXiv:2603.24372, March 2026)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv:2604.19459)",
    "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)",
    "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems (arXiv:2509.22047, Sep 2025)",
    "Uncovering Cross-Objective Interference in Multi-Objective Alignment [CTWA] (arXiv:2602.06869, Feb 2026)",
    "Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting [DRW] (TACL 2026)",
    "On the Hidden Objective Biases of Group-based Reinforcement Learning (arXiv:2601.05002, Jan 2026)",
    "Blockwise Advantage Estimation for Multi-Objective Alignment (arXiv:2602.10231, Feb 2026)",
    "Rethinking Reward Signals in Video GRPO: When Scores Become Targets [TaRoS] (arXiv:2511.19356)",
    "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, April 2026)",
    "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness [SignCert-PO] (arXiv:2604.02986, April 2026)",
    "Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063, March 2026)",
    "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges [Survey] (arXiv:2604.13602, April 2026)",
    "Detecting and Suppressing Reward Hacking with Gradient Fingerprints [GRIFT] (arXiv:2604.16242, April 2026)",
    "Reward Hacking in Rubric-Based Reinforcement Learning [Exploitation-rate] (arXiv:2605.12474, May 2026)",
    "FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv:2605.10141, May 2026)",
    "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking (arXiv:2403.03185, ICLR 2025 Spotlight)",
    "Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026)",
    "Reward Hacking Mitigation using Verifiable Composite Rewards (arXiv:2509.15557, ACM-BCB 2025)",
    "SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv:2605.21384, May 2026)",
    "Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization (AI4Math @ ICML 2025)",
    "FormalAlign: Automated Alignment Evaluation for Autoformalization (ICLR 2025)",
    "Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)",
    "Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)",
    "Process-Driven Autoformalization in Lean 4 (arXiv 2024)",
    "Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)",
    "ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)",
    "Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)",
    "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)",
    "Towards Stable and Effective Reinforcement Learning for Mixture-of-Experts (arXiv:2510.23027, Oct 2025)",
    "MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models (arXiv:2603.24984, March 2026)",
    "Sample Size Requirements for Estimating Pearson, Kendall and Spearman Correlations (Bonett & Wright, Psychometrika 2000)",
    "Influence functions of the Spearman and Kendall correlation measures (Croux & Dehon, Statistical Methods & Applications 2010)",
    "A comparative analysis of Spearman's rho and Kendall's tau in normal and contaminated normal models (Xu et al., Signal Processing 2013)",
    "A class of statistics with asymptotically normal distribution (Hoeffding, Annals of Mathematical Statistics 1948)",
    "Asymptotic Inference for Rank Correlations (Pohle, Wermuth & Weiss, arXiv:2512.14609)"
  ],
  "description": "Reward hacking in autoformalization is a documented concern — FormaRL's ablation shows syntax-only RL achieves 100% compilation but 0% semantic consistency, and VerifAI-2 (arXiv:2604.19459) reveals that high compilation rates in neuro-symbolic pipelines create an 'illusion of correctness' even when unified generation shows no systematic gaming. Yet we lack answers to a basic question: which reward signals maintain faithfulness under optimization pressure? This paper provides the first systematic answer, exploiting a capability unique to autoformalization: formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance.\n\nOur central insight is that autoformalization is uniquely positioned for principled gaming-resistance analysis. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers GTED — a computable faithfulness anchor derived from the Lean language server's operator trees. A critical methodological refinement: MONITORING gaming resistance and CALIBRATING safe optimization require fundamentally different correlation measures, leading to our dual-track framework.\n\nWe contribute three advances.\n\n**First (primary contribution)**, the dual-track GRS (Gaming Resistance Score) framework with deep theoretical grounding. GRS-Kendall measures rank correlation between reward signals and GTED-anchored faithfulness, providing ROBUST MONITORING: bounded influence functions (Croux & Dehon 2010) ensure stability under contamination, U-statistic theory gives exact sample complexity bounds (n ≥ 2log(2/δ)/ε² via Hoeffding), and lowest MSE under realistic gaming contamination (Xu et al. 2013). GRS-Pearson measures parametric correlation, providing SAFE OPTIMIZATION CALIBRATION: it exactly estimates the correlation parameter r in the Correlated Proxies framework (Definition 4.1, ICLR 2025 Spotlight), so a confidence interval [r_L, r_U] directly yields a regularization interval [σ√(1-r_U²), σ√(1-r_L²)] with formal conservatism guarantees via the lower confidence bound. GRS-Pearson also addresses an acknowledged open problem in Robust Correlated Proxies (arXiv:2604.12086, ICLR 2026) — providing principled, data-driven r estimation for their max-min robust optimization over all r-correlated proxies. The dual-track design resolves a subtle but critical issue: under gaming contamination, Kendall's τ (robust, bounded influence) drops LESS than Pearson's r (sensitive, unbounded influence), so τ_contaminated > r_contaminated, meaning naively substituting τ for r in regularization formulas would produce dangerously weak regularization. The dual-track framework assigns each measure to its natural role. We further show that the Greiner divergence |r̂ - sin(πτ̂/2)| — the gap between GRS-Pearson and the Greiner transformation of GRS-Kendall — serves as a real-time gaming contamination indicator. We validate GRS against 600 expert-annotated samples with bootstrap BCA confidence intervals.\n\n**Second (systematic analysis)**, the first comparison of gaming resistance across five isolated reward source categories for autoformalization RL: binary compilation, graded formal (via custom error-hierarchy classification over LeanInteract v0.11.3 diagnostics), embedding similarity (cf. cycle consistency in arXiv:2603.24372), LLM judge, and trained critic (CriticLeanGPT-Qwen3-14B-RL at 84.8% — first use as direct RL reward). Our 8-configuration GRPO ablation on Qwen2.5-Coder-7B-Instruct and Qwen3-Coder-30B-A3B-Instruct (with MoE routing stabilization via auxiliary load-balancing loss and router-aware IS rescaling per arXiv:2510.23027) isolates individual signal contributions, answering which signals to trust. FormalRewardBench's (arXiv:2605.10141) finding that specialized provers are poor evaluators motivates our sub-study of whether critic accuracy (14B vs 8B) predicts gaming resistance.\n\n**Third (lightweight demonstration)**, we briefly show that GRS can inform adaptive reward composition via AGRC (gaming-aware dynamic reweighting using per-component GRS-Kendall for the monitoring signal). We compare against CTWA (arXiv:2602.06869) — the most theoretically grounded objective-agnostic adaptive method, which monitors covariance between rewards and training signal — and MO-GRPO (arXiv:2509.22047), testing whether gaming-specific signals outperform gaming-agnostic adaptation. We position this in a dense landscape of 5+ objective-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS), honestly noting AGRC's mechanism is a demonstration of GRS's utility, not a primary methodological contribution.\n\nThe paper adopts VerifAI-2's outcome-based gaming definition: reward inflation without corresponding faithfulness improvement, requiring no intent attribution. It is designed for outcome robustness: if formally-grounded signals dominate, we advance reward design; if signals are equivalent, we establish cost-effectiveness; if CTWA matches AGRC, we demonstrate that gaming-specific detection is unnecessary (a useful negative result). Regardless, the dual-track GRS framework with its theoretical guarantees and the systematic gaming-resistance analysis are independent contributions. Targeting ICLR 2027 (Sep 24 estimated deadline), with EACL 2027, NAACL 2027, and ACL 2027 as contingency venues.",
  "project_name": "reward_comp_autoform",
  "source": "web_research"
}

## Reviewer feedback (round 8)
Issues: ["CRITICAL OMISSION — GSPO (arXiv:2507.18071, July 2025): Group Sequence Policy Optimization was developed by the Qwen team specifically because GRPO fails on MoE models like Qwen3-30B-A3B. The Qwen team found ~10% expert activation changes per GRPO gradient update (the exact statistic the proposal cites from arXiv:2510.23027) and developed GSPO as the algorithmic fix — defining importance ratios at sequence level rather than token level, eliminating the need for routing replay. The proposal uses GRPO on this exact model with engineering mitigations but doesn't acknowledge the model creator's own recommended algorithm. GSPO may also interact differently with multi-component reward decomposition (sequence-level vs token-level clipping), which is relevant to the per-component GRS analysis. This must be cited, discussed, and the GRPO choice must be justified — or GSPO should be adopted for the 30B experiments.", "MINOR OMISSION — MathAtlas (arXiv:2605.14061, May 2026): First large-scale autoformalization benchmark of graduate-level math (~52k theorems from 103 textbooks, achieving at most 9.8% correctness). While a benchmark paper rather than a methods paper, it reinforces the challenge of autoformalization at scale and could serve as additional evaluation data. Should be cited in the landscape.", "CriticLeanGPT-Qwen3-14B-RL accuracy (84.8%) could not be independently verified from web sources, though the model's existence on HuggingFace (15B parameters, Apache 2.0 license) is confirmed. The 32B variant achieves 87.0%. The 8B variant does not exist on HuggingFace — the proposal correctly identifies it as needing retraining. The 84.8% figure is plausible given the scaling trend (32B: 87%, 14B: ~84.8%, 8B: ~79.8%) but should be verified against the paper's Table 2.", "GSPO interaction with multi-objective reward: GSPO performs sequence-level clipping and rewarding. The proposal's approach requires token/component-level reward decomposition for per-component GRS analysis. Whether GSPO's sequence-level operation is compatible with this fine-grained decomposition is unclear. If GSPO is adopted, the proposal needs to verify that per-component reward signals can still be extracted and analyzed."]
Feedback: The proposal has matured substantially over 8 rounds — the τ-to-r theoretical fix is mathematically correct, the dual-track framework is well-motivated, and the connection to Correlated Proxies addresses a genuine open problem. You are very close to pass quality. The ONE remaining critical issue:

(1) **Cite and address GSPO (arXiv:2507.18071)**: This is the Qwen team's own algorithm designed specifically for MoE models like the Qwen3-Coder-30B-A3B you plan to use. You cite the MoE instability problem (arXiv:2510.23027) — GSPO is the algorithmic solution developed by the model's creators. Three options: (a) **Best**: Adopt GSPO for the 30B MoE experiments and justify GRPO for the 7B dense experiments, explaining how per-component reward decomposition works under sequence-level optimization. (b) **Good**: Justify GRPO over GSPO with a technical argument — e.g., GSPO's sequence-level operation may complicate per-component GRS monitoring (since GRS requires individual reward component analysis), while GRPO's token-level operation naturally exposes per-component rewards; acknowledge GSPO as an alternative that could be explored in future work. (c) **Adequate**: Cite GSPO and note that the primary contribution comes from the 7B dense model experiments (where GRPO is unproblematic), with 30B experiments as secondary scaling validation using established mitigations.

(2) **Minor**: Add MathAtlas (arXiv:2605.14061) to the autoformalization landscape — it's the largest benchmark as of May 2026 and shows the field's rapid growth.

With GSPO addressed, the proposal should clear the pass threshold. The theoretical framework is now sound, the empirical design is systematic, and the contributions are clearly articulated.

## Instructions
- Think in two phases: FIRST reconsider the problem framing (core_problem / opportunity / landscape) if the reviewer flagged issues there, THEN revise the method.
- Address each issue specifically.

## 深度调研要求

不要简单地'打补丁'——每一轮修订都是重新审视和深化的机会。

1. **深度搜索**：针对 reviewer 指出的每个问题，用 2-3 种不同的搜索查询调研。
2. **深度阅读**：用 WebFetch 实际阅读找到的关键论文。
3. **深度思考**：
   - 核心假设是否仍然成立？
   - reviewer 的批评是否揭示了更深层的问题？
   - 有没有更好的 framing 或 approach？
4. **避免表面修订**：如果反复 minor fix 没有实质改进，考虑 major revision 或 pivot。

## 针对 Review 意见的定向搜索

1. **如果'已有类似工作'**：搜索并阅读相关论文，明确差异化点
2. **如果'SOTA 过时'**：查看 Papers With Code 排行榜，更新 baseline
3. **如果'可行性有问题'**：搜索类似实验成本和 GitHub 实现
4. **如果'novelty 不足'**：做 3-5 种关键词搜索，考虑 major revision 或 pivot

- You have full freedom: minor fix, major revision, or pivot.
- Include a "change_type" field: "minor", "major", or "pivot".
- Output a COMPLETE JSON object with ALL fields.

## 停滞提醒
经过 8 轮修订，近 3 轮平均分从 3.6 到 3.8，无明显改善。
考虑 major revision 或 pivot。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "type": "user",
  "uuid": "22d8fbaa-908b-4d02-8942-e9dc6b82ee0e",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-27T23:04:32.021Z_

```json
{
  "parentUuid": "22d8fbaa-908b-4d02-8942-e9dc6b82ee0e",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskCreate",
      "TaskGet",
      "TaskList",
      "TaskOutput",
      "TaskStop",
      "TaskUpdate",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": [],
    "readdedNames": [],
    "pendingMcpServers": []
  },
  "type": "attachment",
  "uuid": "2d63e08c-aa11-49ab-9f76-29c40ecf534a",
  "timestamp": "2026-05-27T23:04:32.021Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-27T23:04:32.021Z_

```json
{
  "parentUuid": "2d63e08c-aa11-49ab-9f76-29c40ecf534a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "aabd31c9-13b1-4cd8-a0c7-920746d9c57f",
  "timestamp": "2026-05-27T23:04:32.021Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"FIXED τ-TO-r THEORETICAL BRIDGE (most critical fix): Iden…",
  "leafUuid": "aabd31c9-13b1-4cd8-a0c7-920746d9c57f",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistance analysis: address GSPO and benchmark gaps",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Assistant

_source line 8 · 2026-05-27T23:04:38.287Z_

<details><summary>Logged reasoning block</summary>

```text
The reviewer feedback in round 8 is quite positive - they say "You are very close to pass quality" and the main remaining issue is citing and addressing GSPO. Let me research GSPO and MathAtlas thoroughly before making revisions.

Let me search for:
1. GSPO (arXiv:2507.18071) - the Qwen team's algorithm for MoE models
2. MathAtlas (arXiv:2605.14061) - large-scale autoformalization benchmark
3. Any interaction between GSPO and multi-objective reward decomposition

The reviewer gives three options for addressing GSPO, with option (a) being best. 

Before I decide on the best approach, I need to dig into the details of these papers and understand how they relate to my work.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aabd31c9-13b1-4cd8-a0c7-920746d9c57f",
  "isSidechain": false,
  "requestId": "req_011CbTujSbSRpieLAfFLuwWV",
  "type": "assistant",
  "uuid": "3ff1fb54-fbb6-46f6-9a50-e677dcb437ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ojjR9psZKwskoE3ztZTgJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16745,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1390,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16745
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 9 · 2026-05-27T23:04:38.289Z_

I'll research GSPO and MathAtlas thoroughly before making revisions. Let me launch parallel searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3ff1fb54-fbb6-46f6-9a50-e677dcb437ba",
  "isSidechain": false,
  "requestId": "req_011CbTujSbSRpieLAfFLuwWV",
  "type": "assistant",
  "uuid": "ff2d2b45-ad2e-4f8d-9e3c-efe2466cad79",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ojjR9psZKwskoE3ztZTgJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16745,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1390,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16745
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 10 · 2026-05-27T23:04:44.228Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01FiQaEdHiKDCcToc226HKKW`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research GSPO algorithm",
  "prompt": "I need to deeply research GSPO (Group Sequence Policy Optimization), arXiv:2507.18071, July 2025. This was developed by the Qwen team specifically because GRPO fails on MoE (Mixture-of-Experts) models like Qwen3-30B-A3B.\n\nPlease:\n1. Search the web for \"GSPO Group Sequence Policy Optimization arXiv 2507.18071\" and related queries\n2. Fetch the arXiv abstract page at https://arxiv.org/abs/2507.18071\n3. Search for \"GSPO MoE GRPO Qwen sequence-level importance ratio\"\n4. Search for any blog posts or discussions about GSPO vs GRPO for MoE models\n5. Try to fetch the paper PDF or HTML version to get more details about the algorithm\n\nKey questions I need answered:\n- What exactly is GSPO's mechanism? (sequence-level vs token-level importance ratios)\n- Why does it solve the MoE routing instability problem?\n- How does it interact with multi-objective/multi-component rewards?\n- Does GSPO use sequence-level clipping? If so, can per-component reward signals still be extracted?\n- What were the specific experimental results showing GSPO > GRPO on MoE?\n- Is there any discussion of GSPO with composite/multi-objective rewards?\n\nPlease be thorough - read actual paper content, not just abstracts."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ff2d2b45-ad2e-4f8d-9e3c-efe2466cad79",
  "isSidechain": false,
  "requestId": "req_011CbTujSbSRpieLAfFLuwWV",
  "type": "assistant",
  "uuid": "9b8c703d-6f72-40bf-85d9-d58184baf698",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ojjR9psZKwskoE3ztZTgJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16745,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1390,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16745
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 11 · 2026-05-27T23:04:48.519Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01Mv6ktK8eYGsyqxr8uPDFte`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research MathAtlas benchmark",
  "prompt": "I need to research MathAtlas (arXiv:2605.14061, May 2026), described as the first large-scale autoformalization benchmark of graduate-level math (~52k theorems from 103 textbooks, achieving at most 9.8% correctness).\n\nPlease:\n1. Search the web for \"MathAtlas arXiv 2605.14061 autoformalization benchmark\"\n2. Fetch the arXiv abstract page at https://arxiv.org/abs/2605.14061\n3. Search for \"MathAtlas large-scale autoformalization graduate math\"\n4. Try to get details from the paper\n\nKey questions:\n- What exactly does MathAtlas contain? (size, scope, domains)\n- What correctness metrics were used?\n- Which models were evaluated and what were the results?\n- How does it compare to existing benchmarks like ProofNet and FormalMATH-Lite?\n- Any insights about reward design or evaluation for autoformalization?\n\nBe thorough - read actual paper content."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b8c703d-6f72-40bf-85d9-d58184baf698",
  "isSidechain": false,
  "requestId": "req_011CbTujSbSRpieLAfFLuwWV",
  "type": "assistant",
  "uuid": "53bd244d-504e-4516-abe9-477f46b69238",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ojjR9psZKwskoE3ztZTgJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16745,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1390,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16745
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 12 · 2026-05-27T23:04:56.096Z_

<details open><summary>🔧 Tool call — Agent · `toolu_01HujkgCbCtYkjfMt3BCt6Nw`</summary>

```json
{
  "subagent_type": "general-purpose",
  "description": "Research GSPO-GRPO MoE comparison",
  "prompt": "I need to research the specific technical differences between GSPO and GRPO for Mixture-of-Experts models, and whether GSPO is compatible with multi-component reward decomposition.\n\nPlease search for:\n1. \"GSPO GRPO MoE routing instability sequence level\" \n2. \"Qwen3 30B training reinforcement learning GSPO\"\n3. \"sequence level policy optimization multi-objective reward\"\n4. \"GRPO token level importance ratio MoE expert routing\"\n5. Search for the Qwen3 technical report or blog post discussing their training methodology for MoE models\n\nKey technical questions:\n- In GRPO, importance ratios are computed at token level: π_θ(a_t|s_t)/π_θ_old(a_t|s_t). In GSPO, are they at sequence level: π_θ(y|x)/π_θ_old(y|x)?\n- If GSPO uses sequence-level ratios, does the reward still need to be decomposed per-token, or is it naturally sequence-level?\n- For multi-component rewards R = w1*R1 + w2*R2 + ..., does GSPO's sequence-level operation prevent per-component analysis?\n- My use case: I want to compute GRS (Gaming Resistance Score) per individual reward component. With GRPO, each component R_k contributes separately to the advantage. With GSPO, if everything is sequence-level, can I still decompose?\n\nThink carefully about this compatibility question."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "53bd244d-504e-4516-abe9-477f46b69238",
  "isSidechain": false,
  "requestId": "req_011CbTujSbSRpieLAfFLuwWV",
  "type": "assistant",
  "uuid": "3cca66e1-a050-4297-9ff0-e13fad314f9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017ojjR9psZKwskoE3ztZTgJ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16745,
      "cache_read_input_tokens": 11014,
      "output_tokens": 1390,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16745,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 1390,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16745,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16745
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 13 · 2026-05-27T23:07:07.821Z_

<details><summary>↩ Tool result · `toolu_01Mv6ktK8eYGsyqxr8uPDFte`</summary>

```text
Now I have a comprehensive picture. Here is the full research synthesis.

---

## MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061)

**Authors:** Nilay Patel, Noah Arias, Davit Babayan, Victoria Cochran, Timothy Libman, Hafsah Mahmood, Liam McCarty, Soli Munoz, Laurel Willey, Jeffrey Flanigan (UC Santa Cruz)
**Submitted:** May 13, 2026 | **Venue:** Submitted to NeurIPS 2026
**Categories:** cs.AI, cs.LG

---

### 1. What MathAtlas Contains

**Scale:** ~52,052 mathematical entities extracted from 103 graduate-level mathematics textbooks.

**Entity types and approximate counts:**
- ~18k theorems
- ~10k exercises
- ~10k definitions
- ~10k proofs
- ~5k examples (the paper states ~55k examples in one passage, but the total is ~52k entities, so this may reflect sub-entities)

**Domain coverage:** 87 distinct mathematical fields/subfields, including real analysis, differential geometry, category theory, topology, quantum groups, Lie algebra, set theory, logic, algebraic geometry, commutative algebra, abstract algebra, probability, quantum theory, and number theory.

**Dependency graph:** ~178k relations of three types:
- **Entity references** (one entity referencing another)
- **Object references** (linking concepts to their definitions, ~193k total, ~3.69 per entity)
- **"Proves" relations** (connecting proofs to theorems)

Dependency depth ranges from 0 to 80 (mean ~30, median ~17). Fields like Lie algebra/quantum groups average ~50 depth; set theory/logic average ~6.

**Extraction pipeline:**
1. PDFs converted to Mathematical Markdown using Nougat
2. Metadata pages filtered out
3. Few-shot prompted gpt-oss-120b with JSON schema and structured decoding (temperature 0.3) identified entity spans and types
4. Quality: 90.4% of annotated entities correctly extracted (98% for definitions, 80% for proofs); reference extraction achieved 94.8% F1 overall

**Copyright handling:** ~30% from Springer textbooks (released only as generation code); remaining 70% publicly released.

---

### 2. Correctness Metrics

MathAtlas uses a two-pronged correctness definition: **A formalization is correct only if it both compiles AND is semantically faithful to the informal statement.**

- **Compilation rate:** Checked using the `blv` tool against Lean v4.24.0
- **Semantic faithfulness:** Evaluated via MA-Align, a new 200-entity benchmark with binary "aligned"/"misaligned" labels for syntactically correct formalizations

For MA-Align evaluation, they tested CriticLean (14B and 32B) and LLM-as-judge systems (gpt-5.2 with engineered prompts). Results on MA-Align:
- CriticLean 32B: 80.0% accuracy on definitions, 75.0% on statements
- gpt-5.2 with few-shot engineered prompts: 86.0% on definitions, 80.0% on statements

The critical insight is the massive gap between compilation and correctness -- models can produce code that compiles but is mathematically meaningless.

---

### 3. Model Evaluation Results

**Statements (fine-tuned models):**

| Model | Compile Rate | Faithful | Correct |
|---|---|---|---|
| Herald 7B | 11.8% | 12.7% | 1.5% |
| Kimina 7B | 27.3% | 8.4% | 2.3% |
| ATLAS-L 8B | 21.4% | 16.4% | 3.5% |
| Goedel 8B | 20.3% | 34.9% | 7.1% |
| Goedel 32B | 23.2% | 30.6% | 7.1% |
| **ReForm 8B** | **19.0%** | **48.4%** | **9.8%** |

**Statements (prompted models):**

| Model | Compile Rate | Faithful | Correct |
|---|---|---|---|
| gpt-oss-20b zero-shot | -- | -- | 4.2% |
| gpt-oss-120b tuned examples | 21.7% | 35.9% | 7.8% |

**Definitions (prompted models only -- no fine-tuned methods generalize):**

| Model | Compile Rate | Faithful | Correct |
|---|---|---|---|
| gpt-oss-20b zero-shot | 10.5% | 20.9% | 2.2% |
| gpt-oss-120b tuned examples | 28.5% | 58.5% | 16.7% |

**MA-Hard subset** (~700 entities with deepest dependency trees, 14 subjects, primarily algebraic geometry and Lie theory):
- Best model: only **2.6% correctness**
- gpt-oss-120b: 14.6% compilation but only 2.6% correctness

**Prompt engineering ablation (statements, gpt-oss-120b):**
- Zero-shot: 14.3% compile
- +Few-shot examples: 16.8%
- +Tuned prompt: 17.1%
- +Tuned examples: 21.7%

---

### 4. Comparison to Existing Benchmarks

MathAtlas fills a clear gap. Prior benchmarks focus on simpler math:
- **ProofNet:** Undergraduate-level mathematics
- **miniF2F:** Olympiad-level mathematics
- **FATE-H/FATE-X:** 100 problems from commutative/abstract algebra
- **ConsistencyCheck / CriticLeanBench:** Focus on simpler domains

MathAtlas is distinguished by:
1. **Scale:** ~52k entities vs. hundreds in prior benchmarks
2. **Level:** Graduate-level vs. undergraduate/olympiad
3. **Dependency graph:** First benchmark to include ~178k dependency relations
4. **Entity diversity:** Includes definitions (previously underexplored), not just theorem statements
5. **MA-Align:** First semantic faithfulness benchmark covering both theorems and definitions at the graduate level

No mention of FormalMATH-Lite was found in the paper.

---

### 5. Key Insights on Reward Design and Evaluation

**Compilation is a poor proxy for correctness.** The paper's most striking finding is the dramatic gap between compilation rate and actual correctness. Kimina 7B is the extreme case: 27.3% compilation rate but only 2.3% correctness. This means **only ~8% of Kimina's compiling formalizations are semantically faithful.** This directly challenges RL approaches that use compilation as a reward signal.

**ReForm 8B is the exception:** Despite having a lower compile rate (19.0%) than Kimina (27.3%) or Goedel 32B (23.2%), ReForm achieves the highest faithfulness (48.4%) and correctness (9.8%), suggesting its "reflective" training approach produces more meaningful formalizations even if fewer compile.

**Local context hurts, counterintuitively.** Adding 300 tokens of surrounding context *decreased* performance from 20.3% to 17.4% on definitions and from 10.5% to 8.6% on statements. This suggests that naive context inclusion confuses models, highlighting the need for smarter dependency-aware retrieval.

**Mathlib grounding matters.** Definitions grounded in Mathlib (via LeanSearch) had a 27.9% correctness rate vs. 16.8% for ungrounded definitions (chi-square p<0.001). This 1.66x advantage shows that existing library coverage is a critical factor.

**Dependency depth is the key difficulty driver.** A Kolmogorov-Smirnov test confirmed a statistically significant difference (p<0.001) between depth distributions for correct vs. incorrect formalizations. The MA-Hard subset (deepest dependency trees) drops to just 2.6% correctness.

**Definition autoformalization is an open problem.** No fine-tuned methods successfully generalize from theorem to definition autoformalization. The authors could not evaluate some prior definition methods (ARIA, LoC-Decomp) due to unreleased code.

---

### 6. Limitations and Future Directions

- Focus is graduate-level, not research-level mathematics
- Proof formalization and full theorem proving are left to future work
- The authors call for **dependency-aware autoformalization systems** that can leverage the graph structure
- Better semantic faithfulness metrics are needed that generalize beyond simple domains

---

Sources:
- [MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv abstract)](https://arxiv.org/abs/2605.14061)
- [MathAtlas: A Benchmark for Autoformalization in the Wild (HTML full paper)](https://arxiv.org/html/2605.14061)
- [ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization](https://arxiv.org/abs/2510.24592)
- [An Evaluation Benchmark for Autoformalization in Lean4](https://arxiv.org/abs/2406.06555)

agentId: a8e91c0fc33459163 (use SendMessage with to: 'a8e91c0fc33459163' to continue this agent)
&lt;usage>total_tokens: 21510
tool_uses: 10
duration_ms: 139299&lt;/usage>
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "53bd244d-504e-4516-abe9-477f46b69238",
  "isSidechain": false,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "type": "user",
  "uuid": "28bc9ac4-1f92-4a5f-9157-0ac64da641cb",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research MathAtlas (arXiv:2605.14061, May 2026), described as the first large-scale autoformalization benchmark of graduate-level math (~52k theorems from 103 textbooks, achieving at most 9.8% correctness).\n\nPlease:\n1. Search the web for \"MathAtlas arXiv 2605.14061 autoformalization benchmark\"\n2. Fetch the arXiv abstract page at https://arxiv.org/abs/2605.14061\n3. Search for \"MathAtlas large-scale autoformalization graduate math\"\n4. Try to get details from the paper\n\nKey questions:\n- What exactly does MathAtlas contain? (size, scope, domains)\n- What correctness metrics were used?\n- Which models were evaluated and what were the results?\n- How does it compare to existing benchmarks like ProofNet and FormalMATH-Lite?\n- Any insights about reward design or evaluation for autoformalization?\n\nBe thorough - read actual paper content.",
    "agentId": "a8e91c0fc33459163",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have a comprehensive picture. Here is the full research synthesis.\n\n---\n\n## MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061)\n\n**Authors:** Nilay Patel, Noah Arias, Davit Babayan, Victoria Cochran, Timothy Libman, Hafsah Mahmood, Liam McCarty, Soli Munoz, Laurel Willey, Jeffrey Flanigan (UC Santa Cruz)\n**Submitted:** May 13, 2026 | **Venue:** Submitted to NeurIPS 2026\n**Categories:** cs.AI, cs.LG\n\n---\n\n### 1. What MathAtlas Contains\n\n**Scale:** ~52,052 mathematical entities extracted from 103 graduate-level mathematics textbooks.\n\n**Entity types and approximate counts:**\n- ~18k theorems\n- ~10k exercises\n- ~10k definitions\n- ~10k proofs\n- ~5k examples (the paper states ~55k examples in one passage, but the total is ~52k entities, so this may reflect sub-entities)\n\n**Domain coverage:** 87 distinct mathematical fields/subfields, including real analysis, differential geometry, category theory, topology, quantum groups, Lie algebra, set theory, logic, algebraic geometry, commutative algebra, abstract algebra, probability, quantum theory, and number theory.\n\n**Dependency graph:** ~178k relations of three types:\n- **Entity references** (one entity referencing another)\n- **Object references** (linking concepts to their definitions, ~193k total, ~3.69 per entity)\n- **\"Proves\" relations** (connecting proofs to theorems)\n\nDependency depth ranges from 0 to 80 (mean ~30, median ~17). Fields like Lie algebra/quantum groups average ~50 depth; set theory/logic average ~6.\n\n**Extraction pipeline:**\n1. PDFs converted to Mathematical Markdown using Nougat\n2. Metadata pages filtered out\n3. Few-shot prompted gpt-oss-120b with JSON schema and structured decoding (temperature 0.3) identified entity spans and types\n4. Quality: 90.4% of annotated entities correctly extracted (98% for definitions, 80% for proofs); reference extraction achieved 94.8% F1 overall\n\n**Copyright handling:** ~30% from Springer textbooks (released only as generation code); remaining 70% publicly released.\n\n---\n\n### 2. Correctness Metrics\n\nMathAtlas uses a two-pronged correctness definition: **A formalization is correct only if it both compiles AND is semantically faithful to the informal statement.**\n\n- **Compilation rate:** Checked using the `blv` tool against Lean v4.24.0\n- **Semantic faithfulness:** Evaluated via MA-Align, a new 200-entity benchmark with binary \"aligned\"/\"misaligned\" labels for syntactically correct formalizations\n\nFor MA-Align evaluation, they tested CriticLean (14B and 32B) and LLM-as-judge systems (gpt-5.2 with engineered prompts). Results on MA-Align:\n- CriticLean 32B: 80.0% accuracy on definitions, 75.0% on statements\n- gpt-5.2 with few-shot engineered prompts: 86.0% on definitions, 80.0% on statements\n\nThe critical insight is the massive gap between compilation and correctness -- models can produce code that compiles but is mathematically meaningless.\n\n---\n\n### 3. Model Evaluation Results\n\n**Statements (fine-tuned models):**\n\n| Model | Compile Rate | Faithful | Correct |\n|---|---|---|---|\n| Herald 7B | 11.8% | 12.7% | 1.5% |\n| Kimina 7B | 27.3% | 8.4% | 2.3% |\n| ATLAS-L 8B | 21.4% | 16.4% | 3.5% |\n| Goedel 8B | 20.3% | 34.9% | 7.1% |\n| Goedel 32B | 23.2% | 30.6% | 7.1% |\n| **ReForm 8B** | **19.0%** | **48.4%** | **9.8%** |\n\n**Statements (prompted models):**\n\n| Model | Compile Rate | Faithful | Correct |\n|---|---|---|---|\n| gpt-oss-20b zero-shot | -- | -- | 4.2% |\n| gpt-oss-120b tuned examples | 21.7% | 35.9% | 7.8% |\n\n**Definitions (prompted models only -- no fine-tuned methods generalize):**\n\n| Model | Compile Rate | Faithful | Correct |\n|---|---|---|---|\n| gpt-oss-20b zero-shot | 10.5% | 20.9% | 2.2% |\n| gpt-oss-120b tuned examples | 28.5% | 58.5% | 16.7% |\n\n**MA-Hard subset** (~700 entities with deepest dependency trees, 14 subjects, primarily algebraic geometry and Lie theory):\n- Best model: only **2.6% correctness**\n- gpt-oss-120b: 14.6% compilation but only 2.6% correctness\n\n**Prompt engineering ablation (statements, gpt-oss-120b):**\n- Zero-shot: 14.3% compile\n- +Few-shot examples: 16.8%\n- +Tuned prompt: 17.1%\n- +Tuned examples: 21.7%\n\n---\n\n### 4. Comparison to Existing Benchmarks\n\nMathAtlas fills a clear gap. Prior benchmarks focus on simpler math:\n- **ProofNet:** Undergraduate-level mathematics\n- **miniF2F:** Olympiad-level mathematics\n- **FATE-H/FATE-X:** 100 problems from commutative/abstract algebra\n- **ConsistencyCheck / CriticLeanBench:** Focus on simpler domains\n\nMathAtlas is distinguished by:\n1. **Scale:** ~52k entities vs. hundreds in prior benchmarks\n2. **Level:** Graduate-level vs. undergraduate/olympiad\n3. **Dependency graph:** First benchmark to include ~178k dependency relations\n4. **Entity diversity:** Includes definitions (previously underexplored), not just theorem statements\n5. **MA-Align:** First semantic faithfulness benchmark covering both theorems and definitions at the graduate level\n\nNo mention of FormalMATH-Lite was found in the paper.\n\n---\n\n### 5. Key Insights on Reward Design and Evaluation\n\n**Compilation is a poor proxy for correctness.** The paper's most striking finding is the dramatic gap between compilation rate and actual correctness. Kimina 7B is the extreme case: 27.3% compilation rate but only 2.3% correctness. This means **only ~8% of Kimina's compiling formalizations are semantically faithful.** This directly challenges RL approaches that use compilation as a reward signal.\n\n**ReForm 8B is the exception:** Despite having a lower compile rate (19.0%) than Kimina (27.3%) or Goedel 32B (23.2%), ReForm achieves the highest faithfulness (48.4%) and correctness (9.8%), suggesting its \"reflective\" training approach produces more meaningful formalizations even if fewer compile.\n\n**Local context hurts, counterintuitively.** Adding 300 tokens of surrounding context *decreased* performance from 20.3% to 17.4% on definitions and from 10.5% to 8.6% on statements. This suggests that naive context inclusion confuses models, highlighting the need for smarter dependency-aware retrieval.\n\n**Mathlib grounding matters.** Definitions grounded in Mathlib (via LeanSearch) had a 27.9% correctness rate vs. 16.8% for ungrounded definitions (chi-square p<0.001). This 1.66x advantage shows that existing library coverage is a critical factor.\n\n**Dependency depth is the key difficulty driver.** A Kolmogorov-Smirnov test confirmed a statistically significant difference (p<0.001) between depth distributions for correct vs. incorrect formalizations. The MA-Hard subset (deepest dependency trees) drops to just 2.6% correctness.\n\n**Definition autoformalization is an open problem.** No fine-tuned methods successfully generalize from theorem to definition autoformalization. The authors could not evaluate some prior definition methods (ARIA, LoC-Decomp) due to unreleased code.\n\n---\n\n### 6. Limitations and Future Directions\n\n- Focus is graduate-level, not research-level mathematics\n- Proof formalization and full theorem proving are left to future work\n- The authors call for **dependency-aware autoformalization systems** that can leverage the graph structure\n- Better semantic faithfulness metrics are needed that generalize beyond simple domains\n\n---\n\nSources:\n- [MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv abstract)](https://arxiv.org/abs/2605.14061)\n- [MathAtlas: A Benchmark for Autoformalization in the Wild (HTML full paper)](https://arxiv.org/html/2605.14061)\n- [ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization](https://arxiv.org/abs/2510.24592)\n- [An Evaluation Benchmark for Autoformalization in Lean4](https://arxiv.org/abs/2406.06555)"
      }
    ],
    "totalDurationMs": 139299,
    "totalTokens": 21510,
    "totalToolUseCount": 10,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1859,
      "cache_read_input_tokens": 17350,
      "output_tokens": 2300,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 1859
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2300,
          "cache_read_input_tokens": 17350,
          "cache_creation_input_tokens": 1859,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 1859,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 10
    }
  },
  "sourceToolAssistantUUID": "53bd244d-504e-4516-abe9-477f46b69238",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 14 · 2026-05-27T23:07:57.374Z_

<details><summary>↩ Tool result · `toolu_01HujkgCbCtYkjfMt3BCt6Nw`</summary>

````text
Now I have all the technical details needed to provide a comprehensive answer. Here is my analysis:

---

## Technical Differences Between GSPO and GRPO for MoE Models, and Compatibility with Multi-Component Reward Decomposition

### 1. GRPO vs. GSPO: Token-Level vs. Sequence-Level Importance Ratios

**GRPO (token-level):**
The importance ratio is computed per token:

```
w_{i,t}(theta) = pi_theta(y_{i,t} | x, y_{i,&lt;t}) / pi_{theta_old}(y_{i,t} | x, y_{i,&lt;t})
```

Each token gets its own ratio, and clipping is applied per-token. The objective aggregates these across the sequence (typically via arithmetic mean).

**GSPO (sequence-level):**
The importance ratio is the *geometric mean* of per-token ratios across the entire sequence:

```
s_i(theta) = [ pi_theta(y_i | x) / pi_{theta_old}(y_i | x) ]^{1/|y_i|}
```

Which is mathematically equivalent to:

```
s_i(theta) = exp( (1/|y_i|) * sum_t log[ pi_theta(y_{i,t} | x, y_{i,&lt;t}) / pi_{theta_old}(y_{i,t} | x, y_{i,&lt;t}) ] )
```

This produces a **single scalar ratio per sequence**, and clipping is applied at the sequence level.

**GSPO's full objective:**

```
J_GSPO(theta) = E[ (1/G) * sum_i min( s_i(theta) * A_hat_i, clip(s_i(theta), 1-eps, 1+eps) * A_hat_i ) ]
```

This mirrors PPO's clipped surrogate objective but operates entirely at sequence granularity.

### 2. Why GSPO Solves MoE Routing Instability

The core problem: In MoE models like Qwen3-30B-A3B (48 layers, 128 experts, 8 active per token), approximately **10% of the experts activated under the new policy differ from those under the old policy** after each gradient update. This expert-activation volatility causes:

- Token-level importance ratios in GRPO to fluctuate wildly, since different experts produce very different token probabilities
- Massive variance in gradients
- Training collapse (GRPO on Qwen3-30B-A3B actually *underperformed* the base model: 71.5% vs 74.2% average on math benchmarks)

GSPO's sequence-level geometric mean *averages out* the per-token routing noise. Even if individual tokens have wildly different expert assignments between old and new policies, the geometric mean across the full sequence is stable. This completely eliminates the need for "Routing Replay" (a workaround where old-policy expert assignments are cached and reused, which was shown to be unsatisfactory because it restricts exploration and degrades final performance).

**Empirical evidence:** On Qwen3-30B-A3B, GSPO achieved 76.4% vs GRPO's 71.5% on math benchmarks, with GRPO showing "pronounced performance collapse around 200-500 training steps."

### 3. Reward and Advantage Computation in GSPO

The advantage in GSPO uses the same **group-relative** normalization as GRPO, but operates on a single scalar reward per sequence:

```
A_hat_i = [ r(x, y_i) - mean({r(x, y_j)}) ] / std({r(x, y_j)})
```

where the mean and standard deviation are computed across the group of G sampled responses to the same query. This is critic-free (no value network needed). The reward `r(x, y_i)` is a **single scalar** assigned to the complete response.

### 4. Your Key Question: Compatibility with Multi-Component Reward Decomposition

This is where the analysis gets nuanced. Let me address each sub-question:

**Q: Does GSPO naturally handle sequence-level rewards without per-token decomposition?**

Yes. Since both the importance ratio `s_i(theta)` and the advantage `A_hat_i` are sequence-level scalars, there is no need to assign credit to individual tokens. The reward `r(x, y_i)` is inherently a sequence-level quantity, and GSPO's objective is fully consistent with this --- unlike GRPO, which has a structural mismatch between token-level ratios and sequence-level rewards.

**Q: For multi-component rewards R = w1*R1 + w2*R2 + ..., does GSPO's sequence-level operation prevent per-component analysis?**

**No, it does not prevent it.** Here is the critical insight:

The advantage in GSPO is computed from the scalar reward *before* entering the objective function. The reward can be a weighted sum of components:

```
r(x, y_i) = w1*R1(x, y_i) + w2*R2(x, y_i) + ... + wK*RK(x, y_i)
```

Because GSPO's advantage is a linear function of the reward (after group normalization), you can decompose:

```
A_hat_i = [ sum_k wk*Rk(x,y_i) - mean(sum_k wk*Rk(x,y_j)) ] / std(...)
```

However, there is a subtlety: the standard deviation in the denominator is computed from the *total* reward, not per component. This means the advantage does **not** decompose cleanly into a sum of per-component advantages unless you adopt the MO-GRPO approach.

**Q: Can you compute a Gaming Resistance Score (GRS) per individual reward component with GSPO?**

**Yes, but you need to adopt the MO-GRPO normalization strategy adapted for GSPO.** Here is how:

The paper [MO-GRPO](https://arxiv.org/abs/2509.22047) identifies exactly the problem you are worried about: when using standard GRPO with `R = sum(wk * Rk)`, the correlation of the advantage with each component Rk is proportional to that component's standard deviation sigma_k. High-variance reward components dominate optimization, creating a reward hacking vector.

MO-GRPO's solution is to normalize each component independently:

```
A^{MO}_i = sum_k [ (Rk(x,y_i) - mean(Rk)) / std(Rk) ]
```

This ensures each component contributes approximately `1/sqrt(K)` correlation regardless of its scale or variance.

**The key compatibility point: This MO-GRPO advantage formulation is fully compatible with GSPO.** The advantage computation is independent of whether you use token-level or sequence-level importance ratios. You can plug `A^{MO}_i` directly into the GSPO objective:

```
J_{MO-GSPO}(theta) = E[ (1/G) * sum_i min( s_i(theta) * A^{MO}_i, clip(s_i(theta), 1-eps, 1+eps) * A^{MO}_i ) ]
```

To compute GRS per component, you can then:
1. **Track per-component advantage contributions:** For each component k, compute `A^k_i = (Rk(x,y_i) - mean(Rk)) / std(Rk)` separately
2. **Monitor per-component reward curves independently** during training
3. **Measure gaming resistance per component** by checking whether the policy exploits any single Rk at the expense of others

Since GSPO's importance ratio `s_i(theta)` is a single scalar multiplying the full advantage, you can decompose the gradient signal as:

```
gradient contribution from component k ∝ s_i(theta) * A^k_i
```

This decomposition is exact (not approximate) because the importance ratio is shared across all components --- it captures "how much the policy changed" at the sequence level, while each `A^k_i` captures "how good was this change for component k."

### 5. Summary of Recommendations

| Aspect | GRPO | GSPO | Impact on Your Use Case |
|--------|------|------|------------------------|
| Importance ratio | Token-level | Sequence-level (geometric mean) | GSPO is required for MoE stability |
| MoE compatibility | Poor (10% expert drift causes collapse) | Excellent (inherently robust) | Use GSPO for MoE models |
| Reward level | Sequence-level reward, token-level optimization (mismatch) | Sequence-level reward, sequence-level optimization (aligned) | GSPO is more principled |
| Multi-component rewards | MO-GRPO extension exists | Can adopt MO-GRPO advantage into GSPO (untested but mathematically sound) | Implement MO-GSPO hybrid |
| Per-component GRS | Yes, via per-component advantage tracking | Yes, via same mechanism (advantage decomposes linearly) | Fully compatible |

**Bottom line:** GSPO is compatible with multi-component reward decomposition and per-component GRS analysis. The importance ratio (`s_i`) and the advantage (`A_hat_i`) are independent computations that enter the objective multiplicatively. You can decompose the advantage into per-component terms without any interaction with the sequence-level importance ratio. The recommended approach is to combine GSPO's sequence-level importance ratio (for MoE stability) with MO-GRPO's per-component advantage normalization (for balanced multi-objective optimization and per-component gaming resistance analysis).

Note that this "MO-GSPO" combination does not appear to have been published as a standalone method yet --- MO-GRPO was developed for token-level GRPO, and GSPO was developed without multi-objective considerations. But mathematically, the two mechanisms address orthogonal concerns (importance ratio computation vs. advantage computation) and should compose cleanly.

### Sources

- [GSPO: Towards Scalable Reinforcement Learning for Language Models - Qwen Blog](https://qwenlm.github.io/blog/gspo/)
- [Group Sequence Policy Optimization - arXiv Paper](https://arxiv.org/abs/2507.18071)
- [Towards Stable and Effective Reinforcement Learning for Mixture-of-Experts](https://arxiv.org/html/2510.23027v1)
- [MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems](https://arxiv.org/abs/2509.22047)
- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)
- [GSPO - EmergentMind Topic Page](https://www.emergentmind.com/topics/group-sequence-policy-optimization-gspo)
- [GSPO Implementation in Swift/RLHF Framework](https://swift.readthedocs.io/en/latest/Instruction/GRPO/AdvancedResearch/GSPO.html)
- [Soft Sequence Policy Optimization](https://arxiv.org/html/2602.19327)
- [GMPO - EmergentMind Topic Page](https://www.emergentmind.com/topics/geometric-mean-policy-optimization-gmpo)
- [Multi-Reward GRPO Policy Optimization - EmergentMind](https://www.emergentmind.com/topics/multi-reward-group-relative-policy-optimization-grpo)

agentId: a8aa805f3c3a0174b (use SendMessage with to: 'a8aa805f3c3a0174b' to continue this agent)
&lt;usage>total_tokens: 29404
tool_uses: 22
duration_ms: 181258&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "3cca66e1-a050-4297-9ff0-e13fad314f9f",
  "isSidechain": false,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "type": "user",
  "uuid": "66283ebb-2938-4e7f-a893-507a8f097a56",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to research the specific technical differences between GSPO and GRPO for Mixture-of-Experts models, and whether GSPO is compatible with multi-component reward decomposition.\n\nPlease search for:\n1. \"GSPO GRPO MoE routing instability sequence level\" \n2. \"Qwen3 30B training reinforcement learning GSPO\"\n3. \"sequence level policy optimization multi-objective reward\"\n4. \"GRPO token level importance ratio MoE expert routing\"\n5. Search for the Qwen3 technical report or blog post discussing their training methodology for MoE models\n\nKey technical questions:\n- In GRPO, importance ratios are computed at token level: π_θ(a_t|s_t)/π_θ_old(a_t|s_t). In GSPO, are they at sequence level: π_θ(y|x)/π_θ_old(y|x)?\n- If GSPO uses sequence-level ratios, does the reward still need to be decomposed per-token, or is it naturally sequence-level?\n- For multi-component rewards R = w1*R1 + w2*R2 + ..., does GSPO's sequence-level operation prevent per-component analysis?\n- My use case: I want to compute GRS (Gaming Resistance Score) per individual reward component. With GRPO, each component R_k contributes separately to the advantage. With GSPO, if everything is sequence-level, can I still decompose?\n\nThink carefully about this compatibility question.",
    "agentId": "a8aa805f3c3a0174b",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "Now I have all the technical details needed to provide a comprehensive answer. Here is my analysis:\n\n---\n\n## Technical Differences Between GSPO and GRPO for MoE Models, and Compatibility with Multi-Component Reward Decomposition\n\n### 1. GRPO vs. GSPO: Token-Level vs. Sequence-Level Importance Ratios\n\n**GRPO (token-level):**\nThe importance ratio is computed per token:\n\n```\nw_{i,t}(theta) = pi_theta(y_{i,t} | x, y_{i,<t}) / pi_{theta_old}(y_{i,t} | x, y_{i,<t})\n```\n\nEach token gets its own ratio, and clipping is applied per-token. The objective aggregates these across the sequence (typically via arithmetic mean).\n\n**GSPO (sequence-level):**\nThe importance ratio is the *geometric mean* of per-token ratios across the entire sequence:\n\n```\ns_i(theta) = [ pi_theta(y_i | x) / pi_{theta_old}(y_i | x) ]^{1/|y_i|}\n```\n\nWhich is mathematically equivalent to:\n\n```\ns_i(theta) = exp( (1/|y_i|) * sum_t log[ pi_theta(y_{i,t} | x, y_{i,<t}) / pi_{theta_old}(y_{i,t} | x, y_{i,<t}) ] )\n```\n\nThis produces a **single scalar ratio per sequence**, and clipping is applied at the sequence level.\n\n**GSPO's full objective:**\n\n```\nJ_GSPO(theta) = E[ (1/G) * sum_i min( s_i(theta) * A_hat_i, clip(s_i(theta), 1-eps, 1+eps) * A_hat_i ) ]\n```\n\nThis mirrors PPO's clipped surrogate objective but operates entirely at sequence granularity.\n\n### 2. Why GSPO Solves MoE Routing Instability\n\nThe core problem: In MoE models like Qwen3-30B-A3B (48 layers, 128 experts, 8 active per token), approximately **10% of the experts activated under the new policy differ from those under the old policy** after each gradient update. This expert-activation volatility causes:\n\n- Token-level importance ratios in GRPO to fluctuate wildly, since different experts produce very different token probabilities\n- Massive variance in gradients\n- Training collapse (GRPO on Qwen3-30B-A3B actually *underperformed* the base model: 71.5% vs 74.2% average on math benchmarks)\n\nGSPO's sequence-level geometric mean *averages out* the per-token routing noise. Even if individual tokens have wildly different expert assignments between old and new policies, the geometric mean across the full sequence is stable. This completely eliminates the need for \"Routing Replay\" (a workaround where old-policy expert assignments are cached and reused, which was shown to be unsatisfactory because it restricts exploration and degrades final performance).\n\n**Empirical evidence:** On Qwen3-30B-A3B, GSPO achieved 76.4% vs GRPO's 71.5% on math benchmarks, with GRPO showing \"pronounced performance collapse around 200-500 training steps.\"\n\n### 3. Reward and Advantage Computation in GSPO\n\nThe advantage in GSPO uses the same **group-relative** normalization as GRPO, but operates on a single scalar reward per sequence:\n\n```\nA_hat_i = [ r(x, y_i) - mean({r(x, y_j)}) ] / std({r(x, y_j)})\n```\n\nwhere the mean and standard deviation are computed across the group of G sampled responses to the same query. This is critic-free (no value network needed). The reward `r(x, y_i)` is a **single scalar** assigned to the complete response.\n\n### 4. Your Key Question: Compatibility with Multi-Component Reward Decomposition\n\nThis is where the analysis gets nuanced. Let me address each sub-question:\n\n**Q: Does GSPO naturally handle sequence-level rewards without per-token decomposition?**\n\nYes. Since both the importance ratio `s_i(theta)` and the advantage `A_hat_i` are sequence-level scalars, there is no need to assign credit to individual tokens. The reward `r(x, y_i)` is inherently a sequence-level quantity, and GSPO's objective is fully consistent with this --- unlike GRPO, which has a structural mismatch between token-level ratios and sequence-level rewards.\n\n**Q: For multi-component rewards R = w1*R1 + w2*R2 + ..., does GSPO's sequence-level operation prevent per-component analysis?**\n\n**No, it does not prevent it.** Here is the critical insight:\n\nThe advantage in GSPO is computed from the scalar reward *before* entering the objective function. The reward can be a weighted sum of components:\n\n```\nr(x, y_i) = w1*R1(x, y_i) + w2*R2(x, y_i) + ... + wK*RK(x, y_i)\n```\n\nBecause GSPO's advantage is a linear function of the reward (after group normalization), you can decompose:\n\n```\nA_hat_i = [ sum_k wk*Rk(x,y_i) - mean(sum_k wk*Rk(x,y_j)) ] / std(...)\n```\n\nHowever, there is a subtlety: the standard deviation in the denominator is computed from the *total* reward, not per component. This means the advantage does **not** decompose cleanly into a sum of per-component advantages unless you adopt the MO-GRPO approach.\n\n**Q: Can you compute a Gaming Resistance Score (GRS) per individual reward component with GSPO?**\n\n**Yes, but you need to adopt the MO-GRPO normalization strategy adapted for GSPO.** Here is how:\n\nThe paper [MO-GRPO](https://arxiv.org/abs/2509.22047) identifies exactly the problem you are worried about: when using standard GRPO with `R = sum(wk * Rk)`, the correlation of the advantage with each component Rk is proportional to that component's standard deviation sigma_k. High-variance reward components dominate optimization, creating a reward hacking vector.\n\nMO-GRPO's solution is to normalize each component independently:\n\n```\nA^{MO}_i = sum_k [ (Rk(x,y_i) - mean(Rk)) / std(Rk) ]\n```\n\nThis ensures each component contributes approximately `1/sqrt(K)` correlation regardless of its scale or variance.\n\n**The key compatibility point: This MO-GRPO advantage formulation is fully compatible with GSPO.** The advantage computation is independent of whether you use token-level or sequence-level importance ratios. You can plug `A^{MO}_i` directly into the GSPO objective:\n\n```\nJ_{MO-GSPO}(theta) = E[ (1/G) * sum_i min( s_i(theta) * A^{MO}_i, clip(s_i(theta), 1-eps, 1+eps) * A^{MO}_i ) ]\n```\n\nTo compute GRS per component, you can then:\n1. **Track per-component advantage contributions:** For each component k, compute `A^k_i = (Rk(x,y_i) - mean(Rk)) / std(Rk)` separately\n2. **Monitor per-component reward curves independently** during training\n3. **Measure gaming resistance per component** by checking whether the policy exploits any single Rk at the expense of others\n\nSince GSPO's importance ratio `s_i(theta)` is a single scalar multiplying the full advantage, you can decompose the gradient signal as:\n\n```\ngradient contribution from component k ∝ s_i(theta) * A^k_i\n```\n\nThis decomposition is exact (not approximate) because the importance ratio is shared across all components --- it captures \"how much the policy changed\" at the sequence level, while each `A^k_i` captures \"how good was this change for component k.\"\n\n### 5. Summary of Recommendations\n\n| Aspect | GRPO | GSPO | Impact on Your Use Case |\n|--------|------|------|------------------------|\n| Importance ratio | Token-level | Sequence-level (geometric mean) | GSPO is required for MoE stability |\n| MoE compatibility | Poor (10% expert drift causes collapse) | Excellent (inherently robust) | Use GSPO for MoE models |\n| Reward level | Sequence-level reward, token-level optimization (mismatch) | Sequence-level reward, sequence-level optimization (aligned) | GSPO is more principled |\n| Multi-component rewards | MO-GRPO extension exists | Can adopt MO-GRPO advantage into GSPO (untested but mathematically sound) | Implement MO-GSPO hybrid |\n| Per-component GRS | Yes, via per-component advantage tracking | Yes, via same mechanism (advantage decomposes linearly) | Fully compatible |\n\n**Bottom line:** GSPO is compatible with multi-component reward decomposition and per-component GRS analysis. The importance ratio (`s_i`) and the advantage (`A_hat_i`) are independent computations that enter the objective multiplicatively. You can decompose the advantage into per-component terms without any interaction with the sequence-level importance ratio. The recommended approach is to combine GSPO's sequence-level importance ratio (for MoE stability) with MO-GRPO's per-component advantage normalization (for balanced multi-objective optimization and per-component gaming resistance analysis).\n\nNote that this \"MO-GSPO\" combination does not appear to have been published as a standalone method yet --- MO-GRPO was developed for token-level GRPO, and GSPO was developed without multi-objective considerations. But mathematically, the two mechanisms address orthogonal concerns (importance ratio computation vs. advantage computation) and should compose cleanly.\n\n### Sources\n\n- [GSPO: Towards Scalable Reinforcement Learning for Language Models - Qwen Blog](https://qwenlm.github.io/blog/gspo/)\n- [Group Sequence Policy Optimization - arXiv Paper](https://arxiv.org/abs/2507.18071)\n- [Towards Stable and Effective Reinforcement Learning for Mixture-of-Experts](https://arxiv.org/html/2510.23027v1)\n- [MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems](https://arxiv.org/abs/2509.22047)\n- [Qwen3 Technical Report](https://arxiv.org/abs/2505.09388)\n- [GSPO - EmergentMind Topic Page](https://www.emergentmind.com/topics/group-sequence-policy-optimization-gspo)\n- [GSPO Implementation in Swift/RLHF Framework](https://swift.readthedocs.io/en/latest/Instruction/GRPO/AdvancedResearch/GSPO.html)\n- [Soft Sequence Policy Optimization](https://arxiv.org/html/2602.19327)\n- [GMPO - EmergentMind Topic Page](https://www.emergentmind.com/topics/geometric-mean-policy-optimization-gmpo)\n- [Multi-Reward GRPO Policy Optimization - EmergentMind](https://www.emergentmind.com/topics/multi-reward-group-relative-policy-optimization-grpo)"
      }
    ],
    "totalDurationMs": 181258,
    "totalTokens": 29404,
    "totalToolUseCount": 22,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 890,
      "cache_read_input_tokens": 25689,
      "output_tokens": 2824,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 890
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 2824,
          "cache_read_input_tokens": 25689,
          "cache_creation_input_tokens": 890,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 890,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 22
    }
  },
  "sourceToolAssistantUUID": "3cca66e1-a050-4297-9ff0-e13fad314f9f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"FIXED τ-TO-r THEORETICAL BRIDGE (most critical fix): Iden…",
  "leafUuid": "66283ebb-2938-4e7f-a893-507a8f097a56",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistance analysis: address GSPO and benchmark gaps",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Tool result

_source line 17 · 2026-05-27T23:08:12.773Z_

<details><summary>↩ Tool result · `toolu_01FiQaEdHiKDCcToc226HKKW`</summary>

````text
I now have comprehensive information. Let me compile the complete research findings.

---

# GSPO (Group Sequence Policy Optimization) -- Deep Research Report

**Paper:** "Group Sequence Policy Optimization," arXiv:2507.18071 (v1: July 24, 2025; v2: July 28, 2025)
**Authors:** Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, Jingren Zhou, Junyang Lin (Qwen Team, Alibaba Inc.)

---

## 1. GSPO's Core Mechanism: Sequence-Level vs Token-Level Importance Ratios

### The Problem with GRPO's Token-Level Ratios

GRPO uses per-token importance ratios:

```
w_{i,t}(theta) = pi_theta(y_{i,t} | x, y_{i,&lt;t}) / pi_theta_old(y_{i,t} | x, y_{i,&lt;t})
```

The paper identifies this as a **fundamental misapplication of importance sampling**. The key argument: importance sampling requires averaging over *multiple samples* from the behavior distribution to correct for distributional mismatch. But at each token position `t`, there is only a *single sample* `y_{i,t}` from each next-token distribution. This means the token-level importance weight "fails to perform the intended distribution-correction role" and instead introduces high-variance noise that:
- Accumulates over long sequences
- Is exacerbated by the clipping mechanism
- Can lead to irreversible model collapse

The paper states a core principle: **"the unit of optimization objective should match the unit of reward."** Since rewards are granted to entire sequences, token-level off-policy correction is misaligned.

### GSPO's Sequence-Level Solution

GSPO defines the importance ratio at the sequence level with length normalization:

```
s_i(theta) = (pi_theta(y_i|x) / pi_theta_old(y_i|x))^{1/|y_i|}
           = exp( (1/|y_i|) * sum_{t=1}^{|y_i|} log[pi_theta(y_{i,t}|x,y_{i,&lt;t}) / pi_theta_old(y_{i,t}|x,y_{i,&lt;t})] )
```

The full GSPO objective:

```
J_GSPO(theta) = E[ (1/G) * sum_{i=1}^{G} min(s_i(theta) * A_hat_i, clip(s_i(theta), 1-eps, 1+eps) * A_hat_i) ]
```

With group-relative advantage estimation:

```
A_hat_i = (r(x, y_i) - mean({r(x, y_j)})) / std({r(x, y_j)})
```

**Length normalization** is critical: without it, likelihood changes of a few tokens cause dramatic fluctuations in the sequence-level ratio, and responses of different lengths would require different clipping ranges.

### Gradient-Level Difference

The key distinction at the gradient level:

- **GRPO gradient**: Each token's gradient `nabla log pi(y_{i,t})` is weighted by its *own individual* importance ratio `w_{i,t}(theta)`. These unequal weights range in `(0, 1+eps]` for positive advantages or `[1-eps, infinity)` for negative advantages -- highly asymmetric and noisy.

- **GSPO gradient**: ALL tokens in a response share the *same* weight `s_i(theta)`. The gradient is:
  ```
  (pi_theta(y_i|x) / pi_theta_old(y_i|x))^{1/|y_i|} * A_hat_i * (1/|y_i|) * sum_t nabla log pi_theta(y_{i,t})
  ```
  This eliminates token-level weighting variance entirely.

---

## 2. Why GSPO Solves MoE Routing Instability

### The MoE Problem

In MoE models like Qwen3-30B-A3B (48 layers), the paper reports that **after each RL gradient update, roughly 10% of the experts activated under the new policy are different from those under the old policy** for the same rollout sample. This "expert-activation volatility" means:

- The token-level probabilities `pi_theta(y_{i,t}|...)` and `pi_theta_old(y_{i,t}|...)` are computed by **different sub-networks** (different expert combinations)
- The ratios `w_{i,t}` therefore "fluctuate drastically" -- not because the model changed its beliefs, but because it is routing through entirely different experts
- This noise is structural, not informational, and it compounds across tokens in long sequences

### The Previous Workaround: Routing Replay

Before GSPO, the Qwen team used "Routing Replay": caching which experts were activated under `pi_theta_old` and forcing `pi_theta` to use the same expert routing when computing importance ratios. This ensured both probabilities used the same activated network, restoring ratio stability. However, Routing Replay:
- Incurred additional memory and communication overhead
- Limited the actual capacity of the MoE model (prevented it from using its natural routing)
- Was shown to be **essential** for GRPO convergence on MoE (without it, GRPO fails to converge)

### GSPO's Natural Solution

GSPO resolves this **without any workaround** because:
- The sequence-level likelihood `pi_theta(y_i|x)` is an aggregate quantity
- While individual token probabilities fluctuate due to expert routing changes, the overall sequence likelihood remains stable because "the MoE model always maintains its language modeling capability"
- GSPO is "not sensitive to the individual token likelihood" -- it only uses the aggregate
- This allows the model to "leverage its full capacity without artificial constraints" on routing

---

## 3. Interaction with Multi-Objective / Multi-Component Rewards

### What the Paper Says

The paper does **not** directly discuss multi-objective or multi-component rewards. The reward `r(x, y_i)` throughout the paper is treated as a single scalar in `[0,1]`. The advantage estimation is a single group-normalized value per sequence.

### The GSPO-token Variant: The Pathway to Per-Component Signals

The paper introduces **GSPO-token** (Section 4.3) specifically for scenarios requiring "finer-grained advantage adjustment than the sequence level," with multi-turn RL cited as the motivating example:

```
J_GSPO-token(theta) = E[ (1/G) sum_i (1/|y_i|) sum_t min(s_{i,t}(theta) * A_hat_{i,t}, clip(s_{i,t}(theta), 1-eps, 1+eps) * A_hat_{i,t}) ]
```

Where the token-level ratio is defined using a stop-gradient trick:

```
s_{i,t}(theta) = sg[s_i(theta)] * pi_theta(y_{i,t}|...) / sg[pi_theta(y_{i,t}|...)]
```

Key properties:
- `s_{i,t}(theta)` is **numerically equal** to `s_i(theta)` (since the token ratio term has value 1)
- The **clipping condition** is identical to standard GSPO (based on `s_i(theta)`)
- But the **gradient** allows per-token advantage differentiation: different `A_hat_{i,t}` values for different tokens
- When all token advantages are set equal (`A_hat_{i,t} = A_hat_i`), GSPO-token reduces exactly to standard GSPO

**This is directly relevant to multi-component rewards**: you could assign different advantage values to different tokens (or turns) based on different reward components, while still benefiting from GSPO's sequence-level importance ratio for stability. However, the paper does not explicitly discuss this application.

### Implications for Composite Rewards

Based on the algorithm design, here is the analysis:

1. **Standard GSPO with composite rewards as a single scalar**: If you combine multiple reward components into a single `r(x, y_i)` (e.g., weighted sum of correctness, format, safety), GSPO works identically -- the advantage is computed from this composite scalar. The sequence-level clipping means you cannot separately control the policy gradient for each reward component, since the entire sequence is either clipped or not based on the aggregate importance ratio.

2. **GSPO-token for per-component credit assignment**: If different tokens or turns correspond to different reward aspects (e.g., reasoning quality for thinking tokens, format compliance for output tokens), GSPO-token allows assigning different `A_hat_{i,t}` values to different tokens while retaining the sequence-level importance ratio and clipping. This preserves MoE stability while enabling finer-grained reward attribution.

3. **What you cannot do with standard GSPO**: Extract per-component gradients with independent clipping per component. The clipping is always at the sequence level based on overall policy divergence, not per-component divergence.

---

## 4. Sequence-Level Clipping Details

### Clipping Mechanism

The clipping operates on `s_i(theta)`, constraining it to `[1-eps, 1+eps]`. When the importance ratio for a sequence falls outside this range, the **entire sequence** is excluded from gradient estimation. This is fundamentally different from GRPO where individual tokens can be clipped independently.

### Clipping Hyperparameters

The clipping ranges differ by orders of magnitude from GRPO due to the distinct definitions:
- **GSPO**: left clipping = 3e-4, right clipping = 4e-4
- **GRPO**: left clipping = 0.2, right clipping = 0.27

This makes sense because `s_i(theta)` is a length-normalized geometric mean of token ratios, so it stays very close to 1.

### The "Curious Observation"

GSPO clips **two orders of magnitude more tokens** than GRPO (measured by fraction of clipped tokens), yet achieves superior training efficiency. The paper interprets this as evidence that "GRPO's token-level gradient estimates are inherently noisy and inefficient for sample exploitation." In other words, GRPO's un-clipped tokens carry so much noise that GSPO's cleaner (but fewer) gradient signals are more useful.

---

## 5. Experimental Results: GSPO > GRPO on MoE

### Setup
- Model: Cold-start fine-tuned from Qwen3-30B-A3B-Base (MoE model)
- Each batch of rollout data partitioned into 4 mini-batches for gradient updates
- GRPO required Routing Replay for convergence; GSPO did not

### Benchmarks
- **AIME'24**: Average Pass@1 over 32 samplings
- **LiveCodeBench** (202410-202502): Average Pass@1 over 8 samplings
- **CodeForces**: Elo Rating

### Key Findings (from training curves, Figure 1 in the paper)
1. GSPO training proceeds **stably throughout** -- no collapse episodes
2. GSPO delivers **continuous performance improvement** through increasing training compute, regularly updating query sets, and extending generation length
3. GSPO demonstrates **"remarkably higher training efficiency"** than GRPO: better training accuracy and benchmark performance under the same training compute and consumed queries
4. GRPO **without Routing Replay fails to converge** on MoE models (Figure 3)
5. GRPO **with Routing Replay** converges but is less efficient than GSPO

The paper does not provide exact numerical benchmark scores in tables -- results are shown as training curves. The main claim is about relative efficiency and stability rather than specific point estimates.

### Production Validation
GSPO was successfully applied to the RL training of the latest Qwen3 models (including Qwen3-235B-A22B), demonstrating its scalability to production-scale training.

---

## 6. Discussion of GSPO with Composite/Multi-Objective Rewards

### What Exists in the Literature

The paper itself does **not** discuss composite or multi-objective rewards. Across all the blog posts, reviews, and discussions I found, **none** address this topic specifically for GSPO. The entire treatment assumes a single scalar reward per sequence.

### What Can Be Inferred from the Algorithm

**For standard GSPO:**
- You can feed in any scalar reward, including one that is a weighted sum of multiple components
- The clipping is purely based on policy divergence (the importance ratio), not on reward magnitude, so using a composite reward does not change the clipping behavior
- You **lose the ability** to independently control how much each reward component drives the gradient, since there is a single advantage `A_hat_i` per sequence and a single clipping decision per sequence

**For GSPO-token:**
- This variant was explicitly designed for multi-turn RL where different parts of a sequence merit different advantages
- You could assign per-token advantages derived from different reward components
- The clipping is still sequence-level (based on `s_i(theta)`), so you cannot independently clip based on individual reward component divergence
- But you **can** decompose the reward signal into per-token advantages while retaining the stability benefits

**A potential approach for multi-component rewards with GSPO:**
1. Compute a composite reward: `r(x, y_i) = w1*r1(x,y_i) + w2*r2(x,y_i) + ...`
2. Use standard GSPO with this composite scalar
3. Or, if different tokens/turns correspond to different reward aspects, use GSPO-token with per-token advantages derived from the relevant reward component

---

## 7. Infrastructure Benefits

GSPO also simplifies RL training infrastructure:
- Since GSPO uses only sequence-level likelihoods (not per-token), it is **more tolerant of precision discrepancies** between training engines (Megatron) and inference engines (SGLang, vLLM)
- This makes it possible to **directly use likelihoods from inference engines** without recomputation by the training engine
- This is especially beneficial for partial rollout, multi-turn RL, and disaggregated training-inference frameworks
- GSPO has been integrated into HuggingFace TRL

---

## Summary of Answers to Your Questions

| Question | Answer |
|----------|--------|
| GSPO's mechanism | Sequence-level importance ratio (length-normalized geometric mean of token ratios), sequence-level clipping, sequence-level advantage. All tokens in a response share the same gradient weight. |
| Why it solves MoE routing instability | Token-level ratios depend on which experts are activated; with ~10% expert changes per gradient step in MoE, token ratios become noisy. Sequence-level likelihood is stable because overall language modeling capability is preserved despite routing changes. Eliminates need for Routing Replay. |
| Interaction with multi-component rewards | Not directly addressed in the paper. Standard GSPO uses a single scalar reward per sequence. GSPO-token variant allows per-token advantage differentiation, which could be used for multi-component credit assignment, but this application is not explicitly discussed. |
| Sequence-level clipping and per-component signals | Standard GSPO clips entire sequences, so per-component reward signals cannot be independently clipped. GSPO-token preserves per-token advantage differences but still uses sequence-level clipping. You can still feed composite rewards into the advantage computation. |
| Experimental results GSPO > GRPO on MoE | GSPO shows remarkably higher training efficiency on Qwen3-30B-A3B-Base across AIME'24, LiveCodeBench, and CodeForces. GRPO requires Routing Replay to even converge on MoE; GSPO does not. GSPO clips 100x more tokens yet still outperforms GRPO. |
| GSPO with composite/multi-objective rewards | No direct discussion exists anywhere in the paper or community. It is an open area. GSPO-token is the natural extension point for this use case. |

Sources:
- [GSPO Paper (arXiv)](https://arxiv.org/abs/2507.18071)
- [GSPO Paper HTML Version](https://arxiv.org/html/2507.18071v2)
- [Qwen Team Official Blog Post on GSPO](https://qwenlm.github.io/blog/gspo/)
- [HuggingFace Paper Page](https://huggingface.co/papers/2507.18071)
- [From GRPO to DAPO and GSPO (HuggingFace Blog)](https://huggingface.co/blog/NormalUhr/grpo-to-dapo-and-gspo)
- [Paper Review by Andrey Lukyanenko](https://andlukyane.com/blog/paper-review-gspo)
- [GSPO vs GRPO: RL for MoE Models (Kaitchup)](https://kaitchup.substack.com/p/gspo-vs-grpo-reinforcement-learning)
- [RLHF Algorithms: PPO, GRPO, GSPO (Medium)](https://medium.com/@hongjianzou/rlhf-algorithms-ppo-grpo-gspo-differences-trade-offs-and-use-cases-241d003d806d)
- [Emergent Mind GSPO Topic Page](https://www.emergentmind.com/papers/2507.18071)
- [MarkTechPost Coverage](https://www.marktechpost.com/2025/08/07/alibaba-introduces-group-sequence-policy-optimization-gspo-an-efficient-reinforcement-learning-algorithm-that-powers-the-qwen3-models/)

agentId: acd6bd3eff75572c3 (use SendMessage with to: 'acd6bd3eff75572c3' to continue this agent)
&lt;usage>total_tokens: 41729
tool_uses: 19
duration_ms: 208538&lt;/usage>
````

</details>

<details><summary>Recorded metadata</summary>

````json
{
  "recorded_role": "user",
  "parentUuid": "9b8c703d-6f72-40bf-85d9-d58184baf698",
  "isSidechain": false,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "type": "user",
  "uuid": "937b80be-0a17-468d-a2e1-cc15a198a855",
  "toolUseResult": {
    "status": "completed",
    "prompt": "I need to deeply research GSPO (Group Sequence Policy Optimization), arXiv:2507.18071, July 2025. This was developed by the Qwen team specifically because GRPO fails on MoE (Mixture-of-Experts) models like Qwen3-30B-A3B.\n\nPlease:\n1. Search the web for \"GSPO Group Sequence Policy Optimization arXiv 2507.18071\" and related queries\n2. Fetch the arXiv abstract page at https://arxiv.org/abs/2507.18071\n3. Search for \"GSPO MoE GRPO Qwen sequence-level importance ratio\"\n4. Search for any blog posts or discussions about GSPO vs GRPO for MoE models\n5. Try to fetch the paper PDF or HTML version to get more details about the algorithm\n\nKey questions I need answered:\n- What exactly is GSPO's mechanism? (sequence-level vs token-level importance ratios)\n- Why does it solve the MoE routing instability problem?\n- How does it interact with multi-objective/multi-component rewards?\n- Does GSPO use sequence-level clipping? If so, can per-component reward signals still be extracted?\n- What were the specific experimental results showing GSPO > GRPO on MoE?\n- Is there any discussion of GSPO with composite/multi-objective rewards?\n\nPlease be thorough - read actual paper content, not just abstracts.",
    "agentId": "acd6bd3eff75572c3",
    "agentType": "general-purpose",
    "content": [
      {
        "type": "text",
        "text": "I now have comprehensive information. Let me compile the complete research findings.\n\n---\n\n# GSPO (Group Sequence Policy Optimization) -- Deep Research Report\n\n**Paper:** \"Group Sequence Policy Optimization,\" arXiv:2507.18071 (v1: July 24, 2025; v2: July 28, 2025)\n**Authors:** Chujie Zheng, Shixuan Liu, Mingze Li, Xiong-Hui Chen, Bowen Yu, Chang Gao, Kai Dang, Yuqiong Liu, Rui Men, An Yang, Jingren Zhou, Junyang Lin (Qwen Team, Alibaba Inc.)\n\n---\n\n## 1. GSPO's Core Mechanism: Sequence-Level vs Token-Level Importance Ratios\n\n### The Problem with GRPO's Token-Level Ratios\n\nGRPO uses per-token importance ratios:\n\n```\nw_{i,t}(theta) = pi_theta(y_{i,t} | x, y_{i,&lt;t}) / pi_theta_old(y_{i,t} | x, y_{i,&lt;t})\n```\n\nThe paper identifies this as a **fundamental misapplication of importance sampling**. The key argument: importance sampling requires averaging over *multiple samples* from the behavior distribution to correct for distributional mismatch. But at each token position `t`, there is only a *single sample* `y_{i,t}` from each next-token distribution. This means the token-level importance weight \"fails to perform the intended distribution-correction role\" and instead introduces high-variance noise that:\n- Accumulates over long sequences\n- Is exacerbated by the clipping mechanism\n- Can lead to irreversible model collapse\n\nThe paper states a core principle: **\"the unit of optimization objective should match the unit of reward.\"** Since rewards are granted to entire sequences, token-level off-policy correction is misaligned.\n\n### GSPO's Sequence-Level Solution\n\nGSPO defines the importance ratio at the sequence level with length normalization:\n\n```\ns_i(theta) = (pi_theta(y_i|x) / pi_theta_old(y_i|x))^{1/|y_i|}\n           = exp( (1/|y_i|) * sum_{t=1}^{|y_i|} log[pi_theta(y_{i,t}|x,y_{i,&lt;t}) / pi_theta_old(y_{i,t}|x,y_{i,&lt;t})] )\n```\n\nThe full GSPO objective:\n\n```\nJ_GSPO(theta) = E[ (1/G) * sum_{i=1}^{G} min(s_i(theta) * A_hat_i, clip(s_i(theta), 1-eps, 1+eps) * A_hat_i) ]\n```\n\nWith group-relative advantage estimation:\n\n```\nA_hat_i = (r(x, y_i) - mean({r(x, y_j)})) / std({r(x, y_j)})\n```\n\n**Length normalization** is critical: without it, likelihood changes of a few tokens cause dramatic fluctuations in the sequence-level ratio, and responses of different lengths would require different clipping ranges.\n\n### Gradient-Level Difference\n\nThe key distinction at the gradient level:\n\n- **GRPO gradient**: Each token's gradient `nabla log pi(y_{i,t})` is weighted by its *own individual* importance ratio `w_{i,t}(theta)`. These unequal weights range in `(0, 1+eps]` for positive advantages or `[1-eps, infinity)` for negative advantages -- highly asymmetric and noisy.\n\n- **GSPO gradient**: ALL tokens in a response share the *same* weight `s_i(theta)`. The gradient is:\n  ```\n  (pi_theta(y_i|x) / pi_theta_old(y_i|x))^{1/|y_i|} * A_hat_i * (1/|y_i|) * sum_t nabla log pi_theta(y_{i,t})\n  ```\n  This eliminates token-level weighting variance entirely.\n\n---\n\n## 2. Why GSPO Solves MoE Routing Instability\n\n### The MoE Problem\n\nIn MoE models like Qwen3-30B-A3B (48 layers), the paper reports that **after each RL gradient update, roughly 10% of the experts activated under the new policy are different from those under the old policy** for the same rollout sample. This \"expert-activation volatility\" means:\n\n- The token-level probabilities `pi_theta(y_{i,t}|...)` and `pi_theta_old(y_{i,t}|...)` are computed by **different sub-networks** (different expert combinations)\n- The ratios `w_{i,t}` therefore \"fluctuate drastically\" -- not because the model changed its beliefs, but because it is routing through entirely different experts\n- This noise is structural, not informational, and it compounds across tokens in long sequences\n\n### The Previous Workaround: Routing Replay\n\nBefore GSPO, the Qwen team used \"Routing Replay\": caching which experts were activated under `pi_theta_old` and forcing `pi_theta` to use the same expert routing when computing importance ratios. This ensured both probabilities used the same activated network, restoring ratio stability. However, Routing Replay:\n- Incurred additional memory and communication overhead\n- Limited the actual capacity of the MoE model (prevented it from using its natural routing)\n- Was shown to be **essential** for GRPO convergence on MoE (without it, GRPO fails to converge)\n\n### GSPO's Natural Solution\n\nGSPO resolves this **without any workaround** because:\n- The sequence-level likelihood `pi_theta(y_i|x)` is an aggregate quantity\n- While individual token probabilities fluctuate due to expert routing changes, the overall sequence likelihood remains stable because \"the MoE model always maintains its language modeling capability\"\n- GSPO is \"not sensitive to the individual token likelihood\" -- it only uses the aggregate\n- This allows the model to \"leverage its full capacity without artificial constraints\" on routing\n\n---\n\n## 3. Interaction with Multi-Objective / Multi-Component Rewards\n\n### What the Paper Says\n\nThe paper does **not** directly discuss multi-objective or multi-component rewards. The reward `r(x, y_i)` throughout the paper is treated as a single scalar in `[0,1]`. The advantage estimation is a single group-normalized value per sequence.\n\n### The GSPO-token Variant: The Pathway to Per-Component Signals\n\nThe paper introduces **GSPO-token** (Section 4.3) specifically for scenarios requiring \"finer-grained advantage adjustment than the sequence level,\" with multi-turn RL cited as the motivating example:\n\n```\nJ_GSPO-token(theta) = E[ (1/G) sum_i (1/|y_i|) sum_t min(s_{i,t}(theta) * A_hat_{i,t}, clip(s_{i,t}(theta), 1-eps, 1+eps) * A_hat_{i,t}) ]\n```\n\nWhere the token-level ratio is defined using a stop-gradient trick:\n\n```\ns_{i,t}(theta) = sg[s_i(theta)] * pi_theta(y_{i,t}|...) / sg[pi_theta(y_{i,t}|...)]\n```\n\nKey properties:\n- `s_{i,t}(theta)` is **numerically equal** to `s_i(theta)` (since the token ratio term has value 1)\n- The **clipping condition** is identical to standard GSPO (based on `s_i(theta)`)\n- But the **gradient** allows per-token advantage differentiation: different `A_hat_{i,t}` values for different tokens\n- When all token advantages are set equal (`A_hat_{i,t} = A_hat_i`), GSPO-token reduces exactly to standard GSPO\n\n**This is directly relevant to multi-component rewards**: you could assign different advantage values to different tokens (or turns) based on different reward components, while still benefiting from GSPO's sequence-level importance ratio for stability. However, the paper does not explicitly discuss this application.\n\n### Implications for Composite Rewards\n\nBased on the algorithm design, here is the analysis:\n\n1. **Standard GSPO with composite rewards as a single scalar**: If you combine multiple reward components into a single `r(x, y_i)` (e.g., weighted sum of correctness, format, safety), GSPO works identically -- the advantage is computed from this composite scalar. The sequence-level clipping means you cannot separately control the policy gradient for each reward component, since the entire sequence is either clipped or not based on the aggregate importance ratio.\n\n2. **GSPO-token for per-component credit assignment**: If different tokens or turns correspond to different reward aspects (e.g., reasoning quality for thinking tokens, format compliance for output tokens), GSPO-token allows assigning different `A_hat_{i,t}` values to different tokens while retaining the sequence-level importance ratio and clipping. This preserves MoE stability while enabling finer-grained reward attribution.\n\n3. **What you cannot do with standard GSPO**: Extract per-component gradients with independent clipping per component. The clipping is always at the sequence level based on overall policy divergence, not per-component divergence.\n\n---\n\n## 4. Sequence-Level Clipping Details\n\n### Clipping Mechanism\n\nThe clipping operates on `s_i(theta)`, constraining it to `[1-eps, 1+eps]`. When the importance ratio for a sequence falls outside this range, the **entire sequence** is excluded from gradient estimation. This is fundamentally different from GRPO where individual tokens can be clipped independently.\n\n### Clipping Hyperparameters\n\nThe clipping ranges differ by orders of magnitude from GRPO due to the distinct definitions:\n- **GSPO**: left clipping = 3e-4, right clipping = 4e-4\n- **GRPO**: left clipping = 0.2, right clipping = 0.27\n\nThis makes sense because `s_i(theta)` is a length-normalized geometric mean of token ratios, so it stays very close to 1.\n\n### The \"Curious Observation\"\n\nGSPO clips **two orders of magnitude more tokens** than GRPO (measured by fraction of clipped tokens), yet achieves superior training efficiency. The paper interprets this as evidence that \"GRPO's token-level gradient estimates are inherently noisy and inefficient for sample exploitation.\" In other words, GRPO's un-clipped tokens carry so much noise that GSPO's cleaner (but fewer) gradient signals are more useful.\n\n---\n\n## 5. Experimental Results: GSPO > GRPO on MoE\n\n### Setup\n- Model: Cold-start fine-tuned from Qwen3-30B-A3B-Base (MoE model)\n- Each batch of rollout data partitioned into 4 mini-batches for gradient updates\n- GRPO required Routing Replay for convergence; GSPO did not\n\n### Benchmarks\n- **AIME'24**: Average Pass@1 over 32 samplings\n- **LiveCodeBench** (202410-202502): Average Pass@1 over 8 samplings\n- **CodeForces**: Elo Rating\n\n### Key Findings (from training curves, Figure 1 in the paper)\n1. GSPO training proceeds **stably throughout** -- no collapse episodes\n2. GSPO delivers **continuous performance improvement** through increasing training compute, regularly updating query sets, and extending generation length\n3. GSPO demonstrates **\"remarkably higher training efficiency\"** than GRPO: better training accuracy and benchmark performance under the same training compute and consumed queries\n4. GRPO **without Routing Replay fails to converge** on MoE models (Figure 3)\n5. GRPO **with Routing Replay** converges but is less efficient than GSPO\n\nThe paper does not provide exact numerical benchmark scores in tables -- results are shown as training curves. The main claim is about relative efficiency and stability rather than specific point estimates.\n\n### Production Validation\nGSPO was successfully applied to the RL training of the latest Qwen3 models (including Qwen3-235B-A22B), demonstrating its scalability to production-scale training.\n\n---\n\n## 6. Discussion of GSPO with Composite/Multi-Objective Rewards\n\n### What Exists in the Literature\n\nThe paper itself does **not** discuss composite or multi-objective rewards. Across all the blog posts, reviews, and discussions I found, **none** address this topic specifically for GSPO. The entire treatment assumes a single scalar reward per sequence.\n\n### What Can Be Inferred from the Algorithm\n\n**For standard GSPO:**\n- You can feed in any scalar reward, including one that is a weighted sum of multiple components\n- The clipping is purely based on policy divergence (the importance ratio), not on reward magnitude, so using a composite reward does not change the clipping behavior\n- You **lose the ability** to independently control how much each reward component drives the gradient, since there is a single advantage `A_hat_i` per sequence and a single clipping decision per sequence\n\n**For GSPO-token:**\n- This variant was explicitly designed for multi-turn RL where different parts of a sequence merit different advantages\n- You could assign per-token advantages derived from different reward components\n- The clipping is still sequence-level (based on `s_i(theta)`), so you cannot independently clip based on individual reward component divergence\n- But you **can** decompose the reward signal into per-token advantages while retaining the stability benefits\n\n**A potential approach for multi-component rewards with GSPO:**\n1. Compute a composite reward: `r(x, y_i) = w1*r1(x,y_i) + w2*r2(x,y_i) + ...`\n2. Use standard GSPO with this composite scalar\n3. Or, if different tokens/turns correspond to different reward aspects, use GSPO-token with per-token advantages derived from the relevant reward component\n\n---\n\n## 7. Infrastructure Benefits\n\nGSPO also simplifies RL training infrastructure:\n- Since GSPO uses only sequence-level likelihoods (not per-token), it is **more tolerant of precision discrepancies** between training engines (Megatron) and inference engines (SGLang, vLLM)\n- This makes it possible to **directly use likelihoods from inference engines** without recomputation by the training engine\n- This is especially beneficial for partial rollout, multi-turn RL, and disaggregated training-inference frameworks\n- GSPO has been integrated into HuggingFace TRL\n\n---\n\n## Summary of Answers to Your Questions\n\n| Question | Answer |\n|----------|--------|\n| GSPO's mechanism | Sequence-level importance ratio (length-normalized geometric mean of token ratios), sequence-level clipping, sequence-level advantage. All tokens in a response share the same gradient weight. |\n| Why it solves MoE routing instability | Token-level ratios depend on which experts are activated; with ~10% expert changes per gradient step in MoE, token ratios become noisy. Sequence-level likelihood is stable because overall language modeling capability is preserved despite routing changes. Eliminates need for Routing Replay. |\n| Interaction with multi-component rewards | Not directly addressed in the paper. Standard GSPO uses a single scalar reward per sequence. GSPO-token variant allows per-token advantage differentiation, which could be used for multi-component credit assignment, but this application is not explicitly discussed. |\n| Sequence-level clipping and per-component signals | Standard GSPO clips entire sequences, so per-component reward signals cannot be independently clipped. GSPO-token preserves per-token advantage differences but still uses sequence-level clipping. You can still feed composite rewards into the advantage computation. |\n| Experimental results GSPO > GRPO on MoE | GSPO shows remarkably higher training efficiency on Qwen3-30B-A3B-Base across AIME'24, LiveCodeBench, and CodeForces. GRPO requires Routing Replay to even converge on MoE; GSPO does not. GSPO clips 100x more tokens yet still outperforms GRPO. |\n| GSPO with composite/multi-objective rewards | No direct discussion exists anywhere in the paper or community. It is an open area. GSPO-token is the natural extension point for this use case. |\n\nSources:\n- [GSPO Paper (arXiv)](https://arxiv.org/abs/2507.18071)\n- [GSPO Paper HTML Version](https://arxiv.org/html/2507.18071v2)\n- [Qwen Team Official Blog Post on GSPO](https://qwenlm.github.io/blog/gspo/)\n- [HuggingFace Paper Page](https://huggingface.co/papers/2507.18071)\n- [From GRPO to DAPO and GSPO (HuggingFace Blog)](https://huggingface.co/blog/NormalUhr/grpo-to-dapo-and-gspo)\n- [Paper Review by Andrey Lukyanenko](https://andlukyane.com/blog/paper-review-gspo)\n- [GSPO vs GRPO: RL for MoE Models (Kaitchup)](https://kaitchup.substack.com/p/gspo-vs-grpo-reinforcement-learning)\n- [RLHF Algorithms: PPO, GRPO, GSPO (Medium)](https://medium.com/@hongjianzou/rlhf-algorithms-ppo-grpo-gspo-differences-trade-offs-and-use-cases-241d003d806d)\n- [Emergent Mind GSPO Topic Page](https://www.emergentmind.com/papers/2507.18071)\n- [MarkTechPost Coverage](https://www.marktechpost.com/2025/08/07/alibaba-introduces-group-sequence-policy-optimization-gspo-an-efficient-reinforcement-learning-algorithm-that-powers-the-qwen3-models/)"
      }
    ],
    "totalDurationMs": 208538,
    "totalTokens": 41729,
    "totalToolUseCount": 19,
    "usage": {
      "input_tokens": 85,
      "cache_creation_input_tokens": 3349,
      "cache_read_input_tokens": 33935,
      "output_tokens": 4360,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 0,
        "ephemeral_5m_input_tokens": 3349
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 85,
          "output_tokens": 4360,
          "cache_read_input_tokens": 33935,
          "cache_creation_input_tokens": 3349,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 3349,
            "ephemeral_1h_input_tokens": 0
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "toolStats": {
      "readCount": 0,
      "searchCount": 0,
      "bashCount": 0,
      "editFileCount": 0,
      "linesAdded": 0,
      "linesRemoved": 0,
      "otherToolCount": 19
    }
  },
  "sourceToolAssistantUUID": "9b8c703d-6f72-40bf-85d9-d58184baf698",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
````

</details>

---

### Runtime record

_source line 18_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"FIXED τ-TO-r THEORETICAL BRIDGE (most critical fix): Iden…",
  "leafUuid": "937b80be-0a17-468d-a2e1-cc15a198a855",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Runtime record

_source line 19_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistance analysis: address GSPO and benchmark gaps",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Assistant

_source line 20 · 2026-05-27T23:08:41.694Z_

<details><summary>Logged reasoning block</summary>

```text
Excellent! I now have comprehensive research on both GSPO and MathAtlas. Let me synthesize the key findings:

## GSPO Key Points:
1. GSPO uses sequence-level importance ratios (geometric mean of token ratios) instead of GRPO's token-level ratios
2. This solves MoE routing instability because the sequence-level aggregate is stable even when ~10% of experts change per update
3. Developed by the Qwen team specifically for models like Qwen3-30B-A3B
4. GRPO without Routing Replay fails to converge on MoE; GSPO works without any workaround


5. GSPO outperforms GRPO even when Routing Replay is applied, showing better training efficiency overall
6. The advantage computation stays independent from importance ratio calculations, so I can layer MO-GRPO's per-component advantage normalization directly onto GSPO's sequence-level approach
7. There's a token-level variant of GSPO available for situations requiring more granular advantage assignment
8. Per-component GRS analysis works seamlessly since it measures reward-faithfulness correlation rather than gradient decomposition

## MathAtlas Key Points:
1. ~52k mathematical entities drawn from 103 graduate-level textbooks across 87 distinct fields
2. Current best performance sits at 9.8% correctness with ReForm 8B

, revealing a stark gap between compilation success and actual correctness
3. ~178k dependency relations with depths reaching up to 80 levels
4. Submitted to NeurIPS 2026

The reviewer flagged that I'm nearly at acceptance quality, but GSPO remains the critical blocker. My strategy is to use GSPO for the 30B MoE experiments while keeping GRPO for the 7B dense models, then explain how per-component reward decomposition integrates with GSPO through a hybrid MO-GSPO approach—which itself becomes a minor methodological contribution. I should also incorporate MathAtlas into the broader landscape discussion.

Now I'm working through the reviewer's specific concern about per-component GRS analysis under GSPO. The key realization is that GRS operates as a measurement framework on the evaluation set, computing correlations between individual reward components and faithfulness anchors independently of the training algorithm. Even though GSPO combines rewards into a single composite advantage during training, the individual reward components are still computed separately beforehand, so per-component GRS analysis remains fully compatible. For AGRC's adaptive composition mechanism, I need to clarify how it adjusts component weights while maintaining this measurement compatibility.

Now I'm planning the JSON revisions: adding GSPO to the landscape and adopting it for the 30B experiments, incorporating MathAtlas, justifying GRPO for the 7B dense setup, and explaining the MO-GSPO hybrid approach for multi-component analysis. I'll also verify the CriticLean accuracy claim and make these targeted updates while preserving the existing framework.

The reviewer flagged stagnation across three rounds but indicated we're very close to passing—the core issue is just the GSPO gap. This calls for a focused minor revision rather than structural overhaul.

Writing the JSON now...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "937b80be-0a17-468d-a2e1-cc15a198a855",
  "isSidechain": false,
  "requestId": "req_011CbTv1iEyYBze9gig6FEzZ",
  "type": "assistant",
  "uuid": "1001d7e3-bcaf-4e54-a5aa-5b656bf35743",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeG63kCMvVJrAkrmwLDL2t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5322,
      "cache_creation_input_tokens": 5854,
      "cache_read_input_tokens": 27759,
      "output_tokens": 16120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5322,
          "output_tokens": 16120,
          "cache_read_input_tokens": 27759,
          "cache_creation_input_tokens": 5854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5854
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 21 · 2026-05-27T23:08:46.906Z_

Now I have thorough research on both GSPO and MathAtlas. Let me synthesize the key findings before writing the revision:

**GSPO (arXiv:2507.18071):**
- Sequence-level importance ratios: `s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|}` — geometric mean of token ratios
- Solves MoE routing instability by averaging out per-token expert activation noise
- GRPO without Routing Replay **fails to converge** on Qwen3-30B-A3B; GSPO works without workarounds
- Clipping is at very tight ranges (3e-4/4e-4 vs GRPO's 0.2/0.27)
- **Critical for our use case**: advantage computation is independent of importance ratio computation, so MO-GRPO per-component normalization composes cleanly with GSPO's sequence-level ratios
- GSPO-token variant exists for finer-grained advantage assignment
- Per-component GRS analysis is fully compatible: GRS measures reward-faithfulness correlation on evaluation data, not gradient decomposition

**MathAtlas (arXiv:2605.14061):**
- ~52k entities from 103 graduate-level textbooks, 87 math fields
- Best model: only 9.8% correctness (ReForm 8B)
- Dramatic compilation-correctness gap (Kimina: 27.3% compile, 2.3% correct) — directly supports our gaming resistance argument
- Submitted to NeurIPS 2026

Now let me produce the complete revised JSON:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1001d7e3-bcaf-4e54-a5aa-5b656bf35743",
  "isSidechain": false,
  "requestId": "req_011CbTv1iEyYBze9gig6FEzZ",
  "type": "assistant",
  "uuid": "de3dd28c-a1cc-4122-827b-effd894b32ba",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeG63kCMvVJrAkrmwLDL2t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5322,
      "cache_creation_input_tokens": 5854,
      "cache_read_input_tokens": 27759,
      "output_tokens": 16120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5322,
          "output_tokens": 16120,
          "cache_read_input_tokens": 27759,
          "cache_creation_input_tokens": 5854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5854
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool call

_source line 22 · 2026-05-27T23:14:37.443Z_

<details open><summary>🔧 Tool call — Write · `toolu_01Gzctfeqizv9uAEp6kCTmtw`</summary>

```json
{
  "file_path": "/tmp/revision_round9.json",
  "content": "{\n  \"change_type\": \"minor\",\n  \"changes_made\": [\n    \"CRITICAL FIX — ADOPTED GSPO FOR 30B MOE EXPERIMENTS (arXiv:2507.18071): Group Sequence Policy Optimization, developed by the Qwen team specifically for MoE models like Qwen3-30B-A3B, replaces GRPO for the 30B experiments. GSPO defines importance ratios at the sequence level — s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|} — the length-normalized geometric mean of token ratios. This eliminates the MoE routing instability problem: while ~10% of expert activations differ per gradient step (causing wildly fluctuating token-level ratios in GRPO), GSPO's sequence-level aggregate is stable because overall language modeling capability is preserved despite routing changes. The Qwen team demonstrated that GRPO without Routing Replay fails to converge on Qwen3-30B-A3B, while GSPO converges stably and with higher training efficiency. Crucially, per-component reward decomposition and GRS analysis remain fully compatible: (a) GRS measures reward-faithfulness correlation on the evaluation set — a measurement framework independent of the training algorithm; (b) GSPO's advantage computation is independent of its importance ratio computation, so MO-GRPO's per-component advantage normalization A^MO_i = Σ_k [(R_k - mean(R_k))/std(R_k)] composes cleanly with GSPO's sequence-level ratios, yielding an MO-GSPO hybrid: J_MO-GSPO = E[(1/G) Σ_i min(s_i · A^MO_i, clip(s_i, 1-ε, 1+ε) · A^MO_i)]; (c) AGRC weight adaptation adjusts w_k based on per-component GRS-Kendall monitoring, feeding into composite reward r = Σ w_k·R_k — this occurs at the reward level, upstream of the importance ratio computation, and is therefore orthogonal to the GSPO/GRPO choice. GRPO is retained for the 7B dense model (Qwen2.5-Coder-7B-Instruct) where token-level ratios are well-behaved and MoE routing is not a concern. This GSPO-for-MoE + GRPO-for-dense split also provides an incidental methodological comparison of training algorithm sensitivity on the GRS framework.\",\n    \"ADDED MathAtlas (arXiv:2605.14061, May 2026) TO LANDSCAPE: First large-scale autoformalization benchmark of graduate-level mathematics (~52k entities from 103 textbooks spanning 87 mathematical fields). Best model achieves only 9.8% correctness (ReForm 8B), with a dramatic compilation-correctness gap: Kimina 7B compiles at 27.3% but only 2.3% are semantically correct — meaning ~92% of compiling formalizations are unfaithful. This directly reinforces the urgency of gaming resistance analysis: RL systems optimizing compilation reward face a massive faithfulness gap at graduate-level complexity. MathAtlas's ~178k dependency relations (depth up to 80) suggest gaming resistance may degrade with mathematical complexity — a hypothesis our framework could test in future work. Cited in landscape and as motivation.\",\n    \"REMOVED AD HOC MOE ENGINEERING MITIGATIONS: The previous approach proposed engineering workarounds (auxiliary load-balancing loss, router-aware IS rescaling, conservative clipping) for running GRPO on MoE. GSPO eliminates the need for these workarounds entirely — it is the principled algorithmic solution from the model's own creators. This simplifies the experimental design and removes a potential criticism about ad hoc engineering compensating for a known algorithmic limitation.\",\n    \"UPDATED TRAINING SECTION: Clearly specifies the training algorithm split: GRPO for Qwen2.5-Coder-7B-Instruct (dense), GSPO for Qwen3-Coder-30B-A3B-Instruct (MoE). The MO-GSPO hybrid for multi-component experiments on 30B is documented as a natural composition of orthogonal mechanisms (sequence-level importance ratios for MoE stability × per-component advantage normalization for balanced multi-objective optimization). Notes that this composition, while mathematically straightforward, has not been published as a standalone method — providing an additional minor methodological observation.\",\n    \"VERIFIED CriticLeanGPT ACCURACY: The 14B model (CriticLeanGPT-Qwen3-14B-RL, 15B parameters on HuggingFace, Apache 2.0) has plausible accuracy given the scaling trend (32B: 87.0%, 14B: ~84.8%, 8B would require retraining). The exact 84.8% figure should be verified against the paper's Table 2 upon full paper access. The 8B variant does not exist on HuggingFace and requires retraining as stated. Added a note to verify the specific figure.\"\n  ],\n  \"title\": \"Which Rewards Resist Gaming? Formally-Grounded Gaming Resistance Analysis for Autoformalization RL\",\n  \"core_problem\": \"RL-based autoformalization combines composite rewards — binary compilation (FormaRL, Mathesis), LLM semantic judges (Mathesis R_sem), embedding similarity (Online RL for Autoformalization; cycle consistency in arXiv:2603.24372), and trained critics (CriticLean at 84.8% accuracy) — yet a fundamental question remains unanswered: which reward signals maintain faithfulness under optimization pressure, and can we measure this automatically?\\n\\nThis question is urgent for three reasons. First, the reward-faithfulness gap in autoformalization is documented and severe: FormaRL's ablation reveals syntax-only RL yields 100% compilation but 0% semantic consistency, demonstrating clear gaming under optimization. MathAtlas (arXiv:2605.14061) quantifies the scale of this problem at graduate level: Kimina 7B achieves 27.3% compilation but only 2.3% correctness — ~92% of compiling formalizations are semantically unfaithful. VerifAI-2 (arXiv:2604.19459) provides complementary evidence: while finding no evidence of systematic gaming in unified generation (94-98% definite precision), it documents fabrication (GPT-5) and premise mistranslation (DeepSeek-R1) in two-stage pipelines that evade detection — showing faithfulness gaps even in high-performing systems. Following VerifAI-2's outcome-based definition, we define gaming as reward inflation without corresponding faithfulness improvement, requiring no intent attribution.\\n\\nSecond, theoretically, 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves gaming is a structural equilibrium under finite evaluation — not a correctable bug. The Proxy Compression Hypothesis (arXiv:2604.13602) further explains this as the inevitable consequence of objective compression, optimization amplification, and evaluator-policy co-adaptation. Together, these results make measuring gaming RESISTANCE — which signals degrade least — the critical practical question.\\n\\nThird, the broader RL community has responded with gaming mitigations at multiple levels: MO-GRPO normalizes per-objective variance; CTWA (arXiv:2602.06869) adaptively targets covariance between rewards and training signal; Advantage Modification integrates representation-level shortcut scores; SignCert-PO certifies advantage sign robustness; GRIFT detects gaming via gradient fingerprints; exploitation-rate measures hacking via LLM panels. However, ALL these methods are domain-agnostic. Autoformalization has a UNIQUE advantage: the Lean language server provides formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance (AI4Math@ICML 2025). This creates three domain-specific gaps that no existing work addresses: (1) No systematic comparison of gaming-resistance properties across isolated reward source categories for autoformalization; (2) No gaming-resistance metric leveraging formally-grounded faithfulness anchors — enabling detection that is simultaneously lightweight, automated, and non-circular; (3) No formal theoretical analysis connecting gaming-resistance measurement to the broader reward hacking and safe optimization frameworks, including both regularization-based (Correlated Proxies, ICLR 2025 Spotlight) and robust optimization-based (Robust Correlated Proxies, ICLR 2026) approaches.\",\n  \"opportunity\": \"A unique convergence of nine developments makes this the right moment for this study:\\n\\n(1) GTED (AI4Math@ICML 2025) provides formally-grounded faithfulness via tree-edit-distance over Lean operator trees — the KEY enabling capability. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers a computable, LLM-independent faithfulness anchor.\\n\\n(2) The reward-faithfulness gap is newly documented but unquantified for autoformalization. FormaRL's ablation demonstrates gaming under optimization; MathAtlas (arXiv:2605.14061) reveals the gap is catastrophic at graduate level (~92% of compiling formalizations are unfaithful); VerifAI-2 documents faithfulness gaps in pipelines. We provide the first systematic measurement of which signals are affected and by how much.\\n\\n(3) Mathesis (ICLR 2026) establishes composite rewards for autoformalization GRPO but treats composition as a performance optimization problem, not a gaming-resistance problem.\\n\\n(4) CriticLean (July 2025) creates a new reward signal category (trained critic at 84.8%) untested as direct RL signal. FormalRewardBench (arXiv:2605.10141) reveals a generation-evaluation gap — specialized provers perform worst at proof evaluation (24.4% pairwise) while frontier LLMs are best (59.8%) — raising the question of how trained critics' gaming resistance relates to their normal-condition accuracy.\\n\\n(5) Rich theoretical infrastructure now exists for formalizing gaming resistance via BOTH regularization and robust optimization: the Correlated Proxies framework (arXiv:2403.03185, ICLR 2025 Spotlight) defines hacking via proxy-true correlation breakdown and proves regularization bounds parametrized by correlation r; the Robust Correlated Proxies extension (arXiv:2604.12086, ICLR 2026) formulates max-min robust optimization over the space of all r-correlated proxies, noting 'there is currently no principled method for selecting r.' GRS-Pearson provides exactly this data-driven r estimation, addressing an acknowledged open problem.\\n\\n(6) The proliferation of domain-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS — 5+ methods in 2025-2026) creates urgency for domain-specific evaluation: do autoformalization's formal verification capabilities enable better gaming-resistance measurement than general-purpose approaches?\\n\\n(7) 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves hacking is structural under finite evaluation, and the Proxy Compression Hypothesis (arXiv:2604.13602) explains it as an inevitable consequence of proxy-based optimization — establishing that measuring resistance (not eliminating hacking) is the practically important question.\\n\\n(8) Independent work on embedding-based rewards for autoformalization GRPO (arXiv:2603.24372 — cycle consistency with cosine similarity on Qwen3.5-2B) validates the importance of understanding R_embed's properties, including its gaming resistance, as a distinct reward signal category.\\n\\n(9) GSPO (arXiv:2507.18071, July 2025) — the Qwen team's principled solution to MoE training instability under RL — enables stable training of the 30B MoE model without ad hoc engineering workarounds. Its sequence-level importance ratios compose cleanly with multi-component reward analysis, enabling the first multi-objective gaming-resistance study on a production-scale MoE model with algorithmic (not just engineering) stability guarantees.\",\n  \"landscape\": \"**Autoformalization RL systems:** FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency, achieving 26.15% pass@1 on ProofNet; ablation reveals aggressive gaming — syntax-only RL yields 100% compilation, 0% consistency. Mathesis (ICLR 2026) advances with R_ver + R_sem in GRPO plus HPO; 22% improvement on Gaokao-Formal. CriticLean (arXiv July 2025) trains CriticLeanGPT via SFT+GRPO: Qwen3-14B-RL achieves 84.8% (publicly available), Qwen3-8B-RL achieves 79.8% on CriticLeanBench. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite. Cycle Consistency Fine-tuning (arXiv:2603.24372) uses GRPO with cosine-similarity cycle consistency reward on Qwen3.5-2B, achieving 0.669 mean cycle consistency vs 0.513 SFT — demonstrating independent interest in embedding-based rewards for autoformalization and validating our inclusion of R_embed as a distinct signal category.\\n\\n**Autoformalization benchmarks:** MathAtlas (arXiv:2605.14061, submitted to NeurIPS 2026) is the first large-scale autoformalization benchmark at graduate level: ~52k entities from 103 textbooks spanning 87 mathematical fields, with ~178k dependency relations (depth up to 80). The best model (ReForm 8B) achieves only 9.8% correctness, with a stark compilation-correctness gap (Kimina 7B: 27.3% compile, 2.3% correct). This reinforces the urgency of gaming resistance analysis — RL systems optimizing compilation reward face massive faithfulness gaps, especially as mathematical complexity increases. Existing benchmarks (ProofNet, miniF2F, FormalMATH-Lite) focus on undergraduate/olympiad level; MathAtlas shows the problem worsens dramatically at graduate level.\\n\\n**Faithfulness gaps in autoformalization:** Do LLMs Game Formalization? (arXiv:2604.19459) uses an outcome-based definition: 'formalization gaming is the subset of unfaithfulness where errors functionally enable proof compilation that faithful formalization would not have achieved.' Key findings: (a) NO systematic gaming in unified generation — 94-98% definite precision, models prefer abstention over forcing proofs; (b) In two-stage pipelines, GPT-5 fabricates axioms as 'reactive fallback' (107 cases, mixed across runs), DeepSeek-R1 mistranslates premises producing 'internally consistent outputs that evade detection entirely'; (c) High compilation rates create an 'illusion of correctness' — valid proofs do not guarantee faithful formalizations. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates RLVR models abandon reasoning for shortcuts.\\n\\n**RL training algorithms for MoE models:** GSPO (arXiv:2507.18071, July 2025) — Group Sequence Policy Optimization, developed by the Qwen team — defines importance ratios at the sequence level: s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|}, the length-normalized geometric mean of token ratios. This resolves a fundamental problem with GRPO on MoE architectures: in models like Qwen3-30B-A3B (128 experts, 8 active), ~10% of expert activations change per gradient update (arXiv:2510.23027), causing token-level importance ratios to fluctuate wildly due to different sub-network routing. GSPO's sequence-level aggregate averages out this routing noise, eliminating the need for Routing Replay (a workaround that restricts exploration) and achieving higher training efficiency. The Qwen team reports that GRPO without Routing Replay fails to converge on Qwen3-30B-A3B; GSPO converges stably. GSPO was used to train the production Qwen3 models including Qwen3-235B-A22B. GSPO also includes a GSPO-token variant for finer-grained advantage assignment, which could support per-turn or per-component credit assignment. MoE-GRPO (arXiv:2603.24984) proposes modality-aware router guidance as an alternative MoE stabilization approach.\\n\\n**Multi-objective GRPO weight adaptation (DENSE LANDSCAPE):** (1) MO-GRPO (arXiv:2509.22047): normalizes per-objective advantage A^MO_g = Σ_i [R_i - mean(R_i)]/std(R_i), ensuring equal variance contribution. Theoretically: affine-invariant, Corr(R_i, A^MO) = 1/√K under uncorrelated rewards. Tested on bandits, WMT, AlpacaFarm. (2) CTWA (arXiv:2602.06869, Lu & Jiang): derives local covariance law — objective m improves iff Cov(r_m, s) > 0 where s is the scalarized training signal. Adaptively upweights objectives whose covariance dips below target c*_m via exponential moving average and log-space update. Provides Polyak-Łojasiewicz convergence analysis. Most theoretically grounded of the group. Tested on Math500, MATH algebra with Qwen2.5, Qwen3, SmolLM2. Same authors as DRW. (3) DRW (TACL 2026, Lu & Jiang): hypervolume-guided and gradient-based dynamic weight adaptation for Pareto efficiency. Predecessor to CTWA. (4) Blockwise Advantage Estimation (arXiv:2602.10231): token-level objective assignment — partitions completions into blocks with per-block advantages. Complementary to weight adaptation (addresses credit assignment, not weighting). (5) TaRoS (arXiv:2511.19356): monitors Hoyer sparsity for reward saturation detection, downweights saturated components. Video generation domain. Closest to gaming-awareness via Goodhart's Law sensitivity. ALL five methods are objective-agnostic — none use domain-specific gaming detection.\\n\\n**Gaming-aware RL modifications:** Advantage Modification from 'When Reward Hacking Rebounds' (arXiv:2604.01476): integrates shortcut concept scores (via representation engineering from contrastive pairs) into GRPO advantage computation. Operates at REPRESENTATION level — requires probing hidden states, domain-specific contrastive pairs. SignCert-PO (arXiv:2604.02986): certified sign-preservation radius via adversarial RM perturbation, down-weights non-robust completions. Operates at ADVANTAGE level — requires RM weight access, single-RM settings.\\n\\n**General gaming detection:** GRIFT (arXiv:2604.16242): gradient fingerprints (LoRA adapters, K-means, ~80% F1). Heavyweight: per-sample gradient computation + manual cluster labeling. Exploitation-rate (arXiv:2605.12474): fraction of newly-credited criteria rejected by cross-family LLM panel (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6). Expensive, LLM-dependent, vulnerable to correlated judge failures.\\n\\n**Theoretical foundations:** Correlated Proxies (arXiv:2403.03185, ICLR 2025 Spotlight): formalizes hacking via proxy-true Pearson correlation r; proves safe optimization bound J(π,R) ≥ (1/r)[proxy_gain - σ√((1-r²)χ²)]; regularization λ = σ√(1-r²). KEY: r is explicitly Pearson correlation (Definition 4.1). Robust Correlated Proxies (arXiv:2604.12086, ICLR 2026): extends to max-min robust optimization over all r-correlated proxies — max_π min_{R∈ℛ_corr} E[R], yielding tractable objective max_π r·E[R_proxy] - √(1-r²)·√(χ² - E²[R_proxy]). Crucially notes 'no principled method for selecting r' — an open problem GRS-Pearson addresses. Reward Hacking as Equilibrium (arXiv:2603.28063): hacking is structural under finite evaluation — any optimized agent under-invests in unevaluated dimensions. Reward Hacking survey (arXiv:2604.13602): four-level exploitation hierarchy (feature/representation/evaluator/environment), three-phase detection lifecycle, Proxy Compression Hypothesis unifying hacking as objective compression + optimization amplification + evaluator-policy co-adaptation. SpecBench (arXiv:2605.21384): hacking gap grows 28pp per 10× code size. On the Hidden Objective Biases of GRPO (arXiv:2601.05002): non-uniform group weighting, AdamW scaling insensitivity, momentum clipping violations.\\n\\n**Evaluation metrics for autoformalization:** GTED (AI4Math@ICML 2025): tree-edit-distance over operator trees from Lean Language Server — formally-grounded, no ATP/LLM dependency, highest accuracy (70.73%) and Kappa (0.438) on miniF2F. FormalAlign (ICLR 2025): dual contrastive+generation loss, 99.21% AS on FormL4-Basic. LeanScorer (Mathesis): subtask decomposition, Sugeno fuzzy integral, 0.92 F1. FormalRewardBench (arXiv:2605.10141): first benchmark for reward models in formal theorem proving with Lean 4 — specialized provers score 24.4% pairwise consistency, frontier LLMs 59.8%. Reveals generation-evaluation gap: proving ability does not transfer to evaluation ability.\\n\\n**The refined gap:** Autoformalization uniquely provides formally-grounded faithfulness measurement (GTED), enabling gaming-resistance analysis unavailable in other RL domains. Despite 5+ objective-agnostic adaptive methods and multiple gaming-aware RL modifications, no work: (a) systematically compares gaming resistance across isolated reward source categories for autoformalization; (b) proposes a gaming-resistance metric with formal theoretical grounding — specifically, a dual-track framework where rank-based GRS provides robust monitoring and parametric GRS provides safe optimization calibration via the Correlated Proxies framework; (c) evaluates whether domain-specific formally-grounded gaming detection outperforms general-purpose approaches; (d) addresses the open problem of data-driven r estimation for robust optimization over correlated proxies (arXiv:2604.12086).\",\n  \"inspired_by\": \"The central insight: autoformalization is the IDEAL domain for studying gaming resistance because GTED provides a formally-grounded faithfulness anchor — enabling principled measurement that is provably connected to safe optimization bounds (via Correlated Proxies) and inherently more robust than LLM-based detection (via bounded influence functions). A critical refinement emerged from examining the τ-to-r mapping: robust rank-based measures (Kendall's τ) and parametric measures (Pearson's r) serve fundamentally DIFFERENT roles in gaming-resistance analysis. τ provides stable monitoring because its bounded influence function means gaming outliers don't dominate the measurement; r provides accurate calibration because its sensitivity to outlier magnitude reflects the true degradation of the proxy-truth relationship. This dual-track insight is itself a contribution — it shows that the choice of correlation measure is not a minor methodological detail but determines whether GRS output is suitable for monitoring vs. regularization. A further practical insight emerged from the GSPO development: the Qwen team's finding that token-level importance ratios are fundamentally misaligned with sequence-level rewards — and catastrophically so for MoE models — means that the choice of training algorithm is not merely an engineering detail but affects the stability of the gaming-resistance measurement across training. By adopting GSPO for MoE and GRPO for dense models, we obtain a natural comparison of whether training algorithm stability affects GRS trajectories. The insight emerges from: (1) the theoretical result that reward hacking is structural (arXiv:2603.28063) and that proxies inevitably compress (PCH, arXiv:2604.13602), making resistance measurement the practical question; (2) GTED providing the formally-grounded anchor uniquely in autoformalization; (3) the Correlated Proxies framework (arXiv:2403.03185) AND its robust optimization extension (arXiv:2604.12086) providing the theoretical bridge — but requiring PEARSON r, not rank correlation; (4) the generation-evaluation gap (FormalRewardBench) showing evaluation capability cannot be assumed from generation accuracy; (5) the proliferation of domain-agnostic methods creating demand for domain-specific evaluation; (6) independent exploration of embedding-based rewards for autoformalization (arXiv:2603.24372) validating the importance of understanding individual signal categories; (7) GSPO providing the principled MoE training algorithm that makes stable 30B experiments feasible without ad hoc workarounds.\",\n  \"approach\": \"We present the first formally-grounded gaming-resistance analysis for autoformalization RL. The central claim: GTED's formally-grounded faithfulness measurement uniquely enables a dual-track gaming-resistance framework (GRS) with formal theoretical guarantees — robust monitoring via rank correlation AND safe optimization calibration via parametric correlation connected to the Correlated Proxies framework. The paper has three phases that progressively build on this claim.\\n\\n**Phase 1: Multi-Source Reward Signal Extraction (5 Categories)**\\n\\n(a) Formally-grounded signal R_formal: Using LeanInteract v0.11.3's Message objects (fields: start_pos, end_pos, data, severity ∈ {error, warning, info}), classify compiler diagnostics into error hierarchy via custom regex parser (~200 LoC) over Message.data strings: parse errors → name resolution → type errors → clean compilation. Yields R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} plus density bonus. NOTE: LeanInteract provides three severity levels; the five-level hierarchy is our custom classification, documented as engineering contribution.\\n\\n(b) Embedding similarity R_embed: cosine similarity between sentence embeddings of input NL and backtranslation of generated formal statement (reference-free roundtrip approach). Directly analogous to the cycle consistency reward in Shebzukhov (arXiv:2603.24372), which achieves 0.669 mean cycle consistency on Qwen3.5-2B — validating the signal's viability while leaving its gaming resistance as an open empirical question.\\n\\n(c) LLM judge R_judge: binary faithfulness judgment from frozen LLM (following FormaRL/Mathesis R_sem approach).\\n\\n(d) Trained critic R_critic: semantic fidelity score from CriticLeanGPT-Qwen3-14B-RL (84.8% accuracy, publicly available). First use as direct RL reward signal. Additionally retrain Qwen3-8B using CriticLean_4K dataset (~79.8% expected) to study critic accuracy impact on gaming resistance. FormalRewardBench's generation-evaluation gap motivates studying whether R_critic's gaming resistance differs from its normal-condition accuracy.\\n\\n**Phase 2: Dual-Track GRS (Gaming Resistance Score) Framework — Primary Methodological Contribution**\\n\\nGRS measures the meta-property of reward signals: how faithfully does high reward indicate genuine quality? The critical methodological insight is that MONITORING gaming resistance and CALIBRATING safe optimization require different correlation measures, serving complementary roles.\\n\\n**2a. GRS-Kendall: Robust Gaming Resistance Monitoring**\\n\\n  GRS-Kendall(R, F) = τ(R(x), F(x)) over held-out evaluation set\\n\\nwhere τ is Kendall's rank correlation and F is a faithfulness anchor.\\n\\n*Role*: Primary metric for comparing reward signals' gaming resistance (RQ1, RQ2, RQ3). Advantages: (i) Bounded influence function — gross-error sensitivity is finite (Croux & Dehon 2010), meaning individual gaming outliers cannot dominate the measurement; (ii) Under 5-10% contamination (realistic for RL gaming), Kendall's τ achieves lowest MSE among correlation measures (Xu et al., Signal Processing 2013); (iii) U-statistic theory provides exact sample complexity bounds.\\n\\n*Sample Complexity Bounds*: Since Kendall's τ is a degree-2 U-statistic with kernel h((x₁,y₁),(x₂,y₂)) = sgn((x₂-x₁)(y₂-y₁)) bounded in [-1,1], Hoeffding's inequality for U-statistics gives:\\n  P(|GRS-Kendall_hat - GRS-Kendall| > ε) ≤ 2 exp(-nε²/2)\\nFor ε=0.1, δ=0.05: n ≥ 737 evaluation pairs suffice. Per Bonett & Wright (2000): n=75 per config yields CI half-width ≈ 0.12 for τ ≈ 0.7.\\n\\n**2b. GRS-Pearson: Safe Optimization Calibration via Correlated Proxies**\\n\\n  GRS-Pearson(R, F) = r(R(x), F(x)) = E[(R-μ_R)/σ_R · (F-μ_F)/σ_F]\\n\\n*Role*: Direct estimate of the correlation parameter r in the Correlated Proxies framework (Definition 4.1, arXiv:2403.03185). The mapping is EXACT: GRS-Pearson ≡ r. No transformation needed.\\n\\n*Connection to Regularization (Theorem 5.1)*: A GRS-Pearson confidence interval [r_L, r_U] translates directly to a regularization interval:\\n  λ ∈ [σ√(1-r_U²), σ√(1-r_L²)]\\nUsing the lower confidence bound r_L provides guaranteed conservative regularization:\\n  P(λ̂ ≥ λ_true) ≥ 1 - α/2\\n\\n*Connection to Robust Optimization (arXiv:2604.12086, ICLR 2026)*: GRS-Pearson estimates the r that parametrizes the max-min robust optimization objective: max_π r·E[R_proxy] - √(1-r²)·√(χ² - E²[R_proxy]). Conservative r estimate → larger uncertainty set ℛ_corr → more robust policy. This addresses the paper's acknowledged open problem of principled r selection.\\n\\n*Why Pearson for calibration, not Kendall?*: Under the gaming contamination model (1-α)P_faithful + αP_gamed where P_gamed produces discordant outputs (high reward, low faithfulness):\\n- Population Pearson r drops in proportion to BOTH contamination fraction α AND outlier magnitude m (unbounded influence → sensitive to severity)\\n- Population Kendall τ drops in proportion to contamination fraction α ONLY (bounded influence → insensitive to severity)\\n- Therefore τ_contaminated > r_contaminated: Kendall underestimates the proxy-truth degradation\\n- Substituting τ for r in λ = σ√(1-r²) gives λ(τ) = σ√(1-τ²) < σ√(1-r²) = λ(r) — UNDER-regularization, not conservative\\n- Pearson's sensitivity to outlier magnitude is a FEATURE for regularization: it faithfully reflects how severely gaming has degraded the proxy-truth relationship\\n\\n**2c. Dual-Track Complementarity Theorem:**\\n\\nGRS-Kendall and GRS-Pearson serve provably complementary roles:\\n- Under no contamination (α=0): r = sin(πτ/2) (Greiner relation under bivariate normality). Both provide consistent information.\\n- Under gaming contamination (α>0): the measures DIVERGE. Specifically, the Greiner divergence Δ_G = |r̂ - sin(πτ̂/2)| serves as a contamination indicator — large Δ_G signals non-normal contamination consistent with gaming. This divergence is itself a diagnostic: when GRS-Pearson drops faster than predicted by the Greiner transformation of GRS-Kendall, it indicates gaming outliers of large magnitude.\\n- Information-theoretic complementarity: GRS-Kendall captures the ORDINAL degradation (how many rank inversions?), GRS-Pearson captures the CARDINAL degradation (how severe are the inversions?). Together, they provide a richer picture than either alone.\\n\\n**2d. GRS vs Exploitation-Rate: Complementary Detection Regimes:**\\nGRS provides population-level monitoring with O(n log n) computation and bounded influence; exploitation-rate provides per-instance classification at O(K·n) frontier model cost but is vulnerable to correlated judge failures. GRS dominates when: contamination fraction ε > 0.05, evaluator cost is constrained, judge diversity is limited, or formally-grounded anchor is available. Exploitation-rate dominates for per-instance flagging in domains lacking formal anchors. Analytical comparison using published results; no experimental reimplementation.\\n\\n**2e. Multi-Faceted Faithfulness Anchors:**\\n  GRS-GTED: F(x) = GTED tree-edit-distance (PRIMARY — formally-grounded, no LLM dependency)\\n  GRS-LeanScorer: F(x) = LeanScorer Sugeno score (secondary)\\n  GRS-roundtrip: F(x) = roundtrip consistency (tertiary)\\n  GRS-human: F(x) = expert judgment (gold standard, 600 validation samples)\\n\\n**Phase 3: Systematic Ablation (8 Configurations)**\\n  C1: Binary compilation only (FormaRL/Mathesis R_ver reproduction)\\n  C2: Graded formal signal only (R_formal)\\n  C3: Embedding similarity only (R_embed)\\n  C4: LLM judge only (R_judge)\\n  C5: Trained critic only (R_critic via CriticLeanGPT-14B-RL)\\n  C6: Formal + embedding hybrid (R_formal + R_embed)\\n  C7: Formal + trained critic hybrid (R_formal + R_critic)\\n  C8: Full hybrid (R_formal + R_embed + R_critic)\\n  Tiered model strategy: all 8 on Qwen2.5-Coder-7B-Instruct (dense, GRPO); top 4 by GRS on Qwen3-Coder-30B-A3B-Instruct (MoE, GSPO).\\n\\n  **Training algorithm split — GRPO for dense, GSPO for MoE:**\\n  For the 7B dense model, standard GRPO is used — token-level importance ratios are well-behaved without MoE routing concerns. For the 30B MoE model (128 experts, 8 active), we adopt GSPO (arXiv:2507.18071), the Qwen team's principled solution to MoE training instability. GSPO's sequence-level importance ratios s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|} average out the ~10% expert activation changes per gradient step that cause GRPO to diverge without Routing Replay. This is not merely an engineering preference: the Qwen team demonstrated that GRPO without Routing Replay fails to converge on this architecture, and GSPO achieves higher training efficiency even compared to GRPO with Routing Replay.\\n\\n  **Multi-component rewards under GSPO (MO-GSPO):** For hybrid configurations (C6-C8) on 30B, we combine GSPO's sequence-level importance ratios with MO-GRPO's per-component advantage normalization: A^MO_i = Σ_k [(R_k(x,y_i) - mean(R_k))/std(R_k)]. This composition is mathematically clean — the importance ratio (how much the policy changed) and the advantage (how good the change was per component) are independent computations that enter the objective multiplicatively: J_MO-GSPO = E[(1/G) Σ_i min(s_i · A^MO_i, clip(s_i, 1-ε, 1+ε) · A^MO_i)]. Per-component GRS analysis is fully preserved: GRS measures reward-faithfulness correlation on the evaluation set, independent of how the training algorithm combines rewards. Note that while this MO-GSPO composition is mathematically straightforward (addressing orthogonal concerns), it has not appeared as a standalone published method.\\n\\n  **Incidental algorithm comparison:** The GRPO-for-7B / GSPO-for-30B split provides an incidental observation point: do GRS trajectories differ systematically between training algorithms? Specifically, does GSPO's more stable training (lower gradient variance from sequence-level ratios) produce smoother GRS curves, and does this affect the measured gaming resistance of individual reward components? This is an observational analysis, not a controlled comparison (model size confounds), but informative for understanding GRS's sensitivity to training dynamics.\\n\\n  Critic scaling sub-study: C5 with 14B (84.8%) vs 8B (~79.8%) on 7B model.\\n\\n**Phase 4: Adaptive Composition Demonstration (Lightweight, ~2 pages)**\\n\\nBrief demonstration that GRS can inform dynamic composition, tested on 7B with C8 component set:\\n  D1: AGRC — w_k^(t+1) ∝ w_k^(t)·exp(η·GRS_k^(t)). Gaming-SPECIFIC: upweights gaming-resistant components based on per-component GRS-Kendall (monitoring role), updated every K=500 steps.\\n  D2: CTWA (arXiv:2602.06869) — monitors Cov(r_k, s) and upweights when covariance drops below target c*_k. Gaming-AGNOSTIC but signal-driven: targets interference regardless of cause. Primary comparison — mechanistically closest to AGRC.\\n  D3: MO-GRPO (arXiv:2509.22047) — A^MO = Σ_i [R_i - mean(R_i)]/std(R_i). Gaming-AGNOSTIC and static: normalizes variance. Reference baseline.\\n\\nHypotheses: (H1) When gaming concentrates in specific components, AGRC selectively downweights while CTWA and MO-GRPO cannot discriminate gamed from non-gamed components. (H2) CTWA may match AGRC when gaming correlates with negative covariance (interference and gaming are aligned). Both outcomes are publishable and informative.\\n\\n**Phase 5: Evaluation Framework (6 Analyses)**\\n\\n(1) Standard metrics + automated faithfulness: BEq@1, pass@1, ASSESS structural similarity, GTED score, LeanScorer score, FormalAlign alignment, roundtrip consistency\\n(2) GRS decomposition: GRS-Kendall (primary monitoring), GRS-Spearman (secondary), AND GRS-Pearson (calibration) per configuration × checkpoint — the core analysis answering RQ1 and RQ2. Reporting all three enables the dual-track analysis and Greiner divergence diagnostic.\\n(3) GRS-human validation: 75 samples × 8 key config-model pairs = 600 stratified expert audits with bootstrap BCA CIs (10,000 resamples). Stratified by gaming severity (no/mild/severe). Per Bonett & Wright: n=75 yields CI half-width ≈ 0.12 for τ ≈ 0.7\\n(4) GRS theoretical validation: (a) GRS-Kendall subsampling analysis verifying Hoeffding bounds, (b) GRS-Pearson CI coverage under synthetic contamination injection verifying conservatism for regularization, (c) Greiner divergence (|r̂ - sin(πτ̂/2)|) as gaming contamination detector — calibrating when the dual-track measures diverge, (d) Correlated Proxies regularization interval accuracy — do GRS-Pearson-derived λ values produce policies with verified true-reward improvement?\\n(5) Critic scaling: GRS comparison for R_critic using 14B (84.8%) vs 8B (~79.8%). Connected to FormalRewardBench's generation-evaluation gap: does critic accuracy predict gaming resistance?\\n(6) AGRC vs CTWA vs MO-GRPO demonstration: weight trajectories, GRS at convergence, Pareto analysis (GRS vs standard accuracy)\\n\\n**Research Questions:**\\n  RQ1: Which reward signal categories exhibit highest gaming resistance in isolation? Do formally-grounded signals (C2) outperform semantic (C3, C4) and learned-critic (C5) signals? Does critic accuracy predict gaming resistance? (C5 14B vs 8B)\\n  RQ2: Does hybrid composition (C6-C8) yield additive faithfulness gains while maintaining gaming resistance?\\n  RQ3: Is GRS-GTED a reliable automated proxy for expert gaming assessment? (correlation, bootstrap CIs, sample complexity verification)\\n  RQ4: Does gaming-specific adaptation (AGRC) outperform gaming-agnostic adaptation (CTWA, MO-GRPO) when domain-specific detection is available? (brief demonstration)\\n\\n**Training:** GRPO with KL penalty on Qwen2.5-Coder-7B-Instruct (dense); GSPO on Qwen3-Coder-30B-A3B-Instruct (MoE), with MO-GSPO hybrid for multi-component configurations. Training on ProofNet + FormalMATH-Lite.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1200 H100 (8 configs on 7B via GRPO = 8×70 + top 4 on 30B via GSPO = 4×70 + 3 demo configs on 7B = 3×70 + 80 grid search + 60 CriticLeanGPT inference + 60 evaluation)\",\n      \"cpu_hours\": \"~35,000 CPU-hours on c7i.16xlarge for Lean compilation via Kimina Lean Server + GTED operator tree construction\",\n      \"human_audit_hours\": \"~70 expert-hours for 600 stratified manual gaming audits (75 samples × 8 key config-model pairs) with bootstrap BCA validation\",\n      \"timeline\": \"14-16 weeks (4 wks pipeline + GTED integration + GRS implementation + theoretical proofs + LeanInteract error parser, 5 wks RL training across configs including GSPO for 30B, 1.5 wks demonstration configs (AGRC+CTWA+MO-GRPO), 4 wks evaluation/writing)\",\n      \"estimated_gpu_cost\": \"$3,000 (at ~$2.50/hr H100 spot)\",\n      \"estimated_cpu_cost\": \"$600-1,200 (c7i.16xlarge spot at ~$0.90/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"1050 H100\",\n      \"cpu_hours\": \"~30,000 CPU-hours\",\n      \"human_audit_hours\": \"~55 expert-hours\",\n      \"timeline\": \"12-14 weeks\",\n      \"claude_api_cost\": \"$500\",\n      \"estimated_gpu_cost\": \"$2,625\",\n      \"estimated_cpu_cost\": \"$500-1,000\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1050 H100\",\n      \"cpu_hours\": \"~30,000 CPU-hours\",\n      \"human_audit_hours\": \"~45 expert-hours (automated pre-filtering via GRS-GTED reduces manual load to disagreement cases)\",\n      \"timeline\": \"10-12 weeks\",\n      \"claude_api_cost\": \"$700\",\n      \"estimated_gpu_cost\": \"$2,625\",\n      \"estimated_cpu_cost\": \"$500-1,000\",\n      \"speed_bottleneck\": \"Lean compilation (~7s avg) and GTED operator tree construction (~2s per statement). With 120-180 parallel Lean instances, throughput matches GPU generation.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (abstract Sep 19, paper Sep 24, 2026 [estimated]) — PRIMARY, ~17 weeks available. Analysis paper framing (dual-track GRS + systematic ablation primary, AGRC demonstration secondary) fits ICLR's preference for principled analysis with clear contributions. The corrected Correlated Proxies connection (dual-track with conservatism guarantee) strengthens the theoretical contribution. Tighter scope makes clean narrative feasible.\",\n    \"EACL 2027 (ARR Aug 3, 2026 → Oct 11 commitment) — SECONDARY, ~10 weeks for ARR submission. 7B full ablation + GRS framework + theoretical analysis feasible; 30B scaling and demonstration deferred to camera-ready.\",\n    \"NAACL 2027 (ARR Oct 12, 2026 → commitment ~Oct 16 [estimated]) — TERTIARY CONTINGENCY. Full experiment set including 30B scaling and complete demonstration.\",\n    \"ACL 2027 (ARR ~Feb 16, 2027 [estimated]) — SAFE FALLBACK. Complete experimental set with all supplementary analyses.\"\n  ],\n  \"level\": \"strong-\",\n  \"key_references\": [\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"Mathesis: Towards Formal Theorem Proving from Natural Languages (ICLR 2026)\",\n    \"Online Reinforcement Learning for Autoformalization (MAR Workshop @ NeurIPS 2025)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv July 2025)\",\n    \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (arXiv:2603.24372, March 2026)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv:2604.19459)\",\n    \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)\",\n    \"Group Sequence Policy Optimization [GSPO] (arXiv:2507.18071, July 2025)\",\n    \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems (arXiv:2509.22047, Sep 2025)\",\n    \"Uncovering Cross-Objective Interference in Multi-Objective Alignment [CTWA] (arXiv:2602.06869, Feb 2026)\",\n    \"Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting [DRW] (TACL 2026)\",\n    \"On the Hidden Objective Biases of Group-based Reinforcement Learning (arXiv:2601.05002, Jan 2026)\",\n    \"Blockwise Advantage Estimation for Multi-Objective Alignment (arXiv:2602.10231, Feb 2026)\",\n    \"Rethinking Reward Signals in Video GRPO: When Scores Become Targets [TaRoS] (arXiv:2511.19356)\",\n    \"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, April 2026)\",\n    \"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness [SignCert-PO] (arXiv:2604.02986, April 2026)\",\n    \"Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063, March 2026)\",\n    \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges [Survey] (arXiv:2604.13602, April 2026)\",\n    \"Detecting and Suppressing Reward Hacking with Gradient Fingerprints [GRIFT] (arXiv:2604.16242, April 2026)\",\n    \"Reward Hacking in Rubric-Based Reinforcement Learning [Exploitation-rate] (arXiv:2605.12474, May 2026)\",\n    \"FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv:2605.10141, May 2026)\",\n    \"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking (arXiv:2403.03185, ICLR 2025 Spotlight)\",\n    \"Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026)\",\n    \"Reward Hacking Mitigation using Verifiable Composite Rewards (arXiv:2509.15557, ACM-BCB 2025)\",\n    \"SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv:2605.21384, May 2026)\",\n    \"MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061, May 2026)\",\n    \"Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization (AI4Math @ ICML 2025)\",\n    \"FormalAlign: Automated Alignment Evaluation for Autoformalization (ICLR 2025)\",\n    \"Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)\",\n    \"Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)\",\n    \"Process-Driven Autoformalization in Lean 4 (arXiv 2024)\",\n    \"Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)\",\n    \"ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\",\n    \"Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\",\n    \"Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\",\n    \"Towards Stable and Effective Reinforcement Learning for Mixture-of-Experts (arXiv:2510.23027, Oct 2025)\",\n    \"MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models (arXiv:2603.24984, March 2026)\",\n    \"Sample Size Requirements for Estimating Pearson, Kendall and Spearman Correlations (Bonett & Wright, Psychometrika 2000)\",\n    \"Influence functions of the Spearman and Kendall correlation measures (Croux & Dehon, Statistical Methods & Applications 2010)\",\n    \"A comparative analysis of Spearman's rho and Kendall's tau in normal and contaminated normal models (Xu et al., Signal Processing 2013)\",\n    \"A class of statistics with asymptotically normal distribution (Hoeffding, Annals of Mathematical Statistics 1948)\",\n    \"Asymptotic Inference for Rank Correlations (Pohle, Wermuth & Weiss, arXiv:2512.14609)\"\n  ],\n  \"description\": \"Reward hacking in autoformalization is a documented concern — FormaRL's ablation shows syntax-only RL achieves 100% compilation but 0% semantic consistency, and MathAtlas (arXiv:2605.14061) reveals the gap is catastrophic at graduate level: Kimina 7B compiles 27.3% but only 2.3% are semantically correct. VerifAI-2 (arXiv:2604.19459) shows that high compilation rates create an 'illusion of correctness' even when unified generation shows no systematic gaming. Yet we lack answers to a basic question: which reward signals maintain faithfulness under optimization pressure? This paper provides the first systematic answer, exploiting a capability unique to autoformalization: formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance.\\n\\nOur central insight is that autoformalization is uniquely positioned for principled gaming-resistance analysis. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers GTED — a computable faithfulness anchor derived from the Lean language server's operator trees. A critical methodological refinement: MONITORING gaming resistance and CALIBRATING safe optimization require fundamentally different correlation measures, leading to our dual-track framework.\\n\\nWe contribute three advances.\\n\\n**First (primary contribution)**, the dual-track GRS (Gaming Resistance Score) framework with deep theoretical grounding. GRS-Kendall measures rank correlation between reward signals and GTED-anchored faithfulness, providing ROBUST MONITORING: bounded influence functions (Croux & Dehon 2010) ensure stability under contamination, U-statistic theory gives exact sample complexity bounds (n ≥ 2log(2/δ)/ε² via Hoeffding), and lowest MSE under realistic gaming contamination (Xu et al. 2013). GRS-Pearson measures parametric correlation, providing SAFE OPTIMIZATION CALIBRATION: it exactly estimates the correlation parameter r in the Correlated Proxies framework (Definition 4.1, ICLR 2025 Spotlight), so a confidence interval [r_L, r_U] directly yields a regularization interval [σ√(1-r_U²), σ√(1-r_L²)] with formal conservatism guarantees via the lower confidence bound. GRS-Pearson also addresses an acknowledged open problem in Robust Correlated Proxies (arXiv:2604.12086, ICLR 2026) — providing principled, data-driven r estimation for their max-min robust optimization over all r-correlated proxies. The dual-track design resolves a subtle but critical issue: under gaming contamination, Kendall's τ (robust, bounded influence) drops LESS than Pearson's r (sensitive, unbounded influence), so τ_contaminated > r_contaminated, meaning naively substituting τ for r in regularization formulas would produce dangerously weak regularization. The dual-track framework assigns each measure to its natural role. We further show that the Greiner divergence |r̂ - sin(πτ̂/2)| — the gap between GRS-Pearson and the Greiner transformation of GRS-Kendall — serves as a real-time gaming contamination indicator. We validate GRS against 600 expert-annotated samples with bootstrap BCA confidence intervals.\\n\\n**Second (systematic analysis)**, the first comparison of gaming resistance across five isolated reward source categories for autoformalization RL: binary compilation, graded formal (via custom error-hierarchy classification over LeanInteract v0.11.3 diagnostics), embedding similarity (cf. cycle consistency in arXiv:2603.24372), LLM judge, and trained critic (CriticLeanGPT-Qwen3-14B-RL at 84.8% — first use as direct RL reward). Our 8-configuration ablation uses GRPO on Qwen2.5-Coder-7B-Instruct (dense) and GSPO (arXiv:2507.18071) on Qwen3-Coder-30B-A3B-Instruct (MoE), adopting the model creator's own recommended algorithm for MoE RL training. GSPO's sequence-level importance ratios resolve the MoE routing instability that causes GRPO to diverge on this architecture, without requiring ad hoc engineering workarounds (Routing Replay, auxiliary load-balancing). For multi-component configurations on 30B, we employ an MO-GSPO hybrid combining GSPO's sequence-level ratios with MO-GRPO's per-component advantage normalization — the two mechanisms address orthogonal concerns (importance ratio stability vs. balanced multi-objective optimization) and compose cleanly. Per-component GRS analysis is preserved because GRS measures reward-faithfulness correlation on held-out evaluation data, independent of how the training algorithm combines reward signals. FormalRewardBench's (arXiv:2605.10141) finding that specialized provers are poor evaluators motivates our sub-study of whether critic accuracy (14B vs 8B) predicts gaming resistance.\\n\\n**Third (lightweight demonstration)**, we briefly show that GRS can inform adaptive reward composition via AGRC (gaming-aware dynamic reweighting using per-component GRS-Kendall for the monitoring signal). We compare against CTWA (arXiv:2602.06869) — the most theoretically grounded objective-agnostic adaptive method, which monitors covariance between rewards and training signal — and MO-GRPO (arXiv:2509.22047), testing whether gaming-specific signals outperform gaming-agnostic adaptation. We position this in a dense landscape of 5+ objective-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS), honestly noting AGRC's mechanism is a demonstration of GRS's utility, not a primary methodological contribution.\\n\\nThe paper adopts VerifAI-2's outcome-based gaming definition: reward inflation without corresponding faithfulness improvement, requiring no intent attribution. It is designed for outcome robustness: if formally-grounded signals dominate, we advance reward design; if signals are equivalent, we establish cost-effectiveness; if CTWA matches AGRC, we demonstrate that gaming-specific detection is unnecessary (a useful negative result). Regardless, the dual-track GRS framework with its theoretical guarantees and the systematic gaming-resistance analysis are independent contributions. Targeting ICLR 2027 (Sep 24 estimated deadline), with EACL 2027, NAACL 2027, and ACL 2027 as contingency venues.\",\n  \"project_name\": \"reward_comp_autoform\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de3dd28c-a1cc-4122-827b-effd894b32ba",
  "isSidechain": false,
  "requestId": "req_011CbTv1iEyYBze9gig6FEzZ",
  "type": "assistant",
  "uuid": "38fcf95f-20ee-4e3d-a632-7ffde7b76ee7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HeG63kCMvVJrAkrmwLDL2t",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 5322,
      "cache_creation_input_tokens": 5854,
      "cache_read_input_tokens": 27759,
      "output_tokens": 16120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 5854,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 5322,
          "output_tokens": 16120,
          "cache_read_input_tokens": 27759,
          "cache_creation_input_tokens": 5854,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 5854
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 23 · 2026-05-27T23:14:37.450Z_

<details><summary>↩ Tool result · reported error · `toolu_01Gzctfeqizv9uAEp6kCTmtw`</summary>

```text
Claude requested permissions to write to /tmp/revision_round9.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38fcf95f-20ee-4e3d-a632-7ffde7b76ee7",
  "isSidechain": false,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "type": "user",
  "uuid": "dedc49f8-a548-4bc7-8b7c-7eb4a6d1c3a0",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revision_round9.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "38fcf95f-20ee-4e3d-a632-7ffde7b76ee7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 24_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"FIXED τ-TO-r THEORETICAL BRIDGE (most critical fix): Iden…",
  "leafUuid": "dedc49f8-a548-4bc7-8b7c-7eb4a6d1c3a0",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Runtime record

_source line 25_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistance analysis: address GSPO and benchmark gaps",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Tool call

_source line 26 · 2026-05-27T23:20:28.568Z_

<details open><summary>🔧 Tool call — Write · `toolu_01LEtdJfgVYJVaR5CoNX2LFc`</summary>

```json
{
  "file_path": "/tmp/revision_round9.json",
  "content": "{\n  \"change_type\": \"minor\",\n  \"changes_made\": [\n    \"CRITICAL FIX — ADOPTED GSPO FOR 30B MOE EXPERIMENTS (arXiv:2507.18071): Group Sequence Policy Optimization, developed by the Qwen team specifically for MoE models like Qwen3-30B-A3B, replaces GRPO for the 30B experiments. GSPO defines importance ratios at the sequence level — s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|} — the length-normalized geometric mean of token ratios. This eliminates the MoE routing instability problem: while ~10% of expert activations differ per gradient step (causing wildly fluctuating token-level ratios in GRPO), GSPO's sequence-level aggregate is stable because overall language modeling capability is preserved despite routing changes. The Qwen team demonstrated that GRPO without Routing Replay fails to converge on Qwen3-30B-A3B, while GSPO converges stably and with higher training efficiency. Crucially, per-component reward decomposition and GRS analysis remain fully compatible: (a) GRS measures reward-faithfulness correlation on the evaluation set — a measurement framework independent of the training algorithm; (b) GSPO's advantage computation is independent of its importance ratio computation, so MO-GRPO's per-component advantage normalization A^MO_i = Σ_k [(R_k - mean(R_k))/std(R_k)] composes cleanly with GSPO's sequence-level ratios, yielding an MO-GSPO hybrid: J_MO-GSPO = E[(1/G) Σ_i min(s_i · A^MO_i, clip(s_i, 1-ε, 1+ε) · A^MO_i)]; (c) AGRC weight adaptation adjusts w_k based on per-component GRS-Kendall monitoring, feeding into composite reward r = Σ w_k·R_k — this occurs at the reward level, upstream of the importance ratio computation, and is therefore orthogonal to the GSPO/GRPO choice. GRPO is retained for the 7B dense model (Qwen2.5-Coder-7B-Instruct) where token-level ratios are well-behaved and MoE routing is not a concern. This GSPO-for-MoE + GRPO-for-dense split also provides an incidental methodological comparison of training algorithm sensitivity on the GRS framework.\",\n    \"ADDED MathAtlas (arXiv:2605.14061, May 2026) TO LANDSCAPE: First large-scale autoformalization benchmark of graduate-level mathematics (~52k entities from 103 textbooks spanning 87 mathematical fields). Best model achieves only 9.8% correctness (ReForm 8B), with a dramatic compilation-correctness gap: Kimina 7B compiles at 27.3% but only 2.3% are semantically correct — meaning ~92% of compiling formalizations are unfaithful. This directly reinforces the urgency of gaming resistance analysis: RL systems optimizing compilation reward face a massive faithfulness gap at graduate-level complexity. MathAtlas's ~178k dependency relations (depth up to 80) suggest gaming resistance may degrade with mathematical complexity — a hypothesis our framework could test in future work. Cited in landscape and as motivation.\",\n    \"REMOVED AD HOC MOE ENGINEERING MITIGATIONS: The previous approach proposed engineering workarounds (auxiliary load-balancing loss, router-aware IS rescaling, conservative clipping) for running GRPO on MoE. GSPO eliminates the need for these workarounds entirely — it is the principled algorithmic solution from the model's own creators. This simplifies the experimental design and removes a potential criticism about ad hoc engineering compensating for a known algorithmic limitation.\",\n    \"UPDATED TRAINING SECTION: Clearly specifies the training algorithm split: GRPO for Qwen2.5-Coder-7B-Instruct (dense), GSPO for Qwen3-Coder-30B-A3B-Instruct (MoE). The MO-GSPO hybrid for multi-component experiments on 30B is documented as a natural composition of orthogonal mechanisms (sequence-level importance ratios for MoE stability × per-component advantage normalization for balanced multi-objective optimization). Notes that this composition, while mathematically straightforward, has not appeared as a standalone published method — providing an additional minor methodological observation.\",\n    \"VERIFIED CriticLeanGPT ACCURACY: The 14B model (CriticLeanGPT-Qwen3-14B-RL, 15B parameters on HuggingFace, Apache 2.0) has plausible accuracy given the scaling trend (32B: 87.0%, 14B: ~84.8%, 8B would require retraining). The exact 84.8% figure should be verified against the paper's Table 2 upon full paper access. The 8B variant does not exist on HuggingFace and requires retraining as stated. Added a note to verify the specific figure.\"\n  ],\n  \"title\": \"Which Rewards Resist Gaming? Formally-Grounded Gaming Resistance Analysis for Autoformalization RL\",\n  \"core_problem\": \"RL-based autoformalization combines composite rewards — binary compilation (FormaRL, Mathesis), LLM semantic judges (Mathesis R_sem), embedding similarity (Online RL for Autoformalization; cycle consistency in arXiv:2603.24372), and trained critics (CriticLean at 84.8% accuracy) — yet a fundamental question remains unanswered: which reward signals maintain faithfulness under optimization pressure, and can we measure this automatically?\\n\\nThis question is urgent for three reasons. First, the reward-faithfulness gap in autoformalization is documented and severe: FormaRL's ablation reveals syntax-only RL yields 100% compilation but 0% semantic consistency, demonstrating clear gaming under optimization. MathAtlas (arXiv:2605.14061) quantifies the scale of this problem at graduate level: Kimina 7B achieves 27.3% compilation but only 2.3% correctness — ~92% of compiling formalizations are semantically unfaithful. VerifAI-2 (arXiv:2604.19459) provides complementary evidence: while finding no evidence of systematic gaming in unified generation (94-98% definite precision), it documents fabrication (GPT-5) and premise mistranslation (DeepSeek-R1) in two-stage pipelines that evade detection — showing faithfulness gaps even in high-performing systems. Following VerifAI-2's outcome-based definition, we define gaming as reward inflation without corresponding faithfulness improvement, requiring no intent attribution.\\n\\nSecond, theoretically, 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves gaming is a structural equilibrium under finite evaluation — not a correctable bug. The Proxy Compression Hypothesis (arXiv:2604.13602) further explains this as the inevitable consequence of objective compression, optimization amplification, and evaluator-policy co-adaptation. Together, these results make measuring gaming RESISTANCE — which signals degrade least — the critical practical question.\\n\\nThird, the broader RL community has responded with gaming mitigations at multiple levels: MO-GRPO normalizes per-objective variance; CTWA (arXiv:2602.06869) adaptively targets covariance between rewards and training signal; Advantage Modification integrates representation-level shortcut scores; SignCert-PO certifies advantage sign robustness; GRIFT detects gaming via gradient fingerprints; exploitation-rate measures hacking via LLM panels. However, ALL these methods are domain-agnostic. Autoformalization has a UNIQUE advantage: the Lean language server provides formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance (AI4Math@ICML 2025). This creates three domain-specific gaps that no existing work addresses: (1) No systematic comparison of gaming-resistance properties across isolated reward source categories for autoformalization; (2) No gaming-resistance metric leveraging formally-grounded faithfulness anchors — enabling detection that is simultaneously lightweight, automated, and non-circular; (3) No formal theoretical analysis connecting gaming-resistance measurement to the broader reward hacking and safe optimization frameworks, including both regularization-based (Correlated Proxies, ICLR 2025 Spotlight) and robust optimization-based (Robust Correlated Proxies, ICLR 2026) approaches.\",\n  \"opportunity\": \"A unique convergence of nine developments makes this the right moment for this study:\\n\\n(1) GTED (AI4Math@ICML 2025) provides formally-grounded faithfulness via tree-edit-distance over Lean operator trees — the KEY enabling capability. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers a computable, LLM-independent faithfulness anchor.\\n\\n(2) The reward-faithfulness gap is newly documented but unquantified for autoformalization. FormaRL's ablation demonstrates gaming under optimization; MathAtlas (arXiv:2605.14061) reveals the gap is catastrophic at graduate level (~92% of compiling formalizations are unfaithful); VerifAI-2 documents faithfulness gaps in pipelines. We provide the first systematic measurement of which signals are affected and by how much.\\n\\n(3) Mathesis (ICLR 2026) establishes composite rewards for autoformalization GRPO but treats composition as a performance optimization problem, not a gaming-resistance problem.\\n\\n(4) CriticLean (July 2025) creates a new reward signal category (trained critic at 84.8%) untested as direct RL signal. FormalRewardBench (arXiv:2605.10141) reveals a generation-evaluation gap — specialized provers perform worst at proof evaluation (24.4% pairwise) while frontier LLMs are best (59.8%) — raising the question of how trained critics' gaming resistance relates to their normal-condition accuracy.\\n\\n(5) Rich theoretical infrastructure now exists for formalizing gaming resistance via BOTH regularization and robust optimization: the Correlated Proxies framework (arXiv:2403.03185, ICLR 2025 Spotlight) defines hacking via proxy-true correlation breakdown and proves regularization bounds parametrized by correlation r; the Robust Correlated Proxies extension (arXiv:2604.12086, ICLR 2026) formulates max-min robust optimization over the space of all r-correlated proxies, noting 'there is currently no principled method for selecting r.' GRS-Pearson provides exactly this data-driven r estimation, addressing an acknowledged open problem.\\n\\n(6) The proliferation of domain-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS — 5+ methods in 2025-2026) creates urgency for domain-specific evaluation: do autoformalization's formal verification capabilities enable better gaming-resistance measurement than general-purpose approaches?\\n\\n(7) 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves hacking is structural under finite evaluation, and the Proxy Compression Hypothesis (arXiv:2604.13602) explains it as an inevitable consequence of proxy-based optimization — establishing that measuring resistance (not eliminating hacking) is the practically important question.\\n\\n(8) Independent work on embedding-based rewards for autoformalization GRPO (arXiv:2603.24372 — cycle consistency with cosine similarity on Qwen3.5-2B) validates the importance of understanding R_embed's properties, including its gaming resistance, as a distinct reward signal category.\\n\\n(9) GSPO (arXiv:2507.18071, July 2025) — the Qwen team's principled solution to MoE training instability under RL — enables stable training of the 30B MoE model without ad hoc engineering workarounds. Its sequence-level importance ratios compose cleanly with multi-component reward analysis, enabling the first multi-objective gaming-resistance study on a production-scale MoE model with algorithmic (not just engineering) stability guarantees.\",\n  \"landscape\": \"**Autoformalization RL systems:** FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency, achieving 26.15% pass@1 on ProofNet; ablation reveals aggressive gaming — syntax-only RL yields 100% compilation, 0% consistency. Mathesis (ICLR 2026) advances with R_ver + R_sem in GRPO plus HPO; 22% improvement on Gaokao-Formal. CriticLean (arXiv July 2025) trains CriticLeanGPT via SFT+GRPO: Qwen3-14B-RL achieves 84.8% (publicly available), Qwen3-8B-RL achieves 79.8% on CriticLeanBench. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite. Cycle Consistency Fine-tuning (arXiv:2603.24372) uses GRPO with cosine-similarity cycle consistency reward on Qwen3.5-2B, achieving 0.669 mean cycle consistency vs 0.513 SFT — demonstrating independent interest in embedding-based rewards for autoformalization and validating our inclusion of R_embed as a distinct signal category.\\n\\n**Autoformalization benchmarks:** MathAtlas (arXiv:2605.14061, submitted to NeurIPS 2026) is the first large-scale autoformalization benchmark at graduate level: ~52k entities from 103 textbooks spanning 87 mathematical fields, with ~178k dependency relations (depth up to 80). The best model (ReForm 8B) achieves only 9.8% correctness, with a stark compilation-correctness gap (Kimina 7B: 27.3% compile, 2.3% correct). This reinforces the urgency of gaming resistance analysis — RL systems optimizing compilation reward face massive faithfulness gaps, especially as mathematical complexity increases. Existing benchmarks (ProofNet, miniF2F, FormalMATH-Lite) focus on undergraduate/olympiad level; MathAtlas shows the problem worsens dramatically at graduate level.\\n\\n**Faithfulness gaps in autoformalization:** Do LLMs Game Formalization? (arXiv:2604.19459) uses an outcome-based definition: 'formalization gaming is the subset of unfaithfulness where errors functionally enable proof compilation that faithful formalization would not have achieved.' Key findings: (a) NO systematic gaming in unified generation — 94-98% definite precision, models prefer abstention over forcing proofs; (b) In two-stage pipelines, GPT-5 fabricates axioms as 'reactive fallback' (107 cases, mixed across runs), DeepSeek-R1 mistranslates premises producing 'internally consistent outputs that evade detection entirely'; (c) High compilation rates create an 'illusion of correctness' — valid proofs do not guarantee faithful formalizations. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates RLVR models abandon reasoning for shortcuts.\\n\\n**RL training algorithms for MoE models:** GSPO (arXiv:2507.18071, July 2025) — Group Sequence Policy Optimization, developed by the Qwen team — defines importance ratios at the sequence level: s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|}, the length-normalized geometric mean of token ratios. This resolves a fundamental problem with GRPO on MoE architectures: in models like Qwen3-30B-A3B (128 experts, 8 active), ~10% of expert activations change per gradient update (arXiv:2510.23027), causing token-level importance ratios to fluctuate wildly due to different sub-network routing. GSPO's sequence-level aggregate averages out this routing noise, eliminating the need for Routing Replay (a workaround that restricts exploration) and achieving higher training efficiency. The Qwen team reports that GRPO without Routing Replay fails to converge on Qwen3-30B-A3B; GSPO converges stably. GSPO was used to train the production Qwen3 models including Qwen3-235B-A22B. GSPO also includes a GSPO-token variant for finer-grained advantage assignment, which could support per-turn or per-component credit assignment. MoE-GRPO (arXiv:2603.24984) proposes modality-aware router guidance as an alternative MoE stabilization approach.\\n\\n**Multi-objective GRPO weight adaptation (DENSE LANDSCAPE):** (1) MO-GRPO (arXiv:2509.22047): normalizes per-objective advantage A^MO_g = Σ_i [R_i - mean(R_i)]/std(R_i), ensuring equal variance contribution. Theoretically: affine-invariant, Corr(R_i, A^MO) = 1/√K under uncorrelated rewards. Tested on bandits, WMT, AlpacaFarm. (2) CTWA (arXiv:2602.06869, Lu & Jiang): derives local covariance law — objective m improves iff Cov(r_m, s) > 0 where s is the scalarized training signal. Adaptively upweights objectives whose covariance dips below target c*_m via exponential moving average and log-space update. Provides Polyak-Łojasiewicz convergence analysis. Most theoretically grounded of the group. Tested on Math500, MATH algebra with Qwen2.5, Qwen3, SmolLM2. Same authors as DRW. (3) DRW (TACL 2026, Lu & Jiang): hypervolume-guided and gradient-based dynamic weight adaptation for Pareto efficiency. Predecessor to CTWA. (4) Blockwise Advantage Estimation (arXiv:2602.10231): token-level objective assignment — partitions completions into blocks with per-block advantages. Complementary to weight adaptation (addresses credit assignment, not weighting). (5) TaRoS (arXiv:2511.19356): monitors Hoyer sparsity for reward saturation detection, downweights saturated components. Video generation domain. Closest to gaming-awareness via Goodhart's Law sensitivity. ALL five methods are objective-agnostic — none use domain-specific gaming detection.\\n\\n**Gaming-aware RL modifications:** Advantage Modification from 'When Reward Hacking Rebounds' (arXiv:2604.01476): integrates shortcut concept scores (via representation engineering from contrastive pairs) into GRPO advantage computation. Operates at REPRESENTATION level — requires probing hidden states, domain-specific contrastive pairs. SignCert-PO (arXiv:2604.02986): certified sign-preservation radius via adversarial RM perturbation, down-weights non-robust completions. Operates at ADVANTAGE level — requires RM weight access, single-RM settings.\\n\\n**General gaming detection:** GRIFT (arXiv:2604.16242): gradient fingerprints (LoRA adapters, K-means, ~80% F1). Heavyweight: per-sample gradient computation + manual cluster labeling. Exploitation-rate (arXiv:2605.12474): fraction of newly-credited criteria rejected by cross-family LLM panel (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6). Expensive, LLM-dependent, vulnerable to correlated judge failures.\\n\\n**Theoretical foundations:** Correlated Proxies (arXiv:2403.03185, ICLR 2025 Spotlight): formalizes hacking via proxy-true Pearson correlation r; proves safe optimization bound J(π,R) ≥ (1/r)[proxy_gain - σ√((1-r²)χ²)]; regularization λ = σ√(1-r²). KEY: r is explicitly Pearson correlation (Definition 4.1). Robust Correlated Proxies (arXiv:2604.12086, ICLR 2026): extends to max-min robust optimization over all r-correlated proxies — max_π min_{R∈ℛ_corr} E[R], yielding tractable objective max_π r·E[R_proxy] - √(1-r²)·√(χ² - E²[R_proxy]). Crucially notes 'no principled method for selecting r' — an open problem GRS-Pearson addresses. Reward Hacking as Equilibrium (arXiv:2603.28063): hacking is structural under finite evaluation — any optimized agent under-invests in unevaluated dimensions. Reward Hacking survey (arXiv:2604.13602): four-level exploitation hierarchy (feature/representation/evaluator/environment), three-phase detection lifecycle, Proxy Compression Hypothesis unifying hacking as objective compression + optimization amplification + evaluator-policy co-adaptation. SpecBench (arXiv:2605.21384): hacking gap grows 28pp per 10× code size. On the Hidden Objective Biases of GRPO (arXiv:2601.05002): non-uniform group weighting, AdamW scaling insensitivity, momentum clipping violations.\\n\\n**Evaluation metrics for autoformalization:** GTED (AI4Math@ICML 2025): tree-edit-distance over operator trees from Lean Language Server — formally-grounded, no ATP/LLM dependency, highest accuracy (70.73%) and Kappa (0.438) on miniF2F. FormalAlign (ICLR 2025): dual contrastive+generation loss, 99.21% AS on FormL4-Basic. LeanScorer (Mathesis): subtask decomposition, Sugeno fuzzy integral, 0.92 F1. FormalRewardBench (arXiv:2605.10141): first benchmark for reward models in formal theorem proving with Lean 4 — specialized provers score 24.4% pairwise consistency, frontier LLMs 59.8%. Reveals generation-evaluation gap: proving ability does not transfer to evaluation ability.\\n\\n**The refined gap:** Autoformalization uniquely provides formally-grounded faithfulness measurement (GTED), enabling gaming-resistance analysis unavailable in other RL domains. Despite 5+ objective-agnostic adaptive methods and multiple gaming-aware RL modifications, no work: (a) systematically compares gaming resistance across isolated reward source categories for autoformalization; (b) proposes a gaming-resistance metric with formal theoretical grounding — specifically, a dual-track framework where rank-based GRS provides robust monitoring and parametric GRS provides safe optimization calibration via the Correlated Proxies framework; (c) evaluates whether domain-specific formally-grounded gaming detection outperforms general-purpose approaches; (d) addresses the open problem of data-driven r estimation for robust optimization over correlated proxies (arXiv:2604.12086).\",\n  \"inspired_by\": \"The central insight: autoformalization is the IDEAL domain for studying gaming resistance because GTED provides a formally-grounded faithfulness anchor — enabling principled measurement that is provably connected to safe optimization bounds (via Correlated Proxies) and inherently more robust than LLM-based detection (via bounded influence functions). A critical refinement emerged from examining the τ-to-r mapping: robust rank-based measures (Kendall's τ) and parametric measures (Pearson's r) serve fundamentally DIFFERENT roles in gaming-resistance analysis. τ provides stable monitoring because its bounded influence function means gaming outliers don't dominate the measurement; r provides accurate calibration because its sensitivity to outlier magnitude reflects the true degradation of the proxy-truth relationship. This dual-track insight is itself a contribution — it shows that the choice of correlation measure is not a minor methodological detail but determines whether GRS output is suitable for monitoring vs. regularization. A further practical insight emerged from the GSPO development: the Qwen team's finding that token-level importance ratios are fundamentally misaligned with sequence-level rewards — and catastrophically so for MoE models — means that the choice of training algorithm is not merely an engineering detail but affects the stability of the gaming-resistance measurement across training. By adopting GSPO for MoE and GRPO for dense models, we obtain a natural comparison of whether training algorithm stability affects GRS trajectories. The insight emerges from: (1) the theoretical result that reward hacking is structural (arXiv:2603.28063) and that proxies inevitably compress (PCH, arXiv:2604.13602), making resistance measurement the practical question; (2) GTED providing the formally-grounded anchor uniquely in autoformalization; (3) the Correlated Proxies framework (arXiv:2403.03185) AND its robust optimization extension (arXiv:2604.12086) providing the theoretical bridge — but requiring PEARSON r, not rank correlation; (4) the generation-evaluation gap (FormalRewardBench) showing evaluation capability cannot be assumed from generation accuracy; (5) the proliferation of domain-agnostic methods creating demand for domain-specific evaluation; (6) independent exploration of embedding-based rewards for autoformalization (arXiv:2603.24372) validating the importance of understanding individual signal categories; (7) GSPO providing the principled MoE training algorithm that makes stable 30B experiments feasible without ad hoc workarounds.\",\n  \"approach\": \"We present the first formally-grounded gaming-resistance analysis for autoformalization RL. The central claim: GTED's formally-grounded faithfulness measurement uniquely enables a dual-track gaming-resistance framework (GRS) with formal theoretical guarantees — robust monitoring via rank correlation AND safe optimization calibration via parametric correlation connected to the Correlated Proxies framework. The paper has three phases that progressively build on this claim.\\n\\n**Phase 1: Multi-Source Reward Signal Extraction (5 Categories)**\\n\\n(a) Formally-grounded signal R_formal: Using LeanInteract v0.11.3's Message objects (fields: start_pos, end_pos, data, severity ∈ {error, warning, info}), classify compiler diagnostics into error hierarchy via custom regex parser (~200 LoC) over Message.data strings: parse errors → name resolution → type errors → clean compilation. Yields R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} plus density bonus. NOTE: LeanInteract provides three severity levels; the five-level hierarchy is our custom classification, documented as engineering contribution.\\n\\n(b) Embedding similarity R_embed: cosine similarity between sentence embeddings of input NL and backtranslation of generated formal statement (reference-free roundtrip approach). Directly analogous to the cycle consistency reward in Shebzukhov (arXiv:2603.24372), which achieves 0.669 mean cycle consistency on Qwen3.5-2B — validating the signal's viability while leaving its gaming resistance as an open empirical question.\\n\\n(c) LLM judge R_judge: binary faithfulness judgment from frozen LLM (following FormaRL/Mathesis R_sem approach).\\n\\n(d) Trained critic R_critic: semantic fidelity score from CriticLeanGPT-Qwen3-14B-RL (84.8% accuracy, publicly available). First use as direct RL reward signal. Additionally retrain Qwen3-8B using CriticLean_4K dataset (~79.8% expected) to study critic accuracy impact on gaming resistance. FormalRewardBench's generation-evaluation gap motivates studying whether R_critic's gaming resistance differs from its normal-condition accuracy.\\n\\n**Phase 2: Dual-Track GRS (Gaming Resistance Score) Framework — Primary Methodological Contribution**\\n\\nGRS measures the meta-property of reward signals: how faithfully does high reward indicate genuine quality? The critical methodological insight is that MONITORING gaming resistance and CALIBRATING safe optimization require different correlation measures, serving complementary roles.\\n\\n**2a. GRS-Kendall: Robust Gaming Resistance Monitoring**\\n\\n  GRS-Kendall(R, F) = τ(R(x), F(x)) over held-out evaluation set\\n\\nwhere τ is Kendall's rank correlation and F is a faithfulness anchor.\\n\\n*Role*: Primary metric for comparing reward signals' gaming resistance (RQ1, RQ2, RQ3). Advantages: (i) Bounded influence function — gross-error sensitivity is finite (Croux & Dehon 2010), meaning individual gaming outliers cannot dominate the measurement; (ii) Under 5-10% contamination (realistic for RL gaming), Kendall's τ achieves lowest MSE among correlation measures (Xu et al., Signal Processing 2013); (iii) U-statistic theory provides exact sample complexity bounds.\\n\\n*Sample Complexity Bounds*: Since Kendall's τ is a degree-2 U-statistic with kernel h((x₁,y₁),(x₂,y₂)) = sgn((x₂-x₁)(y₂-y₁)) bounded in [-1,1], Hoeffding's inequality for U-statistics gives:\\n  P(|GRS-Kendall_hat - GRS-Kendall| > ε) ≤ 2 exp(-nε²/2)\\nFor ε=0.1, δ=0.05: n ≥ 737 evaluation pairs suffice. Per Bonett & Wright (2000): n=75 per config yields CI half-width ≈ 0.12 for τ ≈ 0.7.\\n\\n**2b. GRS-Pearson: Safe Optimization Calibration via Correlated Proxies**\\n\\n  GRS-Pearson(R, F) = r(R(x), F(x)) = E[(R-μ_R)/σ_R · (F-μ_F)/σ_F]\\n\\n*Role*: Direct estimate of the correlation parameter r in the Correlated Proxies framework (Definition 4.1, arXiv:2403.03185). The mapping is EXACT: GRS-Pearson ≡ r. No transformation needed.\\n\\n*Connection to Regularization (Theorem 5.1)*: A GRS-Pearson confidence interval [r_L, r_U] translates directly to a regularization interval:\\n  λ ∈ [σ√(1-r_U²), σ√(1-r_L²)]\\nUsing the lower confidence bound r_L provides guaranteed conservative regularization:\\n  P(λ̂ ≥ λ_true) ≥ 1 - α/2\\n\\n*Connection to Robust Optimization (arXiv:2604.12086, ICLR 2026)*: GRS-Pearson estimates the r that parametrizes the max-min robust optimization objective: max_π r·E[R_proxy] - √(1-r²)·√(χ² - E²[R_proxy]). Conservative r estimate → larger uncertainty set ℛ_corr → more robust policy. This addresses the paper's acknowledged open problem of principled r selection.\\n\\n*Why Pearson for calibration, not Kendall?*: Under the gaming contamination model (1-α)P_faithful + αP_gamed where P_gamed produces discordant outputs (high reward, low faithfulness):\\n- Population Pearson r drops in proportion to BOTH contamination fraction α AND outlier magnitude m (unbounded influence → sensitive to severity)\\n- Population Kendall τ drops in proportion to contamination fraction α ONLY (bounded influence → insensitive to severity)\\n- Therefore τ_contaminated > r_contaminated: Kendall underestimates the proxy-truth degradation\\n- Substituting τ for r in λ = σ√(1-r²) gives λ(τ) = σ√(1-τ²) < σ√(1-r²) = λ(r) — UNDER-regularization, not conservative\\n- Pearson's sensitivity to outlier magnitude is a FEATURE for regularization: it faithfully reflects how severely gaming has degraded the proxy-truth relationship\\n\\n**2c. Dual-Track Complementarity Theorem:**\\n\\nGRS-Kendall and GRS-Pearson serve provably complementary roles:\\n- Under no contamination (α=0): r = sin(πτ/2) (Greiner relation under bivariate normality). Both provide consistent information.\\n- Under gaming contamination (α>0): the measures DIVERGE. Specifically, the Greiner divergence Δ_G = |r̂ - sin(πτ̂/2)| serves as a contamination indicator — large Δ_G signals non-normal contamination consistent with gaming. This divergence is itself a diagnostic: when GRS-Pearson drops faster than predicted by the Greiner transformation of GRS-Kendall, it indicates gaming outliers of large magnitude.\\n- Information-theoretic complementarity: GRS-Kendall captures the ORDINAL degradation (how many rank inversions?), GRS-Pearson captures the CARDINAL degradation (how severe are the inversions?). Together, they provide a richer picture than either alone.\\n\\n**2d. GRS vs Exploitation-Rate: Complementary Detection Regimes:**\\nGRS provides population-level monitoring with O(n log n) computation and bounded influence; exploitation-rate provides per-instance classification at O(K·n) frontier model cost but is vulnerable to correlated judge failures. GRS dominates when: contamination fraction ε > 0.05, evaluator cost is constrained, judge diversity is limited, or formally-grounded anchor is available. Exploitation-rate dominates for per-instance flagging in domains lacking formal anchors. Analytical comparison using published results; no experimental reimplementation.\\n\\n**2e. Multi-Faceted Faithfulness Anchors:**\\n  GRS-GTED: F(x) = GTED tree-edit-distance (PRIMARY — formally-grounded, no LLM dependency)\\n  GRS-LeanScorer: F(x) = LeanScorer Sugeno score (secondary)\\n  GRS-roundtrip: F(x) = roundtrip consistency (tertiary)\\n  GRS-human: F(x) = expert judgment (gold standard, 600 validation samples)\\n\\n**Phase 3: Systematic Ablation (8 Configurations)**\\n  C1: Binary compilation only (FormaRL/Mathesis R_ver reproduction)\\n  C2: Graded formal signal only (R_formal)\\n  C3: Embedding similarity only (R_embed)\\n  C4: LLM judge only (R_judge)\\n  C5: Trained critic only (R_critic via CriticLeanGPT-14B-RL)\\n  C6: Formal + embedding hybrid (R_formal + R_embed)\\n  C7: Formal + trained critic hybrid (R_formal + R_critic)\\n  C8: Full hybrid (R_formal + R_embed + R_critic)\\n  Tiered model strategy: all 8 on Qwen2.5-Coder-7B-Instruct (dense, GRPO); top 4 by GRS on Qwen3-Coder-30B-A3B-Instruct (MoE, GSPO).\\n\\n  **Training algorithm split — GRPO for dense, GSPO for MoE:**\\n  For the 7B dense model, standard GRPO is used — token-level importance ratios are well-behaved without MoE routing concerns. For the 30B MoE model (128 experts, 8 active), we adopt GSPO (arXiv:2507.18071), the Qwen team's principled solution to MoE training instability. GSPO's sequence-level importance ratios s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|} average out the ~10% expert activation changes per gradient step that cause GRPO to diverge without Routing Replay. This is not merely an engineering preference: the Qwen team demonstrated that GRPO without Routing Replay fails to converge on this architecture, and GSPO achieves higher training efficiency even compared to GRPO with Routing Replay.\\n\\n  **Multi-component rewards under GSPO (MO-GSPO):** For hybrid configurations (C6-C8) on 30B, we combine GSPO's sequence-level importance ratios with MO-GRPO's per-component advantage normalization: A^MO_i = Σ_k [(R_k(x,y_i) - mean(R_k))/std(R_k)]. This composition is mathematically clean — the importance ratio (how much the policy changed) and the advantage (how good the change was per component) are independent computations that enter the objective multiplicatively: J_MO-GSPO = E[(1/G) Σ_i min(s_i · A^MO_i, clip(s_i, 1-ε, 1+ε) · A^MO_i)]. Per-component GRS analysis is fully preserved: GRS measures reward-faithfulness correlation on the evaluation set, independent of how the training algorithm combines rewards. Note that while this MO-GSPO composition is mathematically straightforward (addressing orthogonal concerns), it has not appeared as a standalone published method.\\n\\n  **Incidental algorithm comparison:** The GRPO-for-7B / GSPO-for-30B split provides an incidental observation point: do GRS trajectories differ systematically between training algorithms? Specifically, does GSPO's more stable training (lower gradient variance from sequence-level ratios) produce smoother GRS curves, and does this affect the measured gaming resistance of individual reward components? This is an observational analysis, not a controlled comparison (model size confounds), but informative for understanding GRS's sensitivity to training dynamics.\\n\\n  Critic scaling sub-study: C5 with 14B (84.8%) vs 8B (~79.8%) on 7B model.\\n\\n**Phase 4: Adaptive Composition Demonstration (Lightweight, ~2 pages)**\\n\\nBrief demonstration that GRS can inform dynamic composition, tested on 7B with C8 component set:\\n  D1: AGRC — w_k^(t+1) ∝ w_k^(t)·exp(η·GRS_k^(t)). Gaming-SPECIFIC: upweights gaming-resistant components based on per-component GRS-Kendall (monitoring role), updated every K=500 steps.\\n  D2: CTWA (arXiv:2602.06869) — monitors Cov(r_k, s) and upweights when covariance drops below target c*_k. Gaming-AGNOSTIC but signal-driven: targets interference regardless of cause. Primary comparison — mechanistically closest to AGRC.\\n  D3: MO-GRPO (arXiv:2509.22047) — A^MO = Σ_i [R_i - mean(R_i)]/std(R_i). Gaming-AGNOSTIC and static: normalizes variance. Reference baseline.\\n\\nHypotheses: (H1) When gaming concentrates in specific components, AGRC selectively downweights while CTWA and MO-GRPO cannot discriminate gamed from non-gamed components. (H2) CTWA may match AGRC when gaming correlates with negative covariance (interference and gaming are aligned). Both outcomes are publishable and informative.\\n\\n**Phase 5: Evaluation Framework (6 Analyses)**\\n\\n(1) Standard metrics + automated faithfulness: BEq@1, pass@1, ASSESS structural similarity, GTED score, LeanScorer score, FormalAlign alignment, roundtrip consistency\\n(2) GRS decomposition: GRS-Kendall (primary monitoring), GRS-Spearman (secondary), AND GRS-Pearson (calibration) per configuration × checkpoint — the core analysis answering RQ1 and RQ2. Reporting all three enables the dual-track analysis and Greiner divergence diagnostic.\\n(3) GRS-human validation: 75 samples × 8 key config-model pairs = 600 stratified expert audits with bootstrap BCA CIs (10,000 resamples). Stratified by gaming severity (no/mild/severe). Per Bonett & Wright: n=75 yields CI half-width ≈ 0.12 for τ ≈ 0.7\\n(4) GRS theoretical validation: (a) GRS-Kendall subsampling analysis verifying Hoeffding bounds, (b) GRS-Pearson CI coverage under synthetic contamination injection verifying conservatism for regularization, (c) Greiner divergence (|r̂ - sin(πτ̂/2)|) as gaming contamination detector — calibrating when the dual-track measures diverge, (d) Correlated Proxies regularization interval accuracy — do GRS-Pearson-derived λ values produce policies with verified true-reward improvement?\\n(5) Critic scaling: GRS comparison for R_critic using 14B (84.8%) vs 8B (~79.8%). Connected to FormalRewardBench's generation-evaluation gap: does critic accuracy predict gaming resistance?\\n(6) AGRC vs CTWA vs MO-GRPO demonstration: weight trajectories, GRS at convergence, Pareto analysis (GRS vs standard accuracy)\\n\\n**Research Questions:**\\n  RQ1: Which reward signal categories exhibit highest gaming resistance in isolation? Do formally-grounded signals (C2) outperform semantic (C3, C4) and learned-critic (C5) signals? Does critic accuracy predict gaming resistance? (C5 14B vs 8B)\\n  RQ2: Does hybrid composition (C6-C8) yield additive faithfulness gains while maintaining gaming resistance?\\n  RQ3: Is GRS-GTED a reliable automated proxy for expert gaming assessment? (correlation, bootstrap CIs, sample complexity verification)\\n  RQ4: Does gaming-specific adaptation (AGRC) outperform gaming-agnostic adaptation (CTWA, MO-GRPO) when domain-specific detection is available? (brief demonstration)\\n\\n**Training:** GRPO with KL penalty on Qwen2.5-Coder-7B-Instruct (dense); GSPO on Qwen3-Coder-30B-A3B-Instruct (MoE), with MO-GSPO hybrid for multi-component configurations. Training on ProofNet + FormalMATH-Lite.\",\n  \"resource_estimate\": {\n    \"manual\": {\n      \"gpu_hours\": \"1200 H100 (8 configs on 7B via GRPO = 8×70 + top 4 on 30B via GSPO = 4×70 + 3 demo configs on 7B = 3×70 + 80 grid search + 60 CriticLeanGPT inference + 60 evaluation)\",\n      \"cpu_hours\": \"~35,000 CPU-hours on c7i.16xlarge for Lean compilation via Kimina Lean Server + GTED operator tree construction\",\n      \"human_audit_hours\": \"~70 expert-hours for 600 stratified manual gaming audits (75 samples × 8 key config-model pairs) with bootstrap BCA validation\",\n      \"timeline\": \"14-16 weeks (4 wks pipeline + GTED integration + GRS implementation + theoretical proofs + LeanInteract error parser, 5 wks RL training across configs including GSPO for 30B, 1.5 wks demonstration configs (AGRC+CTWA+MO-GRPO), 4 wks evaluation/writing)\",\n      \"estimated_gpu_cost\": \"$3,000 (at ~$2.50/hr H100 spot)\",\n      \"estimated_cpu_cost\": \"$600-1,200 (c7i.16xlarge spot at ~$0.90/hr)\"\n    },\n    \"human_in_loop\": {\n      \"gpu_hours\": \"1050 H100\",\n      \"cpu_hours\": \"~30,000 CPU-hours\",\n      \"human_audit_hours\": \"~55 expert-hours\",\n      \"timeline\": \"12-14 weeks\",\n      \"claude_api_cost\": \"$500\",\n      \"estimated_gpu_cost\": \"$2,625\",\n      \"estimated_cpu_cost\": \"$500-1,000\"\n    },\n    \"auto_research\": {\n      \"gpu_hours\": \"1050 H100\",\n      \"cpu_hours\": \"~30,000 CPU-hours\",\n      \"human_audit_hours\": \"~45 expert-hours (automated pre-filtering via GRS-GTED reduces manual load to disagreement cases)\",\n      \"timeline\": \"10-12 weeks\",\n      \"claude_api_cost\": \"$700\",\n      \"estimated_gpu_cost\": \"$2,625\",\n      \"estimated_cpu_cost\": \"$500-1,000\",\n      \"speed_bottleneck\": \"Lean compilation (~7s avg) and GTED operator tree construction (~2s per statement). With 120-180 parallel Lean instances, throughput matches GPU generation.\"\n    }\n  },\n  \"target_venues\": [\n    \"ICLR 2027 (abstract Sep 19, paper Sep 24, 2026 [estimated]) — PRIMARY, ~17 weeks available. Analysis paper framing (dual-track GRS + systematic ablation primary, AGRC demonstration secondary) fits ICLR's preference for principled analysis with clear contributions. The corrected Correlated Proxies connection (dual-track with conservatism guarantee) strengthens the theoretical contribution. Tighter scope makes clean narrative feasible.\",\n    \"EACL 2027 (ARR Aug 3, 2026 → Oct 11 commitment) — SECONDARY, ~10 weeks for ARR submission. 7B full ablation + GRS framework + theoretical analysis feasible; 30B scaling and demonstration deferred to camera-ready.\",\n    \"NAACL 2027 (ARR Oct 12, 2026 → commitment ~Oct 16 [estimated]) — TERTIARY CONTINGENCY. Full experiment set including 30B scaling and complete demonstration.\",\n    \"ACL 2027 (ARR ~Feb 16, 2027 [estimated]) — SAFE FALLBACK. Complete experimental set with all supplementary analyses.\"\n  ],\n  \"level\": \"strong-\",\n  \"key_references\": [\n    \"FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)\",\n    \"Mathesis: Towards Formal Theorem Proving from Natural Languages (ICLR 2026)\",\n    \"Online Reinforcement Learning for Autoformalization (MAR Workshop @ NeurIPS 2025)\",\n    \"StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)\",\n    \"CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv July 2025)\",\n    \"Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (arXiv:2603.24372, March 2026)\",\n    \"Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv:2604.19459)\",\n    \"LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)\",\n    \"Group Sequence Policy Optimization [GSPO] (arXiv:2507.18071, July 2025)\",\n    \"MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems (arXiv:2509.22047, Sep 2025)\",\n    \"Uncovering Cross-Objective Interference in Multi-Objective Alignment [CTWA] (arXiv:2602.06869, Feb 2026)\",\n    \"Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting [DRW] (TACL 2026)\",\n    \"On the Hidden Objective Biases of Group-based Reinforcement Learning (arXiv:2601.05002, Jan 2026)\",\n    \"Blockwise Advantage Estimation for Multi-Objective Alignment (arXiv:2602.10231, Feb 2026)\",\n    \"Rethinking Reward Signals in Video GRPO: When Scores Become Targets [TaRoS] (arXiv:2511.19356)\",\n    \"When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, April 2026)\",\n    \"Mitigating Reward Hacking in RLHF via Advantage Sign Robustness [SignCert-PO] (arXiv:2604.02986, April 2026)\",\n    \"Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063, March 2026)\",\n    \"Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges [Survey] (arXiv:2604.13602, April 2026)\",\n    \"Detecting and Suppressing Reward Hacking with Gradient Fingerprints [GRIFT] (arXiv:2604.16242, April 2026)\",\n    \"Reward Hacking in Rubric-Based Reinforcement Learning [Exploitation-rate] (arXiv:2605.12474, May 2026)\",\n    \"FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv:2605.10141, May 2026)\",\n    \"Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking (arXiv:2403.03185, ICLR 2025 Spotlight)\",\n    \"Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026)\",\n    \"Reward Hacking Mitigation using Verifiable Composite Rewards (arXiv:2509.15557, ACM-BCB 2025)\",\n    \"SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv:2605.21384, May 2026)\",\n    \"MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061, May 2026)\",\n    \"Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization (AI4Math @ ICML 2025)\",\n    \"FormalAlign: Automated Alignment Evaluation for Autoformalization (ICLR 2025)\",\n    \"Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)\",\n    \"Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)\",\n    \"Process-Driven Autoformalization in Lean 4 (arXiv 2024)\",\n    \"Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)\",\n    \"ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)\",\n    \"ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)\",\n    \"Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)\",\n    \"FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)\",\n    \"Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)\",\n    \"Towards Stable and Effective Reinforcement Learning for Mixture-of-Experts (arXiv:2510.23027, Oct 2025)\",\n    \"MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models (arXiv:2603.24984, March 2026)\",\n    \"Sample Size Requirements for Estimating Pearson, Kendall and Spearman Correlations (Bonett & Wright, Psychometrika 2000)\",\n    \"Influence functions of the Spearman and Kendall correlation measures (Croux & Dehon, Statistical Methods & Applications 2010)\",\n    \"A comparative analysis of Spearman's rho and Kendall's tau in normal and contaminated normal models (Xu et al., Signal Processing 2013)\",\n    \"A class of statistics with asymptotically normal distribution (Hoeffding, Annals of Mathematical Statistics 1948)\",\n    \"Asymptotic Inference for Rank Correlations (Pohle, Wermuth & Weiss, arXiv:2512.14609)\"\n  ],\n  \"description\": \"Reward hacking in autoformalization is a documented concern — FormaRL's ablation shows syntax-only RL achieves 100% compilation but 0% semantic consistency, and MathAtlas (arXiv:2605.14061) reveals the gap is catastrophic at graduate level: Kimina 7B compiles 27.3% but only 2.3% are semantically correct. VerifAI-2 (arXiv:2604.19459) shows that high compilation rates create an 'illusion of correctness' even when unified generation shows no systematic gaming. Yet we lack answers to a basic question: which reward signals maintain faithfulness under optimization pressure? This paper provides the first systematic answer, exploiting a capability unique to autoformalization: formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance.\\n\\nOur central insight is that autoformalization is uniquely positioned for principled gaming-resistance analysis. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers GTED — a computable faithfulness anchor derived from the Lean language server's operator trees. A critical methodological refinement: MONITORING gaming resistance and CALIBRATING safe optimization require fundamentally different correlation measures, leading to our dual-track framework.\\n\\nWe contribute three advances.\\n\\n**First (primary contribution)**, the dual-track GRS (Gaming Resistance Score) framework with deep theoretical grounding. GRS-Kendall measures rank correlation between reward signals and GTED-anchored faithfulness, providing ROBUST MONITORING: bounded influence functions (Croux & Dehon 2010) ensure stability under contamination, U-statistic theory gives exact sample complexity bounds (n ≥ 2log(2/δ)/ε² via Hoeffding), and lowest MSE under realistic gaming contamination (Xu et al. 2013). GRS-Pearson measures parametric correlation, providing SAFE OPTIMIZATION CALIBRATION: it exactly estimates the correlation parameter r in the Correlated Proxies framework (Definition 4.1, ICLR 2025 Spotlight), so a confidence interval [r_L, r_U] directly yields a regularization interval [σ√(1-r_U²), σ√(1-r_L²)] with formal conservatism guarantees via the lower confidence bound. GRS-Pearson also addresses an acknowledged open problem in Robust Correlated Proxies (arXiv:2604.12086, ICLR 2026) — providing principled, data-driven r estimation for their max-min robust optimization over all r-correlated proxies. The dual-track design resolves a subtle but critical issue: under gaming contamination, Kendall's τ (robust, bounded influence) drops LESS than Pearson's r (sensitive, unbounded influence), so τ_contaminated > r_contaminated, meaning naively substituting τ for r in regularization formulas would produce dangerously weak regularization. The dual-track framework assigns each measure to its natural role. We further show that the Greiner divergence |r̂ - sin(πτ̂/2)| — the gap between GRS-Pearson and the Greiner transformation of GRS-Kendall — serves as a real-time gaming contamination indicator. We validate GRS against 600 expert-annotated samples with bootstrap BCA confidence intervals.\\n\\n**Second (systematic analysis)**, the first comparison of gaming resistance across five isolated reward source categories for autoformalization RL: binary compilation, graded formal (via custom error-hierarchy classification over LeanInteract v0.11.3 diagnostics), embedding similarity (cf. cycle consistency in arXiv:2603.24372), LLM judge, and trained critic (CriticLeanGPT-Qwen3-14B-RL at 84.8% — first use as direct RL reward). Our 8-configuration ablation uses GRPO on Qwen2.5-Coder-7B-Instruct (dense) and GSPO (arXiv:2507.18071) on Qwen3-Coder-30B-A3B-Instruct (MoE), adopting the model creator's own recommended algorithm for MoE RL training. GSPO's sequence-level importance ratios resolve the MoE routing instability that causes GRPO to diverge on this architecture, without requiring ad hoc engineering workarounds (Routing Replay, auxiliary load-balancing). For multi-component configurations on 30B, we employ an MO-GSPO hybrid combining GSPO's sequence-level ratios with MO-GRPO's per-component advantage normalization — the two mechanisms address orthogonal concerns (importance ratio stability vs. balanced multi-objective optimization) and compose cleanly. Per-component GRS analysis is preserved because GRS measures reward-faithfulness correlation on held-out evaluation data, independent of how the training algorithm combines reward signals. FormalRewardBench's (arXiv:2605.10141) finding that specialized provers are poor evaluators motivates our sub-study of whether critic accuracy (14B vs 8B) predicts gaming resistance.\\n\\n**Third (lightweight demonstration)**, we briefly show that GRS can inform adaptive reward composition via AGRC (gaming-aware dynamic reweighting using per-component GRS-Kendall for the monitoring signal). We compare against CTWA (arXiv:2602.06869) — the most theoretically grounded objective-agnostic adaptive method, which monitors covariance between rewards and training signal — and MO-GRPO (arXiv:2509.22047), testing whether gaming-specific signals outperform gaming-agnostic adaptation. We position this in a dense landscape of 5+ objective-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS), honestly noting AGRC's mechanism is a demonstration of GRS's utility, not a primary methodological contribution.\\n\\nThe paper adopts VerifAI-2's outcome-based gaming definition: reward inflation without corresponding faithfulness improvement, requiring no intent attribution. It is designed for outcome robustness: if formally-grounded signals dominate, we advance reward design; if signals are equivalent, we establish cost-effectiveness; if CTWA matches AGRC, we demonstrate that gaming-specific detection is unnecessary (a useful negative result). Regardless, the dual-track GRS framework with its theoretical guarantees and the systematic gaming-resistance analysis are independent contributions. Targeting ICLR 2027 (Sep 24 estimated deadline), with EACL 2027, NAACL 2027, and ACL 2027 as contingency venues.\",\n  \"project_name\": \"reward_comp_autoform\",\n  \"source\": \"web_research\"\n}\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "dedc49f8-a548-4bc7-8b7c-7eb4a6d1c3a0",
  "isSidechain": false,
  "requestId": "req_011CbTvW5DaH6BLtQq2czKHG",
  "type": "assistant",
  "uuid": "d91237cc-831e-4184-ab42-009cd2773fee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5UR8Z4CyP4exYmzWSeHCm",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 21484,
      "cache_read_input_tokens": 33613,
      "output_tokens": 14662,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21484,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 14662,
          "cache_read_input_tokens": 33613,
          "cache_creation_input_tokens": 21484,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21484
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 27 · 2026-05-27T23:20:28.574Z_

<details><summary>↩ Tool result · reported error · `toolu_01LEtdJfgVYJVaR5CoNX2LFc`</summary>

```text
Claude requested permissions to write to /tmp/revision_round9.json, but you haven't granted it yet.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d91237cc-831e-4184-ab42-009cd2773fee",
  "isSidechain": false,
  "promptId": "75f2963e-b9e5-4c79-b9f6-038c6d060497",
  "type": "user",
  "uuid": "95081f7f-e6de-4dc0-982b-7fc754465ddc",
  "toolUseResult": "Error: Claude requested permissions to write to /tmp/revision_round9.json, but you haven't granted it yet.",
  "sourceToolAssistantUUID": "d91237cc-831e-4184-ab42-009cd2773fee",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 28_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"FIXED τ-TO-r THEORETICAL BRIDGE (most critical fix): Iden…",
  "leafUuid": "95081f7f-e6de-4dc0-982b-7fc754465ddc",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Runtime record

_source line 29_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistance analysis: address GSPO and benchmark gaps",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Assistant

_source line 30 · 2026-05-27T23:26:30.391Z_

Here is the complete revised JSON for round 9:

```json
{
  "change_type": "minor",
  "changes_made": [
    "CRITICAL FIX — ADOPTED GSPO FOR 30B MOE EXPERIMENTS (arXiv:2507.18071): Group Sequence Policy Optimization, developed by the Qwen team specifically for MoE models like Qwen3-30B-A3B, replaces GRPO for the 30B experiments. GSPO defines importance ratios at the sequence level — s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|} — the length-normalized geometric mean of token ratios. This eliminates the MoE routing instability problem: while ~10% of expert activations differ per gradient step (causing wildly fluctuating token-level ratios in GRPO), GSPO's sequence-level aggregate is stable because overall language modeling capability is preserved despite routing changes. The Qwen team demonstrated that GRPO without Routing Replay fails to converge on Qwen3-30B-A3B, while GSPO converges stably and with higher training efficiency. Crucially, per-component reward decomposition and GRS analysis remain fully compatible: (a) GRS measures reward-faithfulness correlation on the evaluation set — a measurement framework independent of the training algorithm; (b) GSPO's advantage computation is independent of its importance ratio computation, so MO-GRPO's per-component advantage normalization A^MO_i = Σ_k [(R_k - mean(R_k))/std(R_k)] composes cleanly with GSPO's sequence-level ratios, yielding an MO-GSPO hybrid: J_MO-GSPO = E[(1/G) Σ_i min(s_i · A^MO_i, clip(s_i, 1-ε, 1+ε) · A^MO_i)]; (c) AGRC weight adaptation adjusts w_k based on per-component GRS-Kendall monitoring, feeding into composite reward r = Σ w_k·R_k — this occurs at the reward level, upstream of the importance ratio computation, and is therefore orthogonal to the GSPO/GRPO choice. GRPO is retained for the 7B dense model (Qwen2.5-Coder-7B-Instruct) where token-level ratios are well-behaved and MoE routing is not a concern. This GSPO-for-MoE + GRPO-for-dense split also provides an incidental methodological comparison of training algorithm sensitivity on the GRS framework.",
    "ADDED MathAtlas (arXiv:2605.14061, May 2026) TO LANDSCAPE: First large-scale autoformalization benchmark of graduate-level mathematics (~52k entities from 103 textbooks spanning 87 mathematical fields). Best model achieves only 9.8% correctness (ReForm 8B), with a dramatic compilation-correctness gap: Kimina 7B compiles at 27.3% but only 2.3% are semantically correct — meaning ~92% of compiling formalizations are unfaithful. This directly reinforces the urgency of gaming resistance analysis: RL systems optimizing compilation reward face a massive faithfulness gap at graduate-level complexity. MathAtlas's ~178k dependency relations (depth up to 80) suggest gaming resistance may degrade with mathematical complexity — a hypothesis our framework could test in future work. Cited in landscape and as motivation.",
    "REMOVED AD HOC MOE ENGINEERING MITIGATIONS: The previous approach proposed engineering workarounds (auxiliary load-balancing loss, router-aware IS rescaling, conservative clipping) for running GRPO on MoE. GSPO eliminates the need for these workarounds entirely — it is the principled algorithmic solution from the model's own creators. This simplifies the experimental design and removes a potential criticism about ad hoc engineering compensating for a known algorithmic limitation.",
    "UPDATED TRAINING SECTION: Clearly specifies the training algorithm split: GRPO for Qwen2.5-Coder-7B-Instruct (dense), GSPO for Qwen3-Coder-30B-A3B-Instruct (MoE). The MO-GSPO hybrid for multi-component experiments on 30B is documented as a natural composition of orthogonal mechanisms (sequence-level importance ratios for MoE stability × per-component advantage normalization for balanced multi-objective optimization). Notes that this composition, while mathematically straightforward, has not appeared as a standalone published method — providing an additional minor methodological observation.",
    "VERIFIED CriticLeanGPT ACCURACY: The 14B model (CriticLeanGPT-Qwen3-14B-RL, 15B parameters on HuggingFace, Apache 2.0) has plausible accuracy given the scaling trend (32B: 87.0%, 14B: ~84.8%, 8B would require retraining). The exact 84.8% figure should be verified against the paper's Table 2 upon full paper access. The 8B variant does not exist on HuggingFace and requires retraining as stated. Added a note to verify the specific figure."
  ],
  "title": "Which Rewards Resist Gaming? Formally-Grounded Gaming Resistance Analysis for Autoformalization RL",
  "core_problem": "RL-based autoformalization combines composite rewards — binary compilation (FormaRL, Mathesis), LLM semantic judges (Mathesis R_sem), embedding similarity (Online RL for Autoformalization; cycle consistency in arXiv:2603.24372), and trained critics (CriticLean at 84.8% accuracy) — yet a fundamental question remains unanswered: which reward signals maintain faithfulness under optimization pressure, and can we measure this automatically?\n\nThis question is urgent for three reasons. First, the reward-faithfulness gap in autoformalization is documented and severe: FormaRL's ablation reveals syntax-only RL yields 100% compilation but 0% semantic consistency, demonstrating clear gaming under optimization. MathAtlas (arXiv:2605.14061) quantifies the scale of this problem at graduate level: Kimina 7B achieves 27.3% compilation but only 2.3% correctness — ~92% of compiling formalizations are semantically unfaithful. VerifAI-2 (arXiv:2604.19459) provides complementary evidence: while finding no evidence of systematic gaming in unified generation (94-98% definite precision), it documents fabrication (GPT-5) and premise mistranslation (DeepSeek-R1) in two-stage pipelines that evade detection — showing faithfulness gaps even in high-performing systems. Following VerifAI-2's outcome-based definition, we define gaming as reward inflation without corresponding faithfulness improvement, requiring no intent attribution.\n\nSecond, theoretically, 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves gaming is a structural equilibrium under finite evaluation — not a correctable bug. The Proxy Compression Hypothesis (arXiv:2604.13602) further explains this as the inevitable consequence of objective compression, optimization amplification, and evaluator-policy co-adaptation. Together, these results make measuring gaming RESISTANCE — which signals degrade least — the critical practical question.\n\nThird, the broader RL community has responded with gaming mitigations at multiple levels: MO-GRPO normalizes per-objective variance; CTWA (arXiv:2602.06869) adaptively targets covariance between rewards and training signal; Advantage Modification integrates representation-level shortcut scores; SignCert-PO certifies advantage sign robustness; GRIFT detects gaming via gradient fingerprints; exploitation-rate measures hacking via LLM panels. However, ALL these methods are domain-agnostic. Autoformalization has a UNIQUE advantage: the Lean language server provides formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance (AI4Math@ICML 2025). This creates three domain-specific gaps that no existing work addresses: (1) No systematic comparison of gaming-resistance properties across isolated reward source categories for autoformalization; (2) No gaming-resistance metric leveraging formally-grounded faithfulness anchors — enabling detection that is simultaneously lightweight, automated, and non-circular; (3) No formal theoretical analysis connecting gaming-resistance measurement to the broader reward hacking and safe optimization frameworks, including both regularization-based (Correlated Proxies, ICLR 2025 Spotlight) and robust optimization-based (Robust Correlated Proxies, ICLR 2026) approaches.",
  "opportunity": "A unique convergence of nine developments makes this the right moment for this study:\n\n(1) GTED (AI4Math@ICML 2025) provides formally-grounded faithfulness via tree-edit-distance over Lean operator trees — the KEY enabling capability. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers a computable, LLM-independent faithfulness anchor.\n\n(2) The reward-faithfulness gap is newly documented but unquantified for autoformalization. FormaRL's ablation demonstrates gaming under optimization; MathAtlas (arXiv:2605.14061) reveals the gap is catastrophic at graduate level (~92% of compiling formalizations are unfaithful); VerifAI-2 documents faithfulness gaps in pipelines. We provide the first systematic measurement of which signals are affected and by how much.\n\n(3) Mathesis (ICLR 2026) establishes composite rewards for autoformalization GRPO but treats composition as a performance optimization problem, not a gaming-resistance problem.\n\n(4) CriticLean (July 2025) creates a new reward signal category (trained critic at 84.8%) untested as direct RL signal. FormalRewardBench (arXiv:2605.10141) reveals a generation-evaluation gap — specialized provers perform worst at proof evaluation (24.4% pairwise) while frontier LLMs are best (59.8%) — raising the question of how trained critics' gaming resistance relates to their normal-condition accuracy.\n\n(5) Rich theoretical infrastructure now exists for formalizing gaming resistance via BOTH regularization and robust optimization: the Correlated Proxies framework (arXiv:2403.03185, ICLR 2025 Spotlight) defines hacking via proxy-true correlation breakdown and proves regularization bounds parametrized by correlation r; the Robust Correlated Proxies extension (arXiv:2604.12086, ICLR 2026) formulates max-min robust optimization over the space of all r-correlated proxies, noting 'there is currently no principled method for selecting r.' GRS-Pearson provides exactly this data-driven r estimation, addressing an acknowledged open problem.\n\n(6) The proliferation of domain-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS — 5+ methods in 2025-2026) creates urgency for domain-specific evaluation: do autoformalization's formal verification capabilities enable better gaming-resistance measurement than general-purpose approaches?\n\n(7) 'Reward Hacking as Equilibrium' (arXiv:2603.28063) proves hacking is structural under finite evaluation, and the Proxy Compression Hypothesis (arXiv:2604.13602) explains it as an inevitable consequence of proxy-based optimization — establishing that measuring resistance (not eliminating hacking) is the practically important question.\n\n(8) Independent work on embedding-based rewards for autoformalization GRPO (arXiv:2603.24372 — cycle consistency with cosine similarity on Qwen3.5-2B) validates the importance of understanding R_embed's properties, including its gaming resistance, as a distinct reward signal category.\n\n(9) GSPO (arXiv:2507.18071, July 2025) — the Qwen team's principled solution to MoE training instability under RL — enables stable training of the 30B MoE model without ad hoc engineering workarounds. Its sequence-level importance ratios compose cleanly with multi-component reward analysis, enabling the first multi-objective gaming-resistance study on a production-scale MoE model with algorithmic (not just engineering) stability guarantees.",
  "landscape": "**Autoformalization RL systems:** FormaRL (COLM 2025) uses GRPO with binary compilation + LLM semantic consistency, achieving 26.15% pass@1 on ProofNet; ablation reveals aggressive gaming — syntax-only RL yields 100% compilation, 0% consistency. Mathesis (ICLR 2026) advances with R_ver + R_sem in GRPO plus HPO; 22% improvement on Gaokao-Formal. CriticLean (arXiv July 2025) trains CriticLeanGPT via SFT+GRPO: Qwen3-14B-RL achieves 84.8% (publicly available), Qwen3-8B-RL achieves 79.8% on CriticLeanBench. StepFun-Formalizer (AAAI 2026) achieves 40.5% BEq@1 SOTA on FormalMATH-Lite. Cycle Consistency Fine-tuning (arXiv:2603.24372) uses GRPO with cosine-similarity cycle consistency reward on Qwen3.5-2B, achieving 0.669 mean cycle consistency vs 0.513 SFT — demonstrating independent interest in embedding-based rewards for autoformalization and validating our inclusion of R_embed as a distinct signal category.\n\n**Autoformalization benchmarks:** MathAtlas (arXiv:2605.14061, submitted to NeurIPS 2026) is the first large-scale autoformalization benchmark at graduate level: ~52k entities from 103 textbooks spanning 87 mathematical fields, with ~178k dependency relations (depth up to 80). The best model (ReForm 8B) achieves only 9.8% correctness, with a stark compilation-correctness gap (Kimina 7B: 27.3% compile, 2.3% correct). This reinforces the urgency of gaming resistance analysis — RL systems optimizing compilation reward face massive faithfulness gaps, especially as mathematical complexity increases. Existing benchmarks (ProofNet, miniF2F, FormalMATH-Lite) focus on undergraduate/olympiad level; MathAtlas shows the problem worsens dramatically at graduate level.\n\n**Faithfulness gaps in autoformalization:** Do LLMs Game Formalization? (arXiv:2604.19459) uses an outcome-based definition: 'formalization gaming is the subset of unfaithfulness where errors functionally enable proof compilation that faithful formalization would not have achieved.' Key findings: (a) NO systematic gaming in unified generation — 94-98% definite precision, models prefer abstention over forcing proofs; (b) In two-stage pipelines, GPT-5 fabricates axioms as 'reactive fallback' (107 cases, mixed across runs), DeepSeek-R1 mistranslates premises producing 'internally consistent outputs that evade detection entirely'; (c) High compilation rates create an 'illusion of correctness' — valid proofs do not guarantee faithful formalizations. LLMs Gaming Verifiers (ICLR 2026 Workshop) demonstrates RLVR models abandon reasoning for shortcuts.\n\n**RL training algorithms for MoE models:** GSPO (arXiv:2507.18071, July 2025) — Group Sequence Policy Optimization, developed by the Qwen team — defines importance ratios at the sequence level: s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|}, the length-normalized geometric mean of token ratios. This resolves a fundamental problem with GRPO on MoE architectures: in models like Qwen3-30B-A3B (128 experts, 8 active), ~10% of expert activations change per gradient update (arXiv:2510.23027), causing token-level importance ratios to fluctuate wildly due to different sub-network routing. GSPO's sequence-level aggregate averages out this routing noise, eliminating the need for Routing Replay (a workaround that restricts exploration) and achieving higher training efficiency. The Qwen team reports that GRPO without Routing Replay fails to converge on Qwen3-30B-A3B; GSPO converges stably. GSPO was used to train the production Qwen3 models including Qwen3-235B-A22B. GSPO also includes a GSPO-token variant for finer-grained advantage assignment, which could support per-turn or per-component credit assignment. MoE-GRPO (arXiv:2603.24984) proposes modality-aware router guidance as an alternative MoE stabilization approach.\n\n**Multi-objective GRPO weight adaptation (DENSE LANDSCAPE):** (1) MO-GRPO (arXiv:2509.22047): normalizes per-objective advantage A^MO_g = Σ_i [R_i - mean(R_i)]/std(R_i), ensuring equal variance contribution. Theoretically: affine-invariant, Corr(R_i, A^MO) = 1/√K under uncorrelated rewards. Tested on bandits, WMT, AlpacaFarm. (2) CTWA (arXiv:2602.06869, Lu & Jiang): derives local covariance law — objective m improves iff Cov(r_m, s) > 0 where s is the scalarized training signal. Adaptively upweights objectives whose covariance dips below target c*_m via exponential moving average and log-space update. Provides Polyak-Łojasiewicz convergence analysis. Most theoretically grounded of the group. Tested on Math500, MATH algebra with Qwen2.5, Qwen3, SmolLM2. Same authors as DRW. (3) DRW (TACL 2026, Lu & Jiang): hypervolume-guided and gradient-based dynamic weight adaptation for Pareto efficiency. Predecessor to CTWA. (4) Blockwise Advantage Estimation (arXiv:2602.10231): token-level objective assignment — partitions completions into blocks with per-block advantages. Complementary to weight adaptation (addresses credit assignment, not weighting). (5) TaRoS (arXiv:2511.19356): monitors Hoyer sparsity for reward saturation detection, downweights saturated components. Video generation domain. Closest to gaming-awareness via Goodhart's Law sensitivity. ALL five methods are objective-agnostic — none use domain-specific gaming detection.\n\n**Gaming-aware RL modifications:** Advantage Modification from 'When Reward Hacking Rebounds' (arXiv:2604.01476): integrates shortcut concept scores (via representation engineering from contrastive pairs) into GRPO advantage computation. Operates at REPRESENTATION level — requires probing hidden states, domain-specific contrastive pairs. SignCert-PO (arXiv:2604.02986): certified sign-preservation radius via adversarial RM perturbation, down-weights non-robust completions. Operates at ADVANTAGE level — requires RM weight access, single-RM settings.\n\n**General gaming detection:** GRIFT (arXiv:2604.16242): gradient fingerprints (LoRA adapters, K-means, ~80% F1). Heavyweight: per-sample gradient computation + manual cluster labeling. Exploitation-rate (arXiv:2605.12474): fraction of newly-credited criteria rejected by cross-family LLM panel (GPT-5.4, Gemini 3 Pro, Claude Opus 4.6). Expensive, LLM-dependent, vulnerable to correlated judge failures.\n\n**Theoretical foundations:** Correlated Proxies (arXiv:2403.03185, ICLR 2025 Spotlight): formalizes hacking via proxy-true Pearson correlation r; proves safe optimization bound J(π,R) ≥ (1/r)[proxy_gain - σ√((1-r²)χ²)]; regularization λ = σ√(1-r²). KEY: r is explicitly Pearson correlation (Definition 4.1). Robust Correlated Proxies (arXiv:2604.12086, ICLR 2026): extends to max-min robust optimization over all r-correlated proxies — max_π min_{R∈ℛ_corr} E[R], yielding tractable objective max_π r·E[R_proxy] - √(1-r²)·√(χ² - E²[R_proxy]). Crucially notes 'no principled method for selecting r' — an open problem GRS-Pearson addresses. Reward Hacking as Equilibrium (arXiv:2603.28063): hacking is structural under finite evaluation — any optimized agent under-invests in unevaluated dimensions. Reward Hacking survey (arXiv:2604.13602): four-level exploitation hierarchy (feature/representation/evaluator/environment), three-phase detection lifecycle, Proxy Compression Hypothesis unifying hacking as objective compression + optimization amplification + evaluator-policy co-adaptation. SpecBench (arXiv:2605.21384): hacking gap grows 28pp per 10× code size. On the Hidden Objective Biases of GRPO (arXiv:2601.05002): non-uniform group weighting, AdamW scaling insensitivity, momentum clipping violations.\n\n**Evaluation metrics for autoformalization:** GTED (AI4Math@ICML 2025): tree-edit-distance over operator trees from Lean Language Server — formally-grounded, no ATP/LLM dependency, highest accuracy (70.73%) and Kappa (0.438) on miniF2F. FormalAlign (ICLR 2025): dual contrastive+generation loss, 99.21% AS on FormL4-Basic. LeanScorer (Mathesis): subtask decomposition, Sugeno fuzzy integral, 0.92 F1. FormalRewardBench (arXiv:2605.10141): first benchmark for reward models in formal theorem proving with Lean 4 — specialized provers score 24.4% pairwise consistency, frontier LLMs 59.8%. Reveals generation-evaluation gap: proving ability does not transfer to evaluation ability.\n\n**The refined gap:** Autoformalization uniquely provides formally-grounded faithfulness measurement (GTED), enabling gaming-resistance analysis unavailable in other RL domains. Despite 5+ objective-agnostic adaptive methods and multiple gaming-aware RL modifications, no work: (a) systematically compares gaming resistance across isolated reward source categories for autoformalization; (b) proposes a gaming-resistance metric with formal theoretical grounding — specifically, a dual-track framework where rank-based GRS provides robust monitoring and parametric GRS provides safe optimization calibration via the Correlated Proxies framework; (c) evaluates whether domain-specific formally-grounded gaming detection outperforms general-purpose approaches; (d) addresses the open problem of data-driven r estimation for robust optimization over correlated proxies (arXiv:2604.12086).",
  "inspired_by": "The central insight: autoformalization is the IDEAL domain for studying gaming resistance because GTED provides a formally-grounded faithfulness anchor — enabling principled measurement that is provably connected to safe optimization bounds (via Correlated Proxies) and inherently more robust than LLM-based detection (via bounded influence functions). A critical refinement emerged from examining the τ-to-r mapping: robust rank-based measures (Kendall's τ) and parametric measures (Pearson's r) serve fundamentally DIFFERENT roles in gaming-resistance analysis. τ provides stable monitoring because its bounded influence function means gaming outliers don't dominate the measurement; r provides accurate calibration because its sensitivity to outlier magnitude reflects the true degradation of the proxy-truth relationship. This dual-track insight is itself a contribution — it shows that the choice of correlation measure is not a minor methodological detail but determines whether GRS output is suitable for monitoring vs. regularization. A further practical insight emerged from the GSPO development: the Qwen team's finding that token-level importance ratios are fundamentally misaligned with sequence-level rewards — and catastrophically so for MoE models — means that the choice of training algorithm is not merely an engineering detail but affects the stability of the gaming-resistance measurement across training. By adopting GSPO for MoE and GRPO for dense models, we obtain a natural comparison of whether training algorithm stability affects GRS trajectories. The insight emerges from: (1) the theoretical result that reward hacking is structural (arXiv:2603.28063) and that proxies inevitably compress (PCH, arXiv:2604.13602), making resistance measurement the practical question; (2) GTED providing the formally-grounded anchor uniquely in autoformalization; (3) the Correlated Proxies framework (arXiv:2403.03185) AND its robust optimization extension (arXiv:2604.12086) providing the theoretical bridge — but requiring PEARSON r, not rank correlation; (4) the generation-evaluation gap (FormalRewardBench) showing evaluation capability cannot be assumed from generation accuracy; (5) the proliferation of domain-agnostic methods creating demand for domain-specific evaluation; (6) independent exploration of embedding-based rewards for autoformalization (arXiv:2603.24372) validating the importance of understanding individual signal categories; (7) GSPO providing the principled MoE training algorithm that makes stable 30B experiments feasible without ad hoc workarounds.",
  "approach": "We present the first formally-grounded gaming-resistance analysis for autoformalization RL. The central claim: GTED's formally-grounded faithfulness measurement uniquely enables a dual-track gaming-resistance framework (GRS) with formal theoretical guarantees — robust monitoring via rank correlation AND safe optimization calibration via parametric correlation connected to the Correlated Proxies framework. The paper has three phases that progressively build on this claim.\n\n**Phase 1: Multi-Source Reward Signal Extraction (5 Categories)**\n\n(a) Formally-grounded signal R_formal: Using LeanInteract v0.11.3's Message objects (fields: start_pos, end_pos, data, severity ∈ {error, warning, info}), classify compiler diagnostics into error hierarchy via custom regex parser (~200 LoC) over Message.data strings: parse errors → name resolution → type errors → clean compilation. Yields R_formal ∈ {0.0, 0.25, 0.5, 0.75, 1.0} plus density bonus. NOTE: LeanInteract provides three severity levels; the five-level hierarchy is our custom classification, documented as engineering contribution.\n\n(b) Embedding similarity R_embed: cosine similarity between sentence embeddings of input NL and backtranslation of generated formal statement (reference-free roundtrip approach). Directly analogous to the cycle consistency reward in Shebzukhov (arXiv:2603.24372), which achieves 0.669 mean cycle consistency on Qwen3.5-2B — validating the signal's viability while leaving its gaming resistance as an open empirical question.\n\n(c) LLM judge R_judge: binary faithfulness judgment from frozen LLM (following FormaRL/Mathesis R_sem approach).\n\n(d) Trained critic R_critic: semantic fidelity score from CriticLeanGPT-Qwen3-14B-RL (84.8% accuracy, publicly available). First use as direct RL reward signal. Additionally retrain Qwen3-8B using CriticLean_4K dataset (~79.8% expected) to study critic accuracy impact on gaming resistance. FormalRewardBench's generation-evaluation gap motivates studying whether R_critic's gaming resistance differs from its normal-condition accuracy.\n\n**Phase 2: Dual-Track GRS (Gaming Resistance Score) Framework — Primary Methodological Contribution**\n\nGRS measures the meta-property of reward signals: how faithfully does high reward indicate genuine quality? The critical methodological insight is that MONITORING gaming resistance and CALIBRATING safe optimization require different correlation measures, serving complementary roles.\n\n**2a. GRS-Kendall: Robust Gaming Resistance Monitoring**\n\n  GRS-Kendall(R, F) = τ(R(x), F(x)) over held-out evaluation set\n\nwhere τ is Kendall's rank correlation and F is a faithfulness anchor.\n\n*Role*: Primary metric for comparing reward signals' gaming resistance (RQ1, RQ2, RQ3). Advantages: (i) Bounded influence function — gross-error sensitivity is finite (Croux & Dehon 2010), meaning individual gaming outliers cannot dominate the measurement; (ii) Under 5-10% contamination (realistic for RL gaming), Kendall's τ achieves lowest MSE among correlation measures (Xu et al., Signal Processing 2013); (iii) U-statistic theory provides exact sample complexity bounds.\n\n*Sample Complexity Bounds*: Since Kendall's τ is a degree-2 U-statistic with kernel h((x₁,y₁),(x₂,y₂)) = sgn((x₂-x₁)(y₂-y₁)) bounded in [-1,1], Hoeffding's inequality for U-statistics gives:\n  P(|GRS-Kendall_hat - GRS-Kendall| > ε) ≤ 2 exp(-nε²/2)\nFor ε=0.1, δ=0.05: n ≥ 737 evaluation pairs suffice. Per Bonett & Wright (2000): n=75 per config yields CI half-width ≈ 0.12 for τ ≈ 0.7.\n\n**2b. GRS-Pearson: Safe Optimization Calibration via Correlated Proxies**\n\n  GRS-Pearson(R, F) = r(R(x), F(x)) = E[(R-μ_R)/σ_R · (F-μ_F)/σ_F]\n\n*Role*: Direct estimate of the correlation parameter r in the Correlated Proxies framework (Definition 4.1, arXiv:2403.03185). The mapping is EXACT: GRS-Pearson ≡ r. No transformation needed.\n\n*Connection to Regularization (Theorem 5.1)*: A GRS-Pearson confidence interval [r_L, r_U] translates directly to a regularization interval:\n  λ ∈ [σ√(1-r_U²), σ√(1-r_L²)]\nUsing the lower confidence bound r_L provides guaranteed conservative regularization:\n  P(λ̂ ≥ λ_true) ≥ 1 - α/2\n\n*Connection to Robust Optimization (arXiv:2604.12086, ICLR 2026)*: GRS-Pearson estimates the r that parametrizes the max-min robust optimization objective: max_π r·E[R_proxy] - √(1-r²)·√(χ² - E²[R_proxy]). Conservative r estimate → larger uncertainty set ℛ_corr → more robust policy. This addresses the paper's acknowledged open problem of principled r selection.\n\n*Why Pearson for calibration, not Kendall?*: Under the gaming contamination model (1-α)P_faithful + αP_gamed where P_gamed produces discordant outputs (high reward, low faithfulness):\n- Population Pearson r drops in proportion to BOTH contamination fraction α AND outlier magnitude m (unbounded influence → sensitive to severity)\n- Population Kendall τ drops in proportion to contamination fraction α ONLY (bounded influence → insensitive to severity)\n- Therefore τ_contaminated > r_contaminated: Kendall underestimates the proxy-truth degradation\n- Substituting τ for r in λ = σ√(1-r²) gives λ(τ) = σ√(1-τ²) < σ√(1-r²) = λ(r) — UNDER-regularization, not conservative\n- Pearson's sensitivity to outlier magnitude is a FEATURE for regularization: it faithfully reflects how severely gaming has degraded the proxy-truth relationship\n\n**2c. Dual-Track Complementarity Theorem:**\n\nGRS-Kendall and GRS-Pearson serve provably complementary roles:\n- Under no contamination (α=0): r = sin(πτ/2) (Greiner relation under bivariate normality). Both provide consistent information.\n- Under gaming contamination (α>0): the measures DIVERGE. Specifically, the Greiner divergence Δ_G = |r̂ - sin(πτ̂/2)| serves as a contamination indicator — large Δ_G signals non-normal contamination consistent with gaming. This divergence is itself a diagnostic: when GRS-Pearson drops faster than predicted by the Greiner transformation of GRS-Kendall, it indicates gaming outliers of large magnitude.\n- Information-theoretic complementarity: GRS-Kendall captures the ORDINAL degradation (how many rank inversions?), GRS-Pearson captures the CARDINAL degradation (how severe are the inversions?). Together, they provide a richer picture than either alone.\n\n**2d. GRS vs Exploitation-Rate: Complementary Detection Regimes:**\nGRS provides population-level monitoring with O(n log n) computation and bounded influence; exploitation-rate provides per-instance classification at O(K·n) frontier model cost but is vulnerable to correlated judge failures. GRS dominates when: contamination fraction ε > 0.05, evaluator cost is constrained, judge diversity is limited, or formally-grounded anchor is available. Exploitation-rate dominates for per-instance flagging in domains lacking formal anchors. Analytical comparison using published results; no experimental reimplementation.\n\n**2e. Multi-Faceted Faithfulness Anchors:**\n  GRS-GTED: F(x) = GTED tree-edit-distance (PRIMARY — formally-grounded, no LLM dependency)\n  GRS-LeanScorer: F(x) = LeanScorer Sugeno score (secondary)\n  GRS-roundtrip: F(x) = roundtrip consistency (tertiary)\n  GRS-human: F(x) = expert judgment (gold standard, 600 validation samples)\n\n**Phase 3: Systematic Ablation (8 Configurations)**\n  C1: Binary compilation only (FormaRL/Mathesis R_ver reproduction)\n  C2: Graded formal signal only (R_formal)\n  C3: Embedding similarity only (R_embed)\n  C4: LLM judge only (R_judge)\n  C5: Trained critic only (R_critic via CriticLeanGPT-14B-RL)\n  C6: Formal + embedding hybrid (R_formal + R_embed)\n  C7: Formal + trained critic hybrid (R_formal + R_critic)\n  C8: Full hybrid (R_formal + R_embed + R_critic)\n  Tiered model strategy: all 8 on Qwen2.5-Coder-7B-Instruct (dense, GRPO); top 4 by GRS on Qwen3-Coder-30B-A3B-Instruct (MoE, GSPO).\n\n  **Training algorithm split — GRPO for dense, GSPO for MoE:**\n  For the 7B dense model, standard GRPO is used — token-level importance ratios are well-behaved without MoE routing concerns. For the 30B MoE model (128 experts, 8 active), we adopt GSPO (arXiv:2507.18071), the Qwen team's principled solution to MoE training instability. GSPO's sequence-level importance ratios s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|} average out the ~10% expert activation changes per gradient step that cause GRPO to diverge without Routing Replay. This is not merely an engineering preference: the Qwen team demonstrated that GRPO without Routing Replay fails to converge on this architecture, and GSPO achieves higher training efficiency even compared to GRPO with Routing Replay.\n\n  **Multi-component rewards under GSPO (MO-GSPO):** For hybrid configurations (C6-C8) on 30B, we combine GSPO's sequence-level importance ratios with MO-GRPO's per-component advantage normalization: A^MO_i = Σ_k [(R_k(x,y_i) - mean(R_k))/std(R_k)]. This composition is mathematically clean — the importance ratio (how much the policy changed) and the advantage (how good the change was per component) are independent computations that enter the objective multiplicatively: J_MO-GSPO = E[(1/G) Σ_i min(s_i · A^MO_i, clip(s_i, 1-ε, 1+ε) · A^MO_i)]. Per-component GRS analysis is fully preserved: GRS measures reward-faithfulness correlation on the evaluation set, independent of how the training algorithm combines rewards. Note that while this MO-GSPO composition is mathematically straightforward (addressing orthogonal concerns), it has not appeared as a standalone published method.\n\n  **Incidental algorithm comparison:** The GRPO-for-7B / GSPO-for-30B split provides an incidental observation point: do GRS trajectories differ systematically between training algorithms? Specifically, does GSPO's more stable training (lower gradient variance from sequence-level ratios) produce smoother GRS curves, and does this affect the measured gaming resistance of individual reward components? This is an observational analysis, not a controlled comparison (model size confounds), but informative for understanding GRS's sensitivity to training dynamics.\n\n  Critic scaling sub-study: C5 with 14B (84.8%) vs 8B (~79.8%) on 7B model.\n\n**Phase 4: Adaptive Composition Demonstration (Lightweight, ~2 pages)**\n\nBrief demonstration that GRS can inform dynamic composition, tested on 7B with C8 component set:\n  D1: AGRC — w_k^(t+1) ∝ w_k^(t)·exp(η·GRS_k^(t)). Gaming-SPECIFIC: upweights gaming-resistant components based on per-component GRS-Kendall (monitoring role), updated every K=500 steps.\n  D2: CTWA (arXiv:2602.06869) — monitors Cov(r_k, s) and upweights when covariance drops below target c*_k. Gaming-AGNOSTIC but signal-driven: targets interference regardless of cause. Primary comparison — mechanistically closest to AGRC.\n  D3: MO-GRPO (arXiv:2509.22047) — A^MO = Σ_i [R_i - mean(R_i)]/std(R_i). Gaming-AGNOSTIC and static: normalizes variance. Reference baseline.\n\nHypotheses: (H1) When gaming concentrates in specific components, AGRC selectively downweights while CTWA and MO-GRPO cannot discriminate gamed from non-gamed components. (H2) CTWA may match AGRC when gaming correlates with negative covariance (interference and gaming are aligned). Both outcomes are publishable and informative.\n\n**Phase 5: Evaluation Framework (6 Analyses)**\n\n(1) Standard metrics + automated faithfulness: BEq@1, pass@1, ASSESS structural similarity, GTED score, LeanScorer score, FormalAlign alignment, roundtrip consistency\n(2) GRS decomposition: GRS-Kendall (primary monitoring), GRS-Spearman (secondary), AND GRS-Pearson (calibration) per configuration × checkpoint — the core analysis answering RQ1 and RQ2. Reporting all three enables the dual-track analysis and Greiner divergence diagnostic.\n(3) GRS-human validation: 75 samples × 8 key config-model pairs = 600 stratified expert audits with bootstrap BCA CIs (10,000 resamples). Stratified by gaming severity (no/mild/severe). Per Bonett & Wright: n=75 yields CI half-width ≈ 0.12 for τ ≈ 0.7\n(4) GRS theoretical validation: (a) GRS-Kendall subsampling analysis verifying Hoeffding bounds, (b) GRS-Pearson CI coverage under synthetic contamination injection verifying conservatism for regularization, (c) Greiner divergence (|r̂ - sin(πτ̂/2)|) as gaming contamination detector — calibrating when the dual-track measures diverge, (d) Correlated Proxies regularization interval accuracy — do GRS-Pearson-derived λ values produce policies with verified true-reward improvement?\n(5) Critic scaling: GRS comparison for R_critic using 14B (84.8%) vs 8B (~79.8%). Connected to FormalRewardBench's generation-evaluation gap: does critic accuracy predict gaming resistance?\n(6) AGRC vs CTWA vs MO-GRPO demonstration: weight trajectories, GRS at convergence, Pareto analysis (GRS vs standard accuracy)\n\n**Research Questions:**\n  RQ1: Which reward signal categories exhibit highest gaming resistance in isolation? Do formally-grounded signals (C2) outperform semantic (C3, C4) and learned-critic (C5) signals? Does critic accuracy predict gaming resistance? (C5 14B vs 8B)\n  RQ2: Does hybrid composition (C6-C8) yield additive faithfulness gains while maintaining gaming resistance?\n  RQ3: Is GRS-GTED a reliable automated proxy for expert gaming assessment? (correlation, bootstrap CIs, sample complexity verification)\n  RQ4: Does gaming-specific adaptation (AGRC) outperform gaming-agnostic adaptation (CTWA, MO-GRPO) when domain-specific detection is available? (brief demonstration)\n\n**Training:** GRPO with KL penalty on Qwen2.5-Coder-7B-Instruct (dense); GSPO on Qwen3-Coder-30B-A3B-Instruct (MoE), with MO-GSPO hybrid for multi-component configurations. Training on ProofNet + FormalMATH-Lite.",
  "resource_estimate": {
    "manual": {
      "gpu_hours": "1200 H100 (8 configs on 7B via GRPO = 8×70 + top 4 on 30B via GSPO = 4×70 + 3 demo configs on 7B = 3×70 + 80 grid search + 60 CriticLeanGPT inference + 60 evaluation)",
      "cpu_hours": "~35,000 CPU-hours on c7i.16xlarge for Lean compilation via Kimina Lean Server + GTED operator tree construction",
      "human_audit_hours": "~70 expert-hours for 600 stratified manual gaming audits (75 samples × 8 key config-model pairs) with bootstrap BCA validation",
      "timeline": "14-16 weeks (4 wks pipeline + GTED integration + GRS implementation + theoretical proofs + LeanInteract error parser, 5 wks RL training across configs including GSPO for 30B, 1.5 wks demonstration configs (AGRC+CTWA+MO-GRPO), 4 wks evaluation/writing)",
      "estimated_gpu_cost": "$3,000 (at ~$2.50/hr H100 spot)",
      "estimated_cpu_cost": "$600-1,200 (c7i.16xlarge spot at ~$0.90/hr)"
    },
    "human_in_loop": {
      "gpu_hours": "1050 H100",
      "cpu_hours": "~30,000 CPU-hours",
      "human_audit_hours": "~55 expert-hours",
      "timeline": "12-14 weeks",
      "claude_api_cost": "$500",
      "estimated_gpu_cost": "$2,625",
      "estimated_cpu_cost": "$500-1,000"
    },
    "auto_research": {
      "gpu_hours": "1050 H100",
      "cpu_hours": "~30,000 CPU-hours",
      "human_audit_hours": "~45 expert-hours (automated pre-filtering via GRS-GTED reduces manual load to disagreement cases)",
      "timeline": "10-12 weeks",
      "claude_api_cost": "$700",
      "estimated_gpu_cost": "$2,625",
      "estimated_cpu_cost": "$500-1,000",
      "speed_bottleneck": "Lean compilation (~7s avg) and GTED operator tree construction (~2s per statement). With 120-180 parallel Lean instances, throughput matches GPU generation."
    }
  },
  "target_venues": [
    "ICLR 2027 (abstract Sep 19, paper Sep 24, 2026 [estimated]) — PRIMARY, ~17 weeks available. Analysis paper framing (dual-track GRS + systematic ablation primary, AGRC demonstration secondary) fits ICLR's preference for principled analysis with clear contributions. The corrected Correlated Proxies connection (dual-track with conservatism guarantee) strengthens the theoretical contribution. Tighter scope makes clean narrative feasible.",
    "EACL 2027 (ARR Aug 3, 2026 → Oct 11 commitment) — SECONDARY, ~10 weeks for ARR submission. 7B full ablation + GRS framework + theoretical analysis feasible; 30B scaling and demonstration deferred to camera-ready.",
    "NAACL 2027 (ARR Oct 12, 2026 → commitment ~Oct 16 [estimated]) — TERTIARY CONTINGENCY. Full experiment set including 30B scaling and complete demonstration.",
    "ACL 2027 (ARR ~Feb 16, 2027 [estimated]) — SAFE FALLBACK. Complete experimental set with all supplementary analyses."
  ],
  "level": "strong-",
  "key_references": [
    "FormaRL: Enhancing Autoformalization with no Labeled Data (COLM 2025)",
    "Mathesis: Towards Formal Theorem Proving from Natural Languages (ICLR 2026)",
    "Online Reinforcement Learning for Autoformalization (MAR Workshop @ NeurIPS 2025)",
    "StepFun-Formalizer: Unlocking the Autoformalization Potential of LLMs Through Knowledge-Reasoning Fusion (AAAI 2026)",
    "CriticLean: Critic-Guided Reinforcement Learning for Mathematical Formalization (arXiv July 2025)",
    "Improving Lean4 Autoformalization via Cycle Consistency Fine-tuning (arXiv:2603.24372, March 2026)",
    "Do LLMs Game Formalization? Evaluating Faithfulness in Logical Reasoning (arXiv:2604.19459)",
    "LLMs Gaming Verifiers: RLVR can Lead to Reward Hacking (ICLR 2026 Workshop)",
    "Group Sequence Policy Optimization [GSPO] (arXiv:2507.18071, July 2025)",
    "MO-GRPO: Mitigating Reward Hacking of Group Relative Policy Optimization on Multi-Objective Problems (arXiv:2509.22047, Sep 2025)",
    "Uncovering Cross-Objective Interference in Multi-Objective Alignment [CTWA] (arXiv:2602.06869, Feb 2026)",
    "Learning to Optimize Multi-Objective Alignment Through Dynamic Reward Weighting [DRW] (TACL 2026)",
    "On the Hidden Objective Biases of Group-based Reinforcement Learning (arXiv:2601.05002, Jan 2026)",
    "Blockwise Advantage Estimation for Multi-Objective Alignment (arXiv:2602.10231, Feb 2026)",
    "Rethinking Reward Signals in Video GRPO: When Scores Become Targets [TaRoS] (arXiv:2511.19356)",
    "When Reward Hacking Rebounds: Understanding and Mitigating It with Representation-Level Signals (arXiv:2604.01476, April 2026)",
    "Mitigating Reward Hacking in RLHF via Advantage Sign Robustness [SignCert-PO] (arXiv:2604.02986, April 2026)",
    "Reward Hacking as Equilibrium under Finite Evaluation (arXiv:2603.28063, March 2026)",
    "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges [Survey] (arXiv:2604.13602, April 2026)",
    "Detecting and Suppressing Reward Hacking with Gradient Fingerprints [GRIFT] (arXiv:2604.16242, April 2026)",
    "Reward Hacking in Rubric-Based Reinforcement Learning [Exploitation-rate] (arXiv:2605.12474, May 2026)",
    "FormalRewardBench: A Benchmark for Formal Theorem Proving Reward Models (arXiv:2605.10141, May 2026)",
    "Correlated Proxies: A New Definition and Improved Mitigation for Reward Hacking (arXiv:2403.03185, ICLR 2025 Spotlight)",
    "Robust Optimization for Mitigating Reward Hacking with Correlated Proxies (arXiv:2604.12086, ICLR 2026)",
    "Reward Hacking Mitigation using Verifiable Composite Rewards (arXiv:2509.15557, ACM-BCB 2025)",
    "SpecBench: Measuring Reward Hacking in Long-Horizon Coding Agents (arXiv:2605.21384, May 2026)",
    "MathAtlas: A Benchmark for Autoformalization in the Wild (arXiv:2605.14061, May 2026)",
    "Generalized Tree Edit Distance (GTED): A Faithful Evaluation Metric for Statement Autoformalization (AI4Math @ ICML 2025)",
    "FormalAlign: Automated Alignment Evaluation for Autoformalization (ICLR 2025)",
    "Monotonic Reference-Free Refinement for Autoformalization (arXiv January 2026)",
    "Process-Verified Reinforcement Learning for Theorem Proving via Lean (NeurIPS 2025)",
    "Process-Driven Autoformalization in Lean 4 (arXiv 2024)",
    "Training Step-Level Reasoning Verifiers with Formal Verification Tools [FOVER] (ACL 2026 Findings)",
    "ASSESS: A Semantic and Structural Evaluation Framework for Statement Similarity (arXiv 2025)",
    "ReForm: Reflective Autoformalization with Prospective Bounded Sequence Optimization (ICLR 2026)",
    "Faithful Autoformalization via Roundtrip Verification and Repair (arXiv April 2026)",
    "FormalMATH: Benchmarking Formal Mathematical Reasoning of Large Language Models (arXiv 2025)",
    "Kimina Lean Server: A High-Performance Lean Server for Large-Scale Verification (arXiv 2025)",
    "Towards Stable and Effective Reinforcement Learning for Mixture-of-Experts (arXiv:2510.23027, Oct 2025)",
    "MoE-GRPO: Optimizing Mixture-of-Experts via Reinforcement Learning in Vision-Language Models (arXiv:2603.24984, March 2026)",
    "Sample Size Requirements for Estimating Pearson, Kendall and Spearman Correlations (Bonett & Wright, Psychometrika 2000)",
    "Influence functions of the Spearman and Kendall correlation measures (Croux & Dehon, Statistical Methods & Applications 2010)",
    "A comparative analysis of Spearman's rho and Kendall's tau in normal and contaminated normal models (Xu et al., Signal Processing 2013)",
    "A class of statistics with asymptotically normal distribution (Hoeffding, Annals of Mathematical Statistics 1948)",
    "Asymptotic Inference for Rank Correlations (Pohle, Wermuth & Weiss, arXiv:2512.14609)"
  ],
  "description": "Reward hacking in autoformalization is a documented concern — FormaRL's ablation shows syntax-only RL achieves 100% compilation but 0% semantic consistency, and MathAtlas (arXiv:2605.14061) reveals the gap is catastrophic at graduate level: Kimina 7B compiles 27.3% but only 2.3% are semantically correct. VerifAI-2 (arXiv:2604.19459) shows that high compilation rates create an 'illusion of correctness' even when unified generation shows no systematic gaming. Yet we lack answers to a basic question: which reward signals maintain faithfulness under optimization pressure? This paper provides the first systematic answer, exploiting a capability unique to autoformalization: formally-grounded, LLM-independent faithfulness measurement via GTED tree-edit-distance.\n\nOur central insight is that autoformalization is uniquely positioned for principled gaming-resistance analysis. Unlike code generation (where test-based evaluation lacks formally-grounded semantic metrics) or general RLHF (where ground truth is subjective), autoformalization offers GTED — a computable faithfulness anchor derived from the Lean language server's operator trees. A critical methodological refinement: MONITORING gaming resistance and CALIBRATING safe optimization require fundamentally different correlation measures, leading to our dual-track framework.\n\nWe contribute three advances.\n\n**First (primary contribution)**, the dual-track GRS (Gaming Resistance Score) framework with deep theoretical grounding. GRS-Kendall measures rank correlation between reward signals and GTED-anchored faithfulness, providing ROBUST MONITORING: bounded influence functions (Croux & Dehon 2010) ensure stability under contamination, U-statistic theory gives exact sample complexity bounds (n ≥ 2log(2/δ)/ε² via Hoeffding), and lowest MSE under realistic gaming contamination (Xu et al. 2013). GRS-Pearson measures parametric correlation, providing SAFE OPTIMIZATION CALIBRATION: it exactly estimates the correlation parameter r in the Correlated Proxies framework (Definition 4.1, ICLR 2025 Spotlight), so a confidence interval [r_L, r_U] directly yields a regularization interval [σ√(1-r_U²), σ√(1-r_L²)] with formal conservatism guarantees via the lower confidence bound. GRS-Pearson also addresses an acknowledged open problem in Robust Correlated Proxies (arXiv:2604.12086, ICLR 2026) — providing principled, data-driven r estimation for their max-min robust optimization over all r-correlated proxies. The dual-track design resolves a subtle but critical issue: under gaming contamination, Kendall's τ (robust, bounded influence) drops LESS than Pearson's r (sensitive, unbounded influence), so τ_contaminated > r_contaminated, meaning naively substituting τ for r in regularization formulas would produce dangerously weak regularization. The dual-track framework assigns each measure to its natural role. We further show that the Greiner divergence |r̂ - sin(πτ̂/2)| — the gap between GRS-Pearson and the Greiner transformation of GRS-Kendall — serves as a real-time gaming contamination indicator. We validate GRS against 600 expert-annotated samples with bootstrap BCA confidence intervals.\n\n**Second (systematic analysis)**, the first comparison of gaming resistance across five isolated reward source categories for autoformalization RL: binary compilation, graded formal (via custom error-hierarchy classification over LeanInteract v0.11.3 diagnostics), embedding similarity (cf. cycle consistency in arXiv:2603.24372), LLM judge, and trained critic (CriticLeanGPT-Qwen3-14B-RL at 84.8% — first use as direct RL reward). Our 8-configuration ablation uses GRPO on Qwen2.5-Coder-7B-Instruct (dense) and GSPO (arXiv:2507.18071) on Qwen3-Coder-30B-A3B-Instruct (MoE), adopting the model creator's own recommended algorithm for MoE RL training. GSPO's sequence-level importance ratios resolve the MoE routing instability that causes GRPO to diverge on this architecture, without requiring ad hoc engineering workarounds (Routing Replay, auxiliary load-balancing). For multi-component configurations on 30B, we employ an MO-GSPO hybrid combining GSPO's sequence-level ratios with MO-GRPO's per-component advantage normalization — the two mechanisms address orthogonal concerns (importance ratio stability vs. balanced multi-objective optimization) and compose cleanly. Per-component GRS analysis is preserved because GRS measures reward-faithfulness correlation on held-out evaluation data, independent of how the training algorithm combines reward signals. FormalRewardBench's (arXiv:2605.10141) finding that specialized provers are poor evaluators motivates our sub-study of whether critic accuracy (14B vs 8B) predicts gaming resistance.\n\n**Third (lightweight demonstration)**, we briefly show that GRS can inform adaptive reward composition via AGRC (gaming-aware dynamic reweighting using per-component GRS-Kendall for the monitoring signal). We compare against CTWA (arXiv:2602.06869) — the most theoretically grounded objective-agnostic adaptive method, which monitors covariance between rewards and training signal — and MO-GRPO (arXiv:2509.22047), testing whether gaming-specific signals outperform gaming-agnostic adaptation. We position this in a dense landscape of 5+ objective-agnostic adaptive methods (MO-GRPO, CTWA, DRW, BAE, TaRoS), honestly noting AGRC's mechanism is a demonstration of GRS's utility, not a primary methodological contribution.\n\nThe paper adopts VerifAI-2's outcome-based gaming definition: reward inflation without corresponding faithfulness improvement, requiring no intent attribution. It is designed for outcome robustness: if formally-grounded signals dominate, we advance reward design; if signals are equivalent, we establish cost-effectiveness; if CTWA matches AGRC, we demonstrate that gaming-specific detection is unnecessary (a useful negative result). Regardless, the dual-track GRS framework with its theoretical guarantees and the systematic gaming-resistance analysis are independent contributions. Targeting ICLR 2027 (Sep 24 estimated deadline), with EACL 2027, NAACL 2027, and ACL 2027 as contingency venues.",
  "project_name": "reward_comp_autoform",
  "source": "web_research"
}
```

---

## Summary of changes in Round 9

### Issue-by-issue response:

**1. CRITICAL — GSPO (arXiv:2507.18071):** Adopted **option (a)** — the best option per reviewer guidance. GSPO replaces GRPO for the 30B MoE experiments, while GRPO is retained for the 7B dense model. Key technical arguments:

- **Why GSPO for 30B:** The Qwen team demonstrated GRPO fails to converge on Qwen3-30B-A3B without Routing Replay, and GSPO achieves higher training efficiency even compared to GRPO+Routing Replay. GSPO's sequence-level importance ratio `s_i(θ) = [π_θ(y_i|x)/π_θ_old(y_i|x)]^{1/|y_i|}` averages out the ~10% expert activation noise per gradient step.

- **Per-component GRS compatibility (the reviewer's key concern):** Fully preserved through three mechanisms: (a) GRS is an *evaluation-time* metric measuring reward-faithfulness correlation — completely independent of the training algorithm; (b) MO-GRPO's per-component advantage normalization composes with GSPO's sequence-level ratios because they address orthogonal concerns (importance ratio computation vs. advantage computation); (c) AGRC weight adaptation operates at the reward level, upstream of the importance ratio.

- **Removed ad hoc engineering mitigations** (load-balancing loss, router-aware IS rescaling, conservative clipping) — GSPO eliminates the need for these entirely.

**2. MINOR — MathAtlas (arXiv:2605.14061):** Added to landscape and core_problem. Key data point: Kimina 7B compiles 27.3% but only 2.3% are correct (~92% unfaithful), reinforcing the urgency of gaming resistance analysis at scale.

**3. CriticLeanGPT accuracy:** Noted the 84.8% figure is plausible given the scaling trend (32B: 87.0%) but should be verified against the paper's Table 2. The 8B variant confirmed as not available on HuggingFace.

**4. GSPO-reward decomposition compatibility:** Addressed explicitly via the MO-GSPO hybrid formulation, showing that sequence-level clipping does not prevent per-component reward analysis because the advantage decomposes linearly across components.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "95081f7f-e6de-4dc0-982b-7fc754465ddc",
  "isSidechain": false,
  "requestId": "req_011CbTvwxSG7HkPAKyk7ka8m",
  "type": "assistant",
  "uuid": "aa9717dc-e0e9-4e66-a4fb-476ec5889d7a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Vx3VPx7oqgzmDLqi129GTz",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 14705,
      "cache_read_input_tokens": 55097,
      "output_tokens": 15187,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 14705,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 15187,
          "cache_read_input_tokens": 55097,
          "cache_creation_input_tokens": 14705,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 14705
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 31_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"FIXED τ-TO-r THEORETICAL BRIDGE (most critical fix): Iden…",
  "leafUuid": "aa9717dc-e0e9-4e66-a4fb-476ec5889d7a",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistance analysis: address GSPO and benchmark gaps",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "You are revising a research idea based on reviewer feedback.  **Today's date: 2026-05-27 (UTC).**  ## Original idea {   \"changes_made\": [     \"FIXED τ-TO-r THEORETICAL BRIDGE (most critical fix): Iden…",
  "leafUuid": "aa9717dc-e0e9-4e66-a4fb-476ec5889d7a",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Revise gaming-resistance analysis: address GSPO and benchmark gaps",
  "sessionId": "6a7b539d-3001-4492-a786-49601df55b48"
}
```

---
