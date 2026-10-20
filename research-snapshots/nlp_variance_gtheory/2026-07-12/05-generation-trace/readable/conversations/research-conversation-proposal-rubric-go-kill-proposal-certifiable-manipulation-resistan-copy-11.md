# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # Certifiable Manipulation Resistan

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 47
- **Recorded user turns:** 1
- **Tool calls:** 12
- **Original source:** `logs/chats/exported-trajectories/account-3/6d02cf48-9e78-46e7-b465-97583625cdc6.jsonl`
- **Structured JSON:** [`1271ed3e92d25df72948.json`](../../sessions/12/1271ed3e92d25df72948.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T04:43:55.266Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T04:43:55.266Z",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Correlation Structure\n\n## Description\nLLM evaluation faces systematic adversarial vulnerabilities—open-source judge models show 50–68% average attack success rates (SoK, April 2026), and arena rankings can be flipped with ~1,000 strategic votes (ICML 2025). While Robertson & Koyejo (2025) proved bounded f-divergence certification guarantees for single evaluators, concurrent works established peer prediction incentive-compatibility (Qiu et al., ICLR 2026, via BNE; Chen et al., NeurIPS 2025, via dominant-strategy DMI), and Kaneko & Baldwin (NeurIPS 2025 spotlight) proved tight single-model attack cost bounds (N_min ≥ log₂(1/ε)/I_max), no work provides formal N-judge manipulation-cost scaling—the adversarial dual of the task-performance scaling recently established by Yang et al. (ICLR 2026 Workshop AIMS). We bridge this gap by proving that adversarial manipulation cost grows as Ω(K^{g(I_max)}) where g is an explicit decreasing function of inter-judge signal correlation, derived via a three-pillar proof strategy: (1) SDPI contraction composition (Polyanskiy & Wu) showing perturbation decays multiplicatively across independent channels; (2) Fano-ensemble decomposition (Morishita et al., ICML 2022) separating relevance, redundancy, and combination loss; (3) Gaussian-copula closed form—adapting Turkmen et al.'s equicorrelated model, we derive K_eff = 1+(K-1)·exp(-2·I_max). Under the copula model, g(I_max) = ½·log(K_eff)/log(K), which equals ½ for independent judges (matching √K certified radius scaling from randomized smoothing) and degrades gracefully with correlation. For cross-family ensembles (DeepSeek-V4-Flash, Qwen-3.5, Llama-4-Maverick), we estimate α ∈ [0.35, 0.65] based on copula correlations ρ~0.4-0.5 (Turkmen et al.) and correlated error measurements (Kim et al., ICML 2025), providing certified manipulation-cost bounds of 2.6–3.7× for K=7. We frame this as certifiable robustness for LLM evaluation: just as certified adversarial defenses provide provable guarantees despite sometimes modest empirical margins, our protocol certifies per-evaluation manipulation-resistance bounds that hold against arbitrary future attacks—a guarantee majority voting fundamentally cannot provide. We validate against RobustJudge's 15 realistic attack methods, reporting certified bounds alongside empirical ASR, with sensitivity analysis for α ∈ [0.2, 0.8].\n\n## Core Problem\nCan we provide certifiable manipulation-resistance guarantees for N-judge LLM evaluation protocols, where the certified robustness bound is an explicit, computable function of measurable inter-judge signal correlation, validated against realistic adversarial attacks?\n\n## Opportunity\nRobertson & Koyejo (2025) established that bounded f-divergences like TVD maintain polynomial certification guarantees under adversarial manipulation while unbounded measures (KL) fail (Theorem 3.3), and multiple concurrent works have established peer prediction incentive-compatibility for LLM evaluation (Qiu et al., ICLR 2026; Chen et al., NeurIPS 2025). However, three critical gaps remain: (1) No existing work provides formal N-agent scaling results connecting manipulation cost to measurable inter-judge signal correlation—Robertson & Koyejo analyze pairwise evaluations without multi-judge aggregation theory, Qiu et al. provide no polynomial cost bounds tied to judge count, and Chen et al.'s PEG dominant-strategy guarantee requires conditional independence without characterizing degradation under partial correlation; (2) Empirical validation uses only generic semantic-preserving transforms or deceptive finetuning, not realistic attack vectors documented by the SoK (prompt injection ASR 50–68%, adversarial suffixes, strategic vote rigging); (3) The information-theoretic diversity-scaling framework of Yang et al. (ICLR 2026 Workshop AIMS) shows that multi-agent system performance is bounded by effective channel count K* with residual uncertainty decaying as (1-α_c)^{K*}, but this addresses task performance, not adversarial manipulation resistance—no work establishes the dual result for manipulation cost. Meanwhile, Turkmen et al. (2602.08003) prove that correlated ensembles hit an irreducible error floor Φ(Φ⁻¹(1-p)/√ρ) under their Gaussian copula model, and their three-term MI decomposition (accuracy - redundancy + error correlation) provides the mathematical toolkit for our α estimation. Kaneko & Baldwin (NeurIPS 2025 spotlight) prove tight single-model information-theoretic attack cost bounds N_min ≥ log₂(1/ε)/I_max via Fano inequality, but do not address multi-judge composition. The SoK (2603.29403) finds that 7-model committees empirically reduce ASR to 10–19% but provides no formal explanation. We aim to bridge these gaps by providing the adversarial-robustness dual of the task-performance scaling theory, yielding certifiable manipulation-resistance bounds analogous to certified adversarial robustness in classification.\n\n## Landscape\nRobertson & Koyejo's 'Let's Measure Information Step-by-Step' (arXiv 2508.05469, under TMLR review) formalizes LLM evaluation as an information elicitation game using TVD-MI, proves that bounded f-divergences maintain polynomial certification guarantees under mode-collapse attacks (Theorem 3.3) while unbounded measures like KL degrade exponentially, and demonstrates TVD-MI effectiveness (AUC 0.70–0.77) under generic semantic transforms. Their Identity-Link IRT follow-up (2510.14966) extends to sparse evaluation with two-judge validation (Spearman ρ=0.872) but without formal multi-judge theory.\n\nQiu et al.'s 'Truthfulness Despite Weak Supervision' (ICLR 2026, 2601.20299) applies peer prediction to LLM evaluation/training with Bayesian Nash equilibrium guarantees (Theorem 1) and an empirical inverse scaling property, but targets output truthfulness rather than adversarial robustness of the evaluation protocol itself, acknowledges only unilateral deception (not collusion), and uses no information-theoretic divergence measures.\n\nChen et al.'s 'Incentivizing Truthful Language Models via Peer Elicitation Games' (NeurIPS 2025, 2505.13636) introduces multi-agent peer elicitation using Determinant Mutual Information (DMI) scoring and proves a strictly stronger result: dominant strategy truthfulness (Lemma 1), meaning truthful reporting is optimal regardless of other agents' strategies—not just in Bayesian Nash equilibrium. Their sublinear O(√T) regret bound (Theorem 2) and last-iterate convergence to Nash equilibrium (Theorem 3) via online mirror descent provide a complementary theoretical foundation to Qiu et al.'s BNE. PEG requires n≥2 discriminators and K_t≥4 tasks with conditional independence (Assumption 4), and their experiments use 3 discriminators with the theoretical minimum n≥2 and K_t≥4 tasks required by Lemma 1. However, PEG does not characterize how its manipulation-resistance guarantees degrade when the conditional independence assumption is violated—precisely the regime we analyze.\n\nYang et al.'s 'Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity' (ICLR 2026 Workshop AIMS, 2602.03794) provides an information-theoretic framework where multi-agent system performance is bounded by intrinsic task uncertainty H(Y|X) with residual uncertainty decaying as (1-α_c)^{K*}, where α_c is the complementarity rate and K* = 2^{H(ρ)} is the effective channel count computed via von Neumann entropy of the embedding Gram matrix (Theorem 4.3). Their heterogeneity advantage corollary (Corollary 4.4) formally shows α_het·K_het > α_hom·K_hom implies strictly better performance. Critically, K* captures diversity in embedding space without labels and empirically correlates with accuracy (r=0.388 overall, r=0.535 for K*_c among correct agents). However, their framework addresses task performance (information recovery) not adversarial manipulation resistance (information perturbation cost). Our work establishes the adversarial dual: while their K* governs how quickly residual uncertainty decreases, our framework shows that the same correlation structure governs how quickly manipulation cost increases.\n\nTurkmen et al.'s 'Don't Always Pick the Highest-Performing Model' (arXiv 2602.08003, Feb 2026) formulates ensemble selection as MI maximization with a Gaussian-copula correlated error model and proves an information-theoretic error floor (Theorem 4.4): lim_{m→∞} P_e = Φ(Φ⁻¹(1-p)/√ρ) > 0 for equicorrelated ensembles with pairwise copula correlation ρ. Their three-term MI decomposition (Theorem 4.3)—Δ(j|S) = I(Y;X_j) - I(X_j;X_S) + I(E_j;E_S)—separates accuracy, redundancy, and error correlation. Empirically, they find within-family correlations ρ~0.7-0.8 and cross-family ρ~0.4-0.5. Their copula model provides the mathematical foundation for our derivation of effective independent channel count K_eff.\n\nKaneko & Baldwin's 'Bits Leaked per Query' (NeurIPS 2025 spotlight, arXiv 2510.17000) establishes tight information-theoretic bounds on adversarial attack costs against individual LLMs: any adaptive attack achieving error ≤ ε requires at least N_min ≥ log₂(1/ε)/I_max queries, where I_max is the maximum per-query mutual information leakage (Theorem 1), and this bound is achieved by sequential probability ratio tests (Theorem 2). Validated across 7 LLMs including Llama-4 and DeepSeek-R1, they identify four disclosure regimes (answer-only ~0.001-0.01 bits to full-access ~1.0+ bits). This provides the single-model information-theoretic attack cost foundation; our work extends the composition theory to multi-judge settings where an adversary must simultaneously fool K correlated judges.\n\nShen et al.'s 'Robust LLM Performance Certification via Constrained MLE' (arXiv 2604.03257, Google DeepMind/UCL, 2026) proposes constrained maximum likelihood estimation fusing human labels, LLM-judge annotations, and domain constraints (known TPR/FPR bounds) for certified LLM performance estimation. While addressing performance certification under benign judge noise, it assumes honest judges and does not model adversarial manipulation—precisely the threat model we address.\n\nFeng et al.'s 'Noisy but Valid' (ICLR 2026, arXiv 2601.20913) provides a statistical hypothesis testing framework for certifying LLM failure rates using imperfect judges, with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty. Using a small human-labeled calibration set to estimate judge TPR/FPR, they derive variance-corrected critical thresholds (Theorem 5.4 gives exact conditions for judge adoption). Like Shen et al., this assumes honest but fallible judges, not adversarial manipulation. Our work complements both: Shen et al. certify performance estimates via constrained MLE, Feng et al. certify statistical validity via hypothesis testing, and we certify manipulation resistance under adversarial attacks.\n\nJung & Na's 'Logarithmic Scores, Power-Law Discoveries' (arXiv 2604.00477, April 2026) identifies a score-coverage dissociation in multi-agent evaluation panels: scoring reliability (ICC) scales logarithmically with panel size N (R²=0.974) while unique issue discovery follows a sublinear power law y=7.8·N^0.69 (R²=0.999). Scores saturate ~2× faster than discoveries, with N=8 achieving 82% of maximum scoring reliability but only ~42% of N=32 discovery level. This has direct implications for our K-scaling claims: manipulation-cost scaling benefits may exhibit similar dissociation, where formal robustness guarantees saturate faster than empirical coverage of attack surface. We analyze this explicitly.\n\nThe SoK on LLM-as-Judge Security (2603.29403, April 2026) catalogs extensive vulnerabilities: open-source models showing 50–68% average ASR and frontier models 27–44%; 7-model diverse committees reduce ASR to 10–19% empirically but without formal explanation. RobustJudge (2506.09443) benchmarks 15 attack methods and 7 defense strategies. CAP (OpenReview 2026) shows comparative assessment is more robust than absolute scoring but provides no formal guarantees.\n\nOn error correlation and independence: Kim et al.'s 'Correlated Errors in Large Language Models' (ICML 2025, arXiv 2506.07962) shows 60% pairwise agreement when both err on Helm (vs. 33% random baseline), with same-company adding +0.066 and same-architecture adding +0.076 agreement. Chen et al.'s behavioral entanglement framework (arXiv 2604.07650) introduces BEI and CIG metrics across 18 LLMs from 6 families, finding cross-family entanglement 40–60% lower than intra-family.\n\nOn coordination failure: Frongillo et al. (2503.16280) prove that uninformative equilibria become unstable with fine-grained signals. Keppo et al.'s collusion fragility analysis (2603.20281) finds increasing LLM count from 2→5 breaks collusion (+22%→+3%), but same-family size heterogeneity stabilizes via leader-follower dynamics—motivating cross-family diversity.\n\nOn multi-agent evaluation: CollabEval (2603.00993) proposes three-phase multi-agent evaluation without formal adversarial guarantees. Ebrahimi et al. (IJCNLP-AACL 2025, 2505.24239) uses credibility-based iterative aggregation for adversary resistance without information-theoretic measures.\n\nOn certified ensemble robustness: Chen et al. (2107.10873) prove that diversified gradient and large confidence margin are jointly necessary and sufficient for certified ensemble robustness—standard ensembles achieve only marginal improvements without explicit diversity. Horvath et al. (2106.06946) show randomized smoothing ensembles achieve √K-type certified radius improvement. These provide precedent for polynomial scaling bounds from diversity.\n\nTHE KEY GAP: No existing work provides formal N-agent manipulation-cost scaling results—the adversarial dual of Yang et al.'s task-performance scaling—where the bound is an explicit computable function of measurable inter-judge signal correlation, yielding certifiable robustness guarantees validated against realistic attacks. Kaneko & Baldwin provide the single-model attack cost foundation; we provide the multi-judge composition theory. Shen et al. and Feng et al. certify evaluation quality under noise; we certify resistance under adversarial attacks.\n\n## Approach\nWe extend Robertson & Koyejo's TVD-MI framework from pairwise evaluation to N-agent multi-judge settings with certifiable manipulation-resistance bounds, drawing on the Gaussian-copula correlation model (Turkmen et al.) and information-theoretic diversity scaling (Yang et al.) for the formal machinery, and extending Kaneko & Baldwin's single-model attack cost bounds to multi-judge composition. Our contribution has five components:\n\n**Component 1: Theoretical Framework—The Adversarial Dual of Diversity Scaling.**\n\nWe prove that when K judge models evaluate candidate responses using TVD-MI scoring, the adversarial manipulation cost grows as Ω(K^{g(I_max)}), where g is an explicit decreasing function of the maximum pairwise mutual information I_max between judge signals. This establishes the adversarial dual of Yang et al.'s task-performance result: while their Theorem 4.3 shows residual uncertainty decreases as (1-α_c)^{K*}, we show manipulation cost increases polynomially in K with exponent determined by the same underlying correlation structure.\n\n**Proof Strategy (Three-Pillar Approach):**\n\n*Pillar 1—Strong Data Processing Inequality (SDPI) Composition.* We model each judge as a noisy channel from the 'true quality' signal to an evaluation score. Following Polyanskiy & Wu (2017), SDPI contraction coefficients compose multiplicatively across independent channels: an adversary pushing perturbation through K independent channels experiences η^K total contraction, where η ∈ (0,1) is the per-channel contraction coefficient. Under inter-judge correlation, the effective number of independent channels is reduced from K to K_eff. This extends Kaneko & Baldwin's single-channel result (N_min ≥ log₂(1/ε)/I_max) to multi-channel settings: the adversary's total information gain across K correlated judges is bounded by K_eff · I_max per query round.\n\n*Pillar 2—Fano-Ensemble Decomposition.* Following Morishita et al. (ICML 2022), we decompose the total MI I(Y; Z_1,...,Z_K) available to the aggregator into K individual relevance terms, pairwise redundancy terms involving I_max, and combination loss terms. The adversary must reduce this total MI below the Fano threshold for correct decision-making, and the required perturbation energy is lower-bounded by the effective information.\n\n*Pillar 3—Gaussian Copula Closed Form.* Adapting Turkmen et al.'s equicorrelated Gaussian copula model (where Z_j = √ρ·U + √(1-ρ)·ξ_j with shared latent factor U), we derive the effective independent channel count:\n\n  K_eff = 1 + (K-1)·exp(-2·I_max)\n\nwhere I_max = -½ log(1-ρ²) is the pairwise MI under the copula model. This formula is our own derivation, obtained by computing the effective rank of the K×K correlation matrix under equicorrelation: eigenvalues are λ₁ = 1+(K-1)ρ (multiplicity 1) and λ₂ = 1-ρ (multiplicity K-1), and the effective independent dimensionality follows from the ratio of total to maximum variance, expressed as a function of MI via the ρ-to-I_max mapping ρ² = 1-exp(-2·I_max).\n\nThe manipulation cost lower bound is then Ω(K_eff^{1/2}) from variance-reduction arguments (following Horvath et al.'s √K certified radius scaling for randomized smoothing ensembles), giving:\n\n  g(I_max) = ½ · log(1 + (K-1)·exp(-2·I_max)) / log(K)\n\nThis satisfies the boundary conditions: g(0) = ½·log(K)/log(K) = ½ for fully independent judges (matching √K variance reduction), and g(I_max) → 0 as I_max → ∞ (fully correlated judges collapse to a single effective channel). The ½ exponent for independent judges is tight under the variance-reduction argument; if the SDPI chain yields linear rather than √K scaling, we get g(0) = 1.\n\n*Key Lemma (Connection from MI to Perturbation Budget):* We connect information-theoretic bounds to operational manipulation cost via Marton's inequality: TV(P,Q)² ≤ ½·KL(P||Q), combined with Robertson & Koyejo's Theorem 3.3 relating TVD-MI to certification bounds. The adversary's perturbation must overcome the TVD gap, which scales with √K_eff under the copula model.\n\n*Distributional Assumptions:* The closed-form result requires the equicorrelated Gaussian copula on judge signals (marginals can be arbitrary; only the dependence structure is Gaussian) and equicorrelation (all pairwise MIs equal I_max). We prove a weaker but more general result under arbitrary pairwise MI structure: g depends on the minimum eigenvalue of the correlation matrix, giving g ≥ ½·λ_min(Σ). For heterogeneous correlation, we use the effective rank of the correlation matrix (analogous to Yang et al.'s K* = 2^{H(ρ)}) as a tighter proxy.\n\n**Component 2: Practical α Regime Analysis with Sensitivity Bounds.**\n\nUsing Turkmen et al.'s empirical copula correlations (within-family ρ~0.7-0.8, cross-family ρ~0.4-0.5) and Kim et al.'s correlated error data (same-company +0.066, same-architecture +0.076; ICML 2025, arXiv 2506.07962), we estimate for the proposed three-judge cross-family ensemble:\n\n- Central estimate: ρ ≈ 0.45, I_max ≈ 0.11, α = g(I_max) ∈ [0.35, 0.65]\n- At α=0.5, K=7: manipulation cost ≈ 7^0.5 ≈ 2.65× single-judge baseline\n- At α=0.65, K=7: manipulation cost ≈ 7^0.65 ≈ 3.7×\n\n*Sensitivity analysis and break-even:* We explicitly plan for the possibility that empirically measured α falls outside our predicted range, since current correlation data is from prior-generation models (Kim et al.'s 350+ mostly older LLMs, Chen et al.'s 18 models from prior families). DeepSeek-V4, Qwen-3.5, and Llama-4-Maverick may show different correlation structures due to shared training data evolution (Common Crawl, synthetic data from frontier models) and partial architectural convergence (all three use MoE, though with different routing and attention mechanisms).\n\n- If α = 0.2 (more correlated than expected, ρ ≈ 0.65): K=7 yields only 7^0.2 ≈ 1.55× cost increase. The protocol still provides formal guarantees that majority voting cannot, but the practical margin is thin. At this α, our protocol's value proposition is primarily the certifiability—analogous to how randomized smoothing provides modest certified radii but with provable guarantees.\n- If α = 0.8 (more independent than expected, ρ ≈ 0.25): K=7 yields 7^0.8 ≈ 5.2× cost increase—substantially better than baseline. This would indicate that cross-family diversity is even more effective than prior-generation data suggested.\n- Break-even analysis: Majority voting with K=7 achieves empirical ASR reduction from 50-68% to 10-19% (SoK), a ~4-5× reduction in success probability. Our protocol must provide comparable ASR reduction plus formal guarantees to be justified. We identify the critical α threshold where the certified bound becomes vacuous (i.e., the formal guarantee is weaker than the trivially achievable baseline): for K=7, this occurs at approximately α ≤ 0.05, corresponding to ρ ≥ 0.95 (near-identical judges). For any realistic cross-family ensemble, we are well above this threshold.\n- Diminishing returns analysis: Following Jung & Na's (2604.00477) finding that scoring reliability scales logarithmically while discovery scales as N^0.69, we analyze whether our manipulation-cost scaling exhibits similar dissociation. The formal certified bound may saturate faster (logarithmically in K) than the empirical ASR reduction (which may follow a power law), creating a gap between what we can certify and what we observe.\n\n**Component 3: Practical Protocol Design.**\n\nWe instantiate the framework as a deployable multi-judge evaluation protocol using three architecturally diverse open-weight model families—DeepSeek-V4-Flash (284B MoE, 13B active, Multi-head Latent Attention), Qwen-3.5 (397B MoE, 17B active), and Llama-4-Maverick (400B MoE, 17B active). These models are chosen because: (a) they come from three different organizations with different training data pipelines, minimizing same-company correlation (+0.066 per Kim et al.); (b) they use different architectural innovations, minimizing same-architecture correlation (+0.076); (c) Turkmen et al.'s copula framework predicts cross-family ρ~0.4-0.5 for such configurations.\n\nThe protocol operates in three phases:\n1. **Independence measurement:** Compute pairwise TVD-MI scores between all judge pairs on a calibration set; estimate the copula correlation ρ_ij and I_max; compute effective channel count K* (à la Yang et al.) and predicted α.\n2. **Evaluation with certified scoring:** Each judge evaluates candidates using TVD-MI; the aggregator combines scores via DMI-weighted aggregation (adapting PEG's determinant-based scoring from Chen et al., NeurIPS 2025), which provides dominant-strategy truthfulness (Lemma 1) when judges are approximately conditionally independent.\n3. **Certification:** Output both the aggregated evaluation and the certified manipulation-cost bound Ω(K^α) with the empirically measured α, constituting a per-evaluation robustness certificate.\n\nWe prove the coordination failure argument leveraging both PEG's dominant-strategy result (which applies under conditional independence) and Qiu et al.'s BNE framework (which applies under the weaker shared-prior assumption). For the regime between these extremes—partial correlation that violates conditional independence but maintains bounded MI—we provide interpolating bounds via the SDPI framework.\n\n**Component 4: Certifiable Robustness Framing.**\n\nWe explicitly frame our contribution as 'certifiable robustness for LLM evaluation,' drawing the analogy to certified adversarial robustness in classification (randomized smoothing, interval bound propagation). Just as certified adversarial defenses often achieve smaller empirical improvements than heuristic defenses but provide provable guarantees, our protocol may achieve ASR reductions comparable to majority voting but with formal certificates. The value proposition is:\n\n- Majority voting: empirically reduces ASR from ~60% to ~15% for K=7 (SoK), but with no formal guarantee—the ASR could spike under novel attacks.\n- Our protocol: achieves comparable empirical ASR reduction AND provides a formal lower bound on the manipulation cost that scales as Ω(K^α), certified per-evaluation. This means even against unforeseen future attacks, the manipulation cost is provably bounded below.\n- Connection to single-model bounds: Kaneko & Baldwin's N_min ≥ log₂(1/ε)/I_max provides the per-judge attack cost floor; our multi-judge composition shows that the adversary's total cost scales as K_eff times this single-judge bound, yielding certifiable multi-judge manipulation resistance.\n\nThis framing directly addresses the concern that 2.65-4.0× scaling may seem modest: in certified adversarial robustness, even modest certified radii are valued because they are provable, while large empirical margins can be broken by adaptive attacks.\n\n**Component 5: Realistic Adversarial Validation.**\n\nWe evaluate against RobustJudge's 15 attack methods (including PAIR, combined attacks, adversarial suffixes, and prompt injection) plus the SoK's documented attack vectors, on text summarization, code generation, and knowledge-intensive QA tasks. We benchmark against: (a) all 7 RobustJudge heuristic defenses; (b) CAP comparative augmented prompting; (c) CollabEval's consensus-based multi-agent approach; (d) Ebrahimi et al.'s credibility-scoring framework; (e) Robertson & Koyejo's single-evaluator TVD-MI baseline; (f) simple majority voting (K=3,5,7); (g) PEG with DMI scoring (Chen et al.). For each experimental condition, we report: (i) attack success rate, (ii) empirically measured ρ_ij and I_max, (iii) computed α, (iv) the gap between the certified manipulation-cost bound and the observed empirical manipulation cost, and (v) whether the formal bound is tight (ratio of empirical to certified). Following the score-coverage dissociation insight (Jung & Na), we separately analyze certification tightness (how close the formal bound is to the empirical one) and attack surface coverage (what fraction of attack types the bound holds against).\n\n## Resource Estimate\n{'manual': {'gpu_hours': '1,000-1,500 H100-equivalent', 'timeline': '14-18 weeks', 'estimated_gpu_cost': '$2,500-$3,750 at $2.50/hr H100 spot', 'gpu_breakdown': 'DeepSeek-V4-Flash: 2×H100 FP8 (~160GB VRAM); Qwen-3.5: 4×H100 INT4 (~200GB) or 8×H100 FP8 (~400GB); Llama-4-Maverick: 4×H100 INT4 (~200GB) or 8×H100 FP8 (~400GB). Running all 3 simultaneously: 10×H100 (INT4) to 18×H100 (FP8). Per-experiment: single-judge baselines across 15 attacks × 3 tasks × 3 models ≈ 450 H100-hrs; multi-judge protocol evaluation across 45 conditions on 10-GPU cluster ≈ 500 H100-hrs; signal independence measurement, copula fitting, and α estimation ≈ 100 H100-hrs; ablations (K=1,2,3,5,7 judges, homogeneous vs. heterogeneous) ≈ 200 H100-hrs; development/debugging ≈ 150 H100-hrs'}, 'human_in_loop': {'gpu_hours': '800-1,200 H100-equivalent', 'timeline': '10-14 weeks', 'claude_api_cost': '$400-$600 (Sonnet 4.6 for code generation, proof assistance, paper drafting; ~130-200M tokens)', 'estimated_gpu_cost': '$2,000-$3,000 at $2.50/hr H100 spot', 'gpu_breakdown': 'Same per-model requirements; efficiency gains from Claude-assisted theorem proving, experiment scheduling, and copula fitting, reducing wasted debugging runs by ~20%'}, 'auto_research': {'gpu_hours': '1,200-1,800 H100-equivalent', 'timeline': '6-9 weeks', 'claude_api_cost': '$1,200-$2,000 (Opus 4.7 for theorem proving, SDPI chain verification, experiment design; ~250-400M tokens)', 'estimated_gpu_cost': '$3,000-$4,500 at $2.50/hr H100 spot', 'speed_bottleneck': 'The three-pillar proof strategy (SDPI + Fano + copula) has well-defined mathematical components that autonomous systems can work on in parallel, but ensuring the chain composes correctly across the three pillars requires human mathematical judgment. The key risk is that the SDPI contraction yields a weaker-than-expected bound, requiring fallback to the √K variance-reduction argument.'}}\n\n## Inspired By\nThe convergence of seven lines of work: (1) Robertson & Koyejo's bounded f-divergence theory for single-evaluator manipulation resistance; (2) The dual peer prediction results—Qiu et al.'s BNE and Chen et al.'s dominant-strategy PEG—providing complementary incentive-compatibility guarantees; (3) Yang et al.'s information-theoretic diversity-scaling framework establishing the task-performance scaling law via effective channel count K*—we provide the adversarial dual; (4) Turkmen et al.'s Gaussian-copula model with its error floor theorem and MI decomposition, which provides the mathematical foundation from which we derive our closed-form K_eff; (5) Kaneko & Baldwin's tight single-model information-theoretic attack cost bounds (N_min ≥ log₂(1/ε)/I_max), which we extend to multi-judge composition; (6) The SoK's empirical finding that 7-model committees reduce ASR to 10–19% without formal explanation; (7) The behavioral entanglement and correlated error literature (Chen et al. 2604.07650, Kim et al. ICML 2025) providing quantitative inter-judge independence measurements. We unify these into a certifiable manipulation-resistance framework where the certified bound is an explicit function of measurable signal correlation.\n\n## Target Venues\n- AAAI 2027 Main Technical Track (abstract: July 21, 2026; full paper: July 28, 2026; primary target—theory + experiments with certified robustness framing)\n- USENIX Security 2027 Cycle 1 (abstract: August 18, 2026; full paper: August 25, 2026; security-focused version emphasizing certifiable robustness against realistic attacks)\n- NeurIPS 2026 Workshops (contributed papers: ~August 29, 2026; workshop version connecting to the diversity-scaling and certified robustness communities)\n- ICLR 2027 (estimated deadline: October 2026; polished archival version with extended theory, comprehensive experiments, and tightness analysis)\n\n## Key References\n- Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes (Robertson & Koyejo, arXiv 2508.05469, 2025) — foundational TVD-MI theory, Theorem 3.3 polynomial certification bounds, primary work we extend\n- Identity-Link IRT for Label-Free LLM Evaluation: Preserving Additivity in TVD-MI Scores (Robertson, arXiv 2510.14966, 2025) — sparse TVD-MI evaluation, two-judge preliminary validation\n- Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction (Qiu et al., ICLR 2026, 2601.20299) — BNE incentive-compatibility for LLM peer prediction, inverse scaling property\n- Incentivizing Truthful Language Models via Peer Elicitation Games (Chen et al., NeurIPS 2025, 2505.13636) — DMI-based multi-agent peer elicitation with dominant strategy truthfulness (Lemma 1), sublinear O(√T) regret bound (Theorem 2), last-iterate convergence to Nash equilibrium (Theorem 3) via online mirror descent; experiments use 3 discriminators (n≥2 required by Lemma 1)\n- Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity (Yang et al., ICLR 2026 Workshop AIMS, 2602.03794) — information-theoretic diversity-scaling framework: effective channel count K* = 2^{H(ρ)}, residual uncertainty (1-α_c)^{K*} geometric contraction (Theorem 4.3), heterogeneity advantage (Corollary 4.4); we provide the adversarial dual of their task-performance result\n- Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection (Turkmen et al., arXiv 2602.08003, 2026) — Gaussian-copula correlated error model (Z_j = √ρ·U + √(1-ρ)·ξ_j), information-theoretic error floor Φ(Φ⁻¹(1-p)/√ρ) (Theorem 4.4), three-term MI decomposition into accuracy-redundancy-error correlation (Theorem 4.3); copula model provides the mathematical foundation from which we derive our K_eff formula\n- Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs (Kaneko & Baldwin, NeurIPS 2025 spotlight, arXiv 2510.17000) — tight single-model attack cost bound N_min ≥ log₂(1/ε)/I_max via K-ary Fano inequality (Theorem 1), achieved by SPRT (Theorem 2); validated across 7 LLMs including Llama-4 and DeepSeek-R1; provides single-channel foundation that we extend to multi-judge composition\n- Robust LLM Performance Certification via Constrained Maximum Likelihood Estimation (Shen et al., arXiv 2604.03257, Google DeepMind/UCL, 2026) — constrained MLE fusing human labels, LLM-judge annotations, and domain constraints for certified performance estimation; addresses honest-judge noise, not adversarial manipulation; occupies adjacent 'certifiable evaluation' space\n- Noisy but Valid: Robust Statistical Evaluation of LLMs with Imperfect Judges (Feng, Shen, Balashankar, Gerner-Beuerle & Rodrigues, ICLR 2026, arXiv 2601.20913) — statistical hypothesis testing framework for LLM evaluation certification with finite-sample Type-I error control (Theorem 5.1) despite calibration uncertainty; variance-corrected thresholds using judge TPR/FPR estimation; assumes honest but fallible judges, not adversarial manipulation; complements Shen et al. in the 'certifiable evaluation' space\n- Logarithmic Scores, Power-Law Discoveries: Disentangling Measurement from Coverage in Agent-Based Evaluation (Jung & Na, arXiv 2604.00477, 2026) — score-coverage dissociation: scoring reliability scales logarithmically, discovery follows power law N^0.69; informs our analysis of when certified bounds saturate vs. empirical gains\n- Security in LLM-as-a-Judge: A Comprehensive SoK (arXiv 2603.29403, April 2026) — comprehensive vulnerability catalog, 50-68% ASR on open-source, 7-model committee reduces ASR to 10-19%; primary empirical evidence for diversity benefit without formal explanation\n- LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge (arXiv 2506.09443, 2025) — RobustJudge benchmark, 15 attacks, 7 defenses, 12 models\n- Correlated Errors in Large Language Models (Kim, Garg, Peng & Garg, ICML 2025, arXiv 2506.07962) — error correlation across 350+ LLMs: 60% agreement when both err (vs 33% baseline), same-company +0.066, same-architecture +0.076; KEY for α regime analysis\n- How Independent are Large Language Models? A Statistical Framework for Auditing Behavioral Entanglement (Chen et al., arXiv 2604.07650, 2026) — BEI and CIG metrics across 18 LLMs from 6 families; cross-family entanglement 40-60% lower than intra-family\n- Benchmark Illusion: Disagreement among LLMs and Its Scientific Consequences (arXiv 2602.11898, 2026) — 16-38% disagreement among top frontier models despite similar accuracy\n- Strong Data-Processing Inequalities for Channels and Bayesian Networks (Polyanskiy & Wu, arXiv 1508.06025, 2017) — SDPI contraction coefficients compose multiplicatively; foundational for our Pillar 1 proof strategy\n- Rethinking Fano's Inequality in Ensemble Learning (Morishita et al., ICML 2022, arXiv 2205.12683) — decomposes Fano bound for ensembles into relevance, redundancy, and combination loss; foundational for our Pillar 2 proof strategy\n- On the Certified Robustness for Ensemble Models and Beyond (Chen et al., arXiv 2107.10873, 2021) — diversified gradient + large confidence margin jointly necessary and sufficient for certified ensemble robustness\n- Boosting Randomized Smoothing with Variance Reduced Classifiers (Horvath et al., arXiv 2106.06946, 2021) — ensemble variance reduction yields √K-type certified radius improvement; precedent for polynomial scaling from diversity\n- Information-Theoretically Optimal Adversarial Attacks (Yi et al., arXiv 2007.14042, 2020) — proves attack cost scales up with number of redundant signal copies; direct precedent for manipulation cost scaling with K\n- On the Fragility of AI Agent Collusion (Keppo et al., arXiv 2603.20281, 2026) — increasing LLM count 2→5 breaks collusion (+22%→+3%); same-family size heterogeneity stabilizes via leader-follower; motivates cross-family diversity\n- CollabEval: Multi-Agent Collaborative Evaluation (arXiv 2603.00993, March 2026) — three-phase multi-agent evaluation without formal adversarial guarantees\n- An Adversary-Resistant Multi-Agent LLM System via Credibility Scoring (Ebrahimi et al., IJCNLP-AACL 2025, arXiv 2505.24239) — credibility-based iterative aggregation; game-theoretic but not information-theoretic\n- Certifying Joint Adversarial Robustness for Model Ensembles (Chiang et al., arXiv 2004.10250, 2020) — vulnerability space disjointness for ensemble certification\n- Peer Prediction with More Signals than Reports (Frongillo et al., arXiv 2503.16280, 2025) — fine-grained signals destabilize uninformative equilibria\n- Exploring and Mitigating Adversarial Manipulation of Voting-Based Leaderboards (ICML 2025)\n- Improving Your Model Ranking on Chatbot Arena by Vote Rigging (ICML 2025)\n- am-ELO: A Stable Framework for Arena-based LLM Evaluation (ICML 2025 Poster)\n- CAP: Improving the Robustness of LLM-as-a-Judge Against Adversarial Score Manipulation via Comparative Augmented Prompting (OpenReview 2026)\n- Aligned Textual Scoring Rules (Lu et al., arXiv 2507.06221, 2025)\n- Can You Trick the Grader? Adversarial Persuasion of LLM Judges (EMNLP 2025 Findings)\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-20T04:43:55.270Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T04:43:55.270Z",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---

## Round 1

45 recorded events

### User

_source line 3 · 2026-05-20T04:43:55.283Z_

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
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "a70c7847-3ea8-4489-8f0c-154a8fab9db9",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T04:43:55.281Z_

```json
{
  "parentUuid": "a70c7847-3ea8-4489-8f0c-154a8fab9db9",
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
  "uuid": "e1aed3d6-ef0e-4569-b7fa-ad6b55c7b572",
  "timestamp": "2026-05-20T04:43:55.281Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T04:43:55.281Z_

```json
{
  "parentUuid": "e1aed3d6-ef0e-4569-b7fa-ad6b55c7b572",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "76d22fea-c50d-4b12-91a8-6d3de858bd62",
  "timestamp": "2026-05-20T04:43:55.281Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
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
  "leafUuid": "76d22fea-c50d-4b12-91a8-6d3de858bd62",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable manipulation resistance for multi-judge LLM evaluation",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---

### Assistant

_source line 8 · 2026-05-20T04:44:00.605Z_

<details><summary>Logged reasoning block</summary>

```text
This is a complex proposal evaluation task. Let me carefully analyze this proposal for EMNLP 2026. Before I can give a proper assessment, I need to do the required web searches to understand the current landscape.

Let me first load the WebSearch tool, then conduct the required research.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76d22fea-c50d-4b12-91a8-6d3de858bd62",
  "isSidechain": false,
  "requestId": "req_011CbDD9BH366YkiDuZXsmcQ",
  "type": "assistant",
  "uuid": "c3185aaa-6de4-49af-9a97-568343945beb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GibkYDQCaopB6QvsjUp3Xh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11953,
      "cache_read_input_tokens": 14333,
      "output_tokens": 153,
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
          "output_tokens": 153,
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

_source line 9 · 2026-05-20T04:44:01.128Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01AjiP3ubyjXotRT1fd2QWfp`</summary>

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
  "parentUuid": "c3185aaa-6de4-49af-9a97-568343945beb",
  "isSidechain": false,
  "requestId": "req_011CbDD9BH366YkiDuZXsmcQ",
  "type": "assistant",
  "uuid": "666178a7-595d-4c20-9911-074ee5b71d52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GibkYDQCaopB6QvsjUp3Xh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11953,
      "cache_read_input_tokens": 14333,
      "output_tokens": 153,
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
          "output_tokens": 153,
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

_source line 10 · 2026-05-20T04:44:01.134Z_

<details><summary>↩ Tool result · `toolu_01AjiP3ubyjXotRT1fd2QWfp`</summary>

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
  "parentUuid": "666178a7-595d-4c20-9911-074ee5b71d52",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "369b09d3-a951-48a9-a609-335d75027f29",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "666178a7-595d-4c20-9911-074ee5b71d52",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-20T04:44:08.034Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required 3-5 targeted web searches to understand the landscape before evaluating this proposal. I need to search for:

1. Recent work on certified robustness for LLM-as-judge / LLM evaluation adversarial attacks
2. Multi-judge LLM evaluation manipulation resistance - information theoretic approaches
3. Key papers cited in the proposal (Robertson & Koyejo, Kaneko & Baldwin, etc.)
4. Yang et al. diversity scaling for multi-agent systems
5. SoK on LLM-as-judge security


Running these searches now.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "369b09d3-a951-48a9-a609-335d75027f29",
  "isSidechain": false,
  "requestId": "req_011CbDD9cXpvQvzKDND98z4w",
  "type": "assistant",
  "uuid": "21d0eeb2-d7cf-45f9-8bdd-8a6f85db54c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QH4AeqjZztv9DZfaS32Hbo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 26286,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 12 · 2026-05-20T04:44:08.342Z_

I'll now conduct the required pre-assessment research. Let me run multiple targeted searches in parallel to understand the current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "21d0eeb2-d7cf-45f9-8bdd-8a6f85db54c9",
  "isSidechain": false,
  "requestId": "req_011CbDD9cXpvQvzKDND98z4w",
  "type": "assistant",
  "uuid": "a5844aa0-8a61-4e1e-bde8-274f7a041072",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QH4AeqjZztv9DZfaS32Hbo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 26286,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 13 · 2026-05-20T04:44:08.881Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NJ9iiMz1CGReX8BDM5A8tA`</summary>

```json
{
  "query": "certified robustness LLM-as-judge adversarial manipulation multi-judge evaluation 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a5844aa0-8a61-4e1e-bde8-274f7a041072",
  "isSidechain": false,
  "requestId": "req_011CbDD9cXpvQvzKDND98z4w",
  "type": "assistant",
  "uuid": "536aba22-da5b-403a-98aa-1c9a9e6fa7b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QH4AeqjZztv9DZfaS32Hbo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 26286,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 14 · 2026-05-20T04:44:09.821Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PQDGnoGz4Dx1kJE8KoxTs3`</summary>

```json
{
  "query": "information-theoretic bounds adversarial attacks LLM evaluation multi-agent scaling 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "536aba22-da5b-403a-98aa-1c9a9e6fa7b5",
  "isSidechain": false,
  "requestId": "req_011CbDD9cXpvQvzKDND98z4w",
  "type": "assistant",
  "uuid": "4ca70b8f-7e15-45d1-945c-7208820a5bd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QH4AeqjZztv9DZfaS32Hbo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 26286,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 15 · 2026-05-20T04:44:10.878Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01A4LkmkNB2hqzodLyXPvoHa`</summary>

```json
{
  "query": "Kaneko Baldwin \"Bits Leaked per Query\" NeurIPS 2025 information-theoretic attack cost bounds"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4ca70b8f-7e15-45d1-945c-7208820a5bd3",
  "isSidechain": false,
  "requestId": "req_011CbDD9cXpvQvzKDND98z4w",
  "type": "assistant",
  "uuid": "264d5c76-9ef9-4b8e-81e8-51ca92ba7486",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QH4AeqjZztv9DZfaS32Hbo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 26286,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 16 · 2026-05-20T04:44:11.904Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HtoiUi4P1oQdZYCogozDas`</summary>

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
  "parentUuid": "264d5c76-9ef9-4b8e-81e8-51ca92ba7486",
  "isSidechain": false,
  "requestId": "req_011CbDD9cXpvQvzKDND98z4w",
  "type": "assistant",
  "uuid": "3f1ed416-669e-42ed-8e88-13150a764500",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QH4AeqjZztv9DZfaS32Hbo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 26286,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 17 · 2026-05-20T04:44:12.969Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01VSjgQ78SDx3piZPr8UxCKD`</summary>

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
  "parentUuid": "3f1ed416-669e-42ed-8e88-13150a764500",
  "isSidechain": false,
  "requestId": "req_011CbDD9cXpvQvzKDND98z4w",
  "type": "assistant",
  "uuid": "4c023d41-d889-4bb6-ab50-a85fd2d5a674",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01QH4AeqjZztv9DZfaS32Hbo",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 679,
      "cache_read_input_tokens": 26286,
      "output_tokens": 498,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 679,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 498,
          "cache_read_input_tokens": 26286,
          "cache_creation_input_tokens": 679,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 679
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

_source line 18 · 2026-05-20T04:44:15.237Z_

<details><summary>↩ Tool result · `toolu_01NJ9iiMz1CGReX8BDM5A8tA`</summary>

```text
Web search results for query: "certified robustness LLM-as-judge adversarial manipulation multi-judge evaluation 2025 2026"

Links: [{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"LLM-as-a-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"},{"title":"LLM-as-Judge Evaluation","url":"https://www.emergentmind.com/topics/llm-as-a-judge-evaluation"},{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"Benchmarking adversarial robustness to bias elicitation in large language models: scalable automated assessment with LLM-as-a-judge | Machine Learning | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s10994-025-06862-6"},{"title":"LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/html/2506.09443v1"},{"title":"[2506.09443] LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge","url":"https://arxiv.org/abs/2506.09443"}]

I found relevant research on certified robustness and adversarial manipulation of LLM-as-Judge systems. Here are the key findings:

## Overview

LLM-as-a-Judge systems, which are widely used for automated evaluation including red teaming and benchmarking, are susceptible to adversarial attacks that can manipulate evaluation outcomes, raising critical concerns about their robustness and trustworthiness.

## Vulnerabilities to Adversarial Manipulation

LLM-as-a-Judge systems are highly sensitive to adversarial attacks—including handcrafted injections and optimization-based manipulations such as Combined Attack and PAIR—destabilizing judge scoring even in production deployments. LLM-based judges can be easily manipulated by adversarial prompt modifications such as Combined Attack (escape characters, context ignoring, injected completions) or optimization-based attacks such as PAIR, which achieves high attack success rates.

## RobustJudge Framework

A fully automated and scalable framework called RobustJudge has been designed to systematically evaluate the robustness of LLM-as-a-Judge systems. RobustJudge benchmarks 15 attack methods and 7 defense strategies across 12 models spanning closed-source, open-source, fine-tuned, and reasoning-specialized architectures.

## Defense Mechanisms and Robustness Solutions

LLM-as-a-Judge systems remain vulnerable to Combined Attack and PAIR, while defense mechanisms such as Re-tokenization and LLM-based Detectors offer improved protection. Robustness is highly sensitive to the choice of prompt template, with minor changes in phrasing or structure able to swing vulnerability metrics and attack success rates.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "536aba22-da5b-403a-98aa-1c9a9e6fa7b5",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "ecefcc9b-b6e7-44e2-b821-f831a0904beb",
  "toolUseResult": {
    "query": "certified robustness LLM-as-judge adversarial manipulation multi-judge evaluation 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Af3dcKPjccbzbwuK1EhipX",
        "content": [
          {
            "title": "SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK",
            "url": "https://arxiv.org/pdf/2603.29403"
          },
          {
            "title": "LLM-as-a-Judge Evaluation",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-evaluations"
          },
          {
            "title": "LLM-as-Judge Evaluation",
            "url": "https://www.emergentmind.com/topics/llm-as-a-judge-evaluation"
          },
          {
            "title": "Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment",
            "url": "https://arxiv.org/pdf/2402.14016"
          },
          {
            "title": "Benchmarking adversarial robustness to bias elicitation in large language models: scalable automated assessment with LLM-as-a-judge | Machine Learning | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s10994-025-06862-6"
          },
          {
            "title": "LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge",
            "url": "https://arxiv.org/html/2506.09443v1"
          },
          {
            "title": "[2506.09443] LLMs Cannot Reliably Judge (Yet?): A Comprehensive Assessment on the Robustness of LLM-as-a-Judge",
            "url": "https://arxiv.org/abs/2506.09443"
          }
        ]
      },
      "I found relevant research on certified robustness and adversarial manipulation of LLM-as-Judge systems. Here are the key findings:\n\n## Overview\n\nLLM-as-a-Judge systems, which are widely used for automated evaluation including red teaming and benchmarking, are susceptible to adversarial attacks that can manipulate evaluation outcomes, raising critical concerns about their robustness and trustworthiness.\n\n## Vulnerabilities to Adversarial Manipulation\n\nLLM-as-a-Judge systems are highly sensitive to adversarial attacks—including handcrafted injections and optimization-based manipulations such as Combined Attack and PAIR—destabilizing judge scoring even in production deployments. LLM-based judges can be easily manipulated by adversarial prompt modifications such as Combined Attack (escape characters, context ignoring, injected completions) or optimization-based attacks such as PAIR, which achieves high attack success rates.\n\n## RobustJudge Framework\n\nA fully automated and scalable framework called RobustJudge has been designed to systematically evaluate the robustness of LLM-as-a-Judge systems. RobustJudge benchmarks 15 attack methods and 7 defense strategies across 12 models spanning closed-source, open-source, fine-tuned, and reasoning-specialized architectures.\n\n## Defense Mechanisms and Robustness Solutions\n\nLLM-as-a-Judge systems remain vulnerable to Combined Attack and PAIR, while defense mechanisms such as Re-tokenization and LLM-based Detectors offer improved protection. Robustness is highly sensitive to the choice of prompt template, with minor changes in phrasing or structure able to swing vulnerability metrics and attack success rates."
    ],
    "durationSeconds": 6.351221962999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "536aba22-da5b-403a-98aa-1c9a9e6fa7b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 19 · 2026-05-20T04:44:17.587Z_

<details><summary>↩ Tool result · `toolu_01PQDGnoGz4Dx1kJE8KoxTs3`</summary>

```text
Web search results for query: "information-theoretic bounds adversarial attacks LLM evaluation multi-agent scaling 2025 2026"

Links: [{"title":"Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems","url":"https://arxiv.org/html/2603.05520"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/pdf/2510.17000"},{"title":"Monitoring LLM-based Multi-Agent Systems Against Corruptions via Node Evaluation","url":"https://arxiv.org/html/2510.19420"},{"title":"More Agents Improve Math Problem Solving but Adversarial Robustness Gap Persists","url":"https://arxiv.org/html/2511.07112"},{"title":"Frontiers | Adversarial robustness of LLM-based multi-agent systems for engineering problems","url":"https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1784484/full"}]

I've completed the web search for your query. Here are the key findings on information-theoretic bounds, adversarial attacks on LLMs, LLM evaluation, and multi-agent scaling from 2025-2026:

## Information-Theoretic Bounds and Adversarial Attacks

An information-theoretic framework computes how much information can be safely disclosed, treating mutual information between observations and target properties as leaked bits per query, showing that achieving error requires at least log(1/ε)/I(Z;T) queries. Even a modest increase in disclosure can collapse attack costs from quadratic to logarithmic in terms of desired accuracy.

## Privacy in Multi-Agent LLM Systems

Privacy leakage induced by sequential composition of agent representations remains poorly understood, which is increasingly problematic as modern LLM deployments shift toward agentic architectures where intermediate representations are reused across multiple stages.

## Adversarial Attacks on Multi-Agent Systems

Attacks in multi-agent systems exhibit contagious characteristics, where by intercepting and manipulating the output of a specific LLM within the system, the malicious influence can propagate to adjacent LLMs, resulting in cascading compromised behavior.

## Multi-Agent Scaling and Robustness

Across experiments, there is a consistent, monotonic gain from increasing the number of collaborating agents. However, adversarial manipulation or misalignment at the level of a single agent can propagate through the collective, undermining both safety and task performance.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4ca70b8f-7e15-45d1-945c-7208820a5bd3",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "af93daef-c55b-4618-b674-5994e263bf79",
  "toolUseResult": {
    "query": "information-theoretic bounds adversarial attacks LLM evaluation multi-agent scaling 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01K7wEP73NxYiWFhERmqx9F9",
        "content": [
          {
            "title": "Information-Theoretic Privacy Control for Sequential Multi-Agent LLM Systems",
            "url": "https://arxiv.org/html/2603.05520"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/pdf/2510.17000"
          },
          {
            "title": "Monitoring LLM-based Multi-Agent Systems Against Corruptions via Node Evaluation",
            "url": "https://arxiv.org/html/2510.19420"
          },
          {
            "title": "More Agents Improve Math Problem Solving but Adversarial Robustness Gap Persists",
            "url": "https://arxiv.org/html/2511.07112"
          },
          {
            "title": "Frontiers | Adversarial robustness of LLM-based multi-agent systems for engineering problems",
            "url": "https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2026.1784484/full"
          }
        ]
      },
      "I've completed the web search for your query. Here are the key findings on information-theoretic bounds, adversarial attacks on LLMs, LLM evaluation, and multi-agent scaling from 2025-2026:\n\n## Information-Theoretic Bounds and Adversarial Attacks\n\nAn information-theoretic framework computes how much information can be safely disclosed, treating mutual information between observations and target properties as leaked bits per query, showing that achieving error requires at least log(1/ε)/I(Z;T) queries. Even a modest increase in disclosure can collapse attack costs from quadratic to logarithmic in terms of desired accuracy.\n\n## Privacy in Multi-Agent LLM Systems\n\nPrivacy leakage induced by sequential composition of agent representations remains poorly understood, which is increasingly problematic as modern LLM deployments shift toward agentic architectures where intermediate representations are reused across multiple stages.\n\n## Adversarial Attacks on Multi-Agent Systems\n\nAttacks in multi-agent systems exhibit contagious characteristics, where by intercepting and manipulating the output of a specific LLM within the system, the malicious influence can propagate to adjacent LLMs, resulting in cascading compromised behavior.\n\n## Multi-Agent Scaling and Robustness\n\nAcross experiments, there is a consistent, monotonic gain from increasing the number of collaborating agents. However, adversarial manipulation or misalignment at the level of a single agent can propagate through the collective, undermining both safety and task performance."
    ],
    "durationSeconds": 7.7624160889999985,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4ca70b8f-7e15-45d1-945c-7208820a5bd3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 20 · 2026-05-20T04:44:19.240Z_

<details><summary>↩ Tool result · `toolu_01HtoiUi4P1oQdZYCogozDas`</summary>

```text
Web search results for query: "Robertson Koyejo "Let's Measure Information Step-by-Step" TVD-MI LLM evaluation 2508.05469"

Links: [{"title":"[PDF] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Let's-Measure-Information-Step-by-Step:-LLM-Based-Robertson-Koyejo/824098ede34f59514ebc25a69c69c68d1e89b664"},{"title":"(PDF) Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://www.researchgate.net/publication/394397315_Let's_Measure_Information_Step-by-Step_LLM-Based_Evaluation_Beyond_Vibes"},{"title":"[2508.05469] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/abs/2508.05469"},{"title":"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/pdf/2508.05469"},{"title":"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes - Consensus","url":"https://consensus.app/papers/lets-measure-information-stepbystep-llmbased-evaluation-robertson-koyejo/d4e764d3a82a56c9a8a885ba75e29ce4/"},{"title":"Identity-Link IRT for Label-Free LLM Evaluation: Preserving Additivity in TVD-MI Scores","url":"https://arxiv.org/pdf/2510.14966"}]

Based on the search results, I found detailed information about this paper:

## Paper Overview

"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes" is by Zachary Robertson and Sanmi Koyejo from Stanford's Department of Computer Science. The paper was published on August 7, 2025.

## Main Research Focus

The paper studies evaluation of AI systems without ground truth by exploiting a link between strategic gaming and information loss. It analyzes which information-theoretic mechanisms resist adversarial manipulation, extending finite-sample bounds to show that bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially.

## TVD-MI Method

The paper's implementation uses TVD-MI (Total Variation Distance MI) with an LLM critic (GPT-4o-mini) to estimate bounded mutual information, where the critic evaluates whether two responses show evidence of addressing the same source material and outputs categorical judgments of whether the responses share a source.

## Key Results

Under adversarial attacks, TVD-MI maintains effectiveness (area under curve 0.70-0.77) while traditional judge queries are near chance (AUC ≈ 0.50), demonstrating that querying the same LLM for information relationships rather than quality judgments provides both theoretical and practical robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3f1ed416-669e-42ed-8e88-13150a764500",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "09c5101b-1fa7-46af-9743-bffb539178e2",
  "toolUseResult": {
    "query": "Robertson Koyejo \"Let's Measure Information Step-by-Step\" TVD-MI LLM evaluation 2508.05469",
    "results": [
      {
        "tool_use_id": "srvtoolu_013SnFC4j35uo7ZEqwozroD3",
        "content": [
          {
            "title": "[PDF] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/Let's-Measure-Information-Step-by-Step:-LLM-Based-Robertson-Koyejo/824098ede34f59514ebc25a69c69c68d1e89b664"
          },
          {
            "title": "(PDF) Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://www.researchgate.net/publication/394397315_Let's_Measure_Information_Step-by-Step_LLM-Based_Evaluation_Beyond_Vibes"
          },
          {
            "title": "[2508.05469] Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/abs/2508.05469"
          },
          {
            "title": "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/pdf/2508.05469"
          },
          {
            "title": "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes - Consensus",
            "url": "https://consensus.app/papers/lets-measure-information-stepbystep-llmbased-evaluation-robertson-koyejo/d4e764d3a82a56c9a8a885ba75e29ce4/"
          },
          {
            "title": "Identity-Link IRT for Label-Free LLM Evaluation: Preserving Additivity in TVD-MI Scores",
            "url": "https://arxiv.org/pdf/2510.14966"
          }
        ]
      },
      "Based on the search results, I found detailed information about this paper:\n\n## Paper Overview\n\n\"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes\" is by Zachary Robertson and Sanmi Koyejo from Stanford's Department of Computer Science. The paper was published on August 7, 2025.\n\n## Main Research Focus\n\nThe paper studies evaluation of AI systems without ground truth by exploiting a link between strategic gaming and information loss. It analyzes which information-theoretic mechanisms resist adversarial manipulation, extending finite-sample bounds to show that bounded f-divergences (e.g., total variation distance) maintain polynomial guarantees under attacks while unbounded measures (e.g., KL divergence) degrade exponentially.\n\n## TVD-MI Method\n\nThe paper's implementation uses TVD-MI (Total Variation Distance MI) with an LLM critic (GPT-4o-mini) to estimate bounded mutual information, where the critic evaluates whether two responses show evidence of addressing the same source material and outputs categorical judgments of whether the responses share a source.\n\n## Key Results\n\nUnder adversarial attacks, TVD-MI maintains effectiveness (area under curve 0.70-0.77) while traditional judge queries are near chance (AUC ≈ 0.50), demonstrating that querying the same LLM for information relationships rather than quality judgments provides both theoretical and practical robustness."
    ],
    "durationSeconds": 7.332953601999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3f1ed416-669e-42ed-8e88-13150a764500",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
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
  "leafUuid": "09c5101b-1fa7-46af-9743-bffb539178e2",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable manipulation resistance for multi-judge LLM evaluation",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---

### Tool result

_source line 23 · 2026-05-20T04:44:19.675Z_

<details><summary>↩ Tool result · `toolu_01A4LkmkNB2hqzodLyXPvoHa`</summary>

```text
Web search results for query: "Kaneko Baldwin "Bits Leaked per Query" NeurIPS 2025 information-theoretic attack cost bounds"

Links: [{"title":"How many queries does it take to break an AI? We put a number on it. - MBZUAI","url":"https://mbzuai.ac.ae/news/how-many-queries-does-it-take-to-break-an-ai-we-put-a-number-on-it/"},{"title":"[2510.17000] Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/abs/2510.17000"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/html/2510.17000v1"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs","url":"https://arxiv.org/pdf/2510.17000"},{"title":"Bits Leaked per Query: Information-Theoretic Bounds for Adversarial Attacks on LLMs | OpenReview","url":"https://openreview.net/forum?id=DwXX8c7xst"},{"title":"MBZUAI on X: \"This year, our NeurIPS papers share a simple ambition: to make AI that doesn’t just predict, but understands, imagines, and communicates. We looked at how models leak information (Bits Leaked per Query), how they learn cause and effect (CausalVerse), how their abilities evolve https://t.co/GJTBnxYtEd\" / X","url":"https://x.com/mbzuai/status/1995414451705758049"},{"title":"Investigating How Pre-training Data Leakage Affects Models’ Reproduction and Detection Capabilities - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1201/"}]

Based on the search results, here's the information about the Kaneko & Baldwin "Bits Leaked per Query" paper:

## Overview

This is a NeurIPS 2025 Spotlight paper from MBZUAI postdoc researcher Masahiro Kaneko and Tim Baldwin proposing to measure the bits leaked per query to predict the minimum number of queries an adversary needs.

## Core Framework

The paper frames adversarial attacks as attempts to infer a target property T (such as the binary flag triggering harmful responses or the degree information deleted by unlearning can be restored) through an observable signal Z that leaks information through response tokens, thinking process tokens, or logits.

## Key Information-Theoretic Bounds

The formula to calculate attack query complexity is: to drive the attack error rate down to ε, you need at least log(1/ε)/I queries, where I is the mutual information between what the model exposes and the attacker's target.

More specifically, if the observable signal carries almost no information about success, an attacker needs roughly 1/ε queries, but leaking even a small, fixed number of bits reduces the requirement to log(1/ε) queries.

## Evaluation and Impact

The study provides the first systematic, multi-model confirmation that the query cost of attacking an LLM falls in near-perfect inverse proportion to the information it leaks, giving auditors and defenders a bit-per-query yardstick for quantifying risk. The evaluation covers seven LLMs: GPT-4, DeepSeek-R1, three OLMo-2 variants, and two Llama-4 checkpoints.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "264d5c76-9ef9-4b8e-81e8-51ca92ba7486",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "f31342df-0343-40d0-b265-6b8a3d4503ab",
  "toolUseResult": {
    "query": "Kaneko Baldwin \"Bits Leaked per Query\" NeurIPS 2025 information-theoretic attack cost bounds",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N4mk5LeEQniiRvXr3LyyjC",
        "content": [
          {
            "title": "How many queries does it take to break an AI? We put a number on it. - MBZUAI",
            "url": "https://mbzuai.ac.ae/news/how-many-queries-does-it-take-to-break-an-ai-we-put-a-number-on-it/"
          },
          {
            "title": "[2510.17000] Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/abs/2510.17000"
          },
          {
            "title": "Bits Leaked per Query: Information-Theoretic Bounds on Adversarial Attacks against LLMs",
            "url": "https://arxiv.org/html/2510.17000v1"
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
            "title": "MBZUAI on X: \"This year, our NeurIPS papers share a simple ambition: to make AI that doesn’t just predict, but understands, imagines, and communicates. We looked at how models leak information (Bits Leaked per Query), how they learn cause and effect (CausalVerse), how their abilities evolve https://t.co/GJTBnxYtEd\" / X",
            "url": "https://x.com/mbzuai/status/1995414451705758049"
          },
          {
            "title": "Investigating How Pre-training Data Leakage Affects Models’ Reproduction and Detection Capabilities - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1201/"
          }
        ]
      },
      "Based on the search results, here's the information about the Kaneko & Baldwin \"Bits Leaked per Query\" paper:\n\n## Overview\n\nThis is a NeurIPS 2025 Spotlight paper from MBZUAI postdoc researcher Masahiro Kaneko and Tim Baldwin proposing to measure the bits leaked per query to predict the minimum number of queries an adversary needs.\n\n## Core Framework\n\nThe paper frames adversarial attacks as attempts to infer a target property T (such as the binary flag triggering harmful responses or the degree information deleted by unlearning can be restored) through an observable signal Z that leaks information through response tokens, thinking process tokens, or logits.\n\n## Key Information-Theoretic Bounds\n\nThe formula to calculate attack query complexity is: to drive the attack error rate down to ε, you need at least log(1/ε)/I queries, where I is the mutual information between what the model exposes and the attacker's target.\n\nMore specifically, if the observable signal carries almost no information about success, an attacker needs roughly 1/ε queries, but leaking even a small, fixed number of bits reduces the requirement to log(1/ε) queries.\n\n## Evaluation and Impact\n\nThe study provides the first systematic, multi-model confirmation that the query cost of attacking an LLM falls in near-perfect inverse proportion to the information it leaks, giving auditors and defenders a bit-per-query yardstick for quantifying risk. The evaluation covers seven LLMs: GPT-4, DeepSeek-R1, three OLMo-2 variants, and two Llama-4 checkpoints."
    ],
    "durationSeconds": 8.795310101000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "264d5c76-9ef9-4b8e-81e8-51ca92ba7486",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 24 · 2026-05-20T04:44:26.137Z_

<details><summary>↩ Tool result · `toolu_01VSjgQ78SDx3piZPr8UxCKD`</summary>

```text
Web search results for query: "Yang et al "Understanding Agent Scaling" diversity multi-agent ICLR 2026 2602.03794"

Links: [{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/pdf/2602.03794"},{"title":"Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity","url":"https://arxiv.org/html/2602.03794"},{"title":"Towards a Science of Scaling Agent Systems","url":"https://arxiv.org/html/2512.08296v1"},{"title":"Published as a conference paper at ICLR 2026 Workshop on MALGAI","url":"https://openreview.net/pdf?id=RLHUTcvsA9"},{"title":"Beyond Quantity: Trajectory Diversity Scaling for Code Agents","url":"https://arxiv.org/pdf/2602.03219"}]

I found the paper! Here's what I located:

**Title:** Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity

**Authors:** Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, and Shangding Gu

**ArXiv ID:** 2602.03794

**Key Findings:**

The paper finds that scaling performance by increasing the number of agents exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (e.g., different models, prompts, or tools) continues to yield substantial gains.

The authors present an information-theoretic framework showing that MAS performance is bounded by the intrinsic task uncertainty, not by agent count, and derive architecture-agnostic bounds demonstrating that improvements depend on how many effective channels the system accesses.

Empirically, they show that heterogeneous configurations consistently outperform homogeneous scaling: 2 diverse agents can match or exceed the performance of 16 homogeneous agents.

The paper is available at https://arxiv.org/pdf/2602.03794.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4c023d41-d889-4bb6-ab50-a85fd2d5a674",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "9bda5190-e447-46fb-be22-0b5c7cf5e087",
  "toolUseResult": {
    "query": "Yang et al \"Understanding Agent Scaling\" diversity multi-agent ICLR 2026 2602.03794",
    "results": [
      {
        "tool_use_id": "srvtoolu_01US7Zk7eKTWJkfV8XmuWj1X",
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
      "I found the paper! Here's what I located:\n\n**Title:** Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity\n\n**Authors:** Yingxuan Yang, Chengrui Qu, Muning Wen, Laixi Shi, Ying Wen, Weinan Zhang, Adam Wierman, and Shangding Gu\n\n**ArXiv ID:** 2602.03794\n\n**Key Findings:**\n\nThe paper finds that scaling performance by increasing the number of agents exhibits strong diminishing returns in homogeneous settings, while introducing heterogeneity (e.g., different models, prompts, or tools) continues to yield substantial gains.\n\nThe authors present an information-theoretic framework showing that MAS performance is bounded by the intrinsic task uncertainty, not by agent count, and derive architecture-agnostic bounds demonstrating that improvements depend on how many effective channels the system accesses.\n\nEmpirically, they show that heterogeneous configurations consistently outperform homogeneous scaling: 2 diverse agents can match or exceed the performance of 16 homogeneous agents.\n\nThe paper is available at https://arxiv.org/pdf/2602.03794."
    ],
    "durationSeconds": 13.164081377000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "4c023d41-d889-4bb6-ab50-a85fd2d5a674",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 25 · 2026-05-20T04:44:33.369Z_

<details><summary>Logged reasoning block</summary>

```text
Good, I have initial research results. Let me now search for a few more specific topics:

1. Turkmen et al. "Don't Always Pick the Highest-Performing Model" Gaussian copula ensemble
2. The SoK on LLM-as-judge security (2603.29403)
3. Chen et al. PEG peer elicitation games NeurIPS 2025
4. Any recent work on multi-judge manipulation cost scaling that might directly compete with this proposal
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9bda5190-e447-46fb-be22-0b5c7cf5e087",
  "isSidechain": false,
  "requestId": "req_011CbDDBT9aE4CLPvjnm58Hy",
  "type": "assistant",
  "uuid": "c05b48ab-de96-46b1-8ec7-3478082433d9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EEjqkwMGkNTiutVK6hAwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4258,
      "cache_read_input_tokens": 26965,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 388,
          "cache_read_input_tokens": 26965,
          "cache_creation_input_tokens": 4258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4258
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

_source line 26 · 2026-05-20T04:44:34.335Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013EyeGYjzJ2ZHnt9NjTdxvd`</summary>

```json
{
  "query": "Turkmen et al \"Don't Always Pick the Highest-Performing Model\" Gaussian copula ensemble LLM 2602.08003"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c05b48ab-de96-46b1-8ec7-3478082433d9",
  "isSidechain": false,
  "requestId": "req_011CbDDBT9aE4CLPvjnm58Hy",
  "type": "assistant",
  "uuid": "b6ecefc4-43c2-4d59-8890-f472562346e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EEjqkwMGkNTiutVK6hAwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4258,
      "cache_read_input_tokens": 26965,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 388,
          "cache_read_input_tokens": 26965,
          "cache_creation_input_tokens": 4258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4258
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

_source line 27 · 2026-05-20T04:44:34.817Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YJF1YvHDN2mG7n8kYDEhyh`</summary>

```json
{
  "query": "SoK LLM-as-judge security 2603.29403 seven model committee attack success rate 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b6ecefc4-43c2-4d59-8890-f472562346e3",
  "isSidechain": false,
  "requestId": "req_011CbDDBT9aE4CLPvjnm58Hy",
  "type": "assistant",
  "uuid": "38c3fadc-76df-4a56-be86-86e0985574b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EEjqkwMGkNTiutVK6hAwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4258,
      "cache_read_input_tokens": 26965,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 388,
          "cache_read_input_tokens": 26965,
          "cache_creation_input_tokens": 4258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4258
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

_source line 28 · 2026-05-20T04:44:35.895Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01DjcbmA9DjvP9SaPndV4L6L`</summary>

```json
{
  "query": "Chen et al \"Peer Elicitation Games\" DMI scoring dominant strategy truthfulness NeurIPS 2025 2505.13636"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38c3fadc-76df-4a56-be86-86e0985574b8",
  "isSidechain": false,
  "requestId": "req_011CbDDBT9aE4CLPvjnm58Hy",
  "type": "assistant",
  "uuid": "9c9d56e3-1bbe-4594-b8ef-2289f530b57d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EEjqkwMGkNTiutVK6hAwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4258,
      "cache_read_input_tokens": 26965,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 388,
          "cache_read_input_tokens": 26965,
          "cache_creation_input_tokens": 4258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4258
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

_source line 29 · 2026-05-20T04:44:36.470Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ER4MVCBkGxogDMDMg6LWNz`</summary>

```json
{
  "query": "multi-judge LLM evaluation formal manipulation cost scaling certified bounds information theory 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c9d56e3-1bbe-4594-b8ef-2289f530b57d",
  "isSidechain": false,
  "requestId": "req_011CbDDBT9aE4CLPvjnm58Hy",
  "type": "assistant",
  "uuid": "496ce892-369a-4d81-8aed-505dd094d0b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017EEjqkwMGkNTiutVK6hAwn",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 4258,
      "cache_read_input_tokens": 26965,
      "output_tokens": 388,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 4258,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 388,
          "cache_read_input_tokens": 26965,
          "cache_creation_input_tokens": 4258,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 4258
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

_source line 30 · 2026-05-20T04:44:40.749Z_

<details><summary>↩ Tool result · `toolu_013EyeGYjzJ2ZHnt9NjTdxvd`</summary>

```text
Web search results for query: "Turkmen et al "Don't Always Pick the Highest-Performing Model" Gaussian copula ensemble LLM 2602.08003"

Links: [{"title":"[2602.08003] Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/abs/2602.08003"},{"title":"Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/html/2602.08003v1"},{"title":"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection","url":"https://arxiv.org/pdf/2602.08003"},{"title":"LLM-Guided Ensemble Learning for Contextual Bandits with Copula and Gaussian Process Models","url":"https://www.mdpi.com/2227-7390/13/15/2523"},{"title":"LLM-Guided Ensemble Learning for Contextual Bandits with Copula and Gaussian Process Models - Experts@Minnesota","url":"https://experts.umn.edu/en/publications/llm-guided-ensemble-learning-for-contextual-bandits-with-copula-a-2/"}]

I found the paper you're looking for! Here's what the search revealed:

"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection" by Yigit Turkmen, Baturalp Buyukates, and Melih Bastopcu addresses the question of which models should be selected when forming an LLM ensemble by formulating budgeted ensemble selection as maximizing the mutual information between the true label and predictions of the selected models.

The paper models the correlated errors of the models using Gaussian-copula and shows an information-theoretic error floor for the performance of the ensemble. The authors propose a greedy mutual-information selection algorithm that estimates the required information terms directly from data and iteratively builds an ensemble under a query budget.

The approach is tested on MEDMCQA, MMLU, and IMDB movie reviews datasets, where the method consistently outperforms strong baselines under the same query budget.

The paper is available on arXiv as document 2602.08003 (published February 10, 2026).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b6ecefc4-43c2-4d59-8890-f472562346e3",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "4fb50485-0a84-4972-84a0-3528a6dd3185",
  "toolUseResult": {
    "query": "Turkmen et al \"Don't Always Pick the Highest-Performing Model\" Gaussian copula ensemble LLM 2602.08003",
    "results": [
      {
        "tool_use_id": "srvtoolu_01KybHnMyjsir2mpRXvCiwKc",
        "content": [
          {
            "title": "[2602.08003] Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/abs/2602.08003"
          },
          {
            "title": "Don’t Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/html/2602.08003v1"
          },
          {
            "title": "Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection",
            "url": "https://arxiv.org/pdf/2602.08003"
          },
          {
            "title": "LLM-Guided Ensemble Learning for Contextual Bandits with Copula and Gaussian Process Models",
            "url": "https://www.mdpi.com/2227-7390/13/15/2523"
          },
          {
            "title": "LLM-Guided Ensemble Learning for Contextual Bandits with Copula and Gaussian Process Models - Experts@Minnesota",
            "url": "https://experts.umn.edu/en/publications/llm-guided-ensemble-learning-for-contextual-bandits-with-copula-a-2/"
          }
        ]
      },
      "I found the paper you're looking for! Here's what the search revealed:\n\n\"Don't Always Pick the Highest-Performing Model: An Information Theoretic View of LLM Ensemble Selection\" by Yigit Turkmen, Baturalp Buyukates, and Melih Bastopcu addresses the question of which models should be selected when forming an LLM ensemble by formulating budgeted ensemble selection as maximizing the mutual information between the true label and predictions of the selected models.\n\nThe paper models the correlated errors of the models using Gaussian-copula and shows an information-theoretic error floor for the performance of the ensemble. The authors propose a greedy mutual-information selection algorithm that estimates the required information terms directly from data and iteratively builds an ensemble under a query budget.\n\nThe approach is tested on MEDMCQA, MMLU, and IMDB movie reviews datasets, where the method consistently outperforms strong baselines under the same query budget.\n\nThe paper is available on arXiv as document 2602.08003 (published February 10, 2026)."
    ],
    "durationSeconds": 6.410042238000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b6ecefc4-43c2-4d59-8890-f472562346e3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 31 · 2026-05-20T04:44:40.841Z_

<details><summary>↩ Tool result · `toolu_01YJF1YvHDN2mG7n8kYDEhyh`</summary>

```text
Web search results for query: "SoK LLM-as-judge security 2603.29403 seven model committee attack success rate 2026"

Links: [{"title":"[2603.29403] Security in LLM-as-a-Judge: A Comprehensive SoK","url":"https://arxiv.org/abs/2603.29403"},{"title":"SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK","url":"https://arxiv.org/pdf/2603.29403"},{"title":"Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment","url":"https://arxiv.org/pdf/2402.14016"},{"title":"BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge | OpenReview","url":"https://openreview.net/forum?id=eC2a2IndIt"},{"title":"Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks","url":"https://arxiv.org/pdf/2505.13348"},{"title":"BadJudge: Backdoor Vulnerabilities of LLM-as-a-Judge","url":"https://arxiv.org/pdf/2503.00596"}]

Based on the search results, I found relevant information about the paper you're inquiring about. This paper presents the first Systematization of Knowledge (SoK) focusing on the security aspects of LLM-as-a-Judge systems, analyzing 863 works and selecting 45 relevant studies published between 2020 and 2026.

Regarding the specific findings about the seven-model committee and attack success rates: Multi-model committees of seven architecturally diverse models reduced attack success rates to as low as 10-19%, making committee-based evaluation the strongest available mitigation strategy. In contrast, individual defenses were evaded 32-67% of the time.

The paper (arXiv 2603.29403) examines how LLM-based judges can become both targets of adversarial manipulation and instruments through which attacks are conducted, potentially compromising the trustworthiness of evaluation pipelines.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "38c3fadc-76df-4a56-be86-86e0985574b8",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "66c51e2a-a0b0-410d-a65e-0192915fa4e8",
  "toolUseResult": {
    "query": "SoK LLM-as-judge security 2603.29403 seven model committee attack success rate 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DfP3ySEZi8DYeANNxauLWx",
        "content": [
          {
            "title": "[2603.29403] Security in LLM-as-a-Judge: A Comprehensive SoK",
            "url": "https://arxiv.org/abs/2603.29403"
          },
          {
            "title": "SECURITY IN LLM-AS-A-JUDGE: A COMPREHENSIVE SOK",
            "url": "https://arxiv.org/pdf/2603.29403"
          },
          {
            "title": "Is LLM-as-a-Judge Robust? Investigating Universal Adversarial Attacks on   Zero-shot LLM Assessment",
            "url": "https://arxiv.org/pdf/2402.14016"
          },
          {
            "title": "BadJudge: Backdoor Vulnerabilities of LLM-As-A-Judge | OpenReview",
            "url": "https://openreview.net/forum?id=eC2a2IndIt"
          },
          {
            "title": "Investigating the Vulnerability of LLM-as-a-Judge Architectures to Prompt-Injection Attacks",
            "url": "https://arxiv.org/pdf/2505.13348"
          },
          {
            "title": "BadJudge: Backdoor Vulnerabilities of LLM-as-a-Judge",
            "url": "https://arxiv.org/pdf/2503.00596"
          }
        ]
      },
      "Based on the search results, I found relevant information about the paper you're inquiring about. This paper presents the first Systematization of Knowledge (SoK) focusing on the security aspects of LLM-as-a-Judge systems, analyzing 863 works and selecting 45 relevant studies published between 2020 and 2026.\n\nRegarding the specific findings about the seven-model committee and attack success rates: Multi-model committees of seven architecturally diverse models reduced attack success rates to as low as 10-19%, making committee-based evaluation the strongest available mitigation strategy. In contrast, individual defenses were evaded 32-67% of the time.\n\nThe paper (arXiv 2603.29403) examines how LLM-based judges can become both targets of adversarial manipulation and instruments through which attacks are conducted, potentially compromising the trustworthiness of evaluation pipelines."
    ],
    "durationSeconds": 6.0208385909999995,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "38c3fadc-76df-4a56-be86-86e0985574b8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 32 · 2026-05-20T04:44:42.988Z_

<details><summary>↩ Tool result · `toolu_01DjcbmA9DjvP9SaPndV4L6L`</summary>

```text
Web search results for query: "Chen et al "Peer Elicitation Games" DMI scoring dominant strategy truthfulness NeurIPS 2025 2505.13636"

Links: [{"title":"GitHub - toz015/neurips2025-repo: Code and experiments for a NeurIPS 2025 submission · GitHub","url":"https://github.com/toz015/neurips2025-repo"},{"title":"NeurIPS Poster Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://neurips.cc/virtual/2025/poster/119902"},{"title":"Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/html/2505.13636v2"},{"title":"[2505.13636] Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/abs/2505.13636"},{"title":"Game Theory Meets Large Language Models: A Systematic Survey with Taxonomy and New Frontiers","url":"https://arxiv.org/html/2502.09053v2"},{"title":"Incentivizing Truthful Language Models via Peer Elicitation Games","url":"https://arxiv.org/pdf/2505.13636"},{"title":"Computer Science and Game Theory May 2025","url":"https://www.arxiv.org/list/cs.GT/2025-05?skip=100&show=2000"},{"title":"NeurIPS 2025 Adopts a New 6-Point Review Scoring System: Simplified Scoring for Enhanced Consistency | CSPaper","url":"https://cspaper.org/topic/83/neurips-2025-adopts-a-new-6-point-review-scoring-system-simplified-scoring-for-enhanced-consistency"}]

Based on the search results, I found the paper you're looking for. Here's what I can tell you about it:

The paper is titled "Incentivizing Truthful Language Models via Peer Elicitation Games" by Chen, Baiting and Zhu, Tong and Han, Jiale and Li, Lexin and Li, Gang and Dai, Xiaowu, published as arXiv preprint arXiv:2505.13636 in 2025.

The work introduces Peer Elicitation Games (PEG), a training-free, game-theoretic framework for aligning LLMs through a peer elicitation mechanism involving a generator and multiple discriminators instantiated from distinct base models.

Regarding the key aspects you mentioned:

- **DMI Scoring**: Discriminators interact in a peer evaluation setting, where utilities are computed using a determinant-based mutual information score that provably incentivizes truthful reporting without requiring ground-truth labels.

- **Dominant Strategy Truthfulness**: The determinant-based mutual information score provably incentivizes truthful reporting without requiring ground-truth labels.

- **Theoretical Guarantees**: Each agent, via online learning, achieves sublinear regret in the sense their cumulative performance approaches that of the best fixed truthful strategy in hindsight.

The paper was presented as a poster at NeurIPS on Wednesday, December 3, 2025.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9c9d56e3-1bbe-4594-b8ef-2289f530b57d",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "b504a649-fc45-4dd2-82e9-82f0922eeab2",
  "toolUseResult": {
    "query": "Chen et al \"Peer Elicitation Games\" DMI scoring dominant strategy truthfulness NeurIPS 2025 2505.13636",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JJ5BWYtskRAwXYSR1ki2hi",
        "content": [
          {
            "title": "GitHub - toz015/neurips2025-repo: Code and experiments for a NeurIPS 2025 submission · GitHub",
            "url": "https://github.com/toz015/neurips2025-repo"
          },
          {
            "title": "NeurIPS Poster Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://neurips.cc/virtual/2025/poster/119902"
          },
          {
            "title": "Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://arxiv.org/html/2505.13636v2"
          },
          {
            "title": "[2505.13636] Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://arxiv.org/abs/2505.13636"
          },
          {
            "title": "Game Theory Meets Large Language Models: A Systematic Survey with Taxonomy and New Frontiers",
            "url": "https://arxiv.org/html/2502.09053v2"
          },
          {
            "title": "Incentivizing Truthful Language Models via Peer Elicitation Games",
            "url": "https://arxiv.org/pdf/2505.13636"
          },
          {
            "title": "Computer Science and Game Theory May 2025",
            "url": "https://www.arxiv.org/list/cs.GT/2025-05?skip=100&show=2000"
          },
          {
            "title": "NeurIPS 2025 Adopts a New 6-Point Review Scoring System: Simplified Scoring for Enhanced Consistency | CSPaper",
            "url": "https://cspaper.org/topic/83/neurips-2025-adopts-a-new-6-point-review-scoring-system-simplified-scoring-for-enhanced-consistency"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for. Here's what I can tell you about it:\n\nThe paper is titled \"Incentivizing Truthful Language Models via Peer Elicitation Games\" by Chen, Baiting and Zhu, Tong and Han, Jiale and Li, Lexin and Li, Gang and Dai, Xiaowu, published as arXiv preprint arXiv:2505.13636 in 2025.\n\nThe work introduces Peer Elicitation Games (PEG), a training-free, game-theoretic framework for aligning LLMs through a peer elicitation mechanism involving a generator and multiple discriminators instantiated from distinct base models.\n\nRegarding the key aspects you mentioned:\n\n- **DMI Scoring**: Discriminators interact in a peer evaluation setting, where utilities are computed using a determinant-based mutual information score that provably incentivizes truthful reporting without requiring ground-truth labels.\n\n- **Dominant Strategy Truthfulness**: The determinant-based mutual information score provably incentivizes truthful reporting without requiring ground-truth labels.\n\n- **Theoretical Guarantees**: Each agent, via online learning, achieves sublinear regret in the sense their cumulative performance approaches that of the best fixed truthful strategy in hindsight.\n\nThe paper was presented as a poster at NeurIPS on Wednesday, December 3, 2025."
    ],
    "durationSeconds": 7.0667806820000045,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9c9d56e3-1bbe-4594-b8ef-2289f530b57d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 33_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "b504a649-fc45-4dd2-82e9-82f0922eeab2",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---

### Runtime record

_source line 34_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable manipulation resistance for multi-judge LLM evaluation",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---

### Tool result

_source line 35 · 2026-05-20T04:44:43.870Z_

<details><summary>↩ Tool result · `toolu_01ER4MVCBkGxogDMDMg6LWNz`</summary>

```text
Web search results for query: "multi-judge LLM evaluation formal manipulation cost scaling certified bounds information theory 2026"

Links: [{"title":"Cer-Eval: Certifiable and Cost-Efficient Evaluation Framework for LLMs","url":"https://arxiv.org/pdf/2505.03814"},{"title":"LLM-as-Judge Best Practices in 2026: Calibration, Bias, and Cost","url":"https://futureagi.com/blog/llm-as-judge-best-practices-2026"},{"title":"Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes","url":"https://arxiv.org/pdf/2508.05469"},{"title":"Tuning LLM Judge Design Decisions for 1/1000 of the Cost","url":"https://arxiv.org/pdf/2501.17178"},{"title":"LLM-as-a-Judge Simply Explained: The Complete Guide to Run LLM Evals at Scale - Confident AI","url":"https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method"},{"title":"LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data","url":"https://labelyourdata.com/articles/llm-as-a-judge"},{"title":"Debate, Deliberate, Decide (D3): A Cost-Aware Adversarial Framework for Reliable and Interpretable LLM Evaluation","url":"https://arxiv.org/pdf/2410.04663"},{"title":"Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation","url":"https://arxiv.org/pdf/2601.14691"}]

I found several relevant research papers and articles on LLM evaluation with multi-judge approaches, cost scaling, and information-theoretic perspectives:

## Key Findings:

**Certifiable Evaluation Frameworks:**
Research on test sample complexity derives tight bounds on the number of test points needed for certifiable evaluation and develops partition-based algorithms that adaptively select test points to minimize evaluation cost. Such approaches can save 20% to 40% of test points while maintaining comparable estimation error and providing confidence guarantees.

**Information-Theoretic Approaches:**
Detecting strategic manipulation in AI systems reduces to a well-defined information-theoretic problem. Finite-sample robustness bounds for information-based mechanisms under adversarial attacks show that bounded measures retain polynomial guarantees whereas unbounded ones can degrade exponentially.

**Multi-Judge Frameworks:**
Multi-judge approaches using debate and deliberation achieve state-of-the-art agreement with human judgments while reducing biases through anonymization and role diversification, with cost-accuracy tradeoffs enabled by budgeted stopping.

**Vulnerability to Manipulation:**
Content-based manipulation strategies are more effective than style-based ones, and while prompting and scaling judge compute reduce susceptibility, they do not fully eliminate it, revealing a fundamental vulnerability in LLM-based evaluation.

The search results primarily feature papers from 2025-2026, addressing formal bounds, information theory, and cost-efficient evaluation of multi-judge LLM systems.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "496ce892-369a-4d81-8aed-505dd094d0b5",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "e2c2980b-e333-4632-9d5b-f251bbf58108",
  "toolUseResult": {
    "query": "multi-judge LLM evaluation formal manipulation cost scaling certified bounds information theory 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01U8YcW543yWTtKGMrXVw88w",
        "content": [
          {
            "title": "Cer-Eval: Certifiable and Cost-Efficient Evaluation Framework for LLMs",
            "url": "https://arxiv.org/pdf/2505.03814"
          },
          {
            "title": "LLM-as-Judge Best Practices in 2026: Calibration, Bias, and Cost",
            "url": "https://futureagi.com/blog/llm-as-judge-best-practices-2026"
          },
          {
            "title": "Let's Measure Information Step-by-Step: LLM-Based Evaluation Beyond Vibes",
            "url": "https://arxiv.org/pdf/2508.05469"
          },
          {
            "title": "Tuning LLM Judge Design Decisions for 1/1000 of the Cost",
            "url": "https://arxiv.org/pdf/2501.17178"
          },
          {
            "title": "LLM-as-a-Judge Simply Explained: The Complete Guide to Run LLM Evals at Scale - Confident AI",
            "url": "https://www.confident-ai.com/blog/why-llm-as-a-judge-is-the-best-llm-evaluation-method"
          },
          {
            "title": "LLM as a Judge: A 2026 Guide to Automated Model Assessment | Label Your Data",
            "url": "https://labelyourdata.com/articles/llm-as-a-judge"
          },
          {
            "title": "Debate, Deliberate, Decide (D3): A Cost-Aware Adversarial Framework for Reliable and Interpretable LLM Evaluation",
            "url": "https://arxiv.org/pdf/2410.04663"
          },
          {
            "title": "Gaming the Judge: Unfaithful Chain-of-Thought Can Undermine Agent Evaluation",
            "url": "https://arxiv.org/pdf/2601.14691"
          }
        ]
      },
      "I found several relevant research papers and articles on LLM evaluation with multi-judge approaches, cost scaling, and information-theoretic perspectives:\n\n## Key Findings:\n\n**Certifiable Evaluation Frameworks:**\nResearch on test sample complexity derives tight bounds on the number of test points needed for certifiable evaluation and develops partition-based algorithms that adaptively select test points to minimize evaluation cost. Such approaches can save 20% to 40% of test points while maintaining comparable estimation error and providing confidence guarantees.\n\n**Information-Theoretic Approaches:**\nDetecting strategic manipulation in AI systems reduces to a well-defined information-theoretic problem. Finite-sample robustness bounds for information-based mechanisms under adversarial attacks show that bounded measures retain polynomial guarantees whereas unbounded ones can degrade exponentially.\n\n**Multi-Judge Frameworks:**\nMulti-judge approaches using debate and deliberation achieve state-of-the-art agreement with human judgments while reducing biases through anonymization and role diversification, with cost-accuracy tradeoffs enabled by budgeted stopping.\n\n**Vulnerability to Manipulation:**\nContent-based manipulation strategies are more effective than style-based ones, and while prompting and scaling judge compute reduce susceptibility, they do not fully eliminate it, revealing a fundamental vulnerability in LLM-based evaluation.\n\nThe search results primarily feature papers from 2025-2026, addressing formal bounds, information theory, and cost-efficient evaluation of multi-judge LLM systems."
    ],
    "durationSeconds": 7.3969646629999986,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "496ce892-369a-4d81-8aed-505dd094d0b5",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 36 · 2026-05-20T04:44:43.874Z_

```json
{
  "parentUuid": "e2c2980b-e333-4632-9d5b-f251bbf58108",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "d6132b74-6abe-42d0-8cde-ffc86fc32a22",
  "timestamp": "2026-05-20T04:44:43.874Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 37 · 2026-05-20T04:44:48.893Z_

<details><summary>Logged reasoning block</summary>

```text
Let me do one more search to check if there's any existing work that directly provides multi-judge manipulation cost scaling bounds, which would undermine the novelty claim of this proposal.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d6132b74-6abe-42d0-8cde-ffc86fc32a22",
  "isSidechain": false,
  "requestId": "req_011CbDDCm29AtQMRQP3aERPo",
  "type": "assistant",
  "uuid": "73723733-e0bc-4435-b88c-be18c25be258",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcPWQFbZjmjR9oVq3prAXr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3274,
      "cache_read_input_tokens": 31223,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 31223,
          "cache_creation_input_tokens": 3274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3274
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

_source line 38 · 2026-05-20T04:44:50.333Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01KV5bczwhnzcxRXNAd18fTJ`</summary>

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
  "parentUuid": "73723733-e0bc-4435-b88c-be18c25be258",
  "isSidechain": false,
  "requestId": "req_011CbDDCm29AtQMRQP3aERPo",
  "type": "assistant",
  "uuid": "389d68e4-cd3f-4bbb-b000-4a3c152e0fef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcPWQFbZjmjR9oVq3prAXr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3274,
      "cache_read_input_tokens": 31223,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 31223,
          "cache_creation_input_tokens": 3274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3274
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

_source line 39 · 2026-05-20T04:44:50.998Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TEoeAN9gd9y2R2pCJcrpZc`</summary>

```json
{
  "query": "ensemble certified robustness sqrt K scaling randomized smoothing variance reduction adversarial 2021 2022"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "389d68e4-cd3f-4bbb-b000-4a3c152e0fef",
  "isSidechain": false,
  "requestId": "req_011CbDDCm29AtQMRQP3aERPo",
  "type": "assistant",
  "uuid": "3b775ba6-5ce3-4530-b805-447ddab7a68a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01GcPWQFbZjmjR9oVq3prAXr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 3274,
      "cache_read_input_tokens": 31223,
      "output_tokens": 193,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 3274,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 193,
          "cache_read_input_tokens": 31223,
          "cache_creation_input_tokens": 3274,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 3274
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

_source line 40 · 2026-05-20T04:44:57.052Z_

<details><summary>↩ Tool result · `toolu_01TEoeAN9gd9y2R2pCJcrpZc`</summary>

```text
Web search results for query: "ensemble certified robustness sqrt K scaling randomized smoothing variance reduction adversarial 2021 2022"

Links: [{"title":"Boosting Certified Robustness for Time Series Classification with Efficient Self-Ensemble","url":"https://arxiv.org/html/2409.02802"},{"title":"Multi-head ensemble of smoothed classifiers for certified robustness - ScienceDirect","url":"https://www.sciencedirect.com/science/article/abs/pii/S0893608025003053"},{"title":"Certified Robustness for Top-k Predictions against Adversarial   Perturbations via Randomized Smoothing","url":"https://arxiv.org/pdf/1912.09899"},{"title":"Boosting Randomized Smoothing with Variance Reduced Classifiers | SRI Lab","url":"https://www.sri.inf.ethz.ch/blog/smoothens"},{"title":"Certified Adversarial Robustness via Randomized Smoothing","url":"https://github.com/locuslab/smoothing"},{"title":"Double Sampling Randomized Smoothing","url":"https://arxiv.org/pdf/2206.07912"},{"title":"Adaptive Randomized Smoothing: Certified Adversarial Robustness for Multi-Step Defences","url":"https://arxiv.org/pdf/2406.10427"},{"title":"Multi-head Ensemble of Smoothed Classifiers for Certified Robustness","url":"https://arxiv.org/html/2211.10882"}]

Based on the search results, I found relevant information about ensemble certified robustness with randomized smoothing and variance reduction from 2021-2022:

## Key Findings

Horváth et al. (2021) show that the ensemble of multiple DNNs trained separately can reduce the predictive variance against Gaussian noises, leading to certified robustness improvements.

Ensembles are particularly suitable base models for constructing certifiably robust classifiers via Randomized Smoothing, with the key insight that the reduced variance of ensembles over the perturbations introduced in RS leads to significantly more consistent classifications for a given input. This, in turn, leads to substantially increased certifiable radii for samples close to the decision boundary. These results were published in an ICLR 2022 paper.

Variance reduction via ensembling multiple DNNs trained from different random seeds distinctively improves the performance for certified robustness.

The research demonstrates that ensemble approaches can provide improvements in certified robustness through variance reduction mechanisms when combined with randomized smoothing, particularly relevant for adversarial robustness guarantees in that time period.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3b775ba6-5ce3-4530-b805-447ddab7a68a",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "c10e2ca8-5a85-454c-8610-1d676711f09d",
  "toolUseResult": {
    "query": "ensemble certified robustness sqrt K scaling randomized smoothing variance reduction adversarial 2021 2022",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VpAgnrPfXGMo9JEvwXVcym",
        "content": [
          {
            "title": "Boosting Certified Robustness for Time Series Classification with Efficient Self-Ensemble",
            "url": "https://arxiv.org/html/2409.02802"
          },
          {
            "title": "Multi-head ensemble of smoothed classifiers for certified robustness - ScienceDirect",
            "url": "https://www.sciencedirect.com/science/article/abs/pii/S0893608025003053"
          },
          {
            "title": "Certified Robustness for Top-k Predictions against Adversarial   Perturbations via Randomized Smoothing",
            "url": "https://arxiv.org/pdf/1912.09899"
          },
          {
            "title": "Boosting Randomized Smoothing with Variance Reduced Classifiers | SRI Lab",
            "url": "https://www.sri.inf.ethz.ch/blog/smoothens"
          },
          {
            "title": "Certified Adversarial Robustness via Randomized Smoothing",
            "url": "https://github.com/locuslab/smoothing"
          },
          {
            "title": "Double Sampling Randomized Smoothing",
            "url": "https://arxiv.org/pdf/2206.07912"
          },
          {
            "title": "Adaptive Randomized Smoothing: Certified Adversarial Robustness for Multi-Step Defences",
            "url": "https://arxiv.org/pdf/2406.10427"
          },
          {
            "title": "Multi-head Ensemble of Smoothed Classifiers for Certified Robustness",
            "url": "https://arxiv.org/html/2211.10882"
          }
        ]
      },
      "Based on the search results, I found relevant information about ensemble certified robustness with randomized smoothing and variance reduction from 2021-2022:\n\n## Key Findings\n\nHorváth et al. (2021) show that the ensemble of multiple DNNs trained separately can reduce the predictive variance against Gaussian noises, leading to certified robustness improvements.\n\nEnsembles are particularly suitable base models for constructing certifiably robust classifiers via Randomized Smoothing, with the key insight that the reduced variance of ensembles over the perturbations introduced in RS leads to significantly more consistent classifications for a given input. This, in turn, leads to substantially increased certifiable radii for samples close to the decision boundary. These results were published in an ICLR 2022 paper.\n\nVariance reduction via ensembling multiple DNNs trained from different random seeds distinctively improves the performance for certified robustness.\n\nThe research demonstrates that ensemble approaches can provide improvements in certified robustness through variance reduction mechanisms when combined with randomized smoothing, particularly relevant for adversarial robustness guarantees in that time period."
    ],
    "durationSeconds": 6.050174017999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3b775ba6-5ce3-4530-b805-447ddab7a68a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool result

_source line 41 · 2026-05-20T04:45:02.896Z_

<details><summary>↩ Tool result · `toolu_01KV5bczwhnzcxRXNAd18fTJ`</summary>

```text
Web search results for query: "Qiu et al "Truthfulness Despite Weak Supervision" peer prediction LLM ICLR 2026 2601.20299"

Links: [{"title":"Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction","url":"https://arxiv.org/html/2601.20299"},{"title":"[2601.20299] Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction","url":"https://arxiv.org/abs/2601.20299"},{"title":"Published as a conference paper at ICLR 2026","url":"https://openreview.net/pdf/58f19dcd2f739eb3573b20a0bf8a70f7a08c30b8.pdf"},{"title":"Evaluating and Training LLMs Using Peer Prediction","url":"https://arxiv.org/pdf/2601.20299"},{"title":"Truthfulness Without Supervision: Model Evaluation Using Peer Prediction | OpenReview","url":"https://openreview.net/forum?id=EW62GvCzP9"},{"title":"Published as a conference paper at ICLR 2026 WHEN WEAK LLMS SPEAK","url":"https://openreview.net/pdf?id=ROioaZ45Yz"},{"title":"Published as a conference paper at ICLR 2026 PREDICTING LLM OUTPUT LENGTH VIA","url":"https://arxiv.org/pdf/2602.11812"},{"title":"Weakly supervised veracity classification with LLM-predicted credibility signals","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11845407/"}]

I found the paper you're looking for! Here's what I can tell you about it:

The paper "Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction" is authored by Tianyi Alex Qiu, Micah Carroll, and Cameron Allen from the Center for Human-Compatible Artificial Intelligence at UC Berkeley.

The work introduces the peer prediction method for model evaluation and post-training, which rewards honest and informative answers over deceptive and uninformative ones, using a metric based on mutual predictability and without requiring ground truth labels.

Key findings include:

- Training an 8B model with peer prediction-based reward recovers most of the drop in truthfulness due to prior malicious finetuning, even when the reward is produced by a 0.135B language model with no finetuning.

- The paper discovers an inverse scaling property in peer prediction, where resistance to deception is strengthened as the capability gap between the experts and participants widens, enabling reliable evaluation of strong models with weak supervision.

- The method demonstrates effectiveness and resistance to deception, with both theoretical guarantees and empirical validation on models with up to 405B parameters.

The paper (arxiv 2601.20299) was published as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "389d68e4-cd3f-4bbb-b000-4a3c152e0fef",
  "isSidechain": false,
  "promptId": "55eafad2-94a0-4eeb-809a-4bbee281015c",
  "type": "user",
  "uuid": "a731c129-a84b-436b-9ada-9966dc2c86f3",
  "toolUseResult": {
    "query": "Qiu et al \"Truthfulness Despite Weak Supervision\" peer prediction LLM ICLR 2026 2601.20299",
    "results": [
      {
        "tool_use_id": "srvtoolu_0138Zcj5K1XT9hT1tEoVTvPB",
        "content": [
          {
            "title": "Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction",
            "url": "https://arxiv.org/html/2601.20299"
          },
          {
            "title": "[2601.20299] Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction",
            "url": "https://arxiv.org/abs/2601.20299"
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
            "title": "Truthfulness Without Supervision: Model Evaluation Using Peer Prediction | OpenReview",
            "url": "https://openreview.net/forum?id=EW62GvCzP9"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 WHEN WEAK LLMS SPEAK",
            "url": "https://openreview.net/pdf?id=ROioaZ45Yz"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 PREDICTING LLM OUTPUT LENGTH VIA",
            "url": "https://arxiv.org/pdf/2602.11812"
          },
          {
            "title": "Weakly supervised veracity classification with LLM-predicted credibility signals",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11845407/"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I can tell you about it:\n\nThe paper \"Truthfulness Despite Weak Supervision: Evaluating and Training LLMs Using Peer Prediction\" is authored by Tianyi Alex Qiu, Micah Carroll, and Cameron Allen from the Center for Human-Compatible Artificial Intelligence at UC Berkeley.\n\nThe work introduces the peer prediction method for model evaluation and post-training, which rewards honest and informative answers over deceptive and uninformative ones, using a metric based on mutual predictability and without requiring ground truth labels.\n\nKey findings include:\n\n- Training an 8B model with peer prediction-based reward recovers most of the drop in truthfulness due to prior malicious finetuning, even when the reward is produced by a 0.135B language model with no finetuning.\n\n- The paper discovers an inverse scaling property in peer prediction, where resistance to deception is strengthened as the capability gap between the experts and participants widens, enabling reliable evaluation of strong models with weak supervision.\n\n- The method demonstrates effectiveness and resistance to deception, with both theoretical guarantees and empirical validation on models with up to 405B parameters.\n\nThe paper (arxiv 2601.20299) was published as a conference paper at ICLR 2026."
    ],
    "durationSeconds": 12.559487412999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "389d68e4-cd3f-4bbb-b000-4a3c152e0fef",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-20T04:46:23.192Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough research to evaluate this proposal. Let me synthesize my findings and provide the assessment.

## Summary of the proposal

The proposal aims to prove that adversarial manipulation cost in multi-judge LLM evaluation grows as Ω(K^{g(I_max)}) where g is a function of inter-judge signal correlation. It draws on several existing frameworks:
1. SDPI contraction composition (Polyanskiy & Wu)
2. Fano-ensemble decomposition (Morishita et al.)
3. Gaussian-copula closed form (adapting Turkmen et al.)


The claimed contribution is positioning this as the "adversarial dual" of Yang et al.'s task-performance scaling laws.

## Critical Analysis

The core tension here is whether the theoretical guarantees justify the added complexity over simple majority voting, which already achieves substantial improvements—reducing error rates from 50-68% down to 10-19% with just seven models. The proposal's strength lies in offering provable certifiability rather than empirical results, though the practical gains are modest at 2.6-3.7× for K=7 under their model. I'm also noticing a simpler alternative: applying randomized smoothing directly to evaluation outputs might sidestep much of this machinery entirely.

The proposal does acknowledge randomized smoothing's √K scaling but argues their framework adds value through correlation-aware bounds—accounting for judge dependencies where randomized smoothing assumes independence. That's a legitimate technical contribution, though I need to assess whether it's substantial enough.

Tracing the novelty landscape: Robertson & Koyejo handle single-evaluator manipulation resistance, Kaneko & Baldwin bound single-model attack costs, Yang et al. derive multi-agent scaling through effective channel capacity, and Turkmen et al. appear to address something related but the reference cuts off. The question is whether combining these insights into a multi-judge adversarial framework constitutes sufficient novelty or if it's primarily a straightforward extension. The core derivation follows fairly directly from standard tools — taking the equicorrelated copula model, computing effective rank via linear algebra, mapping correlation to mutual information, then applying the √K variance reduction scaling. While each step is competent composition of existing results, the individual pieces aren't deeply novel. What stands out is framing this as the adversarial dual of diversity scaling and the SDPI chain composition, which offers a nice conceptual angle connecting positive and negative scaling results.

The practical impact is more limited than the theory suggests — certified bounds yield 2.6-3.7× improvement for a 7-judge ensemble, but majority voting empirically achieves 4-5× ASR reduction. The main value proposition is certifiability rather than raw robustness, which matters less to practitioners who prioritize empirical performance over formal guarantees.

The related work section is exceptionally thorough, covering 25+ papers with clear differentiation and positioning. I'm noticing some potential issues with citation dates — several references show 2026 arXiv IDs that I should verify exist — and the proposal targets AAAI 2027 and ICLR 2027 rather than EMNLP 2026, though that doesn't affect my assessment of the core idea quality.

Now I'm examining the key assumptions underlying the approach. The framework relies on the equicorrelated Gaussian copula for its closed-form results, though the authors do provide a weaker general case when this doesn't hold. There's also an assumption that adversarial corruption propagates independently across judges, but in reality attacks like universal adversarial suffixes could fool multiple models in correlated ways. The SDPI contraction composition and the application of prior estimates for judge correlation coefficients both warrant scrutiny, as the interaction between correlation structure and adversarial perturbation could be more intricate than the model captures.

The most concerning assumption is the independence of corruption — if adversarial attacks exploit shared vulnerabilities across models (which the literature suggests they do), the actual cost of manipulation could scale far worse than the theoretical bounds predict.

On novelty, this is a solid application of existing tools like SDPI, Fano, and Gaussian copulas to an important problem, with a clever framing around the adversarial dual of diversity scaling. But the technical composition itself is fairly straightforward, so I'd rate the novelty as moderate. The significance is real given the importance of LLM evaluation security and the lack of formal guarantees, though the practical improvements are modest at 2.6-3.7× for K=7, which raises questions about the actual value proposition.

Looking at the probability rubric, the core finding feels intuitive to information-theoretic reviewers — that manipulation cost scales polynomially with effective independent judges is something most would have expected. The closed-form result is nice but not surprising, and the √K scaling doesn't push beyond what the field would naturally anticipate.

The strong execution and comprehensive framing are markers of quality work, but they shouldn't inflate my estimate of the underlying idea novelty. The real question is whether "multi-judge manipulation cost scales as Ω(K^{g(I_max)}) with correlation-dependent exponent" constitutes a sufficiently novel contribution, and I think it lands in the 25-32% range, probably around 28%.

The core insight—that correlation structure governs both task-performance scaling and adversarial manipulation cost—is elegant but somewhat intuitive given the existing literature, and the practical margins are modest enough that reviewers might see this as a solid theoretical result without breakthrough potential. The specificity of the mathematical claims cuts both ways — reviewers can rigorously verify the formulas, but if there are gaps or the experiments don't validate the predictions, the whole framework weakens considerably. Weighing the intuitive nature of the core result against the modest practical improvements over simple baselines, I'm settling on 25-33%, with a median of 28%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a731c129-a84b-436b-9ada-9966dc2c86f3",
  "isSidechain": false,
  "requestId": "req_011CbDDEAL8Hor4beiddHwYL",
  "type": "assistant",
  "uuid": "2022dcdb-62fd-4ae4-9ba5-7999c358a421",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wmcQdYZjgMzNWk1DYSZta",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 679,
      "cache_creation_input_tokens": 958,
      "cache_read_input_tokens": 34497,
      "output_tokens": 7449,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 958,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 679,
          "output_tokens": 7449,
          "cache_read_input_tokens": 34497,
          "cache_creation_input_tokens": 958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 958
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

_source line 43 · 2026-05-20T04:48:05.617Z_

Now I have sufficient research to provide a thorough evaluation. Let me compile my assessment.

---

```
【阶段】: Triage

【领域调研】:

1. **Robertson & Koyejo, "Let's Measure Information Step-by-Step" (arXiv 2508.05469, 2025, under TMLR review)**:
   确认存在。提出 TVD-MI 框架，证明 bounded f-divergences（如 TVD）在对抗攻击下保持多项式认证保证（Theorem 3.3），而 KL 等 unbounded measures 指数退化。在对抗攻击下 AUC 达 0.70-0.77。本 proposal 声称从 pairwise 扩展到 N-judge——准确。但 Robertson & Koyejo 本身只做了 single/pairwise evaluator 理论，没有 multi-judge composition theory。

2. **Kaneko & Baldwin, "Bits Leaked per Query" (NeurIPS 2025 Spotlight, arXiv 2510.17000)**:
   确认存在且为 NeurIPS 2025 Spotlight。建立单模型攻击成本下界 N_min ≥ log₂(1/ε)/I_max。在 7 个 LLM 上验证。proposal 声称将此结果扩展到多 judge composition——定位准确，Kaneko & Baldwin 确实未涉及多 judge 组合。

3. **Yang et al., "Understanding Agent Scaling in LLM-Based Multi-Agent Systems via Diversity" (ICLR 2026 Workshop AIMS, arXiv 2602.03794)**:
   确认存在。建立 information-theoretic diversity scaling 框架：有效通道数 K* = 2^{H(ρ)}，残余不确定性以 (1-α_c)^{K*} 几何衰减。但该工作仅分析任务性能（information recovery），不涉及对抗操纵成本——proposal 的 "adversarial dual" framing 是准确的。注意：这是 workshop paper，非主会论文。

4. **Turkmen et al., "Don't Always Pick the Highest-Performing Model" (arXiv 2602.08003, Feb 2026)**:
   确认存在。Gaussian copula 相关误差模型，信息论 error floor Φ(Φ⁻¹(1-p)/√ρ)，三项 MI 分解。within-family ρ~0.7-0.8，cross-family ρ~0.4-0.5。proposal 借用其 copula 模型推导 K_eff——合理。但注意该论文本身是做 ensemble selection，不涉及 adversarial robustness。

5. **Chen et al., "Incentivizing Truthful Language Models via Peer Elicitation Games" (NeurIPS 2025 Poster, arXiv 2505.13636)**:
   确认存在。DMI-based dominant strategy truthfulness（Lemma 1），O(√T) regret bound，需要 n≥2 discriminators 和条件独立性。proposal 正确指出 PEG 没有分析条件独立假设违反时的退化行为。

6. **Qiu et al., "Truthfulness Despite Weak Supervision" (ICLR 2026, arXiv 2601.20299)**:
   确认存在。Peer prediction for LLM evaluation/training，BNE guarantees，inverse scaling property。proposal 正确定位其与本工作的差异（BNE vs. adversarial robustness，无多项式成本界）。

7. **SoK on LLM-as-Judge Security (arXiv 2603.29403, April 2026)**:
   确认存在。分析 863 篇论文，7-model diverse committee 将 ASR 从 50-68% 降至 10-19%——但无形式化解释。这是本 proposal 要解决的核心 empirical gap。

8. **Horvath et al. (arXiv 2106.06946, ICLR 2022)**:
   Randomized smoothing ensemble 通过方差减少实现 √K 型 certified radius improvement。这是 proposal 中 g(0) = 1/2（独立 judge）的直接 precedent。

9. **直接竞争搜索**:
   未找到任何已发表工作提供 formal N-judge manipulation cost scaling bounds as a function of measurable inter-judge correlation。这一 gap 看上去是真实存在的。

- **调研总结**: LLM-as-judge 安全领域正在快速发展：单模型攻击成本界（Kaneko & Baldwin）、single-evaluator 信息论框架（Robertson & Koyejo）、peer prediction 激励兼容（Qiu et al., Chen et al.）、多 agent 性能 scaling（Yang et al.）、ensemble 相关性建模（Turkmen et al.）均已就位。但"多 judge 操纵成本的形式化 scaling law（作为可测相关性的函数）"这一特定组合确实尚无人做。proposal 定位于将这些独立工具组合为统一的 certified manipulation-resistance 框架。

---

【Trivial Alternative 检验】:

**存在显著的 trivial alternative 威胁。**

最直接的 trivial baseline 是 **simple majority voting**。SoK (2603.29403) 已经证实 7-model committee 将 ASR 从 50-68% 降至 10-19%（~4-5× empirical reduction），且零形式化——纯粹靠投票。proposal 的 certified bound 在 K=7、α=0.5 时给出 2.65× manipulation cost increase，在最乐观的 α=0.65 时给出 3.7×。

也就是说：**简单多数投票在实证上已经比 proposal 的 certified bound 提供了更大的防护**。proposal 对此的回应是"certifiability"——certified bounds 即使数值modest，但提供了对任意未来攻击的 provable guarantee，而多数投票没有形式保证。

这是一个合理的论点，但审稿人的直觉反应很可能是："certified bound 在数值上弱于无任何理论支持的 majority voting 经验结果，实际意义何在？" 这类似于 randomized smoothing 在 adversarial robustness 领域的处境——理论优雅但 certified radii 远小于 empirical robustness margins。

**增量价值在于**：(1) 形式化 certification——可量化每次 evaluation 的 manipulation-resistance guarantee；(2) correlation-aware bound——知道 when diversity helps and when it doesn't（而 majority voting 不知道）；(3) 对 judge 选择的指导——K_eff 公式可以指导如何组建最有效的 ensemble。但这些增量价值主要是理论性的，实际部署的吸引力有限。

---

【前提假设检验】:

核心 claim 的逻辑链中有几个未经验证的关键假设：

1. **Equicorrelated Gaussian copula 假设**：闭式结果依赖于 judge 信号遵循等相关 Gaussian copula。这是一个数学上方便但现实中可能不成立的假设。真实 judge 的相关结构可能是异质的（跨任务、跨 prompt 变化），且非 Gaussian 依赖结构（如 tail dependence）可能很重要。proposal 提供了更一般但更弱的结果（基于相关矩阵最小特征值），但核心narrative 和所有数值预测都基于 copula 假设。

2. **对抗扰动通过独立通道传播的假设**：SDPI 组合论证假设对抗者的扰动通过各个 judge "通道"传播。但实际上，adversarial attacks 往往利用 judge 模型的**共享脆弱性**——例如 universal adversarial suffixes 可以同时欺骗多个模型，因为它们共享训练数据和类似的 tokenization。在这种情况下，有效独立通道数可能远低于 K_eff 预测。**这是最关键的未验证假设。**

3. **先代模型的 ρ 估计适用于当代模型**：proposal 用 Turkmen et al.（2602.08003）的 cross-family ρ~0.4-0.5 和 Kim et al.（ICML 2025）的 350+ 模型相关性数据来估计 α。但这些数据来自较早一代模型。DeepSeek-V4、Qwen-3.5、Llama-4-Maverick 可能因为共享更多合成训练数据而更相关。proposal 承认了这一风险但没有提供缓解方案。

4. **从 MI bound 到操纵成本的连接**：通过 Marton's inequality（TV² ≤ ½·KL）连接信息论 bound 到操作性操纵成本。这一步虽然数学上有效，但可能很松——Marton bound 通常不紧，导致 certified bound 过于保守。

---

【3 维度打分】:

1. **Novelty: 中** —
   proposal 所声称的 gap 确实存在：调研确认没有任何已发表工作提供 formal N-judge manipulation cost scaling as a function of measurable correlation。这是真实的 novelty delta。
   
   然而，技术层面的 novelty 较为有限。核心推导是将已有数学工具进行组合：(a) Turkmen et al. 的 Gaussian copula → K_eff 公式（本质上是等相关矩阵的有效秩，这是教科书级线性代数）；(b) Horvath et al. 的 √K 方差减少 → g(0)=1/2 的 boundary condition；(c) SDPI 的乘法组合（Polyanskiy & Wu 2017 的直接应用）。每一步都是现有工具的 standard application，组合本身不需要深刻的新洞察。
   
   "adversarial dual of diversity scaling" 的概念框架是优雅的，但对于 information-theory literate 的审稿人来说，这个 duality 是相当自然的——同一个通道的容量（capacity）既决定了信息恢复速率，也决定了扰动成本。
   
   Qualitative result（"更多样化的 judge = 更难操纵，且关系由相关性决定"）是直觉上显而易见的。Quantitative closed form 是有用的，但不 surprising。

2. **Significance: 中** —
   问题的重要性毋庸置疑：LLM evaluation 安全是热门且重要的方向，SoK 的发现（50-68% ASR）凸显了紧迫性。形式化保证的缺失也是被广泛认可的 gap。
   
   然而，practical significance 受限于两个因素：
   - Certified bounds 数值上弱于 empirical majority voting（2.65× vs. ~4-5× ASR reduction）——这降低了实际部署的吸引力
   - 结果高度依赖 distributional assumptions（equicorrelated Gaussian copula），限制了可推广性
   
   对领域的影响路径也需审慎评估。如果结果 positive，审稿人大概率会说 "I would have guessed that manipulation cost scales polynomially with effective independent judge count"——定性结论是直觉预期的。定量贡献（K_eff 的闭式表达式）有用但不改变人们对问题的根本理解。
   
   与之对比，Kaneko & Baldwin 的 single-model bound 之所以获得 NeurIPS spotlight，部分原因是它量化了一个之前完全未知的量（per-query information leakage across disclosure regimes），且揭示了 "few bits leak can collapse attack cost from quadratic to logarithmic" 这一 surprising 的 threshold 效应。本 proposal 的 multi-judge composition 没有类似的 surprising threshold 或 phase transition。

3. **Related Work: 强** —
   Related work 覆盖是本 proposal 最强的维度。25+ 篇论文的引用，每一篇的定位和差异化都清晰且准确（调研验证了所有关键论文的存在性和描述准确性）。proposal 不仅引用了直接竞争者，还覆盖了 adjacent areas（peer prediction、ensemble robustness、behavioral entanglement、collusion fragility 等），展示了对整个研究生态的深入理解。
   
   gap 的识别是精准的：Robertson & Koyejo 做 single-evaluator 理论、Kaneko & Baldwin 做 single-model 攻击界、Yang et al. 做任务性能 scaling、Turkmen et al. 做 ensemble selection——没有人做 multi-judge manipulation cost scaling as f(correlation)。
   
   唯一的minor weakness：部分引用是 workshop papers（Yang et al. ICLR 2026 Workshop AIMS）或预印本，在正式审稿时可能需要注意措辞。

---

【概率估计】: [22% - 32%] 中位 27%

【估计理由】:
- **Related Work 强**（+）：gap 识别精准，定位清晰，无遗漏的直接竞争者
- **Novelty 中**（限制上界）：技术贡献主要是现有工具的标准组合（copula 有效秩 + SDPI 组合 + √K 方差减少），缺少需要深刻新洞察的步骤。"Adversarial dual" 框架优雅但对信息论专家来说是自然的
- **Significance 中**（限制上界）：定性结果直觉上可预期（"更多样 = 更难操纵"）；certified bound 数值上弱于 empirical majority voting；无 surprising threshold effect
- 上界主要被 **Novelty** 和 **Significance** 共同限制：核心发现如果 positive，审稿人很可能说 "I would have guessed this" 而非 "surprising"
- 下界受益于 gap 的真实性和 framing 的完整性——这不是一个 flawed idea，而是一个 solid but incremental 的理论贡献

【主要风险】:
1. **"I would have guessed this" 风险**：核心定性结论（多样 judge 的操纵成本多项式增长，指数取决于相关性）是直觉上可预期的。审稿人可能认为 formal proof 虽然正确但 incremental，特别是当每一步都是现有工具的标准应用时。这是最可能导致 reject 的 idea-level 风险。
2. **Trivial alternative 被动性**：certified bound（K=7 时 2.65-3.7×）在数值上弱于 naive majority voting 的经验结果（~4-5× ASR reduction），审稿人可能认为 "certifiability" 的价值不足以弥补数值差距——特别是在 NLP/CL 社区（相比理论 CS 社区），empirical results 通常比 formal guarantees 更受重视。
```

Sources:
- [Security in LLM-as-a-Judge: A Comprehensive SoK](https://arxiv.org/abs/2603.29403)
- [LLMs Cannot Reliably Judge (Yet?) - RobustJudge](https://arxiv.org/abs/2506.09443)
- [Bits Leaked per Query - Kaneko & Baldwin](https://arxiv.org/abs/2510.17000)
- [Let's Measure Information Step-by-Step - Robertson & Koyejo](https://arxiv.org/abs/2508.05469)
- [Understanding Agent Scaling via Diversity - Yang et al.](https://arxiv.org/abs/2602.03794)
- [Don't Always Pick the Highest-Performing Model - Turkmen et al.](https://arxiv.org/abs/2602.08003)
- [Incentivizing Truthful Language Models via Peer Elicitation Games - Chen et al.](https://arxiv.org/abs/2505.13636)
- [Truthfulness Despite Weak Supervision - Qiu et al.](https://arxiv.org/abs/2601.20299)
- [Boosting Randomized Smoothing with Variance Reduced Classifiers - Horvath et al.](https://www.sri.inf.ethz.ch/blog/smoothens)
- [MBZUAI - How many queries to break an AI?](https://mbzuai.ac.ae/news/how-many-queries-does-it-take-to-break-an-ai-we-put-a-number-on-it/)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2022dcdb-62fd-4ae4-9ba5-7999c358a421",
  "isSidechain": false,
  "requestId": "req_011CbDDEAL8Hor4beiddHwYL",
  "type": "assistant",
  "uuid": "1095499e-8572-41ed-aef7-ebb7bd5bdc60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu/idea_review",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016wmcQdYZjgMzNWk1DYSZta",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 679,
      "cache_creation_input_tokens": 958,
      "cache_read_input_tokens": 34497,
      "output_tokens": 7449,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 958,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 679,
          "output_tokens": 7449,
          "cache_read_input_tokens": 34497,
          "cache_creation_input_tokens": 958,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 958
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

_source line 44_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "1095499e-8572-41ed-aef7-ebb7bd5bdc60",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable manipulation resistance for multi-judge LLM evaluation",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---

### Runtime record

_source line 46_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # Certifiable Manipulation Resistance for Multi-Judge LLM Evaluation: Information-Theoretic Bounds via Signal Corr…",
  "leafUuid": "1095499e-8572-41ed-aef7-ebb7bd5bdc60",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---

### Runtime record

_source line 47_

```json
{
  "type": "ai-title",
  "aiTitle": "Certifiable manipulation resistance for multi-judge LLM evaluation",
  "sessionId": "6d02cf48-9e78-46e7-b465-97583625cdc6"
}
```

---
