# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # CRADE: Joint Contamination-Abilit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 54
- **Recorded user turns:** 1
- **Tool calls:** 14
- **Original source:** `logs/chats/exported-trajectories/account-1/dbc09836-8363-423e-8f39-5a36a2157b70.jsonl`
- **Structured JSON:** [`e56864d783468c2c3b26.json`](../../sessions/e5/e56864d783468c2c3b26.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T14:03:21.814Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T14:03:21.814Z",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items\n\n## Core Problem\n\nNo existing framework can determine whether a model fails adversarial benchmark variants because it memorized original answers (contamination) or because it lacks genuine reasoning ability (capability deficit) — all current work observes this entanglement but none models it within a measurement-theoretic framework, preventing trustworthy LLM capability assessment.\n\n## Research Opportunity\n\nThree previously siloed research streams — IRT-based LLM evaluation (PSN-IRT AAAI 2026 Oral, ATLAS, LEGO-IRT), contamination detection/correction (DCR EMNLP 2025, ConStat NeurIPS 2024, JECS arXiv May 2026), and adversarial robustness testing (MaSTer, RIDE, MATH-Perturb ICML 2025) — have each matured independently to the point where their integration is both technically feasible and urgently needed. The critical catalyst is Wang et al.'s ICLR 2026 proof that all likelihood-based contamination detection fails on reasoning models (AUROC ≈ 50%), creating demand for response-pattern-based alternatives that bypass token-probability signals entirely. A key theoretical precedent exists but has never been applied to LLMs: the Deterministic Gated IRT model (DGM; Shu, Henson & Luecht, Psychometrika 2013) decomposes test performance into genuine ability and cheating/preknowledge components conditioned on item exposure status — precisely the structure needed for LLM contamination. PSN-IRT showed IRT works for LLMs (12 models, 41,871 items, 4PL) but left contamination-adjusted scoring as an explicit open question, flagging anomalous guessing-rate parameters as contamination indicators without providing corrected ability estimates. RankLLM (ICLR 2026) demonstrated that non-parametric difficulty-aware ranking achieves 90% human alignment with only a damping hyperparameter — but provides no contamination decomposition, producing rankings without interpretable ability vs. memorization parameters. A crucial practical enabler has emerged: the Open LLM Leaderboard V1 provides per-item binary response data for 2,000+ models across standard benchmarks including GSM8K (1,359 items), accessible via per-model details datasets (Polo et al., ICML 2024). Combined with Growing Pains' (arXiv April 2026) demonstration that two-stage fixed-parameter calibration achieves <2% error with 100 anchor items and ρ ≥ 0.9 ranking stability, this large-N calibration data resolves the fundamental feasibility concern of fitting IRT-based models with only 15-20 LLMs — by fixing well-calibrated item parameters from Stage 1, Stage 2 estimation reduces to person-level and contamination parameters only. The AAAI 2027 deadline (abstracts July 21, papers July 28, 2026) is 8 weeks out. Nobody sits at the three-way intersection of IRT estimation, contamination correction, and adversarial pairing because these communities publish at different venues (ACL/EMNLP for contamination, ICLR/NeurIPS for robustness, AAAI for psychometric evaluation, Psychometrika/JEBS for test security).\n\n## Research Landscape\n\nThe current best contamination-to-correction pipeline is DCR (EMNLP 2025), which produces a DCR Factor via fuzzy inference across four contamination levels, achieving ~4% average error on three benchmarks — but its ad-hoc multiplicative correction Acc_adj = Acc × (1 − DCR Factor) has no measurement-theoretic justification and empirically weakens on hard tasks (r=0.66). PSN-IRT (AAAI 2026 Oral) demonstrates IRT's power for LLM evaluation using a 4PL model across 12 LLMs on 11 benchmarks (41,871 items), flagging contamination indirectly via anomalous guessing-rate parameters, but produces no contamination-adjusted ability scores; critically, PSN-IRT succeeds with 12 models by using neural network estimation (pseudo-Siamese architecture) rather than classical MLE, establishing that neural IRT estimation is viable at small model counts. RankLLM (ICLR 2026) provides a strong non-parametric baseline: bidirectional score propagation between models and questions achieves 90% human alignment on 30 models × 35,550 questions, with remarkable stability under model removal (ρ = 0.94 even with 50% pool removed) and 0.006s convergence — but it produces difficulty-weighted rankings without any contamination modeling. RIDE (arXiv 2025) combines IRT with adversarial perturbation for math evaluation — but uses IRT only as a difficulty reward signal for RL-based question rewriting via RIDE-8B, not for joint ability-contamination estimation. JECS (arXiv May 2026) achieves formal conformal guarantees for multi-model decontamination via joint envelope conformal selection, but wastes information by binarizing items into keep/discard rather than producing continuous corrected scores. ConStat (NeurIPS 2024) detects contamination via performance gaps on rephrased samples using a statistical comparison against reference models, but does not model it as a latent variable within a psychometric framework. In psychometrics, the DGM (Shu et al., Psychometrika 2013) uses a gated IRT formulation estimated via hierarchical MCMC to decompose examinee performance into genuine ability and item-preknowledge components — but assumes item exposure status is known a priori, which is unavailable for LLM training data, and was validated only at operational testing sample sizes (hundreds of examinees). Two paired-item approaches exist but use no IRT: PaCoST (arXiv 2024) performs paired confidence significance testing for binary contamination detection, and ConStat compares primary vs. reference benchmark performance — both confirm the paired-item signal is informative but neither models it as a latent variable. For adversarial variant generation, MaSTer (arXiv 2026) provides a validated multi-round rewrite-verify pipeline (5 parallel streams × 3 iterations) achieving 45-94% target failure rates on GSM8K and MATH-500 using Qwen2.5-32B-Instruct for both rewriting and LLM-based verification (98% precision); code is claimed at github.com/sustech-nlp/MaSTer but was unavailable as of May 2026 — backup pipelines exist via MathCheck (ICLR 2025, open code) and MATH-Perturb (ICML 2025, 279 expert-crafted perturbations with open code). Growing Pains (arXiv April 2026) demonstrates two-stage fixed-parameter calibration for extensible LLM evaluation: calibrating MIRT 2PL item parameters on 295+ reference models, then scoring new models via fixed anchor items, achieving <2% MAE and ρ ≥ 0.9 with 100 anchor items per benchmark — directly applicable to our setting where item parameters are calibrated on large-N leaderboard data and contamination parameters estimated on a smaller model pool. Konig et al. (Behavior Research Methods 2023) demonstrate that hierarchical Bayesian 2PL (OH2PL) with half-Cauchy hyperpriors produces unbiased item parameter estimates down to N=50, while standard MML shows 75-89% inadmissible solutions at that sample size — establishing that Bayesian estimation is the correct choice for small-N IRT. Fox (JEBS 2025) pushes further: IRT-BCSM integrates out person parameters for stable estimation at N=50-100, with RMSE of 0.110 for discrimination at N=50 while standard 2PL/MML collapses (RMSE=1.782). MathArena (NeurIPS 2025 D&B Track) has expanded to ~900 problems across 2025-2026 competitions (AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, Apex) with 50+ models, providing rich uncontaminated ground-truth rankings. Concurrent work search (arXiv, OpenReview, May 2026): no paper attempts joint IRT-based contamination-ability decomposition with paired adversarial items or two-stage fixed-parameter calibration for contamination-aware scoring — the intersection remains unoccupied.\n\n## Proposed Approach\n\nWe extend the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from the test-security domain to LLM contamination assessment, introducing the Gated-2PL (G-2PL) model as the primary framework where correct-response probability decomposes into ability-driven and contamination-driven components via a gating mechanism. The key innovations over DGM are: (1) item exposure status is not assumed known but is identified from paired adversarial items, and (2) a two-stage fixed-parameter calibration architecture leverages large-N leaderboard data to resolve the small-sample estimation challenge.\n\n**Two-stage fixed-parameter calibration architecture (central methodological contribution):**\n\nStage 1 — Item parameter calibration (large-N, standard 2PL):\n- Assemble per-item binary response matrix from Open LLM Leaderboard V1 per-model details datasets for GSM8K (N_cal ≈ 2,000+ models × 1,359 items). Per-item data resides in individual per-model datasets under huggingface.co/open-llm-leaderboard-old (naming pattern: details_{org}__{model}), reconstructible following Polo et al. (ICML 2024, tinyBenchmarks). Each dataset contains per-task configurations (e.g., harness_gsm8k) with item-level correctness indicators.\n- Fit standard 2PL via marginal maximum likelihood (MML): estimate â_i (discrimination) and b̂_i (difficulty) for each GSM8K item. With N_cal ≈ 2,000+, these estimates are highly stable — Growing Pains demonstrates <2% MAE and ρ ≥ 0.9 with as few as 100 reference models on similar data.\n- Validate calibration quality: item-fit statistics (S-X², item-total correlations), dimensionality assessment (eigenvalue ratios from the item correlation matrix), and comparison with Growing Pains' calibrated parameters if available.\n- For MATH-500 (secondary benchmark): Stage 1 calibration assembled from (a) V2 leaderboard MATH Level 5 per-model details for the ~100 Level 5 items in MATH-500 (hundreds of models available via gated datasets at huggingface.co/datasets/open-llm-leaderboard/{org}__{model}-details), (b) publicly available per-item MATH-500 evaluation results from major papers and evaluation frameworks (lm-evaluation-harness), and (c) targeted evaluation of ~50-100 small open-weight models (7B-13B) from V1 leaderboard checkpoints on MATH-500 (~15 H100-hrs). Expected N_cal for MATH-500 ≈ 50-200, adequate for Bayesian 2PL calibration per Konig et al. (2023).\n\nStage 2 — Gated model estimation (small-N, fixed item parameters):\n- Fix a_i = â_i, b_i = b̂_i from Stage 1. This eliminates 2K parameters from estimation, leaving only θ_j (M), ξ_j (M), η_i (K), and δ_i (K) = 2M + 2K free parameters.\n- Estimate via Bayesian MCMC on the 15-20-model paired (original + variant) response matrix.\n- The fixed-parameter approach is critical: with a_i and b_i grounded in large-N calibration, θ_j identification from variant items is well-conditioned (each model responds to K ≈ 1,000 items with known parameters), and contamination parameters (ξ_j, η_i) are identified from original-variant performance gaps with θ_j already anchored.\n\n**Model specifications (two-tier: reduced and full):**\n\nReduced G-2PL (R-G-2PL, person-level contamination only, M additional parameters):\n- For variant item i*: P(Y_{j,i*}=1 | θ_j) = σ(a_i(θ_j − b_i − δ_i))\n- For original item i: P(Y_{j,i}=1 | θ_j, ξ_j) = ξ_j + (1−ξ_j)·σ(a_i(θ_j − b_i))\n- θ_j = model j's genuine reasoning ability (person parameter)\n- ξ_j ∈ [0,1] = model j's global contamination probability (person parameter) — probability that model j has memorized any given original item, assumed uniform across items\n- a_i, b_i = discrimination and difficulty (fixed from Stage 1)\n- δ_i = variant difficulty shift (estimated in Stage 2)\n- Only M additional contamination parameters (vs. M+K for full model), yielding far stronger identifiability at N=15-20\n- Interpretation: ξ_j captures bulk training data contamination (entire benchmarks appearing in web scrapes), which is the dominant contamination mechanism for LLMs\n\nFull G-2PL (person × item contamination, M+K additional parameters):\n- For variant item i*: P(Y_{j,i*}=1 | θ_j) = σ(a_i(θ_j − b_i − δ_i))\n- For original item i: P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i))\n- η_i ∈ [0,1] = item i's contamination susceptibility (item parameter)\n- Adopted only if the simulation study (see below) confirms η_i is recoverable at N=15-20 with acceptable RMSE\n- Each η_i has only M=15-20 observations, making estimation challenging — hierarchical priors provide regularization\n\n**Rationale for G-2PL over G-3PL:** The guessing parameter c_i in 3PL requires 200+ examinees for stable estimation under classical methods, while we have only 15-20 models. Dropping c_i to use 2PL eliminates the most problematic parameter for small samples while retaining the core contamination decomposition. For math benchmarks with open-ended answers (MATH-500, GSM8K), guessing probability is effectively zero, making 2PL substantively appropriate.\n\n**Ablation to Gated-3PL (G-3PL):**\n- P(Y_{j,i*}=1 | θ_j) = c_i + (1−c_i)·σ(a_i(θ_j − b_i − δ_i))\n- P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·[c_i + (1−c_i)·σ(a_i(θ_j − b_i))]\n- c_i fixed to domain-specific constants: c_i = 0 for open-ended math (MATH-500, GSM8K), enabling estimation only for any future MCQ extensions.\n\n**Estimation strategy (fully specified):**\nPrimary: Bayesian MCMC via NumPyro/Stan with hierarchical priors, following DGM's original estimation framework:\n- θ_j ~ N(0, σ²_θ), σ_θ ~ Half-Cauchy(0, 2.5)\n- ξ_j ~ Beta(α_ξ, β_ξ), with α_ξ, β_ξ ~ Gamma(2, 1) (hierarchical; allows posterior to concentrate near 0 for clean models or near 1 for heavily contaminated ones)\n- η_i ~ Beta(α_η, β_η), with α_η, β_η ~ Gamma(2, 1) (hierarchical; full G-2PL only)\n- δ_i ~ N(0, σ²_δ), σ_δ ~ Half-Cauchy(0, 1) (hierarchical; variant shifts expected small)\n- a_i, b_i: fixed from Stage 1 (NOT estimated in Stage 2)\n- MCMC: 4 chains × 2,000 warmup + 2,000 samples, NUTS sampler, R̂ < 1.05 convergence criterion, ESS > 400 per parameter\nComparison: Neural estimation extending PSN-IRT's pseudo-Siamese architecture with an additional gating head that outputs (ξ_j, η_i) — trained via binary cross-entropy on the joint original+variant response matrix, with a_i and b_i initialized from Stage 1 and optionally frozen. This provides a non-Bayesian point estimate comparison.\nAblation: Variational inference via Pyro SVI as a faster alternative to MCMC, using amortized inference for scalability testing.\n\n**Formal identifiability (strengthened by two-stage calibration):**\nWe prove identifiability via a two-step argument that is substantially strengthened by fixing a_i and b_i from Stage 1:\n\n(1) Variant items serve as contamination-free anchors. With a_i, b_i fixed from Stage 1, θ_j is identified from variant responses via standard 2PL person parameter estimation (K ≈ 1,000 items per model, well-determined even for a single model). The difficulty shift δ_i is identified from M model responses per variant item; with M=15-20 and hierarchical priors, this yields credible estimates (validated in simulation study). Key advantage of fixed-parameter calibration: θ_j identification does not depend on the number of models M, only on the number of items K per model — eliminating the classical IRT concern about few examinees.\n\n(2) Given identified θ_j, fixed a_i, b_i, and estimated δ_i, the original-variant performance gap identifies the contamination gate. For R-G-2PL: M gaps per item constrain M values ξ_j — with K ≈ 1,000 items per model, each ξ_j is massively over-determined. For full G-2PL: M·K observed gaps constrain the bilinear product ξ_j·η_i. Under rank-1 bilinear decomposition with M models and K items, M·K observations constrain M+K−1 free parameters (one fixed for scale), identifiable when (M−1)(K−1) > 0 — satisfied for any M,K ≥ 2.\n\n(3) Fisher information: The 2PL Fisher information matrix is well-conditioned even at M=15, unlike 3PL where c_i creates flat likelihood surfaces. With fixed a_i and b_i, the conditional Fisher information for (θ_j, ξ_j) given item parameters has full rank, ensuring local identifiability. The two-stage approach avoids the joint estimation instabilities that plague IRT with few examinees.\n\n**Simulation study for parameter recovery (new, Week 4, 1-2 days CPU):**\n\nDesign: Fully crossed simulation validating G-2PL parameter recovery under two-stage calibration at the target sample sizes.\n\nGenerating model:\n- Item parameters: a_i ~ LogNormal(0, 0.5), b_i ~ N(0, 1), fixed as Stage 1 calibrated values (not re-estimated)\n- θ_j ~ N(0, 1)\n- Contamination prevalence/strength, three scenarios:\n  (a) Low: 20% of models contaminated (ξ_j ~ Beta(8,2) for contaminated, ξ_j = 0 for clean)\n  (b) Medium: 50% of models with ξ_j ~ Beta(5,5) (moderate, variable contamination)\n  (c) High: 80% of models with ξ_j ~ Beta(2,2) (widespread, variable strength)\n- η_i ~ Beta(2, 5) for full G-2PL (most items not highly susceptible)\n- δ_i ~ N(0, 0.5)\n\nConditions (fully crossed):\n- N (models): {15, 20, 50}\n- K (paired items): {100, 500}\n- Contamination scenario: {low, medium, high}\n- Model: {R-G-2PL (ξ_j only), full G-2PL (ξ_j and η_i)}\n- Total: 3 × 2 × 3 × 2 = 36 conditions\n\nReplications: 500 per condition (following Konig et al. 2023; Fox 2025 used 1,000 but with simpler models)\n\nMetrics (per condition, averaged over replications):\n- θ_j: bias, RMSE, 95% credible interval coverage, Kendall-τ with true θ ranking\n- ξ_j: bias, RMSE, 95% CI coverage, Kendall-τ with true ξ ranking\n- η_i (full G-2PL only): bias, RMSE, 95% CI coverage\n- Classification: sensitivity/specificity for identifying contaminated models (ξ_j > 0.3)\n- MCMC diagnostics: mean R̂, mean ESS, non-convergence rate\n\nMCMC per replication: 4 chains × 1,000 warmup + 1,000 samples, NUTS. Estimated compute: ~30s per replication (small model with fixed item params) × 18,000 fits = ~150 CPU-hours, parallelizable across cores to complete in 1-2 days.\n\nDecision rule: If ξ_j RMSE < 0.15 and coverage ∈ [0.90, 0.98] at N=15, proceed with full G-2PL. If η_i recovery is poor (RMSE > 0.25 or coverage < 0.85), adopt R-G-2PL as primary and relegate full G-2PL to future work with larger model pools.\n\n**Prior sensitivity analysis (new, 1 day):**\n\nThree prior specifications applied to the real data MCMC:\n(a) Proposed hierarchical: ξ_j ~ Beta(α_ξ, β_ξ), α_ξ, β_ξ ~ Gamma(2,1) — data-driven, allows concentration near 0 or 1\n(b) Weakly informative flat: ξ_j ~ Beta(1,1) (uniform on [0,1]), η_i ~ Beta(1,1) — maximum prior uncertainty, no hierarchical pooling\n(c) Informative: ξ_j ~ Beta(α_j, β_j) with person-specific priors informed by ConStat contamination flags where available (models flagged contaminated get ξ_j ~ Beta(5,2), unflagged get ξ_j ~ Beta(2,5)); η_i ~ Beta(2,5) reflecting prior belief that most items are not highly susceptible\n\nReport:\n- θ_j ranking stability: Kendall-τ between corrected ability rankings under the three prior specifications\n- ξ_j ordering stability: Kendall-τ between contamination orderings\n- Posterior credible interval widths: precision comparison across priors\n- Key qualitative conclusions: do the same models get flagged as high-contamination (ξ_j > 0.5)?\n- Sensitivity metric: maximum |Δξ_j| across prior pairs for any model — quantifies worst-case prior influence\n\n**Bilinear rank-1 model adequacy plan (full G-2PL only):**\nThe rank-1 assumption (ξ_j·η_i) treats contamination as model-global and item-global, a first-order approximation. We assess:\n(a) Compute standardized residuals r_{j,i} = (Y_{j,i} − P̂_{j,i}) / √(P̂_{j,i}(1−P̂_{j,i})) from the rank-1 fit and report the residual matrix.\n(b) Compute Yen's Q3 statistic for local dependence among original items after conditioning on θ_j — systematic topic-structured residuals would indicate rank-1 insufficiency.\n(c) Apply person-fit statistics (standardized log-likelihood lz*) to detect models whose original-item response patterns deviate from the G-2PL predictions, flagging potential topic-specific contamination.\n(d) If structured residuals emerge, explore rank-2 extension (ξ_j·η_i → ξ_j^(1)·η_i^(1) + ξ_j^(2)·η_i^(2)) or topic-stratified estimation as explicit future work.\n(e) Justification for rank-1 as starting point: LLM contamination is primarily driven by overall training data overlap (entire benchmark suites appearing in Common Crawl/web scrapes) rather than topic-selective memorization; the rank-1 model captures this dominant effect.\n\n**Data collection (within 200 H100-hr budget):**\n\nStage 1 data: Assemble GSM8K per-item response matrix from Open LLM Leaderboard V1 per-model details datasets (huggingface.co/open-llm-leaderboard-old, ~7,000 per-model datasets). Each model's GSM8K details available in configuration 'harness_gsm8k' with per-item correctness fields. Data assembly via HuggingFace datasets library: iterate over available details datasets, extract GSM8K responses, construct binary response matrix. Expected: N_cal ≈ 2,000+ models × 1,359 items. Data assembly effort: ~1 day engineering. For MATH-500: supplement with targeted evaluation of ~50-100 small V1 models on MATH-500 (~15 H100-hrs) plus V2 Level 5 per-item data where available.\n\nStage 2 data: For ~1,000 items (all 1,359 GSM8K items + MATH-500 items up to budget), generate adversarial variants via a novel SymPy-verified rewrite pipeline. This is NOT a MaSTer replication — MaSTer uses LLM-based verification via Qwen2.5-32B-Instruct (98% precision on a rewrite meaning-preservation check); our pipeline instead combines LLM-based rewriting (Qwen3.6-27B for multi-round adversarial rewrites) with formal symbolic verification (SymPy for numerical answer correctness), a novel hybrid that provides stronger guarantees than LLM-only verification for math problems with determinate numerical answers. Pipeline: (1) Qwen3.6-27B generates candidate variants via value/structure perturbation, (2) SymPy verifies that the perturbed problem has a valid, determinate answer differing from the original, (3) human spot-check on 10% sample. Estimated: ~25 H100-hrs for variant generation.\n\nBackup pipelines (if primary pipeline yields <80% valid variants by Week 2): (a) MathCheck (ICLR 2025, open code at github.com/PremiLab-Math/MathCheck) for GSM8K variants; (b) seed with MATH-Perturb's 279 expert-crafted Level 5 perturbations (ICML 2025, open code at github.com/Kaffaljidhmah2/MATH-Perturb) and extend via LLM rewriting for remaining items.\n\nModel evaluation: Collect response matrices from 15-20 models: 10 open-weight (DeepSeek-R2 32B, DeepSeek-V4-Flash 284B, Qwen3.6-27B, Qwen3.5-397B-A17B, GLM-5.1 754B-A40B, OLMo-2-13B, Llama-4-Maverick-17B-A400B, Mistral-Large-3, plus 2 smaller reference models) and 5-8 closed-API models (GPT-4o, GPT-5.2, Claude Sonnet 4.6, Gemini 2.5 Flash, Gemini 3.1 Pro). For GSM8K originals: reuse Open LLM Leaderboard V1 per-item data where available (many open-weight models already evaluated); run new inference only for models not on V1 (~40 H100-hrs). Variant inference: all 15-20 models on generated variants (~80 H100-hrs for open-weight models). Closed-model API costs estimated separately. IRT fitting is negligible (<1 hr CPU for MCMC).\n\n**Validation (four-pronged, addressing domain mismatch concern):**\n\n(1) External ranking correlation: Kendall-τ of CRADE-corrected ability rankings vs. MathArena 2026 uncontaminated competition rankings (~900 problems, 50+ models), targeting τ ≥ 0.85 (revised from 0.90 given domain mismatch between textbook-style MATH-500/GSM8K and competition-style MathArena). Report bootstrap 95% confidence interval. Compare against: (a) raw accuracy rankings, (b) RankLLM difficulty-weighted rankings, (c) DCR-corrected rankings (r=0.66 on hard tasks), (d) JECS-filtered rankings.\n\n(2) Synthetic contamination injection (causal validation): Deliberately fine-tune OLMo-2-13B on MATH-500 training items (1 epoch, mild contamination following established protocols from contamination survey literature) and re-evaluate. If G-2PL correctly recovers elevated ξ for the fine-tuned model while θ remains stable (matching pre-contamination ability), this provides causal evidence that the decomposition works. Compare fine-tuned ξ against clean OLMo-2-13B ξ via posterior credible interval separation. This is the strongest validation because it provides ground-truth contamination status.\n\n(3) Convergent validity with existing detectors: Correlate G-2PL's per-model ξ_j estimates with: (a) ConStat contamination flags (performance gap on rephrased vs. original), (b) PaCoST binary contamination verdicts (paired confidence significance test), (c) PSN-IRT's anomalous guessing-rate parameters. High concordance validates that ξ captures the same construct; low concordance would require investigation of what ξ uniquely captures beyond existing methods.\n\n(4) Ablation showing differential correction benefit: Demonstrate that CRADE correction improves ranking accuracy (vs. MathArena) more for models with high estimated ξ (provably or detectably contaminated) than for models with low ξ. This confirms the correction is targeted rather than uniformly applied.\n\n**Anchor assumption validation (variant contamination-free):**\n(a) Fit standard 2PL to variant-only response matrix (with a_i fixed from Stage 1, estimating only θ_j and δ_i) and compute item-fit statistics (S-X² or Orlando-Thissen) and person-fit statistics (lz*). Good fit supports the anchor assumption — variants behave like clean IRT items measuring genuine ability.\n(b) Check that variant difficulty b_i + δ_i is predictable from original difficulty b_i plus a systematic shift; high-residual outlier items may indicate re-contaminated variants and should be flagged for manual review.\n(c) Cross-validation: Hold out 20% of variant items, fit 2PL on remaining 80%, predict held-out responses. Prediction accuracy comparable to full-data fit supports generalizability.\n(d) Ablation: Compare CRADE results using MATH-Perturb's expert-crafted perturbations (strongest anchor assumption) vs. our SymPy-verified rewrite pipeline to assess sensitivity to variant quality.\n\nAblations: (a) R-G-2PL (ξ_j only) vs. full G-2PL (ξ_j and η_i) — does item-level susceptibility add meaningful signal?, (b) G-2PL vs. G-3PL (with fixed c_i = 0 for math), (c) Bayesian MCMC vs. neural estimation vs. variational inference, (d) number of variant items (100/500/1000), (e) number of models (10/15/20), (f) sensitivity to variant difficulty shift δ_i, (g) rank-1 vs. rank-2 bilinear decomposition if residuals warrant it, (h) RankLLM vs. G-2PL ranking quality, (i) two-stage calibration (GSM8K) vs. concurrent estimation (MATH-500) quality comparison, (j) prior sensitivity across 3 specifications.\n\n## Detailed Description\n\nCRADE introduces a measurement-theoretic framework for decomposing LLM benchmark performance into genuine reasoning ability (θ), contamination exposure (ξ), and item properties, by extending the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from test-security psychometrics to LLM evaluation. The central methodological innovation is a two-stage fixed-parameter calibration architecture: Stage 1 calibrates item parameters (discrimination a_i, difficulty b_i) from Open LLM Leaderboard V1 per-item response data (~2,000+ models × 1,359 GSM8K items, following Polo et al. ICML 2024 and Growing Pains arXiv April 2026), providing well-identified item parameters grounded in large-N calibration; Stage 2 fixes these item parameters and estimates the gated contamination model on a 15-20-model paired response matrix, reducing the estimation problem to person-level ability (θ_j), contamination (ξ_j), item susceptibility (η_i), and variant difficulty shifts (δ_i) only. Two model tiers are presented: (1) the Reduced G-2PL (R-G-2PL), where P(Y_{j,i}=1) = ξ_j + (1−ξ_j)·σ(a_i(θ_j − b_i)) adds only M person-level contamination parameters, maximally parsimonious at N=15-20; and (2) the Full G-2PL, where P(Y_{j,i}=1) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i)) adds M+K parameters with item-specific susceptibility, adopted only if the simulation study confirms η_i recovery. The simulation study (500 replications × 36 conditions: N∈{15,20,50} × K∈{100,500} × 3 contamination scenarios × 2 models) validates parameter recovery under two-stage calibration, reporting bias, RMSE, and 95% credible interval coverage for θ_j and ξ_j — the single most important addition for psychometric-savvy reviewers. Prior sensitivity analysis under three specifications (hierarchical Beta, flat Beta(1,1), ConStat-informed) demonstrates robustness of person-level conclusions. The paired-item design couples each benchmark question with a SymPy-verified adversarial variant — a novel hybrid pipeline combining LLM-based rewriting (Qwen3.6-27B) with symbolic answer verification, providing stronger mathematical guarantees than MaSTer's LLM-only verification. Variant items serve as contamination-free anchors: with item parameters fixed from Stage 1, θ_j is identified from ~1,000 variant items per model (well-determined even for a single model), then contamination parameters are identified from original-variant performance gaps with provable identifiability ((M−1)(K−1) > 0 for rank-1 bilinear decomposition). This circumvents the critical failure of likelihood-based contamination detection on reasoning models (AUROC ≈ 50%, Wang et al. ICLR 2026) by operating entirely on response patterns. Four-pronged validation: (1) Kendall-τ ≥ 0.85 against MathArena's ~900-problem uncontaminated rankings, compared against RankLLM non-parametric baseline, DCR correction, and JECS-filtered rankings; (2) synthetic contamination injection via fine-tuning OLMo-2-13B to causally verify ξ recovery; (3) convergent validity with ConStat, PaCoST, and PSN-IRT; (4) differential correction benefit for high-ξ models. Model adequacy assessed via standardized residuals, Q3 statistics, and person-fit lz* from rank-1 bilinear fit. Focused on GSM8K (1,359 items, full two-stage calibration) with MATH-500 as secondary benchmark, 15-20 models including DeepSeek-R2 32B, Qwen3.6-27B, GLM-5.1, and 5-8 closed-API models, within 230 H100-hrs.\n\n## Key References\n\n- Lost in Benchmarks? Rethinking LLM Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral) — 4PL IRT for 12 LLMs on 41,871 items via pseudo-Siamese neural estimation; flags contamination via guessing-rate anomalies but leaves corrected scoring as open question; demonstrates neural IRT estimation works with very few examinees\n- RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty (ICLR 2026) — non-parametric bidirectional score propagation achieving 90% human alignment on 30 models × 35,550 questions; robust to 50% model removal (ρ=0.94); no contamination modeling; our primary non-parametric baseline\n- DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025) — ad-hoc multiplicative contamination correction achieving r=0.66 on hard tasks; our measurement-theoretic G-2PL subsumes this\n- On The Fragility of Benchmark Contamination Detection in Reasoning Models [Wang, Li, Ko, Zhang] (ICLR 2026) — proves likelihood-based detection fails on reasoning models (AUROC ≈ 50%); motivates response-pattern-based approach\n- Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise [DGM; Shu, Henson, Luecht] (Psychometrika 2013) — key theoretical precedent: gated IRT with hierarchical MCMC estimation decomposes performance into ability + preknowledge; we extend to unknown item exposure via paired items and two-stage calibration\n- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024) — detects contamination via performance gaps on rephrased samples against reference models; confirms paired-item signal but no latent-variable model; used as convergent validity comparison and informative prior source\n- Provable Joint Decontamination for Benchmarking Multiple Large Language Models [JECS] (arXiv May 2026) — conformal p-values via joint envelope selection for multi-model decontamination; binarizes items (keep/discard) while we produce continuous corrected scores\n- RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025) — uses IRT as difficulty reward for RL-based rewriting; we use IRT for joint ability-contamination estimation\n- Toward Automated Robustness Evaluation of Mathematical Reasoning [MaSTer] (arXiv 2026) — validated multi-round adversarial variant pipeline (5 streams × 3 iterations) on 4×4090 GPUs using Qwen2.5-32B-Instruct with LLM-based verification (98% precision); 45-94% failure rates on GSM8K/MATH-500; code claimed at github.com/sustech-nlp/MaSTer but unavailable as of May 2026; our pipeline differs by using SymPy-based symbolic verification instead of LLM-based verification\n- Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist [MathCheck] (ICLR 2025) — open-source variant generation pipeline for GSM8K and GeoQA; backup pipeline for variant generation\n- MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations (ICML 2025) — 279 expert-crafted MATH Level-5 perturbations with SymPy verification; demonstrates 10-25% drops on frontier models; open code provides seed perturbations and strongest anchor-assumption validation\n- MathArena: Evaluating LLMs on Uncontaminated Math Competitions (NeurIPS 2025 D&B Track) — expanded to ~900 problems across 2025-2026 competitions including AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, and Apex; our primary ground-truth validation source\n- PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in LLMs (arXiv 2024) — paired original-perturbed items for binary contamination detection via three-step statistical analysis; confirms paired signal without latent-variable modeling; used as convergent validity comparison\n- Redefining Item Response Models for Small Samples [Fox] (Journal of Educational and Behavioral Statistics 2025) — IRT-BCSM integrates out person parameters for stable estimation at N=50-100; RMSE=0.110 for discrimination at N=50 while standard MML collapses (RMSE=1.782); establishes that Bayesian IRT estimation is viable with small person samples\n- On the Identifiability of 3- and 4-Parameter IRT Models From the Perspective of Knowledge Space Theory [Noventa, Ye, Kelava, Spoto] (Psychometrika 2024) — establishes identifiability conditions for 3PL/4PL via knowledge space theory; our G-2PL proof builds on these results with simpler conditions enabled by the 2PL base\n- Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration [Habba, Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Choshen, Stanovsky] (arXiv April 2026) — two-stage MIRT 2PL fixed-parameter calibration on 295+ Open LLM Leaderboard models, <2% MAE with 100 anchor items, ρ≥0.9; validates the two-stage architecture we adopt for item parameter calibration\n- tinyBenchmarks: evaluating LLMs with fewer examples [Polo, Weber, Choshen, Sun, Xu, Stanovsky] (ICML 2024) — assembles per-item binary response data from Open LLM Leaderboard V1 for 395 models × ~29K items; provides the data assembly methodology and validates IRT-based prediction from small item subsets; our Stage 1 calibration follows their data reconstruction approach\n- Robustness of the Hierarchical 2PL Bayesian Model Under Diverse Conditions [Konig, Khorramdel, Falk, Schmitt] (Behavior Research Methods 2023) — OH2PL with half-Cauchy hyperpriors produces unbiased estimates at N=50 (bias ±0.04) while MML yields 75-89% inadmissible solutions; validates hierarchical Bayesian IRT at small sample sizes; 864 conditions × 100 replications across 6 sample sizes\n- Investigating a weakly informative prior for item scale hyperparameters in hierarchical 3PNO IRT models [Luo, Jiao] (Frontiers in Psychology 2017) — half-t priors for hierarchical IRT; informs our prior specification and sensitivity analysis design for the G-2PL contamination parameters\n- py-irt: A Scalable Item Response Theory Library for Python (IJOC 2023) — GPU-accelerated Bayesian IRT fitting via variational inference; comparison estimation method\n- The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models (arXiv April 2026) — reasoning modes (genuine/scaffolding/decorative); provides qualitative taxonomy for interpreting contamination-ability decomposition\n\n## Resource Estimate\n\n- **manual**: gpu_hours: ~200 H100-hrs (Stage 1 data assembly: 0 GPU / 1 day engineering for GSM8K, 15 hrs for MATH-500 model evaluation; variant generation: 25 hrs with Qwen3.6-27B; open-weight inference on variants: 80 hrs across 10 models; gap-filling original inference: 40 hrs; synthetic contamination fine-tuning of OLMo-2-13B: 5 hrs; buffer: 10 hrs; simulation study: ~150 CPU-hrs / 0 GPU; prior sensitivity: ~10 CPU-hrs / 0 GPU), timeline: 8 weeks (1 researcher: wk1 pipeline+V1 data assembly+variant generation start, wk2 variant generation completion+Stage 1 2PL calibration, wk3 inference+Stage 2 data collection, wk4 G-2PL+R-G-2PL implementation in NumPyro+simulation study (1-2 days CPU), wk5 fitting on real data+prior sensitivity analysis+synthetic contamination experiment, wk6 validation+ablations+RankLLM comparison, wk7-8 writing+proofs+residual analysis), estimated_gpu_cost: $2,100 ($600 GPU compute at $3/hr + $1,400 closed-model API for 8 models × 1K items × ~$0.002/item avg + $100 OLMo fine-tuning)\n- **human_in_loop**: gpu_hours: ~170 H100-hrs (aggressive leaderboard data reuse for Stage 1, focused variant generation on GSM8K only for initial submission, MATH-500 as ablation, skip MATH-500 Stage 1 model evaluation), timeline: 6 weeks, claude_api_cost: $300 (G-2PL+R-G-2PL model implementation in NumPyro, identifiability proof verification, simulation study scripting, residual analysis scripts, RankLLM baseline implementation, prior sensitivity analysis, paper drafting), estimated_gpu_cost: $1,900 ($510 GPU + $1,390 closed-model APIs)\n- **auto_research**: gpu_hours: ~230 H100-hrs (full 20-model coverage, automated hyperparameter sweeps over R-G-2PL/G-2PL/G-3PL variants, extended MATH-500 coverage with Stage 1 calibration, synthetic contamination experiment with 3 fine-tuning recipes, 1000-replication simulation study), timeline: 4 weeks (parallel inference, automated ablation grid), claude_api_cost: $950 (variant generation QA, pipeline orchestration, automated ablation analysis including R-G-2PL vs G-2PL comparison, simulation study analysis, prior sensitivity, draft writing, RankLLM reimplementation), estimated_gpu_cost: $2,600 ($690 GPU + $1,910 closed-model APIs), speed_bottleneck: Sequential GPU inference for MoE models (DeepSeek-V4-Flash on 2×H100, Qwen3.5-397B on 4×H100, GLM-5.1 on 4×H100); MCMC fitting with 4 chains is parallelizable but takes ~30 min on CPU; simulation study is embarrassingly parallel across conditions\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T14:03:21.823Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T14:03:21.823Z",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

## Round 1

52 recorded events

### User

_source line 3 · 2026-05-28T14:03:21.851Z_

【任务】: 请评估以下 proposal 的客观中稿概率。
必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。

【proposal】:
# CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items

## Core Problem

No existing framework can determine whether a model fails adversarial benchmark variants because it memorized original answers (contamination) or because it lacks genuine reasoning ability (capability deficit) — all current work observes this entanglement but none models it within a measurement-theoretic framework, preventing trustworthy LLM capability assessment.

## Research Opportunity

Three previously siloed research streams — IRT-based LLM evaluation (PSN-IRT AAAI 2026 Oral, ATLAS, LEGO-IRT), contamination detection/correction (DCR EMNLP 2025, ConStat NeurIPS 2024, JECS arXiv May 2026), and adversarial robustness testing (MaSTer, RIDE, MATH-Perturb ICML 2025) — have each matured independently to the point where their integration is both technically feasible and urgently needed. The critical catalyst is Wang et al.'s ICLR 2026 proof that all likelihood-based contamination detection fails on reasoning models (AUROC ≈ 50%), creating demand for response-pattern-based alternatives that bypass token-probability signals entirely. A key theoretical precedent exists but has never been applied to LLMs: the Deterministic Gated IRT model (DGM; Shu, Henson & Luecht, Psychometrika 2013) decomposes test performance into genuine ability and cheating/preknowledge components conditioned on item exposure status — precisely the structure needed for LLM contamination. PSN-IRT showed IRT works for LLMs (12 models, 41,871 items, 4PL) but left contamination-adjusted scoring as an explicit open question, flagging anomalous guessing-rate parameters as contamination indicators without providing corrected ability estimates. RankLLM (ICLR 2026) demonstrated that non-parametric difficulty-aware ranking achieves 90% human alignment with only a damping hyperparameter — but provides no contamination decomposition, producing rankings without interpretable ability vs. memorization parameters. A crucial practical enabler has emerged: the Open LLM Leaderboard V1 provides per-item binary response data for 2,000+ models across standard benchmarks including GSM8K (1,359 items), accessible via per-model details datasets (Polo et al., ICML 2024). Combined with Growing Pains' (arXiv April 2026) demonstration that two-stage fixed-parameter calibration achieves <2% error with 100 anchor items and ρ ≥ 0.9 ranking stability, this large-N calibration data resolves the fundamental feasibility concern of fitting IRT-based models with only 15-20 LLMs — by fixing well-calibrated item parameters from Stage 1, Stage 2 estimation reduces to person-level and contamination parameters only. The AAAI 2027 deadline (abstracts July 21, papers July 28, 2026) is 8 weeks out. Nobody sits at the three-way intersection of IRT estimation, contamination correction, and adversarial pairing because these communities publish at different venues (ACL/EMNLP for contamination, ICLR/NeurIPS for robustness, AAAI for psychometric evaluation, Psychometrika/JEBS for test security).

## Research Landscape

The current best contamination-to-correction pipeline is DCR (EMNLP 2025), which produces a DCR Factor via fuzzy inference across four contamination levels, achieving ~4% average error on three benchmarks — but its ad-hoc multiplicative correction Acc_adj = Acc × (1 − DCR Factor) has no measurement-theoretic justification and empirically weakens on hard tasks (r=0.66). PSN-IRT (AAAI 2026 Oral) demonstrates IRT's power for LLM evaluation using a 4PL model across 12 LLMs on 11 benchmarks (41,871 items), flagging contamination indirectly via anomalous guessing-rate parameters, but produces no contamination-adjusted ability scores; critically, PSN-IRT succeeds with 12 models by using neural network estimation (pseudo-Siamese architecture) rather than classical MLE, establishing that neural IRT estimation is viable at small model counts. RankLLM (ICLR 2026) provides a strong non-parametric baseline: bidirectional score propagation between models and questions achieves 90% human alignment on 30 models × 35,550 questions, with remarkable stability under model removal (ρ = 0.94 even with 50% pool removed) and 0.006s convergence — but it produces difficulty-weighted rankings without any contamination modeling. RIDE (arXiv 2025) combines IRT with adversarial perturbation for math evaluation — but uses IRT only as a difficulty reward signal for RL-based question rewriting via RIDE-8B, not for joint ability-contamination estimation. JECS (arXiv May 2026) achieves formal conformal guarantees for multi-model decontamination via joint envelope conformal selection, but wastes information by binarizing items into keep/discard rather than producing continuous corrected scores. ConStat (NeurIPS 2024) detects contamination via performance gaps on rephrased samples using a statistical comparison against reference models, but does not model it as a latent variable within a psychometric framework. In psychometrics, the DGM (Shu et al., Psychometrika 2013) uses a gated IRT formulation estimated via hierarchical MCMC to decompose examinee performance into genuine ability and item-preknowledge components — but assumes item exposure status is known a priori, which is unavailable for LLM training data, and was validated only at operational testing sample sizes (hundreds of examinees). Two paired-item approaches exist but use no IRT: PaCoST (arXiv 2024) performs paired confidence significance testing for binary contamination detection, and ConStat compares primary vs. reference benchmark performance — both confirm the paired-item signal is informative but neither models it as a latent variable. For adversarial variant generation, MaSTer (arXiv 2026) provides a validated multi-round rewrite-verify pipeline (5 parallel streams × 3 iterations) achieving 45-94% target failure rates on GSM8K and MATH-500 using Qwen2.5-32B-Instruct for both rewriting and LLM-based verification (98% precision); code is claimed at github.com/sustech-nlp/MaSTer but was unavailable as of May 2026 — backup pipelines exist via MathCheck (ICLR 2025, open code) and MATH-Perturb (ICML 2025, 279 expert-crafted perturbations with open code). Growing Pains (arXiv April 2026) demonstrates two-stage fixed-parameter calibration for extensible LLM evaluation: calibrating MIRT 2PL item parameters on 295+ reference models, then scoring new models via fixed anchor items, achieving <2% MAE and ρ ≥ 0.9 with 100 anchor items per benchmark — directly applicable to our setting where item parameters are calibrated on large-N leaderboard data and contamination parameters estimated on a smaller model pool. Konig et al. (Behavior Research Methods 2023) demonstrate that hierarchical Bayesian 2PL (OH2PL) with half-Cauchy hyperpriors produces unbiased item parameter estimates down to N=50, while standard MML shows 75-89% inadmissible solutions at that sample size — establishing that Bayesian estimation is the correct choice for small-N IRT. Fox (JEBS 2025) pushes further: IRT-BCSM integrates out person parameters for stable estimation at N=50-100, with RMSE of 0.110 for discrimination at N=50 while standard 2PL/MML collapses (RMSE=1.782). MathArena (NeurIPS 2025 D&B Track) has expanded to ~900 problems across 2025-2026 competitions (AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, Apex) with 50+ models, providing rich uncontaminated ground-truth rankings. Concurrent work search (arXiv, OpenReview, May 2026): no paper attempts joint IRT-based contamination-ability decomposition with paired adversarial items or two-stage fixed-parameter calibration for contamination-aware scoring — the intersection remains unoccupied.

## Proposed Approach

We extend the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from the test-security domain to LLM contamination assessment, introducing the Gated-2PL (G-2PL) model as the primary framework where correct-response probability decomposes into ability-driven and contamination-driven components via a gating mechanism. The key innovations over DGM are: (1) item exposure status is not assumed known but is identified from paired adversarial items, and (2) a two-stage fixed-parameter calibration architecture leverages large-N leaderboard data to resolve the small-sample estimation challenge.

**Two-stage fixed-parameter calibration architecture (central methodological contribution):**

Stage 1 — Item parameter calibration (large-N, standard 2PL):
- Assemble per-item binary response matrix from Open LLM Leaderboard V1 per-model details datasets for GSM8K (N_cal ≈ 2,000+ models × 1,359 items). Per-item data resides in individual per-model datasets under huggingface.co/open-llm-leaderboard-old (naming pattern: details_{org}__{model}), reconstructible following Polo et al. (ICML 2024, tinyBenchmarks). Each dataset contains per-task configurations (e.g., harness_gsm8k) with item-level correctness indicators.
- Fit standard 2PL via marginal maximum likelihood (MML): estimate â_i (discrimination) and b̂_i (difficulty) for each GSM8K item. With N_cal ≈ 2,000+, these estimates are highly stable — Growing Pains demonstrates <2% MAE and ρ ≥ 0.9 with as few as 100 reference models on similar data.
- Validate calibration quality: item-fit statistics (S-X², item-total correlations), dimensionality assessment (eigenvalue ratios from the item correlation matrix), and comparison with Growing Pains' calibrated parameters if available.
- For MATH-500 (secondary benchmark): Stage 1 calibration assembled from (a) V2 leaderboard MATH Level 5 per-model details for the ~100 Level 5 items in MATH-500 (hundreds of models available via gated datasets at huggingface.co/datasets/open-llm-leaderboard/{org}__{model}-details), (b) publicly available per-item MATH-500 evaluation results from major papers and evaluation frameworks (lm-evaluation-harness), and (c) targeted evaluation of ~50-100 small open-weight models (7B-13B) from V1 leaderboard checkpoints on MATH-500 (~15 H100-hrs). Expected N_cal for MATH-500 ≈ 50-200, adequate for Bayesian 2PL calibration per Konig et al. (2023).

Stage 2 — Gated model estimation (small-N, fixed item parameters):
- Fix a_i = â_i, b_i = b̂_i from Stage 1. This eliminates 2K parameters from estimation, leaving only θ_j (M), ξ_j (M), η_i (K), and δ_i (K) = 2M + 2K free parameters.
- Estimate via Bayesian MCMC on the 15-20-model paired (original + variant) response matrix.
- The fixed-parameter approach is critical: with a_i and b_i grounded in large-N calibration, θ_j identification from variant items is well-conditioned (each model responds to K ≈ 1,000 items with known parameters), and contamination parameters (ξ_j, η_i) are identified from original-variant performance gaps with θ_j already anchored.

**Model specifications (two-tier: reduced and full):**

Reduced G-2PL (R-G-2PL, person-level contamination only, M additional parameters):
- For variant item i*: P(Y_{j,i*}=1 | θ_j) = σ(a_i(θ_j − b_i − δ_i))
- For original item i: P(Y_{j,i}=1 | θ_j, ξ_j) = ξ_j + (1−ξ_j)·σ(a_i(θ_j − b_i))
- θ_j = model j's genuine reasoning ability (person parameter)
- ξ_j ∈ [0,1] = model j's global contamination probability (person parameter) — probability that model j has memorized any given original item, assumed uniform across items
- a_i, b_i = discrimination and difficulty (fixed from Stage 1)
- δ_i = variant difficulty shift (estimated in Stage 2)
- Only M additional contamination parameters (vs. M+K for full model), yielding far stronger identifiability at N=15-20
- Interpretation: ξ_j captures bulk training data contamination (entire benchmarks appearing in web scrapes), which is the dominant contamination mechanism for LLMs

Full G-2PL (person × item contamination, M+K additional parameters):
- For variant item i*: P(Y_{j,i*}=1 | θ_j) = σ(a_i(θ_j − b_i − δ_i))
- For original item i: P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i))
- η_i ∈ [0,1] = item i's contamination susceptibility (item parameter)
- Adopted only if the simulation study (see below) confirms η_i is recoverable at N=15-20 with acceptable RMSE
- Each η_i has only M=15-20 observations, making estimation challenging — hierarchical priors provide regularization

**Rationale for G-2PL over G-3PL:** The guessing parameter c_i in 3PL requires 200+ examinees for stable estimation under classical methods, while we have only 15-20 models. Dropping c_i to use 2PL eliminates the most problematic parameter for small samples while retaining the core contamination decomposition. For math benchmarks with open-ended answers (MATH-500, GSM8K), guessing probability is effectively zero, making 2PL substantively appropriate.

**Ablation to Gated-3PL (G-3PL):**
- P(Y_{j,i*}=1 | θ_j) = c_i + (1−c_i)·σ(a_i(θ_j − b_i − δ_i))
- P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·[c_i + (1−c_i)·σ(a_i(θ_j − b_i))]
- c_i fixed to domain-specific constants: c_i = 0 for open-ended math (MATH-500, GSM8K), enabling estimation only for any future MCQ extensions.

**Estimation strategy (fully specified):**
Primary: Bayesian MCMC via NumPyro/Stan with hierarchical priors, following DGM's original estimation framework:
- θ_j ~ N(0, σ²_θ), σ_θ ~ Half-Cauchy(0, 2.5)
- ξ_j ~ Beta(α_ξ, β_ξ), with α_ξ, β_ξ ~ Gamma(2, 1) (hierarchical; allows posterior to concentrate near 0 for clean models or near 1 for heavily contaminated ones)
- η_i ~ Beta(α_η, β_η), with α_η, β_η ~ Gamma(2, 1) (hierarchical; full G-2PL only)
- δ_i ~ N(0, σ²_δ), σ_δ ~ Half-Cauchy(0, 1) (hierarchical; variant shifts expected small)
- a_i, b_i: fixed from Stage 1 (NOT estimated in Stage 2)
- MCMC: 4 chains × 2,000 warmup + 2,000 samples, NUTS sampler, R̂ < 1.05 convergence criterion, ESS > 400 per parameter
Comparison: Neural estimation extending PSN-IRT's pseudo-Siamese architecture with an additional gating head that outputs (ξ_j, η_i) — trained via binary cross-entropy on the joint original+variant response matrix, with a_i and b_i initialized from Stage 1 and optionally frozen. This provides a non-Bayesian point estimate comparison.
Ablation: Variational inference via Pyro SVI as a faster alternative to MCMC, using amortized inference for scalability testing.

**Formal identifiability (strengthened by two-stage calibration):**
We prove identifiability via a two-step argument that is substantially strengthened by fixing a_i and b_i from Stage 1:

(1) Variant items serve as contamination-free anchors. With a_i, b_i fixed from Stage 1, θ_j is identified from variant responses via standard 2PL person parameter estimation (K ≈ 1,000 items per model, well-determined even for a single model). The difficulty shift δ_i is identified from M model responses per variant item; with M=15-20 and hierarchical priors, this yields credible estimates (validated in simulation study). Key advantage of fixed-parameter calibration: θ_j identification does not depend on the number of models M, only on the number of items K per model — eliminating the classical IRT concern about few examinees.

(2) Given identified θ_j, fixed a_i, b_i, and estimated δ_i, the original-variant performance gap identifies the contamination gate. For R-G-2PL: M gaps per item constrain M values ξ_j — with K ≈ 1,000 items per model, each ξ_j is massively over-determined. For full G-2PL: M·K observed gaps constrain the bilinear product ξ_j·η_i. Under rank-1 bilinear decomposition with M models and K items, M·K observations constrain M+K−1 free parameters (one fixed for scale), identifiable when (M−1)(K−1) > 0 — satisfied for any M,K ≥ 2.

(3) Fisher information: The 2PL Fisher information matrix is well-conditioned even at M=15, unlike 3PL where c_i creates flat likelihood surfaces. With fixed a_i and b_i, the conditional Fisher information for (θ_j, ξ_j) given item parameters has full rank, ensuring local identifiability. The two-stage approach avoids the joint estimation instabilities that plague IRT with few examinees.

**Simulation study for parameter recovery (new, Week 4, 1-2 days CPU):**

Design: Fully crossed simulation validating G-2PL parameter recovery under two-stage calibration at the target sample sizes.

Generating model:
- Item parameters: a_i ~ LogNormal(0, 0.5), b_i ~ N(0, 1), fixed as Stage 1 calibrated values (not re-estimated)
- θ_j ~ N(0, 1)
- Contamination prevalence/strength, three scenarios:
  (a) Low: 20% of models contaminated (ξ_j ~ Beta(8,2) for contaminated, ξ_j = 0 for clean)
  (b) Medium: 50% of models with ξ_j ~ Beta(5,5) (moderate, variable contamination)
  (c) High: 80% of models with ξ_j ~ Beta(2,2) (widespread, variable strength)
- η_i ~ Beta(2, 5) for full G-2PL (most items not highly susceptible)
- δ_i ~ N(0, 0.5)

Conditions (fully crossed):
- N (models): {15, 20, 50}
- K (paired items): {100, 500}
- Contamination scenario: {low, medium, high}
- Model: {R-G-2PL (ξ_j only), full G-2PL (ξ_j and η_i)}
- Total: 3 × 2 × 3 × 2 = 36 conditions

Replications: 500 per condition (following Konig et al. 2023; Fox 2025 used 1,000 but with simpler models)

Metrics (per condition, averaged over replications):
- θ_j: bias, RMSE, 95% credible interval coverage, Kendall-τ with true θ ranking
- ξ_j: bias, RMSE, 95% CI coverage, Kendall-τ with true ξ ranking
- η_i (full G-2PL only): bias, RMSE, 95% CI coverage
- Classification: sensitivity/specificity for identifying contaminated models (ξ_j > 0.3)
- MCMC diagnostics: mean R̂, mean ESS, non-convergence rate

MCMC per replication: 4 chains × 1,000 warmup + 1,000 samples, NUTS. Estimated compute: ~30s per replication (small model with fixed item params) × 18,000 fits = ~150 CPU-hours, parallelizable across cores to complete in 1-2 days.

Decision rule: If ξ_j RMSE < 0.15 and coverage ∈ [0.90, 0.98] at N=15, proceed with full G-2PL. If η_i recovery is poor (RMSE > 0.25 or coverage < 0.85), adopt R-G-2PL as primary and relegate full G-2PL to future work with larger model pools.

**Prior sensitivity analysis (new, 1 day):**

Three prior specifications applied to the real data MCMC:
(a) Proposed hierarchical: ξ_j ~ Beta(α_ξ, β_ξ), α_ξ, β_ξ ~ Gamma(2,1) — data-driven, allows concentration near 0 or 1
(b) Weakly informative flat: ξ_j ~ Beta(1,1) (uniform on [0,1]), η_i ~ Beta(1,1) — maximum prior uncertainty, no hierarchical pooling
(c) Informative: ξ_j ~ Beta(α_j, β_j) with person-specific priors informed by ConStat contamination flags where available (models flagged contaminated get ξ_j ~ Beta(5,2), unflagged get ξ_j ~ Beta(2,5)); η_i ~ Beta(2,5) reflecting prior belief that most items are not highly susceptible

Report:
- θ_j ranking stability: Kendall-τ between corrected ability rankings under the three prior specifications
- ξ_j ordering stability: Kendall-τ between contamination orderings
- Posterior credible interval widths: precision comparison across priors
- Key qualitative conclusions: do the same models get flagged as high-contamination (ξ_j > 0.5)?
- Sensitivity metric: maximum |Δξ_j| across prior pairs for any model — quantifies worst-case prior influence

**Bilinear rank-1 model adequacy plan (full G-2PL only):**
The rank-1 assumption (ξ_j·η_i) treats contamination as model-global and item-global, a first-order approximation. We assess:
(a) Compute standardized residuals r_{j,i} = (Y_{j,i} − P̂_{j,i}) / √(P̂_{j,i}(1−P̂_{j,i})) from the rank-1 fit and report the residual matrix.
(b) Compute Yen's Q3 statistic for local dependence among original items after conditioning on θ_j — systematic topic-structured residuals would indicate rank-1 insufficiency.
(c) Apply person-fit statistics (standardized log-likelihood lz*) to detect models whose original-item response patterns deviate from the G-2PL predictions, flagging potential topic-specific contamination.
(d) If structured residuals emerge, explore rank-2 extension (ξ_j·η_i → ξ_j^(1)·η_i^(1) + ξ_j^(2)·η_i^(2)) or topic-stratified estimation as explicit future work.
(e) Justification for rank-1 as starting point: LLM contamination is primarily driven by overall training data overlap (entire benchmark suites appearing in Common Crawl/web scrapes) rather than topic-selective memorization; the rank-1 model captures this dominant effect.

**Data collection (within 200 H100-hr budget):**

Stage 1 data: Assemble GSM8K per-item response matrix from Open LLM Leaderboard V1 per-model details datasets (huggingface.co/open-llm-leaderboard-old, ~7,000 per-model datasets). Each model's GSM8K details available in configuration 'harness_gsm8k' with per-item correctness fields. Data assembly via HuggingFace datasets library: iterate over available details datasets, extract GSM8K responses, construct binary response matrix. Expected: N_cal ≈ 2,000+ models × 1,359 items. Data assembly effort: ~1 day engineering. For MATH-500: supplement with targeted evaluation of ~50-100 small V1 models on MATH-500 (~15 H100-hrs) plus V2 Level 5 per-item data where available.

Stage 2 data: For ~1,000 items (all 1,359 GSM8K items + MATH-500 items up to budget), generate adversarial variants via a novel SymPy-verified rewrite pipeline. This is NOT a MaSTer replication — MaSTer uses LLM-based verification via Qwen2.5-32B-Instruct (98% precision on a rewrite meaning-preservation check); our pipeline instead combines LLM-based rewriting (Qwen3.6-27B for multi-round adversarial rewrites) with formal symbolic verification (SymPy for numerical answer correctness), a novel hybrid that provides stronger guarantees than LLM-only verification for math problems with determinate numerical answers. Pipeline: (1) Qwen3.6-27B generates candidate variants via value/structure perturbation, (2) SymPy verifies that the perturbed problem has a valid, determinate answer differing from the original, (3) human spot-check on 10% sample. Estimated: ~25 H100-hrs for variant generation.

Backup pipelines (if primary pipeline yields <80% valid variants by Week 2): (a) MathCheck (ICLR 2025, open code at github.com/PremiLab-Math/MathCheck) for GSM8K variants; (b) seed with MATH-Perturb's 279 expert-crafted Level 5 perturbations (ICML 2025, open code at github.com/Kaffaljidhmah2/MATH-Perturb) and extend via LLM rewriting for remaining items.

Model evaluation: Collect response matrices from 15-20 models: 10 open-weight (DeepSeek-R2 32B, DeepSeek-V4-Flash 284B, Qwen3.6-27B, Qwen3.5-397B-A17B, GLM-5.1 754B-A40B, OLMo-2-13B, Llama-4-Maverick-17B-A400B, Mistral-Large-3, plus 2 smaller reference models) and 5-8 closed-API models (GPT-4o, GPT-5.2, Claude Sonnet 4.6, Gemini 2.5 Flash, Gemini 3.1 Pro). For GSM8K originals: reuse Open LLM Leaderboard V1 per-item data where available (many open-weight models already evaluated); run new inference only for models not on V1 (~40 H100-hrs). Variant inference: all 15-20 models on generated variants (~80 H100-hrs for open-weight models). Closed-model API costs estimated separately. IRT fitting is negligible (<1 hr CPU for MCMC).

**Validation (four-pronged, addressing domain mismatch concern):**

(1) External ranking correlation: Kendall-τ of CRADE-corrected ability rankings vs. MathArena 2026 uncontaminated competition rankings (~900 problems, 50+ models), targeting τ ≥ 0.85 (revised from 0.90 given domain mismatch between textbook-style MATH-500/GSM8K and competition-style MathArena). Report bootstrap 95% confidence interval. Compare against: (a) raw accuracy rankings, (b) RankLLM difficulty-weighted rankings, (c) DCR-corrected rankings (r=0.66 on hard tasks), (d) JECS-filtered rankings.

(2) Synthetic contamination injection (causal validation): Deliberately fine-tune OLMo-2-13B on MATH-500 training items (1 epoch, mild contamination following established protocols from contamination survey literature) and re-evaluate. If G-2PL correctly recovers elevated ξ for the fine-tuned model while θ remains stable (matching pre-contamination ability), this provides causal evidence that the decomposition works. Compare fine-tuned ξ against clean OLMo-2-13B ξ via posterior credible interval separation. This is the strongest validation because it provides ground-truth contamination status.

(3) Convergent validity with existing detectors: Correlate G-2PL's per-model ξ_j estimates with: (a) ConStat contamination flags (performance gap on rephrased vs. original), (b) PaCoST binary contamination verdicts (paired confidence significance test), (c) PSN-IRT's anomalous guessing-rate parameters. High concordance validates that ξ captures the same construct; low concordance would require investigation of what ξ uniquely captures beyond existing methods.

(4) Ablation showing differential correction benefit: Demonstrate that CRADE correction improves ranking accuracy (vs. MathArena) more for models with high estimated ξ (provably or detectably contaminated) than for models with low ξ. This confirms the correction is targeted rather than uniformly applied.

**Anchor assumption validation (variant contamination-free):**
(a) Fit standard 2PL to variant-only response matrix (with a_i fixed from Stage 1, estimating only θ_j and δ_i) and compute item-fit statistics (S-X² or Orlando-Thissen) and person-fit statistics (lz*). Good fit supports the anchor assumption — variants behave like clean IRT items measuring genuine ability.
(b) Check that variant difficulty b_i + δ_i is predictable from original difficulty b_i plus a systematic shift; high-residual outlier items may indicate re-contaminated variants and should be flagged for manual review.
(c) Cross-validation: Hold out 20% of variant items, fit 2PL on remaining 80%, predict held-out responses. Prediction accuracy comparable to full-data fit supports generalizability.
(d) Ablation: Compare CRADE results using MATH-Perturb's expert-crafted perturbations (strongest anchor assumption) vs. our SymPy-verified rewrite pipeline to assess sensitivity to variant quality.

Ablations: (a) R-G-2PL (ξ_j only) vs. full G-2PL (ξ_j and η_i) — does item-level susceptibility add meaningful signal?, (b) G-2PL vs. G-3PL (with fixed c_i = 0 for math), (c) Bayesian MCMC vs. neural estimation vs. variational inference, (d) number of variant items (100/500/1000), (e) number of models (10/15/20), (f) sensitivity to variant difficulty shift δ_i, (g) rank-1 vs. rank-2 bilinear decomposition if residuals warrant it, (h) RankLLM vs. G-2PL ranking quality, (i) two-stage calibration (GSM8K) vs. concurrent estimation (MATH-500) quality comparison, (j) prior sensitivity across 3 specifications.

## Detailed Description

CRADE introduces a measurement-theoretic framework for decomposing LLM benchmark performance into genuine reasoning ability (θ), contamination exposure (ξ), and item properties, by extending the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from test-security psychometrics to LLM evaluation. The central methodological innovation is a two-stage fixed-parameter calibration architecture: Stage 1 calibrates item parameters (discrimination a_i, difficulty b_i) from Open LLM Leaderboard V1 per-item response data (~2,000+ models × 1,359 GSM8K items, following Polo et al. ICML 2024 and Growing Pains arXiv April 2026), providing well-identified item parameters grounded in large-N calibration; Stage 2 fixes these item parameters and estimates the gated contamination model on a 15-20-model paired response matrix, reducing the estimation problem to person-level ability (θ_j), contamination (ξ_j), item susceptibility (η_i), and variant difficulty shifts (δ_i) only. Two model tiers are presented: (1) the Reduced G-2PL (R-G-2PL), where P(Y_{j,i}=1) = ξ_j + (1−ξ_j)·σ(a_i(θ_j − b_i)) adds only M person-level contamination parameters, maximally parsimonious at N=15-20; and (2) the Full G-2PL, where P(Y_{j,i}=1) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i)) adds M+K parameters with item-specific susceptibility, adopted only if the simulation study confirms η_i recovery. The simulation study (500 replications × 36 conditions: N∈{15,20,50} × K∈{100,500} × 3 contamination scenarios × 2 models) validates parameter recovery under two-stage calibration, reporting bias, RMSE, and 95% credible interval coverage for θ_j and ξ_j — the single most important addition for psychometric-savvy reviewers. Prior sensitivity analysis under three specifications (hierarchical Beta, flat Beta(1,1), ConStat-informed) demonstrates robustness of person-level conclusions. The paired-item design couples each benchmark question with a SymPy-verified adversarial variant — a novel hybrid pipeline combining LLM-based rewriting (Qwen3.6-27B) with symbolic answer verification, providing stronger mathematical guarantees than MaSTer's LLM-only verification. Variant items serve as contamination-free anchors: with item parameters fixed from Stage 1, θ_j is identified from ~1,000 variant items per model (well-determined even for a single model), then contamination parameters are identified from original-variant performance gaps with provable identifiability ((M−1)(K−1) > 0 for rank-1 bilinear decomposition). This circumvents the critical failure of likelihood-based contamination detection on reasoning models (AUROC ≈ 50%, Wang et al. ICLR 2026) by operating entirely on response patterns. Four-pronged validation: (1) Kendall-τ ≥ 0.85 against MathArena's ~900-problem uncontaminated rankings, compared against RankLLM non-parametric baseline, DCR correction, and JECS-filtered rankings; (2) synthetic contamination injection via fine-tuning OLMo-2-13B to causally verify ξ recovery; (3) convergent validity with ConStat, PaCoST, and PSN-IRT; (4) differential correction benefit for high-ξ models. Model adequacy assessed via standardized residuals, Q3 statistics, and person-fit lz* from rank-1 bilinear fit. Focused on GSM8K (1,359 items, full two-stage calibration) with MATH-500 as secondary benchmark, 15-20 models including DeepSeek-R2 32B, Qwen3.6-27B, GLM-5.1, and 5-8 closed-API models, within 230 H100-hrs.

## Key References

- Lost in Benchmarks? Rethinking LLM Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral) — 4PL IRT for 12 LLMs on 41,871 items via pseudo-Siamese neural estimation; flags contamination via guessing-rate anomalies but leaves corrected scoring as open question; demonstrates neural IRT estimation works with very few examinees
- RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty (ICLR 2026) — non-parametric bidirectional score propagation achieving 90% human alignment on 30 models × 35,550 questions; robust to 50% model removal (ρ=0.94); no contamination modeling; our primary non-parametric baseline
- DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025) — ad-hoc multiplicative contamination correction achieving r=0.66 on hard tasks; our measurement-theoretic G-2PL subsumes this
- On The Fragility of Benchmark Contamination Detection in Reasoning Models [Wang, Li, Ko, Zhang] (ICLR 2026) — proves likelihood-based detection fails on reasoning models (AUROC ≈ 50%); motivates response-pattern-based approach
- Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise [DGM; Shu, Henson, Luecht] (Psychometrika 2013) — key theoretical precedent: gated IRT with hierarchical MCMC estimation decomposes performance into ability + preknowledge; we extend to unknown item exposure via paired items and two-stage calibration
- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024) — detects contamination via performance gaps on rephrased samples against reference models; confirms paired-item signal but no latent-variable model; used as convergent validity comparison and informative prior source
- Provable Joint Decontamination for Benchmarking Multiple Large Language Models [JECS] (arXiv May 2026) — conformal p-values via joint envelope selection for multi-model decontamination; binarizes items (keep/discard) while we produce continuous corrected scores
- RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025) — uses IRT as difficulty reward for RL-based rewriting; we use IRT for joint ability-contamination estimation
- Toward Automated Robustness Evaluation of Mathematical Reasoning [MaSTer] (arXiv 2026) — validated multi-round adversarial variant pipeline (5 streams × 3 iterations) on 4×4090 GPUs using Qwen2.5-32B-Instruct with LLM-based verification (98% precision); 45-94% failure rates on GSM8K/MATH-500; code claimed at github.com/sustech-nlp/MaSTer but unavailable as of May 2026; our pipeline differs by using SymPy-based symbolic verification instead of LLM-based verification
- Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist [MathCheck] (ICLR 2025) — open-source variant generation pipeline for GSM8K and GeoQA; backup pipeline for variant generation
- MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations (ICML 2025) — 279 expert-crafted MATH Level-5 perturbations with SymPy verification; demonstrates 10-25% drops on frontier models; open code provides seed perturbations and strongest anchor-assumption validation
- MathArena: Evaluating LLMs on Uncontaminated Math Competitions (NeurIPS 2025 D&B Track) — expanded to ~900 problems across 2025-2026 competitions including AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, and Apex; our primary ground-truth validation source
- PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in LLMs (arXiv 2024) — paired original-perturbed items for binary contamination detection via three-step statistical analysis; confirms paired signal without latent-variable modeling; used as convergent validity comparison
- Redefining Item Response Models for Small Samples [Fox] (Journal of Educational and Behavioral Statistics 2025) — IRT-BCSM integrates out person parameters for stable estimation at N=50-100; RMSE=0.110 for discrimination at N=50 while standard MML collapses (RMSE=1.782); establishes that Bayesian IRT estimation is viable with small person samples
- On the Identifiability of 3- and 4-Parameter IRT Models From the Perspective of Knowledge Space Theory [Noventa, Ye, Kelava, Spoto] (Psychometrika 2024) — establishes identifiability conditions for 3PL/4PL via knowledge space theory; our G-2PL proof builds on these results with simpler conditions enabled by the 2PL base
- Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration [Habba, Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Choshen, Stanovsky] (arXiv April 2026) — two-stage MIRT 2PL fixed-parameter calibration on 295+ Open LLM Leaderboard models, <2% MAE with 100 anchor items, ρ≥0.9; validates the two-stage architecture we adopt for item parameter calibration
- tinyBenchmarks: evaluating LLMs with fewer examples [Polo, Weber, Choshen, Sun, Xu, Stanovsky] (ICML 2024) — assembles per-item binary response data from Open LLM Leaderboard V1 for 395 models × ~29K items; provides the data assembly methodology and validates IRT-based prediction from small item subsets; our Stage 1 calibration follows their data reconstruction approach
- Robustness of the Hierarchical 2PL Bayesian Model Under Diverse Conditions [Konig, Khorramdel, Falk, Schmitt] (Behavior Research Methods 2023) — OH2PL with half-Cauchy hyperpriors produces unbiased estimates at N=50 (bias ±0.04) while MML yields 75-89% inadmissible solutions; validates hierarchical Bayesian IRT at small sample sizes; 864 conditions × 100 replications across 6 sample sizes
- Investigating a weakly informative prior for item scale hyperparameters in hierarchical 3PNO IRT models [Luo, Jiao] (Frontiers in Psychology 2017) — half-t priors for hierarchical IRT; informs our prior specification and sensitivity analysis design for the G-2PL contamination parameters
- py-irt: A Scalable Item Response Theory Library for Python (IJOC 2023) — GPU-accelerated Bayesian IRT fitting via variational inference; comparison estimation method
- The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models (arXiv April 2026) — reasoning modes (genuine/scaffolding/decorative); provides qualitative taxonomy for interpreting contamination-ability decomposition

## Resource Estimate

- **manual**: gpu_hours: ~200 H100-hrs (Stage 1 data assembly: 0 GPU / 1 day engineering for GSM8K, 15 hrs for MATH-500 model evaluation; variant generation: 25 hrs with Qwen3.6-27B; open-weight inference on variants: 80 hrs across 10 models; gap-filling original inference: 40 hrs; synthetic contamination fine-tuning of OLMo-2-13B: 5 hrs; buffer: 10 hrs; simulation study: ~150 CPU-hrs / 0 GPU; prior sensitivity: ~10 CPU-hrs / 0 GPU), timeline: 8 weeks (1 researcher: wk1 pipeline+V1 data assembly+variant generation start, wk2 variant generation completion+Stage 1 2PL calibration, wk3 inference+Stage 2 data collection, wk4 G-2PL+R-G-2PL implementation in NumPyro+simulation study (1-2 days CPU), wk5 fitting on real data+prior sensitivity analysis+synthetic contamination experiment, wk6 validation+ablations+RankLLM comparison, wk7-8 writing+proofs+residual analysis), estimated_gpu_cost: $2,100 ($600 GPU compute at $3/hr + $1,400 closed-model API for 8 models × 1K items × ~$0.002/item avg + $100 OLMo fine-tuning)
- **human_in_loop**: gpu_hours: ~170 H100-hrs (aggressive leaderboard data reuse for Stage 1, focused variant generation on GSM8K only for initial submission, MATH-500 as ablation, skip MATH-500 Stage 1 model evaluation), timeline: 6 weeks, claude_api_cost: $300 (G-2PL+R-G-2PL model implementation in NumPyro, identifiability proof verification, simulation study scripting, residual analysis scripts, RankLLM baseline implementation, prior sensitivity analysis, paper drafting), estimated_gpu_cost: $1,900 ($510 GPU + $1,390 closed-model APIs)
- **auto_research**: gpu_hours: ~230 H100-hrs (full 20-model coverage, automated hyperparameter sweeps over R-G-2PL/G-2PL/G-3PL variants, extended MATH-500 coverage with Stage 1 calibration, synthetic contamination experiment with 3 fine-tuning recipes, 1000-replication simulation study), timeline: 4 weeks (parallel inference, automated ablation grid), claude_api_cost: $950 (variant generation QA, pipeline orchestration, automated ablation analysis including R-G-2PL vs G-2PL comparison, simulation study analysis, prior sensitivity, draft writing, RankLLM reimplementation), estimated_gpu_cost: $2,600 ($690 GPU + $1,910 closed-model APIs), speed_bottleneck: Sequential GPU inference for MoE models (DeepSeek-V4-Flash on 2×H100, Qwen3.5-397B on 4×H100, GLM-5.1 on 4×H100); MCMC fitting with 4 chains is parallelizable but takes ~30 min on CPU; simulation study is embarrassingly parallel across conditions


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "0a457796-5b5a-4d5d-8e8e-b26efb7ec580",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T14:03:21.848Z_

```json
{
  "parentUuid": "0a457796-5b5a-4d5d-8e8e-b26efb7ec580",
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
  "uuid": "6d5fd9b4-2ac8-4100-a802-2c0c1638303d",
  "timestamp": "2026-05-28T14:03:21.848Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T14:03:21.848Z_

```json
{
  "parentUuid": "6d5fd9b4-2ac8-4100-a802-2c0c1638303d",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "1f61edcc-f588-474b-8584-f8dbb3da3fd9",
  "timestamp": "2026-05-28T14:03:21.848Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "1f61edcc-f588-474b-8584-f8dbb3da3fd9",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate proposal on contamination-ability LLM decomposition",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Assistant

_source line 8 · 2026-05-28T14:03:30.413Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed research proposal for CRADE (Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items). I need to evaluate this proposal's idea quality for AAAI 2026 submission potential.

Let me first do the required web searches to understand the current landscape before making any judgments.

Key things I need to search for:
1. IRT-based LLM evaluation (PSN-IRT, Growing Pains, RankLLM)
2. Contamination detection/correction in LLMs (DCR, ConStat, JECS)


3. Adversarial robustness testing for math benchmarks (MaSTer, MATH-Perturb)
4. The DGM model from psychometrics
5. Wang et al. ICLR 2026 on likelihood-based contamination detection failure

I'll search for these systematically to get a comprehensive picture of the related work landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f61edcc-f588-474b-8584-f8dbb3da3fd9",
  "isSidechain": false,
  "requestId": "req_011CbV6GqytuGhzsZQaz9GwE",
  "type": "assistant",
  "uuid": "e261a33e-729a-4c2a-8549-c6b5b917b113",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpCLPBzhB2hVGAfGSBSLFu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16246,
      "cache_read_input_tokens": 11014,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 333,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16246
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

_source line 9 · 2026-05-28T14:03:30.417Z_

I need to conduct thorough field research before evaluating this proposal. Let me start with multiple targeted searches to understand the current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e261a33e-729a-4c2a-8549-c6b5b917b113",
  "isSidechain": false,
  "requestId": "req_011CbV6GqytuGhzsZQaz9GwE",
  "type": "assistant",
  "uuid": "a0dfd6b1-1208-44ae-8092-a2c2ee60a415",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpCLPBzhB2hVGAfGSBSLFu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16246,
      "cache_read_input_tokens": 11014,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 333,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16246
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

_source line 10 · 2026-05-28T14:03:30.425Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01VSmTASoKcjMyAF8WsSJxic`</summary>

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
  "parentUuid": "a0dfd6b1-1208-44ae-8092-a2c2ee60a415",
  "isSidechain": false,
  "requestId": "req_011CbV6GqytuGhzsZQaz9GwE",
  "type": "assistant",
  "uuid": "6ecb0989-d5ca-482c-8e1e-47a226a6a650",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01KpCLPBzhB2hVGAfGSBSLFu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16246,
      "cache_read_input_tokens": 11014,
      "output_tokens": 333,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16246,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 333,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16246,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16246
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

_source line 11 · 2026-05-28T14:03:30.457Z_

<details><summary>↩ Tool result · `toolu_01VSmTASoKcjMyAF8WsSJxic`</summary>

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
  "parentUuid": "6ecb0989-d5ca-482c-8e1e-47a226a6a650",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "c6c0cbba-d1ea-4659-a402-739b92accf38",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "6ecb0989-d5ca-482c-8e1e-47a226a6a650",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T14:03:33.551Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct the required searches. I'll do multiple searches in parallel to cover the key areas.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c6c0cbba-d1ea-4659-a402-739b92accf38",
  "isSidechain": false,
  "requestId": "req_011CbV6HUaK9MYW9Y1WYey3U",
  "type": "assistant",
  "uuid": "1d624941-680a-4640-929c-cba6d404a74d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SW9mB2q6x3spgGv77KS6fN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 27260,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 120,
          "cache_read_input_tokens": 27260,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 13 · 2026-05-28T14:03:34.128Z_

Let me conduct the required field research with multiple targeted searches.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1d624941-680a-4640-929c-cba6d404a74d",
  "isSidechain": false,
  "requestId": "req_011CbV6HUaK9MYW9Y1WYey3U",
  "type": "assistant",
  "uuid": "c4ceb213-7ec3-428e-9f6e-bf38a7d57178",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SW9mB2q6x3spgGv77KS6fN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 27260,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 120,
          "cache_read_input_tokens": 27260,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 14 · 2026-05-28T14:03:34.413Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_015pLTCxGjhmQue2N8S82wRc`</summary>

```json
{
  "query": "PSN-IRT item response theory LLM evaluation AAAI 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c4ceb213-7ec3-428e-9f6e-bf38a7d57178",
  "isSidechain": false,
  "requestId": "req_011CbV6HUaK9MYW9Y1WYey3U",
  "type": "assistant",
  "uuid": "f31819e2-dd39-46d1-b305-b4f41a9aad60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SW9mB2q6x3spgGv77KS6fN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 860,
      "cache_read_input_tokens": 27260,
      "output_tokens": 120,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 860,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 120,
          "cache_read_input_tokens": 27260,
          "cache_creation_input_tokens": 860,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 860
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

_source line 15 · 2026-05-28T14:03:43.069Z_

<details><summary>↩ Tool result · `toolu_015pLTCxGjhmQue2N8S82wRc`</summary>

```text
Web search results for query: "PSN-IRT item response theory LLM evaluation AAAI 2026"

Links: [{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v3"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://ojs.aaai.org/index.php/AAAI/article/download/40814/44775"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"},{"title":"When Classical Test Theory Alone Is Not Enough: How Item Response Theory + Psychometrics Strengthen Modern LLM Evaluation | by Lulu Yan | Medium","url":"https://luluyan.medium.com/why-classical-test-theory-falls-short-for-llm-evaluation-and-how-item-response-theory-irt-93f03f3b6a2a"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory","url":"https://arxiv.org/pdf/2509.22888"}]

Based on the search results, here's what I found about PSN-IRT:

## Overview

PSN-IRT is a framework based on Item Response Theory (IRT) for a deep analysis of LLM benchmark quality. The full name is Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture.

## AAAI 2026 Publication

The paper was accepted as an AAAI 2026 Oral presentation, with the title "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory."

## Scope and Findings

PSN-IRT was used to conduct extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. The framework was validated through extensive experiments on evaluation results from 12 LLMs across 11 benchmarks, and the results show that PSN-IRT outperforms previous approaches in both parameter estimation accuracy and reliability.

## Key Contributions

The analysis revealed that LLM benchmarks fail to achieve simultaneous excellence across multiple measurements, suffer from widespread saturation and insufficient difficulty ceilings, and exhibit data contamination in numerous items. The paper also demonstrates that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.

The code is available on GitHub at https://github.com/Joe-Hall-Lee/PSN-IRT.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f31819e2-dd39-46d1-b305-b4f41a9aad60",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "812e26a4-7889-4115-9a56-4aa7410d7ddd",
  "toolUseResult": {
    "query": "PSN-IRT item response theory LLM evaluation AAAI 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Uan2eP3pLJg1mqDjUMXDW7",
        "content": [
          {
            "title": "GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub",
            "url": "https://github.com/Joe-Hall-Lee/PSN-IRT"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40814"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v3"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/pdf/2505.15055"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/download/40814/44775"
          },
          {
            "title": "[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/abs/2505.15055"
          },
          {
            "title": "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory",
            "url": "https://arxiv.org/pdf/2602.00521"
          },
          {
            "title": "When Classical Test Theory Alone Is Not Enough: How Item Response Theory + Psychometrics Strengthen Modern LLM Evaluation | by Lulu Yan | Medium",
            "url": "https://luluyan.medium.com/why-classical-test-theory-falls-short-for-llm-evaluation-and-how-item-response-theory-irt-93f03f3b6a2a"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/pdf/2511.04689"
          },
          {
            "title": "JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory",
            "url": "https://arxiv.org/pdf/2509.22888"
          }
        ]
      },
      "Based on the search results, here's what I found about PSN-IRT:\n\n## Overview\n\nPSN-IRT is a framework based on Item Response Theory (IRT) for a deep analysis of LLM benchmark quality. The full name is Pseudo-Siamese Network for Item Response Theory (PSN-IRT), an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture.\n\n## AAAI 2026 Publication\n\nThe paper was accepted as an AAAI 2026 Oral presentation, with the title \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory.\"\n\n## Scope and Findings\n\nPSN-IRT was used to conduct extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. The framework was validated through extensive experiments on evaluation results from 12 LLMs across 11 benchmarks, and the results show that PSN-IRT outperforms previous approaches in both parameter estimation accuracy and reliability.\n\n## Key Contributions\n\nThe analysis revealed that LLM benchmarks fail to achieve simultaneous excellence across multiple measurements, suffer from widespread saturation and insufficient difficulty ceilings, and exhibit data contamination in numerous items. The paper also demonstrates that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.\n\nThe code is available on GitHub at https://github.com/Joe-Hall-Lee/PSN-IRT."
    ],
    "durationSeconds": 8.644349613,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f31819e2-dd39-46d1-b305-b4f41a9aad60",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 16 · 2026-05-28T14:03:46.858Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014ASyRkWr4RgM3Meie5jbHe`</summary>

```json
{
  "query": "RankLLM weighted ranking question difficulty ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "812e26a4-7889-4115-9a56-4aa7410d7ddd",
  "isSidechain": false,
  "requestId": "req_011CbV6JR1XbFndHGRsGj7Mz",
  "type": "assistant",
  "uuid": "077edbbd-4260-4104-9990-ed16648de4d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015UVPZQvjLV1YUnfw18MsYA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1087,
      "cache_read_input_tokens": 28120,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1087,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 28120,
          "cache_creation_input_tokens": 1087,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1087
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

_source line 17 · 2026-05-28T14:03:52.578Z_

<details><summary>↩ Tool result · `toolu_014ASyRkWr4RgM3Meie5jbHe`</summary>

```text
Web search results for query: "RankLLM weighted ranking question difficulty ICLR 2026"

Links: [{"title":"RANKLLM: WEIGHTED RANKING OF LLMS BY QUAN","url":"https://openreview.net/pdf/c22aab26d0cee50994697242fa86488f0f24707d.pdf"},{"title":"(PDF) RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://www.researchgate.net/publication/400812163_RankLLM_Weighted_Ranking_of_LLMs_by_Quantifying_Question_Difficulty"},{"title":"[2602.12424v1] RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://arxiv.org/abs/2602.12424v1"},{"title":"[2602.12424] RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://arxiv.org/abs/2602.12424"},{"title":"RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty | OpenReview","url":"https://openreview.net/forum?id=jnX5GJIoYt"},{"title":"RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://arxiv.org/html/2602.12424"}]

I found relevant information about RankLLM. Here's what the search reveals:

## RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty

RankLLM is a novel framework designed to quantify both question difficulty and model competency. RankLLM introduces difficulty as the primary criterion for differentiation, enabling a more fine-grained evaluation of LLM capabilities.

### Core Mechanism

The core intuition of RankLLM is that a model earns a competency score when it correctly answers a question, while a question's difficulty score increases when it challenges a model. RankLLM constructs a directed bipartite interaction graph between models and questions and performs damped bidirectional score propagation: solving a hard question carries more evidential weight for competency; failing an easy question contributes more weight to difficulty.

### Key Results

The framework evaluates 30 models on 35,550 questions across multiple domains. RankLLM achieves 90% agreement with human judgments and consistently outperforms strong baselines such as IRT.

### ICLR 2026 Status

The paper was published as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "077edbbd-4260-4104-9990-ed16648de4d8",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "722ccfab-4139-46e9-bfa8-04b11623b215",
  "toolUseResult": {
    "query": "RankLLM weighted ranking question difficulty ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016NivZnNk5nFEFUzMDU5KF4",
        "content": [
          {
            "title": "RANKLLM: WEIGHTED RANKING OF LLMS BY QUAN",
            "url": "https://openreview.net/pdf/c22aab26d0cee50994697242fa86488f0f24707d.pdf"
          },
          {
            "title": "(PDF) RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty",
            "url": "https://www.researchgate.net/publication/400812163_RankLLM_Weighted_Ranking_of_LLMs_by_Quantifying_Question_Difficulty"
          },
          {
            "title": "[2602.12424v1] RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty",
            "url": "https://arxiv.org/abs/2602.12424v1"
          },
          {
            "title": "[2602.12424] RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty",
            "url": "https://arxiv.org/abs/2602.12424"
          },
          {
            "title": "RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty | OpenReview",
            "url": "https://openreview.net/forum?id=jnX5GJIoYt"
          },
          {
            "title": "RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty",
            "url": "https://arxiv.org/html/2602.12424"
          }
        ]
      },
      "I found relevant information about RankLLM. Here's what the search reveals:\n\n## RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty\n\nRankLLM is a novel framework designed to quantify both question difficulty and model competency. RankLLM introduces difficulty as the primary criterion for differentiation, enabling a more fine-grained evaluation of LLM capabilities.\n\n### Core Mechanism\n\nThe core intuition of RankLLM is that a model earns a competency score when it correctly answers a question, while a question's difficulty score increases when it challenges a model. RankLLM constructs a directed bipartite interaction graph between models and questions and performs damped bidirectional score propagation: solving a hard question carries more evidential weight for competency; failing an easy question contributes more weight to difficulty.\n\n### Key Results\n\nThe framework evaluates 30 models on 35,550 questions across multiple domains. RankLLM achieves 90% agreement with human judgments and consistently outperforms strong baselines such as IRT.\n\n### ICLR 2026 Status\n\nThe paper was published as a conference paper at ICLR 2026."
    ],
    "durationSeconds": 5.715752356000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "077edbbd-4260-4104-9990-ed16648de4d8",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 18 · 2026-05-28T14:03:55.791Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01NNUBMhpMTcBJMd26Bi7VYY`</summary>

```json
{
  "query": "DCR data contamination correction LLM EMNLP 2025 ConStat NeurIPS 2024 JECS decontamination 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "722ccfab-4139-46e9-bfa8-04b11623b215",
  "isSidechain": false,
  "requestId": "req_011CbV6K6xcT5EsTf1aDHJ2D",
  "type": "assistant",
  "uuid": "4cf09209-26d2-400c-969d-59e43b97a9ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q19XhTEikgGzhbgRRqW2my",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 29207,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 732,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 29207,
          "cache_creation_input_tokens": 732,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 732
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

_source line 19 · 2026-05-28T14:04:05.296Z_

<details><summary>↩ Tool result · `toolu_01NNUBMhpMTcBJMd26Bi7VYY`</summary>

```text
Web search results for query: "DCR data contamination correction LLM EMNLP 2025 ConStat NeurIPS 2024 JECS decontamination 2026"

Links: [{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1173/"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/pdf/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/html/2507.11405"},{"title":"[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/abs/2507.11405"},{"title":"Data Contamination Can Cross Language Barriers","url":"https://arxiv.org/pdf/2406.13236"},{"title":"Generalization or Memorization: Data Contamination and Trustworthy   Evaluation for Large Language Models","url":"https://arxiv.org/pdf/2402.15938"},{"title":"Data Contamination Calibration for Black-box LLMs","url":"https://arxiv.org/pdf/2405.11930"}]

Links: [{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"ConStat: Performance-Based Contamination Detection in LLMs - YouTube","url":"https://www.youtube.com/watch?v=dgvU0jDFa0c"},{"title":"NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://neurips.cc/virtual/2024/poster/96266"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"},{"title":"Rethinking Benchmark and Contamination for Language Models with   Rephrased Samples","url":"https://arxiv.org/pdf/2311.04850"}]

Links: [{"title":"Decontamination services - Singapore - JECS","url":"https://jecs.com.sg/service/decontamination-services/"},{"title":"Home - JECS","url":"https://jecs.com.sg/"},{"title":"Selective Digestive Decontamination — Finding the Way Forward | New England Journal of Medicine","url":"https://www.nejm.org/doi/abs/10.1056/NEJMe2602823"},{"title":"Result conferences - JECS Trust","url":"https://www.jecstrust.org/news/479/421/0926-Shaping-10-Conference/d,ceramic_details_conferences"},{"title":"Patients undergo decontamination process after chemical emergency","url":"https://www.wsaz.com/2026/04/23/patients-undergo-decontamination-process-after-chemical-emergency/"},{"title":"Journal of The Electrochemical Society - ECS","url":"https://www.electrochem.org/publications/jes"},{"title":"Decontamination, Sterilization and Disinfection Quiz – 2026 – Study and Practice Guide - Decontamination, Sterilization and DisinfectioN - Stuvia","url":"https://www.stuvia.com/doc/10821785/decontamination-sterilization-and-disinfection-quiz-2026-study-and-practice-guide"},{"title":"Study Overview | About the Study | Japan Environment and Children's Study","url":"https://www.env.go.jp/chemi/ceh/en/about/outline.html"},{"title":"Journal of the European Ceramic Society | ScienceDirect.com by Elsevier","url":"https://www.sciencedirect.com/journal/journal-of-the-european-ceramic-society"},{"title":"jecs - Home","url":"https://www.jecstrust.org/"}]

Based on my web search results, I found information about the DCR and ConStat papers. However, the search for "JECS decontamination 2026" returned results about unrelated topics (a ceramic society journal, a decontamination services company, and a Japanese environmental health study), so there doesn't appear to be an academic paper with that specific combination of terms.

Here's what I found:

## DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)

The Data Contamination Risk (DCR) framework is a lightweight, interpretable pipeline designed to detect and quantify BDC (benchmark data contamination) risk across four granular levels: semantic, informational, data, and label, producing a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance. The framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, achieving within 4% average error across the three benchmarks compared to the uncontaminated baseline.

## ConStat: Performance-Based Contamination Detection (NeurIPS 2024)

ConStat is a statistical method that reliably detects and quantifies contamination by comparing performance between a primary and reference benchmark relative to a set of reference models. It proposes a novel definition of contamination as artificially inflated and non-generalizing benchmark performance, enabling detection of any model with performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.

## JECS and 2026

I could not find an academic paper related to "JECS decontamination 2026" in the context of LLM data contamination. The search results returned information about unrelated JECS organizations (the Journal of the European Ceramic Society and other entities), so this may not be an actual research publication or may use different terminology.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "4cf09209-26d2-400c-969d-59e43b97a9ae",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "82525050-6608-4937-9b69-dcf155aa97c0",
  "toolUseResult": {
    "query": "DCR data contamination correction LLM EMNLP 2025 ConStat NeurIPS 2024 JECS decontamination 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N251GVb2qjfkZ637XGu2aR",
        "content": [
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.1173/"
          },
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://arxiv.org/pdf/2507.11405"
          },
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://arxiv.org/html/2507.11405"
          },
          {
            "title": "[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://arxiv.org/abs/2507.11405"
          },
          {
            "title": "Data Contamination Can Cross Language Barriers",
            "url": "https://arxiv.org/pdf/2406.13236"
          },
          {
            "title": "Generalization or Memorization: Data Contamination and Trustworthy   Evaluation for Large Language Models",
            "url": "https://arxiv.org/pdf/2402.15938"
          },
          {
            "title": "Data Contamination Calibration for Black-box LLMs",
            "url": "https://arxiv.org/pdf/2405.11930"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_013wXwW98sCKrrTbSmSt3hS3",
        "content": [
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in LLMs - YouTube",
            "url": "https://www.youtube.com/watch?v=dgvU0jDFa0c"
          },
          {
            "title": "NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://neurips.cc/virtual/2024/poster/96266"
          },
          {
            "title": "When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/pdf/2601.19334"
          },
          {
            "title": "Rethinking Benchmark and Contamination for Language Models with   Rephrased Samples",
            "url": "https://arxiv.org/pdf/2311.04850"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_01EXFqHxMLiRa7dzGgieJzEj",
        "content": [
          {
            "title": "Decontamination services - Singapore - JECS",
            "url": "https://jecs.com.sg/service/decontamination-services/"
          },
          {
            "title": "Home - JECS",
            "url": "https://jecs.com.sg/"
          },
          {
            "title": "Selective Digestive Decontamination — Finding the Way Forward | New England Journal of Medicine",
            "url": "https://www.nejm.org/doi/abs/10.1056/NEJMe2602823"
          },
          {
            "title": "Result conferences - JECS Trust",
            "url": "https://www.jecstrust.org/news/479/421/0926-Shaping-10-Conference/d,ceramic_details_conferences"
          },
          {
            "title": "Patients undergo decontamination process after chemical emergency",
            "url": "https://www.wsaz.com/2026/04/23/patients-undergo-decontamination-process-after-chemical-emergency/"
          },
          {
            "title": "Journal of The Electrochemical Society - ECS",
            "url": "https://www.electrochem.org/publications/jes"
          },
          {
            "title": "Decontamination, Sterilization and Disinfection Quiz – 2026 – Study and Practice Guide - Decontamination, Sterilization and DisinfectioN - Stuvia",
            "url": "https://www.stuvia.com/doc/10821785/decontamination-sterilization-and-disinfection-quiz-2026-study-and-practice-guide"
          },
          {
            "title": "Study Overview | About the Study | Japan Environment and Children's Study",
            "url": "https://www.env.go.jp/chemi/ceh/en/about/outline.html"
          },
          {
            "title": "Journal of the European Ceramic Society | ScienceDirect.com by Elsevier",
            "url": "https://www.sciencedirect.com/journal/journal-of-the-european-ceramic-society"
          },
          {
            "title": "jecs - Home",
            "url": "https://www.jecstrust.org/"
          }
        ]
      },
      "Based on my web search results, I found information about the DCR and ConStat papers. However, the search for \"JECS decontamination 2026\" returned results about unrelated topics (a ceramic society journal, a decontamination services company, and a Japanese environmental health study), so there doesn't appear to be an academic paper with that specific combination of terms.\n\nHere's what I found:\n\n## DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025)\n\nThe Data Contamination Risk (DCR) framework is a lightweight, interpretable pipeline designed to detect and quantify BDC (benchmark data contamination) risk across four granular levels: semantic, informational, data, and label, producing a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance. The framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, achieving within 4% average error across the three benchmarks compared to the uncontaminated baseline.\n\n## ConStat: Performance-Based Contamination Detection (NeurIPS 2024)\n\nConStat is a statistical method that reliably detects and quantifies contamination by comparing performance between a primary and reference benchmark relative to a set of reference models. It proposes a novel definition of contamination as artificially inflated and non-generalizing benchmark performance, enabling detection of any model with performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.\n\n## JECS and 2026\n\nI could not find an academic paper related to \"JECS decontamination 2026\" in the context of LLM data contamination. The search results returned information about unrelated JECS organizations (the Journal of the European Ceramic Society and other entities), so this may not be an actual research publication or may use different terminology."
    ],
    "durationSeconds": 9.500728079,
    "searchCount": 3
  },
  "sourceToolAssistantUUID": "4cf09209-26d2-400c-969d-59e43b97a9ae",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "82525050-6608-4937-9b69-dcf155aa97c0",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate proposal on contamination-ability LLM decomposition",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Tool call

_source line 22 · 2026-05-28T14:04:08.738Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EYmf5NK68sqDEZYvC53eP3`</summary>

```json
{
  "query": "Wang Li Ko Zhang \"fragility of benchmark contamination detection\" reasoning models ICLR 2026 likelihood-based detection fails"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "82525050-6608-4937-9b69-dcf155aa97c0",
  "isSidechain": false,
  "requestId": "req_011CbV6L3aF32AT1jteekNDp",
  "type": "assistant",
  "uuid": "7986d0f5-9914-426d-a35b-09a7e2f2a2ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014Pw3ypgFXYdfWphMzy8SVU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1651,
      "cache_read_input_tokens": 29939,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1651,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 29939,
          "cache_creation_input_tokens": 1651,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1651
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

_source line 23 · 2026-05-28T14:04:17.460Z_

<details><summary>↩ Tool result · `toolu_01EYmf5NK68sqDEZYvC53eP3`</summary>

```text
Web search results for query: "Wang Li Ko Zhang "fragility of benchmark contamination detection" reasoning models ICLR 2026 likelihood-based detection fails"

Links: [{"title":"Carnegie Mellon at ICLR 2026 – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2026/04/20/carnegie-mellon-at-iclr-2026/"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"[PDF] On The Fragility of Benchmark Contamination Detection in Reasoning Models | Semantic Scholar","url":"https://www.semanticscholar.org/paper/On-The-Fragility-of-Benchmark-Contamination-in-Wang-Li/9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3"},{"title":"[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/abs/2510.02386"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/html/2510.02386v2"},{"title":"Published as a conference paper at ICLR 2026 CONTAMINATION DETECTION","url":"https://openreview.net/pdf?id=gk6OC3XIZW"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"}]

I found the paper you're looking for! The paper is titled "On The Fragility of Benchmark Contamination Detection in Reasoning Models" by Han Wang (University of Illinois Urbana-Champaign), Haoyu Li (University of Illinois Urbana-Champaign), Brian Ko (University of Washington), and Huan Zhang (CMU). It was presented at ICLR 2026.

The paper examines benchmark contamination—where evaluation benchmarks are incorporated into training data to yield inflated performance—and finds that evading contamination detections for large reasoning models (LRMs) is alarmingly easy.

Key findings include: When a base model evolves into an LRM via supervised fine-tuning (SFT) and reinforcement learning (RL), contamination during SFT can originally be identified by contamination detection methods, yet even brief GRPO training can markedly conceal contamination signals that most detection methods rely on. Further empirical experiments and theoretical analysis indicate that PPO style importance sampling and clipping objectives are the root cause of this detection concealment, indicating that a broad class of RL methods may inherently exhibit similar issues.

You can access the full paper on arXiv (2510.02386) or through OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7986d0f5-9914-426d-a35b-09a7e2f2a2ec",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "b08c9c70-70dd-4081-b6f2-ef9193ec4edb",
  "toolUseResult": {
    "query": "Wang Li Ko Zhang \"fragility of benchmark contamination detection\" reasoning models ICLR 2026 likelihood-based detection fails",
    "results": [
      {
        "tool_use_id": "srvtoolu_01N6EtwpvgnnQ6WW3zYejfuj",
        "content": [
          {
            "title": "Carnegie Mellon at ICLR 2026 – Machine Learning Blog | ML@CMU | Carnegie Mellon University",
            "url": "https://blog.ml.cmu.edu/2026/04/20/carnegie-mellon-at-iclr-2026/"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "[PDF] On The Fragility of Benchmark Contamination Detection in Reasoning Models | Semantic Scholar",
            "url": "https://www.semanticscholar.org/paper/On-The-Fragility-of-Benchmark-Contamination-in-Wang-Li/9a5bf5d3c7116cc4a104c06599fbcef2d1b5abf3"
          },
          {
            "title": "[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/abs/2510.02386"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/html/2510.02386v2"
          },
          {
            "title": "Published as a conference paper at ICLR 2026 CONTAMINATION DETECTION",
            "url": "https://openreview.net/pdf?id=gk6OC3XIZW"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"
          }
        ]
      },
      "I found the paper you're looking for! The paper is titled \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" by Han Wang (University of Illinois Urbana-Champaign), Haoyu Li (University of Illinois Urbana-Champaign), Brian Ko (University of Washington), and Huan Zhang (CMU). It was presented at ICLR 2026.\n\nThe paper examines benchmark contamination—where evaluation benchmarks are incorporated into training data to yield inflated performance—and finds that evading contamination detections for large reasoning models (LRMs) is alarmingly easy.\n\nKey findings include: When a base model evolves into an LRM via supervised fine-tuning (SFT) and reinforcement learning (RL), contamination during SFT can originally be identified by contamination detection methods, yet even brief GRPO training can markedly conceal contamination signals that most detection methods rely on. Further empirical experiments and theoretical analysis indicate that PPO style importance sampling and clipping objectives are the root cause of this detection concealment, indicating that a broad class of RL methods may inherently exhibit similar issues.\n\nYou can access the full paper on arXiv (2510.02386) or through OpenReview."
    ],
    "durationSeconds": 8.71681478,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7986d0f5-9914-426d-a35b-09a7e2f2a2ec",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 24 · 2026-05-28T14:04:20.119Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_013xSm2zwKLWqB6AVWGP6QWC`</summary>

```json
{
  "query": "\"Growing Pains\" extensible LLM benchmarking fixed parameter calibration IRT 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b08c9c70-70dd-4081-b6f2-ef9193ec4edb",
  "isSidechain": false,
  "requestId": "req_011CbV6LwLDk4L8QKpJoacQE",
  "type": "assistant",
  "uuid": "a2090225-aac6-4718-836e-272fa843536b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FzM3K2PpPFh7z4LPRaK3fE",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 829,
      "cache_read_input_tokens": 31590,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 829,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 31590,
          "cache_creation_input_tokens": 829,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 829
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

_source line 25 · 2026-05-28T14:04:27.922Z_

<details><summary>↩ Tool result · `toolu_013xSm2zwKLWqB6AVWGP6QWC`</summary>

```text
Web search results for query: ""Growing Pains" extensible LLM benchmarking fixed parameter calibration IRT 2026"

Links: [{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"Agent psychometrics: Task-level performance prediction in agentic coding benchmarks","url":"https://arxiv.org/pdf/2604.00594"},{"title":"Preprint. Accepted at the ICLR 2026 LIT Workshop","url":"https://arxiv.org/pdf/2602.09924"},{"title":"LLM Evaluation and Benchmarking 2026 | Zylos Research","url":"https://zylos.ai/research/2026-01-16-llm-evaluation-benchmarking"}]

I found the paper you're looking for! Here are the key details about "Growing Pains":

**Title:** Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration

**Core Contribution:** The paper proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.

**Key Features:**
- The approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.

**Use Cases:**
- For new-model evaluation, the framework tests only the anchor questions and uses the calibrated IRT model to infer performance over the larger historical pool, reducing the amount of inference required.
- For new-dataset integration, it calibrates the dataset into the existing evaluation suite and then uses already-estimated model scores to estimate how models would perform on the new items, avoiding expensive model runs.

**Evaluation Results:** In large-scale experiments on more than 400 models, the framework predicts full-evaluation performance within 2–3 percentage points using only 100 anchor questions per dataset, with Spearman ρ≥0.9 for ranking preservation.

Code is available at https://github.com/eliyahabba/growing-pains/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a2090225-aac6-4718-836e-272fa843536b",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "9c0eebaa-1841-41cd-a7f0-5b0f4d195ba2",
  "toolUseResult": {
    "query": "\"Growing Pains\" extensible LLM benchmarking fixed parameter calibration IRT 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Rq7h1rKTvLxPGaNj72XwTn",
        "content": [
          {
            "title": "Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration",
            "url": "https://arxiv.org/html/2604.12843"
          },
          {
            "title": "[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration",
            "url": "https://arxiv.org/abs/2604.12843"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/pdf/2511.04689"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/html/2511.04689"
          },
          {
            "title": "Agent psychometrics: Task-level performance prediction in agentic coding benchmarks",
            "url": "https://arxiv.org/pdf/2604.00594"
          },
          {
            "title": "Preprint. Accepted at the ICLR 2026 LIT Workshop",
            "url": "https://arxiv.org/pdf/2602.09924"
          },
          {
            "title": "LLM Evaluation and Benchmarking 2026 | Zylos Research",
            "url": "https://zylos.ai/research/2026-01-16-llm-evaluation-benchmarking"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details about \"Growing Pains\":\n\n**Title:** Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\n\n**Core Contribution:** The paper proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.\n\n**Key Features:**\n- The approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.\n\n**Use Cases:**\n- For new-model evaluation, the framework tests only the anchor questions and uses the calibrated IRT model to infer performance over the larger historical pool, reducing the amount of inference required.\n- For new-dataset integration, it calibrates the dataset into the existing evaluation suite and then uses already-estimated model scores to estimate how models would perform on the new items, avoiding expensive model runs.\n\n**Evaluation Results:** In large-scale experiments on more than 400 models, the framework predicts full-evaluation performance within 2–3 percentage points using only 100 anchor questions per dataset, with Spearman ρ≥0.9 for ranking preservation.\n\nCode is available at https://github.com/eliyahabba/growing-pains/."
    ],
    "durationSeconds": 7.796944823999991,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a2090225-aac6-4718-836e-272fa843536b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 26 · 2026-05-28T14:04:31.068Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019Vm8GFGAZBh2Biotnba72a`</summary>

```json
{
  "query": "MATH-Perturb benchmarking LLM math reasoning perturbations ICML 2025 MaSTer automated robustness evaluation mathematical reasoning 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9c0eebaa-1841-41cd-a7f0-5b0f4d195ba2",
  "isSidechain": false,
  "requestId": "req_011CbV6Mi4YBc5nhNQ4aJrMD",
  "type": "assistant",
  "uuid": "379f45f1-1ece-4fd3-b54d-c64922b78133",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01A3ctS7yuhaRah4G5tJ7FEq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 779,
      "cache_read_input_tokens": 32419,
      "output_tokens": 90,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 779,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 90,
          "cache_read_input_tokens": 32419,
          "cache_creation_input_tokens": 779,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 779
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

_source line 27 · 2026-05-28T14:04:37.381Z_

<details><summary>↩ Tool result · `toolu_019Vm8GFGAZBh2Biotnba72a`</summary>

```text
Web search results for query: "MATH-Perturb benchmarking LLM math reasoning perturbations ICML 2025 MaSTer automated robustness evaluation mathematical reasoning 2026"

Links: [{"title":"MATH-Perturb","url":"https://math-perturb.github.io/"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview","url":"https://openreview.net/forum?id=OZy70UggXr"},{"title":"GitHub - Kaffaljidhmah2/MATH-Perturb: Evaluation Code and Dataset for [ICML 2025] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://github.com/Kaffaljidhmah2/MATH-Perturb"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/math-perturb-benchmarking-llms-math-reasoning-abilities"},{"title":"[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/abs/2502.06453"},{"title":"BENCHMARKING LLMS' MATH REASONING ABILITIES ...","url":"https://openreview.net/pdf?id=M8OLGgYK7e"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard   Perturbations","url":"https://arxiv.org/pdf/2502.06453"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://proceedings.mlr.press/v267/huang25k.html"},{"title":"ICML Poster MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://icml.cc/virtual/2025/poster/45435"}]

Based on the search results, I found comprehensive information about MATH-Perturb and ICML 2025. However, the search didn't return specific results about "MaSTer" or "automated robustness evaluation" in relation to this work. Here's what I found:

## MATH-Perturb Overview

MATH-Perturb is a benchmark accepted at ICML 2025 that evaluates LLMs' math reasoning abilities against hard perturbations. The benchmark constructs MATH-P-Simple and MATH-P-Hard via simple and hard perturbations respectively, each consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset.

## Key Findings

The work addresses whether large language models' impressive performance on challenging mathematical reasoning tasks is achieved by true reasoning capability or memorization. While prior work has constructed mathematical benchmarks with simple perturbations that preserve underlying reasoning patterns, MATH-Perturb explores hard perturbations that fundamentally change the nature of the problem so that the original solution steps do not apply.

## Performance Results

Significant performance drops on MATH-P-Hard were observed across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%). The research raises concerns about a novel form of memorization where models blindly apply learned problem-solving skills without assessing their applicability to modified contexts, an issue amplified when using original problems for in-context learning.

Note: The search results did not contain specific information about "MaSTer" or detailed discussion of automated robustness evaluation methods as part of this research.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "379f45f1-1ece-4fd3-b54d-c64922b78133",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "1b01d17d-1e00-4a76-bc9c-d5158de49ea4",
  "toolUseResult": {
    "query": "MATH-Perturb benchmarking LLM math reasoning perturbations ICML 2025 MaSTer automated robustness evaluation mathematical reasoning 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01VKC3HHqeSdiRonjX29Brie",
        "content": [
          {
            "title": "MATH-Perturb",
            "url": "https://math-perturb.github.io/"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=OZy70UggXr"
          },
          {
            "title": "GitHub - Kaffaljidhmah2/MATH-Perturb: Evaluation Code and Dataset for [ICML 2025] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://github.com/Kaffaljidhmah2/MATH-Perturb"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | AI Research Paper Details",
            "url": "https://www.aimodels.fyi/papers/arxiv/math-perturb-benchmarking-llms-math-reasoning-abilities"
          },
          {
            "title": "[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://arxiv.org/abs/2502.06453"
          },
          {
            "title": "BENCHMARKING LLMS' MATH REASONING ABILITIES ...",
            "url": "https://openreview.net/pdf?id=M8OLGgYK7e"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard   Perturbations",
            "url": "https://arxiv.org/pdf/2502.06453"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations",
            "url": "https://proceedings.mlr.press/v267/huang25k.html"
          },
          {
            "title": "ICML Poster MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://icml.cc/virtual/2025/poster/45435"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about MATH-Perturb and ICML 2025. However, the search didn't return specific results about \"MaSTer\" or \"automated robustness evaluation\" in relation to this work. Here's what I found:\n\n## MATH-Perturb Overview\n\nMATH-Perturb is a benchmark accepted at ICML 2025 that evaluates LLMs' math reasoning abilities against hard perturbations. The benchmark constructs MATH-P-Simple and MATH-P-Hard via simple and hard perturbations respectively, each consisting of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset.\n\n## Key Findings\n\nThe work addresses whether large language models' impressive performance on challenging mathematical reasoning tasks is achieved by true reasoning capability or memorization. While prior work has constructed mathematical benchmarks with simple perturbations that preserve underlying reasoning patterns, MATH-Perturb explores hard perturbations that fundamentally change the nature of the problem so that the original solution steps do not apply.\n\n## Performance Results\n\nSignificant performance drops on MATH-P-Hard were observed across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%). The research raises concerns about a novel form of memorization where models blindly apply learned problem-solving skills without assessing their applicability to modified contexts, an issue amplified when using original problems for in-context learning.\n\nNote: The search results did not contain specific information about \"MaSTer\" or detailed discussion of automated robustness evaluation methods as part of this research."
    ],
    "durationSeconds": 6.309686566000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "379f45f1-1ece-4fd3-b54d-c64922b78133",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 28 · 2026-05-28T14:04:39.989Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YCkT2fpMAB964pGBJHnH5R`</summary>

```json
{
  "query": "MaSTer \"automated robustness evaluation\" mathematical reasoning adversarial rewrite pipeline 2026 arXiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1b01d17d-1e00-4a76-bc9c-d5158de49ea4",
  "isSidechain": false,
  "requestId": "req_011CbV6NQZ71xJ6v4Dnzu868",
  "type": "assistant",
  "uuid": "196dd575-b1fd-4e43-93a3-2ca08c68bb9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015Ea1RsnHmbgH9yEPBQHFxN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1046,
      "cache_read_input_tokens": 33198,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1046,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 33198,
          "cache_creation_input_tokens": 1046,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1046
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

_source line 29 · 2026-05-28T14:04:47.392Z_

<details><summary>↩ Tool result · `toolu_01YCkT2fpMAB964pGBJHnH5R`</summary>

```text
Web search results for query: "MaSTer "automated robustness evaluation" mathematical reasoning adversarial rewrite pipeline 2026 arXiv"

Links: [{"title":"[2506.05038] Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/abs/2506.05038"},{"title":"Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/html/2506.05038"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.04120"},{"title":"MSCR: Exploring the Vulnerability of LLMs' Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement","url":"https://arxiv.org/pdf/2511.08055"},{"title":"Automatic Robustness Stress Testing of LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/pdf/2506.05038"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v2"},{"title":"MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning","url":"https://arxiv.org/pdf/2510.06430"}]

I found the paper you're looking for! Here are the key details about MaSTer:

MaSTer (Math Stress Tester) is an automated framework inspired by software stress testing. MaSTer generates adversarial variants via a multi-round rewrite-verify loop, ensuring semantic consistency while successfully inducing model failure.

The paper addresses a significant limitation in existing approaches: existing robustness evaluations predominantly rely on hand-crafted templates or a limited set of perturbation rules, and consequently lack the adaptability to probe latent vulnerabilities unique to specific models and remain susceptible to data contamination.

Key features of MaSTer include:

- The framework establishes an automated adversarial loop comprising a rewriter, a verifier, and the target LLM, where the rewriter rewrites mathematical problems into variants while keeping the core meaning unchanged.

- The framework generates benchmark variants dynamically for each LLM, thus minimizing the risk of data contamination.

- Experiments on GSM8K, MATH-500, and broader benchmarks demonstrate that the framework is effective in evaluating the robustness of LLMs, and the adversarial variants synthesized by MaSTer serve as high-quality training data, significantly enhancing model robustness through fine-tuning.

The paper was published on arXiv on April 24, 2026 (arXiv ID: 2506.05038).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "196dd575-b1fd-4e43-93a3-2ca08c68bb9d",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "efaecee3-c99e-4f1d-9a2a-de3ebcf4bf81",
  "toolUseResult": {
    "query": "MaSTer \"automated robustness evaluation\" mathematical reasoning adversarial rewrite pipeline 2026 arXiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DPWHqSqzXyUAph7VWDSmeU",
        "content": [
          {
            "title": "[2506.05038] Toward Automated Robustness Evaluation of Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2506.05038"
          },
          {
            "title": "Toward Automated Robustness Evaluation of Mathematical Reasoning",
            "url": "https://arxiv.org/html/2506.05038"
          },
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2511.04120"
          },
          {
            "title": "MSCR: Exploring the Vulnerability of LLMs' Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement",
            "url": "https://arxiv.org/pdf/2511.08055"
          },
          {
            "title": "Automatic Robustness Stress Testing of LLMs as Mathematical Problem Solvers",
            "url": "https://arxiv.org/pdf/2506.05038"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833v2"
          },
          {
            "title": "MathRobust-LV: Evaluation of Large Language Models' Robustness to Linguistic Variations in Mathematical Reasoning",
            "url": "https://arxiv.org/pdf/2510.06430"
          }
        ]
      },
      "I found the paper you're looking for! Here are the key details about MaSTer:\n\nMaSTer (Math Stress Tester) is an automated framework inspired by software stress testing. MaSTer generates adversarial variants via a multi-round rewrite-verify loop, ensuring semantic consistency while successfully inducing model failure.\n\nThe paper addresses a significant limitation in existing approaches: existing robustness evaluations predominantly rely on hand-crafted templates or a limited set of perturbation rules, and consequently lack the adaptability to probe latent vulnerabilities unique to specific models and remain susceptible to data contamination.\n\nKey features of MaSTer include:\n\n- The framework establishes an automated adversarial loop comprising a rewriter, a verifier, and the target LLM, where the rewriter rewrites mathematical problems into variants while keeping the core meaning unchanged.\n\n- The framework generates benchmark variants dynamically for each LLM, thus minimizing the risk of data contamination.\n\n- Experiments on GSM8K, MATH-500, and broader benchmarks demonstrate that the framework is effective in evaluating the robustness of LLMs, and the adversarial variants synthesized by MaSTer serve as high-quality training data, significantly enhancing model robustness through fine-tuning.\n\nThe paper was published on arXiv on April 24, 2026 (arXiv ID: 2506.05038)."
    ],
    "durationSeconds": 7.393669151999988,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "196dd575-b1fd-4e43-93a3-2ca08c68bb9d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 30 · 2026-05-28T14:04:47.405Z_

```json
{
  "parentUuid": "efaecee3-c99e-4f1d-9a2a-de3ebcf4bf81",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "8cf32651-6a8f-47f9-a39a-59abd1eb4599",
  "timestamp": "2026-05-28T14:04:47.405Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 31 · 2026-05-28T14:04:50.687Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TAk6foX8RkpGeYRKwbG64g`</summary>

```json
{
  "query": "Shu Henson Luecht \"Deterministic Gated\" item response theory cheating item compromise Psychometrika 2013"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8cf32651-6a8f-47f9-a39a-59abd1eb4599",
  "isSidechain": false,
  "requestId": "req_011CbV6P9W1jqrzhYmfDPrQB",
  "type": "assistant",
  "uuid": "06c5a7a0-3c73-46f3-90ed-48fcf9fa1afd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01158R5uvy41T28kvhezF6sb",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 877,
      "cache_read_input_tokens": 34244,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 877,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 34244,
          "cache_creation_input_tokens": 877,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 877
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

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "06c5a7a0-3c73-46f3-90ed-48fcf9fa1afd",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate proposal on contamination-ability LLM decomposition",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Tool result

_source line 34 · 2026-05-28T14:04:57.175Z_

<details><summary>↩ Tool result · `toolu_01TAk6foX8RkpGeYRKwbG64g`</summary>

```text
Web search results for query: "Shu Henson Luecht "Deterministic Gated" item response theory cheating item compromise Psychometrika 2013"

Links: [{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11336-012-9311-3"},{"title":"Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/25106396/"},{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Cambridge Core","url":"https://www.cambridge.org/core/journals/psychometrika/article/abs/using-deterministic-gated-item-response-theory-model-to-detect-test-cheating-due-to-item-compromise/34FE98C0FA7367881713D0019619E53E"},{"title":"(PDF) Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise","url":"https://www.researchgate.net/publication/257678777_Using_Deterministic_Gated_Item_Response_Theory_Model_to_Detect_Test_Cheating_due_to_Item_Compromise"},{"title":"Item pre-knowledge true prevalence in clinical anatomy - application of gated item response theory model","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6659220/"},{"title":"Combining Item Response Theory and Diagnostic Classification Models: A Psychometric Model for Scaling Ability and Diagnosing Misconceptions | Psychometrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11336-013-9350-4"}]

I found the article you're looking for! Here are the key details:

The article "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise" was published in Psychometrika in 2013 by Shu, Z., Henson, R., and Luecht, R. The full citation is: Psychometrika 78, 481–497 (2013).

The Deterministic, Gated Item Response Theory Model (DGM) is proposed to identify cheaters who obtain significant score gain on tests due to item exposure/compromise by conditioning on the item status (exposed or unexposed items). A "gated" function is introduced to decompose the observed examinees' performance into two distributions (the true ability distribution determined by examinees' true ability and the cheating distribution determined by examinees' cheating ability).

You can access the full article at: https://link.springer.com/article/10.1007/s11336-012-9311-3


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06c5a7a0-3c73-46f3-90ed-48fcf9fa1afd",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "e56da15c-65a5-47d1-a358-3b0743954841",
  "toolUseResult": {
    "query": "Shu Henson Luecht \"Deterministic Gated\" item response theory cheating item compromise Psychometrika 2013",
    "results": [
      {
        "tool_use_id": "srvtoolu_015mEkL1hdZbrLiCrPLCsfGc",
        "content": [
          {
            "title": "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11336-012-9311-3"
          },
          {
            "title": "Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/25106396/"
          },
          {
            "title": "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Cambridge Core",
            "url": "https://www.cambridge.org/core/journals/psychometrika/article/abs/using-deterministic-gated-item-response-theory-model-to-detect-test-cheating-due-to-item-compromise/34FE98C0FA7367881713D0019619E53E"
          },
          {
            "title": "(PDF) Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise",
            "url": "https://www.researchgate.net/publication/257678777_Using_Deterministic_Gated_Item_Response_Theory_Model_to_Detect_Test_Cheating_due_to_Item_Compromise"
          },
          {
            "title": "Item pre-knowledge true prevalence in clinical anatomy - application of gated item response theory model",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6659220/"
          },
          {
            "title": "Combining Item Response Theory and Diagnostic Classification Models: A Psychometric Model for Scaling Ability and Diagnosing Misconceptions | Psychometrika | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11336-013-9350-4"
          }
        ]
      },
      "I found the article you're looking for! Here are the key details:\n\nThe article \"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\" was published in Psychometrika in 2013 by Shu, Z., Henson, R., and Luecht, R. The full citation is: Psychometrika 78, 481–497 (2013).\n\nThe Deterministic, Gated Item Response Theory Model (DGM) is proposed to identify cheaters who obtain significant score gain on tests due to item exposure/compromise by conditioning on the item status (exposed or unexposed items). A \"gated\" function is introduced to decompose the observed examinees' performance into two distributions (the true ability distribution determined by examinees' true ability and the cheating distribution determined by examinees' cheating ability).\n\nYou can access the full article at: https://link.springer.com/article/10.1007/s11336-012-9311-3"
    ],
    "durationSeconds": 6.481594999000008,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "06c5a7a0-3c73-46f3-90ed-48fcf9fa1afd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 35 · 2026-05-28T14:04:59.685Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012aMr2U1PHaFjyzH9srRyHJ`</summary>

```json
{
  "query": "joint IRT contamination ability decomposition LLM benchmark paired adversarial items 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e56da15c-65a5-47d1-a358-3b0743954841",
  "isSidechain": false,
  "requestId": "req_011CbV6PsAXui3QHFF4T4n4M",
  "type": "assistant",
  "uuid": "7a973b60-d18d-4b19-aa7e-f07a60a48afd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Nv87sMb5w8RnaUb5PNySRC",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 826,
      "cache_read_input_tokens": 35121,
      "output_tokens": 74,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 826,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 74,
          "cache_read_input_tokens": 35121,
          "cache_creation_input_tokens": 826,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 826
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

_source line 36 · 2026-05-28T14:05:07.620Z_

<details><summary>↩ Tool result · `toolu_012aMr2U1PHaFjyzH9srRyHJ`</summary>

```text
Web search results for query: "joint IRT contamination ability decomposition LLM benchmark paired adversarial items 2025 2026"

Links: [{"title":"Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/html/2605.21543"},{"title":"[2605.21543] Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/abs/2605.21543"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v3"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"},{"title":"Benchmarking LLMs for Unit Test Generation from Real-World Functions","url":"https://arxiv.org/pdf/2508.00408"},{"title":"Towards Contamination Resistant Benchmarks","url":"https://arxiv.org/pdf/2505.08389"},{"title":"Rethinking Benchmark and Contamination for Language Models with","url":"https://arxiv.org/pdf/2311.04850"},{"title":"JE-IRT: A Geometric Lens on LLM Abilities through Joint ...","url":"https://www.arxiv.org/pdf/2509.22888"}]

Links: [{"title":"AutoAdvExBench: Benchmarking Autonomous Exploitation of Adversarial Example Defenses | OpenReview","url":"https://openreview.net/forum?id=FJKnru1xUF"},{"title":"Benchmarking Misuse Mitigation Against Covert Adversaries","url":"https://arxiv.org/html/2506.06414v1"},{"title":"ai-benchmark/report_adversarial_stats.py at main · succinctlabs/ai-benchmark","url":"https://github.com/succinctlabs/ai-benchmark/blob/main/report_adversarial_stats.py"},{"title":"A Benchmark for Evaluating Outcome-Driven Constraint ...","url":"https://arxiv.org/pdf/2512.20798"},{"title":"Adversarial AI Digest — January 2026","url":"https://medium.com/ai-security-hub/adversarial-ai-digest-january-2026-e6bf7abf88e6"},{"title":"AutoAdvExBench: Benchmarking autonomous exploitation of adversarial example defenses | Request PDF","url":"https://www.researchgate.net/publication/389580278_AutoAdvExBench_Benchmarking_autonomous_exploitation_of_adversarial_example_defenses"},{"title":"TeleAI-Safety: A comprehensive LLM jailbreaking benchmark towards attacks,","url":"https://arxiv.org/pdf/2512.05485"},{"title":"AutoAdvExBench: Benchmarking autonomous exploitation of adversarial   example defenses","url":"https://arxiv.org/pdf/2503.01811"}]

Based on my web search results, I found several relevant papers addressing different aspects of your query:

## Joint IRT and Contamination

A recent paper "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" (published January 16, 2026) presents PSN-IRT, which outperforms previous approaches in both parameter estimation accuracy and reliability. The work addresses how LLM benchmarks exhibit data contamination in numerous items, compromising their reliability.

Additionally, another work called JE-IRT evaluates recent LLMs such as Qwen3-30B-A3B (Qwen Team, 2025) and remains effective when onboarding up-to-date models.

## Joint Decontamination

A paper titled "Provable Joint Decontamination for Benchmarking Multiple Large Language Models" proposes Joint Envelope Conformal Selection (JECS), a conformal procedure that enables global contamination rate (GCR) control.

## Paired Adversarial Items

Regarding paired adversarial benchmarks, the MTJ-Pro benchmark includes paired jailbreak and benign dialogues, together with two deception-oriented metrics, MSR and ARC.

These papers collectively address themes of IRT-based ability decomposition, contamination analysis, and adversarial evaluation in LLM benchmarking from 2025-2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a973b60-d18d-4b19-aa7e-f07a60a48afd",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "22dc6cbf-577a-49d5-b3c6-8b2506a00591",
  "toolUseResult": {
    "query": "joint IRT contamination ability decomposition LLM benchmark paired adversarial items 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PXRmVg7kz18vjN99dBWuc1",
        "content": [
          {
            "title": "Provable Joint Decontamination for Benchmarking Multiple Large Language Models",
            "url": "https://arxiv.org/html/2605.21543"
          },
          {
            "title": "[2605.21543] Provable Joint Decontamination for Benchmarking Multiple Large Language Models",
            "url": "https://arxiv.org/abs/2605.21543"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v3"
          },
          {
            "title": "When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/pdf/2601.19334"
          },
          {
            "title": "Benchmarking LLMs for Unit Test Generation from Real-World Functions",
            "url": "https://arxiv.org/pdf/2508.00408"
          },
          {
            "title": "Towards Contamination Resistant Benchmarks",
            "url": "https://arxiv.org/pdf/2505.08389"
          },
          {
            "title": "Rethinking Benchmark and Contamination for Language Models with",
            "url": "https://arxiv.org/pdf/2311.04850"
          },
          {
            "title": "JE-IRT: A Geometric Lens on LLM Abilities through Joint ...",
            "url": "https://www.arxiv.org/pdf/2509.22888"
          }
        ]
      },
      {
        "tool_use_id": "srvtoolu_01PrQaKgjJVcHF3pvFk2swSF",
        "content": [
          {
            "title": "AutoAdvExBench: Benchmarking Autonomous Exploitation of Adversarial Example Defenses | OpenReview",
            "url": "https://openreview.net/forum?id=FJKnru1xUF"
          },
          {
            "title": "Benchmarking Misuse Mitigation Against Covert Adversaries",
            "url": "https://arxiv.org/html/2506.06414v1"
          },
          {
            "title": "ai-benchmark/report_adversarial_stats.py at main · succinctlabs/ai-benchmark",
            "url": "https://github.com/succinctlabs/ai-benchmark/blob/main/report_adversarial_stats.py"
          },
          {
            "title": "A Benchmark for Evaluating Outcome-Driven Constraint ...",
            "url": "https://arxiv.org/pdf/2512.20798"
          },
          {
            "title": "Adversarial AI Digest — January 2026",
            "url": "https://medium.com/ai-security-hub/adversarial-ai-digest-january-2026-e6bf7abf88e6"
          },
          {
            "title": "AutoAdvExBench: Benchmarking autonomous exploitation of adversarial example defenses | Request PDF",
            "url": "https://www.researchgate.net/publication/389580278_AutoAdvExBench_Benchmarking_autonomous_exploitation_of_adversarial_example_defenses"
          },
          {
            "title": "TeleAI-Safety: A comprehensive LLM jailbreaking benchmark towards attacks,",
            "url": "https://arxiv.org/pdf/2512.05485"
          },
          {
            "title": "AutoAdvExBench: Benchmarking autonomous exploitation of adversarial   example defenses",
            "url": "https://arxiv.org/pdf/2503.01811"
          }
        ]
      },
      "Based on my web search results, I found several relevant papers addressing different aspects of your query:\n\n## Joint IRT and Contamination\n\nA recent paper \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\" (published January 16, 2026) presents PSN-IRT, which outperforms previous approaches in both parameter estimation accuracy and reliability. The work addresses how LLM benchmarks exhibit data contamination in numerous items, compromising their reliability.\n\nAdditionally, another work called JE-IRT evaluates recent LLMs such as Qwen3-30B-A3B (Qwen Team, 2025) and remains effective when onboarding up-to-date models.\n\n## Joint Decontamination\n\nA paper titled \"Provable Joint Decontamination for Benchmarking Multiple Large Language Models\" proposes Joint Envelope Conformal Selection (JECS), a conformal procedure that enables global contamination rate (GCR) control.\n\n## Paired Adversarial Items\n\nRegarding paired adversarial benchmarks, the MTJ-Pro benchmark includes paired jailbreak and benign dialogues, together with two deception-oriented metrics, MSR and ARC.\n\nThese papers collectively address themes of IRT-based ability decomposition, contamination analysis, and adversarial evaluation in LLM benchmarking from 2025-2026."
    ],
    "durationSeconds": 7.928682795,
    "searchCount": 2
  },
  "sourceToolAssistantUUID": "7a973b60-d18d-4b19-aa7e-f07a60a48afd",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 37 · 2026-05-28T14:05:10.244Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01P8hJ3FMGbMnEt1uwc75mHs`</summary>

```json
{
  "query": "JECS \"joint envelope conformal selection\" decontamination LLM benchmark arXiv 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "22dc6cbf-577a-49d5-b3c6-8b2506a00591",
  "isSidechain": false,
  "requestId": "req_011CbV6QdnPqiRSrMxKXjJF1",
  "type": "assistant",
  "uuid": "5304cf74-cec6-47aa-a02b-a6a21eb93523",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XG3Edp3kMzyZ6fiQL22URU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1177,
      "cache_read_input_tokens": 35947,
      "output_tokens": 75,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1177,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 75,
          "cache_read_input_tokens": 35947,
          "cache_creation_input_tokens": 1177,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1177
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

_source line 38 · 2026-05-28T14:05:16.972Z_

<details><summary>↩ Tool result · `toolu_01P8hJ3FMGbMnEt1uwc75mHs`</summary>

```text
Web search results for query: "JECS "joint envelope conformal selection" decontamination LLM benchmark arXiv 2026"

Links: [{"title":"[2605.21543] Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/abs/2605.21543"},{"title":"Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/html/2605.21543"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"},{"title":"An Expert-grounded benchmark of General Purpose LLMs in LCA","url":"https://arxiv.org/pdf/2510.19886"},{"title":"Rethinking Benchmark and Contamination for Language Models with","url":"https://arxiv.org/pdf/2311.04850"}]

Based on the search results, I found the paper you're looking for:

Joint Envelope Conformal Selection (JECS) is a conformal procedure that formalizes multi-model benchmark decontamination as a joint selection problem and enables global contamination rate (GCR) control under stated assumptions.

JECS computes per-model conformal p-values, aggregates them by the per-item maximum, and reconstructs a conservative envelope of the max-p null distribution from right-tail observations above a data-driven threshold. By applying the adaptive Benjamini-Hochberg (BH) procedure to the envelope-rescaled values, the method selects a benchmark with provable GCR control.

The paper addresses benchmark data contamination, a central challenge in LLM evaluation where evaluation examples appear in the training data of one or more audited models, causing reported performance to be inflated and cross-model comparisons to become unreliable.

The paper is available on arXiv as [2605.21543](https://arxiv.org/abs/2605.21543): "Provable Joint Decontamination for Benchmarking Multiple Large Language Models"


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "5304cf74-cec6-47aa-a02b-a6a21eb93523",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "10e5d945-3106-4519-b576-1a399465a11f",
  "toolUseResult": {
    "query": "JECS \"joint envelope conformal selection\" decontamination LLM benchmark arXiv 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01QLuCU95YrbGQvoAWiefFd7",
        "content": [
          {
            "title": "[2605.21543] Provable Joint Decontamination for Benchmarking Multiple Large Language Models",
            "url": "https://arxiv.org/abs/2605.21543"
          },
          {
            "title": "Provable Joint Decontamination for Benchmarking Multiple Large Language Models",
            "url": "https://arxiv.org/html/2605.21543"
          },
          {
            "title": "When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/pdf/2601.19334"
          },
          {
            "title": "An Expert-grounded benchmark of General Purpose LLMs in LCA",
            "url": "https://arxiv.org/pdf/2510.19886"
          },
          {
            "title": "Rethinking Benchmark and Contamination for Language Models with",
            "url": "https://arxiv.org/pdf/2311.04850"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nJoint Envelope Conformal Selection (JECS) is a conformal procedure that formalizes multi-model benchmark decontamination as a joint selection problem and enables global contamination rate (GCR) control under stated assumptions.\n\nJECS computes per-model conformal p-values, aggregates them by the per-item maximum, and reconstructs a conservative envelope of the max-p null distribution from right-tail observations above a data-driven threshold. By applying the adaptive Benjamini-Hochberg (BH) procedure to the envelope-rescaled values, the method selects a benchmark with provable GCR control.\n\nThe paper addresses benchmark data contamination, a central challenge in LLM evaluation where evaluation examples appear in the training data of one or more audited models, causing reported performance to be inflated and cross-model comparisons to become unreliable.\n\nThe paper is available on arXiv as [2605.21543](https://arxiv.org/abs/2605.21543): \"Provable Joint Decontamination for Benchmarking Multiple Large Language Models\""
    ],
    "durationSeconds": 6.7205815360000125,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "5304cf74-cec6-47aa-a02b-a6a21eb93523",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 39 · 2026-05-28T14:05:20.154Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SWizTg6Bmdnv97FXZBp8eW`</summary>

```json
{
  "query": "IRT gated model contamination LLM ability estimation psychometric two-stage calibration decontamination 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "10e5d945-3106-4519-b576-1a399465a11f",
  "isSidechain": false,
  "requestId": "req_011CbV6RKu9TWWizcsHQdbta",
  "type": "assistant",
  "uuid": "3baa9e11-d81a-411d-98df-94a24a0e09d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01S77Z12GavSHGkERYjekfu6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 602,
      "cache_read_input_tokens": 37124,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 602,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 37124,
          "cache_creation_input_tokens": 602,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 602
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

_source line 40 · 2026-05-28T14:05:29.697Z_

<details><summary>↩ Tool result · `toolu_01SWizTg6Bmdnv97FXZBp8eW`</summary>

```text
Web search results for query: "IRT gated model contamination LLM ability estimation psychometric two-stage calibration decontamination 2025 2026"

Links: [{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"[2510.07175] Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/abs/2510.07175"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"}]

Based on the search results, I found several highly relevant papers addressing your research interests:

## Key Findings

### 1. **IRT-based Adaptive Testing for LLM Evaluation**

A computerized adaptive testing (CAT) framework grounded in item response theory (IRT) has been proposed for efficient assessment of standardized medical knowledge in LLMs. The study comprises a two-phase design with a Monte Carlo simulation to identify optimal CAT configurations and an empirical evaluation of 38 LLMs, where models completed both the full item bank and an adaptive test that dynamically selected items based on real-time ability estimates.

### 2. **Data Contamination in Psychometric Evaluations**

A framework to systematically measure data contamination in psychometric evaluations of LLMs evaluates three aspects: (1) item memorization, (2) evaluation memorization, and (3) target score matching. Evidence shows that popular inventories such as the Big Five Inventory (BFI-44) and Portrait Values Questionnaire (PVQ-40) exhibit strong contamination.

### 3. **IRT-based Ability Estimation vs. Static Benchmarks**

ATLAS first calibrates benchmark items using three-parameter logistic (3PL) IRT models to estimate item difficulty, discrimination, and guessing parameters, then dynamically selects items with maximum Fisher information for each model's current estimated ability, terminating when precision thresholds are reached. IRT-based ability estimates provide form-invariant, uncertainty-aware alternatives that adjust for item difficulty and discrimination, addressing issues with form-dependence, nonlinear scaling, and contamination sensitivity.

### 4. **Inference-Time Decontamination**

DeconIEP is a decontamination framework that operates entirely during evaluation by applying small, bounded perturbations in the input embedding space, with a relatively less-contaminated reference model guiding an instance-adaptive perturbation generator.

These papers from 2025-2026 directly address the intersection of IRT methodology, contamination detection, two-stage calibration approaches, and psychometric evaluation of LLMs.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3baa9e11-d81a-411d-98df-94a24a0e09d7",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "5ab35981-9cfa-4539-9b1a-0cbfef69934f",
  "toolUseResult": {
    "query": "IRT gated model contamination LLM ability estimation psychometric two-stage calibration decontamination 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_0112YnARE1SWzH2AtmWhKAgw",
        "content": [
          {
            "title": "Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking",
            "url": "https://arxiv.org/pdf/2603.23506"
          },
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/pdf/2510.07175"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "[2510.07175] Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/abs/2510.07175"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/html/2511.04689"
          },
          {
            "title": "When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/pdf/2601.19334"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/pdf/2511.04689"
          }
        ]
      },
      "Based on the search results, I found several highly relevant papers addressing your research interests:\n\n## Key Findings\n\n### 1. **IRT-based Adaptive Testing for LLM Evaluation**\n\nA computerized adaptive testing (CAT) framework grounded in item response theory (IRT) has been proposed for efficient assessment of standardized medical knowledge in LLMs. The study comprises a two-phase design with a Monte Carlo simulation to identify optimal CAT configurations and an empirical evaluation of 38 LLMs, where models completed both the full item bank and an adaptive test that dynamically selected items based on real-time ability estimates.\n\n### 2. **Data Contamination in Psychometric Evaluations**\n\nA framework to systematically measure data contamination in psychometric evaluations of LLMs evaluates three aspects: (1) item memorization, (2) evaluation memorization, and (3) target score matching. Evidence shows that popular inventories such as the Big Five Inventory (BFI-44) and Portrait Values Questionnaire (PVQ-40) exhibit strong contamination.\n\n### 3. **IRT-based Ability Estimation vs. Static Benchmarks**\n\nATLAS first calibrates benchmark items using three-parameter logistic (3PL) IRT models to estimate item difficulty, discrimination, and guessing parameters, then dynamically selects items with maximum Fisher information for each model's current estimated ability, terminating when precision thresholds are reached. IRT-based ability estimates provide form-invariant, uncertainty-aware alternatives that adjust for item difficulty and discrimination, addressing issues with form-dependence, nonlinear scaling, and contamination sensitivity.\n\n### 4. **Inference-Time Decontamination**\n\nDeconIEP is a decontamination framework that operates entirely during evaluation by applying small, bounded perturbations in the input embedding space, with a relatively less-contaminated reference model guiding an instance-adaptive perturbation generator.\n\nThese papers from 2025-2026 directly address the intersection of IRT methodology, contamination detection, two-stage calibration approaches, and psychometric evaluation of LLMs."
    ],
    "durationSeconds": 9.537596292000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3baa9e11-d81a-411d-98df-94a24a0e09d7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 41 · 2026-05-28T14:05:33.704Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me also check one more important thing - whether there's any existing work that already does exactly what this proposal is suggesting (IRT-based contamination-ability decomposition with paired items).
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ab35981-9cfa-4539-9b1a-0cbfef69934f",
  "isSidechain": false,
  "requestId": "req_011CbV6SGEukBAkVJap2V1mB",
  "type": "assistant",
  "uuid": "b50a0716-9079-4ac8-b06b-60ab57225664",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AYpvJETof5sv13MvYczyD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 37726,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 37726,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 936
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

_source line 42 · 2026-05-28T14:05:34.702Z_

Let me do one more targeted search to check for the most directly competing work.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b50a0716-9079-4ac8-b06b-60ab57225664",
  "isSidechain": false,
  "requestId": "req_011CbV6SGEukBAkVJap2V1mB",
  "type": "assistant",
  "uuid": "d222e935-f701-43f7-b8d6-c6f989b7424a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AYpvJETof5sv13MvYczyD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 37726,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 37726,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 936
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

_source line 43 · 2026-05-28T14:05:35.025Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01BKaPDecJbZ8FkvADK7vSQZ`</summary>

```json
{
  "query": "\"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" arXiv 2510.07175 IRT contamination"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d222e935-f701-43f7-b8d6-c6f989b7424a",
  "isSidechain": false,
  "requestId": "req_011CbV6SGEukBAkVJap2V1mB",
  "type": "assistant",
  "uuid": "1b21f292-debc-496e-a44a-dc7f73994b4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014AYpvJETof5sv13MvYczyD",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 936,
      "cache_read_input_tokens": 37726,
      "output_tokens": 157,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 936,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 157,
          "cache_read_input_tokens": 37726,
          "cache_creation_input_tokens": 936,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 936
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
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "1b21f292-debc-496e-a44a-dc7f73994b4a",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Runtime record

_source line 45_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate proposal on contamination-ability LLM decomposition",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Tool result

_source line 46 · 2026-05-28T14:05:41.874Z_

<details><summary>↩ Tool result · `toolu_01BKaPDecJbZ8FkvADK7vSQZ`</summary>

```text
Web search results for query: ""Quantifying Data Contamination in Psychometric Evaluations of LLMs" arXiv 2510.07175 IRT contamination"

Links: [{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"},{"title":"[2510.07175] Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/abs/2510.07175"},{"title":"Computation and Language 2025","url":"https://arxiv.org/list/cs.CL/2025?skip=13625&show=50"},{"title":"Machine Learning Oct 2025","url":"https://arxiv.org/list/cs.LG/2025-10?skip=3475&show=50"},{"title":"Measure what Matters: Psychometric Evaluation of AI with Situational Judgment Tests","url":"https://arxiv.org/html/2510.22170"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs - ACL Anthology","url":"https://aclanthology.org/2026.findings-eacl.319/"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/pdf/2507.11405"}]

I found the paper you were searching for. Here's what I found:

## Overview

The paper "Quantifying Data Contamination in Psychometric Evaluations of LLMs" is authored by Jongwook Han, Woojung Song, Jonggeun Lee, and Yohan Jo (arXiv:2510.07175).

## Research Focus

The paper applies psychometric questionnaires to Large Language Models (LLMs) to assess high-level psychological constructs such as values, personality, moral foundations, and dark traits. Although prior work has raised concerns about possible data contamination from psychometric inventories, which may threaten the reliability of such evaluations, there has been no systematic attempt to quantify the extent of this contamination.

## Framework

The framework covers three aspects: (1) item memorization (direct exposure to inventory items), (2) evaluation memorization (familiarity with scoring protocols), and (3) target score matching (the ability to steer toward a desired score).

## Psychometric Inventories Tested

The framework was applied to multiple model families and widely used inventories, including the Big Five Inventory (BFI-44), PVQ, Moral Foundations Questionnaire (MFQ), and the Short Dark Triad (SD-3).

## Publication Status

The paper was accepted to EACL 2026 Findings.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1b21f292-debc-496e-a44a-dc7f73994b4a",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "335a282d-9b08-4357-b187-6100e208a475",
  "toolUseResult": {
    "query": "\"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" arXiv 2510.07175 IRT contamination",
    "results": [
      {
        "tool_use_id": "srvtoolu_01An1parRkv21qm4LqYiuZrG",
        "content": [
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/pdf/2510.07175"
          },
          {
            "title": "[2510.07175] Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/abs/2510.07175"
          },
          {
            "title": "Computation and Language 2025",
            "url": "https://arxiv.org/list/cs.CL/2025?skip=13625&show=50"
          },
          {
            "title": "Machine Learning Oct 2025",
            "url": "https://arxiv.org/list/cs.LG/2025-10?skip=3475&show=50"
          },
          {
            "title": "Measure what Matters: Psychometric Evaluation of AI with Situational Judgment Tests",
            "url": "https://arxiv.org/html/2510.22170"
          },
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs - ACL Anthology",
            "url": "https://aclanthology.org/2026.findings-eacl.319/"
          },
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://arxiv.org/pdf/2507.11405"
          }
        ]
      },
      "I found the paper you were searching for. Here's what I found:\n\n## Overview\n\nThe paper \"Quantifying Data Contamination in Psychometric Evaluations of LLMs\" is authored by Jongwook Han, Woojung Song, Jonggeun Lee, and Yohan Jo (arXiv:2510.07175).\n\n## Research Focus\n\nThe paper applies psychometric questionnaires to Large Language Models (LLMs) to assess high-level psychological constructs such as values, personality, moral foundations, and dark traits. Although prior work has raised concerns about possible data contamination from psychometric inventories, which may threaten the reliability of such evaluations, there has been no systematic attempt to quantify the extent of this contamination.\n\n## Framework\n\nThe framework covers three aspects: (1) item memorization (direct exposure to inventory items), (2) evaluation memorization (familiarity with scoring protocols), and (3) target score matching (the ability to steer toward a desired score).\n\n## Psychometric Inventories Tested\n\nThe framework was applied to multiple model families and widely used inventories, including the Big Five Inventory (BFI-44), PVQ, Moral Foundations Questionnaire (MFQ), and the Short Dark Triad (SD-3).\n\n## Publication Status\n\nThe paper was accepted to EACL 2026 Findings."
    ],
    "durationSeconds": 6.83941056400002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "1b21f292-debc-496e-a44a-dc7f73994b4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 47 · 2026-05-28T14:05:44.567Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WJvKz9JbRv9yevAMNDQ1G6`</summary>

```json
{
  "query": "RIDE difficulty evolving perturbation item response theory mathematical reasoning IRT RL rewriting arXiv 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "335a282d-9b08-4357-b187-6100e208a475",
  "isSidechain": false,
  "requestId": "req_011CbV6TAGmE3o5BNKbaW5UW",
  "type": "assistant",
  "uuid": "f03635bc-f044-41fc-8b3f-eb8e009644bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XnHcd7kCmvGfpeHCCgUcRT",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 839,
      "cache_read_input_tokens": 38662,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 839,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 38662,
          "cache_creation_input_tokens": 839,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 839
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

_source line 48 · 2026-05-28T14:05:51.393Z_

<details><summary>↩ Tool result · `toolu_01WJvKz9JbRv9yevAMNDQ1G6`</summary>

```text
Web search results for query: "RIDE difficulty evolving perturbation item response theory mathematical reasoning IRT RL rewriting arXiv 2025"

Links: [{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/html/2511.04120"},{"title":"[2511.04120] RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/abs/2511.04120"},{"title":"RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ITEM ...","url":"https://openreview.net/pdf/d5ed0f963c21d7ed1a8a3c452c9d81b161061351.pdf"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response ...","url":"https://arxiv.org/pdf/2511.04120"},{"title":"RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ...","url":"https://openreview.net/pdf?id=PPkzchpdNK"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning | OpenReview","url":"https://openreview.net/forum?id=PPkzchpdNK"},{"title":"DeepMath-103K: A Large-Scale, Challenging, Decontaminated, and Verifiable Mathematical Dataset for Advancing Reasoning | Request PDF","url":"https://www.researchgate.net/publication/392086521_DeepMath-103K_A_Large-Scale_Challenging_Decontaminated_and_Verifiable_Mathematical_Dataset_for_Advancing_Reasoning"}]

I found the paper you're looking for! Here's what I discovered:

## RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning

RIDE is a novel adversarial question-rewriting framework that leverages Item Response Theory (IRT) to rigorously measure question difficulty and to generate intrinsically more challenging, well-posed variations of mathematical problems.

### Key Motivation
Large language models achieve high performance on mathematical reasoning, but these results can be inflated by training data leakage or superficial pattern matching rather than genuine reasoning, so an adversarial perturbation-based evaluation is needed to measure true mathematical reasoning ability.

### Methodology
The framework leverages IRT to measure question difficulty, employs 35 LLMs to simulate students and build a difficulty ranker from their responses, which provides a reward signal during reinforcement learning and guides a question-rewriting model to reformulate existing questions across difficulty levels.

### Advantages Over Prior Work
Unlike rule-based methods, the approach adapts a reinforcement learning-based rewriting approach to generate perturbations, producing better-formed data, avoiding unsolvable or multiple-solution cases, and increasing unpredictability.

### Resources
The paper releases a question rewriting model (RIDE-8B), two rewritten competition-level benchmarks (RIDE-AIME and RIDE-AMC), and a training dataset of over 10K rewritten questions (RIDE-DeepMath).

The paper was published on arXiv in 2025 (arXiv:2511.04120).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f03635bc-f044-41fc-8b3f-eb8e009644bc",
  "isSidechain": false,
  "promptId": "388e3ca5-830e-4bb8-8461-8addb4d25cdc",
  "type": "user",
  "uuid": "460b2df5-593e-485c-9e06-c84966226146",
  "toolUseResult": {
    "query": "RIDE difficulty evolving perturbation item response theory mathematical reasoning IRT RL rewriting arXiv 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_011fnbBpQ7nCUjgbFrCboZor",
        "content": [
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning",
            "url": "https://arxiv.org/html/2511.04120"
          },
          {
            "title": "[2511.04120] RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2511.04120"
          },
          {
            "title": "RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ITEM ...",
            "url": "https://openreview.net/pdf/d5ed0f963c21d7ed1a8a3c452c9d81b161061351.pdf"
          },
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response ...",
            "url": "https://arxiv.org/pdf/2511.04120"
          },
          {
            "title": "RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ...",
            "url": "https://openreview.net/pdf?id=PPkzchpdNK"
          },
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=PPkzchpdNK"
          },
          {
            "title": "DeepMath-103K: A Large-Scale, Challenging, Decontaminated, and Verifiable Mathematical Dataset for Advancing Reasoning | Request PDF",
            "url": "https://www.researchgate.net/publication/392086521_DeepMath-103K_A_Large-Scale_Challenging_Decontaminated_and_Verifiable_Mathematical_Dataset_for_Advancing_Reasoning"
          }
        ]
      },
      "I found the paper you're looking for! Here's what I discovered:\n\n## RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning\n\nRIDE is a novel adversarial question-rewriting framework that leverages Item Response Theory (IRT) to rigorously measure question difficulty and to generate intrinsically more challenging, well-posed variations of mathematical problems.\n\n### Key Motivation\nLarge language models achieve high performance on mathematical reasoning, but these results can be inflated by training data leakage or superficial pattern matching rather than genuine reasoning, so an adversarial perturbation-based evaluation is needed to measure true mathematical reasoning ability.\n\n### Methodology\nThe framework leverages IRT to measure question difficulty, employs 35 LLMs to simulate students and build a difficulty ranker from their responses, which provides a reward signal during reinforcement learning and guides a question-rewriting model to reformulate existing questions across difficulty levels.\n\n### Advantages Over Prior Work\nUnlike rule-based methods, the approach adapts a reinforcement learning-based rewriting approach to generate perturbations, producing better-formed data, avoiding unsolvable or multiple-solution cases, and increasing unpredictability.\n\n### Resources\nThe paper releases a question rewriting model (RIDE-8B), two rewritten competition-level benchmarks (RIDE-AIME and RIDE-AMC), and a training dataset of over 10K rewritten questions (RIDE-DeepMath).\n\nThe paper was published on arXiv in 2025 (arXiv:2511.04120)."
    ],
    "durationSeconds": 6.818742735000007,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f03635bc-f044-41fc-8b3f-eb8e009644bc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 49 · 2026-05-28T14:06:54.386Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have sufficient information to conduct my evaluation. Let me synthesize what I've found and assess this proposal carefully.

Key findings from my research:

1. **PSN-IRT (AAAI 2026 Oral)**: Confirmed - uses 4PL IRT for LLM evaluation, flags contamination via guessing-rate anomalies but doesn't produce corrected ability scores. Neural estimation viable at small N.

2. **RankLLM (ICLR 2026)**: Confirmed - non-parametric difficulty-weighted ranking, 90% human alignment, no contamination modeling.


3. **DCR (EMNLP 2025)**: Confirmed - applies a multiplicative correction factor for contamination with roughly 4% error across three benchmarks, though performance drops to r=0.66 on harder tasks.

4. **Wang et al. (ICLR 2026)**: Confirmed - their likelihood-based contamination detection approach breaks down on reasoning models because RL training masks the contamination signals.

5. **Growing Pains (arXiv April 2026)**: Confirmed - uses a two-stage calibration process with MIRT 2PL parameters, achieving under 2-3% mean absolute error when working with 100 anchor items and maintaining correlations above 0.9.

6. **DGM (Shu et al.,** - still reviewing this approach.

Now looking at the remaining methods: a gated IRT model designed to catch test cheating when item exposure is known, a conformal procedure that jointly decontaminates by binarizing items, and several perturbation-based approaches like MATH-Perturb with hundreds of expert-crafted variants that cause 10-25% performance drops on frontier models. There's also MaSTer's multi-round adversarial pipeline and RIDE which uses IRT as a difficulty reward signal for RL rewriting rather than for decomposing contamination itself. One paper I initially flagged about psychometric questionnaire contamination turns out to be about personality tests rather than benchmark contamination in the IRT sense, so that's not directly relevant. ConStat rounds out the landscape with its performance-based detection using reference models.

The proposal's genuine strength is occupying that three-way intersection of IRT-based contamination correction paired with adversarial items—I haven't found anything doing joint decomposition of contamination and ability using paired variants. The theoretical grounding in the Differential Gamma Model is solid, and extending it to handle unknown exposure status through paired items is a meaningful contribution. The two-stage calibration approach is well-motivated by Growing Pains' findings, and the work shows real depth across psychometrics, IRT, and LLM evaluation.

But there's an immediate concern: why not just measure the performance gap between original and adversarial items directly without invoking IRT? ConStat and PaCoST already work with paired comparisons, so the added complexity of the IRT machinery needs stronger justification.

The proposal does offer answers—continuous corrected ability scores instead of binary flags, disentangling item-level from model-level contamination, and principled ranking corrections. A simpler regression approach might get similar practical results, but the IRT framework provides principled measurement-theoretic decomposition and better interpretability.

There's also the anchor assumption that adversarial variants are truly contamination-free, which is reasonable for newly generated items though the proposal does acknowledge this and includes validation checks. Then there's the bilinear rank-1 assumption that contamination factors cleanly into separable item and model components—

topic-specific contamination like a model trained on algebra but not geometry would break this, but again the proposal includes residual analysis to catch it.

The model pool size of 15-20 is quite small for IRT estimation. The two-stage approach helps with item parameters, but person-level parameters still only have 15-20 data points to establish meaningful variance, though the simulation study does address this concern. Ultimately, even if CRADE works perfectly, there's a question of whether the field actually needs continuous contamination-corrected ability scores or if simpler approaches like just using uncontaminated benchmarks such as MathArena would suffice. The proposal argues contamination correction lets us reuse existing benchmarks, but the growing availability of uncontaminated evaluations like MathArena and MATH-Perturb somewhat undermines that argument.

The core novelty lies in extending DGM to LLM contamination with unknown exposure status identified through paired items—that's genuinely novel and I haven't found anything like it. The two-stage calibration using leaderboard data is clever engineering but not deeply novel since Growing Pains already demonstrated this approach works. The real novelty claim is the combination of IRT, adversarial pairing, and contamination correction, which does appear to hold up. The problem itself is important and timely given that contamination is central to LLM evaluation, and Wang et al.'s ICLR 2026 finding that likelihood-based detection fails creates real demand for alternatives. But the practical significance ultimately hinges on whether the IRT-based decomposition actually produces meaningfully better rankings than simpler methods like just using MathArena.

The related work is extremely thorough—roughly 20 papers spanning psychometrics, IRT, contamination, and adversarial evaluation—and the positioning relative to PSN-IRT, RankLLM, DCR, JECS, ConStat, DGM, and Growing Pains is well-articulated. All the cited papers check out as real and accurately described. This is a strong, well-researched proposal with genuine novelty at the intersection of three fields. The main risks are whether the practical improvement over simpler alternatives justifies the added complexity, whether N=15-20 is sufficient for meaningful contamination parameter estimation despite the two-stage approach, and whether the ability estimates remain stable under the proposed framework.

I'm settling on a probability around 28-38%, with a median of 33%. The three-way intersection is genuinely novel, but the individual components extend existing work, and while it tackles an important problem, it's unclear whether the IRT decomposition is practically necessary given simpler alternatives exist. The thoroughness and genuine gap in the literature work in its favor, though reviewers might find the core finding unsurprising if it simply confirms what psychometric theory would predict.

Actually, reconsidering this — I think the contribution deserves more credit. The reasoning is well-motivated: Wang et al. showed likelihood-based detection fails, so a response-pattern approach is needed; DGM provides the theoretical framework but hasn't been applied to LLMs; the paired adversarial item design addresses DGM's "unknown exposure" limitation; and two-stage calibration solves IRT's "few examinees" problem. Each step addresses a specific constraint, making the integration non-trivial. If the decomposition works empirically, it's significant because it offers the first measurement-theoretic contamination correction rather than ad-hoc approaches, produces continuous corrected scores instead of binary decisions, and avoids likelihood-based methods entirely.

The real question is whether this would reveal surprising patterns about model contamination that simpler methods miss. But I'm concerned about the trivial alternative — a basic paired accuracy gap analysis could give a crude contamination estimate without any IRT machinery. The IRT framework adds principled score correction, though the practical gains over simpler baselines remain uncertain.

I'm settling on novelty as medium-to-strong since the intersection is genuinely novel and the theoretical extension is non-trivial, significance as medium given the important problem but uncertain practical improvement, and strong marks for related work. That puts me at around 30-40% probability, with 34% as my median estimate.

Actually, reconsidering this through an AAAI lens — they value theoretical contributions with identifiability proofs, rigorous methodology with simulation studies and multi-pronged validation, and novel cross-disciplinary integration. The fact that PSN-IRT got an oral there suggests they're receptive to psychometric approaches in NLP. The proposal's length and detail could hurt clarity, but that's a presentation problem rather than a conceptual one. I'll stick with 30-40%, median 34% — the idea has genuine novelty as a principled integration, but it's more of a methodological advance than a surprising discovery.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "460b2df5-593e-485c-9e06-c84966226146",
  "isSidechain": false,
  "requestId": "req_011CbV6Ts2TiCs6GrnA2F7XJ",
  "type": "assistant",
  "uuid": "83e2df1f-911a-4e1a-91cd-4740fdf1332d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXUuK7vjuPzxQcU28PrN2z",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 39501,
      "output_tokens": 7779,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7779,
          "cache_read_input_tokens": 39501,
          "cache_creation_input_tokens": 874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 874
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

_source line 50 · 2026-05-28T14:08:37.521Z_

Now I have sufficient research data to conduct the evaluation. Let me synthesize my findings and produce the formal assessment.

---

```
【阶段】: Triage

【领域调研】:

1. PSN-IRT — "Lost in Benchmarks? Rethinking LLM Benchmarking with IRT" (AAAI 2026 Oral, arXiv:2505.15055):
   - 4PL IRT via pseudo-Siamese neural estimation on 12 LLMs × 41,871 items across 11 benchmarks
   - 发现 benchmark 存在广泛 contamination（通过异常 guessing-rate 参数间接标记），但明确将 contamination-adjusted ability scoring 留为 open question
   - 与本 proposal 的关系：**直接前驱**。PSN-IRT 证明了 IRT 用于 LLM 评估的可行性，但恰好留下了本 proposal 想填的 gap（contamination-corrected ability scores）。这为 CRADE 提供了明确的 "open problem" 锚点

2. RankLLM — "Weighted Ranking of LLMs by Quantifying Question Difficulty" (ICLR 2026, arXiv:2602.12424):
   - 非参数 bidirectional score propagation，30 models × 35,550 questions，90% human alignment，ρ=0.94 even with 50% model removal
   - 与本 proposal 的关系：**强 baseline**。提供了无需 IRT 参数化的 difficulty-weighted ranking，但无 contamination 建模。CRADE 必须在 ranking quality 上至少持平 RankLLM，同时展示 contamination correction 的增量价值

3. DCR — "Quantifying Data Contamination in LLMs Evaluation" (EMNLP 2025, arXiv:2507.11405):
   - Fuzzy inference across 4 contamination levels → DCR Factor → Acc_adj = Acc × (1 − DCR Factor)
   - 9 LLMs (0.5B-72B)，~4% average error on 3 benchmarks，but r=0.66 on hard tasks
   - 与本 proposal 的关系：**最直接的 contamination correction 竞争者**。CRADE 的核心主张之一是 DCR 的 ad-hoc multiplicative correction 缺乏 measurement-theoretic justification——这是合理的批评

4. Wang, Li, Ko, Zhang — "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (ICLR 2026, arXiv:2510.02386):
   - 证明 RL 训练（GRPO/PPO）会掩盖 contamination 信号，使所有 likelihood-based detection 方法在 reasoning models 上失效（AUROC ≈ 50%）
   - 与本 proposal 的关系：**关键 motivator**。如果 likelihood-based detection 不行，就需要 response-pattern-based alternatives。CRADE 恰好完全基于 response patterns，不依赖 token probabilities

5. Growing Pains — "Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration" (arXiv:2604.12843, April 2026):
   - Two-stage MIRT 2PL fixed-parameter calibration on 400+ models，<2-3% MAE with 100 anchor items，ρ≥0.9
   - 与本 proposal 的关系：**技术 enabler**。直接验证了 CRADE 核心的 two-stage calibration architecture 是可行的。Growing Pains 做了 "pure IRT calibration"，CRADE 在此基础上加了 contamination gating

6. DGM — Shu, Henson, Luecht, "Using Deterministic, Gated IRT Model to detect test cheating due to item compromise" (Psychometrika 2013):
   - Gated IRT model 将考试表现分解为 genuine ability 和 cheating/preknowledge 分布，hierarchical MCMC estimation
   - 已确认存在，且从未被应用于 LLM 领域。关键限制：假设 item exposure status 已知（对 LLM 不成立）
   - 与本 proposal 的关系：**理论基础**。CRADE 的核心创新之一就是用 paired adversarial items 解决 DGM 的 "unknown exposure" 限制

7. JECS — "Provable Joint Decontamination for Benchmarking Multiple LLMs" (arXiv:2605.21543, May 2026):
   - Joint Envelope Conformal Selection，conformal p-values + adaptive BH procedure，提供 provable GCR control
   - 与本 proposal 的关系：**concurrent work，不同范式**。JECS binarizes items (keep/discard)，CRADE produces continuous corrected scores。两者可互补而非替代

8. MATH-Perturb (ICML 2025, arXiv:2502.06453):
   - 279 expert-crafted Level-5 perturbations，10-25% drops on frontier models，open code
   - 与本 proposal 的关系：提供 adversarial variant 生成的 backup pipeline 和 anchor assumption 验证的 gold standard

9. MaSTer — "Toward Automated Robustness Evaluation of Mathematical Reasoning" (arXiv:2506.05038, 2026):
   - Multi-round adversarial rewrite-verify pipeline，45-94% failure rates on GSM8K/MATH-500
   - 与本 proposal 的关系：提供 adversarial variant generation 的方法论参考

10. RIDE (arXiv:2511.04120, 2025):
    - 用 IRT 做 difficulty reward for RL-based question rewriting (RIDE-8B)
    - 与本 proposal 的关系：IRT 用于 adversarial perturbation，但目的是 difficulty calibration 而非 contamination decomposition

11. ConStat — "Performance-Based Contamination Detection in LLMs" (NeurIPS 2024):
    - 通过 rephrased vs. original performance gap + reference models 检测 contamination
    - 与本 proposal 的关系：confirms paired-item signal is informative，但无 latent-variable modeling

- **调研总结**: 这个领域目前存在三个成熟但分离的研究流：(a) IRT-based LLM evaluation（PSN-IRT, Growing Pains, RankLLM），(b) contamination detection/correction（DCR, ConStat, JECS），(c) adversarial robustness testing（MaSTer, RIDE, MATH-Perturb）。经详细搜索确认，**没有现有工作尝试将 IRT-based contamination-ability decomposition 与 paired adversarial items 结合**——这个三交叉点确实是空白的。Wang et al. (ICLR 2026) 对 likelihood-based detection 的否定性结果为 response-pattern-based 方法创造了真实的需求窗口。


【Trivial Alternative 检验】:

**存在一个显而易见的 trivial alternative：直接计算 paired accuracy gap。** 即：对每个 model，计算 Δ_j = accuracy(original) − accuracy(variant)，将此 gap 作为 contamination 的粗糙估计，然后用 accuracy(variant) 作为 "corrected ability" proxy。这本质上就是 ConStat 和 PaCoST 的思路，不需要任何 IRT machinery。

**CRADE 的增量价值需要在以下层面被证明：**
1. **连续分数 vs. 二元判定**：简单的 paired gap 只能给出粗糙的 contamination 估计，而 G-2PL 将其分解为 item-level 和 model-level components，提供 calibrated 的连续分数
2. **Ranking correction quality**：如果 CRADE-corrected rankings 比 simple variant-only rankings 更好地对齐 MathArena，则证明 IRT decomposition 有实质价值
3. **Parameter interpretability**：ξ_j 和 η_i 的可解释性（哪些 model 被 contaminated，哪些 item 容易被 memorize）是 simple gap 无法提供的

**评估**：trivial alternative 确实存在且成本更低。CRADE 的增量价值理论上成立（measurement-theoretic grounding、连续分数、可解释性），但**实证上是否 meaningful 取决于实验结果**。这是一个合理的风险，但不是致命的——因为 IRT 框架本身的理论贡献（identifiability proof、simulation validation）即使在实证增量不大的情况下也有独立价值。


【前提假设检验】:

核心 claim 的逻辑链条中，以下环节存在未经验证的假设：

1. **Anchor Assumption（variant items are contamination-free）**：这是整个框架的基石假设。如果 adversarial variants 也被 memorize（例如通过 training on adversarial data augmentation 或通过类似 pattern matching），则 θ_j 的估计就会被污染，整个 decomposition 失效。Proposal 包含了验证方案（item-fit statistics, cross-validation, comparison with MATH-Perturb expert variants），但这个假设本身**无法被完全验证**——只能提供 supporting evidence。**风险等级：中等**。对于新生成的 SymPy-verified variants，contamination 可能性很低，但随着 adversarial evaluation 的普及，这个假设的长期稳定性存疑。

2. **Rank-1 bilinear assumption（ξ_j·η_i）**：假设 contamination 可以分解为 model-level × item-level 两个独立因子。如果存在 topic-specific contamination（某 model 只在 algebra 被 contaminated 而 geometry 没有），rank-1 不够。Proposal 承认了这个限制并包含 residual analysis，但**初始假设仍未验证**。**风险等级：低-中**。对于 web-scrape-driven contamination（整个 benchmark 出现在训练数据中），rank-1 是合理的 first-order approximation。

3. **N=15-20 models 足够估计 meaningful contamination parameters**：虽然 two-stage calibration 解决了 item parameter 的小样本问题，但 ξ_j 本身只有 15-20 个值。这意味着关于 contamination **分布**的推断非常有限——本质上是 15-20 个点估计而非对总体的推断。Proposal 通过 simulation study 验证 parameter recovery，但**统计功效问题仍存在**。**风险等级：中等**。

4. **SymPy-verified adversarial variants preserve problem difficulty structure**：variant items 的 difficulty shift δ_i 被假设为可以通过 hierarchical prior 建模的小量偏移。但 adversarial rewriting 可能系统性地改变 problem structure，导致 δ_i 不服从 N(0, σ²_δ) 的假设。**风险等级：低**。这可以通过实际数据检验。


【3 维度打分】:

1. **Novelty: 中-强** — 核心贡献（将 DGM 从 psychometric test security 迁移到 LLM contamination assessment，用 paired adversarial items 解决 unknown exposure 问题，two-stage calibration 解决 small-N 问题）在我详细搜索后确认**确实是未被占据的交叉点**。没有现有工作将 IRT-based contamination-ability decomposition 与 paired adversarial items 结合。然而，需要注意的是：(a) 每个单独组件都是已有工作的 extension（DGM → G-2PL, Growing Pains → two-stage calibration, MaSTer/MATH-Perturb → variant generation），(b) 核心创新更多是 "principled integration" 而非 "surprising new insight"。相对于 PSN-IRT（AAAI 2026 Oral 级别的 novelty），CRADE 的增量是明确的（从 contamination flagging → contamination correction），但是否足够 "surprising" 存疑。RankLLM (ICLR 2026) 用非参数方法达到 90% human alignment，这给 CRADE 的参数化方法施加了 "需要证明 complexity 是 justified" 的压力。

2. **Significance: 中** — 研究问题（LLM benchmark contamination 导致能力评估不可信）无疑是重要且 timely 的。Wang et al. (ICLR 2026) 对 likelihood-based detection 的否定为 response-pattern-based 方法创造了真实需求。然而：(a) MathArena (NeurIPS 2025 D&B) 已扩展到 ~900 problems across 2025-2026 competitions，提供了 uncontaminated ground-truth rankings 的"绕行方案"，部分削弱了 contamination correction 的紧迫性；(b) JECS (arXiv May 2026) 提供了 provable decontamination（虽然是 binary），也在抢占这个 niche；(c) 实际影响取决于 CRADE-corrected rankings 相对于 simple alternatives（variant-only accuracy, RankLLM）的实证改进幅度，这在 idea 阶段无法判断。总体来说，问题重要，但解决方案的**实际增量影响存在不确定性**。

3. **Related Work: 强** — 覆盖极为全面，跨越 psychometrics（DGM, Konig et al., Fox, Noventa et al.）、IRT-based LLM evaluation（PSN-IRT, Growing Pains, RankLLM, RIDE）、contamination detection/correction（DCR, ConStat, JECS, PaCoST, Wang et al.）、adversarial variant generation（MaSTer, MathCheck, MATH-Perturb）。所有我验证的引用论文均真实存在且描述准确。差异化定位清晰：与 PSN-IRT 的差异（flagging → correction）、与 DCR 的差异（ad-hoc → measurement-theoretic）、与 JECS 的差异（binary → continuous）、与 RankLLM 的差异（non-parametric → parametric + contamination）、与 DGM 的差异（known exposure → inferred from paired items）。唯一的轻微缺陷是对 "Quantifying Data Contamination in Psychometric Evaluations of LLMs" (arXiv:2510.07175, EACL 2026 Findings) 的遗漏——虽然该工作关注 personality questionnaire contamination 而非 benchmark contamination，但与 IRT-contamination 交叉相关。


【概率估计】: [28% - 38%] 中位 33%

【估计理由】:
- Novelty (中-强) 是主要的上行驱动力：三交叉点确实未被占据，且 motivation chain（Wang et al. → 需要 response-pattern-based → DGM + paired items）逻辑自洽
- Significance (中) 是主要的上界限制因素：(a) trivial alternative（simple paired gap）的威胁真实存在，IRT 框架的增量价值需要实证证明；(b) MathArena 和 JECS 提供了部分替代路径，削弱了紧迫性；(c) 核心发现如果 positive（"IRT 可以分解 contamination 和 ability"），审稿人可能会认为 "this makes theoretical sense and I would have expected it to work"——而非 "surprising"
- Related Work (强) 提供了坚实的 floor：审稿人不太可能找到 missed related work 来否定 novelty claim
- 综合来看，这是一个"technically solid, well-positioned, but not electrifying" 的 idea。它更像是 psychometric methodology 的 rigorous application 而非 paradigm-shifting insight。在 AAAI，psychometric evaluation 有一个 receptive audience（PSN-IRT 拿了 Oral），但 CRADE 需要展示超越 theoretical elegance 的实证价值才能从 borderline 进入 accept

【主要风险】:
1. **Trivial Alternative 威胁**：审稿人可能会问 "why not just use variant accuracy as corrected ability?"——如果 CRADE-corrected rankings 与 simple variant-only rankings 高度相关（τ > 0.95），整个 IRT 框架的 added value 就难以 justify。这是 idea 层面的风险，因为它质疑的是 contribution 的 significance 而非 correctness。
2. **"Expected Result" 风险**：核心发现（IRT 可以分解 ability 和 contamination）在 psychometric 理论上是 well-motivated 的，审稿人可能认为这是 "applying known theory to a new domain" 而非 "discovering something new"——这会被归类为 incremental 而非 novel。AAAI 2026 Oral 给了 PSN-IRT（首次将 IRT 应用于 LLM），CRADE 是在此基础上的 "next step"，是否足够 interesting 取决于审稿人的 bar。
```

Sources:
- [PSN-IRT: Lost in Benchmarks? (AAAI 2026 Oral)](https://arxiv.org/abs/2505.15055)
- [RankLLM: Weighted Ranking of LLMs (ICLR 2026)](https://arxiv.org/abs/2602.12424)
- [DCR: Quantifying Data Contamination (EMNLP 2025)](https://arxiv.org/abs/2507.11405)
- [Wang et al.: Fragility of Contamination Detection (ICLR 2026)](https://arxiv.org/abs/2510.02386)
- [Growing Pains: Fixed Parameter Calibration (arXiv April 2026)](https://arxiv.org/abs/2604.12843)
- [DGM: Gated IRT for Test Cheating (Psychometrika 2013)](https://link.springer.com/article/10.1007/s11336-012-9311-3)
- [JECS: Provable Joint Decontamination (arXiv May 2026)](https://arxiv.org/abs/2605.21543)
- [MATH-Perturb (ICML 2025)](https://arxiv.org/abs/2502.06453)
- [MaSTer: Automated Robustness Evaluation (arXiv 2026)](https://arxiv.org/abs/2506.05038)
- [RIDE: Difficulty Evolving Perturbation (arXiv 2025)](https://arxiv.org/abs/2511.04120)
- [ConStat: Performance-Based Contamination Detection (NeurIPS 2024)](https://neurips.cc/virtual/2024/poster/96266)
- [Quantifying Data Contamination in Psychometric Evaluations (EACL 2026 Findings)](https://arxiv.org/abs/2510.07175)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "83e2df1f-911a-4e1a-91cd-4740fdf1332d",
  "isSidechain": false,
  "requestId": "req_011CbV6Ts2TiCs6GrnA2F7XJ",
  "type": "assistant",
  "uuid": "71e49c30-0b99-4d0a-9a46-19e1585ea42d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01TXUuK7vjuPzxQcU28PrN2z",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 874,
      "cache_read_input_tokens": 39501,
      "output_tokens": 7779,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 874,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7779,
          "cache_read_input_tokens": 39501,
          "cache_creation_input_tokens": 874,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 874
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

_source line 51_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "71e49c30-0b99-4d0a-9a46-19e1585ea42d",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Runtime record

_source line 52_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate proposal on contamination-ability LLM decomposition",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Runtime record

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "71e49c30-0b99-4d0a-9a46-19e1585ea42d",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Evaluate proposal on contamination-ability LLM decomposition",
  "sessionId": "dbc09836-8363-423e-8f39-5a36a2157b70"
}
```

---
