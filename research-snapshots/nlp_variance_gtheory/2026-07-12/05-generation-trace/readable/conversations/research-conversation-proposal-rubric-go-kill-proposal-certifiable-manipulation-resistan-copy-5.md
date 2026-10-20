# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Certifiable Manipulation Resistan

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 45
- **Recorded user turns:** 1
- **Tool calls:** 11
- **Original source:** `logs/chats/exported-trajectories/account-3/97cb931e-0643-49df-bf91-c7f456ede1a1.jsonl`
- **Structured JSON:** [`a9ec048ca445fb42b321.json`](../../sessions/a9/a9ec048ca445fb42b321.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:43:55.351Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:43:55.351Z",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure\n\n## Description\nLLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025) proved bounded f-divergence certification guarantees for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026, via BNE; Chen et al., NeurIPS 2025, via dominant-strategy DMI), and Kaneko & Baldwin (NeurIPS 2025 spotlight) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling—the adversarial dual of the task-performance scaling recently established by Yang et al. (ICLR 2026 Workshop AIMS). We bridge this gap by proving that adversarial manipulation cost grows as Ω(K^{g(I_max)}) where g is an explicit decreasing function of inter-judge signal correlation, derived via a three-pillar proof strategy: (1) SDPI contraction composition (Polyanskiy & Wu) showing perturbation decays multiplicatively across independent channels; (2) Fano-ensemble decomposition (Morishita et al., ICML 2022) separating relevance, redundancy, and combination loss; (3) Gaussian-copula closed form—adapting Turkmen et al.'s equicorrelated model, we derive K_eff = 1+(K-1)·exp(-2·I_max). Under the copula model, g(I_max) = ½·log(K_eff)/log(K), which equals ½ for independent judges (matching √K certified radius scaling from randomized smoothing) and degrades gracefully with correlation. For cross-family ensembles (DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick), we estimate α ∈ [0.35, 0.65] based on copula correlations ρ~0.4-0.5 (Turkmen et al.) and correlated error measurements (Kim et al., ICML 2025), providing certified manipulation-cost bounds of 2.6–3.7× for K=7. We frame this as certifiable robustness for LLM evaluation: just as certified adversarial defenses provide provable guarantees despite sometimes modest empirical margins, our protocol certifies per-evaluation manipulation-resistance bounds that hold against arbitrary future attacks—a guarantee majority voting fundamentally cannot provide. We validate against RobustJudge's 15 realistic attack methods, reporting certified bounds alongside empirical ASR, with sensitivity analysis for α ∈ [0.2, 0.8].\n\n## Core Problem\nCan we provide certifiable manipulation-resistance guarantees for N-judge LLM evaluation protocols, where the certified robustness bound is an explicit, computable function of measurable inter-judge signal correlation, validated against realistic adversarial attacks?\n\n## Opportunity\nRobertson & Koyejo (2025) established that bounded f-divergences like TVD maintain polynomial certification guarantees under adversarial manipulation while unbounded measures (KL) fail (Theorem 3.3), and multiple concurrent works have established peer prediction incentive-compatibility for LLM evaluation (Qiu et al., ICLR 2026; Chen et al., NeurIPS 2025). However, three critical gaps remain: (1) No existing work provides formal N-agent scaling results connecting manipulation cost to measurable inter-judge signal correlation—Robertson & Koyejo analyze pairwise evaluations without multi-judge aggregation theory, Qiu et al. provide no polynomial cost bounds tied to judge count, and Chen et al.'s PEG dominant-strategy guarantee requires conditional independence without characterizing degradation under partial correlation; (2) Empirical validation uses only generic semantic-preserving transforms or deceptive finetuning, not realistic attack vectors documented by the SoK (prompt injection ASR 50–68%, adversarial suffixes, strategic vote rigging); (3) The information-theoretic diversity-scaling framework of Yang et al. (ICLR 2026 Workshop AIMS) shows that multi-agent system performance is bounded by effective channel count K* with residual uncertainty decaying as (1-α_c)^{K*}, but this addresses task performance, not adversarial manipulation resistance—no work establishes the dual result for manipulation cost. Meanwhile, Turkmen et al. (2602.08003) prove that correlated ensembles hit an irreducible error floor Φ(Φ⁻¹(1-p)/√ρ) under their Gaussian copula model, and their three-term MI decomposition (accuracy - redundancy + error correlation) provides the mathematical toolkit for our α estimation. Kaneko & Baldwin (NeurIPS 2025 spotlight) prove tight single-model information-theoretic attack cost bounds N_min ≥ log₂(1/ε)/I_max via Fano inequality, but do not address multi-judge composition. The SoK (2603.29403) finds that 7-model committees empirically reduce ASR to 10–19% but provides no formal explanation. We aim to bridge these gaps by providing the adversarial-robustness dual of the task-performance scaling theory, yielding certifiable manipulation-resistance bounds analogous to certified adversarial robustness in classification.\n\n## Landscape\nRobertson & Koyejo's 'Let's Measure Information Step-by-Step' (arXiv 2508.05469, under TMLR review) formalizes LLM evaluation as an information elicitation game using TVD-MI, proves that bounded f-divergences maintain polynomial certification guarantees under mode-collapse attacks (Theorem 3.3) while unbounded measures like KL degrade exponentially, and demonstrates TVD-MI effectiveness (AUC 0.70–0.77) under generic semantic transforms. Their Identity-Link IRT follow-up (2510.14966) extends to sparse evaluation with two-judge validation (Spearman ρ=0.872) but without formal multi-judge theory.\n\nQiu et al.'s 'Truthfulness Despite Weak Supervision' (ICLR 2026, 2601.20299) applies peer prediction to LLM evaluation/training with Bayesian Nash equilibrium guarantees (Theorem 1) and an empirical inverse scaling property, but targets output truthfulness rather than adversarial robustness of the evaluation protocol itself, acknowledges only unilateral deception (not collusion), and uses no information-theoretic divergence measures.\n\nChen et al.'s 'Incentivizing Truthful Language Models via Peer Elicitation Games' (NeurIPS 2025, 2505.13636) introduces multi-agent peer elicitation using Determinant Mutual Information (DMI) scoring and proves a strictly stronger result: dominant strategy truthfulness (Lemma 1), meaning truthful reporting is optimal regardless of other agents' strategies—not just in Bayesian Nash equilibrium. Their sublinear O(√T) regret bound (Theorem 2) and last-iterate convergence to Nash equilibrium (Theorem 3) via online mirror descent provide a complementary theoretical foundation to Qiu et al.'s BNE. PEG requires n≥2 discriminators and K_t≥4 tasks with conditional independence (Assumption 4), and their experiments use 3 discriminators with the theoretical minimum n≥2 and K_t≥4 tasks required by Lemma 1. However, PEG does not characterize how its manipulation-resistance guarantees degrade when the conditional independence assumption is violated—precisely the regime we analyze.\n\nYang et al.'s 'Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity' (ICLR 2026 Workshop AIMS, 2602.03794) provides an information-theoretic framework where multi-agent system performance is bounded by intrinsic task uncertainty H(Y|X) with residual uncertainty decaying as (1-α_c)^{K*}, where α_c is the complementarity rate and K* = 2^{H(ρ)} is the effective channel count computed via von Neumann entropy of the embedding Gram matrix (Theorem 4.3). Their heterogeneity advantage corollary (Corollary 4.4) formally shows α_het·K_het > α_hom·K_hom implies strictly better performance. Critically, K* captures diversity in embedding space without labels and empirically correlates with accuracy (r=0.388 overall, r=0.535 for K*_c among correct agents). However, their framework addresses task performance (information recovery) not adversarial manipulation resistance (information perturbation cost). Our work establishes the adversarial dual: while their K* governs how quickly residual uncertainty decreases, our framework shows that the same correlation structure governs how quickly manipulation cost increases.\n\nTurkmen et al.'s 'Don't Always Pick the Highest-Performing Model' (arXiv 2602.08003, Feb 2026) formulates ensemble selection as MI maximization with a Gaussian-copula correlated error model and proves an information-theoretic error floor (Theorem 4.4): lim_{m→∞} P_e = Φ(Φ⁻¹(1-p)/√ρ) > 0 for equicorrelated ensembles with pairwise copula correlation ρ. Their three-term MI decomposition (Theorem 4.3)—Δ(j|S) = I(Y;X_j) - I(X_j;X_S) + I(E_j;E_S)—separates accuracy, redundancy, and error correlation. Empirically, they find within-family correlations ρ~0.7-0.8 and cross-family ρ~0.4-0.5. Their copula model provides the mathematical foundation for our derivation of effective independent channel count K_eff.\n\nKaneko & Baldwin's 'Bits Leaked per Query' (NeurIPS 2025 spotlight, arXiv 2510.17000) establishes tight information-theoretic bounds on adversarial attack costs against individual LLMs: any adaptive attack achieving error ≤ ε requires at least N_min ≥ log₂(1/ε)/I_max queries, where I_max is the maximum per-query mutual information leakage (Theorem 1), and this bound is achieved by sequential probability ratio tests (Theorem 2). Validated across 7 LLMs including Llama-4 and DeepSeek-R1, they identify four disclosure regimes (answer-only ~0.001-0.01 bits to full-access ~1.0+ bits). This provides the single-model information-theoretic attack cost foundation; our work extends the composition theory to multi-judge settings where an adversary must simultaneously fool K correlated judges.\n\nShen et al.'s 'Robust LLM Performance Certification via Constrained MLE' (arXiv 2604.03257, Google DeepMind/UCL, 2026) proposes constrained maximum likelihood estimation fusing human labels, LLM-judge annotations, and domain constraints (known TPR/FPR bounds) for certified LLM performance estimation. While addressing performance certification under benign judge noise, it assumes honest judges and does not model adversarial manipulation—precisely the threat model we address.\n\nFeng et al.'s 'Noisy but Valid' (ICLR 2026, arXiv 2601.20913) provides a statistical hypothesis testing framework for certifying LLM failure rates using imperfect judges, with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty. Using a small human-labeled calibration set to estimate judge TPR/FPR, they derive variance-corrected critical thresholds (Theorem 5.4 gives exact conditions for judge adoption). Like Shen et al., this assumes honest but fallible judges, not adversarial manipulation. Our work complements both: Shen et al. certify performance estimates via constrained MLE, Feng et al. certify statistical validity via hypothesis testing, and we certify manipulation resistance under adversarial attacks.\n\nJung & Na's 'Logarithmic Scores, Power-Law Discoveries' (arXiv 2604.00477, April 2026) identifies a score-coverage dissociation in multi-agent evaluation panels: scoring reliability (ICC) scales logarithmically with panel size N (R²=0.974) while unique issue discovery follows a sublinear power law y=7.8·N^0.69 (R²=0.999). Scores saturate ~2× faster than discoveries, with N=8 achieving 82% of maximum scoring reliability but only ~42% of N=32 discovery level. This has direct implications for our K-scaling claims: manipulation-cost scaling benefits may exhibit similar dissociation, where formal robustness guarantees saturate faster than empirical coverage of attack surface. We analyze this explicitly.\n\nThe SoK on LLM-as-Judge Security (2603.29403, April 2026) catalogs extensive vulnerabilities: open-source models showing 50–68% average ASR and frontier models 27–44%; 7-model diverse committees reduce ASR to 10–19% empirically but without formal explanation. RobustJudge (2506.09443) benchmarks 15 attack methods and 7 defense strategies. CAP (OpenReview 2026) shows comparative assessment is more robust than absolute scoring but provides no formal guarantees.\n\nOn error correlation and independence: Kim et al.'s 'Correlated Errors in Large Language Models' (ICML 2025, arXiv 2506.07962) shows 60% pairwise agreement when both err on Helm (vs. 33% random baseline), with same-company adding +0.066 and same-architecture adding +0.076 agreement. Chen et al.'s behavioral entanglement framework (arXiv 2604.07650) introduces BEI and CIG metrics across 18 LLMs from 6 families, finding cross-family entanglement 40–60% lower than intra-family.\n\nOn coordination failure: Frongillo et al. (2503.16280) prove that uninformative equilibria become unstable with fine-grained signals. Keppo et al.'s collusion fragility analysis (2603.20281) finds increasing LLM count from 2→5 breaks collusion (+22%→+3%), but same-family size heterogeneity stabilizes via leader-follower dynamics—motivating cross-family diversity.\n\nOn multi-agent evaluation: CollabEval (2603.00993) proposes three-phase multi-agent evaluation without formal adversarial guarantees. Ebrahimi et al. (IJCNLP-AACL 2025, 2505.24239) uses credibility-based iterative aggregation for adversary resistance without information-theoretic measures.\n\nOn certified ensemble robustness: Chen et al. (2107.10873) prove that diversified gradient and large confidence margin are jointly necessary and sufficient for certified ensemble robustness—standard ensembles achieve only marginal improvements without explicit diversity. Horvath et al. (2106.06946) show randomized smoothing ensembles achieve √K-type certified radius improvement. These provide precedent for polynomial scaling bounds from diversity.\n\nTHE KEY GAP: No existing work provides formal N-agent manipulation-cost scaling results—the adversarial dual of Yang et al.'s task-performance scaling—where the bound is an explicit computable function of measurable inter-judge signal correlation, yielding certifiable robustness guarantees validated against realistic attacks. Kaneko & Baldwin provide the single-model attack cost foundation; we provide the multi-judge composition theory. Shen et al. and Feng et al. certify evaluation quality under noise; we certify resistance under adversarial attacks.\n\n## Approach\nWe extend Robertson & Koyejo's TVD-MI framework from pairwise evaluation to N-agent multi-judge settings with certifiable manipulation-resistance bounds, drawing on the Gaussian-copula correlation model (Turkmen et al.) and information-theoretic diversity scaling (Yang et al.) for the formal machinery, and extending Kaneko & Baldwin's single-model attack cost bounds to multi-judge composition. Our contribution has five components:\n\n**Component 1: Theoretical Framework—The Adversarial Dual of Diversity Scaling.**\n\nWe prove that when K judge models evaluate candidate responses using TVD-MI scoring, the adversarial manipulation cost grows as Ω(K^{g(I_max)}), where g is an explicit decreasing function of the maximum pairwise mutual information I_max between judge signals. This establishes the adversarial dual of Yang et al.'s task-performance result: while their Theorem 4.3 shows residual uncertainty decreases as (1-α_c)^{K*}, we show manipulation cost increases polynomially in K with exponent determined by the same underlying correlation structure.\n\n**Proof Strategy (Three-Pillar Approach):**\n\n*Pillar 1—Strong Data Processing Inequality (SDPI) Composition.* We model each judge as a noisy channel from the 'true quality' signal to an evaluation score. Following Polyanskiy & Wu (2017), SDPI contraction coefficients compose multiplicatively across independent channels: an adversary pushing perturbation through K independent channels experiences η^K total contraction, where η ∈ (0,1) is the per-channel contraction coefficient. Under inter-judge correlation, the effective number of independent channels is reduced from K to K_eff. This extends Kaneko & Baldwin's single-channel result (N_min ≥ log₂(1/ε)/I_max) to multi-channel settings: the adversary's total information gain across K correlated judges is bounded by K_eff · I_max per query round.\n\n*Pillar 2—Fano-Ensemble Decomposition.* Following Morishita et al. (ICML 2022), we decompose the total MI I(Y; Z_1,...,Z_K) available to the aggregator into K individual relevance terms, pairwise redundancy terms involving I_max, and combination loss terms. The adversary must reduce this total MI below the Fano threshold for correct decision-making, and the required perturbation energy is lower-bounded by the effective information.\n\n*Pillar 3—Gaussian Copula Closed Form.* Adapting Turkmen et al.'s equicorrelated Gaussian copula model (where Z_j = √ρ·U + √(1-ρ)·ξ_j with shared latent factor U), we derive the effective independent channel count:\n\n  K_eff = 1 + (K-1)·exp(-2·I_max)\n\nwhere I_max = -½ log(1-ρ²) is the pairwise MI under the copula model. This formula is our own derivation, obtained by computing the effective rank of the K×K correlation matrix under equicorrelation: eigenvalues are λ₁ = 1+(K-1)ρ (multiplicity 1) and λ₂ = 1-ρ (multiplicity K-1), and the effective independent dimensionality follows from the ratio of total to maximum variance, expressed as a function of MI via the ρ-to-I_max mapping ρ² = 1-exp(-2·I_max).\n\nThe manipulation cost lower bound is then Ω(K_eff^{1/2}) from variance-reduction arguments (following Horvath et al.'s √K certified radius scaling for randomized smoothing ensembles), giving:\n\n  g(I_max) = ½ · log(1 + (K-1)·exp(-2·I_max)) / log(K)\n\nThis satisfies the boundary conditions: g(0) = ½·log(K)/log(K) = ½ for fully independent judges (matching √K variance reduction), and g(I_max) → 0 as I_max → ∞ (fully correlated judges collapse to a single effective channel). The ½ exponent for independent judges is tight under the variance-reduction argument; if the SDPI chain yields linear rather than √K scaling, we get g(0) = 1.\n\n*Key Lemma (Connection from MI to Perturbation Budget):* We connect information-theoretic bounds to operational manipulation cost via Marton's inequality: TV(P,Q)² ≤ ½·KL(P||Q), combined with Robertson & Koyejo's Theorem 3.3 relating TVD-MI to certification bounds. The adversary's perturbation must overcome the TVD gap, which scales with √K_eff under the copula model.\n\n*Distributional Assumptions:* The closed-form result requires the equicorrelated Gaussian copula on judge signals (marginals can be arbitrary; only the dependence structure is Gaussian) and equicorrelation (all pairwise MIs equal I_max). We prove a weaker but more general result under arbitrary pairwise MI structure: g depends on the minimum eigenvalue of the correlation matrix, giving g ≥ ½·λ_min(Σ). For heterogeneous correlation, we use the effective rank of the correlation matrix (analogous to Yang et al.'s K* = 2^{H(ρ)}) as a tighter proxy.\n\n**Component 2: Practical α Regime Analysis with Sensitivity Bounds.**\n\nUsing Turkmen et al.'s empirical copula correlations (within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5) and Kim et al.'s correlated error data (same-company +0.066, same-architecture +0.076; ICML 2025, arXiv 2506.07962), we estimate for the proposed three-judge cross-family ensemble:\n\n- Central estimate: ρ ≈ 0.45, I_max ≈ 0.11, α = g(I_max) ∈ [0.35, 0.65]\n- At α=0.5, K=7: manipulation cost ≈ 7^0.5 ≈ 2.65× single-judge baseline\n- At α=0.65, K=7: manipulation cost ≈ 7^0.65 ≈ 3.7×\n\n*Sensitivity analysis and break-even:* We explicitly plan for the possibility that empirically measured α falls outside our predicted range, since current correlation data is from prior-generation models (Kim et al.'s 350+ mostly older LLMs, Chen et al.'s 18 models from prior families). DeepSeek-V4, Qwen-3.5, and Llama-4-Maverick may show different correlation structures due to shared training data evolution (Common Crawl, synthetic data from frontier models) and partial architectural convergence (all three use MoE, though with different routing and attention mechanisms).\n\n- If α = 0.2 (more correlated than expected, ρ ≈ 0.65): K=7 yields only 7^0.2 ≈ 1.55× cost increase. The protocol still provides formal guarantees that majority voting cannot, but the practical margin is thin. At this α, our protocol's value proposition is primarily the certifiability—analogous to how randomized smoothing provides modest certified radii but with provable guarantees.\n- If α = 0.8 (more independent than expected, ρ ≈ 0.25): K=7 yields 7^0.8 ≈ 5.2× cost increase—substantially better than baseline. This would indicate that cross-family diversity is even more effective than prior-generation data suggested.\n- Break-even analysis: Majority voting with K=7 achieves empirical ASR reduction from 50-68% to 10-19% (SoK), a ~4-5× reduction in success probability. Our protocol must provide comparable ASR reduction plus formal guarantees to be justified. We identify the critical α threshold where the certified bound becomes vacuous (i.e., the formal guarantee is weaker than the trivially achievable baseline): for K=7, this occurs at approximately α ≤ 0.05, corresponding to ρ ≥ 0.95 (near-identical judges). For any realistic cross-family ensemble, we are well above this threshold.\n- Diminishing returns analysis: Following Jung & Na's (2604.00477) finding that scoring reliability scales logarithmically while discovery scales as N^0.69, we analyze whether our manipulation-cost scaling exhibits similar dissociation. The formal certified bound may saturate faster (logarithmically in K) than the empirical ASR reduction (which may follow a power law), creating a gap between what we can certify and what we observe.\n\n**Component 3: Practical Protocol Design.**\n\nWe instantiate the framework as a deployable multi-judge evaluation protocol using three architecturally diverse open-weight model families—DeepSeek-V4-Flash (284B MoE, 13B active, Multi-head Latent Attention), Qwen-3.5 (397B MoE, 17B active), and Llama-4-Maverick (400B MoE, 17B active). These models are chosen because: (a) they come from three different organizations with different training data pipelines, minimizing same-company correlation (+0.066 per Kim et al.); (b) they use different architectural innovations, minimizing same-architecture correlation (+0.076); (c) Turkmen et al.'s copula framework predicts cross-family ρ~0.4-0.5 for such configurations.\n\nThe protocol operates in three phases:\n1. **Independence measurement:** Compute pairwise TVD-MI scores between all judge pairs on a calibration set; estimate the copula correlation ρ_ij and I_max; compute effective channel count K* (à la Yang et al.) and predicted α.\n2. **Evaluation with certified scoring:** Each judge evaluates candidates using TVD-MI; the aggregator combines scores via DMI-weighted aggregation (adapting PEG's determinant-based scoring from Chen et al., NeurIPS 2025), which provides dominant-strategy truthfulness (Lemma 1) when judges are approximately conditionally independent.\n3. **Certification:** Output both the aggregated evaluation and the certified manipulation-cost bound Ω(K^α) with the empirically measured α, constituting a per-evaluation robustness certificate.\n\nWe prove the coordination failure argument leveraging both PEG's dominant-strategy result (which applies under conditional independence) and Qiu et al.'s BNE framework (which applies under the weaker shared-prior assumption). For the regime between these extremes—partial correlation that violates conditional independence but maintains bounded MI—we provide interpolating bounds via the SDPI framework.\n\n**Component 4: Certifiable Robustness Framing.**\n\nWe explicitly frame our contribution as 'certifiable robustness for LLM evaluation,' drawing the analogy to certified adversarial robustness in classification (randomized smoothing, interval bound propagation). Just as certified adversarial defenses often achieve smaller empirical improvements than heuristic defenses but provide provable guarantees, our protocol may achieve ASR reductions comparable to majority voting but with formal certificates. The value proposition is:\n\n- Majority voting: empirically reduces ASR from ~60% to ~15% for K=7 (SoK), but with no formal guarantee—the ASR could spike under novel attacks.\n- Our protocol: achieves comparable empirical ASR reduction AND provides a formal lower bound on the manipulation cost that scales as Ω(K^α), certified per-evaluation. This means even against unforeseen future attacks, the manipulation cost is provably bounded below.\n- Connection to single-model bounds: Kaneko & Baldwin's N_min ≥ log₂(1/ε)/I_max provides the per-judge attack cost floor; our multi-judge composition shows that the adversary's total cost scales as K_eff times this single-judge bound, yielding certifiable multi-judge manipulation resistance.\n\nThis framing directly addresses the concern that 2.65-4.0× scaling may seem modest: in certified adversarial robustness, even modest certified radii are valued because they are provable, while large empirical margins can be broken by adaptive attacks.\n\n**Component 5: Realistic Adversarial Validation.**\n\nWe evaluate against RobustJudge's 15 attack methods (including PAIR, combined attacks, adversarial suffixes, and prompt injection) plus the SoK's documented attack vectors, on text summarization, code generation, and knowledge-intensive QA tasks. We benchmark against: (a) all 7 RobustJudge heuristic defenses; (b) CAP comparative augmented prompting; (c) CollabEval's consensus-based multi-agent approach; (d) Ebrahimi et al.'s credibility-scoring framework; (e) Robertson & Koyejo's single-evaluator TVD-MI baseline; (f) simple majority voting (K=3,5,7); (g) PEG with DMI scoring (Chen et al.). For each experimental condition, we report: (i) attack success rate, (ii) empirically measured ρ_ij and I_max, (iii) computed α, (iv) the gap between the certified manipulation-cost bound and the observed empirical manipulation cost, and (v) whether the formal bound is tight (ratio of empirical to certified). Following the score-coverage dissociation insight (Jung & Na), we separately analyze certification tightness (how close the formal bound is to the empirical one) and attack surface coverage (what fraction of attack types the bound holds against).\n\n## Resource Estimate\n{'manual': {'gpu_hours': '1,000-1,500 H100-equivalent', 'timeline': '14-18 weeks', 'estimated_gpu_cost': '$2,500-$3,750 at $2.50/hr H100 spot', 'gpu_breakdown': 'DeepSeek-V4-Flash: 2×H100 FP8 (~160GB VRAM); Qwen-3.5: 4×H100 INT4 (~200GB) or 8×H100 FP8 (~400GB); Llama-4-Maverick: 4×H100 INT4 (~200GB) or 8×H100 FP8 (~400GB). Running all 3 simultaneously: 10×H100 (INT4) to 18×H100 (FP8). Per-experiment: single-judge baselines across 15 attacks × 3 tasks × 3 models ≈ 450 H100-hrs; multi-judge protocol evaluation across 45 conditions on 10-GPU cluster ≈ 500 H100-hrs; signal independence measurement, copula fitting, and α estimation ≈ 100 H100-hrs; ablations (K=1,2,3,5,7 judges, homogeneous vs. heterogeneous) ≈ 200 H100-hrs; development/debugging ≈ 150 H100-hrs'}, 'human_in_loop': {'gpu_hours': '800-1,200 H100-equivalent', 'timeline': '10-14 weeks', 'claude_api_cost': '$400-$600 (Sonnet 4.6 for code generation, proof assistance, paper drafting; ~130-200M tokens)', 'estimated_gpu_cost': '$2,000-$3,000 at $2.50/hr H100 spot', 'gpu_breakdown': 'Same per-model requirements; efficiency gains from Claude-assisted theorem proving, experiment scheduling, and copula fitting, reducing wasted debugging runs by ~20%'}, 'auto_research': {'gpu_hours': '1,200-1,800 H100-equivalent', 'timeline': '6-9 weeks', 'claude_api_cost': '$1,200-$2,000 (Opus 4.7 for theorem proving, SDPI chain verification, experiment design; ~250-400M tokens)', 'estimated_gpu_cost': '$3,000-$4,500 at $2.50/hr H100 spot', 'speed_bottleneck': 'The three-pillar proof strategy (SDPI + Fano + copula) has well-defined mathematical components that autonomous systems can work on in parallel, but ensuring the chain composes correctly across the three pillars requires human mathematical judgment. The key risk is that the SDPI contraction yields a weaker-than-expected bound, requiring fallback to the √K variance-reduction argument.'}}\n\n## Inspired By\nThe convergence of seven lines of work: (1) Robertson & Koyejo's bounded f-divergence theory for single-evaluator manipulation resistance; (2) The dual peer prediction results—Qiu et al.'s BNE and Chen et al.'s dominant-strategy PEG—providing complementary incentive-compatibility guarantees; (3) Yang et al.'s information-theoretic diversity-scaling framework establishing the task-performance scaling law via effective channel count K*—we provide the adversarial dual; (4) Turkmen et al.'s Gaussian-copula model with its error floor theorem and MI decomposition, which provides the mathematical foundation from which we derive our closed-form K_eff; (5) Kaneko & Baldwin's tight single-model information-theoretic attack cost bounds (N_min ≥ log₂(1/ε)/I_max), which we extend to multi-judge composition; (6) The SoK's empirical finding that 7-model committees reduce ASR to 10–19% without formal explanation; (7) The behavioral entanglement and correlated error literature (Chen et al. 2604.07650, Kim et al. ICML 2025) providing quantitative inter-judge independence measurements. We unify these into a certifiable manipulation-resistance framework where the certified bound is an explicit function of measurable signal correlation.\n\n## Target Venues\n- AAAI 2027 Main Technical Track (abstract: July 21, 2026; full paper: July 28, 2026; primary target—theory + experiments with certified robustness framing)\n- USENIX Security 2027 Cycle 1 (abstract: August 18, 2026; full paper: August 25, 2026; security-focused version emphasizing certifiable robustness against realistic attacks)\n- NeurIPS 2026 Workshops (contributed papers: ~August 29, 2026; workshop version connecting to the diversity-scaling and certified robustness communities)\n- ICLR 2027 (estimated deadline: October 2026; polished archival version with extended theory, comprehensive experiments, and tightness analysis)\n\n## Key References\n- Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes (Robertson & Koyejo, arXiv 2508.05469, 2025) — foundational TVD-MI theory, Theorem 3.3 polynomial certification bounds, primary work we extend\n- Identity-Link IRT for Label-Free LLM Evaluation: Preserving Additivity in TVD-MI Scores (Robertson, arXiv 2510.14966, 2025) — sparse TVD-MI evaluation, two-judge preliminary validation\n- Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction (Qiu et al., ICLR 2026, 2601.20299) — BNE incentive-compatibility for LLM peer prediction, inverse scaling property\n- Incentivizing Truthful Language Models via Peer Elicitation Games (Chen et al., NeurIPS 2025, 2505.13636) — DMI-based multi-agent peer elicitation with dominant strategy truthfulness (Lemma 1), sublinear O(√T) regret bound (Theorem 2), last-iterate convergence to Nash equilibrium (Theorem 3) via online mirror descent; experiments use 3 discriminators (n≥2 required by Lemma 1)\n- Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity (Yang et al., ICLR 2026 Workshop AIMS, 2602.03794) — information-theoretic diversity-scaling framework: effective channel count K* = 2^{H(ρ)}, residual uncertainty (1-α_c)^{K*} geometric contraction (Theorem 4.3), heterogeneity advantage (Corollary 4.4); we provide the adversarial dual of their task-performance result\n- Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection (Turkmen et al., arXiv 2602.08003, 2026) — Gaussian-copula correlated error model (Z_j = √ρ·U + √(1-ρ)·ξ_j), information-theoretic error floor Φ(Φ⁻¹(1-p)/√ρ) (Theorem 4.4), three-term MI decomposition into accuracy-redundancy-error correlation (Theorem 4.3); copula model provides the mathematical foundation from which we derive our K_eff formula\n- Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs (Kaneko & Baldwin, NeurIPS 2025 spotlight, arXiv 2510.17000) — tight single-model attack cost bound N_min ≥ log₂(1/ε)/I_max via K-ary Fano inequality (Theorem 1), achieved by SPRT (Theorem 2); validated across 7 LLMs including Llama-4 and DeepSeek-R1; provides single-channel foundation that we extend to multi-judge composition\n- Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation (Shen et al., arXiv 2604.03257, Google DeepMind/UCL, 2026) — constrained MLE fusing human labels, LLM-judge annotations, and domain constraints for certified performance estimation; addresses honest-judge noise, not adversarial manipulation; occupies adjacent 'certifiable evaluation' space\n- Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges (Feng, Shen, Balashankar, Gerner-Beuerle & Rodrigues, ICLR 2026, arXiv 2601.20913) — statistical hypothesis testing framework for LLM evaluation certification with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty; variance-corrected thresholds using judge TPR/FPR estimation; assumes honest but fallible judges, not adversarial manipulation; complements Shen et al. in the 'certifiable evaluation' space\n- Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation (Jung & Na, arXiv 2604.00477, 2026) — score-coverage dissociation: scoring reliability scales logarithmically, discovery follows power law N^0.69; informs our analysis of when certified bounds saturate vs. empirical gains\n- Security in LLM-as-a-Judge: A Comprehensive SoK (arXiv 2603.29403, April 2026) — comprehensive vulnerability catalog, 50-68% ASR on open-source, 7-model committee reduces ASR to 10-19%; primary empirical evidence for diversity benefit without formal explanation\n- LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge (arXiv 2506.09443, 2025) — RobustJudge benchmark, 15 attacks, 7 defenses, 12 models\n- Correlated Errors in Large Language Models (Kim, Garg, Peng & Garg, ICML 2025, arXiv 2506.07962) — error correlation across 350+ LLMs: 60% agreement when both err (vs 33% baseline), same-company +0.066, same-architecture +0.076; KEY for α regime analysis\n- How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement (Chen et al., arXiv 2604.07650, 2026) — BEI and CIG metrics across 18 LLMs from 6 families; cross-family entanglement 40-60% lower than intra-family\n- Benchmark Illusion: Disagreement among LLMs and Its Scientific Consequences (arXiv 2602.11898, 2026) — 16-38% disagreement among top frontier models despite similar accuracy\n- Strong Data-Processing Inequalities for Channels and Bayesian Networks (Polyanskiy & Wu, arXiv 1508.06025, 2017) — SDPI contraction coefficients compose multiplicatively; foundational for our Pillar 1 proof strategy\n- Rethinking Fano's Inequality in Ensemble Learning (Morishita et al., ICML 2022, arXiv 2205.12683) — decomposes Fano bound for ensembles into relevance, redundancy, and combination loss; foundational for our Pillar 2 proof strategy\n- On the Certified Robustness for Ensemble Models and Beyond (Chen et al., arXiv 2107.10873, 2021) — diversified gradient + large confidence margin jointly necessary and sufficient for certified ensemble robustness\n- Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al., arXiv 2106.06946, 2021) — ensemble variance reduction yields √K-type certified radius improvement; precedent for polynomial scaling from diversity\n- Information-Theoretically Optimal Adversarial Attacks (Yi et al., arXiv 2007.14042, 2020) — proves attack cost scales up with number of redundant signal copies; direct precedent for manipulation cost scaling with K\n- On the Fragility of AI Agent Collusion (Keppo et al., arXiv 2603.20281, 2026) — increasing LLM count 2→5 breaks collusion (+22%→+3%); same-family size heterogeneity stabilizes via leader-follower; motivates cross-family diversity\n- CollabEval: Multi-Agent Collaborative Evaluation (arXiv 2603.00993, March 2026) — three-phase multi-agent evaluation without formal adversarial guarantees\n- An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring (Ebrahimi et al., IJCNLP-AACL 2025, arXiv 2505.24239) — credibility-based iterative aggregation; game-theoretic but not information-theoretic\n- Certifying Joint Adversarial Robustness for Model Ensembles (Chiang et al., arXiv 2004.10250, 2020) — vulnerability space disjointness for ensemble certification\n- Peer Prediction with More Signals than Reports (Frongillo et al., arXiv 2503.16280, 2025) — fine-grained signals destabilize uninformative equilibria\n- Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)\n- Improving Your Model Ranking on Chatbot Arena by Vote Rigging (ICML 2025)\n- am-ELO: A Stable Framework for Arena-based LLM Evaluation (ICML 2025 Poster)\n- CAP: Improving the Robustness of LLM-as-a-Judge Against Adversarial Score Manipulation via Comparative Augmented Prompting (OpenReview 2026)\n- Aligned Textual Scoring Rules (Lu et al., arXiv 2507.06221, 2025)\n- Can You Trick the Grader? Adversarial Persuasion of LLM Judges (EMNLP 2025 Findings)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:43:55.354Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:43:55.354Z",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---

## Round 1

43 recorded events

### User

_source line 3 · 2026-05-20T04:43:55.366Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure

## Description
LLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025) proved bounded f-divergence certification guarantees for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026, via BNE; Chen et al., NeurIPS 2025, via dominant-strategy DMI), and Kaneko & Baldwin (NeurIPS 2025 spotlight) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling—the adversarial dual of the task-performance scaling recently established by Yang et al. (ICLR 2026 Workshop AIMS). We bridge this gap by proving that adversarial manipulation cost grows as Ω(K^{g(I_max)}) where g is an explicit decreasing function of inter-judge signal correlation, derived via a three-pillar proof strategy: (1) SDPI contraction composition (Polyanskiy & Wu) showing perturbation decays multiplicatively across independent channels; (2) Fano-ensemble decomposition (Morishita et al., ICML 2022) separating relevance, redundancy, and combination loss; (3) Gaussian-copula closed form—adapting Turkmen et al.'s equicorrelated model, we derive K_eff = 1+(K-1)·exp(-2·I_max). Under the copula model, g(I_max) = ½·log(K_eff)/log(K), which equals ½ for independent judges (matching √K certified radius scaling from randomized smoothing) and degrades gracefully with correlation. For cross-family ensembles (DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick), we estimate α ∈ [0.35, 0.65] based on copula correlations ρ~0.4-0.5 (Turkmen et al.) and correlated error measurements (Kim et al., ICML 2025), providing certified manipulation-cost bounds of 2.6–3.7× for K=7. We frame this as certifiable robustness for LLM evaluation: just as certified adversarial defenses provide provable guarantees despite sometimes modest empirical margins, our protocol certifies per-evaluation manipulation-resistance bounds that hold against arbitrary future attacks—a guarantee majority voting fundamentally cannot provide. We validate against RobustJudge's 15 realistic attack methods, reporting certified bounds alongside empirical ASR, with sensitivity analysis for α ∈ [0.2, 0.8].

## Core Problem
Can we provide certifiable manipulation-resistance guarantees for N-judge LLM evaluation protocols, where the certified robustness bound is an explicit, computable function of measurable inter-judge signal correlation, validated against realistic adversarial attacks?

## Opportunity
Robertson & Koyejo (2025) established that bounded f-divergences like TVD maintain polynomial certification guarantees under adversarial manipulation while unbounded measures (KL) fail (Theorem 3.3), and multiple concurrent works have established peer prediction incentive-compatibility for LLM evaluation (Qiu et al., ICLR 2026; Chen et al., NeurIPS 2025). However, three critical gaps remain: (1) No existing work provides formal N-agent scaling results connecting manipulation cost to measurable inter-judge signal correlation—Robertson & Koyejo analyze pairwise evaluations without multi-judge aggregation theory, Qiu et al. provide no polynomial cost bounds tied to judge count, and Chen et al.'s PEG dominant-strategy guarantee requires conditional independence without characterizing degradation under partial correlation; (2) Empirical validation uses only generic semantic-preserving transforms or deceptive finetuning, not realistic attack vectors documented by the SoK (prompt injection ASR 50–68%, adversarial suffixes, strategic vote rigging); (3) The information-theoretic diversity-scaling framework of Yang et al. (ICLR 2026 Workshop AIMS) shows that multi-agent system performance is bounded by effective channel count K* with residual uncertainty decaying as (1-α_c)^{K*}, but this addresses task performance, not adversarial manipulation resistance—no work establishes the dual result for manipulation cost. Meanwhile, Turkmen et al. (2602.08003) prove that correlated ensembles hit an irreducible error floor Φ(Φ⁻¹(1-p)/√ρ) under their Gaussian copula model, and their three-term MI decomposition (accuracy - redundancy + error correlation) provides the mathematical toolkit for our α estimation. Kaneko & Baldwin (NeurIPS 2025 spotlight) prove tight single-model information-theoretic attack cost bounds N_min ≥ log₂(1/ε)/I_max via Fano inequality, but do not address multi-judge composition. The SoK (2603.29403) finds that 7-model committees empirically reduce ASR to 10–19% but provides no formal explanation. We aim to bridge these gaps by providing the adversarial-robustness dual of the task-performance scaling theory, yielding certifiable manipulation-resistance bounds analogous to certified adversarial robustness in classification.

## Landscape
Robertson & Koyejo's 'Let's Measure Information Step-by-Step' (arXiv 2508.05469, under TMLR review) formalizes LLM evaluation as an information elicitation game using TVD-MI, proves that bounded f-divergences maintain polynomial certification guarantees under mode-collapse attacks (Theorem 3.3) while unbounded measures like KL degrade exponentially, and demonstrates TVD-MI effectiveness (AUC 0.70–0.77) under generic semantic transforms. Their Identity-Link IRT follow-up (2510.14966) extends to sparse evaluation with two-judge validation (Spearman ρ=0.872) but without formal multi-judge theory.

Qiu et al.'s 'Truthfulness Despite Weak Supervision' (ICLR 2026, 2601.20299) applies peer prediction to LLM evaluation/training with Bayesian Nash equilibrium guarantees (Theorem 1) and an empirical inverse scaling property, but targets output truthfulness rather than adversarial robustness of the evaluation protocol itself, acknowledges only unilateral deception (not collusion), and uses no information-theoretic divergence measures.

Chen et al.'s 'Incentivizing Truthful Language Models via Peer Elicitation Games' (NeurIPS 2025, 2505.13636) introduces multi-agent peer elicitation using Determinant Mutual Information (DMI) scoring and proves a strictly stronger result: dominant strategy truthfulness (Lemma 1), meaning truthful reporting is optimal regardless of other agents' strategies—not just in Bayesian Nash equilibrium. Their sublinear O(√T) regret bound (Theorem 2) and last-iterate convergence to Nash equilibrium (Theorem 3) via online mirror descent provide a complementary theoretical foundation to Qiu et al.'s BNE. PEG requires n≥2 discriminators and K_t≥4 tasks with conditional independence (Assumption 4), and their experiments use 3 discriminators with the theoretical minimum n≥2 and K_t≥4 tasks required by Lemma 1. However, PEG does not characterize how its manipulation-resistance guarantees degrade when the conditional independence assumption is violated—precisely the regime we analyze.

Yang et al.'s 'Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity' (ICLR 2026 Workshop AIMS, 2602.03794) provides an information-theoretic framework where multi-agent system performance is bounded by intrinsic task uncertainty H(Y|X) with residual uncertainty decaying as (1-α_c)^{K*}, where α_c is the complementarity rate and K* = 2^{H(ρ)} is the effective channel count computed via von Neumann entropy of the embedding Gram matrix (Theorem 4.3). Their heterogeneity advantage corollary (Corollary 4.4) formally shows α_het·K_het > α_hom·K_hom implies strictly better performance. Critically, K* captures diversity in embedding space without labels and empirically correlates with accuracy (r=0.388 overall, r=0.535 for K*_c among correct agents). However, their framework addresses task performance (information recovery) not adversarial manipulation resistance (information perturbation cost). Our work establishes the adversarial dual: while their K* governs how quickly residual uncertainty decreases, our framework shows that the same correlation structure governs how quickly manipulation cost increases.

Turkmen et al.'s 'Don't Always Pick the Highest-Performing Model' (arXiv 2602.08003, Feb 2026) formulates ensemble selection as MI maximization with a Gaussian-copula correlated error model and proves an information-theoretic error floor (Theorem 4.4): lim_{m→∞} P_e = Φ(Φ⁻¹(1-p)/√ρ) > 0 for equicorrelated ensembles with pairwise copula correlation ρ. Their three-term MI decomposition (Theorem 4.3)—Δ(j|S) = I(Y;X_j) - I(X_j;X_S) + I(E_j;E_S)—separates accuracy, redundancy, and error correlation. Empirically, they find within-family correlations ρ~0.7-0.8 and cross-family ρ~0.4-0.5. Their copula model provides the mathematical foundation for our derivation of effective independent channel count K_eff.

Kaneko & Baldwin's 'Bits Leaked per Query' (NeurIPS 2025 spotlight, arXiv 2510.17000) establishes tight information-theoretic bounds on adversarial attack costs against individual LLMs: any adaptive attack achieving error ≤ ε requires at least N_min ≥ log₂(1/ε)/I_max queries, where I_max is the maximum per-query mutual information leakage (Theorem 1), and this bound is achieved by sequential probability ratio tests (Theorem 2). Validated across 7 LLMs including Llama-4 and DeepSeek-R1, they identify four disclosure regimes (answer-only ~0.001-0.01 bits to full-access ~1.0+ bits). This provides the single-model information-theoretic attack cost foundation; our work extends the composition theory to multi-judge settings where an adversary must simultaneously fool K correlated judges.

Shen et al.'s 'Robust LLM Performance Certification via Constrained MLE' (arXiv 2604.03257, Google DeepMind/UCL, 2026) proposes constrained maximum likelihood estimation fusing human labels, LLM-judge annotations, and domain constraints (known TPR/FPR bounds) for certified LLM performance estimation. While addressing performance certification under benign judge noise, it assumes honest judges and does not model adversarial manipulation—precisely the threat model we address.

Feng et al.'s 'Noisy but Valid' (ICLR 2026, arXiv 2601.20913) provides a statistical hypothesis testing framework for certifying LLM failure rates using imperfect judges, with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty. Using a small human-labeled calibration set to estimate judge TPR/FPR, they derive variance-corrected critical thresholds (Theorem 5.4 gives exact conditions for judge adoption). Like Shen et al., this assumes honest but fallible judges, not adversarial manipulation. Our work complements both: Shen et al. certify performance estimates via constrained MLE, Feng et al. certify statistical validity via hypothesis testing, and we certify manipulation resistance under adversarial attacks.

Jung & Na's 'Logarithmic Scores, Power-Law Discoveries' (arXiv 2604.00477, April 2026) identifies a score-coverage dissociation in multi-agent evaluation panels: scoring reliability (ICC) scales logarithmically with panel size N (R²=0.974) while unique issue discovery follows a sublinear power law y=7.8·N^0.69 (R²=0.999). Scores saturate ~2× faster than discoveries, with N=8 achieving 82% of maximum scoring reliability but only ~42% of N=32 discovery level. This has direct implications for our K-scaling claims: manipulation-cost scaling benefits may exhibit similar dissociation, where formal robustness guarantees saturate faster than empirical coverage of attack surface. We analyze this explicitly.

The SoK on LLM-as-Judge Security (2603.29403, April 2026) catalogs extensive vulnerabilities: open-source models showing 50–68% average ASR and frontier models 27–44%; 7-model diverse committees reduce ASR to 10–19% empirically but without formal explanation. RobustJudge (2506.09443) benchmarks 15 attack methods and 7 defense strategies. CAP (OpenReview 2026) shows comparative assessment is more robust than absolute scoring but provides no formal guarantees.

On error correlation and independence: Kim et al.'s 'Correlated Errors in Large Language Models' (ICML 2025, arXiv 2506.07962) shows 60% pairwise agreement when both err on Helm (vs. 33% random baseline), with same-company adding +0.066 and same-architecture adding +0.076 agreement. Chen et al.'s behavioral entanglement framework (arXiv 2604.07650) introduces BEI and CIG metrics across 18 LLMs from 6 families, finding cross-family entanglement 40–60% lower than intra-family.

On coordination failure: Frongillo et al. (2503.16280) prove that uninformative equilibria become unstable with fine-grained signals. Keppo et al.'s collusion fragility analysis (2603.20281) finds increasing LLM count from 2→5 breaks collusion (+22%→+3%), but same-family size heterogeneity stabilizes via leader-follower dynamics—motivating cross-family diversity.

On multi-agent evaluation: CollabEval (2603.00993) proposes three-phase multi-agent evaluation without formal adversarial guarantees. Ebrahimi et al. (IJCNLP-AACL 2025, 2505.24239) uses credibility-based iterative aggregation for adversary resistance without information-theoretic measures.

On certified ensemble robustness: Chen et al. (2107.10873) prove that diversified gradient and large confidence margin are jointly necessary and sufficient for certified ensemble robustness—standard ensembles achieve only marginal improvements without explicit diversity. Horvath et al. (2106.06946) show randomized smoothing ensembles achieve √K-type certified radius improvement. These provide precedent for polynomial scaling bounds from diversity.

THE KEY GAP: No existing work provides formal N-agent manipulation-cost scaling results—the adversarial dual of Yang et al.'s task-performance scaling—where the bound is an explicit computable function of measurable inter-judge signal correlation, yielding certifiable robustness guarantees validated against realistic attacks. Kaneko & Baldwin provide the single-model attack cost foundation; we provide the multi-judge composition theory. Shen et al. and Feng et al. certify evaluation quality under noise; we certify resistance under adversarial attacks.

## Approach
We extend Robertson & Koyejo's TVD-MI framework from pairwise evaluation to N-agent multi-judge settings with certifiable manipulation-resistance bounds, drawing on the Gaussian-copula correlation model (Turkmen et al.) and information-theoretic diversity scaling (Yang et al.) for the formal machinery, and extending Kaneko & Baldwin's single-model attack cost bounds to multi-judge composition. Our contribution has five components:

**Component 1: Theoretical Framework—The Adversarial Dual of Diversity Scaling.**

We prove that when K judge models evaluate candidate responses using TVD-MI scoring, the adversarial manipulation cost grows as Ω(K^{g(I_max)}), where g is an explicit decreasing function of the maximum pairwise mutual information I_max between judge signals. This establishes the adversarial dual of Yang et al.'s task-performance result: while their Theorem 4.3 shows residual uncertainty decreases as (1-α_c)^{K*}, we show manipulation cost increases polynomially in K with exponent determined by the same underlying correlation structure.

**Proof Strategy (Three-Pillar Approach):**

*Pillar 1—Strong Data Processing Inequality (SDPI) Composition.* We model each judge as a noisy channel from the 'true quality' signal to an evaluation score. Following Polyanskiy & Wu (2017), SDPI contraction coefficients compose multiplicatively across independent channels: an adversary pushing perturbation through K independent channels experiences η^K total contraction, where η ∈ (0,1) is the per-channel contraction coefficient. Under inter-judge correlation, the effective number of independent channels is reduced from K to K_eff. This extends Kaneko & Baldwin's single-channel result (N_min ≥ log₂(1/ε)/I_max) to multi-channel settings: the adversary's total information gain across K correlated judges is bounded by K_eff · I_max per query round.

*Pillar 2—Fano-Ensemble Decomposition.* Following Morishita et al. (ICML 2022), we decompose the total MI I(Y; Z_1,...,Z_K) available to the aggregator into K individual relevance terms, pairwise redundancy terms involving I_max, and combination loss terms. The adversary must reduce this total MI below the Fano threshold for correct decision-making, and the required perturbation energy is lower-bounded by the effective information.

*Pillar 3—Gaussian Copula Closed Form.* Adapting Turkmen et al.'s equicorrelated Gaussian copula model (where Z_j = √ρ·U + √(1-ρ)·ξ_j with shared latent factor U), we derive the effective independent channel count:

  K_eff = 1 + (K-1)·exp(-2·I_max)

where I_max = -½ log(1-ρ²) is the pairwise MI under the copula model. This formula is our own derivation, obtained by computing the effective rank of the K×K correlation matrix under equicorrelation: eigenvalues are λ₁ = 1+(K-1)ρ (multiplicity 1) and λ₂ = 1-ρ (multiplicity K-1), and the effective independent dimensionality follows from the ratio of total to maximum variance, expressed as a function of MI via the ρ-to-I_max mapping ρ² = 1-exp(-2·I_max).

The manipulation cost lower bound is then Ω(K_eff^{1/2}) from variance-reduction arguments (following Horvath et al.'s √K certified radius scaling for randomized smoothing ensembles), giving:

  g(I_max) = ½ · log(1 + (K-1)·exp(-2·I_max)) / log(K)

This satisfies the boundary conditions: g(0) = ½·log(K)/log(K) = ½ for fully independent judges (matching √K variance reduction), and g(I_max) → 0 as I_max → ∞ (fully correlated judges collapse to a single effective channel). The ½ exponent for independent judges is tight under the variance-reduction argument; if the SDPI chain yields linear rather than √K scaling, we get g(0) = 1.

*Key Lemma (Connection from MI to Perturbation Budget):* We connect information-theoretic bounds to operational manipulation cost via Marton's inequality: TV(P,Q)² ≤ ½·KL(P||Q), combined with Robertson & Koyejo's Theorem 3.3 relating TVD-MI to certification bounds. The adversary's perturbation must overcome the TVD gap, which scales with √K_eff under the copula model.

*Distributional Assumptions:* The closed-form result requires the equicorrelated Gaussian copula on judge signals (marginals can be arbitrary; only the dependence structure is Gaussian) and equicorrelation (all pairwise MIs equal I_max). We prove a weaker but more general result under arbitrary pairwise MI structure: g depends on the minimum eigenvalue of the correlation matrix, giving g ≥ ½·λ_min(Σ). For heterogeneous correlation, we use the effective rank of the correlation matrix (analogous to Yang et al.'s K* = 2^{H(ρ)}) as a tighter proxy.

**Component 2: Practical α Regime Analysis with Sensitivity Bounds.**

Using Turkmen et al.'s empirical copula correlations (within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5) and Kim et al.'s correlated error data (same-company +0.066, same-architecture +0.076; ICML 2025, arXiv 2506.07962), we estimate for the proposed three-judge cross-family ensemble:

- Central estimate: ρ ≈ 0.45, I_max ≈ 0.11, α = g(I_max) ∈ [0.35, 0.65]
- At α=0.5, K=7: manipulation cost ≈ 7^0.5 ≈ 2.65× single-judge baseline
- At α=0.65, K=7: manipulation cost ≈ 7^0.65 ≈ 3.7×

*Sensitivity analysis and break-even:* We explicitly plan for the possibility that empirically measured α falls outside our predicted range, since current correlation data is from prior-generation models (Kim et al.'s 350+ mostly older LLMs, Chen et al.'s 18 models from prior families). DeepSeek-V4, Qwen-3.5, and Llama-4-Maverick may show different correlation structures due to shared training data evolution (Common Crawl, synthetic data from frontier models) and partial architectural convergence (all three use MoE, though with different routing and attention mechanisms).

- If α = 0.2 (more correlated than expected, ρ ≈ 0.65): K=7 yields only 7^0.2 ≈ 1.55× cost increase. The protocol still provides formal guarantees that majority voting cannot, but the practical margin is thin. At this α, our protocol's value proposition is primarily the certifiability—analogous to how randomized smoothing provides modest certified radii but with provable guarantees.
- If α = 0.8 (more independent than expected, ρ ≈ 0.25): K=7 yields 7^0.8 ≈ 5.2× cost increase—substantially better than baseline. This would indicate that cross-family diversity is even more effective than prior-generation data suggested.
- Break-even analysis: Majority voting with K=7 achieves empirical ASR reduction from 50-68% to 10-19% (SoK), a ~4-5× reduction in success probability. Our protocol must provide comparable ASR reduction plus formal guarantees to be justified. We identify the critical α threshold where the certified bound becomes vacuous (i.e., the formal guarantee is weaker than the trivially achievable baseline): for K=7, this occurs at approximately α ≤ 0.05, corresponding to ρ ≥ 0.95 (near-identical judges). For any realistic cross-family ensemble, we are well above this threshold.
- Diminishing returns analysis: Following Jung & Na's (2604.00477) finding that scoring reliability scales logarithmically while discovery scales as N^0.69, we analyze whether our manipulation-cost scaling exhibits similar dissociation. The formal certified bound may saturate faster (logarithmically in K) than the empirical ASR reduction (which may follow a power law), creating a gap between what we can certify and what we observe.

**Component 3: Practical Protocol Design.**

We instantiate the framework as a deployable multi-judge evaluation protocol using three architecturally diverse open-weight model families—DeepSeek-V4-Flash (284B MoE, 13B active, Multi-head Latent Attention), Qwen-3.5 (397B MoE, 17B active), and Llama-4-Maverick (400B MoE, 17B active). These models are chosen because: (a) they come from three different organizations with different training data pipelines, minimizing same-company correlation (+0.066 per Kim et al.); (b) they use different architectural innovations, minimizing same-architecture correlation (+0.076); (c) Turkmen et al.'s copula framework predicts cross-family ρ~0.4-0.5 for such configurations.

The protocol operates in three phases:
1. **Independence measurement:** Compute pairwise TVD-MI scores between all judge pairs on a calibration set; estimate the copula correlation ρ_ij and I_max; compute effective channel count K* (à la Yang et al.) and predicted α.
2. **Evaluation with certified scoring:** Each judge evaluates candidates using TVD-MI; the aggregator combines scores via DMI-weighted aggregation (adapting PEG's determinant-based scoring from Chen et al., NeurIPS 2025), which provides dominant-strategy truthfulness (Lemma 1) when judges are approximately conditionally independent.
3. **Certification:** Output both the aggregated evaluation and the certified manipulation-cost bound Ω(K^α) with the empirically measured α, constituting a per-evaluation robustness certificate.

We prove the coordination failure argument leveraging both PEG's dominant-strategy result (which applies under conditional independence) and Qiu et al.'s BNE framework (which applies under the weaker shared-prior assumption). For the regime between these extremes—partial correlation that violates conditional independence but maintains bounded MI—we provide interpolating bounds via the SDPI framework.

**Component 4: Certifiable Robustness Framing.**

We explicitly frame our contribution as 'certifiable robustness for LLM evaluation,' drawing the analogy to certified adversarial robustness in classification (randomized smoothing, interval bound propagation). Just as certified adversarial defenses often achieve smaller empirical improvements than heuristic defenses but provide provable guarantees, our protocol may achieve ASR reductions comparable to majority voting but with formal certificates. The value proposition is:

- Majority voting: empirically reduces ASR from ~60% to ~15% for K=7 (SoK), but with no formal guarantee—the ASR could spike under novel attacks.
- Our protocol: achieves comparable empirical ASR reduction AND provides a formal lower bound on the manipulation cost that scales as Ω(K^α), certified per-evaluation. This means even against unforeseen future attacks, the manipulation cost is provably bounded below.
- Connection to single-model bounds: Kaneko & Baldwin's N_min ≥ log₂(1/ε)/I_max provides the per-judge attack cost floor; our multi-judge composition shows that the adversary's total cost scales as K_eff times this single-judge bound, yielding certifiable multi-judge manipulation resistance.

This framing directly addresses the concern that 2.65-4.0× scaling may seem modest: in certified adversarial robustness, even modest certified radii are valued because they are provable, while large empirical margins can be broken by adaptive attacks.

**Component 5: Realistic Adversarial Validation.**

We evaluate against RobustJudge's 15 attack methods (including PAIR, combined attacks, adversarial suffixes, and prompt injection) plus the SoK's documented attack vectors, on text summarization, code generation, and knowledge-intensive QA tasks. We benchmark against: (a) all 7 RobustJudge heuristic defenses; (b) CAP comparative augmented prompting; (c) CollabEval's consensus-based multi-agent approach; (d) Ebrahimi et al.'s credibility-scoring framework; (e) Robertson & Koyejo's single-evaluator TVD-MI baseline; (f) simple majority voting (K=3,5,7); (g) PEG with DMI scoring (Chen et al.). For each experimental condition, we report: (i) attack success rate, (ii) empirically measured ρ_ij and I_max, (iii) computed α, (iv) the gap between the certified manipulation-cost bound and the observed empirical manipulation cost, and (v) whether the formal bound is tight (ratio of empirical to certified). Following the score-coverage dissociation insight (Jung & Na), we separately analyze certification tightness (how close the formal bound is to the empirical one) and attack surface coverage (what fraction of attack types the bound holds against).

## Resource Estimate
{'manual': {'gpu_hours': '1,000-1,500 H100-equivalent', 'timeline': '14-18 weeks', 'estimated_gpu_cost': '$2,500-$3,750 at $2.50/hr H100 spot', 'gpu_breakdown': 'DeepSeek-V4-Flash: 2×H100 FP8 (~160GB VRAM); Qwen-3.5: 4×H100 INT4 (~200GB) or 8×H100 FP8 (~400GB); Llama-4-Maverick: 4×H100 INT4 (~200GB) or 8×H100 FP8 (~400GB). Running all 3 simultaneously: 10×H100 (INT4) to 18×H100 (FP8). Per-experiment: single-judge baselines across 15 attacks × 3 tasks × 3 models ≈ 450 H100-hrs; multi-judge protocol evaluation across 45 conditions on 10-GPU cluster ≈ 500 H100-hrs; signal independence measurement, copula fitting, and α estimation ≈ 100 H100-hrs; ablations (K=1,2,3,5,7 judges, homogeneous vs. heterogeneous) ≈ 200 H100-hrs; development/debugging ≈ 150 H100-hrs'}, 'human_in_loop': {'gpu_hours': '800-1,200 H100-equivalent', 'timeline': '10-14 weeks', 'claude_api_cost': '$400-$600 (Sonnet 4.6 for code generation, proof assistance, paper drafting; ~130-200M tokens)', 'estimated_gpu_cost': '$2,000-$3,000 at $2.50/hr H100 spot', 'gpu_breakdown': 'Same per-model requirements; efficiency gains from Claude-assisted theorem proving, experiment scheduling, and copula fitting, reducing wasted debugging runs by ~20%'}, 'auto_research': {'gpu_hours': '1,200-1,800 H100-equivalent', 'timeline': '6-9 weeks', 'claude_api_cost': '$1,200-$2,000 (Opus 4.7 for theorem proving, SDPI chain verification, experiment design; ~250-400M tokens)', 'estimated_gpu_cost': '$3,000-$4,500 at $2.50/hr H100 spot', 'speed_bottleneck': 'The three-pillar proof strategy (SDPI + Fano + copula) has well-defined mathematical components that autonomous systems can work on in parallel, but ensuring the chain composes correctly across the three pillars requires human mathematical judgment. The key risk is that the SDPI contraction yields a weaker-than-expected bound, requiring fallback to the √K variance-reduction argument.'}}

## Inspired By
The convergence of seven lines of work: (1) Robertson & Koyejo's bounded f-divergence theory for single-evaluator manipulation resistance; (2) The dual peer prediction results—Qiu et al.'s BNE and Chen et al.'s dominant-strategy PEG—providing complementary incentive-compatibility guarantees; (3) Yang et al.'s information-theoretic diversity-scaling framework establishing the task-performance scaling law via effective channel count K*—we provide the adversarial dual; (4) Turkmen et al.'s Gaussian-copula model with its error floor theorem and MI decomposition, which provides the mathematical foundation from which we derive our closed-form K_eff; (5) Kaneko & Baldwin's tight single-model information-theoretic attack cost bounds (N_min ≥ log₂(1/ε)/I_max), which we extend to multi-judge composition; (6) The SoK's empirical finding that 7-model committees reduce ASR to 10–19% without formal explanation; (7) The behavioral entanglement and correlated error literature (Chen et al. 2604.07650, Kim et al. ICML 2025) providing quantitative inter-judge independence measurements. We unify these into a certifiable manipulation-resistance framework where the certified bound is an explicit function of measurable signal correlation.

## Target Venues
- AAAI 2027 Main Technical Track (abstract: July 21, 2026; full paper: July 28, 2026; primary target—theory + experiments with certified robustness framing)
- USENIX Security 2027 Cycle 1 (abstract: August 18, 2026; full paper: August 25, 2026; security-focused version emphasizing certifiable robustness against realistic attacks)
- NeurIPS 2026 Workshops (contributed papers: ~August 29, 2026; workshop version connecting to the diversity-scaling and certified robustness communities)
- ICLR 2027 (estimated deadline: October 2026; polished archival version with extended theory, comprehensive experiments, and tightness analysis)

## Key References
- Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes (Robertson & Koyejo, arXiv 2508.05469, 2025) — foundational TVD-MI theory, Theorem 3.3 polynomial certification bounds, primary work we extend
- Identity-Link IRT for Label-Free LLM Evaluation: Preserving Additivity in TVD-MI Scores (Robertson, arXiv 2510.14966, 2025) — sparse TVD-MI evaluation, two-judge preliminary validation
- Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction (Qiu et al., ICLR 2026, 2601.20299) — BNE incentive-compatibility for LLM peer prediction, inverse scaling property
- Incentivizing Truthful Language Models via Peer Elicitation Games (Chen et al., NeurIPS 2025, 2505.13636) — DMI-based multi-agent peer elicitation with dominant strategy truthfulness (Lemma 1), sublinear O(√T) regret bound (Theorem 2), last-iterate convergence to Nash equilibrium (Theorem 3) via online mirror descent; experiments use 3 discriminators (n≥2 required by Lemma 1)
- Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity (Yang et al., ICLR 2026 Workshop AIMS, 2602.03794) — information-theoretic diversity-scaling framework: effective channel count K* = 2^{H(ρ)}, residual uncertainty (1-α_c)^{K*} geometric contraction (Theorem 4.3), heterogeneity advantage (Corollary 4.4); we provide the adversarial dual of their task-performance result
- Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection (Turkmen et al., arXiv 2602.08003, 2026) — Gaussian-copula correlated error model (Z_j = √ρ·U + √(1-ρ)·ξ_j), information-theoretic error floor Φ(Φ⁻¹(1-p)/√ρ) (Theorem 4.4), three-term MI decomposition into accuracy-redundancy-error correlation (Theorem 4.3); copula model provides the mathematical foundation from which we derive our K_eff formula
- Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs (Kaneko & Baldwin, NeurIPS 2025 spotlight, arXiv 2510.17000) — tight single-model attack cost bound N_min ≥ log₂(1/ε)/I_max via K-ary Fano inequality (Theorem 1), achieved by SPRT (Theorem 2); validated across 7 LLMs including Llama-4 and DeepSeek-R1; provides single-channel foundation that we extend to multi-judge composition
- Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation (Shen et al., arXiv 2604.03257, Google DeepMind/UCL, 2026) — constrained MLE fusing human labels, LLM-judge annotations, and domain constraints for certified performance estimation; addresses honest-judge noise, not adversarial manipulation; occupies adjacent 'certifiable evaluation' space
- Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges (Feng, Shen, Balashankar, Gerner-Beuerle & Rodrigues, ICLR 2026, arXiv 2601.20913) — statistical hypothesis testing framework for LLM evaluation certification with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty; variance-corrected thresholds using judge TPR/FPR estimation; assumes honest but fallible judges, not adversarial manipulation; complements Shen et al. in the 'certifiable evaluation' space
- Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation (Jung & Na, arXiv 2604.00477, 2026) — score-coverage dissociation: scoring reliability scales logarithmically, discovery follows power law N^0.69; informs our analysis of when certified bounds saturate vs. empirical gains
- Security in LLM-as-a-Judge: A Comprehensive SoK (arXiv 2603.29403, April 2026) — comprehensive vulnerability catalog, 50-68% ASR on open-source, 7-model committee reduces ASR to 10-19%; primary empirical evidence for diversity benefit without formal explanation
- LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge (arXiv 2506.09443, 2025) — RobustJudge benchmark, 15 attacks, 7 defenses, 12 models
- Correlated Errors in Large Language Models (Kim, Garg, Peng & Garg, ICML 2025, arXiv 2506.07962) — error correlation across 350+ LLMs: 60% agreement when both err (vs 33% baseline), same-company +0.066, same-architecture +0.076; KEY for α regime analysis
- How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement (Chen et al., arXiv 2604.07650, 2026) — BEI and CIG metrics across 18 LLMs from 6 families; cross-family entanglement 40-60% lower than intra-family
- Benchmark Illusion: Disagreement among LLMs and Its Scientific Consequences (arXiv 2602.11898, 2026) — 16-38% disagreement among top frontier models despite similar accuracy
- Strong Data-Processing Inequalities for Channels and Bayesian Networks (Polyanskiy & Wu, arXiv 1508.06025, 2017) — SDPI contraction coefficients compose multiplicatively; foundational for our Pillar 1 proof strategy
- Rethinking Fano's Inequality in Ensemble Learning (Morishita et al., ICML 2022, arXiv 2205.12683) — decomposes Fano bound for ensembles into relevance, redundancy, and combination loss; foundational for our Pillar 2 proof strategy
- On the Certified Robustness for Ensemble Models and Beyond (Chen et al., arXiv 2107.10873, 2021) — diversified gradient + large confidence margin jointly necessary and sufficient for certified ensemble robustness
- Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al., arXiv 2106.06946, 2021) — ensemble variance reduction yields √K-type certified radius improvement; precedent for polynomial scaling from diversity
- Information-Theoretically Optimal Adversarial Attacks (Yi et al., arXiv 2007.14042, 2020) — proves attack cost scales up with number of redundant signal copies; direct precedent for manipulation cost scaling with K
- On the Fragility of AI Agent Collusion (Keppo et al., arXiv 2603.20281, 2026) — increasing LLM count 2→5 breaks collusion (+22%→+3%); same-family size heterogeneity stabilizes via leader-follower; motivates cross-family diversity
- CollabEval: Multi-Agent Collaborative Evaluation (arXiv 2603.00993, March 2026) — three-phase multi-agent evaluation without formal adversarial guarantees
- An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring (Ebrahimi et al., IJCNLP-AACL 2025, arXiv 2505.24239) — credibility-based iterative aggregation; game-theoretic but not information-theoretic
- Certifying Joint Adversarial Robustness for Model Ensembles (Chiang et al., arXiv 2004.10250, 2020) — vulnerability space disjointness for ensemble certification
- Peer Prediction with More Signals than Reports (Frongillo et al., arXiv 2503.16280, 2025) — fine-grained signals destabilize uninformative equilibria
- Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)
- Improving Your Model Ranking on Chatbot Arena by Vote Rigging (ICML 2025)
- am-ELO: A Stable Framework for Arena-based LLM Evaluation (ICML 2025 Poster)
- CAP: Improving the Robustness of LLM-as-a-Judge Against Adversarial Score Manipulation via Comparative Augmented Prompting (OpenReview 2026)
- Aligned Textual Scoring Rules (Lu et al., arXiv 2507.06221, 2025)
- Can You Trick the Grader? Adversarial Persuasion of LLM Judges (EMNLP 2025 Findings)


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "c69b0757-b1d7-425c-94a1-3cc59a5a3069",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:43:55.364Z_

```json
{
  "parentUuid": "c69b0757-b1d7-425c-94a1-3cc59a5a3069",
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
  "uuid": "a7a25d71-546f-41a6-aabc-342796751ebd",
  "timestamp": "2026-05-20T04:43:55.364Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:43:55.364Z_

```json
{
  "parentUuid": "a7a25d71-546f-41a6-aabc-342796751ebd",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "8c186b61-c47e-4a04-9f3f-8d3b9dff87b5",
  "timestamp": "2026-05-20T04:43:55.364Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "8c186b61-c47e-4a04-9f3f-8d3b9dff87b5",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable manipulation resistance for multi-judge LLM evaluation",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:44:01.642Z_

<details><summary>Logged reasoning block</summary>

```text
This is a complex proposal that needs thorough evaluation. Let me first do the required web searches to understand the current landscape before making any assessments. I need to search for:

1. Recent work on LLM-as-judge adversarial robustness and certified defenses
2. Multi-judge evaluation protocols and their formal guarantees
3. The specific key papers cited in this proposal to verify they exist and are accurately described
4. Information-theoretic approaches to LLM evaluation security

Let me start by loading the WebSearch tool and conducting my research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c186b61-c47e-4a04-9f3f-8d3b9dff87b5",
  "isSidechain": false,
  "requestId": "req_011CbDD9BecThQCc2ezuDcoM",
  "type": "assistant",
  "uuid": "17f96217-6900-4bc3-941e-ee8f7f7792e7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xewwBsHMQLUMoqfqGi7wr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11953,
      "cache_read_input_tokens": 14333,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 211,
          "cache_read_input_tokens": 14333,
          "cache_creation_input_tokens": 11953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11953
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

_source line 9 · 2026-05-20T04:44:01.672Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_0172yCBVDTtoRNaE2UXUoB9E`</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": 1
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "17f96217-6900-4bc3-941e-ee8f7f7792e7",
  "isSidechain": false,
  "requestId": "req_011CbDD9BecThQCc2ezuDcoM",
  "type": "assistant",
  "uuid": "a715e376-4965-46ce-bc91-e853d72c18a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_018xewwBsHMQLUMoqfqGi7wr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11953,
      "cache_read_input_tokens": 14333,
      "output_tokens": 211,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11953,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 211,
          "cache_read_input_tokens": 14333,
          "cache_creation_input_tokens": 11953,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11953
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

_source line 10 · 2026-05-20T04:44:01.678Z_

<details><summary>↩ Tool result · `toolu_0172yCBVDTtoRNaE2UXUoB9E`</summary>

````text
```json
{
  "type": "tool_reference",
  "tool_name": "WebSearch"
}
```
````

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a715e376-4965-46ce-bc91-e853d72c18a5",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "3c82d317-bc85-446d-8fdd-f6b36d852632",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "a715e376-4965-46ce-bc91-e853d72c18a5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T04:44:05.051Z_

Now let me conduct the required research searches before evaluating this proposal. I'll run multiple searches in parallel to cover the key areas.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3c82d317-bc85-446d-8fdd-f6b36d852632",
  "isSidechain": false,
  "requestId": "req_011CbDD9f67aq9hp4X5rXQhi",
  "type": "assistant",
  "uuid": "bf45a6e0-ee0a-4f77-91c8-b2b56d854f27",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvCPnytLQ4fQnPFFc3aNHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 26286,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 739
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

_source line 12 · 2026-05-20T04:44:05.527Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HDNzBKda2gmmkmPWFQm93F`</summary>

```json
{
  "query": "certified adversarial robustness LLM-as-judge multi-judge evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bf45a6e0-ee0a-4f77-91c8-b2b56d854f27",
  "isSidechain": false,
  "requestId": "req_011CbDD9f67aq9hp4X5rXQhi",
  "type": "assistant",
  "uuid": "9f20b734-6670-4098-8b2b-21986e4335be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvCPnytLQ4fQnPFFc3aNHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 26286,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 739
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

_source line 13 · 2026-05-20T04:44:06.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uijz5AzaBSjZyfcWu1LCAM`</summary>

```json
{
  "query": "Kaneko Baldwin \"Bits Leaked per Query\" information-theoretic bounds adversarial attacks LLM NeurIPS 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f20b734-6670-4098-8b2b-21986e4335be",
  "isSidechain": false,
  "requestId": "req_011CbDD9f67aq9hp4X5rXQhi",
  "type": "assistant",
  "uuid": "bc78f81c-21dc-4054-8c4b-b5d2d1b25522",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvCPnytLQ4fQnPFFc3aNHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 26286,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 739
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

_source line 14 · 2026-05-20T04:44:06.880Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014byKxyL6LnGzqmETSiQr4X`</summary>

```json
{
  "query": "Robertson Koyejo \"Let's Measure Information Step-by-Step\" TVD-MI LLM evaluation 2508.05469"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc78f81c-21dc-4054-8c4b-b5d2d1b25522",
  "isSidechain": false,
  "requestId": "req_011CbDD9f67aq9hp4X5rXQhi",
  "type": "assistant",
  "uuid": "595e52ac-fd7a-42d3-afc4-fb5614e5c9d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvCPnytLQ4fQnPFFc3aNHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 26286,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 739
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

_source line 15 · 2026-05-20T04:44:07.882Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01F2mzyBzVadhrHrtbpvKCAH`</summary>

```json
{
  "query": "Yang et al \"Understanding Agent Scaling\" diversity multi-agent ICLR 2026 2602.03794"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "595e52ac-fd7a-42d3-afc4-fb5614e5c9d3",
  "isSidechain": false,
  "requestId": "req_011CbDD9f67aq9hp4X5rXQhi",
  "type": "assistant",
  "uuid": "9fb8a27a-b780-4bd9-94ed-6f66c791524d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvCPnytLQ4fQnPFFc3aNHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 26286,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 739
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

_source line 16 · 2026-05-20T04:44:08.234Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Uwd4Bn7xrvSoxyviMb9Ytb`</summary>

```json
{
  "query": "Turkmen et al \"Don't Always Pick Highest-Performing Model\" Gaussian copula ensemble 2602.08003"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9fb8a27a-b780-4bd9-94ed-6f66c791524d",
  "isSidechain": false,
  "requestId": "req_011CbDD9f67aq9hp4X5rXQhi",
  "type": "assistant",
  "uuid": "838dec6c-94c8-421b-9a1d-9f73f861cf1e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EvCPnytLQ4fQnPFFc3aNHe",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 739,
      "cache_read_input_tokens": 26286,
      "output_tokens": 356,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 739,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 356,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 739,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 739
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

_source line 17 · 2026-05-20T04:44:13.431Z_

<details><summary>↩ Tool result · `toolu_01HDNzBKda2gmmkmPWFQm93F`</summary>

```text
Web search results for query: "certified adversarial robustness LLM-as-judge multi-judge evaluation 2025 2026"

Links: [{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/html/2506.09443v1"},{"title":"LLM-as-a-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"},{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"LLM-as-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluation"},{"title":"When AIs Judge AIs: The Rise of Agent-as-a-Judge Evaluation for LLMs","url":"https://arxiv.org/html/2508.02994v1"},{"title":"A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness","url":"https://arxiv.org/pdf/2603.06594"}]

Based on the search results, here's what I found about certified adversarial robustness, LLM-as-judge, and multi-judge evaluation:

## Recent Research (2025-2026)

RobustJudge is a framework that investigates the impact of attack methods and defense strategies, and has found that LLM-as-a-Judge systems remain vulnerable to adversarial attacks including Combined Attack and PAIR, while defense mechanisms like Re-tokenization and LLM-based Detectors offer improved protection.

Robustness is highly sensitive to the choice of prompt template and judge models, and a proposed prompt template optimization method can improve robustness, with JudgeLM-13B demonstrating strong performance as a robust open-source judge.

## Multi-Judge Evaluation

Multi-agent judge frameworks employ multiple LLMs acting in concert to evaluate, with different mechanisms including explicit debates and rebuttals, or parallel assessments and aggregation, all yielding ensemble judgments that benefit from model diversity.

While multi-agent setups could be more robust since a deceptive output would need to fool multiple agents, they could have their own failure modes if all agents are from the same model family, as an exploit that confuses that model could trick all of them.

## Key Vulnerabilities

LLM-based judges can be easily manipulated by adversarial prompt modifications such as Combined Attack or optimization-based attacks like PAIR, achieving high attack success rates and large deviations from correct scores.

Optimization-based attacks could cause judges to misclassify 100% of harmful outputs as safe in some cases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9f20b734-6670-4098-8b2b-21986e4335be",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "8d42a1af-ca00-44db-9c90-1589d694f453",
  "toolUseResult": {
    "query": "certified adversarial robustness LLM-as-judge multi-judge evaluation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_015ENfLtxA778K4LnEUdcfTP",
        "content": [
          {
            "title": "SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK",
            "url": "https://arxiv.org/pdf/2603.29403"
          },
          {
            "title": "LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2506.09443v1"
          },
          {
            "title": "LLM-as-a-Judge Evaluation",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"
          },
          {
            "title": "Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment",
            "url": "https://arxiv.org/pdf/2402.14016"
          },
          {
            "title": "LLM-as-Judge Evaluation",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-evaluation"
          },
          {
            "title": "When AIs Judge AIs: The Rise of Agent-as-a-Judge Evaluation for LLMs",
            "url": "https://arxiv.org/html/2508.02994v1"
          },
          {
            "title": "A Coin Flip for Safety: LLM Judges Fail to Reliably Measure Adversarial Robustness",
            "url": "https://arxiv.org/pdf/2603.06594"
          }
        ]
      },
      "Based on the search results, here's what I found about certified adversarial robustness, LLM-as-judge, and multi-judge evaluation:\n\n## Recent Research (2025-2026)\n\nRobustJudge is a framework that investigates the impact of attack methods and defense strategies, and has found that LLM-as-a-Judge systems remain vulnerable to adversarial attacks including Combined Attack and PAIR, while defense mechanisms like Re-tokenization and LLM-based Detectors offer improved protection.\n\nRobustness is highly sensitive to the choice of prompt template and judge models, and a proposed prompt template optimization method can improve robustness, with JudgeLM-13B demonstrating strong performance as a robust open-source judge.\n\n## Multi-Judge Evaluation\n\nMulti-agent judge frameworks employ multiple LLMs acting in concert to evaluate, with different mechanisms including explicit debates and rebuttals, or parallel assessments and aggregation, all yielding ensemble judgments that benefit from model diversity.\n\nWhile multi-agent setups could be more robust since a deceptive output would need to fool multiple agents, they could have their own failure modes if all agents are from the same model family, as an exploit that confuses that model could trick all of them.\n\n## Key Vulnerabilities\n\nLLM-based judges can be easily manipulated by adversarial prompt modifications such as Combined Attack or optimization-based attacks like PAIR, achieving high attack success rates and large deviations from correct scores.\n\nOptimization-based attacks could cause judges to misclassify 100% of harmful outputs as safe in some cases."
    ],
    "durationSeconds": 7.899360263,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9f20b734-6670-4098-8b2b-21986e4335be",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 18 · 2026-05-20T04:44:13.751Z_

<details><summary>↩ Tool result · `toolu_01Uijz5AzaBSjZyfcWu1LCAM`</summary>

```text
Web search results for query: "Kaneko Baldwin "Bits Leaked per Query" information-theoretic bounds adversarial attacks LLM NeurIPS 2025"

Links: [{"title":"[2510.17000] Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/abs/2510.17000"},{"title":"How many queries does it take to break an AI? We put a number on it. - MBZUAI","url":"https://mbzuai.ac.ae/news/how-many-queries-does-it-take-to-break-an-ai-we-put-a-number-on-it/"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/pdf/2510.17000"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds for Adversarial Attacks on LLMs | OpenReview","url":"https://openreview.net/forum?id=DwXX8c7xst"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/html/2510.17000v1"},{"title":"Rectifying Belief Space via Unlearning to Harness LLMs’ Reasoning","url":"https://www.researchgate.net/publication/394299325_Rectifying_Belief_Space_via_Unlearning_to_Harness_LLMs'_Reasoning"}]

I found comprehensive information about this research. Here's what I discovered:

## Overview

This is a NeurIPS 2025 Spotlight paper from MBZUAI postdoc researcher Masahiro Kaneko and Tim Baldwin that proposes measuring the bits leaked per query to predict the minimum number of queries an adversary needs.

## Key Framework

The research treats mutual information between an observation and target property as leaked bits per query, showing that achieving error ε requires at least log(1/ε)/I(Z;T) queries, scaling linearly with the inverse leak rate and only logarithmically with desired accuracy.

## Main Findings

Experiments on seven LLMs across system-prompt leakage, jailbreak, and relearning attacks show that exposing answer tokens alone requires about a thousand queries; adding logits cuts this to about a hundred; and revealing the full thinking process trims it to a few dozen.

## Application

The results provide the first principled yardstick for balancing transparency and security when deploying LLMs. Adversarial attacks can be viewed as attempts to infer a target property that is unknown when an instruction is issued, becomes knowable only after observing the model's reply, and includes examples like binary flags that trigger harmful responses and the degree to which unlearned information can be restored.

The paper addresses the gap in understanding how much information can be safely disclosed without enabling attackers to compromise LLM safety with fewer queries.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bc78f81c-21dc-4054-8c4b-b5d2d1b25522",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "6757ce04-8ece-473f-9c37-f0bbe87c14d2",
  "toolUseResult": {
    "query": "Kaneko Baldwin \"Bits Leaked per Query\" information-theoretic bounds adversarial attacks LLM NeurIPS 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DUZ8sPgaBfyjSnywdWijp8",
        "content": [
          {
            "title": "[2510.17000] Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/abs/2510.17000"
          },
          {
            "title": "How many queries does it take to break an AI? We put a number on it. - MBZUAI",
            "url": "https://mbzuai.ac.ae/news/how-many-queries-does-it-take-to-break-an-ai-we-put-a-number-on-it/"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/pdf/2510.17000"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds for Adversarial Attacks on LLMs | OpenReview",
            "url": "https://openreview.net/forum?id=DwXX8c7xst"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/html/2510.17000v1"
          },
          {
            "title": "Rectifying Belief Space via Unlearning to Harness LLMs’ Reasoning",
            "url": "https://www.researchgate.net/publication/394299325_Rectifying_Belief_Space_via_Unlearning_to_Harness_LLMs'_Reasoning"
          }
        ]
      },
      "I found comprehensive information about this research. Here's what I discovered:\n\n## Overview\n\nThis is a NeurIPS 2025 Spotlight paper from MBZUAI postdoc researcher Masahiro Kaneko and Tim Baldwin that proposes measuring the bits leaked per query to predict the minimum number of queries an adversary needs.\n\n## Key Framework\n\nThe research treats mutual information between an observation and target property as leaked bits per query, showing that achieving error ε requires at least log(1/ε)/I(Z;T) queries, scaling linearly with the inverse leak rate and only logarithmically with desired accuracy.\n\n## Main Findings\n\nExperiments on seven LLMs across system-prompt leakage, jailbreak, and relearning attacks show that exposing answer tokens alone requires about a thousand queries; adding logits cuts this to about a hundred; and revealing the full thinking process trims it to a few dozen.\n\n## Application\n\nThe results provide the first principled yardstick for balancing transparency and security when deploying LLMs. Adversarial attacks can be viewed as attempts to infer a target property that is unknown when an instruction is issued, becomes knowable only after observing the model's reply, and includes examples like binary flags that trigger harmful responses and the degree to which unlearned information can be restored.\n\nThe paper addresses the gap in understanding how much information can be safely disclosed without enabling attackers to compromise LLM safety with fewer queries."
    ],
    "durationSeconds": 7.278960438000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bc78f81c-21dc-4054-8c4b-b5d2d1b25522",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T04:44:14.218Z_

<details><summary>↩ Tool result · `toolu_01F2mzyBzVadhrHrtbpvKCAH`</summary>

```text
Web search results for query: "Yang et al "Understanding Agent Scaling" diversity multi-agent ICLR 2026 2602.03794"

Links: [{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/pdf/2602.03794"},{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/html/2602.03794"},{"title":"Towards a Science of Scaling Agent Systems","url":"https://arxiv.org/html/2512.08296v1"},{"title":"Published as a conference paper at ICLR 2026 Workshop on MALGAI","url":"https://openreview.net/pdf?id=RLHUTcvsA9"},{"title":"Beyond Quantity: Trajectory Diversity Scaling for Code Agents","url":"https://arxiv.org/pdf/2602.03219"}]

I found the paper you're looking for! Here are the details:

**Title:** Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity

**Authors:** Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, and Shangding Gu

**ArXiv ID:** 2602.03794

**Key Findings:**

Scaling by increasing the number of agents exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (different models, prompts, or tools) yields substantial gains.

The paper presents an information-theoretic framework showing that multi-agent system performance is bounded by intrinsic task uncertainty, with improvements depending on how many effective channels the system accesses.

Homogeneous agents saturate early because their outputs are strongly correlated, whereas heterogeneous agents contribute complementary evidence.

The research demonstrates that 2 diverse agents can match or exceed the performance of 16 homogeneous agents.

The paper is available on arXiv at https://arxiv.org/pdf/2602.03794


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9fb8a27a-b780-4bd9-94ed-6f66c791524d",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "f69f1a77-dc29-4a6d-8d3b-7348281b1986",
  "toolUseResult": {
    "query": "Yang et al \"Understanding Agent Scaling\" diversity multi-agent ICLR 2026 2602.03794",
    "results": [
      {
        "tool_use_id": "srvtoolu_019amrzRfBHjYwXNPjgfSka1",
        "content": [
          {
            "title": "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity",
            "url": "https://arxiv.org/pdf/2602.03794"
          },
          {
            "title": "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity",
            "url": "https://arxiv.org/html/2602.03794"
          },
          {
            "title": "Towards a Science of Scaling Agent Systems",
            "url": "https://arxiv.org/html/2512.08296v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 Workshop on MALGAI",
            "url": "https://openreview.net/pdf?id=RLHUTcvsA9"
          },
          {
            "title": "Beyond Quantity: Trajectory Diversity Scaling for Code Agents",
            "url": "https://arxiv.org/pdf/2602.03219"
          }
        ]
      },
      "I found the paper you're looking for! Here are the details:\n\n**Title:** Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity\n\n**Authors:** Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, and Shangding Gu\n\n**ArXiv ID:** 2602.03794\n\n**Key Findings:**\n\nScaling by increasing the number of agents exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (different models, prompts, or tools) yields substantial gains.\n\nThe paper presents an information-theoretic framework showing that multi-agent system performance is bounded by intrinsic task uncertainty, with improvements depending on how many effective channels the system accesses.\n\nHomogeneous agents saturate early because their outputs are strongly correlated, whereas heterogeneous agents contribute complementary evidence.\n\nThe research demonstrates that 2 diverse agents can match or exceed the performance of 16 homogeneous agents.\n\nThe paper is available on arXiv at https://arxiv.org/pdf/2602.03794"
    ],
    "durationSeconds": 6.333275904,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9fb8a27a-b780-4bd9-94ed-6f66c791524d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T04:44:14.443Z_

<details><summary>↩ Tool result · `toolu_01Uwd4Bn7xrvSoxyviMb9Ytb`</summary>

```text
Web search results for query: "Turkmen et al "Don't Always Pick Highest-Performing Model" Gaussian copula ensemble 2602.08003"

Links: [{"title":"[2602.08003] Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/abs/2602.08003"},{"title":"Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/html/2602.08003"},{"title":"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/pdf/2602.08003"},{"title":"gaussian copula model: Topics by Science.gov","url":"https://www.science.gov/topicpages/g/gaussian+copula+model"},{"title":"The Gaussian Copula in Credit Risk Modelling","url":"https://www.linkedin.com/pulse/gaussian-copula-credit-risk-modelling-correlated-ravichandran-pmivc"}]

I found the paper you're looking for. The paper "Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection" by Yigit Turkmen, Baturalp Buyukates, and Melih Bastopcu addresses the question of which models should be selected when forming an LLM ensemble.

The authors formulate budgeted ensemble selection as maximizing the mutual information between the true label and predictions of the selected models. To explain why performance can saturate even with many models, they model the correlated errors of the models using Gaussian-copula and show an information-theoretic error floor for the performance of the ensemble.

They propose a simple greedy mutual-information selection algorithm that estimates the required information terms directly from data and iteratively builds an ensemble under a query budget. The approach is tested on MEDMCQA, MMLU, and IMDB movie reviews datasets, and consistently outperforms strong baselines under the same query budget.

The paper was published on February 10, 2026 and is available at arXiv:2602.08003.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "838dec6c-94c8-421b-9a1d-9f73f861cf1e",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "5f4ef775-6f66-474b-bbb5-4842bef1c67e",
  "toolUseResult": {
    "query": "Turkmen et al \"Don't Always Pick Highest-Performing Model\" Gaussian copula ensemble 2602.08003",
    "results": [
      {
        "tool_use_id": "srvtoolu_01NxxiJnLLYifhxBnkCAuPzs",
        "content": [
          {
            "title": "[2602.08003] Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/abs/2602.08003"
          },
          {
            "title": "Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/html/2602.08003"
          },
          {
            "title": "Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/pdf/2602.08003"
          },
          {
            "title": "gaussian copula model: Topics by Science.gov",
            "url": "https://www.science.gov/topicpages/g/gaussian+copula+model"
          },
          {
            "title": "The Gaussian Copula in Credit Risk Modelling",
            "url": "https://www.linkedin.com/pulse/gaussian-copula-credit-risk-modelling-correlated-ravichandran-pmivc"
          }
        ]
      },
      "I found the paper you're looking for. The paper \"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection\" by Yigit Turkmen, Baturalp Buyukates, and Melih Bastopcu addresses the question of which models should be selected when forming an LLM ensemble.\n\nThe authors formulate budgeted ensemble selection as maximizing the mutual information between the true label and predictions of the selected models. To explain why performance can saturate even with many models, they model the correlated errors of the models using Gaussian-copula and show an information-theoretic error floor for the performance of the ensemble.\n\nThey propose a simple greedy mutual-information selection algorithm that estimates the required information terms directly from data and iteratively builds an ensemble under a query budget. The approach is tested on MEDMCQA, MMLU, and IMDB movie reviews datasets, and consistently outperforms strong baselines under the same query budget.\n\nThe paper was published on February 10, 2026 and is available at arXiv:2602.08003."
    ],
    "durationSeconds": 6.206691396000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "838dec6c-94c8-421b-9a1d-9f73f861cf1e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 21_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "5f4ef775-6f66-474b-bbb5-4842bef1c67e",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable manipulation resistance for multi-judge LLM evaluation",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---

### Tool result

_source line 23 · 2026-05-20T04:44:19.486Z_

<details><summary>↩ Tool result · `toolu_014byKxyL6LnGzqmETSiQr4X`</summary>

```text
Web search results for query: "Robertson Koyejo "Let's Measure Information Step-by-Step" TVD-MI LLM evaluation 2508.05469"

Links: [{"title":"Identity-Link IRT for Label-Free LLM Evaluation:","url":"https://arxiv.org/pdf/2510.14966"},{"title":"About","url":"https://zrobertson466920.github.io/about/"},{"title":"[PDF] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Measure-Information-Step-by-Step:-LLM-Based-Robertson-Koyejo/824098ede34f59514ebc25a69c69c68d1e89b664"},{"title":"Let’s Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/html/2508.05469v1"},{"title":"(PDF) Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://www.researchgate.net/publication/394397315_Let's_Measure_Information_Step-by-Step_LLM-Based_Evaluation_Beyond_Vibes"},{"title":"[2508.05469] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/abs/2508.05469"}]

Based on the web search results, here's what I found:

Zachary Robertson and Sanmi Koyejo published "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes" (arXiv:2508.05469, 2025).

## Key Research Overview

The paper studies evaluation of AI systems without ground truth by exploiting a link between strategic gaming and information loss. It analyzes which information-theoretic mechanisms resist adversarial manipulation, extending finite-sample bounds to show that bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially.

## TVD-MI Method

The TVD-MI (Total Variation Distance MI) implementation uses an LLM critic (GPT-4o-mini) to estimate bounded mutual information, evaluating whether two responses show evidence of addressing the same source material and outputting categorical judgments.

## Results

Bounded measures like TVD-MI achieve the largest effect sizes (mean d = 5.2) while demonstrating 10-100× better resistance to adversarial manipulation than LLM judges. Under attacks that cause judges to fail catastrophically (-2157% discrimination), TVD-MI degrades by only 31% while maintaining positive discrimination.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "595e52ac-fd7a-42d3-afc4-fb5614e5c9d3",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "6af7b6ba-255c-43e1-86e3-481161181b72",
  "toolUseResult": {
    "query": "Robertson Koyejo \"Let's Measure Information Step-by-Step\" TVD-MI LLM evaluation 2508.05469",
    "results": [
      {
        "tool_use_id": "srvtoolu_01TAjFJG1juuPc62f6kijxZM",
        "content": [
          {
            "title": "Identity-Link IRT for Label-Free LLM Evaluation:",
            "url": "https://arxiv.org/pdf/2510.14966"
          },
          {
            "title": "About",
            "url": "https://zrobertson466920.github.io/about/"
          },
          {
            "title": "[PDF] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Let's-Measure-Information-Step-by-Step:-LLM-Based-Robertson-Koyejo/824098ede34f59514ebc25a69c69c68d1e89b664"
          },
          {
            "title": "Let’s Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/html/2508.05469v1"
          },
          {
            "title": "(PDF) Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://www.researchgate.net/publication/394397315_Let's_Measure_Information_Step-by-Step_LLM-Based_Evaluation_Beyond_Vibes"
          },
          {
            "title": "[2508.05469] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/abs/2508.05469"
          }
        ]
      },
      "Based on the web search results, here's what I found:\n\nZachary Robertson and Sanmi Koyejo published \"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes\" (arXiv:2508.05469, 2025).\n\n## Key Research Overview\n\nThe paper studies evaluation of AI systems without ground truth by exploiting a link between strategic gaming and information loss. It analyzes which information-theoretic mechanisms resist adversarial manipulation, extending finite-sample bounds to show that bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially.\n\n## TVD-MI Method\n\nThe TVD-MI (Total Variation Distance MI) implementation uses an LLM critic (GPT-4o-mini) to estimate bounded mutual information, evaluating whether two responses show evidence of addressing the same source material and outputting categorical judgments.\n\n## Results\n\nBounded measures like TVD-MI achieve the largest effect sizes (mean d = 5.2) while demonstrating 10-100× better resistance to adversarial manipulation than LLM judges. Under attacks that cause judges to fail catastrophically (-2157% discrimination), TVD-MI degrades by only 31% while maintaining positive discrimination."
    ],
    "durationSeconds": 12.602826517,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "595e52ac-fd7a-42d3-afc4-fb5614e5c9d3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 24 · 2026-05-20T04:44:22.989Z_

Good, the key papers are verified. Let me now search for more specific competing work and recent developments.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6af7b6ba-255c-43e1-86e3-481161181b72",
  "isSidechain": false,
  "requestId": "req_011CbDDAxiJEHGxEqx1KSQEj",
  "type": "assistant",
  "uuid": "57d4fc39-9c86-44f4-8e6f-3ce7dec1c7e6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4SZVSrveHksLLVY4Dc3oQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1119,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 27025,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1119,
          "output_tokens": 225,
          "cache_read_input_tokens": 27025,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2604
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

_source line 25 · 2026-05-20T04:44:23.931Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014UhdU7uLZtqGESVVCE2xie`</summary>

```json
{
  "query": "Chen et al \"Incentivizing Truthful Language Models\" peer elicitation games DMI NeurIPS 2025 2505.13636"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "57d4fc39-9c86-44f4-8e6f-3ce7dec1c7e6",
  "isSidechain": false,
  "requestId": "req_011CbDDAxiJEHGxEqx1KSQEj",
  "type": "assistant",
  "uuid": "1deec72f-6f5b-49fe-b26a-8594a609a8c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4SZVSrveHksLLVY4Dc3oQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1119,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 27025,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1119,
          "output_tokens": 225,
          "cache_read_input_tokens": 27025,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2604
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

_source line 26 · 2026-05-20T04:44:25.344Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01JKU9cW5QigtyPweTSj1RgT`</summary>

```json
{
  "query": "Qiu et al \"Truthfulness Despite Weak Supervision\" peer prediction LLM ICLR 2026 2601.20299"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1deec72f-6f5b-49fe-b26a-8594a609a8c6",
  "isSidechain": false,
  "requestId": "req_011CbDDAxiJEHGxEqx1KSQEj",
  "type": "assistant",
  "uuid": "582f8cfb-d6d1-4dfe-9971-fd665291657e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4SZVSrveHksLLVY4Dc3oQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1119,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 27025,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1119,
          "output_tokens": 225,
          "cache_read_input_tokens": 27025,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2604
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

_source line 27 · 2026-05-20T04:44:25.804Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PSG258SgQoeKvvCoNTzq6P`</summary>

```json
{
  "query": "multi-judge LLM evaluation manipulation cost scaling information theory formal bounds 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "582f8cfb-d6d1-4dfe-9971-fd665291657e",
  "isSidechain": false,
  "requestId": "req_011CbDDAxiJEHGxEqx1KSQEj",
  "type": "assistant",
  "uuid": "08bfff39-fc55-4f4e-87fb-0dc2cf19e37f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01X4SZVSrveHksLLVY4Dc3oQ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1119,
      "cache_creation_input_tokens": 2604,
      "cache_read_input_tokens": 27025,
      "output_tokens": 225,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 2604,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1119,
          "output_tokens": 225,
          "cache_read_input_tokens": 27025,
          "cache_creation_input_tokens": 2604,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 2604
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

_source line 28 · 2026-05-20T04:44:30.425Z_

<details><summary>↩ Tool result · `toolu_014UhdU7uLZtqGESVVCE2xie`</summary>

```text
Web search results for query: "Chen et al "Incentivizing Truthful Language Models" peer elicitation games DMI NeurIPS 2025 2505.13636"

Links: [{"title":"GitHub - toz015/neurips2025-repo: Code and experiments for a NeurIPS 2025 submission · GitHub","url":"https://github.com/toz015/neurips2025-repo"},{"title":"Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/pdf/2505.13636"},{"title":"NeurIPS Poster Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://neurips.cc/virtual/2025/poster/119902"},{"title":"Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/html/2505.13636v1"},{"title":"Artificial Intelligence May 2025","url":"https://arxiv.org/list/cs.AI/2025-05?skip=2600&show=250"},{"title":"[2505.13636] Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/abs/2505.13636"},{"title":"Computer Science and Game Theory May 2025","url":"https://www.arxiv.org/list/cs.GT/2025-05?skip=100&show=2000"}]

I found the paper! Here are the details about the Chen et al. paper:

**Title:** "Incentivizing Truthful Language Models via Peer Elicitation Games"

**Authors:** Baiting Chen, Tong Zhu, Jiale Han, Lexin Li, Gang Li, and Xiaowu Dai

**ArXiv ID:** 2505.13636

**Venue:** NeurIPS 2025 Oral

**Summary:**
The paper introduces Peer Elicitation Games (PEG), a training-free, game-theoretic framework for aligning LLMs through a peer elicitation mechanism involving a generator and multiple discriminators instantiated from distinct base models. Discriminators interact in a peer evaluation setting, where utilities are computed using a determinant-based mutual information score that provably incentivizes truthful reporting without requiring ground-truth labels.

**Key Theoretical Results:**
- The authors establish theoretical guarantees showing that each agent, via online learning, achieves sublinear regret in the sense their cumulative performance approaches that of the best fixed truthful strategy in hindsight.
- The paper proves last-iterate convergence to a truthful Nash equilibrium, ensuring that the actual policies used by agents converge to stable and truthful behavior over time.

The official repository with code is available on GitHub at the source listed in the search results.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1deec72f-6f5b-49fe-b26a-8594a609a8c6",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "9d0d78c0-9ecf-4785-9992-1dc4354b0eb5",
  "toolUseResult": {
    "query": "Chen et al \"Incentivizing Truthful Language Models\" peer elicitation games DMI NeurIPS 2025 2505.13636",
    "results": [
      {
        "tool_use_id": "srvtoolu_0111q3ZiLXFE9i3LniHia6oH",
        "content": [
          {
            "title": "GitHub - toz015/neurips2025-repo: Code and experiments for a NeurIPS 2025 submission · GitHub",
            "url": "https://github.com/toz015/neurips2025-repo"
          },
          {
            "title": "Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://arxiv.org/pdf/2505.13636"
          },
          {
            "title": "NeurIPS Poster Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://neurips.cc/virtual/2025/poster/119902"
          },
          {
            "title": "Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://arxiv.org/html/2505.13636v1"
          },
          {
            "title": "Artificial Intelligence May 2025",
            "url": "https://arxiv.org/list/cs.AI/2025-05?skip=2600&show=250"
          },
          {
            "title": "[2505.13636] Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://arxiv.org/abs/2505.13636"
          },
          {
            "title": "Computer Science and Game Theory May 2025",
            "url": "https://www.arxiv.org/list/cs.GT/2025-05?skip=100&show=2000"
          }
        ]
      },
      "I found the paper! Here are the details about the Chen et al. paper:\n\n**Title:** \"Incentivizing Truthful Language Models via Peer Elicitation Games\"\n\n**Authors:** Baiting Chen, Tong Zhu, Jiale Han, Lexin Li, Gang Li, and Xiaowu Dai\n\n**ArXiv ID:** 2505.13636\n\n**Venue:** NeurIPS 2025 Oral\n\n**Summary:**\nThe paper introduces Peer Elicitation Games (PEG), a training-free, game-theoretic framework for aligning LLMs through a peer elicitation mechanism involving a generator and multiple discriminators instantiated from distinct base models. Discriminators interact in a peer evaluation setting, where utilities are computed using a determinant-based mutual information score that provably incentivizes truthful reporting without requiring ground-truth labels.\n\n**Key Theoretical Results:**\n- The authors establish theoretical guarantees showing that each agent, via online learning, achieves sublinear regret in the sense their cumulative performance approaches that of the best fixed truthful strategy in hindsight.\n- The paper proves last-iterate convergence to a truthful Nash equilibrium, ensuring that the actual policies used by agents converge to stable and truthful behavior over time.\n\nThe official repository with code is available on GitHub at the source listed in the search results."
    ],
    "durationSeconds": 6.489429776999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1deec72f-6f5b-49fe-b26a-8594a609a8c6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 29 · 2026-05-20T04:44:32.132Z_

<details><summary>↩ Tool result · `toolu_01JKU9cW5QigtyPweTSj1RgT`</summary>

```text
Web search results for query: "Qiu et al "Truthfulness Despite Weak Supervision" peer prediction LLM ICLR 2026 2601.20299"

Links: [{"title":"[2601.20299] Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction","url":"https://arxiv.org/abs/2601.20299"},{"title":"Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction","url":"https://arxiv.org/html/2601.20299v1"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/58f19dcd2f739eb3573b20a0bf8a70f7a08c30b8.pdf"},{"title":"Evaluating and Training LLMs Using Peer Prediction","url":"https://arxiv.org/pdf/2601.20299"},{"title":"Weakly supervised veracity classification with LLM-predicted credibility signals | EPJ Data Science | Full Text","url":"https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-025-00534-0"},{"title":"Published as a conference paper at ICLR 2026 WHEN WEAK LLMS SPEAK","url":"https://openreview.net/pdf?id=ROioaZ45Yz"},{"title":"Published as a conference paper at ICLR 2026 PREDICTING LLM OUTPUT LENGTH VIA","url":"https://arxiv.org/pdf/2602.11812"}]

I found the paper you're looking for! Here's the information about it:

**Title:** Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction

**Authors:** Tianyi Alex Qiu, Micah Carroll, Cameron Allen from the Center for Human-Compatible Artificial Intelligence at UC Berkeley

**ArXiv ID:** 2601.20299

**Conference:** Published as a conference paper at ICLR 2026

**Key Contribution:** The paper introduces the peer prediction method for model evaluation and post-training, which rewards honest and informative answers over deceptive and uninformative ones, using a metric based on mutual predictability and without requiring ground truth labels.

**Main Results:** Training an 8B model with peer prediction-based reward recovers most of the drop in truthfulness due to prior malicious finetuning, even when the reward is produced by a 0.135B language model with no finetuning. Additionally, the paper discovers an inverse scaling property in peer prediction, where resistance to deception is strengthened as the capability gap between the experts and participants widens, enabling reliable evaluation of strong models with weak supervision.

The paper is available on arXiv at https://arxiv.org/abs/2601.20299 and also appears to be published on OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "582f8cfb-d6d1-4dfe-9971-fd665291657e",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "11e673e0-3d51-447e-bdff-508951280d14",
  "toolUseResult": {
    "query": "Qiu et al \"Truthfulness Despite Weak Supervision\" peer prediction LLM ICLR 2026 2601.20299",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JbnEMDTb43PnqLZHBV3Lk8",
        "content": [
          {
            "title": "[2601.20299] Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction",
            "url": "https://arxiv.org/abs/2601.20299"
          },
          {
            "title": "Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction",
            "url": "https://arxiv.org/html/2601.20299v1"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://openreview.net/pdf/58f19dcd2f739eb3573b20a0bf8a70f7a08c30b8.pdf"
          },
          {
            "title": "Evaluating and Training LLMs Using Peer Prediction",
            "url": "https://arxiv.org/pdf/2601.20299"
          },
          {
            "title": "Weakly supervised veracity classification with LLM-predicted credibility signals | EPJ Data Science | Full Text",
            "url": "https://epjdatascience.springeropen.com/articles/10.1140/epjds/s13688-025-00534-0"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 WHEN WEAK LLMS SPEAK",
            "url": "https://openreview.net/pdf?id=ROioaZ45Yz"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 PREDICTING LLM OUTPUT LENGTH VIA",
            "url": "https://arxiv.org/pdf/2602.11812"
          }
        ]
      },
      "I found the paper you're looking for! Here's the information about it:\n\n**Title:** Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction\n\n**Authors:** Tianyi Alex Qiu, Micah Carroll, Cameron Allen from the Center for Human-Compatible Artificial Intelligence at UC Berkeley\n\n**ArXiv ID:** 2601.20299\n\n**Conference:** Published as a conference paper at ICLR 2026\n\n**Key Contribution:** The paper introduces the peer prediction method for model evaluation and post-training, which rewards honest and informative answers over deceptive and uninformative ones, using a metric based on mutual predictability and without requiring ground truth labels.\n\n**Main Results:** Training an 8B model with peer prediction-based reward recovers most of the drop in truthfulness due to prior malicious finetuning, even when the reward is produced by a 0.135B language model with no finetuning. Additionally, the paper discovers an inverse scaling property in peer prediction, where resistance to deception is strengthened as the capability gap between the experts and participants widens, enabling reliable evaluation of strong models with weak supervision.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2601.20299 and also appears to be published on OpenReview."
    ],
    "durationSeconds": 6.784821048000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "582f8cfb-d6d1-4dfe-9971-fd665291657e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 30 · 2026-05-20T04:44:33.166Z_

<details><summary>↩ Tool result · `toolu_01PSG258SgQoeKvvCoNTzq6P`</summary>

```text
Web search results for query: "multi-judge LLM evaluation manipulation cost scaling information theory formal bounds 2026"

Links: [{"title":"LLM-as-Judge Best Practices in 2026: Calibration, Bias, and Cost","url":"https://futureagi.com/blog/llm-as-judge-best-practices-2026"},{"title":"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/pdf/2508.05469"},{"title":"Limits to scalable evaluation at the frontier: LLM as Judge ...","url":"https://arxiv.org/pdf/2410.13341"},{"title":"LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data","url":"https://labelyourdata.com/articles/llm-as-a-judge"},{"title":"Tuning LLM Judge Design Decisions for 1/1000 of the Cost","url":"https://arxiv.org/pdf/2501.17178"},{"title":"Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation","url":"https://arxiv.org/pdf/2601.14691"},{"title":"Debate, Deliberate, Decide (D3): A Cost-Aware Adversarial Framework for Reliable and Interpretable LLM Evaluation","url":"https://arxiv.org/pdf/2410.04663"}]

I found relevant research on this topic. Here are the key results:

## Multi-Judge LLM Evaluation & Manipulation

Research has identified manipulation strategies in LLM judge evaluation, ranging from style-based approaches that alter presentation to content-based approaches that fabricate signals of progress. Prompting-based techniques and scaling judge-time compute reduce but do not fully eliminate susceptibility to manipulation.

## Information-Theoretic Formal Bounds

A key theoretical result (Theorem 3.3) provides finite-sample robustness bounds for information-theoretic mechanisms under mode-collapse attacks, showing that bounded measures like total variation distance (TVD) retain polynomial guarantees whereas unbounded measures like KL divergence can degrade exponentially. This research reveals that detecting strategic manipulation in AI systems reduces to a well-defined information-theoretic problem.

## Cost & Scaling

Research systematically analyzes and tunes hyperparameters of LLM judges, including the model used, prompt, inference parameters, and parsing mechanisms, analyzing the impact of scaling the judge model and number of instructions on performance. Multi-judge approaches like debate frameworks achieve state-of-the-art agreement with human judgments and enable a favorable cost-accuracy frontier through budgeted stopping.

The search results show active research into formal bounds, manipulation detection via information theory, and cost-aware multi-judge frameworks in 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "08bfff39-fc55-4f4e-87fb-0dc2cf19e37f",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "eeccd6fc-02d6-42c9-a943-a9febdf2bd79",
  "toolUseResult": {
    "query": "multi-judge LLM evaluation manipulation cost scaling information theory formal bounds 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WWFrPo6txg1F9K2c9DYqJ8",
        "content": [
          {
            "title": "LLM-as-Judge Best Practices in 2026: Calibration, Bias, and Cost",
            "url": "https://futureagi.com/blog/llm-as-judge-best-practices-2026"
          },
          {
            "title": "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/pdf/2508.05469"
          },
          {
            "title": "Limits to scalable evaluation at the frontier: LLM as Judge ...",
            "url": "https://arxiv.org/pdf/2410.13341"
          },
          {
            "title": "LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data",
            "url": "https://labelyourdata.com/articles/llm-as-a-judge"
          },
          {
            "title": "Tuning LLM Judge Design Decisions for 1/1000 of the Cost",
            "url": "https://arxiv.org/pdf/2501.17178"
          },
          {
            "title": "Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation",
            "url": "https://arxiv.org/pdf/2601.14691"
          },
          {
            "title": "Debate, Deliberate, Decide (D3): A Cost-Aware Adversarial Framework for Reliable and Interpretable LLM Evaluation",
            "url": "https://arxiv.org/pdf/2410.04663"
          }
        ]
      },
      "I found relevant research on this topic. Here are the key results:\n\n## Multi-Judge LLM Evaluation & Manipulation\n\nResearch has identified manipulation strategies in LLM judge evaluation, ranging from style-based approaches that alter presentation to content-based approaches that fabricate signals of progress. Prompting-based techniques and scaling judge-time compute reduce but do not fully eliminate susceptibility to manipulation.\n\n## Information-Theoretic Formal Bounds\n\nA key theoretical result (Theorem 3.3) provides finite-sample robustness bounds for information-theoretic mechanisms under mode-collapse attacks, showing that bounded measures like total variation distance (TVD) retain polynomial guarantees whereas unbounded measures like KL divergence can degrade exponentially. This research reveals that detecting strategic manipulation in AI systems reduces to a well-defined information-theoretic problem.\n\n## Cost & Scaling\n\nResearch systematically analyzes and tunes hyperparameters of LLM judges, including the model used, prompt, inference parameters, and parsing mechanisms, analyzing the impact of scaling the judge model and number of instructions on performance. Multi-judge approaches like debate frameworks achieve state-of-the-art agreement with human judgments and enable a favorable cost-accuracy frontier through budgeted stopping.\n\nThe search results show active research into formal bounds, manipulation detection via information theory, and cost-aware multi-judge frameworks in 2026."
    ],
    "durationSeconds": 7.3599727669999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "08bfff39-fc55-4f4e-87fb-0dc2cf19e37f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-20T04:44:33.173Z_

```json
{
  "parentUuid": "eeccd6fc-02d6-42c9-a943-a9febdf2bd79",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "e7e3bee7-13c1-4ae8-afb1-37b1f0fd8aea",
  "timestamp": "2026-05-20T04:44:33.173Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 32 · 2026-05-20T04:44:37.475Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do a couple more targeted searches to check for any directly competing work that might have already addressed the "adversarial dual" of diversity scaling, and to verify the SoK and Kim et al. papers.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e7e3bee7-13c1-4ae8-afb1-37b1f0fd8aea",
  "isSidechain": false,
  "requestId": "req_011CbDDByDajrauJv7XH15C6",
  "type": "assistant",
  "uuid": "820ee663-f22e-47eb-9e88-e8b6f6fd55e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mDDMwg8D1jC8JXYE2jg9W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3594,
      "cache_read_input_tokens": 29629,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 29629,
          "cache_creation_input_tokens": 3594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3594
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

_source line 33 · 2026-05-20T04:44:37.946Z_

Let me do two more targeted searches to check for directly competing work and verify remaining key claims.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "820ee663-f22e-47eb-9e88-e8b6f6fd55e3",
  "isSidechain": false,
  "requestId": "req_011CbDDByDajrauJv7XH15C6",
  "type": "assistant",
  "uuid": "541484ed-9115-467d-884f-e6ab1d1fd2cd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mDDMwg8D1jC8JXYE2jg9W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3594,
      "cache_read_input_tokens": 29629,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 29629,
          "cache_creation_input_tokens": 3594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3594
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

_source line 34 · 2026-05-20T04:44:38.911Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Q6uRGhRrHq783cuhVa9rzo`</summary>

```json
{
  "query": "adversarial manipulation cost scaling number of judges ensemble certified robustness evaluation protocol 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "541484ed-9115-467d-884f-e6ab1d1fd2cd",
  "isSidechain": false,
  "requestId": "req_011CbDDByDajrauJv7XH15C6",
  "type": "assistant",
  "uuid": "3d8f97d5-be52-4efd-80b2-a9b1ad80592b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mDDMwg8D1jC8JXYE2jg9W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3594,
      "cache_read_input_tokens": 29629,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 29629,
          "cache_creation_input_tokens": 3594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3594
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

_source line 35 · 2026-05-20T04:44:39.410Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PD3piGP3jMJAUHKVDXLegX`</summary>

```json
{
  "query": "Kim et al \"Correlated Errors in Large Language Models\" ICML 2025 2506.07962 pairwise agreement"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3d8f97d5-be52-4efd-80b2-a9b1ad80592b",
  "isSidechain": false,
  "requestId": "req_011CbDDByDajrauJv7XH15C6",
  "type": "assistant",
  "uuid": "684f5548-0465-473b-8376-c2526d53efae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015mDDMwg8D1jC8JXYE2jg9W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3594,
      "cache_read_input_tokens": 29629,
      "output_tokens": 218,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3594,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 218,
          "cache_read_input_tokens": 29629,
          "cache_creation_input_tokens": 3594,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3594
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

_source line 36_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "684f5548-0465-473b-8376-c2526d53efae",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---

### Runtime record

_source line 37_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable manipulation resistance for multi-judge LLM evaluation",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---

### Tool result

_source line 38 · 2026-05-20T04:44:45.308Z_

<details><summary>↩ Tool result · `toolu_01PD3piGP3jMJAUHKVDXLegX`</summary>

```text
Web search results for query: "Kim et al "Correlated Errors in Large Language Models" ICML 2025 2506.07962 pairwise agreement"

Links: [{"title":"[2506.07962v1] Correlated Errors in Large Language Models","url":"https://arxiv.org/abs/2506.07962v1"},{"title":"[Paper Note] Correlated Errors in Large Language Models, Elliot Kim+, ICML'25 · Issue #2145 · AkihikoWatanabe/paper_notes","url":"https://github.com/AkihikoWatanabe/paper_notes/issues/2145"},{"title":"(PDF) Correlated Errors in Large Language Models","url":"https://www.researchgate.net/publication/392529896_Correlated_Errors_in_Large_Language_Models"},{"title":"[2506.07962] Correlated Errors in Large Language Models","url":"https://arxiv.org/abs/2506.07962"},{"title":"[PDF] Correlated Errors in Large Language Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Correlated-Errors-in-Large-Language-Models-Kim-Garg/365ba5ab458c8ad6d4ed6996ab3e0ff3f386edbc"},{"title":"Correlated Errors in Large Language Models","url":"https://arxiv.org/pdf/2506.07962"},{"title":"Correlated Errors in Large Language Models","url":"https://arxiv.org/html/2506.07962v1"}]

I found the paper you're looking for! Here's what the search reveals:

## "Correlated Errors in Large Language Models"

**Paper Details:**
- Authors: Elliot Kim, Avi Garg, Kenny Peng, Nikhil Garg
- arXiv: 2506.07962 (submitted June 9, 2025)
- The paper is accepted to ICML 2025

**Key Findings:**

The authors conducted a large-scale empirical evaluation on over 350 LLMs overall, using two popular leaderboards and a resume-screening task.

Regarding pairwise agreement (which relates to your query): They found substantial correlation in model errors -- on one leaderboard dataset, models agree 60% of the time when both models err.

**Main Insights:**
- Factors driving model correlation include shared architectures and providers.
- Crucially, larger and more accurate models have highly correlated errors, even with distinct architectures and providers.
- The effects of correlation are shown in two downstream tasks: LLM-as-judge evaluation and hiring.

The paper is available on arXiv at https://arxiv.org/abs/2506.07962


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "684f5548-0465-473b-8376-c2526d53efae",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "b925c805-3dbb-48fd-b3f2-8eee3dc5ea3a",
  "toolUseResult": {
    "query": "Kim et al \"Correlated Errors in Large Language Models\" ICML 2025 2506.07962 pairwise agreement",
    "results": [
      {
        "tool_use_id": "srvtoolu_01HX7vHnNtATF5K5ZQh9xRpv",
        "content": [
          {
            "title": "[2506.07962v1] Correlated Errors in Large Language Models",
            "url": "https://arxiv.org/abs/2506.07962v1"
          },
          {
            "title": "[Paper Note] Correlated Errors in Large Language Models, Elliot Kim+, ICML'25 · Issue #2145 · AkihikoWatanabe/paper_notes",
            "url": "https://github.com/AkihikoWatanabe/paper_notes/issues/2145"
          },
          {
            "title": "(PDF) Correlated Errors in Large Language Models",
            "url": "https://www.researchgate.net/publication/392529896_Correlated_Errors_in_Large_Language_Models"
          },
          {
            "title": "[2506.07962] Correlated Errors in Large Language Models",
            "url": "https://arxiv.org/abs/2506.07962"
          },
          {
            "title": "[PDF] Correlated Errors in Large Language Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Correlated-Errors-in-Large-Language-Models-Kim-Garg/365ba5ab458c8ad6d4ed6996ab3e0ff3f386edbc"
          },
          {
            "title": "Correlated Errors in Large Language Models",
            "url": "https://arxiv.org/pdf/2506.07962"
          },
          {
            "title": "Correlated Errors in Large Language Models",
            "url": "https://arxiv.org/html/2506.07962v1"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search reveals:\n\n## \"Correlated Errors in Large Language Models\"\n\n**Paper Details:**\n- Authors: Elliot Kim, Avi Garg, Kenny Peng, Nikhil Garg\n- arXiv: 2506.07962 (submitted June 9, 2025)\n- The paper is accepted to ICML 2025\n\n**Key Findings:**\n\nThe authors conducted a large-scale empirical evaluation on over 350 LLMs overall, using two popular leaderboards and a resume-screening task.\n\nRegarding pairwise agreement (which relates to your query): They found substantial correlation in model errors -- on one leaderboard dataset, models agree 60% of the time when both models err.\n\n**Main Insights:**\n- Factors driving model correlation include shared architectures and providers.\n- Crucially, larger and more accurate models have highly correlated errors, even with distinct architectures and providers.\n- The effects of correlation are shown in two downstream tasks: LLM-as-judge evaluation and hiring.\n\nThe paper is available on arXiv at https://arxiv.org/abs/2506.07962"
    ],
    "durationSeconds": 5.895177403000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "684f5548-0465-473b-8376-c2526d53efae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 39 · 2026-05-20T04:44:46.670Z_

<details><summary>↩ Tool result · `toolu_01Q6uRGhRrHq783cuhVa9rzo`</summary>

```text
Web search results for query: "adversarial manipulation cost scaling number of judges ensemble certified robustness evaluation protocol 2025 2026"

Links: [{"title":"Provably Cost-Sensitive Adversarial Defense via Randomized Smoothing | OpenReview","url":"https://openreview.net/forum?id=D7qKAO34tp"},{"title":"Certifying Joint Adversarial Robustness for Model Ensembles","url":"https://arxiv.org/pdf/2004.10250"},{"title":"Tight Certificates of Adversarial Robustness for Randomly Smoothed   Classifiers","url":"https://arxiv.org/pdf/1906.04948"},{"title":"An Ensemble Approach Towards Adversarial Robustness","url":"https://arxiv.org/pdf/2106.05996"},{"title":"Provably Cost-Sensitive Adversarial Defense via Randomized Smoothing","url":"https://arxiv.org/pdf/2310.08732"},{"title":"Certified Adversarial Robustness with Additive Noise","url":"https://arxiv.org/pdf/1809.03113"},{"title":"Enhancing Certifiable Robustness via a Deep Model Ensemble","url":"https://arxiv.org/pdf/1910.14655"}]

Based on the web search results, I found several relevant research papers on adversarial robustness, certified defenses, and ensemble methods. Here's what the search revealed:

## Key Research Areas Found:

**Cost-Sensitive Certified Robustness:**
Recent work introduces provably robust learning algorithms to certify and optimize for cost-sensitive robustness using randomized smoothing, formalizing the definition of cost-sensitive certified radius and adapting standard certification algorithms to generate tight robustness certificates tailored to any cost matrix.

**Ensemble-Based Approaches:**
Research proposes novel techniques for certifying the joint robustness of ensembles, building upon prior works on single-model robustness certification. Studies evaluate the robustness of various model ensembles, including models trained using cost-sensitive robustness to be diverse, to improve understanding of the potential effectiveness of ensemble models as a defense against adversarial examples.

**Scalability of Certification:**
Randomized smoothing has emerged as a robustness certification framework that has attracted attention due to its simplicity and scalability.

The search results include papers from 2025-2026 as well as foundational work on adversarial robustness certification, ensemble methods, and cost-sensitive defenses. The research appears to focus on making robustness certification more practical and scalable while maintaining formal guarantees.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3d8f97d5-be52-4efd-80b2-a9b1ad80592b",
  "isSidechain": false,
  "promptId": "9802b013-499c-4ade-88ad-c7b8449fbc5d",
  "type": "user",
  "uuid": "6fa16492-4a03-48f3-ad61-c6feb1907d2f",
  "toolUseResult": {
    "query": "adversarial manipulation cost scaling number of judges ensemble certified robustness evaluation protocol 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01W3AUndsR5vJEZRjPy4BJ8Y",
        "content": [
          {
            "title": "Provably Cost-Sensitive Adversarial Defense via Randomized Smoothing | OpenReview",
            "url": "https://openreview.net/forum?id=D7qKAO34tp"
          },
          {
            "title": "Certifying Joint Adversarial Robustness for Model Ensembles",
            "url": "https://arxiv.org/pdf/2004.10250"
          },
          {
            "title": "Tight Certificates of Adversarial Robustness for Randomly Smoothed   Classifiers",
            "url": "https://arxiv.org/pdf/1906.04948"
          },
          {
            "title": "An Ensemble Approach Towards Adversarial Robustness",
            "url": "https://arxiv.org/pdf/2106.05996"
          },
          {
            "title": "Provably Cost-Sensitive Adversarial Defense via Randomized Smoothing",
            "url": "https://arxiv.org/pdf/2310.08732"
          },
          {
            "title": "Certified Adversarial Robustness with Additive Noise",
            "url": "https://arxiv.org/pdf/1809.03113"
          },
          {
            "title": "Enhancing Certifiable Robustness via a Deep Model Ensemble",
            "url": "https://arxiv.org/pdf/1910.14655"
          }
        ]
      },
      "Based on the web search results, I found several relevant research papers on adversarial robustness, certified defenses, and ensemble methods. Here's what the search revealed:\n\n## Key Research Areas Found:\n\n**Cost-Sensitive Certified Robustness:**\nRecent work introduces provably robust learning algorithms to certify and optimize for cost-sensitive robustness using randomized smoothing, formalizing the definition of cost-sensitive certified radius and adapting standard certification algorithms to generate tight robustness certificates tailored to any cost matrix.\n\n**Ensemble-Based Approaches:**\nResearch proposes novel techniques for certifying the joint robustness of ensembles, building upon prior works on single-model robustness certification. Studies evaluate the robustness of various model ensembles, including models trained using cost-sensitive robustness to be diverse, to improve understanding of the potential effectiveness of ensemble models as a defense against adversarial examples.\n\n**Scalability of Certification:**\nRandomized smoothing has emerged as a robustness certification framework that has attracted attention due to its simplicity and scalability.\n\nThe search results include papers from 2025-2026 as well as foundational work on adversarial robustness certification, ensemble methods, and cost-sensitive defenses. The research appears to focus on making robustness certification more practical and scalable while maintaining formal guarantees."
    ],
    "durationSeconds": 7.754597029000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3d8f97d5-be52-4efd-80b2-a9b1ad80592b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 40 · 2026-05-20T04:45:54.215Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a solid research base. Let me synthesize my findings and evaluate this proposal carefully.

Let me think through this systematically:

## Key papers verified:
1. ✅ Kaneko & Baldwin (NeurIPS 2025 spotlight) - "Bits Leaked per Query" - verified, real paper
2. ✅ Robertson & Koyejo (arXiv 2508.05469) - "Let's Measure Information Step-by-Step" - verified, real paper, under TMLR review
3. ✅ Yang et al. (ICLR 2026 Workshop) - "Understanding Agent Scaling" - verified, real paper


4. ✅ Turkmen et al. (arXiv 2602.08003) - "Don't Always Pick Highest-Performing Model" - verified, real paper
5. ✅ Chen et al. (NeurIPS 2025) - "Incentivizing Truthful Language Models via Peer Elicitation Games" - verified, NeurIPS 2025 Oral, matches the proposal
6. ✅ Qiu et al. (ICLR 2026) - "Truthfulness Despite Weak Supervision" - verified, ICLR 2026
7. ✅ Kim et al. - continuing to verify the remaining citations

...

Now I'm diving into the core claim of the proposal: that adversarial manipulation cost scales as Ω(K^{g(I_max)}) for K-judge evaluation, where g decreases with inter-judge signal correlation. This is positioned as the adversarial counterpart to Yang et al.'s scaling results. The key question is whether the formal certification bounds provide meaningful value beyond what simple majority voting already achieves empirically—the SoK shows 7-model committees drop attack success rates from 50-68% down to 10-19%, so I need to assess whether the theoretical guarantees justify the added complexity.

The proposal does acknowledge this directly, framing the contribution as providing certifiable bounds analogous to certified adversarial robustness. However, there's a significant issue: the certified bounds (2.6-3.7× improvement for K=7) are actually weaker than what majority voting achieves empirically (~4-5× reduction in attack success rates). This is a legitimate research contribution in the certified robustness tradition, but it raises questions about practical utility when the formal guarantees are consistently looser than empirical performance.

For novelty, the K_eff formula derived from the equicorrelated Gaussian copula model's eigenstructure is fairly straightforward—equicorrelated matrices have well-known spectral properties, so this derivation doesn't feel particularly novel.

The √K scaling under independence directly follows from existing work on randomized smoothing ensembles, and the SDPI composition argument applies known results about contraction coefficients to the judge model setting. The "adversarial dual" framing is novel as a conceptual lens, but the underlying mathematics relies on standard information-theoretic tools applied to a new context. The real technical contribution is combining these existing pieces—Gaussian copulas, SDPI contraction, and Fano decomposition—rather than developing fundamentally new theory.

The core finding itself isn't particularly surprising. Most people would intuitively expect that more independent judges make manipulation harder, that the benefit scales with diversity, and that correlation reduces this advantage. The specific functional form and connection to effective judge count adds some interest, but the qualitative conclusion—that √K scaling emerges for independent judges—maps directly from prior results and feels like a natural extension rather than a counterintuitive discovery.

The proof strategy relies on standard techniques: SDPI for showing perturbation decay across independent channels, Fano decomposition to break down mutual information, and straightforward eigenvalue computation for the Gaussian copula case. The connection from information-theoretic bounds to manipulation cost via Marton's inequality is sound but not novel. The main weakness is the equicorrelated Gaussian copula assumption, which is quite restrictive given that real judge correlations are heterogeneous—varying between 0.7-0.8 for same-family judges and 0.4-0.5 across families. The paper acknowledges this limitation and provides a weaker result for more general settings, but this gap between the idealized model and reality is a notable limitation.

The problem itself is significant—LLM-as-judge security is a genuine concern with documented attack success rates of 50-68%—and formal guarantees do matter to the community. However, the practical utility is questionable when certified bounds are substantially weaker than empirical performance, which the proposal itself notes (2.65× certified versus 4-5× empirical). This mirrors the certifiable robustness literature, where papers get published on the strength of formal guarantees despite modest real-world improvements. The related work section is exceptionally thorough, covering 20+ relevant papers with accurate descriptions and clear identification of gaps—this is genuinely one of the proposal's strongest aspects.

That said, the extensive related work also reveals a limitation: the proposal primarily synthesizes existing mathematical tools (SDPI, Fano decomposition, Gaussian copula, √K scaling) rather than introducing fundamentally new techniques, so the novelty lies mainly in how these are combined and applied to LLM-as-judge robustness. I'm also noticing some key assumptions that may not hold in practice—the Gaussian copula model for judge correlations breaks down in heterogeneous settings with much looser bounds, the information-theoretic framing of adversarial manipulation through noisy channels might miss attack vectors like prompt injection targeting specific judge weaknesses, and there's an open question about whether empirical correlation estimates from benign evaluation actually transfer to adversarial settings.

That last concern is particularly troubling: the framework assumes benign inter-judge correlations (around 0.4-0.5) determine the cost of adversarial manipulation, but a sophisticated attacker could exploit shared vulnerabilities that only emerge under adversarial conditions, potentially driving the effective correlation much higher than what benign data suggests. Looking at the overall picture, the work identifies a clear research gap with solid mathematical grounding and a compelling adversarial dual framing, but the core insight—that more diverse judges resist manipulation better—is somewhat intuitive, and the heavy dependence on existing mathematical machinery limits the conceptual novelty.

The certified bounds end up weaker than what you'd get from simple empirical majority voting, which undermines the practical value. For EMNLP 2026, the topic aligns well with the community's interests in LLM-as-judge robustness, and having an actual deployable protocol helps, but the novelty gap is the real vulnerability. I'm thinking this lands somewhere in the 25-35% acceptance range—the direction is sound and there's genuine technical contribution, but it's more about clever synthesis than fundamental breakthrough. The adversarial dual framing genuinely appears novel—I haven't found prior work formally connecting manipulation cost to the correlation structure governing multi-agent task performance. Though the components are established, their synthesis offers a fresh angle. The Gaussian copula assumptions under adversarial conditions are a legitimate concern, but the proposal addresses heterogeneous correlation through the minimum eigenvalue, and the certified robustness framing is honest about modest practical gains. This could genuinely go either way at EMNLP depending on whether reviewers see it as a meaningful synthesis or incremental work, so I'm settling on 25-35% with a median around 30%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6fa16492-4a03-48f3-ad61-c6feb1907d2f",
  "isSidechain": false,
  "requestId": "req_011CbDDCy4w7t6eS1GpqvA3J",
  "type": "assistant",
  "uuid": "7dcf394c-1254-4b4a-8511-fa125c80aef4",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dir4tfutKo1k41DrtNDGD4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 717,
      "cache_creation_input_tokens": 888,
      "cache_read_input_tokens": 33223,
      "output_tokens": 6850,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 717,
          "output_tokens": 6850,
          "cache_read_input_tokens": 33223,
          "cache_creation_input_tokens": 888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 888
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

_source line 41 · 2026-05-20T04:47:19.872Z_

Now I have sufficient research to evaluate this proposal rigorously. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

- [Kaneko & Baldwin, "Bits Leaked per Query", arXiv 2510.17000] (NeurIPS 2025 Spotlight): 
  建立了单模型信息论攻击成本下界 N_min ≥ log₂(1/ε)/I_max。本 proposal 的 Pillar 1 直接建立在此基础上，声称将其推广到多 judge composition。论文已验证存在且描述准确。

- [Robertson & Koyejo, "Let's Measure Information Step-by-Step", arXiv 2508.05469] (Under TMLR review, 2025): 
  提出 TVD-MI 框架，证明有界 f-divergence 在对抗攻击下保持多项式认证保证（Theorem 3.3），而 KL 等无界度量指数退化。本 proposal 将此从 pairwise 扩展到 N-agent。论文已验证，描述准确。

- [Yang et al., "Understanding Agent Scaling via Diversity", arXiv 2602.03794] (ICLR 2026 Workshop AIMS): 
  信息论多智能体性能 scaling 框架，提出有效通道数 K*、residual uncertainty 以 (1-α_c)^{K*} 衰减。本 proposal 声称提供其"adversarial dual"。论文已验证，描述准确。注意这是 workshop paper，非主会。

- [Turkmen et al., "Don't Always Pick the Highest-Performing Model", arXiv 2602.08003] (Feb 2026): 
  Gaussian copula 相关误差模型，证明信息论误差下限，三项 MI 分解。本 proposal 的 K_eff 公式直接由此推导。论文已验证，描述准确。注意这是 arXiv preprint，尚未被会议接收。

- [Chen et al., "Incentivizing Truthful Language Models via PEG", arXiv 2505.13636] (NeurIPS 2025 Oral): 
  DMI-based peer elicitation，证明 dominant strategy truthfulness。proposal 中描述为 NeurIPS 2025，实际确认为 NeurIPS 2025 Oral，描述准确。

- [Qiu et al., "Truthfulness Despite Weak Supervision", arXiv 2601.20299] (ICLR 2026): 
  Peer prediction 用于 LLM 评估/训练，BNE 保证。论文已验证，描述准确。

- [Kim et al., "Correlated Errors in Large Language Models", arXiv 2506.07962] (ICML 2025): 
  350+ LLMs 误差相关性实证：60% pairwise agreement when both err，same-company +0.066，same-architecture +0.076。为 proposal 的 α regime 估计提供实证基础。论文已验证，描述准确。

- [SoK on LLM-as-Judge Security, arXiv 2603.29403] (April 2026): 
  全面漏洞目录，开源模型 50-68% ASR，7-model committee 经验降低到 10-19% 但无形式化解释。论文已验证，与 proposal 描述一致。

- 直接竞争工作搜索结果：**未发现任何已发表工作正式证明 N-judge manipulation cost 的信息论 scaling bounds**。现有工作要么关注单模型（Kaneko & Baldwin），要么关注 incentive compatibility（Chen et al., Qiu et al.），要么关注 task performance scaling（Yang et al.），但没有将这些 unified 为 adversarial manipulation cost 的形式化 scaling 结果。

- 调研总结：LLM-as-judge 安全是一个活跃且重要的研究方向。现有工作在 (a) 单模型攻击成本下界、(b) peer prediction incentive compatibility、(c) task-performance diversity scaling、(d) 经验性 committee 防御 等方面分别取得进展，但确实缺乏将 manipulation cost 与可测量的 inter-judge 信号相关性形式化联系的理论。Proposal 的 gap 定位基本成立。


【Trivial Alternative 检验】:

最直接的 trivial alternative 是 **简单多数投票 (majority voting)**。SoK 已经表明 7-model committee 通过 majority voting 将 ASR 从 50-68% 降至 10-19%（约 4-5× 改善）。这是一个零理论、零额外设计成本的 baseline。

本 proposal 的 certified bound 对 K=7 给出 2.65-3.7× 改善——**在数值上弱于 majority voting 的经验性改善**。Proposal 自身也承认了这一点，并诉诸"certified robustness"类比（类似 randomized smoothing 提供比 empirical defense 更保守但可证明的保证）。

增量价值在于：(1) 形式化保证——即使面对未来未知攻击也成立；(2) 可计算的 per-evaluation robustness certificate；(3) 将 diversity scaling 理论从 task performance 推广到 adversarial manipulation。但这个增量价值的说服力取决于审稿人是否认同"modest certified bound > strong empirical defense without guarantee"的价值体系。在 certified adversarial robustness 社区这被接受，但在 NLP 社区这一价值主张的接受度尚不确定。

**结论：存在有力的 trivial alternative，增量价值是 certifiability，但实际数值 margin 确实 modest。**


【前提假设检验】:

核心 claim 的逻辑链中存在以下未经充分验证的假设：

1. **Gaussian copula 等相关假设在对抗条件下仍然成立**：Turkmen et al. 的 copula 相关性（cross-family ρ~0.4-0.5）是在 benign evaluation 条件下测量的。但在 adversarial 攻击下，judges 的相关结构可能发生剧变——例如，所有 judges 可能对同一类型的 prompt injection 或 adversarial suffix 同等脆弱，使得 effective ρ 在攻击条件下远高于 benign 条件下的估计值。这意味着 α 可能在实际攻击中坍缩到接近 0，使 certified bound 接近 vacuous。**这是最关键的未验证假设。**

2. **对抗操纵可以被建模为通过噪声信道的扰动**：proposal 将每个 judge 建模为从"真实质量"到评分的噪声信道，adversary 的操纵是信道扰动。但现实攻击（如 prompt injection、adversarial suffix）可能绕过信道模型——它们直接修改 judge 的输入而非扰动信道本身。SDPI 框架假设 adversary 的操纵受信道容量限制，但某些攻击可能 exploit 模型的具体漏洞而非通用信息论限制。

3. **Equicorrelation 假设的可推广性**：closed-form 结果需要所有 pairwise MI 相等（I_max），而 Kim et al. 的数据明确表明 same-family 和 cross-family 相关性差异很大（ρ 从 0.4 到 0.8）。虽然 proposal 提供了 heterogeneous correlation 的弱化结果（g ≥ ½·λ_min(Σ)），但 λ_min-based bound 通常非常松散，可能实际上 vacuous。

4. **从 single-model 到 multi-judge 的 composition 假设**：Kaneko & Baldwin 的单模型 bound 假设 adaptive adversary 在每次 query 中获取固定的 mutual information。Multi-judge 设置中 adversary 可以利用 judges 之间的信息泄漏（e.g., 一个 judge 的响应可能泄漏另一个 judge 的决策信息），这并非简单的独立信道 composition。


【3 维度打分】:

1. **Novelty: 中** — 
   核心贡献是将已有数学工具（SDPI from Polyanskiy & Wu 2017, Fano decomposition from Morishita et al. ICML 2022, Gaussian copula from Turkmen et al. 2026, √K scaling from Horvath et al. 2021, single-model bounds from Kaneko & Baldwin NeurIPS 2025）综合应用于新的问题设定（multi-judge adversarial manipulation cost）。经搜索确认，"adversarial dual of diversity scaling"这个特定联系在现有文献中确实未出现——这是一个真实的 novelty delta。
   
   但 novelty 的 **深度** 有限：(a) K_eff = 1+(K-1)·exp(-2·I_max) 本质上是等相关矩阵特征值的标准推导加上 ρ-to-MI 的变量替换；(b) √K 缩放直接来自 Horvath et al.；(c) 三个 pillar 中每一个都是已有工具的直接应用。这是 synthesis novelty 而非 fundamental novelty。核心发现（diverse judges → higher manipulation cost, modulated by correlation）在定性层面完全符合直觉。

2. **Significance: 中** — 
   LLM-as-judge 安全是一个重要且 timely 的方向（SoK 2603.29403 的发现令人担忧，50-68% ASR）。形式化保证在原则上有价值。但显著性受限于：(a) certified bounds 在数值上弱于 trivial majority voting 的经验效果，这使得实际部署价值存疑；(b) 对 NLP 社区而言，"certified robustness for evaluation"这个概念是否足够 impactful 尚不明确——不同于 certified robustness for classification（模型被部署在安全关键场景），evaluation protocol 的 certifiability 需求可能被视为一个较小的问题；(c) 理论结果对已知经验现象（committee 降低 ASR）的解释力是正面的，但 "formalizing what we already observed empirically" 的 significance ceiling 有限。

3. **Related Work: 强** — 
   这是 proposal 最突出的优势。引用了 20+ 篇高度相关的论文，覆盖面极广（information theory, peer prediction, certified robustness, empirical security, error correlation, collusion, multi-agent evaluation）。经验证的所有关键论文（Kaneko & Baldwin, Robertson & Koyejo, Yang et al., Turkmen et al., Chen et al., Qiu et al., Kim et al.）均真实存在且描述准确。Gap 定位清晰且经搜索确认基本成立。唯一的小瑕疵：Yang et al. 是 workshop paper（ICLR 2026 Workshop AIMS），而非主会论文，proposal 中已标注但在 framing 中将其与主会论文并列使用时可能被审稿人挑战其 authority。


【概率估计】: [23% - 33%] 中位 28%

【估计理由】: 
Novelty 是限制上界的主要维度。虽然 "adversarial dual of diversity scaling" 在特定联系层面确实新颖，但核心技术贡献是已有数学工具的综合应用，核心定性结论（多样性 judges 提高操纵成本，受相关性调节）完全符合直觉——如果结果为 positive，大多数审稿人会说 "makes sense, I would have guessed the direction"。Significance 因 certified bounds 在数值上弱于经验性 majority voting 而进一步受限——这使得"为什么不直接用 majority voting"成为一个难以完全回答的审稿问题。Related Work 的强势提升了下界（proposal 形式完善、定位清晰，不会因 coverage 问题被轻易拒绝）。

从 rubric 对应：Novelty 中 + Significance 中 → idea 核心处于 "方向正确、有真实 novelty delta，但核心发现不够 surprising" 的 25-35% 区间。certified bounds 弱于 trivial baseline 的问题以及 Gaussian copula 在对抗条件下的假设风险进一步将中位数拉向区间下半部分。

【主要风险】: 
1. **"Why not just majority vote?" 问题**：certified bounds (2.65-3.7×) 在数值上弱于 majority voting 的经验效果 (~4-5×)。审稿人可能认为 certifiability 的价值不足以弥补 practical margin 的差距，尤其在 NLP 社区（相比 ML safety/robustness 社区）对 formal certification 的重视程度较低的背景下。
2. **Benign-condition correlation ≠ adversarial-condition correlation**：整个理论框架依赖于 benign 条件下测量的 ρ 值来 certify 对抗条件下的 manipulation cost，但 adversarial 攻击可能系统性地利用所有 judges 的共享弱点（如共享训练数据来源的 vulnerability），使得 effective ρ 在攻击下远高于预期，potentially 使 certified bound 接近 vacuous。这是一个 idea 层面的逻辑链漏洞，无法通过补实验解决。
```

Sources:
- [Bits Leaked per Query (Kaneko & Baldwin, NeurIPS 2025)](https://arxiv.org/abs/2510.17000)
- [Let's Measure Information Step-by-Step (Robertson & Koyejo)](https://arxiv.org/abs/2508.05469)
- [Understanding Agent Scaling via Diversity (Yang et al., ICLR 2026 Workshop)](https://arxiv.org/abs/2602.03794)
- [Don't Always Pick the Highest-Performing Model (Turkmen et al.)](https://arxiv.org/abs/2602.08003)
- [Incentivizing Truthful Language Models via PEG (Chen et al., NeurIPS 2025)](https://arxiv.org/abs/2505.13636)
- [Truthfulness Despite Weak Supervision (Qiu et al., ICLR 2026)](https://arxiv.org/abs/2601.20299)
- [Correlated Errors in Large Language Models (Kim et al., ICML 2025)](https://arxiv.org/abs/2506.07962)
- [SoK on LLM-as-Judge Security](https://arxiv.org/abs/2603.29403)
- [LLMs Cannot Reliably Judge (RobustJudge)](https://arxiv.org/abs/2506.09443)
- [Certified Ensemble Robustness (Horvath et al.)](https://arxiv.org/abs/2106.06946)
- [Certifying Joint Adversarial Robustness for Model Ensembles (Chiang et al.)](https://arxiv.org/abs/2004.10250)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7dcf394c-1254-4b4a-8511-fa125c80aef4",
  "isSidechain": false,
  "requestId": "req_011CbDDCy4w7t6eS1GpqvA3J",
  "type": "assistant",
  "uuid": "9151bca5-69c3-4f26-ad9e-77c5d81d6e84",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Dir4tfutKo1k41DrtNDGD4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 717,
      "cache_creation_input_tokens": 888,
      "cache_read_input_tokens": 33223,
      "output_tokens": 6850,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 888,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 717,
          "output_tokens": 6850,
          "cache_read_input_tokens": 33223,
          "cache_creation_input_tokens": 888,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 888
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

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "9151bca5-69c3-4f26-ad9e-77c5d81d6e84",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable manipulation resistance for multi-judge LLM evaluation",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---

### Runtime record

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "9151bca5-69c3-4f26-ad9e-77c5d81d6e84",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable manipulation resistance for multi-judge LLM evaluation",
  "sessionId": "97cb931e-0643-49df-bf91-c7f456ede1a1"
}
```

---
