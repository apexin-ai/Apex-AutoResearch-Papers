# Research conversation: 【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。 【proposal】: # CRADE: Joint Contamination-Abilit

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 64
- **Recorded user turns:** 1
- **Tool calls:** 18
- **Original source:** `logs/chats/exported-trajectories/account-1/57ca1d5f-fa09-46a1-b8fb-8491e77b0326.jsonl`
- **Structured JSON:** [`c4a3078ca7a1a902bb78.json`](../../sessions/c4/c4a3078ca7a1a902bb78.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T14:03:21.766Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T14:03:21.766Z",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "content": "【任务】: 请评估以下 proposal 的客观中稿概率。\n必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。\n\n【proposal】:\n# CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items\n\n## Core Problem\n\nNo existing framework can determine whether a model fails adversarial benchmark variants because it memorized original answers (contamination) or because it lacks genuine reasoning ability (capability deficit) — all current work observes this entanglement but none models it within a measurement-theoretic framework, preventing trustworthy LLM capability assessment.\n\n## Research Opportunity\n\nThree previously siloed research streams — IRT-based LLM evaluation (PSN-IRT AAAI 2026 Oral, ATLAS, LEGO-IRT), contamination detection/correction (DCR EMNLP 2025, ConStat NeurIPS 2024, JECS arXiv May 2026), and adversarial robustness testing (MaSTer, RIDE, MATH-Perturb ICML 2025) — have each matured independently to the point where their integration is both technically feasible and urgently needed. The critical catalyst is Wang et al.'s ICLR 2026 proof that all likelihood-based contamination detection fails on reasoning models (AUROC ≈ 50%), creating demand for response-pattern-based alternatives that bypass token-probability signals entirely. A key theoretical precedent exists but has never been applied to LLMs: the Deterministic Gated IRT model (DGM; Shu, Henson & Luecht, Psychometrika 2013) decomposes test performance into genuine ability and cheating/preknowledge components conditioned on item exposure status — precisely the structure needed for LLM contamination. PSN-IRT showed IRT works for LLMs (12 models, 41,871 items, 4PL) but left contamination-adjusted scoring as an explicit open question, flagging anomalous guessing-rate parameters as contamination indicators without providing corrected ability estimates. RankLLM (ICLR 2026) demonstrated that non-parametric difficulty-aware ranking achieves 90% human alignment with only a damping hyperparameter — but provides no contamination decomposition, producing rankings without interpretable ability vs. memorization parameters. A crucial practical enabler has emerged: the Open LLM Leaderboard V1 provides per-item binary response data for 2,000+ models across standard benchmarks including GSM8K (1,359 items), accessible via per-model details datasets (Polo et al., ICML 2024). Combined with Growing Pains' (arXiv April 2026) demonstration that two-stage fixed-parameter calibration achieves <2% error with 100 anchor items and ρ ≥ 0.9 ranking stability, this large-N calibration data resolves the fundamental feasibility concern of fitting IRT-based models with only 15-20 LLMs — by fixing well-calibrated item parameters from Stage 1, Stage 2 estimation reduces to person-level and contamination parameters only. The AAAI 2027 deadline (abstracts July 21, papers July 28, 2026) is 8 weeks out. Nobody sits at the three-way intersection of IRT estimation, contamination correction, and adversarial pairing because these communities publish at different venues (ACL/EMNLP for contamination, ICLR/NeurIPS for robustness, AAAI for psychometric evaluation, Psychometrika/JEBS for test security).\n\n## Research Landscape\n\nThe current best contamination-to-correction pipeline is DCR (EMNLP 2025), which produces a DCR Factor via fuzzy inference across four contamination levels, achieving ~4% average error on three benchmarks — but its ad-hoc multiplicative correction Acc_adj = Acc × (1 − DCR Factor) has no measurement-theoretic justification and empirically weakens on hard tasks (r=0.66). PSN-IRT (AAAI 2026 Oral) demonstrates IRT's power for LLM evaluation using a 4PL model across 12 LLMs on 11 benchmarks (41,871 items), flagging contamination indirectly via anomalous guessing-rate parameters, but produces no contamination-adjusted ability scores; critically, PSN-IRT succeeds with 12 models by using neural network estimation (pseudo-Siamese architecture) rather than classical MLE, establishing that neural IRT estimation is viable at small model counts. RankLLM (ICLR 2026) provides a strong non-parametric baseline: bidirectional score propagation between models and questions achieves 90% human alignment on 30 models × 35,550 questions, with remarkable stability under model removal (ρ = 0.94 even with 50% pool removed) and 0.006s convergence — but it produces difficulty-weighted rankings without any contamination modeling. RIDE (arXiv 2025) combines IRT with adversarial perturbation for math evaluation — but uses IRT only as a difficulty reward signal for RL-based question rewriting via RIDE-8B, not for joint ability-contamination estimation. JECS (arXiv May 2026) achieves formal conformal guarantees for multi-model decontamination via joint envelope conformal selection, but wastes information by binarizing items into keep/discard rather than producing continuous corrected scores. ConStat (NeurIPS 2024) detects contamination via performance gaps on rephrased samples using a statistical comparison against reference models, but does not model it as a latent variable within a psychometric framework. In psychometrics, the DGM (Shu et al., Psychometrika 2013) uses a gated IRT formulation estimated via hierarchical MCMC to decompose examinee performance into genuine ability and item-preknowledge components — but assumes item exposure status is known a priori, which is unavailable for LLM training data, and was validated only at operational testing sample sizes (hundreds of examinees). Two paired-item approaches exist but use no IRT: PaCoST (arXiv 2024) performs paired confidence significance testing for binary contamination detection, and ConStat compares primary vs. reference benchmark performance — both confirm the paired-item signal is informative but neither models it as a latent variable. For adversarial variant generation, MaSTer (arXiv 2026) provides a validated multi-round rewrite-verify pipeline (5 parallel streams × 3 iterations) achieving 45-94% target failure rates on GSM8K and MATH-500 using Qwen2.5-32B-Instruct for both rewriting and LLM-based verification (98% precision); code is claimed at github.com/sustech-nlp/MaSTer but was unavailable as of May 2026 — backup pipelines exist via MathCheck (ICLR 2025, open code) and MATH-Perturb (ICML 2025, 279 expert-crafted perturbations with open code). Growing Pains (arXiv April 2026) demonstrates two-stage fixed-parameter calibration for extensible LLM evaluation: calibrating MIRT 2PL item parameters on 295+ reference models, then scoring new models via fixed anchor items, achieving <2% MAE and ρ ≥ 0.9 with 100 anchor items per benchmark — directly applicable to our setting where item parameters are calibrated on large-N leaderboard data and contamination parameters estimated on a smaller model pool. Konig et al. (Behavior Research Methods 2023) demonstrate that hierarchical Bayesian 2PL (OH2PL) with half-Cauchy hyperpriors produces unbiased item parameter estimates down to N=50, while standard MML shows 75-89% inadmissible solutions at that sample size — establishing that Bayesian estimation is the correct choice for small-N IRT. Fox (JEBS 2025) pushes further: IRT-BCSM integrates out person parameters for stable estimation at N=50-100, with RMSE of 0.110 for discrimination at N=50 while standard 2PL/MML collapses (RMSE=1.782). MathArena (NeurIPS 2025 D&B Track) has expanded to ~900 problems across 2025-2026 competitions (AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, Apex) with 50+ models, providing rich uncontaminated ground-truth rankings. Concurrent work search (arXiv, OpenReview, May 2026): no paper attempts joint IRT-based contamination-ability decomposition with paired adversarial items or two-stage fixed-parameter calibration for contamination-aware scoring — the intersection remains unoccupied.\n\n## Proposed Approach\n\nWe extend the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from the test-security domain to LLM contamination assessment, introducing the Gated-2PL (G-2PL) model as the primary framework where correct-response probability decomposes into ability-driven and contamination-driven components via a gating mechanism. The key innovations over DGM are: (1) item exposure status is not assumed known but is identified from paired adversarial items, and (2) a two-stage fixed-parameter calibration architecture leverages large-N leaderboard data to resolve the small-sample estimation challenge.\n\n**Two-stage fixed-parameter calibration architecture (central methodological contribution):**\n\nStage 1 — Item parameter calibration (large-N, standard 2PL):\n- Assemble per-item binary response matrix from Open LLM Leaderboard V1 per-model details datasets for GSM8K (N_cal ≈ 2,000+ models × 1,359 items). Per-item data resides in individual per-model datasets under huggingface.co/open-llm-leaderboard-old (naming pattern: details_{org}__{model}), reconstructible following Polo et al. (ICML 2024, tinyBenchmarks). Each dataset contains per-task configurations (e.g., harness_gsm8k) with item-level correctness indicators.\n- Fit standard 2PL via marginal maximum likelihood (MML): estimate â_i (discrimination) and b̂_i (difficulty) for each GSM8K item. With N_cal ≈ 2,000+, these estimates are highly stable — Growing Pains demonstrates <2% MAE and ρ ≥ 0.9 with as few as 100 reference models on similar data.\n- Validate calibration quality: item-fit statistics (S-X², item-total correlations), dimensionality assessment (eigenvalue ratios from the item correlation matrix), and comparison with Growing Pains' calibrated parameters if available.\n- For MATH-500 (secondary benchmark): Stage 1 calibration assembled from (a) V2 leaderboard MATH Level 5 per-model details for the ~100 Level 5 items in MATH-500 (hundreds of models available via gated datasets at huggingface.co/datasets/open-llm-leaderboard/{org}__{model}-details), (b) publicly available per-item MATH-500 evaluation results from major papers and evaluation frameworks (lm-evaluation-harness), and (c) targeted evaluation of ~50-100 small open-weight models (7B-13B) from V1 leaderboard checkpoints on MATH-500 (~15 H100-hrs). Expected N_cal for MATH-500 ≈ 50-200, adequate for Bayesian 2PL calibration per Konig et al. (2023).\n\nStage 2 — Gated model estimation (small-N, fixed item parameters):\n- Fix a_i = â_i, b_i = b̂_i from Stage 1. This eliminates 2K parameters from estimation, leaving only θ_j (M), ξ_j (M), η_i (K), and δ_i (K) = 2M + 2K free parameters.\n- Estimate via Bayesian MCMC on the 15-20-model paired (original + variant) response matrix.\n- The fixed-parameter approach is critical: with a_i and b_i grounded in large-N calibration, θ_j identification from variant items is well-conditioned (each model responds to K ≈ 1,000 items with known parameters), and contamination parameters (ξ_j, η_i) are identified from original-variant performance gaps with θ_j already anchored.\n\n**Model specifications (two-tier: reduced and full):**\n\nReduced G-2PL (R-G-2PL, person-level contamination only, M additional parameters):\n- For variant item i*: P(Y_{j,i*}=1 | θ_j) = σ(a_i(θ_j − b_i − δ_i))\n- For original item i: P(Y_{j,i}=1 | θ_j, ξ_j) = ξ_j + (1−ξ_j)·σ(a_i(θ_j − b_i))\n- θ_j = model j's genuine reasoning ability (person parameter)\n- ξ_j ∈ [0,1] = model j's global contamination probability (person parameter) — probability that model j has memorized any given original item, assumed uniform across items\n- a_i, b_i = discrimination and difficulty (fixed from Stage 1)\n- δ_i = variant difficulty shift (estimated in Stage 2)\n- Only M additional contamination parameters (vs. M+K for full model), yielding far stronger identifiability at N=15-20\n- Interpretation: ξ_j captures bulk training data contamination (entire benchmarks appearing in web scrapes), which is the dominant contamination mechanism for LLMs\n\nFull G-2PL (person × item contamination, M+K additional parameters):\n- For variant item i*: P(Y_{j,i*}=1 | θ_j) = σ(a_i(θ_j − b_i − δ_i))\n- For original item i: P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i))\n- η_i ∈ [0,1] = item i's contamination susceptibility (item parameter)\n- Adopted only if the simulation study (see below) confirms η_i is recoverable at N=15-20 with acceptable RMSE\n- Each η_i has only M=15-20 observations, making estimation challenging — hierarchical priors provide regularization\n\n**Rationale for G-2PL over G-3PL:** The guessing parameter c_i in 3PL requires 200+ examinees for stable estimation under classical methods, while we have only 15-20 models. Dropping c_i to use 2PL eliminates the most problematic parameter for small samples while retaining the core contamination decomposition. For math benchmarks with open-ended answers (MATH-500, GSM8K), guessing probability is effectively zero, making 2PL substantively appropriate.\n\n**Ablation to Gated-3PL (G-3PL):**\n- P(Y_{j,i*}=1 | θ_j) = c_i + (1−c_i)·σ(a_i(θ_j − b_i − δ_i))\n- P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·[c_i + (1−c_i)·σ(a_i(θ_j − b_i))]\n- c_i fixed to domain-specific constants: c_i = 0 for open-ended math (MATH-500, GSM8K), enabling estimation only for any future MCQ extensions.\n\n**Estimation strategy (fully specified):**\nPrimary: Bayesian MCMC via NumPyro/Stan with hierarchical priors, following DGM's original estimation framework:\n- θ_j ~ N(0, σ²_θ), σ_θ ~ Half-Cauchy(0, 2.5)\n- ξ_j ~ Beta(α_ξ, β_ξ), with α_ξ, β_ξ ~ Gamma(2, 1) (hierarchical; allows posterior to concentrate near 0 for clean models or near 1 for heavily contaminated ones)\n- η_i ~ Beta(α_η, β_η), with α_η, β_η ~ Gamma(2, 1) (hierarchical; full G-2PL only)\n- δ_i ~ N(0, σ²_δ), σ_δ ~ Half-Cauchy(0, 1) (hierarchical; variant shifts expected small)\n- a_i, b_i: fixed from Stage 1 (NOT estimated in Stage 2)\n- MCMC: 4 chains × 2,000 warmup + 2,000 samples, NUTS sampler, R̂ < 1.05 convergence criterion, ESS > 400 per parameter\nComparison: Neural estimation extending PSN-IRT's pseudo-Siamese architecture with an additional gating head that outputs (ξ_j, η_i) — trained via binary cross-entropy on the joint original+variant response matrix, with a_i and b_i initialized from Stage 1 and optionally frozen. This provides a non-Bayesian point estimate comparison.\nAblation: Variational inference via Pyro SVI as a faster alternative to MCMC, using amortized inference for scalability testing.\n\n**Formal identifiability (strengthened by two-stage calibration):**\nWe prove identifiability via a two-step argument that is substantially strengthened by fixing a_i and b_i from Stage 1:\n\n(1) Variant items serve as contamination-free anchors. With a_i, b_i fixed from Stage 1, θ_j is identified from variant responses via standard 2PL person parameter estimation (K ≈ 1,000 items per model, well-determined even for a single model). The difficulty shift δ_i is identified from M model responses per variant item; with M=15-20 and hierarchical priors, this yields credible estimates (validated in simulation study). Key advantage of fixed-parameter calibration: θ_j identification does not depend on the number of models M, only on the number of items K per model — eliminating the classical IRT concern about few examinees.\n\n(2) Given identified θ_j, fixed a_i, b_i, and estimated δ_i, the original-variant performance gap identifies the contamination gate. For R-G-2PL: M gaps per item constrain M values ξ_j — with K ≈ 1,000 items per model, each ξ_j is massively over-determined. For full G-2PL: M·K observed gaps constrain the bilinear product ξ_j·η_i. Under rank-1 bilinear decomposition with M models and K items, M·K observations constrain M+K−1 free parameters (one fixed for scale), identifiable when (M−1)(K−1) > 0 — satisfied for any M,K ≥ 2.\n\n(3) Fisher information: The 2PL Fisher information matrix is well-conditioned even at M=15, unlike 3PL where c_i creates flat likelihood surfaces. With fixed a_i and b_i, the conditional Fisher information for (θ_j, ξ_j) given item parameters has full rank, ensuring local identifiability. The two-stage approach avoids the joint estimation instabilities that plague IRT with few examinees.\n\n**Simulation study for parameter recovery (new, Week 4, 1-2 days CPU):**\n\nDesign: Fully crossed simulation validating G-2PL parameter recovery under two-stage calibration at the target sample sizes.\n\nGenerating model:\n- Item parameters: a_i ~ LogNormal(0, 0.5), b_i ~ N(0, 1), fixed as Stage 1 calibrated values (not re-estimated)\n- θ_j ~ N(0, 1)\n- Contamination prevalence/strength, three scenarios:\n  (a) Low: 20% of models contaminated (ξ_j ~ Beta(8,2) for contaminated, ξ_j = 0 for clean)\n  (b) Medium: 50% of models with ξ_j ~ Beta(5,5) (moderate, variable contamination)\n  (c) High: 80% of models with ξ_j ~ Beta(2,2) (widespread, variable strength)\n- η_i ~ Beta(2, 5) for full G-2PL (most items not highly susceptible)\n- δ_i ~ N(0, 0.5)\n\nConditions (fully crossed):\n- N (models): {15, 20, 50}\n- K (paired items): {100, 500}\n- Contamination scenario: {low, medium, high}\n- Model: {R-G-2PL (ξ_j only), full G-2PL (ξ_j and η_i)}\n- Total: 3 × 2 × 3 × 2 = 36 conditions\n\nReplications: 500 per condition (following Konig et al. 2023; Fox 2025 used 1,000 but with simpler models)\n\nMetrics (per condition, averaged over replications):\n- θ_j: bias, RMSE, 95% credible interval coverage, Kendall-τ with true θ ranking\n- ξ_j: bias, RMSE, 95% CI coverage, Kendall-τ with true ξ ranking\n- η_i (full G-2PL only): bias, RMSE, 95% CI coverage\n- Classification: sensitivity/specificity for identifying contaminated models (ξ_j > 0.3)\n- MCMC diagnostics: mean R̂, mean ESS, non-convergence rate\n\nMCMC per replication: 4 chains × 1,000 warmup + 1,000 samples, NUTS. Estimated compute: ~30s per replication (small model with fixed item params) × 18,000 fits = ~150 CPU-hours, parallelizable across cores to complete in 1-2 days.\n\nDecision rule: If ξ_j RMSE < 0.15 and coverage ∈ [0.90, 0.98] at N=15, proceed with full G-2PL. If η_i recovery is poor (RMSE > 0.25 or coverage < 0.85), adopt R-G-2PL as primary and relegate full G-2PL to future work with larger model pools.\n\n**Prior sensitivity analysis (new, 1 day):**\n\nThree prior specifications applied to the real data MCMC:\n(a) Proposed hierarchical: ξ_j ~ Beta(α_ξ, β_ξ), α_ξ, β_ξ ~ Gamma(2,1) — data-driven, allows concentration near 0 or 1\n(b) Weakly informative flat: ξ_j ~ Beta(1,1) (uniform on [0,1]), η_i ~ Beta(1,1) — maximum prior uncertainty, no hierarchical pooling\n(c) Informative: ξ_j ~ Beta(α_j, β_j) with person-specific priors informed by ConStat contamination flags where available (models flagged contaminated get ξ_j ~ Beta(5,2), unflagged get ξ_j ~ Beta(2,5)); η_i ~ Beta(2,5) reflecting prior belief that most items are not highly susceptible\n\nReport:\n- θ_j ranking stability: Kendall-τ between corrected ability rankings under the three prior specifications\n- ξ_j ordering stability: Kendall-τ between contamination orderings\n- Posterior credible interval widths: precision comparison across priors\n- Key qualitative conclusions: do the same models get flagged as high-contamination (ξ_j > 0.5)?\n- Sensitivity metric: maximum |Δξ_j| across prior pairs for any model — quantifies worst-case prior influence\n\n**Bilinear rank-1 model adequacy plan (full G-2PL only):**\nThe rank-1 assumption (ξ_j·η_i) treats contamination as model-global and item-global, a first-order approximation. We assess:\n(a) Compute standardized residuals r_{j,i} = (Y_{j,i} − P̂_{j,i}) / √(P̂_{j,i}(1−P̂_{j,i})) from the rank-1 fit and report the residual matrix.\n(b) Compute Yen's Q3 statistic for local dependence among original items after conditioning on θ_j — systematic topic-structured residuals would indicate rank-1 insufficiency.\n(c) Apply person-fit statistics (standardized log-likelihood lz*) to detect models whose original-item response patterns deviate from the G-2PL predictions, flagging potential topic-specific contamination.\n(d) If structured residuals emerge, explore rank-2 extension (ξ_j·η_i → ξ_j^(1)·η_i^(1) + ξ_j^(2)·η_i^(2)) or topic-stratified estimation as explicit future work.\n(e) Justification for rank-1 as starting point: LLM contamination is primarily driven by overall training data overlap (entire benchmark suites appearing in Common Crawl/web scrapes) rather than topic-selective memorization; the rank-1 model captures this dominant effect.\n\n**Data collection (within 200 H100-hr budget):**\n\nStage 1 data: Assemble GSM8K per-item response matrix from Open LLM Leaderboard V1 per-model details datasets (huggingface.co/open-llm-leaderboard-old, ~7,000 per-model datasets). Each model's GSM8K details available in configuration 'harness_gsm8k' with per-item correctness fields. Data assembly via HuggingFace datasets library: iterate over available details datasets, extract GSM8K responses, construct binary response matrix. Expected: N_cal ≈ 2,000+ models × 1,359 items. Data assembly effort: ~1 day engineering. For MATH-500: supplement with targeted evaluation of ~50-100 small V1 models on MATH-500 (~15 H100-hrs) plus V2 Level 5 per-item data where available.\n\nStage 2 data: For ~1,000 items (all 1,359 GSM8K items + MATH-500 items up to budget), generate adversarial variants via a novel SymPy-verified rewrite pipeline. This is NOT a MaSTer replication — MaSTer uses LLM-based verification via Qwen2.5-32B-Instruct (98% precision on a rewrite meaning-preservation check); our pipeline instead combines LLM-based rewriting (Qwen3.6-27B for multi-round adversarial rewrites) with formal symbolic verification (SymPy for numerical answer correctness), a novel hybrid that provides stronger guarantees than LLM-only verification for math problems with determinate numerical answers. Pipeline: (1) Qwen3.6-27B generates candidate variants via value/structure perturbation, (2) SymPy verifies that the perturbed problem has a valid, determinate answer differing from the original, (3) human spot-check on 10% sample. Estimated: ~25 H100-hrs for variant generation.\n\nBackup pipelines (if primary pipeline yields <80% valid variants by Week 2): (a) MathCheck (ICLR 2025, open code at github.com/PremiLab-Math/MathCheck) for GSM8K variants; (b) seed with MATH-Perturb's 279 expert-crafted Level 5 perturbations (ICML 2025, open code at github.com/Kaffaljidhmah2/MATH-Perturb) and extend via LLM rewriting for remaining items.\n\nModel evaluation: Collect response matrices from 15-20 models: 10 open-weight (DeepSeek-R2 32B, DeepSeek-V4-Flash 284B, Qwen3.6-27B, Qwen3.5-397B-A17B, GLM-5.1 754B-A40B, OLMo-2-13B, Llama-4-Maverick-17B-A400B, Mistral-Large-3, plus 2 smaller reference models) and 5-8 closed-API models (GPT-4o, GPT-5.2, Claude Sonnet 4.6, Gemini 2.5 Flash, Gemini 3.1 Pro). For GSM8K originals: reuse Open LLM Leaderboard V1 per-item data where available (many open-weight models already evaluated); run new inference only for models not on V1 (~40 H100-hrs). Variant inference: all 15-20 models on generated variants (~80 H100-hrs for open-weight models). Closed-model API costs estimated separately. IRT fitting is negligible (<1 hr CPU for MCMC).\n\n**Validation (four-pronged, addressing domain mismatch concern):**\n\n(1) External ranking correlation: Kendall-τ of CRADE-corrected ability rankings vs. MathArena 2026 uncontaminated competition rankings (~900 problems, 50+ models), targeting τ ≥ 0.85 (revised from 0.90 given domain mismatch between textbook-style MATH-500/GSM8K and competition-style MathArena). Report bootstrap 95% confidence interval. Compare against: (a) raw accuracy rankings, (b) RankLLM difficulty-weighted rankings, (c) DCR-corrected rankings (r=0.66 on hard tasks), (d) JECS-filtered rankings.\n\n(2) Synthetic contamination injection (causal validation): Deliberately fine-tune OLMo-2-13B on MATH-500 training items (1 epoch, mild contamination following established protocols from contamination survey literature) and re-evaluate. If G-2PL correctly recovers elevated ξ for the fine-tuned model while θ remains stable (matching pre-contamination ability), this provides causal evidence that the decomposition works. Compare fine-tuned ξ against clean OLMo-2-13B ξ via posterior credible interval separation. This is the strongest validation because it provides ground-truth contamination status.\n\n(3) Convergent validity with existing detectors: Correlate G-2PL's per-model ξ_j estimates with: (a) ConStat contamination flags (performance gap on rephrased vs. original), (b) PaCoST binary contamination verdicts (paired confidence significance test), (c) PSN-IRT's anomalous guessing-rate parameters. High concordance validates that ξ captures the same construct; low concordance would require investigation of what ξ uniquely captures beyond existing methods.\n\n(4) Ablation showing differential correction benefit: Demonstrate that CRADE correction improves ranking accuracy (vs. MathArena) more for models with high estimated ξ (provably or detectably contaminated) than for models with low ξ. This confirms the correction is targeted rather than uniformly applied.\n\n**Anchor assumption validation (variant contamination-free):**\n(a) Fit standard 2PL to variant-only response matrix (with a_i fixed from Stage 1, estimating only θ_j and δ_i) and compute item-fit statistics (S-X² or Orlando-Thissen) and person-fit statistics (lz*). Good fit supports the anchor assumption — variants behave like clean IRT items measuring genuine ability.\n(b) Check that variant difficulty b_i + δ_i is predictable from original difficulty b_i plus a systematic shift; high-residual outlier items may indicate re-contaminated variants and should be flagged for manual review.\n(c) Cross-validation: Hold out 20% of variant items, fit 2PL on remaining 80%, predict held-out responses. Prediction accuracy comparable to full-data fit supports generalizability.\n(d) Ablation: Compare CRADE results using MATH-Perturb's expert-crafted perturbations (strongest anchor assumption) vs. our SymPy-verified rewrite pipeline to assess sensitivity to variant quality.\n\nAblations: (a) R-G-2PL (ξ_j only) vs. full G-2PL (ξ_j and η_i) — does item-level susceptibility add meaningful signal?, (b) G-2PL vs. G-3PL (with fixed c_i = 0 for math), (c) Bayesian MCMC vs. neural estimation vs. variational inference, (d) number of variant items (100/500/1000), (e) number of models (10/15/20), (f) sensitivity to variant difficulty shift δ_i, (g) rank-1 vs. rank-2 bilinear decomposition if residuals warrant it, (h) RankLLM vs. G-2PL ranking quality, (i) two-stage calibration (GSM8K) vs. concurrent estimation (MATH-500) quality comparison, (j) prior sensitivity across 3 specifications.\n\n## Detailed Description\n\nCRADE introduces a measurement-theoretic framework for decomposing LLM benchmark performance into genuine reasoning ability (θ), contamination exposure (ξ), and item properties, by extending the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from test-security psychometrics to LLM evaluation. The central methodological innovation is a two-stage fixed-parameter calibration architecture: Stage 1 calibrates item parameters (discrimination a_i, difficulty b_i) from Open LLM Leaderboard V1 per-item response data (~2,000+ models × 1,359 GSM8K items, following Polo et al. ICML 2024 and Growing Pains arXiv April 2026), providing well-identified item parameters grounded in large-N calibration; Stage 2 fixes these item parameters and estimates the gated contamination model on a 15-20-model paired response matrix, reducing the estimation problem to person-level ability (θ_j), contamination (ξ_j), item susceptibility (η_i), and variant difficulty shifts (δ_i) only. Two model tiers are presented: (1) the Reduced G-2PL (R-G-2PL), where P(Y_{j,i}=1) = ξ_j + (1−ξ_j)·σ(a_i(θ_j − b_i)) adds only M person-level contamination parameters, maximally parsimonious at N=15-20; and (2) the Full G-2PL, where P(Y_{j,i}=1) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i)) adds M+K parameters with item-specific susceptibility, adopted only if the simulation study confirms η_i recovery. The simulation study (500 replications × 36 conditions: N∈{15,20,50} × K∈{100,500} × 3 contamination scenarios × 2 models) validates parameter recovery under two-stage calibration, reporting bias, RMSE, and 95% credible interval coverage for θ_j and ξ_j — the single most important addition for psychometric-savvy reviewers. Prior sensitivity analysis under three specifications (hierarchical Beta, flat Beta(1,1), ConStat-informed) demonstrates robustness of person-level conclusions. The paired-item design couples each benchmark question with a SymPy-verified adversarial variant — a novel hybrid pipeline combining LLM-based rewriting (Qwen3.6-27B) with symbolic answer verification, providing stronger mathematical guarantees than MaSTer's LLM-only verification. Variant items serve as contamination-free anchors: with item parameters fixed from Stage 1, θ_j is identified from ~1,000 variant items per model (well-determined even for a single model), then contamination parameters are identified from original-variant performance gaps with provable identifiability ((M−1)(K−1) > 0 for rank-1 bilinear decomposition). This circumvents the critical failure of likelihood-based contamination detection on reasoning models (AUROC ≈ 50%, Wang et al. ICLR 2026) by operating entirely on response patterns. Four-pronged validation: (1) Kendall-τ ≥ 0.85 against MathArena's ~900-problem uncontaminated rankings, compared against RankLLM non-parametric baseline, DCR correction, and JECS-filtered rankings; (2) synthetic contamination injection via fine-tuning OLMo-2-13B to causally verify ξ recovery; (3) convergent validity with ConStat, PaCoST, and PSN-IRT; (4) differential correction benefit for high-ξ models. Model adequacy assessed via standardized residuals, Q3 statistics, and person-fit lz* from rank-1 bilinear fit. Focused on GSM8K (1,359 items, full two-stage calibration) with MATH-500 as secondary benchmark, 15-20 models including DeepSeek-R2 32B, Qwen3.6-27B, GLM-5.1, and 5-8 closed-API models, within 230 H100-hrs.\n\n## Key References\n\n- Lost in Benchmarks? Rethinking LLM Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral) — 4PL IRT for 12 LLMs on 41,871 items via pseudo-Siamese neural estimation; flags contamination via guessing-rate anomalies but leaves corrected scoring as open question; demonstrates neural IRT estimation works with very few examinees\n- RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty (ICLR 2026) — non-parametric bidirectional score propagation achieving 90% human alignment on 30 models × 35,550 questions; robust to 50% model removal (ρ=0.94); no contamination modeling; our primary non-parametric baseline\n- DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025) — ad-hoc multiplicative contamination correction achieving r=0.66 on hard tasks; our measurement-theoretic G-2PL subsumes this\n- On The Fragility of Benchmark Contamination Detection in Reasoning Models [Wang, Li, Ko, Zhang] (ICLR 2026) — proves likelihood-based detection fails on reasoning models (AUROC ≈ 50%); motivates response-pattern-based approach\n- Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise [DGM; Shu, Henson, Luecht] (Psychometrika 2013) — key theoretical precedent: gated IRT with hierarchical MCMC estimation decomposes performance into ability + preknowledge; we extend to unknown item exposure via paired items and two-stage calibration\n- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024) — detects contamination via performance gaps on rephrased samples against reference models; confirms paired-item signal but no latent-variable model; used as convergent validity comparison and informative prior source\n- Provable Joint Decontamination for Benchmarking Multiple Large Language Models [JECS] (arXiv May 2026) — conformal p-values via joint envelope selection for multi-model decontamination; binarizes items (keep/discard) while we produce continuous corrected scores\n- RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025) — uses IRT as difficulty reward for RL-based rewriting; we use IRT for joint ability-contamination estimation\n- Toward Automated Robustness Evaluation of Mathematical Reasoning [MaSTer] (arXiv 2026) — validated multi-round adversarial variant pipeline (5 streams × 3 iterations) on 4×4090 GPUs using Qwen2.5-32B-Instruct with LLM-based verification (98% precision); 45-94% failure rates on GSM8K/MATH-500; code claimed at github.com/sustech-nlp/MaSTer but unavailable as of May 2026; our pipeline differs by using SymPy-based symbolic verification instead of LLM-based verification\n- Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist [MathCheck] (ICLR 2025) — open-source variant generation pipeline for GSM8K and GeoQA; backup pipeline for variant generation\n- MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations (ICML 2025) — 279 expert-crafted MATH Level-5 perturbations with SymPy verification; demonstrates 10-25% drops on frontier models; open code provides seed perturbations and strongest anchor-assumption validation\n- MathArena: Evaluating LLMs on Uncontaminated Math Competitions (NeurIPS 2025 D&B Track) — expanded to ~900 problems across 2025-2026 competitions including AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, and Apex; our primary ground-truth validation source\n- PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in LLMs (arXiv 2024) — paired original-perturbed items for binary contamination detection via three-step statistical analysis; confirms paired signal without latent-variable modeling; used as convergent validity comparison\n- Redefining Item Response Models for Small Samples [Fox] (Journal of Educational and Behavioral Statistics 2025) — IRT-BCSM integrates out person parameters for stable estimation at N=50-100; RMSE=0.110 for discrimination at N=50 while standard MML collapses (RMSE=1.782); establishes that Bayesian IRT estimation is viable with small person samples\n- On the Identifiability of 3- and 4-Parameter IRT Models From the Perspective of Knowledge Space Theory [Noventa, Ye, Kelava, Spoto] (Psychometrika 2024) — establishes identifiability conditions for 3PL/4PL via knowledge space theory; our G-2PL proof builds on these results with simpler conditions enabled by the 2PL base\n- Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration [Habba, Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Choshen, Stanovsky] (arXiv April 2026) — two-stage MIRT 2PL fixed-parameter calibration on 295+ Open LLM Leaderboard models, <2% MAE with 100 anchor items, ρ≥0.9; validates the two-stage architecture we adopt for item parameter calibration\n- tinyBenchmarks: evaluating LLMs with fewer examples [Polo, Weber, Choshen, Sun, Xu, Stanovsky] (ICML 2024) — assembles per-item binary response data from Open LLM Leaderboard V1 for 395 models × ~29K items; provides the data assembly methodology and validates IRT-based prediction from small item subsets; our Stage 1 calibration follows their data reconstruction approach\n- Robustness of the Hierarchical 2PL Bayesian Model Under Diverse Conditions [Konig, Khorramdel, Falk, Schmitt] (Behavior Research Methods 2023) — OH2PL with half-Cauchy hyperpriors produces unbiased estimates at N=50 (bias ±0.04) while MML yields 75-89% inadmissible solutions; validates hierarchical Bayesian IRT at small sample sizes; 864 conditions × 100 replications across 6 sample sizes\n- Investigating a weakly informative prior for item scale hyperparameters in hierarchical 3PNO IRT models [Luo, Jiao] (Frontiers in Psychology 2017) — half-t priors for hierarchical IRT; informs our prior specification and sensitivity analysis design for the G-2PL contamination parameters\n- py-irt: A Scalable Item Response Theory Library for Python (IJOC 2023) — GPU-accelerated Bayesian IRT fitting via variational inference; comparison estimation method\n- The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models (arXiv April 2026) — reasoning modes (genuine/scaffolding/decorative); provides qualitative taxonomy for interpreting contamination-ability decomposition\n\n## Resource Estimate\n\n- **manual**: gpu_hours: ~200 H100-hrs (Stage 1 data assembly: 0 GPU / 1 day engineering for GSM8K, 15 hrs for MATH-500 model evaluation; variant generation: 25 hrs with Qwen3.6-27B; open-weight inference on variants: 80 hrs across 10 models; gap-filling original inference: 40 hrs; synthetic contamination fine-tuning of OLMo-2-13B: 5 hrs; buffer: 10 hrs; simulation study: ~150 CPU-hrs / 0 GPU; prior sensitivity: ~10 CPU-hrs / 0 GPU), timeline: 8 weeks (1 researcher: wk1 pipeline+V1 data assembly+variant generation start, wk2 variant generation completion+Stage 1 2PL calibration, wk3 inference+Stage 2 data collection, wk4 G-2PL+R-G-2PL implementation in NumPyro+simulation study (1-2 days CPU), wk5 fitting on real data+prior sensitivity analysis+synthetic contamination experiment, wk6 validation+ablations+RankLLM comparison, wk7-8 writing+proofs+residual analysis), estimated_gpu_cost: $2,100 ($600 GPU compute at $3/hr + $1,400 closed-model API for 8 models × 1K items × ~$0.002/item avg + $100 OLMo fine-tuning)\n- **human_in_loop**: gpu_hours: ~170 H100-hrs (aggressive leaderboard data reuse for Stage 1, focused variant generation on GSM8K only for initial submission, MATH-500 as ablation, skip MATH-500 Stage 1 model evaluation), timeline: 6 weeks, claude_api_cost: $300 (G-2PL+R-G-2PL model implementation in NumPyro, identifiability proof verification, simulation study scripting, residual analysis scripts, RankLLM baseline implementation, prior sensitivity analysis, paper drafting), estimated_gpu_cost: $1,900 ($510 GPU + $1,390 closed-model APIs)\n- **auto_research**: gpu_hours: ~230 H100-hrs (full 20-model coverage, automated hyperparameter sweeps over R-G-2PL/G-2PL/G-3PL variants, extended MATH-500 coverage with Stage 1 calibration, synthetic contamination experiment with 3 fine-tuning recipes, 1000-replication simulation study), timeline: 4 weeks (parallel inference, automated ablation grid), claude_api_cost: $950 (variant generation QA, pipeline orchestration, automated ablation analysis including R-G-2PL vs G-2PL comparison, simulation study analysis, prior sensitivity, draft writing, RankLLM reimplementation), estimated_gpu_cost: $2,600 ($690 GPU + $1,910 closed-model APIs), speed_bottleneck: Sequential GPU inference for MoE models (DeepSeek-V4-Flash on 2×H100, Qwen3.5-397B on 4×H100, GLM-5.1 on 4×H100); MCMC fitting with 4 chains is parallelizable but takes ~30 min on CPU; simulation study is embarrassingly parallel across conditions\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T14:03:21.772Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T14:03:21.772Z",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

## Round 1

62 recorded events

### User

_source line 3 · 2026-05-28T14:03:21.796Z_

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
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "3f02069f-ab42-4232-a903-af4a529523d5",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T14:03:21.792Z_

```json
{
  "parentUuid": "3f02069f-ab42-4232-a903-af4a529523d5",
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
  "uuid": "70699575-00f8-4e08-94e5-39b45722add9",
  "timestamp": "2026-05-28T14:03:21.792Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T14:03:21.792Z_

```json
{
  "parentUuid": "70699575-00f8-4e08-94e5-39b45722add9",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "88ffd811-4773-4220-a1a8-b0ae48025134",
  "timestamp": "2026-05-28T14:03:21.792Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
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
  "leafUuid": "88ffd811-4773-4220-a1a8-b0ae48025134",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-ability decomposition via gated IRT",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Assistant

_source line 8 · 2026-05-28T14:03:31.208Z_

<details><summary>Logged reasoning block</summary>

```text
This is a detailed research proposal for CRADE (Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items). I need to evaluate this proposal's idea quality for AAAI 2026 submission potential.

Before I can give a proper evaluation, I need to do thorough literature research. Let me search for the key related works and the current state of this research area.

Let me search for:
1. IRT-based LLM evaluation (PSN-IRT, RankLLM, Growing Pains)
2. Contamination detection/correction (DCR, ConStat, JECS, Wang et al. ICLR 2026)


3. Adversarial robustness testing for math (MaSTer, MATH-Perturb)
4. DGM (Deterministic Gated IRT Model) from psychometrics
5. Any existing work on joint contamination-ability decomposition

I'll start by loading the WebSearch tool to find these papers and understand the current landscape.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "88ffd811-4773-4220-a1a8-b0ae48025134",
  "isSidechain": false,
  "requestId": "req_011CbV6GqdKFKFkLPTPjfPSs",
  "type": "assistant",
  "uuid": "4d7ebb9a-eee7-4595-83d4-e6294398fd4a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdxtyyZexsJ1xuPUehy7MM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16246,
      "cache_read_input_tokens": 11014,
      "output_tokens": 324,
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
          "output_tokens": 324,
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

_source line 9 · 2026-05-28T14:03:31.212Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_018CNyyo7bfga9jasvSpub2i`</summary>

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
  "parentUuid": "4d7ebb9a-eee7-4595-83d4-e6294398fd4a",
  "isSidechain": false,
  "requestId": "req_011CbV6GqdKFKFkLPTPjfPSs",
  "type": "assistant",
  "uuid": "9d8a5176-49ed-459a-b88a-63fd72b08adb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FdxtyyZexsJ1xuPUehy7MM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16246,
      "cache_read_input_tokens": 11014,
      "output_tokens": 324,
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
          "output_tokens": 324,
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

_source line 10 · 2026-05-28T14:03:31.222Z_

<details><summary>↩ Tool result · `toolu_018CNyyo7bfga9jasvSpub2i`</summary>

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
  "parentUuid": "9d8a5176-49ed-459a-b88a-63fd72b08adb",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "08df895d-9ea4-440e-8cc9-0aa14739d3fc",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "9d8a5176-49ed-459a-b88a-63fd72b08adb",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-28T14:03:34.458Z_

<details><summary>Logged reasoning block</summary>

```text
Now let me conduct thorough literature research. I'll search for the key topics in parallel.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "08df895d-9ea4-440e-8cc9-0aa14739d3fc",
  "isSidechain": false,
  "requestId": "req_011CbV6HYNWvTpBVrCudLJkT",
  "type": "assistant",
  "uuid": "79d3b840-c295-40e0-81f8-5b70cd728010",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ak7nmvrUjNannLikiHXAr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 27260,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 27260,
          "cache_creation_input_tokens": 851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 851
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

_source line 12 · 2026-05-28T14:03:34.966Z_

Let me conduct the required literature research before evaluating this proposal. I'll search for the key related works and current state of the field.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79d3b840-c295-40e0-81f8-5b70cd728010",
  "isSidechain": false,
  "requestId": "req_011CbV6HYNWvTpBVrCudLJkT",
  "type": "assistant",
  "uuid": "55b5f278-8f37-4000-abdf-4e6bb143edca",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ak7nmvrUjNannLikiHXAr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 27260,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 27260,
          "cache_creation_input_tokens": 851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 851
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

_source line 13 · 2026-05-28T14:03:35.293Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01FBs1x3uyCUJrHT4xpPghLm`</summary>

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
  "parentUuid": "55b5f278-8f37-4000-abdf-4e6bb143edca",
  "isSidechain": false,
  "requestId": "req_011CbV6HYNWvTpBVrCudLJkT",
  "type": "assistant",
  "uuid": "81184397-6b53-4f0c-8b55-72c3cae60266",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015ak7nmvrUjNannLikiHXAr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 851,
      "cache_read_input_tokens": 27260,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 851,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 134,
          "cache_read_input_tokens": 27260,
          "cache_creation_input_tokens": 851,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 851
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

_source line 14 · 2026-05-28T14:03:43.919Z_

<details><summary>↩ Tool result · `toolu_01FBs1x3uyCUJrHT4xpPghLm`</summary>

```text
Web search results for query: "PSN-IRT item response theory LLM evaluation AAAI 2026"

Links: [{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v3"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://ojs.aaai.org/index.php/AAAI/article/download/40814/44775"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"},{"title":"When Classical Test Theory Alone Is Not Enough: How Item Response Theory + Psychometrics Strengthen Modern LLM Evaluation | by Lulu Yan | Medium","url":"https://luluyan.medium.com/why-classical-test-theory-falls-short-for-llm-evaluation-and-how-item-response-theory-irt-93f03f3b6a2a"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory","url":"https://arxiv.org/pdf/2509.22888"}]

Based on the search results, here's what I found about PSN-IRT:

## Overview

PSN-IRT is a framework based on Item Response Theory (IRT) for a deep analysis of LLM benchmark quality. The paper is an AAAI 2026 Oral presentation titled "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory."

## Framework Details

PSN-IRT is an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture. PSN-IRT processes model identifiers and item identifiers through independent neural network pathways, which respectively estimate latent model ability and a rich set of item parameters.

## Key Findings

The researchers conducted extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. The main findings include:

- LLM benchmarks fail to achieve simultaneous excellence across multiple measurements.
- LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and accurately evaluate advanced models.
- LLM benchmarks exhibit data contamination in numerous items, compromising their reliability.

## Practical Applications

The research demonstrates that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "81184397-6b53-4f0c-8b55-72c3cae60266",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "11144268-d250-4815-bed6-db757a487de2",
  "toolUseResult": {
    "query": "PSN-IRT item response theory LLM evaluation AAAI 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01V1cTgEBi91fnizczE2xodh",
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
      "Based on the search results, here's what I found about PSN-IRT:\n\n## Overview\n\nPSN-IRT is a framework based on Item Response Theory (IRT) for a deep analysis of LLM benchmark quality. The paper is an AAAI 2026 Oral presentation titled \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory.\"\n\n## Framework Details\n\nPSN-IRT is an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture. PSN-IRT processes model identifiers and item identifiers through independent neural network pathways, which respectively estimate latent model ability and a rich set of item parameters.\n\n## Key Findings\n\nThe researchers conducted extensive analysis on 11 LLM benchmarks comprising 41,871 items, revealing significant and varied shortcomings in their measurement quality. The main findings include:\n\n- LLM benchmarks fail to achieve simultaneous excellence across multiple measurements.\n- LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, limiting their ability to challenge and accurately evaluate advanced models.\n- LLM benchmarks exhibit data contamination in numerous items, compromising their reliability.\n\n## Practical Applications\n\nThe research demonstrates that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference."
    ],
    "durationSeconds": 8.618719868,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "81184397-6b53-4f0c-8b55-72c3cae60266",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T14:03:46.565Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01EudzQMAMRrdmCyekpefyJE`</summary>

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
  "parentUuid": "11144268-d250-4815-bed6-db757a487de2",
  "isSidechain": false,
  "requestId": "req_011CbV6JTzcxKDz682T6UAvq",
  "type": "assistant",
  "uuid": "3157a64f-2e63-459b-8e2a-f935cebe5326",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01RdVssq8bDV2vRbuV9p4ZDU",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1058,
      "cache_read_input_tokens": 28111,
      "output_tokens": 67,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1058,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 67,
          "cache_read_input_tokens": 28111,
          "cache_creation_input_tokens": 1058,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1058
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

_source line 16 · 2026-05-28T14:03:52.779Z_

<details><summary>↩ Tool result · `toolu_01EudzQMAMRrdmCyekpefyJE`</summary>

```text
Web search results for query: "RankLLM weighted ranking question difficulty ICLR 2026"

Links: [{"title":"RANKLLM: WEIGHTED RANKING OF LLMS BY QUAN","url":"https://openreview.net/pdf/c22aab26d0cee50994697242fa86488f0f24707d.pdf"},{"title":"(PDF) RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://www.researchgate.net/publication/400812163_RankLLM_Weighted_Ranking_of_LLMs_by_Quantifying_Question_Difficulty"},{"title":"[2602.12424v1] RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://arxiv.org/abs/2602.12424v1"},{"title":"[2602.12424] RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://arxiv.org/abs/2602.12424"},{"title":"RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty | OpenReview","url":"https://openreview.net/forum?id=jnX5GJIoYt"},{"title":"RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://arxiv.org/html/2602.12424"}]

Based on the search results, here's what I found about RankLLM:

## Overview

RankLLM is a novel framework designed to quantify both question difficulty and model competency, introducing difficulty as the primary criterion for differentiation to enable a more fine-grained evaluation of LLM capabilities.

## Core Mechanism

RankLLM's core mechanism facilitates bidirectional score propagation between models and questions, where a model earns a competency score when it correctly answers a question, while a question's difficulty score increases when it challenges a model.

RankLLM constructs a directed bipartite interaction graph between models and questions and performs damped bidirectional score propagation: solving a hard question carries more evidential weight for competency; failing an easy question contributes more weight to difficulty.

## Key Results

RankLLM achieves 90% agreement with human judgments and consistently outperforms strong baselines such as IRT, while exhibiting strong stability, fast convergence, and high computational efficiency. The framework was evaluated on 30 models across 35,550 questions across multiple domains.

## Publication Status

The paper was published as a conference paper at ICLR 2026.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3157a64f-2e63-459b-8e2a-f935cebe5326",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "76de8ec2-dee5-4127-8bb0-7d67c3cc9767",
  "toolUseResult": {
    "query": "RankLLM weighted ranking question difficulty ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016NDxQmyET1XQ7TmEdzQmRc",
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
      "Based on the search results, here's what I found about RankLLM:\n\n## Overview\n\nRankLLM is a novel framework designed to quantify both question difficulty and model competency, introducing difficulty as the primary criterion for differentiation to enable a more fine-grained evaluation of LLM capabilities.\n\n## Core Mechanism\n\nRankLLM's core mechanism facilitates bidirectional score propagation between models and questions, where a model earns a competency score when it correctly answers a question, while a question's difficulty score increases when it challenges a model.\n\nRankLLM constructs a directed bipartite interaction graph between models and questions and performs damped bidirectional score propagation: solving a hard question carries more evidential weight for competency; failing an easy question contributes more weight to difficulty.\n\n## Key Results\n\nRankLLM achieves 90% agreement with human judgments and consistently outperforms strong baselines such as IRT, while exhibiting strong stability, fast convergence, and high computational efficiency. The framework was evaluated on 30 models across 35,550 questions across multiple domains.\n\n## Publication Status\n\nThe paper was published as a conference paper at ICLR 2026."
    ],
    "durationSeconds": 6.208583235000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3157a64f-2e63-459b-8e2a-f935cebe5326",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T14:03:55.409Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B3b1x7FFLxwg4bXcwrJvPz`</summary>

```json
{
  "query": "DCR data contamination correction LLM EMNLP 2025 benchmark evaluation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "76de8ec2-dee5-4127-8bb0-7d67c3cc9767",
  "isSidechain": false,
  "requestId": "req_011CbV6K7ox95XZeQrJckNAB",
  "type": "assistant",
  "uuid": "ebfd3e10-5246-4199-b3d3-05763fe07d54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WEfiEPuwPops5z38w8soB7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 29169,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 29169,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 18 · 2026-05-28T14:04:03.409Z_

<details><summary>↩ Tool result · `toolu_01B3b1x7FFLxwg4bXcwrJvPz`</summary>

```text
Web search results for query: "DCR data contamination correction LLM EMNLP 2025 benchmark evaluation"

Links: [{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1173/"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/pdf/2507.11405"},{"title":"[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/abs/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/html/2507.11405"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation","url":"https://arxiv.org/html/2502.17521v2"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"},{"title":"Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.511/"},{"title":"Generalization or Memorization: Data Contamination and Trustworthy   Evaluation for Large Language Models","url":"https://arxiv.org/pdf/2402.15938"},{"title":"(PDF) NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark","url":"https://www.researchgate.net/publication/376393345_NLP_Evaluation_in_trouble_On_the_Need_to_Measure_LLM_Data_Contamination_for_each_Benchmark"}]

I found relevant results for your search query. Here's what I found:

## DCR: Quantifying Data Contamination in LLMs Evaluation

The DCR (Data Contamination Risk) framework was introduced by Cheng Xu and colleagues at EMNLP 2025 to address benchmark data contamination (BDC), where models inadvertently memorize evaluation data during the training process, inflating performance metrics and undermining genuine generalization assessment.

### Framework Overview

The DCR framework is a lightweight, interpretable pipeline designed to detect and quantify BDC risk across four granular levels: semantic, informational, data, and label. By synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance.

### Evaluation & Validation

The DCR framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, reliably diagnosing contamination severity with accuracy adjusted using the DCR Factor to within 4% average error across the three benchmarks compared to the uncontaminated baseline.

### Practical Applications

The framework emphasizes computational efficiency and transparency, providing a practical tool for integrating contamination assessment into routine evaluations, fostering fairer comparisons and enhancing the credibility of LLM benchmarking practices.

The paper was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) in Suzhou, China.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ebfd3e10-5246-4199-b3d3-05763fe07d54",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "9f8e8589-a4e8-4635-834b-b5daee53da2c",
  "toolUseResult": {
    "query": "DCR data contamination correction LLM EMNLP 2025 benchmark evaluation",
    "results": [
      {
        "tool_use_id": "srvtoolu_01WxkqNAroaHCXzkTTuvXeMy",
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
            "title": "[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://arxiv.org/abs/2507.11405"
          },
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://arxiv.org/html/2507.11405"
          },
          {
            "title": "Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation",
            "url": "https://arxiv.org/html/2502.17521v2"
          },
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://aclanthology.org/2025.emnlp-main.1173.pdf"
          },
          {
            "title": "Benchmarking Large Language Models Under Data Contamination: A Survey from Static to Dynamic Evaluation - ACL Anthology",
            "url": "https://aclanthology.org/2025.emnlp-main.511/"
          },
          {
            "title": "Generalization or Memorization: Data Contamination and Trustworthy   Evaluation for Large Language Models",
            "url": "https://arxiv.org/pdf/2402.15938"
          },
          {
            "title": "(PDF) NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark",
            "url": "https://www.researchgate.net/publication/376393345_NLP_Evaluation_in_trouble_On_the_Need_to_Measure_LLM_Data_Contamination_for_each_Benchmark"
          }
        ]
      },
      "I found relevant results for your search query. Here's what I found:\n\n## DCR: Quantifying Data Contamination in LLMs Evaluation\n\nThe DCR (Data Contamination Risk) framework was introduced by Cheng Xu and colleagues at EMNLP 2025 to address benchmark data contamination (BDC), where models inadvertently memorize evaluation data during the training process, inflating performance metrics and undermining genuine generalization assessment.\n\n### Framework Overview\n\nThe DCR framework is a lightweight, interpretable pipeline designed to detect and quantify BDC risk across four granular levels: semantic, informational, data, and label. By synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance.\n\n### Evaluation & Validation\n\nThe DCR framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, reliably diagnosing contamination severity with accuracy adjusted using the DCR Factor to within 4% average error across the three benchmarks compared to the uncontaminated baseline.\n\n### Practical Applications\n\nThe framework emphasizes computational efficiency and transparency, providing a practical tool for integrating contamination assessment into routine evaluations, fostering fairer comparisons and enhancing the credibility of LLM benchmarking practices.\n\nThe paper was published in the Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025) in Suzhou, China."
    ],
    "durationSeconds": 7.994543831000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ebfd3e10-5246-4199-b3d3-05763fe07d54",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T14:04:06.580Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XdHBnJeAJSdWscnUkX6Dec`</summary>

```json
{
  "query": "Wang Li Ko Zhang \"fragility benchmark contamination detection reasoning models\" ICLR 2026 likelihood-based"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9f8e8589-a4e8-4635-834b-b5daee53da2c",
  "isSidechain": false,
  "requestId": "req_011CbV6KuFgdttbpqHm3WK46",
  "type": "assistant",
  "uuid": "be9239aa-4c20-40fe-8dbd-f2d8ff699026",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MBco8pKWJWMVawpmayfMt3",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 933,
      "cache_read_input_tokens": 29896,
      "output_tokens": 76,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 933,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 76,
          "cache_read_input_tokens": 29896,
          "cache_creation_input_tokens": 933,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 933
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

_source line 20_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "be9239aa-4c20-40fe-8dbd-f2d8ff699026",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Runtime record

_source line 21_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-ability decomposition via gated IRT",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Tool result

_source line 22 · 2026-05-28T14:04:13.244Z_

<details><summary>↩ Tool result · `toolu_01XdHBnJeAJSdWscnUkX6Dec`</summary>

```text
Web search results for query: "Wang Li Ko Zhang "fragility benchmark contamination detection reasoning models" ICLR 2026 likelihood-based"

Links: [{"title":"Carnegie Mellon at ICLR 2026 – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2026/04/20/carnegie-mellon-at-iclr-2026/"},{"title":"[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/abs/2510.02386"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/html/2510.02386v1"},{"title":"detecting data contamination from reinforcement learning ...","url":"https://arxiv.org/pdf/2510.09259"}]

I found the paper you were searching for! The paper is titled "On The Fragility of Benchmark Contamination Detection in Reasoning Models" with authors Han Wang (University of Illinois at Urbana-Champaign), Haoyu Li (University of Illinois at Urbana-Champaign), Brian Ko (University of Washington), and Huan Zhang (CMU), and it was presented at ICLR 2026.

The study finds that evading contamination detections for large reasoning models is alarmingly easy. When a base model evolves into an LRM via SFT and RL, contamination during SFT can be identified by contamination detection methods, but even brief GRPO training can markedly conceal contamination signals that most detection methods rely on.

The paper addresses the challenge of detecting benchmark contamination in the context of large reasoning models and reveals vulnerabilities in existing detection approaches, particularly how reinforcement learning techniques can obscure signals that likelihood-based detectors typically identify.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "be9239aa-4c20-40fe-8dbd-f2d8ff699026",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "8b559bfa-ec90-4661-b376-75c024d46237",
  "toolUseResult": {
    "query": "Wang Li Ko Zhang \"fragility benchmark contamination detection reasoning models\" ICLR 2026 likelihood-based",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AXTkeDteVKqPVG6uJV7ZMe",
        "content": [
          {
            "title": "Carnegie Mellon at ICLR 2026 – Machine Learning Blog | ML@CMU | Carnegie Mellon University",
            "url": "https://blog.ml.cmu.edu/2026/04/20/carnegie-mellon-at-iclr-2026/"
          },
          {
            "title": "[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/abs/2510.02386"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/pdf/2510.02386"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/html/2510.02386v1"
          },
          {
            "title": "detecting data contamination from reinforcement learning ...",
            "url": "https://arxiv.org/pdf/2510.09259"
          }
        ]
      },
      "I found the paper you were searching for! The paper is titled \"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" with authors Han Wang (University of Illinois at Urbana-Champaign), Haoyu Li (University of Illinois at Urbana-Champaign), Brian Ko (University of Washington), and Huan Zhang (CMU), and it was presented at ICLR 2026.\n\nThe study finds that evading contamination detections for large reasoning models is alarmingly easy. When a base model evolves into an LRM via SFT and RL, contamination during SFT can be identified by contamination detection methods, but even brief GRPO training can markedly conceal contamination signals that most detection methods rely on.\n\nThe paper addresses the challenge of detecting benchmark contamination in the context of large reasoning models and reveals vulnerabilities in existing detection approaches, particularly how reinforcement learning techniques can obscure signals that likelihood-based detectors typically identify."
    ],
    "durationSeconds": 6.658950620000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "be9239aa-4c20-40fe-8dbd-f2d8ff699026",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 23 · 2026-05-28T14:04:17.008Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01XR3R6GGN3xWp4vwHc8uuxV`</summary>

```json
{
  "query": "Growing Pains extensible LLM benchmarking fixed parameter calibration IRT 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8b559bfa-ec90-4661-b376-75c024d46237",
  "isSidechain": false,
  "requestId": "req_011CbV6LdUgXxfEUv1pXkUPU",
  "type": "assistant",
  "uuid": "2b30ba81-9b21-450d-b9a0-ca839ca63670",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017vribYFofsWxBf8hWvAe2n",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 649,
      "cache_read_input_tokens": 30829,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 649,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 30829,
          "cache_creation_input_tokens": 649,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 649
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

_source line 24 · 2026-05-28T14:04:24.485Z_

<details><summary>↩ Tool result · `toolu_01XR3R6GGN3xWp4vwHc8uuxV`</summary>

```text
Web search results for query: "Growing Pains extensible LLM benchmarking fixed parameter calibration IRT 2026"

Links: [{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"Agent psychometrics: Task-level performance prediction in agentic coding benchmarks","url":"https://arxiv.org/pdf/2604.00594"},{"title":"Preprint. Accepted at the ICLR 2026 LIT Workshop","url":"https://arxiv.org/pdf/2602.09924"},{"title":"LLM Evaluation and Benchmarking 2026 | Zylos Research","url":"https://zylos.ai/research/2026-01-16-llm-evaluation-benchmarking"}]

I found relevant results for your search. Here's what I discovered:

## Growing Pains: Extensible LLM Benchmarking

The paper proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.

### Key Features

The research addresses the problem that the rapid release of both language models and benchmarks makes it increasingly costly to evaluate every model on every dataset, and in practice, models are often evaluated on different samples, making scores difficult to compare across studies.

The approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.

### Performance Results

In large-scale experiments on more than 400 models, the framework predicts full-evaluation performance within 2-3 percentage points using only 100 anchor questions per dataset, with Spearman ρ≥0.9 for ranking preservation.

The paper was published on arXiv in April 2026, and code is available at https://github.com/eliyahabba/growing-pains/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "2b30ba81-9b21-450d-b9a0-ca839ca63670",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "bc3b9949-fc4e-4ad9-97fb-0cad8ea273bd",
  "toolUseResult": {
    "query": "Growing Pains extensible LLM benchmarking fixed parameter calibration IRT 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01AhSqgkBSAMJcfzh893FGXw",
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
      "I found relevant results for your search. Here's what I discovered:\n\n## Growing Pains: Extensible LLM Benchmarking\n\nThe paper proposes a framework based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.\n\n### Key Features\n\nThe research addresses the problem that the rapid release of both language models and benchmarks makes it increasingly costly to evaluate every model on every dataset, and in practice, models are often evaluated on different samples, making scores difficult to compare across studies.\n\nThe approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.\n\n### Performance Results\n\nIn large-scale experiments on more than 400 models, the framework predicts full-evaluation performance within 2-3 percentage points using only 100 anchor questions per dataset, with Spearman ρ≥0.9 for ranking preservation.\n\nThe paper was published on arXiv in April 2026, and code is available at https://github.com/eliyahabba/growing-pains/."
    ],
    "durationSeconds": 7.472377699999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "2b30ba81-9b21-450d-b9a0-ca839ca63670",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T14:04:27.156Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01S82v6kbXNsBY6FJ5PSDzqT`</summary>

```json
{
  "query": "JECS joint envelope conformal selection decontamination LLM benchmark 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bc3b9949-fc4e-4ad9-97fb-0cad8ea273bd",
  "isSidechain": false,
  "requestId": "req_011CbV6MTPEjdfbcsjfrvfKs",
  "type": "assistant",
  "uuid": "6288a04e-c4a0-4ec2-9be1-f14894fde861",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012B49g9RQThHPzT38D8HZ4d",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 727,
      "cache_read_input_tokens": 31478,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 727,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 31478,
          "cache_creation_input_tokens": 727,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 727
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

_source line 26 · 2026-05-28T14:04:35.608Z_

<details><summary>↩ Tool result · `toolu_01S82v6kbXNsBY6FJ5PSDzqT`</summary>

```text
Web search results for query: "JECS joint envelope conformal selection decontamination LLM benchmark 2026"

Links: [{"title":"[2605.21543] Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/abs/2605.21543"},{"title":"Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/html/2605.21543"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"},{"title":"PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines","url":"https://arxiv.org/html/2605.18812"},{"title":"An Expert-grounded benchmark of General Purpose LLMs in LCA","url":"https://arxiv.org/pdf/2510.19886"}]

Based on the search results, I found relevant information about your query:

JECS (Joint Envelope Conformal Selection) is a conformal procedure that formalizes multi-model benchmark decontamination as a joint selection problem and enables global contamination rate (GCR) control under stated assumptions.

The work addresses benchmark data contamination, which is a central challenge in LLM evaluation where evaluation examples appear in the training data of one or more audited models, causing reported performance to be inflated and cross-model comparisons to become unreliable.

Specifically, JECS computes per-model conformal p-values, aggregates them by the per-item maximum, and reconstructs a conservative envelope of the max-p null distribution. It then applies the adaptive Benjamini-Hochberg procedure to the envelope-rescaled values to select a benchmark with provable GCR control.

The paper appears to have been uploaded to arXiv about a week ago (arxiv 2605.21543) and represents recent research on addressing benchmark contamination in LLM evaluation.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6288a04e-c4a0-4ec2-9be1-f14894fde861",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "f11d54af-7326-4c9a-aeee-45bd082f6269",
  "toolUseResult": {
    "query": "JECS joint envelope conformal selection decontamination LLM benchmark 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Xng8avuJMQtpQLrd26Ar3b",
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
            "title": "PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines",
            "url": "https://arxiv.org/html/2605.18812"
          },
          {
            "title": "An Expert-grounded benchmark of General Purpose LLMs in LCA",
            "url": "https://arxiv.org/pdf/2510.19886"
          }
        ]
      },
      "Based on the search results, I found relevant information about your query:\n\nJECS (Joint Envelope Conformal Selection) is a conformal procedure that formalizes multi-model benchmark decontamination as a joint selection problem and enables global contamination rate (GCR) control under stated assumptions.\n\nThe work addresses benchmark data contamination, which is a central challenge in LLM evaluation where evaluation examples appear in the training data of one or more audited models, causing reported performance to be inflated and cross-model comparisons to become unreliable.\n\nSpecifically, JECS computes per-model conformal p-values, aggregates them by the per-item maximum, and reconstructs a conservative envelope of the max-p null distribution. It then applies the adaptive Benjamini-Hochberg procedure to the envelope-rescaled values to select a benchmark with provable GCR control.\n\nThe paper appears to have been uploaded to arXiv about a week ago (arxiv 2605.21543) and represents recent research on addressing benchmark contamination in LLM evaluation."
    ],
    "durationSeconds": 8.445558277000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6288a04e-c4a0-4ec2-9be1-f14894fde861",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T14:04:38.908Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014hFFgU8hZk3peCKBB1zJKS`</summary>

```json
{
  "query": "Shu Henson Luecht \"deterministic gated item response theory\" cheating item compromise Psychometrika 2013"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f11d54af-7326-4c9a-aeee-45bd082f6269",
  "isSidechain": false,
  "requestId": "req_011CbV6NGxhhLAzPyWKvxzbn",
  "type": "assistant",
  "uuid": "bf51f8c5-beb1-45c7-8607-4297d655b269",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_014vrKj2J5HeEgA3Ni3CayEz",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 586,
      "cache_read_input_tokens": 32205,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 586,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 32205,
          "cache_creation_input_tokens": 586,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 586
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

_source line 28 · 2026-05-28T14:04:44.892Z_

<details><summary>↩ Tool result · `toolu_014hFFgU8hZk3peCKBB1zJKS`</summary>

```text
Web search results for query: "Shu Henson Luecht "deterministic gated item response theory" cheating item compromise Psychometrika 2013"

Links: [{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11336-012-9311-3"},{"title":"Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/25106396/"},{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Cambridge Core","url":"https://www.cambridge.org/core/journals/psychometrika/article/abs/using-deterministic-gated-item-response-theory-model-to-detect-test-cheating-due-to-item-compromise/34FE98C0FA7367881713D0019619E53E"},{"title":"(PDF) Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise","url":"https://www.researchgate.net/publication/257678777_Using_Deterministic_Gated_Item_Response_Theory_Model_to_Detect_Test_Cheating_due_to_Item_Compromise"},{"title":"Item pre-knowledge true prevalence in clinical anatomy - application of gated item response theory model","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6659220/"},{"title":"Combining Item Response Theory and Diagnostic Classification Models: A Psychometric Model for Scaling Ability and Diagnosing Misconceptions | Psychometrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11336-013-9350-4"}]

I found the article you were searching for. The paper "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise" was authored by Shu, Z., Henson, R., and Luecht, R., and was published in Psychometrika in 2013 (Volume 78, pages 481-497).

The Deterministic, Gated Item Response Theory Model (DGM) is proposed to identify cheaters who obtain significant score gain on tests due to item exposure/compromise by conditioning on the item status (exposed or unexposed items). A "gated" function is introduced to decompose the observed examinees' performance into two distributions (the true ability distribution determined by examinees' true ability and the cheating distribution determined by examinees' cheating ability).

The article is available through multiple sources including Springer Nature Link at https://link.springer.com/article/10.1007/s11336-012-9311-3.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf51f8c5-beb1-45c7-8607-4297d655b269",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "1f09bc3e-6b1c-4751-bf20-6e61b7f8c9d0",
  "toolUseResult": {
    "query": "Shu Henson Luecht \"deterministic gated item response theory\" cheating item compromise Psychometrika 2013",
    "results": [
      {
        "tool_use_id": "srvtoolu_011yYBbmx2VqSGVp2QxaTTDH",
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
      "I found the article you were searching for. The paper \"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\" was authored by Shu, Z., Henson, R., and Luecht, R., and was published in Psychometrika in 2013 (Volume 78, pages 481-497).\n\nThe Deterministic, Gated Item Response Theory Model (DGM) is proposed to identify cheaters who obtain significant score gain on tests due to item exposure/compromise by conditioning on the item status (exposed or unexposed items). A \"gated\" function is introduced to decompose the observed examinees' performance into two distributions (the true ability distribution determined by examinees' true ability and the cheating distribution determined by examinees' cheating ability).\n\nThe article is available through multiple sources including Springer Nature Link at https://link.springer.com/article/10.1007/s11336-012-9311-3."
    ],
    "durationSeconds": 5.979429187000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bf51f8c5-beb1-45c7-8607-4297d655b269",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 29 · 2026-05-28T14:04:47.914Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01TybTF4bKXBeVaTBCez2KeG`</summary>

```json
{
  "query": "IRT contamination ability decomposition LLM joint model paired items 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1f09bc3e-6b1c-4751-bf20-6e61b7f8c9d0",
  "isSidechain": false,
  "requestId": "req_011CbV6NyE8ZHiZzFg9G6GFP",
  "type": "assistant",
  "uuid": "d2995371-d7c4-467c-b30d-7b69073021f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01DLY45b6mXffVs8AmHCB2cN",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 814,
      "cache_read_input_tokens": 32791,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 814,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 32791,
          "cache_creation_input_tokens": 814,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 814
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

_source line 30 · 2026-05-28T14:04:56.040Z_

<details><summary>↩ Tool result · `toolu_01TybTF4bKXBeVaTBCez2KeG`</summary>

```text
Web search results for query: "IRT contamination ability decomposition LLM joint model paired items 2025 2026"

Links: [{"title":"(PDF) JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory","url":"https://www.researchgate.net/publication/395969261_JE-IRT_A_Geometric_Lens_on_LLM_Abilities_through_Joint_Embedding_Item_Response_Theory"},{"title":"Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/html/2605.21543"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"[2605.21543] Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/abs/2605.21543"},{"title":"JE-IRT: A Geometric Lens on LLM Abilities through Joint ...","url":"https://www.arxiv.org/pdf/2509.22888"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"}]

I found several relevant research papers on your query. Here are the key findings:

## JE-IRT: Joint Embedding Item Response Theory for LLM Abilities

A 2025 study examined evaluation results across 112 models and 10 benchmarks. The research addresses a fundamental issue: the assumption that a single total order explains correctness across items is violated for LLMs. Specifically, many items show negative or near-zero discrimination, contradicting the monotone-with-ability premise of traditional Item Response Theory.

## Contamination and Decontamination of LLM Benchmarks

Recent work has focused on the challenge of benchmark contamination in LLM evaluation. When evaluation examples appear in the training data of one or more audited models, reported performance can be inflated and cross-model comparisons become unreliable. 

A new approach called Joint Envelope Conformal Selection (JECS) enables global contamination rate control when decontaminating benchmarks across multiple models, addressing the problem that applying contamination detection separately to each model can produce model-specific benchmarks, undermining fair comparison across models.

## Contamination in Psychometric Evaluations

Additionally, frameworks now quantify data contamination across three aspects: item memorization, evaluation memorization, and target score matching in psychometric assessments of LLMs.

These papers represent recent work (2025-2026) at the intersection of IRT methodology, LLM ability decomposition, and contamination detection for fair model comparison.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d2995371-d7c4-467c-b30d-7b69073021f9",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "4339f44f-bff8-4b3a-853d-3deac8684667",
  "toolUseResult": {
    "query": "IRT contamination ability decomposition LLM joint model paired items 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_014Y8HPZZkc1ya3z4mQYUbvu",
        "content": [
          {
            "title": "(PDF) JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory",
            "url": "https://www.researchgate.net/publication/395969261_JE-IRT_A_Geometric_Lens_on_LLM_Abilities_through_Joint_Embedding_Item_Response_Theory"
          },
          {
            "title": "Provable Joint Decontamination for Benchmarking Multiple Large Language Models",
            "url": "https://arxiv.org/html/2605.21543"
          },
          {
            "title": "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide",
            "url": "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
          },
          {
            "title": "[2605.21543] Provable Joint Decontamination for Benchmarking Multiple Large Language Models",
            "url": "https://arxiv.org/abs/2605.21543"
          },
          {
            "title": "JE-IRT: A Geometric Lens on LLM Abilities through Joint ...",
            "url": "https://www.arxiv.org/pdf/2509.22888"
          },
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/pdf/2510.07175"
          }
        ]
      },
      "I found several relevant research papers on your query. Here are the key findings:\n\n## JE-IRT: Joint Embedding Item Response Theory for LLM Abilities\n\nA 2025 study examined evaluation results across 112 models and 10 benchmarks. The research addresses a fundamental issue: the assumption that a single total order explains correctness across items is violated for LLMs. Specifically, many items show negative or near-zero discrimination, contradicting the monotone-with-ability premise of traditional Item Response Theory.\n\n## Contamination and Decontamination of LLM Benchmarks\n\nRecent work has focused on the challenge of benchmark contamination in LLM evaluation. When evaluation examples appear in the training data of one or more audited models, reported performance can be inflated and cross-model comparisons become unreliable. \n\nA new approach called Joint Envelope Conformal Selection (JECS) enables global contamination rate control when decontaminating benchmarks across multiple models, addressing the problem that applying contamination detection separately to each model can produce model-specific benchmarks, undermining fair comparison across models.\n\n## Contamination in Psychometric Evaluations\n\nAdditionally, frameworks now quantify data contamination across three aspects: item memorization, evaluation memorization, and target score matching in psychometric assessments of LLMs.\n\nThese papers represent recent work (2025-2026) at the intersection of IRT methodology, LLM ability decomposition, and contamination detection for fair model comparison."
    ],
    "durationSeconds": 8.120743885000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d2995371-d7c4-467c-b30d-7b69073021f9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 31 · 2026-05-28T14:04:56.045Z_

```json
{
  "parentUuid": "4339f44f-bff8-4b3a-853d-3deac8684667",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "5cf8fba0-7488-46f9-81f2-39335522359c",
  "timestamp": "2026-05-28T14:04:56.045Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 32_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "5cf8fba0-7488-46f9-81f2-39335522359c",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Runtime record

_source line 33_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-ability decomposition via gated IRT",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Tool call

_source line 34 · 2026-05-28T14:04:58.937Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_0147NHCtbu4aeZppZZDuotET`</summary>

```json
{
  "query": "MATH-Perturb benchmark LLM math reasoning perturbation ICML 2025"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5cf8fba0-7488-46f9-81f2-39335522359c",
  "isSidechain": false,
  "requestId": "req_011CbV6PnVjwAWUufkoDLTkc",
  "type": "assistant",
  "uuid": "a010aeec-0f79-4c26-9f76-049e42b22a72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01FkAPmv67eJ4KMfDaLxuepK",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 869,
      "cache_read_input_tokens": 33605,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 869,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 33605,
          "cache_creation_input_tokens": 869,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 869
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

_source line 35 · 2026-05-28T14:05:07.978Z_

<details><summary>↩ Tool result · `toolu_0147NHCtbu4aeZppZZDuotET`</summary>

```text
Web search results for query: "MATH-Perturb benchmark LLM math reasoning perturbation ICML 2025"

Links: [{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview","url":"https://openreview.net/forum?id=OZy70UggXr"},{"title":"GitHub - Kaffaljidhmah2/MATH-Perturb: Evaluation Code and Dataset for [ICML 2025] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://github.com/Kaffaljidhmah2/MATH-Perturb"},{"title":"MATH-Perturb","url":"https://math-perturb.github.io/"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | AI Research Paper Details","url":"https://www.aimodels.fyi/papers/arxiv/math-perturb-benchmarking-llms-math-reasoning-abilities"},{"title":"[2502.06453] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/abs/2502.06453"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://arxiv.org/html/2502.06453v2"},{"title":"MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations","url":"https://proceedings.mlr.press/v267/huang25k.html"},{"title":"ICML Poster MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations","url":"https://icml.cc/virtual/2025/poster/45435"},{"title":"MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard   Perturbations","url":"https://arxiv.org/pdf/2502.06453"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833v1"}]

Based on the search results, here's information about the MATH-Perturb benchmark:

## Overview

MATH-Perturb constructs MATH-P-Simple and MATH-P-Hard to benchmark LLM's math reasoning against simple and hard perturbations, and examine memorization issues.

## Motivation

Large language models have demonstrated impressive performance on challenging mathematical reasoning tasks, which has triggered the discussion of whether the performance is achieved by true reasoning capability or memorization.

## Methodology

Prior work has constructed mathematical benchmarks when questions undergo simple perturbations – modifications that still preserve the underlying reasoning patterns of the solutions. However, no work has explored hard perturbations, which fundamentally change the nature of the problem so that the original solution steps do not apply.

The simple perturbation to the problem is non-essential, so the modified problem can be solved using the same method as the original problem. The hard perturbation changes the problem fundamentally and it requires more difficult problem-solving skills.

## Dataset

Each consists of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset.

## Key Findings

Significant performance drops on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%) were observed.

The research raises concerns about a novel form of memorization where models blindly apply learned problem-solving skills without assessing their applicability to modified contexts.

The paper was accepted at ICML 2025, presented as a poster.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "a010aeec-0f79-4c26-9f76-049e42b22a72",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "de743c0b-a23b-48b1-a113-4d52b668d47e",
  "toolUseResult": {
    "query": "MATH-Perturb benchmark LLM math reasoning perturbation ICML 2025",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Qhy6KVivBx1JGzAbMDu1W3",
        "content": [
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations | OpenReview",
            "url": "https://openreview.net/forum?id=OZy70UggXr"
          },
          {
            "title": "GitHub - Kaffaljidhmah2/MATH-Perturb: Evaluation Code and Dataset for [ICML 2025] MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://github.com/Kaffaljidhmah2/MATH-Perturb"
          },
          {
            "title": "MATH-Perturb",
            "url": "https://math-perturb.github.io/"
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
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations",
            "url": "https://arxiv.org/html/2502.06453v2"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs’ Math Reasoning Abilities against Hard Perturbations",
            "url": "https://proceedings.mlr.press/v267/huang25k.html"
          },
          {
            "title": "ICML Poster MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations",
            "url": "https://icml.cc/virtual/2025/poster/45435"
          },
          {
            "title": "MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard   Perturbations",
            "url": "https://arxiv.org/pdf/2502.06453"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833v1"
          }
        ]
      },
      "Based on the search results, here's information about the MATH-Perturb benchmark:\n\n## Overview\n\nMATH-Perturb constructs MATH-P-Simple and MATH-P-Hard to benchmark LLM's math reasoning against simple and hard perturbations, and examine memorization issues.\n\n## Motivation\n\nLarge language models have demonstrated impressive performance on challenging mathematical reasoning tasks, which has triggered the discussion of whether the performance is achieved by true reasoning capability or memorization.\n\n## Methodology\n\nPrior work has constructed mathematical benchmarks when questions undergo simple perturbations – modifications that still preserve the underlying reasoning patterns of the solutions. However, no work has explored hard perturbations, which fundamentally change the nature of the problem so that the original solution steps do not apply.\n\nThe simple perturbation to the problem is non-essential, so the modified problem can be solved using the same method as the original problem. The hard perturbation changes the problem fundamentally and it requires more difficult problem-solving skills.\n\n## Dataset\n\nEach consists of 279 perturbed math problems derived from level-5 (hardest) problems in the MATH dataset.\n\n## Key Findings\n\nSignificant performance drops on MATH-P-Hard across various models, including o1-mini (-16.49%) and gemini-2.0-flash-thinking (-12.9%) were observed.\n\nThe research raises concerns about a novel form of memorization where models blindly apply learned problem-solving skills without assessing their applicability to modified contexts.\n\nThe paper was accepted at ICML 2025, presented as a poster."
    ],
    "durationSeconds": 9.033896381999991,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "a010aeec-0f79-4c26-9f76-049e42b22a72",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 36 · 2026-05-28T14:05:11.455Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HYVok1uRuFQZUrXm5agkGz`</summary>

```json
{
  "query": "MaSTer automated robustness evaluation mathematical reasoning adversarial rewrite 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "de743c0b-a23b-48b1-a113-4d52b668d47e",
  "isSidechain": false,
  "requestId": "req_011CbV6QfQP7r7xSD965DvKE",
  "type": "assistant",
  "uuid": "bf71b5f1-17c1-430c-bcee-002e48e4806b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0116pjBELp3f9t8KX88C8nZk",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1053,
      "cache_read_input_tokens": 34474,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1053,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 34474,
          "cache_creation_input_tokens": 1053,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1053
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

_source line 37 · 2026-05-28T14:05:20.055Z_

<details><summary>↩ Tool result · `toolu_01HYVok1uRuFQZUrXm5agkGz`</summary>

```text
Web search results for query: "MaSTer automated robustness evaluation mathematical reasoning adversarial rewrite 2026"

Links: [{"title":"[2506.05038] Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/abs/2506.05038"},{"title":"Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/html/2506.05038"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.04120"},{"title":"MSCR: Exploring the Vulnerability of LLMs' Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement","url":"https://arxiv.org/pdf/2511.08055"},{"title":"Model-Agnostic Meta-Attack: Towards Reliable Evaluation of Adversarial   Robustness","url":"https://arxiv.org/pdf/2110.08256"},{"title":"Is Your Model Really A Good Math Reasoner? Evaluating Mathematical   Reasoning with Checklist","url":"https://arxiv.org/pdf/2407.08733"},{"title":"MSCR: Exploring the Vulnerability of LLMs’ Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement","url":"https://arxiv.org/html/2511.08055"},{"title":"From Accuracy to Robustness: A Study of Rule- and Model-based Verifiers in Mathematical Reasoning","url":"https://arxiv.org/html/2505.22203v2"}]

Based on the search results, I found relevant information about MaSTer:

MaSTer (Math Stress Tester) is a framework designed to automatically expose the latent vulnerabilities of target large language models, inspired by stress testing in software engineering. 

MaSTer generates adversarial variants via a multi-round rewrite-verify loop, ensuring semantic consistency while successfully inducing model failure. More specifically, the rewriter rewrites mathematical problems into their variants while keeping the core meaning unchanged, and the verifier checks whether the core meaning of the original question is preserved and whether the target LLM's answer to the rewritten variant is different from the correct answer.

The framework generates benchmark variants dynamically for each LLM, thus minimizing the risk of data contamination. Experiments on GSM8K and MATH-500 demonstrate the effectiveness of MaSTer on mathematical tasks, and the framework's extensibility to non-mathematical tasks highlights its broad applicability.

Additionally, the synthesized variants generated by MaSTer can be utilized as a fine-tuning dataset to significantly enhance the model's robustness.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "bf71b5f1-17c1-430c-bcee-002e48e4806b",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "86e7bd28-006a-4046-a5d4-5678031605bf",
  "toolUseResult": {
    "query": "MaSTer automated robustness evaluation mathematical reasoning adversarial rewrite 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Dr32LksosZF6iFizWrgWFs",
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
            "title": "Model-Agnostic Meta-Attack: Towards Reliable Evaluation of Adversarial   Robustness",
            "url": "https://arxiv.org/pdf/2110.08256"
          },
          {
            "title": "Is Your Model Really A Good Math Reasoner? Evaluating Mathematical   Reasoning with Checklist",
            "url": "https://arxiv.org/pdf/2407.08733"
          },
          {
            "title": "MSCR: Exploring the Vulnerability of LLMs’ Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement",
            "url": "https://arxiv.org/html/2511.08055"
          },
          {
            "title": "From Accuracy to Robustness: A Study of Rule- and Model-based Verifiers in Mathematical Reasoning",
            "url": "https://arxiv.org/html/2505.22203v2"
          }
        ]
      },
      "Based on the search results, I found relevant information about MaSTer:\n\nMaSTer (Math Stress Tester) is a framework designed to automatically expose the latent vulnerabilities of target large language models, inspired by stress testing in software engineering. \n\nMaSTer generates adversarial variants via a multi-round rewrite-verify loop, ensuring semantic consistency while successfully inducing model failure. More specifically, the rewriter rewrites mathematical problems into their variants while keeping the core meaning unchanged, and the verifier checks whether the core meaning of the original question is preserved and whether the target LLM's answer to the rewritten variant is different from the correct answer.\n\nThe framework generates benchmark variants dynamically for each LLM, thus minimizing the risk of data contamination. Experiments on GSM8K and MATH-500 demonstrate the effectiveness of MaSTer on mathematical tasks, and the framework's extensibility to non-mathematical tasks highlights its broad applicability.\n\nAdditionally, the synthesized variants generated by MaSTer can be utilized as a fine-tuning dataset to significantly enhance the model's robustness."
    ],
    "durationSeconds": 8.594332649000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "bf71b5f1-17c1-430c-bcee-002e48e4806b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-28T14:05:23.104Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01UCFP7bNNEqRX6icfSzwtQk`</summary>

```json
{
  "query": "ConStat performance-based contamination detection LLM NeurIPS 2024 rephrased samples"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "86e7bd28-006a-4046-a5d4-5678031605bf",
  "isSidechain": false,
  "requestId": "req_011CbV6RYzSyqtLsFZ8ZHP2T",
  "type": "assistant",
  "uuid": "3edb8972-e720-40fd-a5b1-936a109e74b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NhK7x7Y5NAcyzQe3SMTeMp",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 732,
      "cache_read_input_tokens": 35527,
      "output_tokens": 75,
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
          "output_tokens": 75,
          "cache_read_input_tokens": 35527,
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

_source line 39 · 2026-05-28T14:05:30.144Z_

<details><summary>↩ Tool result · `toolu_01UCFP7bNNEqRX6icfSzwtQk`</summary>

```text
Web search results for query: "ConStat performance-based contamination detection LLM NeurIPS 2024 rephrased samples"

Links: [{"title":"ConStat: Performance-Based Contamination Detection in LLMs - YouTube","url":"https://www.youtube.com/watch?v=dgvU0jDFa0c"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models | OpenReview","url":"https://openreview.net/forum?id=ALISPmDPCq"},{"title":"[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://openreview.net/pdf?id=ALISPmDPCq"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/dekoninck2024constat"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/html/2405.16281v1"},{"title":"ConStat: Performance-Based Contamination Detection in Large Language   Models","url":"https://arxiv.org/pdf/2405.16281"},{"title":"NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://neurips.cc/virtual/2024/poster/96266"},{"title":"[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models","url":"https://arxiv.org/abs/2405.16281"}]

Based on the search results, I found comprehensive information about ConStat and its connection to rephrased samples:

## ConStat: Performance-Based Contamination Detection

ConStat is a statistical method that aims to detect contamination in language models as artificially inflated and non-generalizing benchmark performance. The method addresses the problem where data contamination can lead to inflated performance in public benchmarks, rendering them unreliable for model comparison, making it crucial to detect contamination and estimate its impact on measured performance.

### Key Innovation: Definition Based on Performance Impact

The approach proposes a new perspective on contamination, defining it based on its effect on model performance rather than its cause—specifically, defining contamination as artificially inflated, non-generalizing performance, where a model is contaminated if its performance relative to other models is significantly higher on the original benchmark than on a similar reference benchmark.

### Handling Rephrased Samples

This perspective enables detection of any model with inflated performance, i.e., performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.

Additionally, an alternative approach measures model performance on rephrased benchmarks instead of the original benchmarks to obtain more accurate estimates of model performance, though results vary significantly across benchmarks and lack a statistical framework for contamination detection.

### Results

ConStat found high levels of contamination in multiple popular models including Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3edb8972-e720-40fd-a5b1-936a109e74b9",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "295c23c7-8f76-4853-894f-b79166a205d6",
  "toolUseResult": {
    "query": "ConStat performance-based contamination detection LLM NeurIPS 2024 rephrased samples",
    "results": [
      {
        "tool_use_id": "srvtoolu_014x6PDktB94HvxWFQt2QvZA",
        "content": [
          {
            "title": "ConStat: Performance-Based Contamination Detection in LLMs - YouTube",
            "url": "https://www.youtube.com/watch?v=dgvU0jDFa0c"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models | OpenReview",
            "url": "https://openreview.net/forum?id=ALISPmDPCq"
          },
          {
            "title": "[Quick Review] ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://liner.com/review/constat-performancebased-contamination-detection-in-large-language-models"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://proceedings.neurips.cc/paper_files/paper/2024/file/a7f89793b9e6f8c6568dbbb6ff727b9b-Paper-Conference.pdf"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://openreview.net/pdf?id=ALISPmDPCq"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models | SRI Lab",
            "url": "https://www.sri.inf.ethz.ch/publications/dekoninck2024constat"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/html/2405.16281v1"
          },
          {
            "title": "ConStat: Performance-Based Contamination Detection in Large Language   Models",
            "url": "https://arxiv.org/pdf/2405.16281"
          },
          {
            "title": "NeurIPS Poster ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://neurips.cc/virtual/2024/poster/96266"
          },
          {
            "title": "[2405.16281] ConStat: Performance-Based Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/abs/2405.16281"
          }
        ]
      },
      "Based on the search results, I found comprehensive information about ConStat and its connection to rephrased samples:\n\n## ConStat: Performance-Based Contamination Detection\n\nConStat is a statistical method that aims to detect contamination in language models as artificially inflated and non-generalizing benchmark performance. The method addresses the problem where data contamination can lead to inflated performance in public benchmarks, rendering them unreliable for model comparison, making it crucial to detect contamination and estimate its impact on measured performance.\n\n### Key Innovation: Definition Based on Performance Impact\n\nThe approach proposes a new perspective on contamination, defining it based on its effect on model performance rather than its cause—specifically, defining contamination as artificially inflated, non-generalizing performance, where a model is contaminated if its performance relative to other models is significantly higher on the original benchmark than on a similar reference benchmark.\n\n### Handling Rephrased Samples\n\nThis perspective enables detection of any model with inflated performance, i.e., performance that does not generalize to rephrased samples, synthetic samples from the same distribution, or different benchmarks for the same task.\n\nAdditionally, an alternative approach measures model performance on rephrased benchmarks instead of the original benchmarks to obtain more accurate estimates of model performance, though results vary significantly across benchmarks and lack a statistical framework for contamination detection.\n\n### Results\n\nConStat found high levels of contamination in multiple popular models including Mistral, Llama, Yi, and the top-3 Open LLM Leaderboard models."
    ],
    "durationSeconds": 7.033678597999999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3edb8972-e720-40fd-a5b1-936a109e74b9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-28T14:05:33.172Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01As8djnXnrKsEVxMLUhZL4f`</summary>

```json
{
  "query": "MathArena LLM evaluation uncontaminated math competitions NeurIPS 2025 AIME 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "295c23c7-8f76-4853-894f-b79166a205d6",
  "isSidechain": false,
  "requestId": "req_011CbV6SJBjpLbqkvWnZFRq4",
  "type": "assistant",
  "uuid": "587614b0-bc65-4aae-88d5-46342ce34d43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CvGauVF4c5XD17HfXiJQu",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 951,
      "cache_read_input_tokens": 36259,
      "output_tokens": 79,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 951,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 79,
          "cache_read_input_tokens": 36259,
          "cache_creation_input_tokens": 951,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 951
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

_source line 41 · 2026-05-28T14:05:41.828Z_

<details><summary>↩ Tool result · `toolu_01As8djnXnrKsEVxMLUhZL4f`</summary>

```text
Web search results for query: "MathArena LLM evaluation uncontaminated math competitions NeurIPS 2025 AIME 2026"

Links: [{"title":"MathArena: Evaluating LLMs on Uncontaminated Math Competitions | OpenReview","url":"https://openreview.net/forum?id=y0zL9IZxZ7"},{"title":"MathArena.ai","url":"https://matharena.ai/"},{"title":"[2505.23281] MathArena: Evaluating LLMs on Uncontaminated Math Competitions","url":"https://arxiv.org/abs/2505.23281"},{"title":"MathArena - AIME 2026","url":"https://matharena.ai/?comp=aime--aime_2026"},{"title":"MathArena: Evaluating LLMs on Uncontaminated Math Competitions","url":"https://arxiv.org/html/2505.23281v2"},{"title":"NeurIPS Poster MathArena: Evaluating LLMs on Uncontaminated Math Competitions","url":"https://neurips.cc/virtual/2025/poster/121385"},{"title":"MathArena: Evaluating LLMs on Uncontaminated Math Competitions | SRI Lab","url":"https://www.sri.inf.ethz.ch/publications/balunovic2025matharena"},{"title":"MathArena: Evaluating LLMs on Uncontaminated Math Competitions","url":"https://openreview.net/pdf?id=y0zL9IZxZ7"},{"title":"GitHub - eth-sri/matharena: Evaluation of LLMs on latest math competitions · GitHub","url":"https://github.com/eth-sri/matharena"}]

Based on the search results, here's what I found about MathArena:

## Overview

MathArena is a new benchmark for evaluating LLMs on recurring math competitions which provide a stream of high-quality uncontaminated problems, presented at NeurIPS 2025 Datasets and Benchmarks Track.

## Key Features and Goals

MathArena is a platform for evaluation of LLMs on the latest math competitions and olympiads, with the mission of rigorous evaluation of the reasoning and generalization capabilities of LLMs on new math problems which the models have not seen during training.

The benchmark is based on the key insight that recurring math competitions provide high-quality, challenging problems that can be used for real-time evaluation of LLMs, and by evaluating models as soon as new problems are released, the framework effectively eliminates the risk of contamination.

## Scope

Over 50 models have been evaluated across seven competitions, totaling 162 problems. The platform publishes a leaderboard for each competition showing the scores of different models on individual problems.

## Notable Findings and Capabilities

Using this framework, strong signs of contamination were found in AIME 2024. MathArena is also the first benchmark for proof-writing capabilities, and on IMO 2025, top models achieve slightly less than 40%.

As an evolving benchmark, MathArena will continue to track the progress of LLMs on newly released competitions, ensuring rigorous and up-to-date evaluation of mathematical reasoning.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "587614b0-bc65-4aae-88d5-46342ce34d43",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "79a28daf-ab89-4caa-b3fa-49fdf66edd08",
  "toolUseResult": {
    "query": "MathArena LLM evaluation uncontaminated math competitions NeurIPS 2025 AIME 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01RKCmeKTsHkFMvonMBpWG2c",
        "content": [
          {
            "title": "MathArena: Evaluating LLMs on Uncontaminated Math Competitions | OpenReview",
            "url": "https://openreview.net/forum?id=y0zL9IZxZ7"
          },
          {
            "title": "MathArena.ai",
            "url": "https://matharena.ai/"
          },
          {
            "title": "[2505.23281] MathArena: Evaluating LLMs on Uncontaminated Math Competitions",
            "url": "https://arxiv.org/abs/2505.23281"
          },
          {
            "title": "MathArena - AIME 2026",
            "url": "https://matharena.ai/?comp=aime--aime_2026"
          },
          {
            "title": "MathArena: Evaluating LLMs on Uncontaminated Math Competitions",
            "url": "https://arxiv.org/html/2505.23281v2"
          },
          {
            "title": "NeurIPS Poster MathArena: Evaluating LLMs on Uncontaminated Math Competitions",
            "url": "https://neurips.cc/virtual/2025/poster/121385"
          },
          {
            "title": "MathArena: Evaluating LLMs on Uncontaminated Math Competitions | SRI Lab",
            "url": "https://www.sri.inf.ethz.ch/publications/balunovic2025matharena"
          },
          {
            "title": "MathArena: Evaluating LLMs on Uncontaminated Math Competitions",
            "url": "https://openreview.net/pdf?id=y0zL9IZxZ7"
          },
          {
            "title": "GitHub - eth-sri/matharena: Evaluation of LLMs on latest math competitions · GitHub",
            "url": "https://github.com/eth-sri/matharena"
          }
        ]
      },
      "Based on the search results, here's what I found about MathArena:\n\n## Overview\n\nMathArena is a new benchmark for evaluating LLMs on recurring math competitions which provide a stream of high-quality uncontaminated problems, presented at NeurIPS 2025 Datasets and Benchmarks Track.\n\n## Key Features and Goals\n\nMathArena is a platform for evaluation of LLMs on the latest math competitions and olympiads, with the mission of rigorous evaluation of the reasoning and generalization capabilities of LLMs on new math problems which the models have not seen during training.\n\nThe benchmark is based on the key insight that recurring math competitions provide high-quality, challenging problems that can be used for real-time evaluation of LLMs, and by evaluating models as soon as new problems are released, the framework effectively eliminates the risk of contamination.\n\n## Scope\n\nOver 50 models have been evaluated across seven competitions, totaling 162 problems. The platform publishes a leaderboard for each competition showing the scores of different models on individual problems.\n\n## Notable Findings and Capabilities\n\nUsing this framework, strong signs of contamination were found in AIME 2024. MathArena is also the first benchmark for proof-writing capabilities, and on IMO 2025, top models achieve slightly less than 40%.\n\nAs an evolving benchmark, MathArena will continue to track the progress of LLMs on newly released competitions, ensuring rigorous and up-to-date evaluation of mathematical reasoning."
    ],
    "durationSeconds": 8.649027746000007,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "587614b0-bc65-4aae-88d5-46342ce34d43",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 42_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "79a28daf-ab89-4caa-b3fa-49fdf66edd08",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Runtime record

_source line 43_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-ability decomposition via gated IRT",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Tool call

_source line 44 · 2026-05-28T14:05:45.342Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WDH4ZpChaQNj69mpZMWRHS`</summary>

```json
{
  "query": "RIDE difficulty evolving perturbation item response theory mathematical reasoning IRT reward RL"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "79a28daf-ab89-4caa-b3fa-49fdf66edd08",
  "isSidechain": false,
  "requestId": "req_011CbV6TA6LwN5LdCwiYcXoc",
  "type": "assistant",
  "uuid": "9507d3a8-9d24-4c25-9a98-6c263ba3c737",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01P9tHbz8S5ZYwBCEySDzEn4",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 884,
      "cache_read_input_tokens": 37210,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 884,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 37210,
          "cache_creation_input_tokens": 884,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 884
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

_source line 45 · 2026-05-28T14:05:51.136Z_

<details><summary>↩ Tool result · `toolu_01WDH4ZpChaQNj69mpZMWRHS`</summary>

```text
Web search results for query: "RIDE difficulty evolving perturbation item response theory mathematical reasoning IRT reward RL"

Links: [{"title":"[2511.04120] RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/abs/2511.04120"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/html/2511.04120"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response ...","url":"https://arxiv.org/pdf/2511.04120"},{"title":"RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ...","url":"https://openreview.net/pdf/a83cd39cfda0263faa17943c8f4832d28003298c.pdf"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning | OpenReview","url":"https://openreview.net/forum?id=PPkzchpdNK"},{"title":"DeepMath-103K: A Large-Scale, Challenging, Decontaminated, and Verifiable Mathematical Dataset for Advancing Reasoning | Request PDF","url":"https://www.researchgate.net/publication/392086521_DeepMath-103K_A_Large-Scale_Challenging_Decontaminated_and_Verifiable_Mathematical_Dataset_for_Advancing_Reasoning"}]

Based on the search results, here's what I found about RIDE:

RIDE is a novel adversarial question-rewriting framework that leverages Item Response Theory (IRT) to rigorously measure question difficulty and to generate intrinsically more challenging, well-posed variations of mathematical problems.

**Key Components:**

1. **Problem It Addresses**: Large language models achieve high performance on mathematical reasoning, but current rule-based perturbation methods often generate ill-posed questions and impede the systematic evaluation of question difficulty and the evolution of benchmarks.

2. **Methodology**: The framework employs 35 LLMs to simulate students and builds a difficulty ranker from their responses, which provides a reward signal during reinforcement learning and guides a question-rewriting model to reformulate existing questions.

3. **Reinforcement Learning Component**: Applying reinforcement learning to difficulty-evolving question rewriting encourages the model to adaptively generate questions with higher difficulty, thus avoiding superficial modifications, while further enhancing consistency between the rewritten questions and their answers by setting a correctness reward.

4. **Additional Applications**: The method also serves as an effective data augmentation strategy for mathematical reasoning, with applications to datasets like DeepMath.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "9507d3a8-9d24-4c25-9a98-6c263ba3c737",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "3aae72a0-36dc-4e7a-a9ea-b4974418aa86",
  "toolUseResult": {
    "query": "RIDE difficulty evolving perturbation item response theory mathematical reasoning IRT reward RL",
    "results": [
      {
        "tool_use_id": "srvtoolu_012fesibcNTU2FcQWXD59Ja2",
        "content": [
          {
            "title": "[2511.04120] RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2511.04120"
          },
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning",
            "url": "https://arxiv.org/html/2511.04120"
          },
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response ...",
            "url": "https://arxiv.org/pdf/2511.04120"
          },
          {
            "title": "RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ...",
            "url": "https://openreview.net/pdf/a83cd39cfda0263faa17943c8f4832d28003298c.pdf"
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
      "Based on the search results, here's what I found about RIDE:\n\nRIDE is a novel adversarial question-rewriting framework that leverages Item Response Theory (IRT) to rigorously measure question difficulty and to generate intrinsically more challenging, well-posed variations of mathematical problems.\n\n**Key Components:**\n\n1. **Problem It Addresses**: Large language models achieve high performance on mathematical reasoning, but current rule-based perturbation methods often generate ill-posed questions and impede the systematic evaluation of question difficulty and the evolution of benchmarks.\n\n2. **Methodology**: The framework employs 35 LLMs to simulate students and builds a difficulty ranker from their responses, which provides a reward signal during reinforcement learning and guides a question-rewriting model to reformulate existing questions.\n\n3. **Reinforcement Learning Component**: Applying reinforcement learning to difficulty-evolving question rewriting encourages the model to adaptively generate questions with higher difficulty, thus avoiding superficial modifications, while further enhancing consistency between the rewritten questions and their answers by setting a correctness reward.\n\n4. **Additional Applications**: The method also serves as an effective data augmentation strategy for mathematical reasoning, with applications to datasets like DeepMath."
    ],
    "durationSeconds": 5.788465928999998,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "9507d3a8-9d24-4c25-9a98-6c263ba3c737",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 46 · 2026-05-28T14:05:54.038Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01MTPN2MdfiW7QFxBdGou9ow`</summary>

```json
{
  "query": "\"contamination\" \"ability\" \"decomposition\" OR \"disentangle\" LLM benchmark IRT psychometric 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3aae72a0-36dc-4e7a-a9ea-b4974418aa86",
  "isSidechain": false,
  "requestId": "req_011CbV6TqzhP2bxHDiQXCK9Y",
  "type": "assistant",
  "uuid": "cb6d1245-b8e2-4802-8673-3b40e1da77c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016CyBY8W8uoTSajZ9f3SKGr",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 729,
      "cache_read_input_tokens": 38094,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 729,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 38094,
          "cache_creation_input_tokens": 729,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 729
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

_source line 47 · 2026-05-28T14:06:03.241Z_

<details><summary>↩ Tool result · `toolu_01MTPN2MdfiW7QFxBdGou9ow`</summary>

```text
Web search results for query: ""contamination" "ability" "decomposition" OR "disentangle" LLM benchmark IRT psychometric 2025 2026"

Links: [{"title":"Large Language Models Could Be Rote Learners","url":"https://arxiv.org/pdf/2504.08300"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"},{"title":"Data Contamination or Genuine Generalization ... - SUAS","url":"https://www.suaspress.org/ojs/index.php/AJNS/article/download/v2n2a03/v2n2a03"},{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"Towards Contamination Resistant Benchmarks","url":"https://arxiv.org/pdf/2505.08389"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v3"},{"title":"LogProber: Disentangling confidence from contamination in LLM responses","url":"https://arxiv.org/pdf/2408.14352"}]

I found several relevant research papers and resources on your query. Here are the key results:

## Main Findings

**Contamination & Ability Decomposition:**
A three-tier framework has been proposed to disentangle contamination effects using n-gram alignment, canary insertion, and perturbation testing across open and closed models.

**IRT & Psychometric Approaches:**
A Pseudo-Siamese Network for Item Response Theory (PSN-IRT) framework has been developed that incorporates rich item parameters within an IRT-grounded architecture for accurate estimations of item characteristics and model abilities, with analysis conducted on 11 LLM benchmarks comprising 41,871 items.

Meta probing agents (MPA), a dynamic evaluation protocol inspired by psychometrics, has been proposed to evaluate LLMs by transforming evaluation problems following psychometric theory on three basic cognitive abilities: language understanding, problem solving, and domain knowledge.

**Disentangling Effects:**
NPHardEval4V is a dynamic benchmark designed to address gaps in evaluating reasoning abilities by disentangling the effects of factors such as image recognition and instruction following from overall model performance.

**Recent Work on Contamination:**
A 2026 paper titled "Quantifying the Effect of Test Set Contamination on Generative Evaluations" trained dozens of models while varying test set replicas in pretraining, fitting a dose-response curve where capacity and incentive are the key parameters, with larger models showing steeper dose-response curves.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "cb6d1245-b8e2-4802-8673-3b40e1da77c7",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "d0201b85-910e-40d1-8082-3d0371e8e207",
  "toolUseResult": {
    "query": "\"contamination\" \"ability\" \"decomposition\" OR \"disentangle\" LLM benchmark IRT psychometric 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_019QH6Q7We9iNV7jKGQWfMGb",
        "content": [
          {
            "title": "Large Language Models Could Be Rote Learners",
            "url": "https://arxiv.org/pdf/2504.08300"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          },
          {
            "title": "Data Contamination or Genuine Generalization ... - SUAS",
            "url": "https://www.suaspress.org/ojs/index.php/AJNS/article/download/v2n2a03/v2n2a03"
          },
          {
            "title": "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide",
            "url": "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
          },
          {
            "title": "Towards Contamination Resistant Benchmarks",
            "url": "https://arxiv.org/pdf/2505.08389"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v3"
          },
          {
            "title": "LogProber: Disentangling confidence from contamination in LLM responses",
            "url": "https://arxiv.org/pdf/2408.14352"
          }
        ]
      },
      "I found several relevant research papers and resources on your query. Here are the key results:\n\n## Main Findings\n\n**Contamination & Ability Decomposition:**\nA three-tier framework has been proposed to disentangle contamination effects using n-gram alignment, canary insertion, and perturbation testing across open and closed models.\n\n**IRT & Psychometric Approaches:**\nA Pseudo-Siamese Network for Item Response Theory (PSN-IRT) framework has been developed that incorporates rich item parameters within an IRT-grounded architecture for accurate estimations of item characteristics and model abilities, with analysis conducted on 11 LLM benchmarks comprising 41,871 items.\n\nMeta probing agents (MPA), a dynamic evaluation protocol inspired by psychometrics, has been proposed to evaluate LLMs by transforming evaluation problems following psychometric theory on three basic cognitive abilities: language understanding, problem solving, and domain knowledge.\n\n**Disentangling Effects:**\nNPHardEval4V is a dynamic benchmark designed to address gaps in evaluating reasoning abilities by disentangling the effects of factors such as image recognition and instruction following from overall model performance.\n\n**Recent Work on Contamination:**\nA 2026 paper titled \"Quantifying the Effect of Test Set Contamination on Generative Evaluations\" trained dozens of models while varying test set replicas in pretraining, fitting a dose-response curve where capacity and incentive are the key parameters, with larger models showing steeper dose-response curves."
    ],
    "durationSeconds": 9.198732175000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "cb6d1245-b8e2-4802-8673-3b40e1da77c7",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 48 · 2026-05-28T14:06:06.471Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01RFXKdx7T68rgeKj3egLvzx`</summary>

```json
{
  "query": "PaCoST paired confidence significance testing benchmark contamination detection LLM 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d0201b85-910e-40d1-8082-3d0371e8e207",
  "isSidechain": false,
  "requestId": "req_011CbV6UjgDhyaCHRfgvQkf9",
  "type": "assistant",
  "uuid": "6a3fa22e-fba2-43ba-82bf-a7b8fbcbf2a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Q5owncVrDJ8DUF29D9gE3r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 804,
      "cache_read_input_tokens": 38823,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 804,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 38823,
          "cache_creation_input_tokens": 804,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 804
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

_source line 49 · 2026-05-28T14:06:14.621Z_

<details><summary>↩ Tool result · `toolu_01RFXKdx7T68rgeKj3egLvzx`</summary>

```text
Web search results for query: "PaCoST paired confidence significance testing benchmark contamination detection LLM 2024"

Links: [{"title":"PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models","url":"https://arxiv.org/html/2406.18326"},{"title":"NLP Eval: Measuring LLM Data Contamination","url":"https://www.emergentmind.com/papers/2310.18018"},{"title":"[2406.18326] PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models","url":"https://arxiv.org/abs/2406.18326"},{"title":"(PDF) PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models","url":"https://www.researchgate.net/publication/381737330_PaCoST_Paired_Confidence_Significance_Testing_for_Benchmark_Contamination_Detection_in_Large_Language_Models"},{"title":"PaCoST: Paired Confidence Significance Testing for Benchmark   Contamination Detection in Large Language Models","url":"https://arxiv.org/pdf/2406.18326"},{"title":"Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models | Request PDF","url":"https://www.researchgate.net/publication/394284366_Data_Contamination_Quiz_A_Tool_to_Detect_and_Estimate_Contamination_in_Large_Language_Models"},{"title":"A Survey on Data Contamination for Large Language Models","url":"https://arxiv.org/pdf/2502.14425"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"}]

Here are the search results for PaCoST:

PaCoST (Paired Confidence Significance Testing) is a novel approach designed for the detection of benchmark contamination in open-source LLMs. The method entails a three-step statistical analysis, capable of identifying benchmarks within the model's training data.

Large language models are known to be trained on vast amounts of data, which may unintentionally or intentionally include data from commonly used benchmarks, leading to cheatingly high scores on model leaderboards, yet resulting in disappointing performance in real-world applications.

**How PaCoST Works:**
The method constructs a counterpart for each piece of data with the same distribution, and performs statistical analysis of the corresponding confidence to test whether the model is significantly more confident under the original benchmark. The approach operates under the assumption that the model tends to demonstrate greater confidence when responding to questions it has been trained on.

**Key Findings:**
When applied to popular open-source models and benchmarks, the study found that almost all models and benchmarks tested were suspected to be contaminated more or less.

PaCoST was published in the Findings of the Association for Computational Linguistics: EMNLP 2024.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "6a3fa22e-fba2-43ba-82bf-a7b8fbcbf2a1",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "a85ef21d-0dfe-4281-b056-70975d09269e",
  "toolUseResult": {
    "query": "PaCoST paired confidence significance testing benchmark contamination detection LLM 2024",
    "results": [
      {
        "tool_use_id": "srvtoolu_01EsxYfy8hzkbKoDpPzJUCL9",
        "content": [
          {
            "title": "PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/html/2406.18326"
          },
          {
            "title": "NLP Eval: Measuring LLM Data Contamination",
            "url": "https://www.emergentmind.com/papers/2310.18018"
          },
          {
            "title": "[2406.18326] PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/abs/2406.18326"
          },
          {
            "title": "(PDF) PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in Large Language Models",
            "url": "https://www.researchgate.net/publication/381737330_PaCoST_Paired_Confidence_Significance_Testing_for_Benchmark_Contamination_Detection_in_Large_Language_Models"
          },
          {
            "title": "PaCoST: Paired Confidence Significance Testing for Benchmark   Contamination Detection in Large Language Models",
            "url": "https://arxiv.org/pdf/2406.18326"
          },
          {
            "title": "Data Contamination Quiz: A Tool to Detect and Estimate Contamination in Large Language Models | Request PDF",
            "url": "https://www.researchgate.net/publication/394284366_Data_Contamination_Quiz_A_Tool_to_Detect_and_Estimate_Contamination_in_Large_Language_Models"
          },
          {
            "title": "A Survey on Data Contamination for Large Language Models",
            "url": "https://arxiv.org/pdf/2502.14425"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          }
        ]
      },
      "Here are the search results for PaCoST:\n\nPaCoST (Paired Confidence Significance Testing) is a novel approach designed for the detection of benchmark contamination in open-source LLMs. The method entails a three-step statistical analysis, capable of identifying benchmarks within the model's training data.\n\nLarge language models are known to be trained on vast amounts of data, which may unintentionally or intentionally include data from commonly used benchmarks, leading to cheatingly high scores on model leaderboards, yet resulting in disappointing performance in real-world applications.\n\n**How PaCoST Works:**\nThe method constructs a counterpart for each piece of data with the same distribution, and performs statistical analysis of the corresponding confidence to test whether the model is significantly more confident under the original benchmark. The approach operates under the assumption that the model tends to demonstrate greater confidence when responding to questions it has been trained on.\n\n**Key Findings:**\nWhen applied to popular open-source models and benchmarks, the study found that almost all models and benchmarks tested were suspected to be contaminated more or less.\n\nPaCoST was published in the Findings of the Association for Computational Linguistics: EMNLP 2024."
    ],
    "durationSeconds": 8.139690606999997,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "6a3fa22e-fba2-43ba-82bf-a7b8fbcbf2a1",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 50 · 2026-05-28T14:06:17.867Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the field. Let me do one more targeted search to check if there's any existing work that directly combines IRT with contamination correction (not just detection) in a joint model.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "a85ef21d-0dfe-4281-b056-70975d09269e",
  "isSidechain": false,
  "requestId": "req_011CbV6VaLvJVPUk1FoYTC89",
  "type": "assistant",
  "uuid": "2a23e6cb-7c8d-4749-9f4c-a11941bba1c9",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012D1mphGq5WJr8NamYqoK9V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 39627,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 39627,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 841
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

_source line 51 · 2026-05-28T14:06:18.834Z_

Now let me do one final search to check for any direct competitors attempting joint IRT-contamination modeling:

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2a23e6cb-7c8d-4749-9f4c-a11941bba1c9",
  "isSidechain": false,
  "requestId": "req_011CbV6VaLvJVPUk1FoYTC89",
  "type": "assistant",
  "uuid": "8ae94432-8a09-4a9e-bded-0e361b46cff3",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012D1mphGq5WJr8NamYqoK9V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 39627,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 39627,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 841
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

_source line 52 · 2026-05-28T14:06:19.460Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01B5oRbGgG6J2Mk1eJwVbFYL`</summary>

```json
{
  "query": "\"gated IRT\" OR \"contamination-corrected ability\" OR \"decontaminated IRT\" LLM evaluation score correction 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8ae94432-8a09-4a9e-bded-0e361b46cff3",
  "isSidechain": false,
  "requestId": "req_011CbV6VaLvJVPUk1FoYTC89",
  "type": "assistant",
  "uuid": "c4c2caf4-b9d9-4718-8150-ea41b7376f0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_012D1mphGq5WJr8NamYqoK9V",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 841,
      "cache_read_input_tokens": 39627,
      "output_tokens": 169,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 841,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 169,
          "cache_read_input_tokens": 39627,
          "cache_creation_input_tokens": 841,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 841
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

_source line 53 · 2026-05-28T14:06:28.096Z_

<details><summary>↩ Tool result · `toolu_01B5oRbGgG6J2Mk1eJwVbFYL`</summary>

```text
Web search results for query: ""gated IRT" OR "contamination-corrected ability" OR "decontaminated IRT" LLM evaluation score correction 2025 2026"

Links: [{"title":"GIM: Evaluating models via tasks that integrate multiple cognitive domains","url":"https://arxiv.org/html/2605.18663"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v3"},{"title":"A Practical Guide for Evaluating LLMs and LLM-Reliant Systems","url":"https://arxiv.org/html/2506.13023v1"},{"title":"Rethinking Benchmark and Contamination for Language Models with","url":"https://arxiv.org/pdf/2311.04850"}]

Based on the web search results, I found several recent papers (2025-2026) addressing related topics in LLM evaluation and contamination correction:

## Key Findings:

**1. GIM (Grounded Integration Measure)**
GIM is a benchmark with 820 original problems where a balanced public-private split provides built-in contamination diagnostic. It calibrates a 2-parameter logistic (2PL) IRT model over >200k prompt-response pairs across 28 models, producing robust ability estimates that correctly order test-configurations even when raw accuracy is distorted by errors or missing data.

**2. DeconIEP - Inference-Time Decontamination**
DeconIEP is a decontamination framework that operates during evaluation by applying small, bounded perturbations in the input embedding space. Guided by a reference model, it learns an instance-adaptive perturbation generator that steers models away from memorization-driven shortcut pathways, achieving strong decontamination effectiveness while incurring only minimal degradation in benign utility.

**3. Adaptive Testing with IRT**
IRT-based ability estimation can distinguish models that appear identical under raw accuracy by accounting for item difficulty.

**4. PSN-IRT Framework**
PSN-IRT is a benchmark analysis framework with superior estimation accuracy and reliability, and selecting items with PSN-IRT leads to model rankings that better align with human preference.

These approaches address the challenge of data contamination in LLM benchmarks, which compromises their reliability.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c4c2caf4-b9d9-4718-8150-ea41b7376f0e",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "6a06b869-9077-4043-ab07-98d928069427",
  "toolUseResult": {
    "query": "\"gated IRT\" OR \"contamination-corrected ability\" OR \"decontaminated IRT\" LLM evaluation score correction 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Fje71esNVDBU5SKs7huu1i",
        "content": [
          {
            "title": "GIM: Evaluating models via tasks that integrate multiple cognitive domains",
            "url": "https://arxiv.org/html/2605.18663"
          },
          {
            "title": "When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/pdf/2601.19334"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/html/2511.04689"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v3"
          },
          {
            "title": "A Practical Guide for Evaluating LLMs and LLM-Reliant Systems",
            "url": "https://arxiv.org/html/2506.13023v1"
          },
          {
            "title": "Rethinking Benchmark and Contamination for Language Models with",
            "url": "https://arxiv.org/pdf/2311.04850"
          }
        ]
      },
      "Based on the web search results, I found several recent papers (2025-2026) addressing related topics in LLM evaluation and contamination correction:\n\n## Key Findings:\n\n**1. GIM (Grounded Integration Measure)**\nGIM is a benchmark with 820 original problems where a balanced public-private split provides built-in contamination diagnostic. It calibrates a 2-parameter logistic (2PL) IRT model over >200k prompt-response pairs across 28 models, producing robust ability estimates that correctly order test-configurations even when raw accuracy is distorted by errors or missing data.\n\n**2. DeconIEP - Inference-Time Decontamination**\nDeconIEP is a decontamination framework that operates during evaluation by applying small, bounded perturbations in the input embedding space. Guided by a reference model, it learns an instance-adaptive perturbation generator that steers models away from memorization-driven shortcut pathways, achieving strong decontamination effectiveness while incurring only minimal degradation in benign utility.\n\n**3. Adaptive Testing with IRT**\nIRT-based ability estimation can distinguish models that appear identical under raw accuracy by accounting for item difficulty.\n\n**4. PSN-IRT Framework**\nPSN-IRT is a benchmark analysis framework with superior estimation accuracy and reliability, and selecting items with PSN-IRT leads to model rankings that better align with human preference.\n\nThese approaches address the challenge of data contamination in LLM benchmarks, which compromises their reliability."
    ],
    "durationSeconds": 8.628654001999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "c4c2caf4-b9d9-4718-8150-ea41b7376f0e",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 54_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "6a06b869-9077-4043-ab07-98d928069427",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-ability decomposition via gated IRT",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Tool call

_source line 56 · 2026-05-28T14:06:31.782Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LXvhTEdi9AdAgcNzW2CpEP`</summary>

```json
{
  "query": "Konig Khorramdel Falk Schmitt hierarchical 2PL Bayesian small sample IRT 2023"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6a06b869-9077-4043-ab07-98d928069427",
  "isSidechain": false,
  "requestId": "req_011CbV6WZrRbZKn4k9onRBHV",
  "type": "assistant",
  "uuid": "d16c1fd0-6de0-4221-8468-2b7f6ba1092f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XJjwpizEx2p2yMj7kSy6CZ",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 832,
      "cache_read_input_tokens": 40468,
      "output_tokens": 82,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 832,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 82,
          "cache_read_input_tokens": 40468,
          "cache_creation_input_tokens": 832,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 832
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

_source line 57 · 2026-05-28T14:06:38.009Z_

<details><summary>↩ Tool result · `toolu_01LXvhTEdi9AdAgcNzW2CpEP`</summary>

```text
Web search results for query: "Konig Khorramdel Falk Schmitt hierarchical 2PL Bayesian small sample IRT 2023"

Links: [{"title":"An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC7262992/"},{"title":"Benefits of the Curious Behavior of Bayesian Hierarchical Item Response Theory Models—An in-Depth Investigation and Bias Correction - Christoph König, Rainer W. Alexandrowicz, 2024","url":"https://journals.sagepub.com/doi/full/10.1177/01466216241227547"},{"title":"Bayesian hierarchical response time modelling—A tutorial - Koenig - 2023 - British Journal of Mathematical and Statistical Psychology - Wiley Online Library","url":"https://bpspsychub.onlinelibrary.wiley.com/doi/full/10.1111/bmsp.12302"},{"title":"Robustness of the performance of the optimized hierarchical two-parameter logistic IRT model for small-sample item calibration","url":"https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10700496/"},{"title":"Robustness of the performance of the optimized hierarchical two-parameter logistic IRT model for small-sample item calibration - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/36333627/"},{"title":"An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration - Christoph König, Christian Spoden, Andreas Frey, 2020","url":"https://journals.sagepub.com/doi/abs/10.1177/0146621619893786"},{"title":"Robustness of the performance of the optimized hierarchical two-parameter logistic IRT model for small-sample item calibration - PMC","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC10700496/"}]

Based on the search results, I found relevant research related to your query. However, the specific authors and exact paper you mentioned (Konig, Khorramdel, Falk, Schmitt) from 2023 don't appear in these results. 

What I did find are closely related works by Christoph König and colleagues on hierarchical Bayesian 2PL IRT models for small samples:

1. König et al. compared the small-sample performance of an optimized Bayesian hierarchical 2PL (H2PL) model to its standard inverse Wishart specification, its nonhierarchical counterpart, and both unweighted and weighted least squares estimators (2020).

2. To extend the applicability of the 2PL model to small-scale situations, König et al. illustrated a novel, optimized hierarchical two-parameter logistic (OH2PL) IRT model (2020).

3. The model specifications in a 2023 tutorial reflect the latest knowledge with regard to weakly informative hyperprior specifications.

The search results indicate that there are papers on Bayesian hierarchical 2PL IRT models for small-sample contexts from 2020 and 2023, but the specific paper with all four authors you mentioned may require a more targeted search or may be available through academic databases.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "d16c1fd0-6de0-4221-8468-2b7f6ba1092f",
  "isSidechain": false,
  "promptId": "35aeb398-6997-4766-8971-092aa4e3e8fb",
  "type": "user",
  "uuid": "c404710f-c79d-46ff-93b4-04653f5cd6b0",
  "toolUseResult": {
    "query": "Konig Khorramdel Falk Schmitt hierarchical 2PL Bayesian small sample IRT 2023",
    "results": [
      {
        "tool_use_id": "srvtoolu_01FSYBZocyb4KbqTqQRkiZEH",
        "content": [
          {
            "title": "An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7262992/"
          },
          {
            "title": "Benefits of the Curious Behavior of Bayesian Hierarchical Item Response Theory Models—An in-Depth Investigation and Bias Correction - Christoph König, Rainer W. Alexandrowicz, 2024",
            "url": "https://journals.sagepub.com/doi/full/10.1177/01466216241227547"
          },
          {
            "title": "Bayesian hierarchical response time modelling—A tutorial - Koenig - 2023 - British Journal of Mathematical and Statistical Psychology - Wiley Online Library",
            "url": "https://bpspsychub.onlinelibrary.wiley.com/doi/full/10.1111/bmsp.12302"
          },
          {
            "title": "Robustness of the performance of the optimized hierarchical two-parameter logistic IRT model for small-sample item calibration",
            "url": "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10700496/"
          },
          {
            "title": "Robustness of the performance of the optimized hierarchical two-parameter logistic IRT model for small-sample item calibration - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/36333627/"
          },
          {
            "title": "An Optimized Bayesian Hierarchical Two-Parameter Logistic Model for Small-Sample Item Calibration - Christoph König, Christian Spoden, Andreas Frey, 2020",
            "url": "https://journals.sagepub.com/doi/abs/10.1177/0146621619893786"
          },
          {
            "title": "Robustness of the performance of the optimized hierarchical two-parameter logistic IRT model for small-sample item calibration - PMC",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC10700496/"
          }
        ]
      },
      "Based on the search results, I found relevant research related to your query. However, the specific authors and exact paper you mentioned (Konig, Khorramdel, Falk, Schmitt) from 2023 don't appear in these results. \n\nWhat I did find are closely related works by Christoph König and colleagues on hierarchical Bayesian 2PL IRT models for small samples:\n\n1. König et al. compared the small-sample performance of an optimized Bayesian hierarchical 2PL (H2PL) model to its standard inverse Wishart specification, its nonhierarchical counterpart, and both unweighted and weighted least squares estimators (2020).\n\n2. To extend the applicability of the 2PL model to small-scale situations, König et al. illustrated a novel, optimized hierarchical two-parameter logistic (OH2PL) IRT model (2020).\n\n3. The model specifications in a 2023 tutorial reflect the latest knowledge with regard to weakly informative hyperprior specifications.\n\nThe search results indicate that there are papers on Bayesian hierarchical 2PL IRT models for small-sample contexts from 2020 and 2023, but the specific paper with all four authors you mentioned may require a more targeted search or may be available through academic databases."
    ],
    "durationSeconds": 6.219986066000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "d16c1fd0-6de0-4221-8468-2b7f6ba1092f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 58 · 2026-05-28T14:06:38.017Z_

```json
{
  "parentUuid": "c404710f-c79d-46ff-93b4-04653f5cd6b0",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "c7ba7e50-ddcc-4b9a-813d-46b0fc894518",
  "timestamp": "2026-05-28T14:06:38.017Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Assistant

_source line 59 · 2026-05-28T14:08:12.067Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have enough research to make a thorough evaluation. Let me synthesize my findings and write the triage output.

Let me consolidate what I've found:

**PSN-IRT (AAAI 2026 Oral)**: Confirmed. Uses 4PL IRT with pseudo-Siamese neural network estimation for 12 LLMs on 41,871 items across 11 benchmarks. Flags contamination via anomalous guessing-rate parameters but does not provide contamination-corrected ability scores. This is a real paper and the proposal's description is accurate.

**RankLLM (ICLR 2026)**: Confirmed. 

RankLLM applies non-parametric bidirectional score propagation across 30 models and 35,550 questions, achieving 90% human alignment without explicit contamination modeling. The proposal's description checks out.

**DCR (EMNLP 2025)**: Confirmed. Uses a fuzzy inference system to quantify contamination and produce a DCR Factor for accuracy adjustment, with 4% average error. The proposal's description is accurate.

**Wang et al. (ICLR 2026)**: Confirmed. Demonstrates that contamination detection becomes fragile for reasoning models—likelihood-based detection fails after GRPO training. The proposal's claim about AUR appears to be supported.

**DGM (Shu et al., Psychometrika 2013)**: Confirmed. A gated IRT model that detects test cheating by decomposing performance into ability and preknowledge components. The proposal's description is accurate.

**ConStat (NeurIPS 2024)**: Confirmed. Uses performance-based contamination detection by comparing original versus reference benchmark performance. The proposal's description is accurate.

**JECS (arXiv May 2026)**: Confirmed. Very recent work using conformal p-values for joint decontamination across multiple models, binarizing items into keep/discard decisions. The proposal's description is accurate.

**MATH-Perturb (ICML 2025)**: Confirmed. Involves 279 expert-crafted perturbations of MATH Level...

**MaSTer (arXiv 2026)**: Confirmed. Multi-round adversarial rewrite-verify pipeline. The proposal's description is accurate.

**MathArena (NeurIPS 2025 D&B)**: Confirmed. Evaluates LLMs on uncontaminated math competitions. The ~900 problems claim appears slightly inflated—the original NeurIPS paper mentions 162 problems, though the platform is expanding, so the proposal's reference to recent expansions reaching ~900 problems is plausible.

**Growing Pains (arXiv April 2026)**: Confirmed. Two-stage fixed-parameter IRT calibration across 400+ models achieving under 2-3% MAE with 100 anchor...

**PaCoST (EMNLP 2024 Findings)**: Confirmed. Uses paired confidence significance testing for contamination detection. The proposal's description is accurate.

**RIDE (arXiv 2025)**: Confirmed. Leverages IRT as a difficulty reward signal for RL-based question rewriting. The proposal's description is accurate.

**König et al. (Behavior Research Methods 2023)**: Couldn't locate the exact paper with those four authors, but König's related work on hierarchical Bayesian 2PL IRT at small sample sizes is well-documented, so the broader claim about Bayesian IRT viability at small N holds up.

**GIM (2025-2026)**: Found a new competitor that calibrates 2PL IRT across 200K+ prompt-response pairs from 28 models, with built-in contamination detection using a public-private split approach...

The GIM approach is relevant but takes a different path—it relies on public-private data splitting rather than the gated IRT decomposition proposed here.

Looking at the core proposal itself: the idea is to adapt the Deterministic Gated IRT Model from psychometrics to LLM evaluation by using paired adversarial items to infer unknown item exposure status, then applying two-stage fixed-parameter calibration to work with limited model counts. The genuinely novel contributions are the three-way combination of IRT, contamination correction, and adversarial pairing—no existing work covers all three together. The adaptation of DGM to handle unknown item exposure through paired adversarial items addresses a real gap since the original DGM assumes exposure is known. The two-stage calibration architecture is also a key innovation...

Generating continuous contamination-corrected ability estimates rather than binary keep/discard decisions or ad-hoc multiplicative corrections. The core mathematical framework borrows from Shu et al. 2013's gated IRT, the two-stage calibration approach comes from Growing Pains, and the adversarial variant generation builds on existing methods like MaSTer and MATH-Perturb. So the real novelty lies in how these pieces integrate together—the question becomes whether this combination is sufficiently non-trivial and whether it actually delivers on its promise.

Now I'm checking whether simpler alternatives could achieve similar results. ConStat's paired-item approach with direct contamination subtraction is one option, though the proposal argues DCR's ad-hoc correction lacks theoretical grounding and performs worse on harder tasks. JECS's conformal filtering followed by standard IRT is another simpler path, but the proposal contends that binarizing items discards useful information—though it's unclear if the continuous correction justifies the added complexity. For models evaluated on MathArena itself, using those rankings as ground truth would bypass contamination correction entirely, but the proposal's value proposition depends on handling models outside that benchmark.

The real marginal gain comes from leveraging both original and variant items while extracting explicit contamination parameters that offer interpretive insight, compared to just running IRT on adversarial variants alone. The critical vulnerability is whether adversarial variants truly remain contamination-free—models might benefit from broader pattern exposure even if they haven't seen exact benchmark items. The proposal mitigates this through SymPy verification and anchor validation, which seems reasonable. The gating mechanism itself assumes contamination operates through a rank-1 bilinear model where items are either memorized or not.

The two-stage calibration approach carries real risk: item parameters derived from 2000+ diverse models may not transfer cleanly to a specific set of 15-20 frontier models, potentially introducing systematic bias. Even with fixed item parameters, estimating contamination from such a small sample is statistically tight, though the proposal addresses this with simulation studies and Bayesian methods. The problem itself is genuinely significant for LLM evaluation.

The proposal's strength lies in offering both corrected ability rankings and interpretable contamination estimates—a principled measurement-theoretic approach rather than ad-hoc corrections. The related work coverage is comprehensive across IRT-based evaluation, contamination detection, and psychometric foundations, though the GIM benchmark using 2PL IRT with public-private contamination diagnostics deserves mention as a closely related concurrent effort.

The core contribution integrates three established components—DGM, paired adversarial items, and two-stage calibration—in a non-trivial way that addresses real gaps, but the novelty is primarily in the assembly rather than fundamentally new ideas. The "surprising" factor is moderate; if the decomposition works, it might feel like an obvious solution rather than a breakthrough insight, and the IRT community may view this as a natural extension of existing methods. would expect DGM to work for LLMs; the novelty is more in the engineering of making it work (paired items for unknown exposure, two-stage for small N) than in conceptual surprise.
3. The proposal is extremely detailed and well-structured, which is a positive signal for execution quality, but I should not let this inflate my assessment of the idea quality itself.

**Scoring:**

Novelty: 中 (Medium)
- The three-way intersection IS unoccupied, and the specific combination is non-trivial.
- But each component is borrowed: DGM from Shu et al. 2013, two-stage from Growing Pains 2026, adversarial pairing from MaSTer/MATH-Perturb.
- The key innovation (handling unknown item exposure via paired items) is a natural extension, not a conceptual breakthrough.
- No existing work does exactly this, but it's more a matter of assembling existing pieces than introducing a fundamentally new paradigm.

Significance: 中-强 (Medium-Strong)
- The contamination-ability entanglement problem is genuinely important and timely, especially given Wang et al. ICLR 2026's findings creating demand for response-pattern-based alternatives.
- If successful, this moves beyond ad-hoc corrections to a principled framework that provides both corrected rankings and interpretable contamination estimates.
- The main limitation is scope—it's tailored to math benchmarks with numerical answers verifiable through SymPy, making extension to NLU/NLG tasks unclear.

Related Work: 强 (Strong)
- The coverage across three distinct research communities is exceptionally thorough with clear differentiation, though GIM benchmark isn't mentioned.

Probability estimation: The idea occupies a genuine unoccupied intersection—

novelty is integrative rather than conceptual, which limits the ceiling. The problem is important and timely, the measurement-theoretic framing is principled and differentiating, and the proposal is extremely well-developed. I'd estimate 28-38%, median around 33%. The main risk is reviewers seeing this as component assembly rather than novel contribution, though the counter-argument is that the assembly is non-trivial and addresses a real gap. For AAAI, the psychometric-AI intersection is well-received (PSN-IRT got Oral at AAAI 2026), which is a positive signal. The proposal's strongest arguments are that nobody does joint contamination-ability decomposition within a measurement-theoretic framework, and the DGM extension for LLMs is more engineering-focused than conceptually surprising.

The two-stage architecture elegantly handles the small-N problem, and the validation plan with synthetic contamination injection provides strong causal evidence. But the weakest aspects are the integrative nature, limited "surprising" factor if the decomposition works as expected, and math-only scope limiting generalizability claims. I'm settling on 30-38%, median 34%—the idea has real substance and occupies a genuinely unoccupied intersection, but it's not paradigm-shifting. For AAAI specifically, the precedent of PSN-IRT's Oral acceptance suggests the venue is receptive to this kind of IRT-based LLM evaluation work. directly builds on PSN-IRT's open question (contamination-corrected scoring)
- The psychometric community has a home at AAAI
- The integration of psychometric test-security methods with LLM evaluation is exactly the kind of cross-disciplinary contribution AAAI values

This might push the probability slightly higher. But I should be careful not to evaluate venue fit (which I'm told not to do) vs. idea quality. The idea quality is what it is regardless of venue.

Let me finalize:

Novelty: 中 (Medium) — integrative novelty at a genuinely unoccupied intersection, but each component borrowed
Significance: 强 (Strong) — important problem, principled framework, timely given Wang et al. ICLR 2026
Related Work: 强 (Strong) — exceptionally thorough coverage

Probability: 30-40%, median 35%

Now I need to stress-test this against the trivial alternative. The naive approach would be to just evaluate on adversarial variants and skip the original items entirely — that avoids contamination without needing CRADE at all. What's the actual value-add? Using both original and variant items gives more precise ability estimates, and explicitly estimating contamination parameters has real interpretive value for the community. The practical benefit of correcting existing benchmark scores rather than replacing them matters too, since leaderboard data already exists. Whether the precision gain from combining both item types is substantial enough when you have thousands of variants per model is the real question.

The trivial alternative is a genuine threat to the novelty claim. The core value of the gated model is really in the contamination estimates themselves — that's real and useful, but it does limit how surprising the contribution feels. This reinforces my medium novelty assessment, keeping the probability in the 30-38% range with a median around 34%.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c7ba7e50-ddcc-4b9a-813d-46b0fc894518",
  "isSidechain": false,
  "requestId": "req_011CbV6XJJa8kDJHVt3WoDYA",
  "type": "assistant",
  "uuid": "f68952a0-c67d-46b6-bc89-186ad3e273fa",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ljcy33KaKyAbq1U96d13wA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 41300,
      "output_tokens": 7857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1032,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7857,
          "cache_read_input_tokens": 41300,
          "cache_creation_input_tokens": 1032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1032
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

_source line 60 · 2026-05-28T14:09:32.642Z_

Now I have sufficient research to provide a thorough evaluation. Let me compile the triage assessment.

---

```
【阶段】: Triage

【领域调研】:
- PSN-IRT "Lost in Benchmarks?" (AAAI 2026 Oral): 4PL IRT via pseudo-Siamese neural estimation on 12 LLMs × 41,871 items. Flags contamination indirectly via anomalous guessing parameters but explicitly leaves contamination-corrected scoring as an open question. Proposal's description is accurate — this is the direct predecessor and leaves the exact gap CRADE claims to fill.
- RankLLM (ICLR 2026): Non-parametric bidirectional score propagation on 30 models × 35,550 questions, 90% human alignment. No contamination modeling. Proposal's description confirmed.
- DCR (EMNLP 2025): Fuzzy inference across 4 contamination levels, producing DCR Factor for multiplicative accuracy adjustment. ~4% average error on 3 benchmarks. Ad-hoc correction, no measurement-theoretic justification. Proposal's description confirmed.
- Wang et al. "On The Fragility of Benchmark Contamination Detection in Reasoning Models" (ICLR 2026): Demonstrates that even brief GRPO training after SFT can conceal contamination signals, making likelihood-based detectors fail on reasoning models. This is the key catalyst — response-pattern-based alternatives are genuinely needed. Proposal's description confirmed.
- DGM (Shu, Henson, Luecht; Psychometrika 2013): Gated IRT decomposes test performance into ability + preknowledge components. Assumes item exposure status is known a priori. Validated at operational testing sample sizes (hundreds of examinees). Proposal's description confirmed.
- ConStat (NeurIPS 2024): Performance-based contamination detection comparing original vs. rephrased benchmark performance against reference models. Detects contamination but does not model it as a latent variable. Proposal's description confirmed.
- JECS (arXiv May 2026, 2605.21543): Joint envelope conformal selection for multi-model decontamination with formal GCR guarantees. Binarizes items into keep/discard. Very recent — directly concurrent work. Proposal's description confirmed.
- MATH-Perturb (ICML 2025): 279 expert-crafted Level 5 perturbations showing 10-25% drops on frontier models. Open code. Proposal's description confirmed.
- MaSTer (arXiv 2026): Multi-round adversarial rewrite-verify pipeline for math robustness. Proposal's description confirmed, including code availability concerns.
- MathArena (NeurIPS 2025 D&B): Evaluating LLMs on uncontaminated math competitions. The original paper reports 162 problems and 50+ models; the claim of "~900 problems" likely reflects post-publication expansion on matharena.ai (confirmed the site exists with AIME 2026, HMMT Feb 2026, etc.). Broadly accurate.
- Growing Pains (arXiv April 2026): Two-stage MIRT 2PL fixed-parameter calibration on 400+ models, <2-3% MAE with 100 anchor items. Open code at github.com/eliyahabba/growing-pains. Proposal's description confirmed.
- PaCoST (EMNLP 2024 Findings): Paired confidence significance testing for binary contamination detection. Confirms paired-item signal without latent-variable modeling. Proposal's description confirmed.
- RIDE (arXiv 2025): IRT as difficulty reward for RL-based adversarial question rewriting. Does not do joint ability-contamination estimation. Proposal's description confirmed.
- GIM (2025-2026, not cited by proposal): Calibrates 2PL IRT over 200K+ responses across 28 models, with built-in contamination diagnostic via public-private split. Relevant competitor not mentioned in proposal.
- König et al. / Fox (2023/2025): Papers on Bayesian hierarchical IRT at small sample sizes exist and support the claim that Bayesian estimation is viable at N=50. The specific König et al. 2023 paper was not directly confirmed with all four named authors (Khorramdel, Falk, Schmitt), but closely related König et al. work on OH2PL for small samples is confirmed from 2020 and 2023 publications.

- 调研总结: The field is at a natural convergence point where three mature threads (IRT-based LLM evaluation, contamination detection/correction, adversarial robustness testing) are ready for integration. PSN-IRT explicitly flagged contamination-corrected scoring as an open question; Wang et al. ICLR 2026 created urgent demand for response-pattern-based alternatives; Growing Pains provided the two-stage calibration infrastructure. The specific three-way intersection (gated IRT × contamination correction × adversarial pairing) is confirmed unoccupied as of my search. CRADE sits precisely at this convergence point with a clear theoretical precedent (DGM from psychometrics).

【Trivial Alternative 检验】:
The most threatening trivial alternative is: **evaluate models on adversarial variants only, then run standard 2PL IRT to get contamination-free ability estimates — skipping the gated model entirely.** With ~1,000 variant items per model, standard 2PL person parameter estimation would be well-conditioned, and you'd get clean ability rankings without any contamination modeling.

CRADE's incremental value over this trivial baseline comes from three sources:
(1) **Explicit contamination quantification**: The gated model outputs ξ_j (per-model contamination probability) and η_i (per-item susceptibility), which are interpretively valuable — knowing *how contaminated* each model is matters beyond just knowing corrected rankings. This is real value.
(2) **Information efficiency**: Using both original and variant items should yield more precise θ estimates than variants alone. But with K ≈ 1,000 variant items, the marginal precision gain from including contamination-corrected originals may be modest.
(3) **Practical utility**: The framework can retroactively correct existing benchmark results rather than requiring all-new evaluation. This matters for leaderboard re-calibration.

Assessment: The trivial alternative is a genuine threat to the "corrected ranking" claim but not to the "contamination quantification" claim. The core value proposition needs to be framed around the decomposition itself (the ξ and η parameters) rather than just ranking improvement. The proposal does frame it this way, which is appropriate. **Incremental value is real but moderate — the gated model is primarily valuable for its interpretive output (contamination parameters), not just for ranking correction.**

【前提假设检验】:
The core claim's logic chain rests on several untested assumptions:

1. **Adversarial variants are truly contamination-free (critical)**: This is the anchor assumption of the entire framework. If models have been exposed to similar (not identical) problems during training — via data augmentation, synthetic training data, or broad math corpora — variant items may still trigger partial memorization. The proposal acknowledges this and includes validation (SymPy verification, anchor assumption checks, comparison with MATH-Perturb expert variants), but the assumption remains empirically unvalidated until the experiment runs. This is the single biggest risk to the framework's validity.

2. **Contamination follows a gating mechanism (moderate concern)**: The model assumes contamination operates as a binary gate — either a model "has" the answer via memorization (with probability ξ_j·η_i) or it relies on genuine ability. In practice, contamination might be partial (improved pattern recognition from training exposure rather than full memorization), creating a continuum rather than a binary gate. The model would attribute partial benefits to either θ or ξ, potentially biasing both.

3. **Rank-1 bilinear decomposition of ξ_j·η_i (moderate concern)**: The assumption that model-level and item-level contamination are separable (no interaction beyond the product) may not hold if contamination is topic-structured (e.g., a model is heavily contaminated on algebra but clean on geometry). The proposal includes residual analysis and Q3 statistics to check this, which is appropriate.

4. **Two-stage calibration transfers without domain shift (low-moderate concern)**: Item parameters calibrated on ~2,000+ leaderboard models (dominated by smaller, older models) are assumed valid for the 15-20 frontier models in Stage 2. If frontier models interact with items differently (e.g., different discrimination patterns for reasoning models vs. pattern-matching models), the fixed item parameters could introduce systematic bias.

5. **15-20 models suffice for contamination parameter estimation (addressed but not resolved)**: Even with fixed item parameters, estimating ξ_j for 15-20 models with hierarchical priors is pushing limits. The simulation study will address this, but it's a validity concern until results are in.

None of these are "fatal" — the proposal addresses each with validation strategies — but assumptions #1 and #2 are the most vulnerable and could undermine the core decomposition if they fail.

【3 维度打分】:

1. Novelty: 中 (Medium) — The three-way intersection (gated IRT × contamination correction × adversarial pairing) is confirmed unoccupied by my search. The extension of DGM to unknown item exposure via paired adversarial items is a genuine technical contribution. However, each component is borrowed from existing work: DGM from Shu et al. 2013, two-stage calibration from Growing Pains (April 2026), adversarial pairing from MaSTer/MATH-Perturb. The novelty is primarily *integrative* — assembling known pieces into a new configuration. The key question reviewers will ask is "is the integration non-trivial?" The answer is partially yes (handling unknown exposure status, bridging psychometric and NLP traditions) and partially no (the mathematical model is a direct adaptation of a 2013 psychometric model with standard Bayesian estimation). PSN-IRT (AAAI 2026 Oral) explicitly left contamination-corrected scoring as an open question, which gives CRADE a clear lineage claim, but it also means the contribution was anticipated by the community. A reviewer could say "this is the natural next step from PSN-IRT" — which is both a strength (the gap is real) and a weakness (the idea is expected rather than surprising).

2. Significance: 强 (Strong) — The problem is genuinely important and timely. Wang et al. (ICLR 2026) proving that likelihood-based detection fails on reasoning models creates urgent demand for response-pattern-based alternatives — CRADE directly addresses this. Contamination undermines benchmark trust across the entire field; a principled measurement-theoretic framework for decomposition (vs. DCR's ad-hoc multiplicative correction with r=0.66 on hard tasks, vs. JECS's binary keep/discard) would be a meaningful advance. The framework produces both corrected ability rankings AND interpretable contamination estimates per model and per item — this dual output is practically valuable for the community. The limitation is scope: the SymPy-verification pipeline restricts immediate applicability to math benchmarks with numerical answers, and extending to NLU/NLG tasks is non-trivial. This bounds the impact somewhat. If the decomposition works, it would be a solid contribution to LLM evaluation methodology; if it fails, the negative result (gated IRT doesn't work for LLM contamination) would also be informative.

3. Related Work: 强 (Strong) — Exceptionally thorough coverage spanning three distinct research communities (psychometrics, NLP contamination, adversarial robustness). Clear differentiation against each related work with specific, accurate descriptions of what each does and doesn't do. The key references are verified as real and accurately described. Minor gaps: (a) GIM benchmark (2025-2026) with built-in contamination diagnostic via public-private split is not mentioned; (b) the specific König et al. 2023 paper with all 4 named authors could not be fully verified (closely related König work exists but the exact author list differs). These are minor issues that don't materially affect the coverage.

【概率估计】: [28% - 38%] 中位 33%

【估计理由】:
The idea sits in the solid "有实质内核" range. The three-way intersection is genuinely unoccupied, the problem is timely and important (especially post-Wang et al. ICLR 2026), and the measurement-theoretic framework is more principled than existing alternatives. However, the novelty is primarily integrative — each component (gated IRT, two-stage calibration, adversarial pairing) is borrowed, and the combination, while non-trivial, is somewhat expected (PSN-IRT explicitly anticipated this direction). The "surprising" test: if the decomposition works, reviewers are more likely to say "this makes sense, it's a natural extension of DGM to LLMs" than "I wouldn't have expected this to work." The trivial alternative (IRT on variants only) puts real pressure on demonstrating the marginal value of the gated decomposition. **Significance is the strongest dimension** (genuine problem, timely demand, principled framework). **Novelty is the ceiling-limiting dimension** — integrative novelty at AAAI can work (PSN-IRT showed AAAI values psychometric+AI bridges), but reviewers may question whether the conceptual contribution is sufficient beyond "apply DGM with paired items and two-stage calibration." The upper bound (38%) reflects a scenario where reviewers value the cross-disciplinary synthesis and the contamination quantification is seen as a distinct contribution; the lower bound (28%) reflects a scenario where reviewers view this as incremental assembly of known techniques.

【主要风险】:
1. **"Assembly of existing components" critique**: Reviewers may argue the novelty is insufficient — DGM exists, two-stage calibration exists, adversarial pairing exists, and the combination, while useful, doesn't introduce a fundamentally new idea. The rebuttal (handling unknown exposure, bridging communities) may not fully convince reviewers who want a stronger conceptual contribution.
2. **Anchor assumption vulnerability**: If adversarial variants are not truly contamination-free (due to broad training exposure to similar mathematical patterns), the entire decomposition collapses — θ estimates from variants would still be contamination-biased, and the gating mechanism would misattribute ability vs. contamination. This is the framework's Achilles' heel and no amount of SymPy verification fully eliminates it.
```

Sources:
- [PSN-IRT: Lost in Benchmarks? (AAAI 2026)](https://ojs.aaai.org/index.php/AAAI/article/view/40814)
- [PSN-IRT GitHub](https://github.com/Joe-Hall-Lee/PSN-IRT)
- [RankLLM (ICLR 2026)](https://openreview.net/forum?id=jnX5GJIoYt)
- [DCR (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1173/)
- [Wang et al. Fragility of Contamination Detection (ICLR 2026)](https://arxiv.org/abs/2510.02386)
- [DGM (Shu et al., Psychometrika 2013)](https://link.springer.com/article/10.1007/s11336-012-9311-3)
- [ConStat (NeurIPS 2024)](https://openreview.net/forum?id=ALISPmDPCq)
- [JECS (arXiv May 2026)](https://arxiv.org/abs/2605.21543)
- [MATH-Perturb (ICML 2025)](https://openreview.net/forum?id=OZy70UggXr)
- [MaSTer (arXiv 2026)](https://arxiv.org/abs/2506.05038)
- [MathArena (NeurIPS 2025)](https://openreview.net/forum?id=y0zL9IZxZ7)
- [MathArena Website](https://matharena.ai/)
- [Growing Pains (arXiv April 2026)](https://arxiv.org/abs/2604.12843)
- [PaCoST (EMNLP 2024 Findings)](https://arxiv.org/abs/2406.18326)
- [RIDE (arXiv 2025)](https://arxiv.org/abs/2511.04120)
- [König et al. OH2PL for Small Samples](https://pmc.ncbi.nlm.nih.gov/articles/PMC10700496/)
- [GIM Benchmark (2025-2026)](https://arxiv.org/html/2605.18663)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f68952a0-c67d-46b6-bc89-186ad3e273fa",
  "isSidechain": false,
  "requestId": "req_011CbV6XJJa8kDJHVt3WoDYA",
  "type": "assistant",
  "uuid": "c76a576e-79a2-48b4-bc9c-7a4aab054adc",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Ljcy33KaKyAbq1U96d13wA",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1032,
      "cache_read_input_tokens": 41300,
      "output_tokens": 7857,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1032,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 7857,
          "cache_read_input_tokens": 41300,
          "cache_creation_input_tokens": 1032,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1032
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

_source line 61_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "c76a576e-79a2-48b4-bc9c-7a4aab054adc",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Runtime record

_source line 62_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-ability decomposition via gated IRT",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Runtime record

_source line 63_

```json
{
  "type": "last-prompt",
  "lastPrompt": "【任务】: 请评估以下 proposal 的客观中稿概率。 必须先走 rubric、再估概率，按指定格式输出（不要输出 GO/KILL 决策）。  【proposal】: # CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  #…",
  "leafUuid": "c76a576e-79a2-48b4-bc9c-7a4aab054adc",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---

### Runtime record

_source line 64_

```json
{
  "type": "ai-title",
  "aiTitle": "Contamination-ability decomposition via gated IRT",
  "sessionId": "57ca1d5f-fa09-46a1-b8fb-8491e77b0326"
}
```

---
