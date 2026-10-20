# Research conversation: CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items ## Core Pr

**Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 56
- **Recorded user turns:** 1
- **Tool calls:** 16
- **Original source:** `logs/chats/exported-trajectories/account-1/3e15f2de-7019-46a4-8086-85a482d5a8a5.jsonl`
- **Structured JSON:** [`0af554aab8802df69b0e.json`](../../sessions/0a/0af554aab8802df69b0e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-28T14:15:00.241Z_

```json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-28T14:15:00.241Z",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "content": "# CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items\n\n## Core Problem\n\nNo existing framework can determine whether a model fails adversarial benchmark variants because it memorized original answers (contamination) or because it lacks genuine reasoning ability (capability deficit) — all current work observes this entanglement but none models it within a measurement-theoretic framework, preventing trustworthy LLM capability assessment.\n\n## Research Opportunity\n\nThree previously siloed research streams — IRT-based LLM evaluation (PSN-IRT AAAI 2026 Oral, ATLAS, LEGO-IRT), contamination detection/correction (DCR EMNLP 2025, ConStat NeurIPS 2024, JECS arXiv May 2026), and adversarial robustness testing (MaSTer, RIDE, MATH-Perturb ICML 2025) — have each matured independently to the point where their integration is both technically feasible and urgently needed. The critical catalyst is Wang et al.'s ICLR 2026 proof that all likelihood-based contamination detection fails on reasoning models (AUROC ≈ 50%), creating demand for response-pattern-based alternatives that bypass token-probability signals entirely. A key theoretical precedent exists but has never been applied to LLMs: the Deterministic Gated IRT model (DGM; Shu, Henson & Luecht, Psychometrika 2013) decomposes test performance into genuine ability and cheating/preknowledge components conditioned on item exposure status — precisely the structure needed for LLM contamination. PSN-IRT showed IRT works for LLMs (12 models, 41,871 items, 4PL) but left contamination-adjusted scoring as an explicit open question, flagging anomalous guessing-rate parameters as contamination indicators without providing corrected ability estimates. RankLLM (ICLR 2026) demonstrated that non-parametric difficulty-aware ranking achieves 90% human alignment with only a damping hyperparameter — but provides no contamination decomposition, producing rankings without interpretable ability vs. memorization parameters. A crucial practical enabler has emerged: the Open LLM Leaderboard V1 provides per-item binary response data for 2,000+ models across standard benchmarks including GSM8K (1,359 items), accessible via per-model details datasets (Polo et al., ICML 2024). Combined with Growing Pains' (arXiv April 2026) demonstration that two-stage fixed-parameter calibration achieves <2% error with 100 anchor items and ρ ≥ 0.9 ranking stability, this large-N calibration data resolves the fundamental feasibility concern of fitting IRT-based models with only 15-20 LLMs — by fixing well-calibrated item parameters from Stage 1, Stage 2 estimation reduces to person-level and contamination parameters only. The AAAI 2027 deadline (abstracts July 21, papers July 28, 2026) is 8 weeks out. Nobody sits at the three-way intersection of IRT estimation, contamination correction, and adversarial pairing because these communities publish at different venues (ACL/EMNLP for contamination, ICLR/NeurIPS for robustness, AAAI for psychometric evaluation, Psychometrika/JEBS for test security).\n\n## Research Landscape\n\nThe current best contamination-to-correction pipeline is DCR (EMNLP 2025), which produces a DCR Factor via fuzzy inference across four contamination levels, achieving ~4% average error on three benchmarks — but its ad-hoc multiplicative correction Acc_adj = Acc × (1 − DCR Factor) has no measurement-theoretic justification and empirically weakens on hard tasks (r=0.66). PSN-IRT (AAAI 2026 Oral) demonstrates IRT's power for LLM evaluation using a 4PL model across 12 LLMs on 11 benchmarks (41,871 items), flagging contamination indirectly via anomalous guessing-rate parameters, but produces no contamination-adjusted ability scores; critically, PSN-IRT succeeds with 12 models by using neural network estimation (pseudo-Siamese architecture) rather than classical MLE, establishing that neural IRT estimation is viable at small model counts. RankLLM (ICLR 2026) provides a strong non-parametric baseline: bidirectional score propagation between models and questions achieves 90% human alignment on 30 models × 35,550 questions, with remarkable stability under model removal (ρ = 0.94 even with 50% pool removed) and 0.006s convergence — but it produces difficulty-weighted rankings without any contamination modeling. RIDE (arXiv 2025) combines IRT with adversarial perturbation for math evaluation — but uses IRT only as a difficulty reward signal for RL-based question rewriting via RIDE-8B, not for joint ability-contamination estimation. JECS (arXiv May 2026) achieves formal conformal guarantees for multi-model decontamination via joint envelope conformal selection, but wastes information by binarizing items into keep/discard rather than producing continuous corrected scores. ConStat (NeurIPS 2024) detects contamination via performance gaps on rephrased samples using a statistical comparison against reference models, but does not model it as a latent variable within a psychometric framework. In psychometrics, the DGM (Shu et al., Psychometrika 2013) uses a gated IRT formulation estimated via hierarchical MCMC to decompose examinee performance into genuine ability and item-preknowledge components — but assumes item exposure status is known a priori, which is unavailable for LLM training data, and was validated only at operational testing sample sizes (hundreds of examinees). Two paired-item approaches exist but use no IRT: PaCoST (arXiv 2024) performs paired confidence significance testing for binary contamination detection, and ConStat compares primary vs. reference benchmark performance — both confirm the paired-item signal is informative but neither models it as a latent variable. For adversarial variant generation, MaSTer (arXiv 2026) provides a validated multi-round rewrite-verify pipeline (5 parallel streams × 3 iterations) achieving 45-94% target failure rates on GSM8K and MATH-500 using Qwen2.5-32B-Instruct for both rewriting and LLM-based verification (98% precision); code is claimed at github.com/sustech-nlp/MaSTer but was unavailable as of May 2026 — backup pipelines exist via MathCheck (ICLR 2025, open code) and MATH-Perturb (ICML 2025, 279 expert-crafted perturbations with open code). Growing Pains (arXiv April 2026) demonstrates two-stage fixed-parameter calibration for extensible LLM evaluation: calibrating MIRT 2PL item parameters on 295+ reference models, then scoring new models via fixed anchor items, achieving <2% MAE and ρ ≥ 0.9 with 100 anchor items per benchmark — directly applicable to our setting where item parameters are calibrated on large-N leaderboard data and contamination parameters estimated on a smaller model pool. Konig et al. (Behavior Research Methods 2023) demonstrate that hierarchical Bayesian 2PL (OH2PL) with half-Cauchy hyperpriors produces unbiased item parameter estimates down to N=50, while standard MML shows 75-89% inadmissible solutions at that sample size — establishing that Bayesian estimation is the correct choice for small-N IRT. Fox (JEBS 2025) pushes further: IRT-BCSM integrates out person parameters for stable estimation at N=50-100, with RMSE of 0.110 for discrimination at N=50 while standard 2PL/MML collapses (RMSE=1.782). MathArena (NeurIPS 2025 D&B Track) has expanded to ~900 problems across 2025-2026 competitions (AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, Apex) with 50+ models, providing rich uncontaminated ground-truth rankings. Concurrent work search (arXiv, OpenReview, May 2026): no paper attempts joint IRT-based contamination-ability decomposition with paired adversarial items or two-stage fixed-parameter calibration for contamination-aware scoring — the intersection remains unoccupied.\n\n## Proposed Approach\n\nWe extend the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from the test-security domain to LLM contamination assessment, introducing the Gated-2PL (G-2PL) model as the primary framework where correct-response probability decomposes into ability-driven and contamination-driven components via a gating mechanism. The key innovations over DGM are: (1) item exposure status is not assumed known but is identified from paired adversarial items, and (2) a two-stage fixed-parameter calibration architecture leverages large-N leaderboard data to resolve the small-sample estimation challenge.\n\n**Two-stage fixed-parameter calibration architecture (central methodological contribution):**\n\nStage 1 — Item parameter calibration (large-N, standard 2PL):\n- Assemble per-item binary response matrix from Open LLM Leaderboard V1 per-model details datasets for GSM8K (N_cal ≈ 2,000+ models × 1,359 items). Per-item data resides in individual per-model datasets under huggingface.co/open-llm-leaderboard-old (naming pattern: details_{org}__{model}), reconstructible following Polo et al. (ICML 2024, tinyBenchmarks). Each dataset contains per-task configurations (e.g., harness_gsm8k) with item-level correctness indicators.\n- Fit standard 2PL via marginal maximum likelihood (MML): estimate â_i (discrimination) and b̂_i (difficulty) for each GSM8K item. With N_cal ≈ 2,000+, these estimates are highly stable — Growing Pains demonstrates <2% MAE and ρ ≥ 0.9 with as few as 100 reference models on similar data.\n- Validate calibration quality: item-fit statistics (S-X², item-total correlations), dimensionality assessment (eigenvalue ratios from the item correlation matrix), and comparison with Growing Pains' calibrated parameters if available.\n- For MATH-500 (secondary benchmark): Stage 1 calibration assembled from (a) V2 leaderboard MATH Level 5 per-model details for the ~100 Level 5 items in MATH-500 (hundreds of models available via gated datasets at huggingface.co/datasets/open-llm-leaderboard/{org}__{model}-details), (b) publicly available per-item MATH-500 evaluation results from major papers and evaluation frameworks (lm-evaluation-harness), and (c) targeted evaluation of ~50-100 small open-weight models (7B-13B) from V1 leaderboard checkpoints on MATH-500 (~15 H100-hrs). Expected N_cal for MATH-500 ≈ 50-200, adequate for Bayesian 2PL calibration per Konig et al. (2023).\n\nStage 2 — Gated model estimation (small-N, fixed item parameters):\n- Fix a_i = â_i, b_i = b̂_i from Stage 1. This eliminates 2K parameters from estimation, leaving only θ_j (M), ξ_j (M), η_i (K), and δ_i (K) = 2M + 2K free parameters.\n- Estimate via Bayesian MCMC on the 15-20-model paired (original + variant) response matrix.\n- The fixed-parameter approach is critical: with a_i and b_i grounded in large-N calibration, θ_j identification from variant items is well-conditioned (each model responds to K ≈ 1,000 items with known parameters), and contamination parameters (ξ_j, η_i) are identified from original-variant performance gaps with θ_j already anchored.\n\n**Model specifications (two-tier: reduced and full):**\n\nReduced G-2PL (R-G-2PL, person-level contamination only, M additional parameters):\n- For variant item i*: P(Y_{j,i*}=1 | θ_j) = σ(a_i(θ_j − b_i − δ_i))\n- For original item i: P(Y_{j,i}=1 | θ_j, ξ_j) = ξ_j + (1−ξ_j)·σ(a_i(θ_j − b_i))\n- θ_j = model j's genuine reasoning ability (person parameter)\n- ξ_j ∈ [0,1] = model j's global contamination probability (person parameter) — probability that model j has memorized any given original item, assumed uniform across items\n- a_i, b_i = discrimination and difficulty (fixed from Stage 1)\n- δ_i = variant difficulty shift (estimated in Stage 2)\n- Only M additional contamination parameters (vs. M+K for full model), yielding far stronger identifiability at N=15-20\n- Interpretation: ξ_j captures bulk training data contamination (entire benchmarks appearing in web scrapes), which is the dominant contamination mechanism for LLMs\n\nFull G-2PL (person × item contamination, M+K additional parameters):\n- For variant item i*: P(Y_{j,i*}=1 | θ_j) = σ(a_i(θ_j − b_i − δ_i))\n- For original item i: P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i))\n- η_i ∈ [0,1] = item i's contamination susceptibility (item parameter)\n- Adopted only if the simulation study (see below) confirms η_i is recoverable at N=15-20 with acceptable RMSE\n- Each η_i has only M=15-20 observations, making estimation challenging — hierarchical priors provide regularization\n\n**Rationale for G-2PL over G-3PL:** The guessing parameter c_i in 3PL requires 200+ examinees for stable estimation under classical methods, while we have only 15-20 models. Dropping c_i to use 2PL eliminates the most problematic parameter for small samples while retaining the core contamination decomposition. For math benchmarks with open-ended answers (MATH-500, GSM8K), guessing probability is effectively zero, making 2PL substantively appropriate.\n\n**Ablation to Gated-3PL (G-3PL):**\n- P(Y_{j,i*}=1 | θ_j) = c_i + (1−c_i)·σ(a_i(θ_j − b_i − δ_i))\n- P(Y_{j,i}=1 | θ_j, ξ_j, η_i) = ξ_j·η_i + (1−ξ_j·η_i)·[c_i + (1−c_i)·σ(a_i(θ_j − b_i))]\n- c_i fixed to domain-specific constants: c_i = 0 for open-ended math (MATH-500, GSM8K), enabling estimation only for any future MCQ extensions.\n\n**Estimation strategy (fully specified):**\nPrimary: Bayesian MCMC via NumPyro/Stan with hierarchical priors, following DGM's original estimation framework:\n- θ_j ~ N(0, σ²_θ), σ_θ ~ Half-Cauchy(0, 2.5)\n- ξ_j ~ Beta(α_ξ, β_ξ), with α_ξ, β_ξ ~ Gamma(2, 1) (hierarchical; allows posterior to concentrate near 0 for clean models or near 1 for heavily contaminated ones)\n- η_i ~ Beta(α_η, β_η), with α_η, β_η ~ Gamma(2, 1) (hierarchical; full G-2PL only)\n- δ_i ~ N(0, σ²_δ), σ_δ ~ Half-Cauchy(0, 1) (hierarchical; variant shifts expected small)\n- a_i, b_i: fixed from Stage 1 (NOT estimated in Stage 2)\n- MCMC: 4 chains × 2,000 warmup + 2,000 samples, NUTS sampler, R̂ < 1.05 convergence criterion, ESS > 400 per parameter\nComparison: Neural estimation extending PSN-IRT's pseudo-Siamese architecture with an additional gating head that outputs (ξ_j, η_i) — trained via binary cross-entropy on the joint original+variant response matrix, with a_i and b_i initialized from Stage 1 and optionally frozen. This provides a non-Bayesian point estimate comparison.\nAblation: Variational inference via Pyro SVI as a faster alternative to MCMC, using amortized inference for scalability testing.\n\n**Formal identifiability (strengthened by two-stage calibration):**\nWe prove identifiability via a two-step argument that is substantially strengthened by fixing a_i and b_i from Stage 1:\n\n(1) Variant items serve as contamination-free anchors. With a_i, b_i fixed from Stage 1, θ_j is identified from variant responses via standard 2PL person parameter estimation (K ≈ 1,000 items per model, well-determined even for a single model). The difficulty shift δ_i is identified from M model responses per variant item; with M=15-20 and hierarchical priors, this yields credible estimates (validated in simulation study). Key advantage of fixed-parameter calibration: θ_j identification does not depend on the number of models M, only on the number of items K per model — eliminating the classical IRT concern about few examinees.\n\n(2) Given identified θ_j, fixed a_i, b_i, and estimated δ_i, the original-variant performance gap identifies the contamination gate. For R-G-2PL: M gaps per item constrain M values ξ_j — with K ≈ 1,000 items per model, each ξ_j is massively over-determined. For full G-2PL: M·K observed gaps constrain the bilinear product ξ_j·η_i. Under rank-1 bilinear decomposition with M models and K items, M·K observations constrain M+K−1 free parameters (one fixed for scale), identifiable when (M−1)(K−1) > 0 — satisfied for any M,K ≥ 2.\n\n(3) Fisher information: The 2PL Fisher information matrix is well-conditioned even at M=15, unlike 3PL where c_i creates flat likelihood surfaces. With fixed a_i and b_i, the conditional Fisher information for (θ_j, ξ_j) given item parameters has full rank, ensuring local identifiability. The two-stage approach avoids the joint estimation instabilities that plague IRT with few examinees.\n\n**Simulation study for parameter recovery (new, Week 4, 1-2 days CPU):**\n\nDesign: Fully crossed simulation validating G-2PL parameter recovery under two-stage calibration at the target sample sizes.\n\nGenerating model:\n- Item parameters: a_i ~ LogNormal(0, 0.5), b_i ~ N(0, 1), fixed as Stage 1 calibrated values (not re-estimated)\n- θ_j ~ N(0, 1)\n- Contamination prevalence/strength, three scenarios:\n  (a) Low: 20% of models contaminated (ξ_j ~ Beta(8,2) for contaminated, ξ_j = 0 for clean)\n  (b) Medium: 50% of models with ξ_j ~ Beta(5,5) (moderate, variable contamination)\n  (c) High: 80% of models with ξ_j ~ Beta(2,2) (widespread, variable strength)\n- η_i ~ Beta(2, 5) for full G-2PL (most items not highly susceptible)\n- δ_i ~ N(0, 0.5)\n\nConditions (fully crossed):\n- N (models): {15, 20, 50}\n- K (paired items): {100, 500}\n- Contamination scenario: {low, medium, high}\n- Model: {R-G-2PL (ξ_j only), full G-2PL (ξ_j and η_i)}\n- Total: 3 × 2 × 3 × 2 = 36 conditions\n\nReplications: 500 per condition (following Konig et al. 2023; Fox 2025 used 1,000 but with simpler models)\n\nMetrics (per condition, averaged over replications):\n- θ_j: bias, RMSE, 95% credible interval coverage, Kendall-τ with true θ ranking\n- ξ_j: bias, RMSE, 95% CI coverage, Kendall-τ with true ξ ranking\n- η_i (full G-2PL only): bias, RMSE, 95% CI coverage\n- Classification: sensitivity/specificity for identifying contaminated models (ξ_j > 0.3)\n- MCMC diagnostics: mean R̂, mean ESS, non-convergence rate\n\nMCMC per replication: 4 chains × 1,000 warmup + 1,000 samples, NUTS. Estimated compute: ~30s per replication (small model with fixed item params) × 18,000 fits = ~150 CPU-hours, parallelizable across cores to complete in 1-2 days.\n\nDecision rule: If ξ_j RMSE < 0.15 and coverage ∈ [0.90, 0.98] at N=15, proceed with full G-2PL. If η_i recovery is poor (RMSE > 0.25 or coverage < 0.85), adopt R-G-2PL as primary and relegate full G-2PL to future work with larger model pools.\n\n**Prior sensitivity analysis (new, 1 day):**\n\nThree prior specifications applied to the real data MCMC:\n(a) Proposed hierarchical: ξ_j ~ Beta(α_ξ, β_ξ), α_ξ, β_ξ ~ Gamma(2,1) — data-driven, allows concentration near 0 or 1\n(b) Weakly informative flat: ξ_j ~ Beta(1,1) (uniform on [0,1]), η_i ~ Beta(1,1) — maximum prior uncertainty, no hierarchical pooling\n(c) Informative: ξ_j ~ Beta(α_j, β_j) with person-specific priors informed by ConStat contamination flags where available (models flagged contaminated get ξ_j ~ Beta(5,2), unflagged get ξ_j ~ Beta(2,5)); η_i ~ Beta(2,5) reflecting prior belief that most items are not highly susceptible\n\nReport:\n- θ_j ranking stability: Kendall-τ between corrected ability rankings under the three prior specifications\n- ξ_j ordering stability: Kendall-τ between contamination orderings\n- Posterior credible interval widths: precision comparison across priors\n- Key qualitative conclusions: do the same models get flagged as high-contamination (ξ_j > 0.5)?\n- Sensitivity metric: maximum |Δξ_j| across prior pairs for any model — quantifies worst-case prior influence\n\n**Bilinear rank-1 model adequacy plan (full G-2PL only):**\nThe rank-1 assumption (ξ_j·η_i) treats contamination as model-global and item-global, a first-order approximation. We assess:\n(a) Compute standardized residuals r_{j,i} = (Y_{j,i} − P̂_{j,i}) / √(P̂_{j,i}(1−P̂_{j,i})) from the rank-1 fit and report the residual matrix.\n(b) Compute Yen's Q3 statistic for local dependence among original items after conditioning on θ_j — systematic topic-structured residuals would indicate rank-1 insufficiency.\n(c) Apply person-fit statistics (standardized log-likelihood lz*) to detect models whose original-item response patterns deviate from the G-2PL predictions, flagging potential topic-specific contamination.\n(d) If structured residuals emerge, explore rank-2 extension (ξ_j·η_i → ξ_j^(1)·η_i^(1) + ξ_j^(2)·η_i^(2)) or topic-stratified estimation as explicit future work.\n(e) Justification for rank-1 as starting point: LLM contamination is primarily driven by overall training data overlap (entire benchmark suites appearing in Common Crawl/web scrapes) rather than topic-selective memorization; the rank-1 model captures this dominant effect.\n\n**Data collection (within 200 H100-hr budget):**\n\nStage 1 data: Assemble GSM8K per-item response matrix from Open LLM Leaderboard V1 per-model details datasets (huggingface.co/open-llm-leaderboard-old, ~7,000 per-model datasets). Each model's GSM8K details available in configuration 'harness_gsm8k' with per-item correctness fields. Data assembly via HuggingFace datasets library: iterate over available details datasets, extract GSM8K responses, construct binary response matrix. Expected: N_cal ≈ 2,000+ models × 1,359 items. Data assembly effort: ~1 day engineering. For MATH-500: supplement with targeted evaluation of ~50-100 small V1 models on MATH-500 (~15 H100-hrs) plus V2 Level 5 per-item data where available.\n\nStage 2 data: For ~1,000 items (all 1,359 GSM8K items + MATH-500 items up to budget), generate adversarial variants via a novel SymPy-verified rewrite pipeline. This is NOT a MaSTer replication — MaSTer uses LLM-based verification via Qwen2.5-32B-Instruct (98% precision on a rewrite meaning-preservation check); our pipeline instead combines LLM-based rewriting (Qwen3.6-27B for multi-round adversarial rewrites) with formal symbolic verification (SymPy for numerical answer correctness), a novel hybrid that provides stronger guarantees than LLM-only verification for math problems with determinate numerical answers. Pipeline: (1) Qwen3.6-27B generates candidate variants via value/structure perturbation, (2) SymPy verifies that the perturbed problem has a valid, determinate answer differing from the original, (3) human spot-check on 10% sample. Estimated: ~25 H100-hrs for variant generation.\n\nBackup pipelines (if primary pipeline yields <80% valid variants by Week 2): (a) MathCheck (ICLR 2025, open code at github.com/PremiLab-Math/MathCheck) for GSM8K variants; (b) seed with MATH-Perturb's 279 expert-crafted Level 5 perturbations (ICML 2025, open code at github.com/Kaffaljidhmah2/MATH-Perturb) and extend via LLM rewriting for remaining items.\n\nModel evaluation: Collect response matrices from 15-20 models: 10 open-weight (DeepSeek-R2 32B, DeepSeek-V4-Flash 284B, Qwen3.6-27B, Qwen3.5-397B-A17B, GLM-5.1 754B-A40B, OLMo-2-13B, Llama-4-Maverick-17B-A400B, Mistral-Large-3, plus 2 smaller reference models) and 5-8 closed-API models (GPT-4o, GPT-5.2, Claude Sonnet 4.6, Gemini 2.5 Flash, Gemini 3.1 Pro). For GSM8K originals: reuse Open LLM Leaderboard V1 per-item data where available (many open-weight models already evaluated); run new inference only for models not on V1 (~40 H100-hrs). Variant inference: all 15-20 models on generated variants (~80 H100-hrs for open-weight models). Closed-model API costs estimated separately. IRT fitting is negligible (<1 hr CPU for MCMC).\n\n**Validation (four-pronged, addressing domain mismatch concern):**\n\n(1) External ranking correlation: Kendall-τ of CRADE-corrected ability rankings vs. MathArena 2026 uncontaminated competition rankings (~900 problems, 50+ models), targeting τ ≥ 0.85 (revised from 0.90 given domain mismatch between textbook-style MATH-500/GSM8K and competition-style MathArena). Report bootstrap 95% confidence interval. Compare against: (a) raw accuracy rankings, (b) RankLLM difficulty-weighted rankings, (c) DCR-corrected rankings (r=0.66 on hard tasks), (d) JECS-filtered rankings.\n\n(2) Synthetic contamination injection (causal validation): Deliberately fine-tune OLMo-2-13B on MATH-500 training items (1 epoch, mild contamination following established protocols from contamination survey literature) and re-evaluate. If G-2PL correctly recovers elevated ξ for the fine-tuned model while θ remains stable (matching pre-contamination ability), this provides causal evidence that the decomposition works. Compare fine-tuned ξ against clean OLMo-2-13B ξ via posterior credible interval separation. This is the strongest validation because it provides ground-truth contamination status.\n\n(3) Convergent validity with existing detectors: Correlate G-2PL's per-model ξ_j estimates with: (a) ConStat contamination flags (performance gap on rephrased vs. original), (b) PaCoST binary contamination verdicts (paired confidence significance test), (c) PSN-IRT's anomalous guessing-rate parameters. High concordance validates that ξ captures the same construct; low concordance would require investigation of what ξ uniquely captures beyond existing methods.\n\n(4) Ablation showing differential correction benefit: Demonstrate that CRADE correction improves ranking accuracy (vs. MathArena) more for models with high estimated ξ (provably or detectably contaminated) than for models with low ξ. This confirms the correction is targeted rather than uniformly applied.\n\n**Anchor assumption validation (variant contamination-free):**\n(a) Fit standard 2PL to variant-only response matrix (with a_i fixed from Stage 1, estimating only θ_j and δ_i) and compute item-fit statistics (S-X² or Orlando-Thissen) and person-fit statistics (lz*). Good fit supports the anchor assumption — variants behave like clean IRT items measuring genuine ability.\n(b) Check that variant difficulty b_i + δ_i is predictable from original difficulty b_i plus a systematic shift; high-residual outlier items may indicate re-contaminated variants and should be flagged for manual review.\n(c) Cross-validation: Hold out 20% of variant items, fit 2PL on remaining 80%, predict held-out responses. Prediction accuracy comparable to full-data fit supports generalizability.\n(d) Ablation: Compare CRADE results using MATH-Perturb's expert-crafted perturbations (strongest anchor assumption) vs. our SymPy-verified rewrite pipeline to assess sensitivity to variant quality.\n\nAblations: (a) R-G-2PL (ξ_j only) vs. full G-2PL (ξ_j and η_i) — does item-level susceptibility add meaningful signal?, (b) G-2PL vs. G-3PL (with fixed c_i = 0 for math), (c) Bayesian MCMC vs. neural estimation vs. variational inference, (d) number of variant items (100/500/1000), (e) number of models (10/15/20), (f) sensitivity to variant difficulty shift δ_i, (g) rank-1 vs. rank-2 bilinear decomposition if residuals warrant it, (h) RankLLM vs. G-2PL ranking quality, (i) two-stage calibration (GSM8K) vs. concurrent estimation (MATH-500) quality comparison, (j) prior sensitivity across 3 specifications.\n\n## Detailed Description\n\nCRADE introduces a measurement-theoretic framework for decomposing LLM benchmark performance into genuine reasoning ability (θ), contamination exposure (ξ), and item properties, by extending the Deterministic Gated IRT model (DGM; Shu et al., Psychometrika 2013) from test-security psychometrics to LLM evaluation. The central methodological innovation is a two-stage fixed-parameter calibration architecture: Stage 1 calibrates item parameters (discrimination a_i, difficulty b_i) from Open LLM Leaderboard V1 per-item response data (~2,000+ models × 1,359 GSM8K items, following Polo et al. ICML 2024 and Growing Pains arXiv April 2026), providing well-identified item parameters grounded in large-N calibration; Stage 2 fixes these item parameters and estimates the gated contamination model on a 15-20-model paired response matrix, reducing the estimation problem to person-level ability (θ_j), contamination (ξ_j), item susceptibility (η_i), and variant difficulty shifts (δ_i) only. Two model tiers are presented: (1) the Reduced G-2PL (R-G-2PL), where P(Y_{j,i}=1) = ξ_j + (1−ξ_j)·σ(a_i(θ_j − b_i)) adds only M person-level contamination parameters, maximally parsimonious at N=15-20; and (2) the Full G-2PL, where P(Y_{j,i}=1) = ξ_j·η_i + (1−ξ_j·η_i)·σ(a_i(θ_j − b_i)) adds M+K parameters with item-specific susceptibility, adopted only if the simulation study confirms η_i recovery. The simulation study (500 replications × 36 conditions: N∈{15,20,50} × K∈{100,500} × 3 contamination scenarios × 2 models) validates parameter recovery under two-stage calibration, reporting bias, RMSE, and 95% credible interval coverage for θ_j and ξ_j — the single most important addition for psychometric-savvy reviewers. Prior sensitivity analysis under three specifications (hierarchical Beta, flat Beta(1,1), ConStat-informed) demonstrates robustness of person-level conclusions. The paired-item design couples each benchmark question with a SymPy-verified adversarial variant — a novel hybrid pipeline combining LLM-based rewriting (Qwen3.6-27B) with symbolic answer verification, providing stronger mathematical guarantees than MaSTer's LLM-only verification. Variant items serve as contamination-free anchors: with item parameters fixed from Stage 1, θ_j is identified from ~1,000 variant items per model (well-determined even for a single model), then contamination parameters are identified from original-variant performance gaps with provable identifiability ((M−1)(K−1) > 0 for rank-1 bilinear decomposition). This circumvents the critical failure of likelihood-based contamination detection on reasoning models (AUROC ≈ 50%, Wang et al. ICLR 2026) by operating entirely on response patterns. Four-pronged validation: (1) Kendall-τ ≥ 0.85 against MathArena's ~900-problem uncontaminated rankings, compared against RankLLM non-parametric baseline, DCR correction, and JECS-filtered rankings; (2) synthetic contamination injection via fine-tuning OLMo-2-13B to causally verify ξ recovery; (3) convergent validity with ConStat, PaCoST, and PSN-IRT; (4) differential correction benefit for high-ξ models. Model adequacy assessed via standardized residuals, Q3 statistics, and person-fit lz* from rank-1 bilinear fit. Focused on GSM8K (1,359 items, full two-stage calibration) with MATH-500 as secondary benchmark, 15-20 models including DeepSeek-R2 32B, Qwen3.6-27B, GLM-5.1, and 5-8 closed-API models, within 230 H100-hrs.\n\n## Key References\n\n- Lost in Benchmarks? Rethinking LLM Benchmarking with Item Response Theory [PSN-IRT] (AAAI 2026 Oral) — 4PL IRT for 12 LLMs on 41,871 items via pseudo-Siamese neural estimation; flags contamination via guessing-rate anomalies but leaves corrected scoring as open question; demonstrates neural IRT estimation works with very few examinees\n- RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty (ICLR 2026) — non-parametric bidirectional score propagation achieving 90% human alignment on 30 models × 35,550 questions; robust to 50% model removal (ρ=0.94); no contamination modeling; our primary non-parametric baseline\n- DCR: Quantifying Data Contamination in LLMs Evaluation (EMNLP 2025) — ad-hoc multiplicative contamination correction achieving r=0.66 on hard tasks; our measurement-theoretic G-2PL subsumes this\n- On The Fragility of Benchmark Contamination Detection in Reasoning Models [Wang, Li, Ko, Zhang] (ICLR 2026) — proves likelihood-based detection fails on reasoning models (AUROC ≈ 50%); motivates response-pattern-based approach\n- Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise [DGM; Shu, Henson, Luecht] (Psychometrika 2013) — key theoretical precedent: gated IRT with hierarchical MCMC estimation decomposes performance into ability + preknowledge; we extend to unknown item exposure via paired items and two-stage calibration\n- ConStat: Performance-Based Contamination Detection in Large Language Models (NeurIPS 2024) — detects contamination via performance gaps on rephrased samples against reference models; confirms paired-item signal but no latent-variable model; used as convergent validity comparison and informative prior source\n- Provable Joint Decontamination for Benchmarking Multiple Large Language Models [JECS] (arXiv May 2026) — conformal p-values via joint envelope selection for multi-model decontamination; binarizes items (keep/discard) while we produce continuous corrected scores\n- RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning (arXiv 2025) — uses IRT as difficulty reward for RL-based rewriting; we use IRT for joint ability-contamination estimation\n- Toward Automated Robustness Evaluation of Mathematical Reasoning [MaSTer] (arXiv 2026) — validated multi-round adversarial variant pipeline (5 streams × 3 iterations) on 4×4090 GPUs using Qwen2.5-32B-Instruct with LLM-based verification (98% precision); 45-94% failure rates on GSM8K/MATH-500; code claimed at github.com/sustech-nlp/MaSTer but unavailable as of May 2026; our pipeline differs by using SymPy-based symbolic verification instead of LLM-based verification\n- Is Your Model Really A Good Math Reasoner? Evaluating Mathematical Reasoning with Checklist [MathCheck] (ICLR 2025) — open-source variant generation pipeline for GSM8K and GeoQA; backup pipeline for variant generation\n- MATH-Perturb: Benchmarking LLMs' Math Reasoning Abilities against Hard Perturbations (ICML 2025) — 279 expert-crafted MATH Level-5 perturbations with SymPy verification; demonstrates 10-25% drops on frontier models; open code provides seed perturbations and strongest anchor-assumption validation\n- MathArena: Evaluating LLMs on Uncontaminated Math Competitions (NeurIPS 2025 D&B Track) — expanded to ~900 problems across 2025-2026 competitions including AIME 2026, HMMT Feb 2026, USAMO 2026, ArXivMath monthly, BrokenArxiv, ArXivLean, Visual Math, Project Euler, and Apex; our primary ground-truth validation source\n- PaCoST: Paired Confidence Significance Testing for Benchmark Contamination Detection in LLMs (arXiv 2024) — paired original-perturbed items for binary contamination detection via three-step statistical analysis; confirms paired signal without latent-variable modeling; used as convergent validity comparison\n- Redefining Item Response Models for Small Samples [Fox] (Journal of Educational and Behavioral Statistics 2025) — IRT-BCSM integrates out person parameters for stable estimation at N=50-100; RMSE=0.110 for discrimination at N=50 while standard MML collapses (RMSE=1.782); establishes that Bayesian IRT estimation is viable with small person samples\n- On the Identifiability of 3- and 4-Parameter IRT Models From the Perspective of Knowledge Space Theory [Noventa, Ye, Kelava, Spoto] (Psychometrika 2024) — establishes identifiability conditions for 3PL/4PL via knowledge space theory; our G-2PL proof builds on these results with simpler conditions enabled by the 2PL base\n- Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration [Habba, Itzhak, Yehudai, Perlitz, Bandel, Shmueli-Scheuer, Choshen, Stanovsky] (arXiv April 2026) — two-stage MIRT 2PL fixed-parameter calibration on 295+ Open LLM Leaderboard models, <2% MAE with 100 anchor items, ρ≥0.9; validates the two-stage architecture we adopt for item parameter calibration\n- tinyBenchmarks: evaluating LLMs with fewer examples [Polo, Weber, Choshen, Sun, Xu, Stanovsky] (ICML 2024) — assembles per-item binary response data from Open LLM Leaderboard V1 for 395 models × ~29K items; provides the data assembly methodology and validates IRT-based prediction from small item subsets; our Stage 1 calibration follows their data reconstruction approach\n- Robustness of the Hierarchical 2PL Bayesian Model Under Diverse Conditions [Konig, Khorramdel, Falk, Schmitt] (Behavior Research Methods 2023) — OH2PL with half-Cauchy hyperpriors produces unbiased estimates at N=50 (bias ±0.04) while MML yields 75-89% inadmissible solutions; validates hierarchical Bayesian IRT at small sample sizes; 864 conditions × 100 replications across 6 sample sizes\n- Investigating a weakly informative prior for item scale hyperparameters in hierarchical 3PNO IRT models [Luo, Jiao] (Frontiers in Psychology 2017) — half-t priors for hierarchical IRT; informs our prior specification and sensitivity analysis design for the G-2PL contamination parameters\n- py-irt: A Scalable Item Response Theory Library for Python (IJOC 2023) — GPU-accelerated Bayesian IRT fitting via variational inference; comparison estimation method\n- The Illusion of Reasoning: Step-Level Evaluation Reveals Decorative Chain-of-Thought in Frontier Language Models (arXiv April 2026) — reasoning modes (genuine/scaffolding/decorative); provides qualitative taxonomy for interpreting contamination-ability decomposition\n\n## Resource Estimate\n\n- **manual**: gpu_hours: ~200 H100-hrs (Stage 1 data assembly: 0 GPU / 1 day engineering for GSM8K, 15 hrs for MATH-500 model evaluation; variant generation: 25 hrs with Qwen3.6-27B; open-weight inference on variants: 80 hrs across 10 models; gap-filling original inference: 40 hrs; synthetic contamination fine-tuning of OLMo-2-13B: 5 hrs; buffer: 10 hrs; simulation study: ~150 CPU-hrs / 0 GPU; prior sensitivity: ~10 CPU-hrs / 0 GPU), timeline: 8 weeks (1 researcher: wk1 pipeline+V1 data assembly+variant generation start, wk2 variant generation completion+Stage 1 2PL calibration, wk3 inference+Stage 2 data collection, wk4 G-2PL+R-G-2PL implementation in NumPyro+simulation study (1-2 days CPU), wk5 fitting on real data+prior sensitivity analysis+synthetic contamination experiment, wk6 validation+ablations+RankLLM comparison, wk7-8 writing+proofs+residual analysis), estimated_gpu_cost: $2,100 ($600 GPU compute at $3/hr + $1,400 closed-model API for 8 models × 1K items × ~$0.002/item avg + $100 OLMo fine-tuning)\n- **human_in_loop**: gpu_hours: ~170 H100-hrs (aggressive leaderboard data reuse for Stage 1, focused variant generation on GSM8K only for initial submission, MATH-500 as ablation, skip MATH-500 Stage 1 model evaluation), timeline: 6 weeks, claude_api_cost: $300 (G-2PL+R-G-2PL model implementation in NumPyro, identifiability proof verification, simulation study scripting, residual analysis scripts, RankLLM baseline implementation, prior sensitivity analysis, paper drafting), estimated_gpu_cost: $1,900 ($510 GPU + $1,390 closed-model APIs)\n- **auto_research**: gpu_hours: ~230 H100-hrs (full 20-model coverage, automated hyperparameter sweeps over R-G-2PL/G-2PL/G-3PL variants, extended MATH-500 coverage with Stage 1 calibration, synthetic contamination experiment with 3 fine-tuning recipes, 1000-replication simulation study), timeline: 4 weeks (parallel inference, automated ablation grid), claude_api_cost: $950 (variant generation QA, pipeline orchestration, automated ablation analysis including R-G-2PL vs G-2PL comparison, simulation study analysis, prior sensitivity, draft writing, RankLLM reimplementation), estimated_gpu_cost: $2,600 ($690 GPU + $1,910 closed-model APIs), speed_bottleneck: Sequential GPU inference for MoE models (DeepSeek-V4-Flash on 2×H100, Qwen3.5-397B on 4×H100, GLM-5.1 on 4×H100); MCMC fitting with 4 chains is parallelizable but takes ~30 min on CPU; simulation study is embarrassingly parallel across conditions\n"
}
```

---

### Runtime record

_source line 2 · 2026-05-28T14:15:00.246Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-28T14:15:00.246Z",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

## Round 1

54 recorded events

### User

_source line 3 · 2026-05-28T14:15:00.271Z_

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
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "56ee91bb-1de7-4c69-b6bf-aeea8109f49c",
  "permissionMode": "default",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-28T14:15:00.268Z_

```json
{
  "parentUuid": "56ee91bb-1de7-4c69-b6bf-aeea8109f49c",
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
  "uuid": "ce577362-c866-456d-952a-a5750ef64cd5",
  "timestamp": "2026-05-28T14:15:00.268Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-28T14:15:00.268Z_

```json
{
  "parentUuid": "ce577362-c866-456d-952a-a5750ef64cd5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "38441365-d556-4ce5-8457-0d2fdb570ee0",
  "timestamp": "2026-05-28T14:15:00.268Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
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
  "lastPrompt": "# CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  ## Core Problem  No existing framework can determine whether a model fails adversarial…",
  "leafUuid": "38441365-d556-4ce5-8457-0d2fdb570ee0",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Develop CRADE contamination-ability IRT framework",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Assistant

_source line 8 · 2026-05-28T14:15:07.995Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to act as the "发掘 agent" (Discovery Agent) to analyze this research proposal for AAAI 2026. Let me first read and understand the proposal thoroughly, then conduct web searches to understand the current landscape before providing my analysis.

The proposal is about CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items. It proposes extending the Deterministic Gated IRT model (DGM) from psychometrics to LLM evaluation, using a two-stage calibration approach to decompose benchmark performance into genuine ability and contamination components.


Now I need to search the web to understand what's currently being done in this space and assess how novel this approach really is.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "38441365-d556-4ce5-8457-0d2fdb570ee0",
  "isSidechain": false,
  "requestId": "req_011CbV7AKt6xeCS2pc56FYmQ",
  "type": "assistant",
  "uuid": "160c6adf-5d5f-40bf-988d-f3f272c25706",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwLCxnAmMpuu3gBzvusCE7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16397,
      "cache_read_input_tokens": 11014,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16397,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 289,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16397
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

_source line 9 · 2026-05-28T14:15:08.000Z_

I'll start by thoroughly reading the proposal, then conduct the required web searches to understand the current landscape before providing my analysis. Let me do multiple targeted searches in parallel.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "160c6adf-5d5f-40bf-988d-f3f272c25706",
  "isSidechain": false,
  "requestId": "req_011CbV7AKt6xeCS2pc56FYmQ",
  "type": "assistant",
  "uuid": "3a8126a5-7879-4cda-b6f1-ae3a3b6396b6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwLCxnAmMpuu3gBzvusCE7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16397,
      "cache_read_input_tokens": 11014,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16397,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 289,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16397
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

_source line 10 · 2026-05-28T14:15:08.047Z_

<details open><summary>🔧 Tool call — ToolSearch · `toolu_01DxDi5oEsm7E33aGsPtekRy`</summary>

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
  "parentUuid": "3a8126a5-7879-4cda-b6f1-ae3a3b6396b6",
  "isSidechain": false,
  "requestId": "req_011CbV7AKt6xeCS2pc56FYmQ",
  "type": "assistant",
  "uuid": "1bdb8347-3184-4418-adc2-eae9b7af0c80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PwLCxnAmMpuu3gBzvusCE7",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16397,
      "cache_read_input_tokens": 11014,
      "output_tokens": 289,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16397,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 289,
          "cache_read_input_tokens": 11014,
          "cache_creation_input_tokens": 16397,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16397
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

_source line 11 · 2026-05-28T14:15:08.061Z_

<details><summary>↩ Tool result · `toolu_01DxDi5oEsm7E33aGsPtekRy`</summary>

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
  "parentUuid": "1bdb8347-3184-4418-adc2-eae9b7af0c80",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "2f8542d0-e167-445b-bcb6-2407cfb32faf",
  "toolUseResult": {
    "matches": [
      "WebSearch"
    ],
    "query": "select:WebSearch",
    "total_deferred_tools": 19
  },
  "sourceToolAssistantUUID": "1bdb8347-3184-4418-adc2-eae9b7af0c80",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 12 · 2026-05-28T14:15:10.778Z_

Now let me conduct the required pre-research searches in parallel to understand the current landscape.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2f8542d0-e167-445b-bcb6-2407cfb32faf",
  "isSidechain": false,
  "requestId": "req_011CbV7Au8MhqnxAri2e9B6S",
  "type": "assistant",
  "uuid": "5ee1569f-33d0-4309-acfd-a9816edbca14",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nDFFKELxX98rjLgikLpLi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 27411,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 27411,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 816
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

_source line 13 · 2026-05-28T14:15:10.920Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01PooSFCgJSZsaYmDn6HFNmC`</summary>

```json
{
  "query": "IRT item response theory LLM evaluation contamination detection 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5ee1569f-33d0-4309-acfd-a9816edbca14",
  "isSidechain": false,
  "requestId": "req_011CbV7Au8MhqnxAri2e9B6S",
  "type": "assistant",
  "uuid": "12c4d0a3-9e94-4689-818b-e2481cb6435c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_015nDFFKELxX98rjLgikLpLi",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 3,
      "cache_creation_input_tokens": 816,
      "cache_read_input_tokens": 27411,
      "output_tokens": 89,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 816,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 3,
          "output_tokens": 89,
          "cache_read_input_tokens": 27411,
          "cache_creation_input_tokens": 816,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 816
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

_source line 14 · 2026-05-28T14:15:18.559Z_

<details><summary>↩ Tool result · `toolu_01PooSFCgJSZsaYmDn6HFNmC`</summary>

```text
Web search results for query: "IRT item response theory LLM evaluation contamination detection 2025 2026"

Links: [{"title":"What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide","url":"https://llm-stats.com/blog/research/what-is-a-contaminated-llm"},{"title":"Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory","url":"https://arxiv.org/pdf/2602.00521"},{"title":"Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking","url":"https://arxiv.org/pdf/2603.23506"},{"title":"RADAR: Mechanistic Pathways for Detecting Data Contamination in LLM Evaluation","url":"https://arxiv.org/pdf/2510.08931"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"}]

I found several relevant research papers on these topics from 2025-2026. Here's what the search revealed:

## IRT and LLM Evaluation

A two-phase diagnostic framework grounded in Item Response Theory (IRT) has been introduced for assessing the reliability of LLM-as-a-Judge, adopting the Graded Response Model (GRM) of IRT to formalize reliability along two dimensions: intrinsic consistency and human alignment. This framework provides interpretable signals for diagnosing LLM judgments systematically and offers practical guidance for verifying reliability of LLM-as-a-Judge.

Another approach proposes a computerized adaptive testing (CAT) framework grounded in item response theory for efficient assessment of LLMs, comprising a two-phase design with Monte Carlo simulation and empirical evaluation of 38 LLMs using a human-calibrated medical item bank.

## Contamination Detection

Data contamination remains a major challenge in LLM evaluation, with overlap between training and evaluation sets inflating metrics and obscuring the distinction between genuine reasoning and memorization. A contamination detection method called RADAR achieves 93% accuracy on diverse evaluation sets using mechanistic interpretability features.

Recent work on psychometric evaluations provides evidence that popular inventories such as the Big Five Inventory and Portrait Values Questionnaire exhibit strong contamination, where models can memorize items and adjust responses to achieve specific target scores.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "12c4d0a3-9e94-4689-818b-e2481cb6435c",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "137d5a90-b91c-467a-b6ac-b1d238807798",
  "toolUseResult": {
    "query": "IRT item response theory LLM evaluation contamination detection 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01PUKQc3dBcTFwgd3FcpXApP",
        "content": [
          {
            "title": "What Is a Contaminated LLM? Detection, Famous Cases, 2026 Guide",
            "url": "https://llm-stats.com/blog/research/what-is-a-contaminated-llm"
          },
          {
            "title": "Diagnosing the Reliability of LLM-as-a-Judge via Item Response Theory",
            "url": "https://arxiv.org/pdf/2602.00521"
          },
          {
            "title": "Leveraging Computerized Adaptive Testing for Cost-effective Evaluation of Large Language Models in Medical Benchmarking",
            "url": "https://arxiv.org/pdf/2603.23506"
          },
          {
            "title": "RADAR: Mechanistic Pathways for Detecting Data Contamination in LLM Evaluation",
            "url": "https://arxiv.org/pdf/2510.08931"
          },
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/pdf/2510.07175"
          }
        ]
      },
      "I found several relevant research papers on these topics from 2025-2026. Here's what the search revealed:\n\n## IRT and LLM Evaluation\n\nA two-phase diagnostic framework grounded in Item Response Theory (IRT) has been introduced for assessing the reliability of LLM-as-a-Judge, adopting the Graded Response Model (GRM) of IRT to formalize reliability along two dimensions: intrinsic consistency and human alignment. This framework provides interpretable signals for diagnosing LLM judgments systematically and offers practical guidance for verifying reliability of LLM-as-a-Judge.\n\nAnother approach proposes a computerized adaptive testing (CAT) framework grounded in item response theory for efficient assessment of LLMs, comprising a two-phase design with Monte Carlo simulation and empirical evaluation of 38 LLMs using a human-calibrated medical item bank.\n\n## Contamination Detection\n\nData contamination remains a major challenge in LLM evaluation, with overlap between training and evaluation sets inflating metrics and obscuring the distinction between genuine reasoning and memorization. A contamination detection method called RADAR achieves 93% accuracy on diverse evaluation sets using mechanistic interpretability features.\n\nRecent work on psychometric evaluations provides evidence that popular inventories such as the Big Five Inventory and Portrait Values Questionnaire exhibit strong contamination, where models can memorize items and adjust responses to achieve specific target scores."
    ],
    "durationSeconds": 7.630080907,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "12c4d0a3-9e94-4689-818b-e2481cb6435c",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 15 · 2026-05-28T14:15:21.792Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01ERrRS6kNdLujFUEJi9zbSB`</summary>

```json
{
  "query": "PSN-IRT AAAI 2026 lost in benchmarks rethinking LLM benchmarking item response theory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "137d5a90-b91c-467a-b6ac-b1d238807798",
  "isSidechain": false,
  "requestId": "req_011CbV7BfrvBpcBsagsVFUDr",
  "type": "assistant",
  "uuid": "7afe40d9-f935-47e9-8723-fea8d1a7d47a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Jm6r12kKAmwkG9KDYY8fGa",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 687,
      "cache_read_input_tokens": 28227,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 687,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 28227,
          "cache_creation_input_tokens": 687,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 687
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

_source line 16 · 2026-05-28T14:15:28.094Z_

<details><summary>↩ Tool result · `toolu_01ERrRS6kNdLujFUEJi9zbSB`</summary>

```text
Web search results for query: "PSN-IRT AAAI 2026 lost in benchmarks rethinking LLM benchmarking item response theory"

Links: [{"title":"GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub","url":"https://github.com/Joe-Hall-Lee/PSN-IRT"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://chatpaper.com/paper/139423"},{"title":"Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://huggingface.co/papers/2505.15055"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence","url":"https://ojs.aaai.org/index.php/AAAI/article/view/40814"},{"title":"(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://arxiv.org/pdf/2505.15055"}]

I found information about this paper. Here's what I found:

## Overview

The paper titled "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory" was selected as [AAAI 2026 Oral].

## The PSN-IRT Framework

The paper introduces PSN-IRT, a framework based on Item Response Theory (IRT), for a deep analysis of LLM benchmark quality. More specifically, PSN-IRT is an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture, enabling the estimation of four key item parameters—difficulty, discriminability, guessing-rate, and feasibility—alongside latent model ability.

## Key Findings

The paper highlights inconsistencies across leaderboards and poor separability among top-performing models, suggesting that current evaluation frameworks may not accurately reflect true model abilities. 

The analysis of 11 LLM benchmarks comprising 41,871 items reveals significant and varied shortcomings in their measurement quality. Specifically, LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, and exhibit data contamination in numerous items, compromising their reliability.

## Practical Applications

The paper demonstrates that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7afe40d9-f935-47e9-8723-fea8d1a7d47a",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "02e8198e-6fec-444f-92d5-acee4e4a54c3",
  "toolUseResult": {
    "query": "PSN-IRT AAAI 2026 lost in benchmarks rethinking LLM benchmarking item response theory",
    "results": [
      {
        "tool_use_id": "srvtoolu_01LAP2oocuUzcrgbXhEYeAo4",
        "content": [
          {
            "title": "GitHub - Joe-Hall-Lee/PSN-IRT: [AAAI 2026 Oral] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory · GitHub",
            "url": "https://github.com/Joe-Hall-Lee/PSN-IRT"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://chatpaper.com/paper/139423"
          },
          {
            "title": "Paper page - Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://huggingface.co/papers/2505.15055"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v2"
          },
          {
            "title": "[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/abs/2505.15055"
          },
          {
            "title": "[Literature Review] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://www.themoonlight.io/en/review/lost-in-benchmarks-rethinking-large-language-model-benchmarking-with-item-response-theory"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory | Proceedings of the AAAI Conference on Artificial Intelligence",
            "url": "https://ojs.aaai.org/index.php/AAAI/article/view/40814"
          },
          {
            "title": "(PDF) Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://www.researchgate.net/publication/391954139_Lost_in_Benchmarks_Rethinking_Large_Language_Model_Benchmarking_with_Item_Response_Theory"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with",
            "url": "https://arxiv.org/pdf/2505.15055"
          }
        ]
      },
      "I found information about this paper. Here's what I found:\n\n## Overview\n\nThe paper titled \"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory\" was selected as [AAAI 2026 Oral].\n\n## The PSN-IRT Framework\n\nThe paper introduces PSN-IRT, a framework based on Item Response Theory (IRT), for a deep analysis of LLM benchmark quality. More specifically, PSN-IRT is an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture, enabling the estimation of four key item parameters—difficulty, discriminability, guessing-rate, and feasibility—alongside latent model ability.\n\n## Key Findings\n\nThe paper highlights inconsistencies across leaderboards and poor separability among top-performing models, suggesting that current evaluation frameworks may not accurately reflect true model abilities. \n\nThe analysis of 11 LLM benchmarks comprising 41,871 items reveals significant and varied shortcomings in their measurement quality. Specifically, LLM benchmarks suffer from widespread saturation and insufficient difficulty ceilings, and exhibit data contamination in numerous items, compromising their reliability.\n\n## Practical Applications\n\nThe paper demonstrates that leveraging PSN-IRT is able to construct smaller benchmarks while maintaining stronger alignment with human preference."
    ],
    "durationSeconds": 6.294891392000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7afe40d9-f935-47e9-8723-fea8d1a7d47a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 17 · 2026-05-28T14:15:30.290Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01U5t9NZjtqCkFTjbetsZUBC`</summary>

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
  "parentUuid": "02e8198e-6fec-444f-92d5-acee4e4a54c3",
  "isSidechain": false,
  "requestId": "req_011CbV7CNdc7zfrscjbjRazT",
  "type": "assistant",
  "uuid": "05b57606-2f03-4e27-ab7e-8a7752f9e558",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01MzbupLenL9S9k8ZQCdt69r",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 966,
      "cache_read_input_tokens": 28914,
      "output_tokens": 72,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 966,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 72,
          "cache_read_input_tokens": 28914,
          "cache_creation_input_tokens": 966,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 966
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

_source line 18 · 2026-05-28T14:15:38.576Z_

<details><summary>↩ Tool result · `toolu_01U5t9NZjtqCkFTjbetsZUBC`</summary>

```text
Web search results for query: "Growing Pains extensible LLM benchmarking fixed parameter calibration IRT 2026"

Links: [{"title":"Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/html/2604.12843"},{"title":"[2604.12843] Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration","url":"https://arxiv.org/abs/2604.12843"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"Agent psychometrics: Task-level performance prediction in agentic coding benchmarks","url":"https://arxiv.org/pdf/2604.00594"},{"title":"Preprint. Accepted at the ICLR 2026 LIT Workshop","url":"https://arxiv.org/pdf/2602.09924"},{"title":"LLM Evaluation and Benchmarking 2026 | Zylos Research","url":"https://zylos.ai/research/2026-01-16-llm-evaluation-benchmarking"}]

I found the research paper! Here's what I discovered:

## Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration

The rapid release of both language models and benchmarks makes it increasingly costly to evaluate every model on every dataset. In practice, models are often evaluated on different samples, making scores difficult to compare across studies.

The framework is based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.

### Key Features:

The approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.

### Use Cases:

For new-model evaluation, they test only the anchor questions and use the calibrated IRT model to infer performance over the larger historical pool, reducing the amount of inference required. For new-dataset integration, they calibrate the dataset into the existing evaluation suite and then use already-estimated model scores to estimate how models would perform on the new items, avoiding expensive model runs.

### Experimental Results:

The approach was evaluated on two large-scale benchmark suites: the Open LLM Leaderboard (6 datasets, 395 models) and MMLU (57 subject subsets, 428 models). The framework predicts full-evaluation performance within 2–3 percentage points using only anchor questions, with ranking preservation above 0.9.

The paper is available on arXiv (2604.12843) and was published in April 2026. Code is available at https://github.com/eliyahabba/growing-pains/.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "05b57606-2f03-4e27-ab7e-8a7752f9e558",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "c4a541b9-d022-4ae8-b973-6d03d807aa46",
  "toolUseResult": {
    "query": "Growing Pains extensible LLM benchmarking fixed parameter calibration IRT 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Sa8bT18F3SUr2GxHsEJsqp",
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
      "I found the research paper! Here's what I discovered:\n\n## Growing Pains: Extensible and Efficient LLM Benchmarking Via Fixed Parameter Calibration\n\nThe rapid release of both language models and benchmarks makes it increasingly costly to evaluate every model on every dataset. In practice, models are often evaluated on different samples, making scores difficult to compare across studies.\n\nThe framework is based on multidimensional Item Response Theory (IRT) that uses anchor items to calibrate new benchmarks to the evaluation suite while holding previously calibrated item parameters fixed.\n\n### Key Features:\n\nThe approach supports a realistic evaluation setting in which datasets are introduced over time and models are evaluated only on the datasets available at the time of evaluation, while a fixed anchor set for each dataset is used so that results from different evaluation periods can be compared directly.\n\n### Use Cases:\n\nFor new-model evaluation, they test only the anchor questions and use the calibrated IRT model to infer performance over the larger historical pool, reducing the amount of inference required. For new-dataset integration, they calibrate the dataset into the existing evaluation suite and then use already-estimated model scores to estimate how models would perform on the new items, avoiding expensive model runs.\n\n### Experimental Results:\n\nThe approach was evaluated on two large-scale benchmark suites: the Open LLM Leaderboard (6 datasets, 395 models) and MMLU (57 subject subsets, 428 models). The framework predicts full-evaluation performance within 2–3 percentage points using only anchor questions, with ranking preservation above 0.9.\n\nThe paper is available on arXiv (2604.12843) and was published in April 2026. Code is available at https://github.com/eliyahabba/growing-pains/."
    ],
    "durationSeconds": 8.279824079000003,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "05b57606-2f03-4e27-ab7e-8a7752f9e558",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 19 · 2026-05-28T14:15:41.917Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_016BPAHgkHYFmimemFpPbvvv`</summary>

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
  "parentUuid": "c4a541b9-d022-4ae8-b973-6d03d807aa46",
  "isSidechain": false,
  "requestId": "req_011CbV7DAoV5PCmyNW3H9X4H",
  "type": "assistant",
  "uuid": "fb9a8a71-32a1-4788-9a5f-ffa01b362150",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017yfy1DnebpvZ7VsQ45dZr1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 840,
      "cache_read_input_tokens": 29880,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 840,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 29880,
          "cache_creation_input_tokens": 840,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 840
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

_source line 20 · 2026-05-28T14:15:48.360Z_

<details><summary>↩ Tool result · `toolu_016BPAHgkHYFmimemFpPbvvv`</summary>

```text
Web search results for query: "JECS joint envelope conformal selection decontamination LLM benchmark 2026"

Links: [{"title":"[2605.21543] Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/abs/2605.21543"},{"title":"Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/html/2605.21543"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"},{"title":"PASC: Pipeline-Aware Conformal Prediction with Joint Coverage Guarantees for Multi-Stage NLP and LLM Pipelines","url":"https://arxiv.org/html/2605.18812"},{"title":"An Expert-grounded benchmark of General Purpose LLMs in LCA","url":"https://arxiv.org/pdf/2510.19886"}]

Based on the search results, here's what I found about JECS:

Joint Envelope Conformal Selection (JECS) is a conformal procedure that formalizes multi-model benchmark decontamination as a joint selection problem and enables global contamination rate (GCR) control under stated assumptions.

The work addresses benchmark data contamination, which has become a central challenge in LLM evaluation, as when evaluation examples appear in the training data of one or more audited models, reported performance can be inflated and cross-model comparisons become unreliable.

JECS works by computing per-model conformal p-values, aggregating them by the per-item maximum, reconstructing a conservative envelope of the max-p null distribution from right-tail observations above a data-driven threshold, and then applying the adaptive Benjamini-Hochberg procedure to the envelope-rescaled values to select a benchmark with provable GCR control.

The research appears to be very recent, published on arXiv (paper 2605.21543) approximately one week ago.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "fb9a8a71-32a1-4788-9a5f-ffa01b362150",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "5eebf94e-6b3d-413d-8593-9fb75d40fd25",
  "toolUseResult": {
    "query": "JECS joint envelope conformal selection decontamination LLM benchmark 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DeJ32RmDNdE9u51hFoudjv",
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
      "Based on the search results, here's what I found about JECS:\n\nJoint Envelope Conformal Selection (JECS) is a conformal procedure that formalizes multi-model benchmark decontamination as a joint selection problem and enables global contamination rate (GCR) control under stated assumptions.\n\nThe work addresses benchmark data contamination, which has become a central challenge in LLM evaluation, as when evaluation examples appear in the training data of one or more audited models, reported performance can be inflated and cross-model comparisons become unreliable.\n\nJECS works by computing per-model conformal p-values, aggregating them by the per-item maximum, reconstructing a conservative envelope of the max-p null distribution from right-tail observations above a data-driven threshold, and then applying the adaptive Benjamini-Hochberg procedure to the envelope-rescaled values to select a benchmark with provable GCR control.\n\nThe research appears to be very recent, published on arXiv (paper 2605.21543) approximately one week ago."
    ],
    "durationSeconds": 6.437875138999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "fb9a8a71-32a1-4788-9a5f-ffa01b362150",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
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
  "lastPrompt": "# CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  ## Core Problem  No existing framework can determine whether a model fails adversarial…",
  "leafUuid": "5eebf94e-6b3d-413d-8593-9fb75d40fd25",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Runtime record

_source line 22_

```json
{
  "type": "ai-title",
  "aiTitle": "Develop CRADE contamination-ability IRT framework",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Tool call

_source line 23 · 2026-05-28T14:15:52.327Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_018hhHCZ3gKbsJeAF4iP9NCy`</summary>

```json
{
  "query": "Wang Li Ko Zhang \"fragility of benchmark contamination detection\" reasoning models ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5eebf94e-6b3d-413d-8593-9fb75d40fd25",
  "isSidechain": false,
  "requestId": "req_011CbV7DsGpVcGie1fhGgymd",
  "type": "assistant",
  "uuid": "7bab94f8-3b01-448a-b92d-45d956b31018",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01PJHTJ4J2RYFL8xs516gDEs",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 584,
      "cache_read_input_tokens": 30720,
      "output_tokens": 73,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 584,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 73,
          "cache_read_input_tokens": 30720,
          "cache_creation_input_tokens": 584,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 584
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

_source line 24 · 2026-05-28T14:15:58.542Z_

<details><summary>↩ Tool result · `toolu_018hhHCZ3gKbsJeAF4iP9NCy`</summary>

```text
Web search results for query: "Wang Li Ko Zhang "fragility of benchmark contamination detection" reasoning models ICLR 2026"

Links: [{"title":"Carnegie Mellon at ICLR 2026 – Machine Learning Blog | ML@CMU | Carnegie Mellon University","url":"https://blog.ml.cmu.edu/2026/04/20/carnegie-mellon-at-iclr-2026/"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/pdf/2510.02386"},{"title":"[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/abs/2510.02386"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://arxiv.org/html/2510.02386v2"},{"title":"On The Fragility of Benchmark Contamination Detection in Reasoning Models","url":"https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"},{"title":"Published as a conference paper at ICLR 2026","url":"https://arxiv.org/pdf/2509.24210"},{"title":"Detecting Benchmark Contamination Through Watermarking","url":"https://arxiv.org/pdf/2502.17259"}]

Based on the search results, I found the paper you're looking for:

"On The Fragility of Benchmark Contamination Detection in Reasoning Models" is authored by Han Wang (University of Illinois Urbana-Champaign), Haoyu Li (University of Illinois Urbana-Champaign), Brian Ko (University of Washington), and Huan Zhang (CMU).

Note that the authors' names are slightly different from your query—the actual authors are Han Wang, Haoyu Li, Brian Ko, and Huan Zhang (not "Wang Li Ko Zhang"). 

The paper examines benchmark contamination, where evaluation benchmarks are incorporated into training data to yield inflated performance, and finds that evading contamination detections for large reasoning models (LRMs) is alarmingly easy. The research shows that while contamination during supervised fine-tuning (SFT) can be originally identified by contamination detection methods, even brief GRPO training can markedly conceal contamination signals that most detection methods rely on.

The paper appears to have been published at ICLR 2026 and is available on arXiv.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7bab94f8-3b01-448a-b92d-45d956b31018",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "1dd58b71-3627-4992-a722-f509bb7892b2",
  "toolUseResult": {
    "query": "Wang Li Ko Zhang \"fragility of benchmark contamination detection\" reasoning models ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_013uVPQ1DFRU1XANqYmirizd",
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
            "title": "[2510.02386] On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/abs/2510.02386"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://arxiv.org/html/2510.02386v2"
          },
          {
            "title": "On The Fragility of Benchmark Contamination Detection in Reasoning Models",
            "url": "https://www.researchgate.net/publication/396223620_On_The_Fragility_of_Benchmark_Contamination_Detection_in_Reasoning_Models"
          },
          {
            "title": "Published as a conference paper at ICLR 2026",
            "url": "https://arxiv.org/pdf/2509.24210"
          },
          {
            "title": "Detecting Benchmark Contamination Through Watermarking",
            "url": "https://arxiv.org/pdf/2502.17259"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\n\"On The Fragility of Benchmark Contamination Detection in Reasoning Models\" is authored by Han Wang (University of Illinois Urbana-Champaign), Haoyu Li (University of Illinois Urbana-Champaign), Brian Ko (University of Washington), and Huan Zhang (CMU).\n\nNote that the authors' names are slightly different from your query—the actual authors are Han Wang, Haoyu Li, Brian Ko, and Huan Zhang (not \"Wang Li Ko Zhang\"). \n\nThe paper examines benchmark contamination, where evaluation benchmarks are incorporated into training data to yield inflated performance, and finds that evading contamination detections for large reasoning models (LRMs) is alarmingly easy. The research shows that while contamination during supervised fine-tuning (SFT) can be originally identified by contamination detection methods, even brief GRPO training can markedly conceal contamination signals that most detection methods rely on.\n\nThe paper appears to have been published at ICLR 2026 and is available on arXiv."
    ],
    "durationSeconds": 6.209005087000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7bab94f8-3b01-448a-b92d-45d956b31018",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 25 · 2026-05-28T14:16:02.508Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_012FUy2KTgGYxA82fnKTeZAL`</summary>

```json
{
  "query": "RankLLM weighted ranking quantifying question difficulty ICLR 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "1dd58b71-3627-4992-a722-f509bb7892b2",
  "isSidechain": false,
  "requestId": "req_011CbV7Ecqw6a1BfCA6oXTP9",
  "type": "assistant",
  "uuid": "ac17d8ad-18ec-4e64-a1dc-8a6f66c13851",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wth9o9yDnFFMnGdgERKn2W",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 713,
      "cache_read_input_tokens": 31304,
      "output_tokens": 69,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 713,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 69,
          "cache_read_input_tokens": 31304,
          "cache_creation_input_tokens": 713,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 713
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

_source line 26 · 2026-05-28T14:16:07.375Z_

<details><summary>↩ Tool result · `toolu_012FUy2KTgGYxA82fnKTeZAL`</summary>

```text
Web search results for query: "RankLLM weighted ranking quantifying question difficulty ICLR 2026"

Links: [{"title":"RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty | OpenReview","url":"https://openreview.net/forum?id=jnX5GJIoYt"},{"title":"RANKLLM: WEIGHTED RANKING OF LLMS BY QUAN","url":"https://openreview.net/pdf/c22aab26d0cee50994697242fa86488f0f24707d.pdf"},{"title":"(PDF) RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://www.researchgate.net/publication/400812163_RankLLM_Weighted_Ranking_of_LLMs_by_Quantifying_Question_Difficulty"},{"title":"rankllm: weighted ranking of llms by quan","url":"https://arxiv.org/pdf/2602.12424"},{"title":"[2602.12424v1] RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://arxiv.org/abs/2602.12424v1"},{"title":"RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://arxiv.org/html/2602.12424v1"},{"title":"[2602.12424] RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty","url":"https://arxiv.org/abs/2602.12424"}]

Based on the search results, I found information about RankLLM from ICLR 2026:

## RankLLM: Overview

RankLLM is a paper published as a conference paper at ICLR 2026 by Ziqian Zhang, Xingjian Hu, Yue Huang, and colleagues from multiple institutions including Lehigh University, University of Notre Dame, and Duke University.

## Problem and Solution

Existing benchmarks fail to differentiate question difficulty, limiting their ability to effectively distinguish models' capabilities. To address this limitation, RankLLM is a novel framework designed to quantify both question difficulty and model competency.

## Core Mechanism

The core intuition of RankLLM is that a model earns a competency score when it correctly answers a question, while a question's difficulty score increases when it challenges a model. RankLLM's core mechanism facilitates bidirectional score propagation between models and questions.

## Results

Using this framework, the authors evaluate 30 models on 35,550 questions across multiple domains. RankLLM achieves 90% agreement with human judgments and consistently outperforms strong baselines such as IRT.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "ac17d8ad-18ec-4e64-a1dc-8a6f66c13851",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "cd02bc07-dcff-4165-871f-e988c3561e59",
  "toolUseResult": {
    "query": "RankLLM weighted ranking quantifying question difficulty ICLR 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_016Ym4pCNBhy1rxpVjkwVSDj",
        "content": [
          {
            "title": "RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty | OpenReview",
            "url": "https://openreview.net/forum?id=jnX5GJIoYt"
          },
          {
            "title": "RANKLLM: WEIGHTED RANKING OF LLMS BY QUAN",
            "url": "https://openreview.net/pdf/c22aab26d0cee50994697242fa86488f0f24707d.pdf"
          },
          {
            "title": "(PDF) RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty",
            "url": "https://www.researchgate.net/publication/400812163_RankLLM_Weighted_Ranking_of_LLMs_by_Quantifying_Question_Difficulty"
          },
          {
            "title": "rankllm: weighted ranking of llms by quan",
            "url": "https://arxiv.org/pdf/2602.12424"
          },
          {
            "title": "[2602.12424v1] RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty",
            "url": "https://arxiv.org/abs/2602.12424v1"
          },
          {
            "title": "RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty",
            "url": "https://arxiv.org/html/2602.12424v1"
          },
          {
            "title": "[2602.12424] RankLLM: Weighted Ranking of LLMs by Quantifying Question Difficulty",
            "url": "https://arxiv.org/abs/2602.12424"
          }
        ]
      },
      "Based on the search results, I found information about RankLLM from ICLR 2026:\n\n## RankLLM: Overview\n\nRankLLM is a paper published as a conference paper at ICLR 2026 by Ziqian Zhang, Xingjian Hu, Yue Huang, and colleagues from multiple institutions including Lehigh University, University of Notre Dame, and Duke University.\n\n## Problem and Solution\n\nExisting benchmarks fail to differentiate question difficulty, limiting their ability to effectively distinguish models' capabilities. To address this limitation, RankLLM is a novel framework designed to quantify both question difficulty and model competency.\n\n## Core Mechanism\n\nThe core intuition of RankLLM is that a model earns a competency score when it correctly answers a question, while a question's difficulty score increases when it challenges a model. RankLLM's core mechanism facilitates bidirectional score propagation between models and questions.\n\n## Results\n\nUsing this framework, the authors evaluate 30 models on 35,550 questions across multiple domains. RankLLM achieves 90% agreement with human judgments and consistently outperforms strong baselines such as IRT."
    ],
    "durationSeconds": 4.860310898999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "ac17d8ad-18ec-4e64-a1dc-8a6f66c13851",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 27 · 2026-05-28T14:16:10.574Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014uME8KTTM3SwBL1RghYFyu`</summary>

```json
{
  "query": "\"gated IRT\" OR \"contamination ability decomposition\" OR \"IRT contamination correction\" LLM 2025 2026 arxiv"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cd02bc07-dcff-4165-871f-e988c3561e59",
  "isSidechain": false,
  "requestId": "req_011CbV7FGhFPVWxjvQPVmcio",
  "type": "assistant",
  "uuid": "859f3b3b-46d5-455f-a544-c16c3c22872f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01WhrmeXBAjHfvmd6myjD2pA",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 768,
      "cache_read_input_tokens": 32017,
      "output_tokens": 85,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 768,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 85,
          "cache_read_input_tokens": 32017,
          "cache_creation_input_tokens": 768,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 768
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

_source line 28 · 2026-05-28T14:16:19.284Z_

<details><summary>↩ Tool result · `toolu_014uME8KTTM3SwBL1RghYFyu`</summary>

```text
Web search results for query: ""gated IRT" OR "contamination ability decomposition" OR "IRT contamination correction" LLM 2025 2026 arxiv"

Links: [{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"},{"title":"Detecting Data Contamination in LLMs via In-Context Learning","url":"https://arxiv.org/pdf/2510.27055"},{"title":"Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors","url":"https://arxiv.org/pdf/2506.10949"},{"title":"Time Travel in LLMs: Tracing Data Contamination in Large Language Models","url":"https://arxiv.org/pdf/2308.08493"},{"title":"Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination","url":"https://arxiv.org/pdf/2509.00072"},{"title":"[2605.21543] Provable Joint Decontamination for Benchmarking Multiple Large Language Models","url":"https://arxiv.org/abs/2605.21543"},{"title":"How Much Can We Forget about Data Contamination?","url":"https://arxiv.org/pdf/2410.03249"},{"title":"LLM Benchmark Datasets Should Be Contamination-Resistant","url":"https://arxiv.org/html/2605.19999v1"}]

I found several relevant papers on LLM contamination and related topics from arxiv in 2025-2026. Here are the key results:

## Direct Contamination-Related Papers:

1. **"When Benchmarks Leak: Inference-Time Decontamination for LLMs"** (arxiv:2601.19334)
   - Reports that over 15 LLMs exhibit inflated benchmark performance on six popular benchmarks, with estimated contamination rates ranging from 1% to 45%
   - Discusses inference-time decontamination methods that mitigate contamination effects during model inference rather than by filtering benchmark items

2. **"Detecting Data Contamination in LLMs via In-Context Learning"** (arxiv:2510.27055)
   - Validates contamination detection on diverse LLMs including Pythia, GPT-Neo, RWKV-4, OLMo, and Nemotron models

3. **"Provable Joint Decontamination for Benchmarking Multiple Large Language Models"** (arxiv:2605.21543)
   - Recent paper (May 2026) addressing contamination correction across multiple LLMs

4. **"Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination"** (arxiv:2509.00072)
   - Addresses how data contamination artificially inflates performance metrics, and notes that many previous works have demonstrated contamination reaching concerning proportions across evaluation benchmarks

5. **"How Much Can We Forget about Data Contamination?"** (arxiv:2410.03249)
   - Examines conditions under which contamination affects evaluation validity

6. **"LLM Benchmark Datasets Should Be Contamination-Resistant"** (arxiv:2605.19999)
   - Discusses how even gated benchmarks may be indirectly incorporated through data aggregation pipelines and how this shortens the effective lifespan of benchmarks as clean evaluation tools

The search also returned a paper on decomposition attacks ("Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors"), which involves a different type of attack mechanism but is related to LLM safety.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "859f3b3b-46d5-455f-a544-c16c3c22872f",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "8be20f53-3892-48b8-ab64-9c85fddbbc1f",
  "toolUseResult": {
    "query": "\"gated IRT\" OR \"contamination ability decomposition\" OR \"IRT contamination correction\" LLM 2025 2026 arxiv",
    "results": [
      {
        "tool_use_id": "srvtoolu_013F7bf2JsQyYGJAKU5nFwCA",
        "content": [
          {
            "title": "When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/pdf/2601.19334"
          },
          {
            "title": "Detecting Data Contamination in LLMs via In-Context Learning",
            "url": "https://arxiv.org/pdf/2510.27055"
          },
          {
            "title": "Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors",
            "url": "https://arxiv.org/pdf/2506.10949"
          },
          {
            "title": "Time Travel in LLMs: Tracing Data Contamination in Large Language Models",
            "url": "https://arxiv.org/pdf/2308.08493"
          },
          {
            "title": "Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination",
            "url": "https://arxiv.org/pdf/2509.00072"
          },
          {
            "title": "[2605.21543] Provable Joint Decontamination for Benchmarking Multiple Large Language Models",
            "url": "https://arxiv.org/abs/2605.21543"
          },
          {
            "title": "How Much Can We Forget about Data Contamination?",
            "url": "https://arxiv.org/pdf/2410.03249"
          },
          {
            "title": "LLM Benchmark Datasets Should Be Contamination-Resistant",
            "url": "https://arxiv.org/html/2605.19999v1"
          }
        ]
      },
      "I found several relevant papers on LLM contamination and related topics from arxiv in 2025-2026. Here are the key results:\n\n## Direct Contamination-Related Papers:\n\n1. **\"When Benchmarks Leak: Inference-Time Decontamination for LLMs\"** (arxiv:2601.19334)\n   - Reports that over 15 LLMs exhibit inflated benchmark performance on six popular benchmarks, with estimated contamination rates ranging from 1% to 45%\n   - Discusses inference-time decontamination methods that mitigate contamination effects during model inference rather than by filtering benchmark items\n\n2. **\"Detecting Data Contamination in LLMs via In-Context Learning\"** (arxiv:2510.27055)\n   - Validates contamination detection on diverse LLMs including Pythia, GPT-Neo, RWKV-4, OLMo, and Nemotron models\n\n3. **\"Provable Joint Decontamination for Benchmarking Multiple Large Language Models\"** (arxiv:2605.21543)\n   - Recent paper (May 2026) addressing contamination correction across multiple LLMs\n\n4. **\"Beyond Memorization: Reasoning-Driven Synthesis as a Mitigation Strategy Against Benchmark Contamination\"** (arxiv:2509.00072)\n   - Addresses how data contamination artificially inflates performance metrics, and notes that many previous works have demonstrated contamination reaching concerning proportions across evaluation benchmarks\n\n5. **\"How Much Can We Forget about Data Contamination?\"** (arxiv:2410.03249)\n   - Examines conditions under which contamination affects evaluation validity\n\n6. **\"LLM Benchmark Datasets Should Be Contamination-Resistant\"** (arxiv:2605.19999)\n   - Discusses how even gated benchmarks may be indirectly incorporated through data aggregation pipelines and how this shortens the effective lifespan of benchmarks as clean evaluation tools\n\nThe search also returned a paper on decomposition attacks (\"Monitoring Decomposition Attacks in LLMs with Lightweight Sequential Monitors\"), which involves a different type of attack mechanism but is related to LLM safety."
    ],
    "durationSeconds": 8.706259105000004,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "859f3b3b-46d5-455f-a544-c16c3c22872f",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 29 · 2026-05-28T14:16:19.289Z_

```json
{
  "parentUuid": "8be20f53-3892-48b8-ab64-9c85fddbbc1f",
  "isSidechain": false,
  "attachment": {
    "type": "task_reminder",
    "content": [],
    "itemCount": 0
  },
  "type": "attachment",
  "uuid": "cb7e4843-2bf7-4452-a2bc-b62cfd7d3888",
  "timestamp": "2026-05-28T14:16:19.289Z",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

---

### Tool call

_source line 30 · 2026-05-28T14:16:23.304Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01SMSt5SxxZo8NU8cXcj4Uni`</summary>

```json
{
  "query": "DCR quantifying data contamination evaluation EMNLP 2025 correction factor"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "cb7e4843-2bf7-4452-a2bc-b62cfd7d3888",
  "isSidechain": false,
  "requestId": "req_011CbV7G9UwetqyW8QL5Hxag",
  "type": "assistant",
  "uuid": "71192988-7941-457d-9035-64eac195974d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_016WYkqq4BXVHquQSB4epkGj",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 1088,
      "cache_read_input_tokens": 32785,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 1088,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 32785,
          "cache_creation_input_tokens": 1088,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 1088
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

_source line 31 · 2026-05-28T14:16:30.199Z_

<details><summary>↩ Tool result · `toolu_01SMSt5SxxZo8NU8cXcj4Uni`</summary>

```text
Web search results for query: "DCR quantifying data contamination evaluation EMNLP 2025 correction factor"

Links: [{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation - ACL Anthology","url":"https://aclanthology.org/2025.emnlp-main.1173/"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/pdf/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/html/2507.11405v2"},{"title":"[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://arxiv.org/abs/2507.11405"},{"title":"DCR: Quantifying Data Contamination in LLMs Evaluation","url":"https://aclanthology.org/2025.emnlp-main.1173.pdf"}]

Based on the search results, I found the paper you're looking for:

The DCR (Data Contamination Risk) framework is a lightweight, interpretable pipeline designed to detect and quantify benchmark data contamination (BDC) risk across four granular levels: semantic, informational, data, and label.

By synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance.

The framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, with accuracy adjusted using the DCR Factor achieving within 4% average error across the three benchmarks compared to the uncontaminated baseline.

The paper was published at EMNLP 2025 by Xu, Yan, Guan, Jin, Mei, Guo, and Kechadi. You can access the full paper at the ACL Anthology (https://aclanthology.org/2025.emnlp-main.1173/) or on arXiv (https://arxiv.org/abs/2507.11405).


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "71192988-7941-457d-9035-64eac195974d",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "6989028b-8db4-43fa-a857-db0b62278a12",
  "toolUseResult": {
    "query": "DCR quantifying data contamination evaluation EMNLP 2025 correction factor",
    "results": [
      {
        "tool_use_id": "srvtoolu_01GytXoJXZ87FaWjPJmHep7F",
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
            "url": "https://arxiv.org/html/2507.11405v2"
          },
          {
            "title": "[2507.11405] DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://arxiv.org/abs/2507.11405"
          },
          {
            "title": "DCR: Quantifying Data Contamination in LLMs Evaluation",
            "url": "https://aclanthology.org/2025.emnlp-main.1173.pdf"
          }
        ]
      },
      "Based on the search results, I found the paper you're looking for:\n\nThe DCR (Data Contamination Risk) framework is a lightweight, interpretable pipeline designed to detect and quantify benchmark data contamination (BDC) risk across four granular levels: semantic, informational, data, and label.\n\nBy synthesizing contamination scores via a fuzzy inference system, DCR produces a unified DCR Factor that adjusts raw accuracy to reflect contamination-aware performance.\n\nThe framework was validated on 9 LLMs (0.5B-72B) across sentiment analysis, fake news detection, and arithmetic reasoning tasks, with accuracy adjusted using the DCR Factor achieving within 4% average error across the three benchmarks compared to the uncontaminated baseline.\n\nThe paper was published at EMNLP 2025 by Xu, Yan, Guan, Jin, Mei, Guo, and Kechadi. You can access the full paper at the ACL Anthology (https://aclanthology.org/2025.emnlp-main.1173/) or on arXiv (https://arxiv.org/abs/2507.11405)."
    ],
    "durationSeconds": 6.890945309999996,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "71192988-7941-457d-9035-64eac195974d",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 32 · 2026-05-28T14:16:34.514Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01LmjiY8RszPsU167gAyfGmv`</summary>

```json
{
  "query": "Shu Henson Luecht \"deterministic gated\" IRT model test cheating item compromise Psychometrika 2013"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6989028b-8db4-43fa-a857-db0b62278a12",
  "isSidechain": false,
  "requestId": "req_011CbV7Gx7MxNjMQWpTzA7mh",
  "type": "assistant",
  "uuid": "f3d683a7-25d1-4eeb-87f4-e6f307621145",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_017uHpTH3KJvJthbW67CbpC1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 613,
      "cache_read_input_tokens": 33873,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 613,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 33873,
          "cache_creation_input_tokens": 613,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 613
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

_source line 33 · 2026-05-28T14:16:39.663Z_

<details><summary>↩ Tool result · `toolu_01LmjiY8RszPsU167gAyfGmv`</summary>

```text
Web search results for query: "Shu Henson Luecht "deterministic gated" IRT model test cheating item compromise Psychometrika 2013"

Links: [{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating Due to Item Compromise IRT","url":"https://www.ets.org/research/policy_research_reports/publications/article/2013/jqft.html"},{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Springer Nature Link","url":"https://link.springer.com/article/10.1007/s11336-012-9311-3"},{"title":"(PDF) Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise","url":"https://www.researchgate.net/publication/257678777_Using_Deterministic_Gated_Item_Response_Theory_Model_to_Detect_Test_Cheating_due_to_Item_Compromise"},{"title":"Two New Models for Item Preknowledge - Kylie Gorney, James A. Wollack, 2022","url":"https://journals.sagepub.com/doi/10.1177/01466216221108130"},{"title":"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Cambridge Core","url":"https://www.cambridge.org/core/journals/psychometrika/article/abs/using-deterministic-gated-item-response-theory-model-to-detect-test-cheating-due-to-item-compromise/34FE98C0FA7367881713D0019619E53E"},{"title":"Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/25106396/"},{"title":"Psychological Test and Assessment Modeling, Volume 64, 2022 (4), 425-444","url":"https://www.psychologie-aktuell.com/fileadmin/Redaktion/Journale/ptam_2022-4/PTAM_2022-4_3.pdf"}]

I found the paper you're looking for! The article "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise" was published by Shu, Henson, and Luecht in Psychometrika, Volume 78, Issue 3, pages 481-497 in July 2013.

The paper describes a Deterministic, Gated Item Response Theory Model (DGM) that identifies cheaters who obtain significant score gain on tests due to item exposure/compromise by conditioning on the item status (exposed or unexposed items). A "gated" function decomposes the observed examinees' performance into two distributions (the true ability distribution and the cheating distribution), and test cheaters with score gain due to item exposure are identified through the comparison of the two distributions.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "f3d683a7-25d1-4eeb-87f4-e6f307621145",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "b24f2587-3777-4d75-800f-36f622d24ceb",
  "toolUseResult": {
    "query": "Shu Henson Luecht \"deterministic gated\" IRT model test cheating item compromise Psychometrika 2013",
    "results": [
      {
        "tool_use_id": "srvtoolu_0139pgNL8vbPD8Q2g5d2YEUw",
        "content": [
          {
            "title": "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating Due to Item Compromise IRT",
            "url": "https://www.ets.org/research/policy_research_reports/publications/article/2013/jqft.html"
          },
          {
            "title": "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Springer Nature Link",
            "url": "https://link.springer.com/article/10.1007/s11336-012-9311-3"
          },
          {
            "title": "(PDF) Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise",
            "url": "https://www.researchgate.net/publication/257678777_Using_Deterministic_Gated_Item_Response_Theory_Model_to_Detect_Test_Cheating_due_to_Item_Compromise"
          },
          {
            "title": "Two New Models for Item Preknowledge - Kylie Gorney, James A. Wollack, 2022",
            "url": "https://journals.sagepub.com/doi/10.1177/01466216221108130"
          },
          {
            "title": "Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise | Psychometrika | Cambridge Core",
            "url": "https://www.cambridge.org/core/journals/psychometrika/article/abs/using-deterministic-gated-item-response-theory-model-to-detect-test-cheating-due-to-item-compromise/34FE98C0FA7367881713D0019619E53E"
          },
          {
            "title": "Using Deterministic, Gated Item Response Theory Model to detect test cheating due to item compromise - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/25106396/"
          },
          {
            "title": "Psychological Test and Assessment Modeling, Volume 64, 2022 (4), 425-444",
            "url": "https://www.psychologie-aktuell.com/fileadmin/Redaktion/Journale/ptam_2022-4/PTAM_2022-4_3.pdf"
          }
        ]
      },
      "I found the paper you're looking for! The article \"Using Deterministic, Gated Item Response Theory Model to Detect Test Cheating due to Item Compromise\" was published by Shu, Henson, and Luecht in Psychometrika, Volume 78, Issue 3, pages 481-497 in July 2013.\n\nThe paper describes a Deterministic, Gated Item Response Theory Model (DGM) that identifies cheaters who obtain significant score gain on tests due to item exposure/compromise by conditioning on the item status (exposed or unexposed items). A \"gated\" function decomposes the observed examinees' performance into two distributions (the true ability distribution and the cheating distribution), and test cheaters with score gain due to item exposure are identified through the comparison of the two distributions."
    ],
    "durationSeconds": 5.143866569000005,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "f3d683a7-25d1-4eeb-87f4-e6f307621145",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 34_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  ## Core Problem  No existing framework can determine whether a model fails adversarial…",
  "leafUuid": "b24f2587-3777-4d75-800f-36f622d24ceb",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Runtime record

_source line 35_

```json
{
  "type": "ai-title",
  "aiTitle": "Develop CRADE contamination-ability IRT framework",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Tool call

_source line 36 · 2026-05-28T14:16:42.725Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01YTT1jdKXd1HfKDQ9rJK61m`</summary>

```json
{
  "query": "RIDE difficulty evolving perturbation IRT mathematical reasoning 2025 adversarial"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "b24f2587-3777-4d75-800f-36f622d24ceb",
  "isSidechain": false,
  "requestId": "req_011CbV7HecRpQha9sbCiqDNf",
  "type": "assistant",
  "uuid": "16ad9fd5-ee10-42c6-aa27-d500ac34f022",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019FJR5YHmmou1TpUCSBGpu1",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 849,
      "cache_read_input_tokens": 34486,
      "output_tokens": 70,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 849,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 70,
          "cache_read_input_tokens": 34486,
          "cache_creation_input_tokens": 849,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 849
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

_source line 37 · 2026-05-28T14:16:49.617Z_

<details><summary>↩ Tool result · `toolu_01YTT1jdKXd1HfKDQ9rJK61m`</summary>

```text
Web search results for query: "RIDE difficulty evolving perturbation IRT mathematical reasoning 2025 adversarial"

Links: [{"title":"[2511.04120] RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/abs/2511.04120"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response ...","url":"https://arxiv.org/pdf/2511.04120"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning | OpenReview","url":"https://openreview.net/forum?id=PPkzchpdNK"},{"title":"RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ...","url":"https://openreview.net/pdf/a83cd39cfda0263faa17943c8f4832d28003298c.pdf"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/html/2511.04120"},{"title":"RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ITEM ...","url":"https://openreview.net/pdf/d5ed0f963c21d7ed1a8a3c452c9d81b161061351.pdf"}]

Based on the search results, here's what I found about RIDE:

## RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning

RIDE is a novel adversarial question-rewriting framework that leverages Item Response Theory (IRT) to rigorously measure question difficulty and to generate intrinsically more challenging, well-posed variations of mathematical problems.

### Background

Large language models (LLMs) achieve high performance on mathematical reasoning, but these results can be inflated by training data leakage or superficial pattern matching rather than genuine reasoning. To this end, an adversarial perturbation-based evaluation is needed to measure true mathematical reasoning ability.

### Problem With Previous Approaches

Rule-based approaches may render the rewritten questions ill-posed and unsolvable, thereby undermining their validity as reliable benchmarks. Moreover, previous work has focused mainly on low-difficulty datasets, with limited attempts at more challenging data.

### Methodology

The framework employs 35 LLMs to simulate students and build a difficulty ranker from their responses. This ranker provides a reward signal during reinforcement learning and guides a question-rewriting model to reformulate existing questions across difficulty levels.

The research appears to have been published in 2025 and presented at academic venues like OpenReview.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "16ad9fd5-ee10-42c6-aa27-d500ac34f022",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "ae2f43f0-354c-41ff-b20d-e2dba163cf1a",
  "toolUseResult": {
    "query": "RIDE difficulty evolving perturbation IRT mathematical reasoning 2025 adversarial",
    "results": [
      {
        "tool_use_id": "srvtoolu_01JksYWvQoJ1zaZK93ZpDi8R",
        "content": [
          {
            "title": "[2511.04120] RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2511.04120"
          },
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response ...",
            "url": "https://arxiv.org/pdf/2511.04120"
          },
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning | OpenReview",
            "url": "https://openreview.net/forum?id=PPkzchpdNK"
          },
          {
            "title": "RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ...",
            "url": "https://openreview.net/pdf/a83cd39cfda0263faa17943c8f4832d28003298c.pdf"
          },
          {
            "title": "RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning",
            "url": "https://arxiv.org/html/2511.04120"
          },
          {
            "title": "RIDE: DIFFICULTY EVOLVING PERTURBATION WITH ITEM ...",
            "url": "https://openreview.net/pdf/d5ed0f963c21d7ed1a8a3c452c9d81b161061351.pdf"
          }
        ]
      },
      "Based on the search results, here's what I found about RIDE:\n\n## RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning\n\nRIDE is a novel adversarial question-rewriting framework that leverages Item Response Theory (IRT) to rigorously measure question difficulty and to generate intrinsically more challenging, well-posed variations of mathematical problems.\n\n### Background\n\nLarge language models (LLMs) achieve high performance on mathematical reasoning, but these results can be inflated by training data leakage or superficial pattern matching rather than genuine reasoning. To this end, an adversarial perturbation-based evaluation is needed to measure true mathematical reasoning ability.\n\n### Problem With Previous Approaches\n\nRule-based approaches may render the rewritten questions ill-posed and unsolvable, thereby undermining their validity as reliable benchmarks. Moreover, previous work has focused mainly on low-difficulty datasets, with limited attempts at more challenging data.\n\n### Methodology\n\nThe framework employs 35 LLMs to simulate students and build a difficulty ranker from their responses. This ranker provides a reward signal during reinforcement learning and guides a question-rewriting model to reformulate existing questions across difficulty levels.\n\nThe research appears to have been published in 2025 and presented at academic venues like OpenReview."
    ],
    "durationSeconds": 6.88432693499999,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "16ad9fd5-ee10-42c6-aa27-d500ac34f022",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 38 · 2026-05-28T14:16:52.206Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01WLEAUvrvrFH4HZreRavuMe`</summary>

```json
{
  "query": "\"inference-time decontamination\" OR \"benchmark contamination correction\" LLM measurement theory latent variable 2025 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ae2f43f0-354c-41ff-b20d-e2dba163cf1a",
  "isSidechain": false,
  "requestId": "req_011CbV7JPBGKfzwMmwY3ZTs2",
  "type": "assistant",
  "uuid": "7a6faa51-a4cb-47de-83cd-9404de11ad93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01NErfChuVeUVaYQ8fmKoiyR",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 714,
      "cache_read_input_tokens": 35335,
      "output_tokens": 81,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 714,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 81,
          "cache_read_input_tokens": 35335,
          "cache_creation_input_tokens": 714,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 714
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

_source line 39 · 2026-05-28T14:16:58.315Z_

<details><summary>↩ Tool result · `toolu_01WLEAUvrvrFH4HZreRavuMe`</summary>

```text
Web search results for query: ""inference-time decontamination" OR "benchmark contamination correction" LLM measurement theory latent variable 2025 2026"

Links: [{"title":"[2601.19334] When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/abs/2601.19334"},{"title":"[2601.19334v1] When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/abs/2601.19334v1"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/pdf/2601.19334"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large   Language Model Evaluation","url":"https://arxiv.org/pdf/2406.13990"},{"title":"When Benchmarks Leak: Inference-Time Decontamination for LLMs","url":"https://arxiv.org/html/2601.19334v1"},{"title":"Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation","url":"https://arxiv.org/html/2406.13990v1"},{"title":"GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub","url":"https://github.com/lyy1994/awesome-data-contamination"}]

I found relevant results on inference-time decontamination for LLMs. Here's what the search revealed:

## Key Papers

**Recent Work (2026):**
DeconIEP is a decontamination framework that operates entirely during evaluation by applying small, bounded perturbations in the input embedding space, guided by a relatively less-contaminated reference model to learn an instance-adaptive perturbation generator. Across multiple open-weight LLMs and benchmarks, DeconIEP achieves strong decontamination effectiveness while incurring only minimal degradation in benign utility.

**Earlier Work (2024):**
Inference-Time Decontamination (ITD) addresses benchmark leakage by detecting and rewriting leaked samples without altering their difficulties.

## Problem Context

The reliability of benchmark-based evaluation is increasingly threatened by test set contamination, where test samples or their close variants leak into training data and artificially inflate reported performance. Benchmark-centric evaluation is vulnerable to data contamination, where test items (or closely related variants) appear in training data thereby violating the train–test separation and inflating reported performance.

The search results show active research in this area with both empirical approaches (perturbation-based) and alternative methods like neuron patching and architectural modifications being explored.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "7a6faa51-a4cb-47de-83cd-9404de11ad93",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "2e66cb37-b832-4dc5-952a-643c0f117091",
  "toolUseResult": {
    "query": "\"inference-time decontamination\" OR \"benchmark contamination correction\" LLM measurement theory latent variable 2025 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_017H4pGcQzNTsG8vJzp3RBeV",
        "content": [
          {
            "title": "[2601.19334] When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/abs/2601.19334"
          },
          {
            "title": "[2601.19334v1] When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/abs/2601.19334v1"
          },
          {
            "title": "When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/pdf/2601.19334"
          },
          {
            "title": "Inference-Time Decontamination: Reusing Leaked Benchmarks for Large   Language Model Evaluation",
            "url": "https://arxiv.org/pdf/2406.13990"
          },
          {
            "title": "When Benchmarks Leak: Inference-Time Decontamination for LLMs",
            "url": "https://arxiv.org/html/2601.19334v1"
          },
          {
            "title": "Inference-Time Decontamination: Reusing Leaked Benchmarks for Large Language Model Evaluation",
            "url": "https://arxiv.org/html/2406.13990v1"
          },
          {
            "title": "GitHub - lyy1994/awesome-data-contamination: The Paper List on Data Contamination for Large Language Models Evaluation. · GitHub",
            "url": "https://github.com/lyy1994/awesome-data-contamination"
          }
        ]
      },
      "I found relevant results on inference-time decontamination for LLMs. Here's what the search revealed:\n\n## Key Papers\n\n**Recent Work (2026):**\nDeconIEP is a decontamination framework that operates entirely during evaluation by applying small, bounded perturbations in the input embedding space, guided by a relatively less-contaminated reference model to learn an instance-adaptive perturbation generator. Across multiple open-weight LLMs and benchmarks, DeconIEP achieves strong decontamination effectiveness while incurring only minimal degradation in benign utility.\n\n**Earlier Work (2024):**\nInference-Time Decontamination (ITD) addresses benchmark leakage by detecting and rewriting leaked samples without altering their difficulties.\n\n## Problem Context\n\nThe reliability of benchmark-based evaluation is increasingly threatened by test set contamination, where test samples or their close variants leak into training data and artificially inflate reported performance. Benchmark-centric evaluation is vulnerable to data contamination, where test items (or closely related variants) appear in training data thereby violating the train–test separation and inflating reported performance.\n\nThe search results show active research in this area with both empirical approaches (perturbation-based) and alternative methods like neuron patching and architectural modifications being explored."
    ],
    "durationSeconds": 6.103725649,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "7a6faa51-a4cb-47de-83cd-9404de11ad93",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 40 · 2026-05-28T14:17:01.827Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_019fSWDHXT2U1jrrfoNJbg6P`</summary>

```json
{
  "query": "Gorney Wollack \"item preknowledge\" IRT models 2022 cheating detection psychometrics"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "2e66cb37-b832-4dc5-952a-643c0f117091",
  "isSidechain": false,
  "requestId": "req_011CbV7K2LQwc7MT8zNqL2Ki",
  "type": "assistant",
  "uuid": "b1f7f99a-420e-44c0-af07-748b2d119e9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CD7btzWpi4Wh5xfW8B6Z4g",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 774,
      "cache_read_input_tokens": 36049,
      "output_tokens": 77,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 774,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 77,
          "cache_read_input_tokens": 36049,
          "cache_creation_input_tokens": 774,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 774
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

_source line 41 · 2026-05-28T14:17:08.209Z_

<details><summary>↩ Tool result · `toolu_019fSWDHXT2U1jrrfoNJbg6P`</summary>

```text
Web search results for query: "Gorney Wollack "item preknowledge" IRT models 2022 cheating detection psychometrics"

Links: [{"title":"Two New Models for Item Preknowledge - Kylie Gorney, James A. Wollack, 2022","url":"https://journals.sagepub.com/doi/10.1177/01466216221108130"},{"title":"(PDF) Investigation of Preknowledge Cheating via Joint Hierarchical Modeling Patterns of Response Accuracy and Response Time","url":"https://www.researchgate.net/publication/386182764_Investigation_of_Preknowledge_Cheating_via_Joint_Hierarchical_Modeling_Patterns_of_Response_Accuracy_and_Response_Time"},{"title":"Using Response Times in Answer Similarity Analysis - Kylie Gorney, James A. Wollack, 2025","url":"https://journals.sagepub.com/doi/10.3102/10769986241248770"},{"title":"Using Item Scores and Distractors to Detect Item Compromise and Preknowledge - Kylie Gorney, James A. Wollack, Sandip Sinharay, Carol Eckerly, 2023","url":"https://journals.sagepub.com/doi/10.3102/10769986231159923"},{"title":"Two New Models for Item Preknowledge - PubMed","url":"https://pubmed.ncbi.nlm.nih.gov/35991826/"},{"title":"Generating Models for Item Preknowledge - Gorney - 2022 - Journal of Educational Measurement - Wiley Online Library","url":"https://onlinelibrary.wiley.com/doi/10.1111/jedm.12309"},{"title":"Two New Models for Item Preknowledge - PMC - NIH","url":"https://pmc.ncbi.nlm.nih.gov/articles/PMC9382093/"},{"title":"Generating Models for Item Preknowledge | Request PDF","url":"https://www.researchgate.net/publication/359136362_Generating_Models_for_Item_Preknowledge"}]

I found relevant research on this topic. Here are the key findings:

## Gorney and Wollack's 2022 Research on Item Preknowledge

In 2022, Gorney and Wollack published "Two new models for item preknowledge" in Applied Psychological Measurement, 46(6), 447–461.

To evaluate preknowledge detection methods, researchers often conduct simulation studies in which they use models to generate the data. Gorney and Wollack concluded that the most promising response accuracy and response time models allow the impact of preknowledge to vary across persons or items.

The research examined real-world data, with Gorney and Wollack examining three real data sets with known cases of preknowledge. The models generally assume low ability examinees benefit more from preknowledge than high ability examinees, and difficult items are affected more than easy items—assumptions that were found to hold in their analysis of the three data sets.

Additionally, the authors have published related work on this topic, including a 2022 article on "Generating models for item preknowledge" in the Journal of Educational Measurement, 59(1), 22–42.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "b1f7f99a-420e-44c0-af07-748b2d119e9b",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "f9d54b58-6ad0-4f1f-b638-c080a62267bb",
  "toolUseResult": {
    "query": "Gorney Wollack \"item preknowledge\" IRT models 2022 cheating detection psychometrics",
    "results": [
      {
        "tool_use_id": "srvtoolu_01DV97C4uu43f45j3pjayR7Y",
        "content": [
          {
            "title": "Two New Models for Item Preknowledge - Kylie Gorney, James A. Wollack, 2022",
            "url": "https://journals.sagepub.com/doi/10.1177/01466216221108130"
          },
          {
            "title": "(PDF) Investigation of Preknowledge Cheating via Joint Hierarchical Modeling Patterns of Response Accuracy and Response Time",
            "url": "https://www.researchgate.net/publication/386182764_Investigation_of_Preknowledge_Cheating_via_Joint_Hierarchical_Modeling_Patterns_of_Response_Accuracy_and_Response_Time"
          },
          {
            "title": "Using Response Times in Answer Similarity Analysis - Kylie Gorney, James A. Wollack, 2025",
            "url": "https://journals.sagepub.com/doi/10.3102/10769986241248770"
          },
          {
            "title": "Using Item Scores and Distractors to Detect Item Compromise and Preknowledge - Kylie Gorney, James A. Wollack, Sandip Sinharay, Carol Eckerly, 2023",
            "url": "https://journals.sagepub.com/doi/10.3102/10769986231159923"
          },
          {
            "title": "Two New Models for Item Preknowledge - PubMed",
            "url": "https://pubmed.ncbi.nlm.nih.gov/35991826/"
          },
          {
            "title": "Generating Models for Item Preknowledge - Gorney - 2022 - Journal of Educational Measurement - Wiley Online Library",
            "url": "https://onlinelibrary.wiley.com/doi/10.1111/jedm.12309"
          },
          {
            "title": "Two New Models for Item Preknowledge - PMC - NIH",
            "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9382093/"
          },
          {
            "title": "Generating Models for Item Preknowledge | Request PDF",
            "url": "https://www.researchgate.net/publication/359136362_Generating_Models_for_Item_Preknowledge"
          }
        ]
      },
      "I found relevant research on this topic. Here are the key findings:\n\n## Gorney and Wollack's 2022 Research on Item Preknowledge\n\nIn 2022, Gorney and Wollack published \"Two new models for item preknowledge\" in Applied Psychological Measurement, 46(6), 447–461.\n\nTo evaluate preknowledge detection methods, researchers often conduct simulation studies in which they use models to generate the data. Gorney and Wollack concluded that the most promising response accuracy and response time models allow the impact of preknowledge to vary across persons or items.\n\nThe research examined real-world data, with Gorney and Wollack examining three real data sets with known cases of preknowledge. The models generally assume low ability examinees benefit more from preknowledge than high ability examinees, and difficult items are affected more than easy items—assumptions that were found to hold in their analysis of the three data sets.\n\nAdditionally, the authors have published related work on this topic, including a 2022 article on \"Generating models for item preknowledge\" in the Journal of Educational Measurement, 59(1), 22–42."
    ],
    "durationSeconds": 6.378600183000002,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "b1f7f99a-420e-44c0-af07-748b2d119e9b",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 42 · 2026-05-28T14:17:12.227Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a good understanding of the landscape. Let me also check if there are any very recent works that might threaten the novelty claim - specifically, anything combining IRT with contamination correction in a joint model for LLMs.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f9d54b58-6ad0-4f1f-b638-c080a62267bb",
  "isSidechain": false,
  "requestId": "req_011CbV7KmeQPiH8J7R1n2EFT",
  "type": "assistant",
  "uuid": "e1363619-7144-4a8f-bc9a-0441efb5aa73",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115A6hJrEiumKrioLrmBcg6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 36823,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 36823,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
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

_source line 43 · 2026-05-28T14:17:12.564Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01HCqS3UdEkUtArwj7supK6B`</summary>

```json
{
  "query": "IRT psychometric contamination correction LLM ability estimation joint model paired items 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1363619-7144-4a8f-bc9a-0441efb5aa73",
  "isSidechain": false,
  "requestId": "req_011CbV7KmeQPiH8J7R1n2EFT",
  "type": "assistant",
  "uuid": "dd9a41e8-37c6-481b-9d6f-7f3455323874",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0115A6hJrEiumKrioLrmBcg6",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 895,
      "cache_read_input_tokens": 36823,
      "output_tokens": 134,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 895,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 134,
          "cache_read_input_tokens": 36823,
          "cache_creation_input_tokens": 895,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 895
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

_source line 44 · 2026-05-28T14:17:19.691Z_

<details><summary>↩ Tool result · `toolu_01HCqS3UdEkUtArwj7supK6B`</summary>

```text
Web search results for query: "IRT psychometric contamination correction LLM ability estimation joint model paired items 2026"

Links: [{"title":"Large language model psychometrics: A systematic review of evaluation, validation, and enhancement","url":"https://arxiv.org/html/2505.08245v2"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/html/2511.04689"},{"title":"JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory","url":"https://arxiv.org/pdf/2509.22888"},{"title":"Quantifying Data Contamination in Psychometric Evaluations of LLMs","url":"https://arxiv.org/pdf/2510.07175"}]

Based on the web search results, here are the most relevant findings related to your query:

## Key Findings:

**IRT-based LLM Evaluation:**
Item Response Theory (IRT) is a statistical approach in psychometrics that jointly estimates the latent ability of examinees and the properties (difficulty, discrimination) of test items. Recent approaches introduce IRT-based benchmarks that involve learning to estimate item difficulty and learning to generate novel items calibrated to specific difficulty levels.

**Joint Models and Paired Items:**
A natural approach would be to simulate interactions through a model's ability score and a question's difficulty score, as in traditional item response theory (IRT). One recent example is JE-IRT (Joint Embedding Item Response Theory), which provides accurate item-level predictions and scales to new models after learning question embeddings once.

**Contamination in Psychometric Evaluation:**
A framework quantifies data contamination across three aspects: item memorization, evaluation memorization, and target score matching. Average scores tend to mask meaningful model differences and are often affected by form-dependence, nonlinear scaling, equal weighting of uninformative items, and contamination sensitivity.

**Psychometric Validation:**
Many approaches often lack proper psychometric validation and emphasize predictive accuracy over model fit, making it difficult to ensure that the resulting ability estimates are valid, interpretable, and comparable across models.

The search results show active recent research (2025-2026) addressing contamination correction and improved ability estimation methods for LLMs using IRT frameworks.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "dd9a41e8-37c6-481b-9d6f-7f3455323874",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "618ff079-337e-4a74-a531-559e22ed29f2",
  "toolUseResult": {
    "query": "IRT psychometric contamination correction LLM ability estimation joint model paired items 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01ThZZ13AsgWahUVkcC548PV",
        "content": [
          {
            "title": "Large language model psychometrics: A systematic review of evaluation, validation, and enhancement",
            "url": "https://arxiv.org/html/2505.08245v2"
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
            "title": "JE-IRT: A Geometric Lens on LLM Abilities through Joint Embedding Item Response Theory",
            "url": "https://arxiv.org/pdf/2509.22888"
          },
          {
            "title": "Quantifying Data Contamination in Psychometric Evaluations of LLMs",
            "url": "https://arxiv.org/pdf/2510.07175"
          }
        ]
      },
      "Based on the web search results, here are the most relevant findings related to your query:\n\n## Key Findings:\n\n**IRT-based LLM Evaluation:**\nItem Response Theory (IRT) is a statistical approach in psychometrics that jointly estimates the latent ability of examinees and the properties (difficulty, discrimination) of test items. Recent approaches introduce IRT-based benchmarks that involve learning to estimate item difficulty and learning to generate novel items calibrated to specific difficulty levels.\n\n**Joint Models and Paired Items:**\nA natural approach would be to simulate interactions through a model's ability score and a question's difficulty score, as in traditional item response theory (IRT). One recent example is JE-IRT (Joint Embedding Item Response Theory), which provides accurate item-level predictions and scales to new models after learning question embeddings once.\n\n**Contamination in Psychometric Evaluation:**\nA framework quantifies data contamination across three aspects: item memorization, evaluation memorization, and target score matching. Average scores tend to mask meaningful model differences and are often affected by form-dependence, nonlinear scaling, equal weighting of uninformative items, and contamination sensitivity.\n\n**Psychometric Validation:**\nMany approaches often lack proper psychometric validation and emphasize predictive accuracy over model fit, making it difficult to ensure that the resulting ability estimates are valid, interpretable, and comparable across models.\n\nThe search results show active recent research (2025-2026) addressing contamination correction and improved ability estimation methods for LLMs using IRT frameworks."
    ],
    "durationSeconds": 7.116833243000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "dd9a41e8-37c6-481b-9d6f-7f3455323874",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 45 · 2026-05-28T14:17:22.950Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_014GvB5pd3Ly6xikvdtS8Gks`</summary>

```json
{
  "query": "MaSTer automated robustness evaluation mathematical reasoning adversarial rewrite pipeline 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "618ff079-337e-4a74-a531-559e22ed29f2",
  "isSidechain": false,
  "requestId": "req_011CbV7Lbk7y6ubAaWXTJ1NS",
  "type": "assistant",
  "uuid": "784cd896-ab10-43e2-a0c9-854eb0a5d454",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019zCKH46QF6oye4zem3nfoc",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 741,
      "cache_read_input_tokens": 37718,
      "output_tokens": 71,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 741,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 71,
          "cache_read_input_tokens": 37718,
          "cache_creation_input_tokens": 741,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 741
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

_source line 46 · 2026-05-28T14:17:30.218Z_

<details><summary>↩ Tool result · `toolu_014GvB5pd3Ly6xikvdtS8Gks`</summary>

```text
Web search results for query: "MaSTer automated robustness evaluation mathematical reasoning adversarial rewrite pipeline 2026"

Links: [{"title":"[2506.05038] Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/abs/2506.05038"},{"title":"Toward Automated Robustness Evaluation of Mathematical Reasoning","url":"https://arxiv.org/html/2506.05038v2"},{"title":"An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems","url":"https://arxiv.org/html/2508.08833"},{"title":"RIDE: Difficulty Evolving Perturbation with Item Response Theory for Mathematical Reasoning","url":"https://arxiv.org/pdf/2511.04120"},{"title":"MSCR: Exploring the Vulnerability of LLMs' Mathematical Reasoning Abilities Using Multi-Source Candidate Replacement","url":"https://arxiv.org/pdf/2511.08055"},{"title":"Automatic Robustness Stress Testing of LLMs as Mathematical Problem Solvers","url":"https://arxiv.org/pdf/2506.05038"},{"title":"Robust Reasoning Benchmark","url":"https://arxiv.org/html/2604.08571v2"}]

Based on the search results, I found detailed information about MaSTer:

MaSTer is the Math Stress Tester, an automated framework inspired by software stress testing. MaSTer generates adversarial variants via a multi-round rewrite-verify loop, ensuring semantic consistency while successfully inducing model failure.

The framework operates through an automated adversarial loop comprising a rewriter, a verifier, and the target LLM, where the rewriter rewrites mathematical problems into their variants while keeping the core meaning unchanged.

Experiments on GSM8K, MATH-500, and broader benchmarks demonstrate that the framework is effective in evaluating the robustness of LLMs. Additionally, the adversarial variants synthesized by MaSTer serve as high-quality training data, significantly enhancing model robustness through fine-tuning.

The research was published on arXiv on April 24, 2026, and addresses the problem that existing robustness evaluations predominantly rely on hand-crafted templates or limited perturbation rules, and consequently lack adaptability to probe latent vulnerabilities unique to specific models.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "784cd896-ab10-43e2-a0c9-854eb0a5d454",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "05eecc7d-6d30-4c4b-bd45-62e51aa97986",
  "toolUseResult": {
    "query": "MaSTer automated robustness evaluation mathematical reasoning adversarial rewrite pipeline 2026",
    "results": [
      {
        "tool_use_id": "srvtoolu_01Kd42PzGwGArZuGdkX4uu4g",
        "content": [
          {
            "title": "[2506.05038] Toward Automated Robustness Evaluation of Mathematical Reasoning",
            "url": "https://arxiv.org/abs/2506.05038"
          },
          {
            "title": "Toward Automated Robustness Evaluation of Mathematical Reasoning",
            "url": "https://arxiv.org/html/2506.05038v2"
          },
          {
            "title": "An Investigation of Robustness of LLMs in Mathematical Reasoning: Benchmarking with Mathematically-Equivalent Transformation of Advanced Mathematical Problems",
            "url": "https://arxiv.org/html/2508.08833"
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
            "title": "Robust Reasoning Benchmark",
            "url": "https://arxiv.org/html/2604.08571v2"
          }
        ]
      },
      "Based on the search results, I found detailed information about MaSTer:\n\nMaSTer is the Math Stress Tester, an automated framework inspired by software stress testing. MaSTer generates adversarial variants via a multi-round rewrite-verify loop, ensuring semantic consistency while successfully inducing model failure.\n\nThe framework operates through an automated adversarial loop comprising a rewriter, a verifier, and the target LLM, where the rewriter rewrites mathematical problems into their variants while keeping the core meaning unchanged.\n\nExperiments on GSM8K, MATH-500, and broader benchmarks demonstrate that the framework is effective in evaluating the robustness of LLMs. Additionally, the adversarial variants synthesized by MaSTer serve as high-quality training data, significantly enhancing model robustness through fine-tuning.\n\nThe research was published on arXiv on April 24, 2026, and addresses the problem that existing robustness evaluations predominantly rely on hand-crafted templates or limited perturbation rules, and consequently lack adaptability to probe latent vulnerabilities unique to specific models."
    ],
    "durationSeconds": 7.264272602000012,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "784cd896-ab10-43e2-a0c9-854eb0a5d454",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 47_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  ## Core Problem  No existing framework can determine whether a model fails adversarial…",
  "leafUuid": "05eecc7d-6d30-4c4b-bd45-62e51aa97986",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Runtime record

_source line 48_

```json
{
  "type": "ai-title",
  "aiTitle": "Develop CRADE contamination-ability IRT framework",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Tool call

_source line 49 · 2026-05-28T14:17:33.160Z_

<details open><summary>🔧 Tool call — WebSearch · `toolu_01Jg3pEpUsgnRGDBHf4cBGYu`</summary>

```json
{
  "query": "\"benchmark contamination\" \"item response theory\" \"ability estimation\" correction arxiv 2025 2026 latent variable decomposition"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "05eecc7d-6d30-4c4b-bd45-62e51aa97986",
  "isSidechain": false,
  "requestId": "req_011CbV7MNiKL9dRWvteVLU6R",
  "type": "assistant",
  "uuid": "3571a706-c549-45b3-a653-8095ba28bd6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01VT4mFQHefVZdWyM2KrpVwh",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 675,
      "cache_read_input_tokens": 38459,
      "output_tokens": 80,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 675,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 80,
          "cache_read_input_tokens": 38459,
          "cache_creation_input_tokens": 675,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 675
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

_source line 50 · 2026-05-28T14:17:40.287Z_

<details><summary>↩ Tool result · `toolu_01Jg3pEpUsgnRGDBHf4cBGYu`</summary>

```text
Web search results for query: ""benchmark contamination" "item response theory" "ability estimation" correction arxiv 2025 2026 latent variable decomposition"

Links: [{"title":"Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory","url":"https://arxiv.org/html/2603.02663"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/html/2505.15055v2"},{"title":"[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory","url":"https://arxiv.org/abs/2505.15055"},{"title":"Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks","url":"https://arxiv.org/pdf/2511.04689"},{"title":"Lost in Benchmarks? Rethinking Large Language Model Benchmarking with","url":"https://arxiv.org/pdf/2505.15055"},{"title":"Fantastic Bugs and Where to Find Them in AI Benchmarks","url":"https://arxiv.org/pdf/2511.16842"},{"title":"What Does Your Benchmark Really Measure? A Framework for Robust Inference of AI Capabilities","url":"https://arxiv.org/pdf/2509.19590"},{"title":"Robust Estimation of Item Parameters via Divergence Measures in Item   Response Theory","url":"https://arxiv.org/pdf/2502.10741"}]

I found several relevant papers from the 2025-2026 timeframe that discuss benchmark contamination, item response theory, and ability estimation. Here are the key findings:

## Main Results

LLM benchmarks exhibit data contamination in numerous items, compromising their reliability. The search results reveal multiple approaches addressing this issue:

1. **PSN-IRT Framework**: Pseudo-Siamese Network for Item Response Theory (PSN-IRT) is an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture and can be utilized for accurate and reliable estimations of item characteristics and model abilities.

2. **Multimodal IRT Application**: A recent paper compiles a benchmark contaminated with 50% low-quality questions to evaluate methods, demonstrating how contamination affects evaluation.

3. **Robust IRT Methods**: Recent work explores robust estimation of item parameters via divergence measures in item response theory.

4. **Latent Ability Estimation**: IRT provides item parameters such as difficulty, discrimination, and guessing, as well as latent ability estimates for models.

The papers (from arXiv 2505, 2509, 2511, and 2603 series from 2025-2026) collectively address how benchmark contamination affects ability estimation and propose various IRT-based corrections and validation approaches.


REMINDER: You MUST include the sources above in your response to the user using markdown hyperlinks.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "3571a706-c549-45b3-a653-8095ba28bd6a",
  "isSidechain": false,
  "promptId": "86c0b808-2337-4d0b-89ed-cb4711213963",
  "type": "user",
  "uuid": "c43d3c53-90f5-43e1-9734-2e55cccd5520",
  "toolUseResult": {
    "query": "\"benchmark contamination\" \"item response theory\" \"ability estimation\" correction arxiv 2025 2026 latent variable decomposition",
    "results": [
      {
        "tool_use_id": "srvtoolu_018noYiezRaoubUeekJf8xTa",
        "content": [
          {
            "title": "Evaluating Cross-Modal Reasoning Ability and Problem Characteristics with Multimodal Item Response Theory",
            "url": "https://arxiv.org/html/2603.02663"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/html/2505.15055v2"
          },
          {
            "title": "[2505.15055] Lost in Benchmarks? Rethinking Large Language Model Benchmarking with Item Response Theory",
            "url": "https://arxiv.org/abs/2505.15055"
          },
          {
            "title": "Adaptive Testing for LLM Evaluation: A Psychometric Alternative to Static Benchmarks",
            "url": "https://arxiv.org/pdf/2511.04689"
          },
          {
            "title": "Lost in Benchmarks? Rethinking Large Language Model Benchmarking with",
            "url": "https://arxiv.org/pdf/2505.15055"
          },
          {
            "title": "Fantastic Bugs and Where to Find Them in AI Benchmarks",
            "url": "https://arxiv.org/pdf/2511.16842"
          },
          {
            "title": "What Does Your Benchmark Really Measure? A Framework for Robust Inference of AI Capabilities",
            "url": "https://arxiv.org/pdf/2509.19590"
          },
          {
            "title": "Robust Estimation of Item Parameters via Divergence Measures in Item   Response Theory",
            "url": "https://arxiv.org/pdf/2502.10741"
          }
        ]
      },
      "I found several relevant papers from the 2025-2026 timeframe that discuss benchmark contamination, item response theory, and ability estimation. Here are the key findings:\n\n## Main Results\n\nLLM benchmarks exhibit data contamination in numerous items, compromising their reliability. The search results reveal multiple approaches addressing this issue:\n\n1. **PSN-IRT Framework**: Pseudo-Siamese Network for Item Response Theory (PSN-IRT) is an enhanced Item Response Theory framework that incorporates a rich set of item parameters within an IRT-grounded architecture and can be utilized for accurate and reliable estimations of item characteristics and model abilities.\n\n2. **Multimodal IRT Application**: A recent paper compiles a benchmark contaminated with 50% low-quality questions to evaluate methods, demonstrating how contamination affects evaluation.\n\n3. **Robust IRT Methods**: Recent work explores robust estimation of item parameters via divergence measures in item response theory.\n\n4. **Latent Ability Estimation**: IRT provides item parameters such as difficulty, discrimination, and guessing, as well as latent ability estimates for models.\n\nThe papers (from arXiv 2505, 2509, 2511, and 2603 series from 2025-2026) collectively address how benchmark contamination affects ability estimation and propose various IRT-based corrections and validation approaches."
    ],
    "durationSeconds": 7.122966518000001,
    "searchCount": 1
  },
  "sourceToolAssistantUUID": "3571a706-c549-45b3-a653-8095ba28bd6a",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 51 · 2026-05-28T14:18:33.284Z_

<details><summary>Logged reasoning block</summary>

```text
Now I have a comprehensive understanding of the research landscape. Let me synthesize my findings and provide my analysis as the 发掘 agent.

Key findings from my research:

1. **No existing work combines IRT-based contamination-ability decomposition with paired adversarial items for LLMs.** This confirms the proposal's novelty claim that the intersection is indeed unoccupied.

2. **PSN-IRT (AAAI 2026 Oral)** establishes IRT works for LLMs but explicitly leaves contamination correction as an open question.

3. **Growing Pains (arXiv April 2026)** validates two-stage fixed-parameter calibration for IRT-based LLM evaluation, directly supporting the technical feasibility of CRADE's architecture.
   
4. **Wang et al. (ICLR 2026)** demonstrates that likelihood-based detection approaches break down on reasoning models, which creates a real need for methods based on response patterns instead.

5. **DCR (EMNLP 2025)** and **JECS (arXiv May 2026)** both address contamination correction but lack the measurement-theoretic foundation or produce only binary classifications rather than continuous corrected scores.

6. **Gorney & Wollack (2022)** extended the psychometric test security literature with new models for item preknowledge, showing this field continues to evolve and remains relevant.

7. **RankLLM (ICLR 2026)** and **RIDE** offer difficulty-aware ranking and IRT-based reward signals respectively, but neither models contamination directly or jointly estimates across both dimensions.

8. **DeconIEP (2026)** takes a fundamentally different approach by operating in embedding space rather than analyzing response patterns.

Now looking at where this proposal stands, the combination of IRT, contamination modeling, and adversarial pairing appears to be genuinely novel—no existing work brings these three elements together. The analogy between test cheating and training data contamination is compelling, and the two-stage calibration approach using existing leaderboard data feels both practical and theoretically sound.

But I'm noticing the proposal might be underselling its core contribution. The real novelty isn't just applying DGM to LLMs—it's the identification strategy itself, using paired adversarial items to overcome DGM's fundamental requirement of knowing exposure status. That's actually a broader methodological advance for test security research, not merely an LLM application. The proposal touches on this but doesn't emphasize it enough as the primary innovation.

There's also a critical assumption worth scrutinizing: the claim that contamination and ability decompose cleanly through the gated IRT model depends on whether the performance gap between original and adversarial variants truly isolates contamination effects. But adversarial variants might be harder for reasons unrelated to removing contamination—they could test different reasoning skills or introduce confounding difficulty factors that muddy the signal.

I should also push back on the significance framing. The proposal needs to make a stronger case for why continuous corrected ability scores matter more than just binary contamination flags or item filtering. And there's a real concern with the RankLLM comparison: if RankLLM already achieves 90% human alignment without any contamination modeling, and CRADE-corrected rankings only marginally improve over that, the incremental value of decomposing contamination becomes harder to justify.

There's also a gap around Gorney & Wollack's 2022 extension of the DGM framework, which allows preknowledge effects to vary across both persons and items — that's closer to what CRADE is doing with the full G-2PL, and the proposal should acknowledge and differentiate from that work.

On the flip side, I can see the counterargument: yes, you could just compare original versus variant accuracy and flag large gaps as contamination, like ConStat and PaCoST do, but CRADE produces continuous scores, corrected ability estimates, and a principled measurement model rather than just binary labels. The trivial alternative exists but gives you less actionable output. And sure, you could create fresh uncontaminated benchmarks like MathArena, but that's resource-intensive.

The real tension I'm noticing is in the core assumption: the proposal assumes adversarial variants are contamination-free and measure the same underlying ability, but if variants introduce systematic shifts beyond just contamination, then the θ estimated from variants might not map cleanly back to the original construct. The δ_i parameter captures difficulty shifts, but not potential changes in dimensionality or what's actually being measured.

Actually, stepping back, I think there's a more compelling angle here than just contamination correction. The deeper question CRADE is really addressing — whether a model knows something because it memorized it versus because it can reason — is fundamental to LLM evaluation. Framing this as a general framework for separating memorization from reasoning could be more impactful than positioning it narrowly as a contamination tool.

On the novelty front, Gorney & Wollack's work does have structural similarities with CRADE's approach — they modeled how preknowledge impact varies across people and items. But they assumed known exposure status and worked with large examinee samples in classical testing contexts, whereas CRADE's innovation lies in the identification strategy using paired items and the two-stage calibration designed for small sample sizes.

I should also note that "When Benchmarks Leak" uses a fundamentally different intervention — it modifies model behavior through input perturbation rather than correcting scores after the fact. It's conceptually related but operates in a different paradigm entirely.

Looking at the overall picture, this proposal is genuinely strong with clear novelty in an underexplored space. The real innovation isn't just extending DGM to LLMs, but rather the identification strategy via paired items. That framing would sharpen the contribution considerably.

Beyond that, I want to make sure the significance is positioned not just as contamination correction but as a way to decompose memorization from reasoning. I should also address Gorney & Wollack's more recent test security IRT work, clarify how this adds value beyond RankLLM, and properly differentiate the inference-time decontamination approach from this score-correction method.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c43d3c53-90f5-43e1-9734-2e55cccd5520",
  "isSidechain": false,
  "requestId": "req_011CbV7N7nRGKs97bG91E3Mk",
  "type": "assistant",
  "uuid": "965639bd-127c-4f0d-b6c9-82821e398c41",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j82RUzCzmmiWoTw7dMcen",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 39134,
      "output_tokens": 6446,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6446,
          "cache_read_input_tokens": 39134,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 786
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

_source line 52 · 2026-05-28T14:20:02.360Z_

Now I have sufficient context. Let me provide my analysis.

---

【状态】: 有发掘空间

【前置调研发现】
- **PSN-IRT (AAAI 2026 Oral, arXiv 2505.15055)**: 4PL IRT for 12 LLMs on 41,871 items; explicitly flags contamination via anomalous guessing rates but leaves corrected ability estimation as an open question. Confirms IRT-based LLM evaluation is a recognized, accepted direction at AAAI.
- **Growing Pains (arXiv 2604.12843, April 2026)**: Two-stage MIRT 2PL fixed-parameter calibration on Open LLM Leaderboard data; validates <2% MAE with 100 anchor items. Directly validates the two-stage calibration architecture CRADE proposes to adopt. Code available.
- **Wang et al. (ICLR 2026, arXiv 2510.02386)**: Proves likelihood-based contamination detection fails on reasoning models post-GRPO training (AUROC ≈ 50%). This is a genuine demand-creating result — it invalidates an entire class of detectors and motivates response-pattern-based alternatives.
- **JECS (arXiv 2605.21543, May 2026)**: Conformal p-value approach to joint multi-model decontamination. Binarizes items (keep/discard) — information-lossy. Very recent concurrent work, making CRADE's continuous-score approach a timely counterpoint.
- **RankLLM (ICLR 2026, arXiv 2602.12424)**: Non-parametric bidirectional score propagation, 90% human alignment, robust to 50% model removal. No contamination modeling — but achieves strong ranking quality anyway, posing a "trivial alternative" challenge.
- **DCR (EMNLP 2025, ACL Anthology)**: Ad-hoc multiplicative correction (Acc × (1−DCR Factor)); ~4% average error but r=0.66 on hard tasks. No measurement-theoretic grounding.
- **DeconIEP / "When Benchmarks Leak" (arXiv 2601.19334, 2026)**: Inference-time decontamination via bounded perturbation in input embedding space. Fundamentally different paradigm — behavioral intervention during inference rather than score correction post-hoc.
- **Gorney & Wollack, "Two New Models for Item Preknowledge" (Applied Psychological Measurement, 2022)**: Extends DGM with models where preknowledge impact varies by person (low-ability examinees benefit more) and by item (harder items affected more). Structural similarity to R-G-2PL and full G-2PL — **not currently cited in proposal**.
- **Gorney & Wollack, "Generating Models for Item Preknowledge" (Journal of Educational Measurement, 2022)**: Data-generating models for simulating item preknowledge — directly relevant to the simulation study design.
- **RIDE (arXiv 2511.04120)**: Uses IRT as difficulty reward for RL-based question rewriting across 35 LLMs. IRT is a tool, not the estimation target.
- **Quantifying Data Contamination in Psychometric Evaluations of LLMs (arXiv 2510.07175)**: Examines contamination specifically in psychometric (personality inventory) LLM evaluations — related framing but different application domain.
- 调研总结: The field is converging on two parallel tracks — (1) IRT-based LLM evaluation is gaining acceptance (PSN-IRT at AAAI, Growing Pains, RankLLM) but nobody has incorporated contamination as a latent variable within the IRT model; (2) contamination detection/correction is active but uses ad-hoc methods (DCR), binarization (JECS), or behavioral intervention (DeconIEP) rather than measurement-theoretic decomposition. The three-way intersection remains genuinely unoccupied as of late May 2026.

---

【发掘点 1】
- 维度: novelty 锐化
- 内容: Proposal 当前的 novelty framing 是 "extending DGM to LLMs"，这个表述容易被审稿人矮化为 "application paper"（把已有模型搬到新领域）。但实际上 CRADE 的核心创新是**识别策略**（identification strategy），而非模型本身的转移。DGM 及后续 Gorney & Wollack (2022) 的两个模型都有一个根本限制：假设 item exposure status 已知（来自 test security 机构的监控数据）。CRADE 通过 paired adversarial items 解决了 "exposure status unknown" 下的 identification 问题——这是对 gated IRT 整条文献线的方法论贡献，不仅仅是换了一个 application domain。建议将 primary novelty claim 重新锚定在 "identification via paired adversarial anchors under unknown exposure" 上，而非 "extending DGM to LLMs"。这样做的好处：(a) 即使审稿人不关心 LLM 评估，也能看到方法论层面的新意；(b) 对 psychometrics-savvy 审稿人的说服力更强，因为 unknown exposure 确实是 test security 文献的长期痛点。
- 价值: 直接提升 Novelty 维度。将论文从 "应用导向的 extension" 提升到 "方法论贡献 + 应用验证" 的档次，天花板从 borderline accept 升到 solid accept。
- 调研依据: Gorney & Wollack (APM 2022) 的两个新模型仍假设 known exposure status；DGM (Shu et al. 2013) 同理。Proposal 自身已意识到这一点但未将其定位为 primary novelty。

【发掘点 2】
- 维度: significance 提升
- 内容: Proposal 当前将 significance 定位为 "contamination correction for trustworthy LLM evaluation"。这个定位准确但天花板有限——contamination correction 在审稿人眼中可能只是一个技术问题。更有力的 framing 是将 CRADE 定位为解决一个更根本的问题：**在 LLM 评估中分离 memorization 和 reasoning 的一般性测量框架**。Contamination 只是 memorization 最明显的表现形式，但 θ vs. ξ 的分解本质上回答的是 "模型是因为记住了答案还是因为具备推理能力" 这一 LLM 社区最核心的争论。这与 proposal 已引用的 "Illusion of Reasoning"（decorative CoT）直接相关——如果一个模型的 θ 很低但 ξ 很高，这恰恰就是 decorative reasoning + memorization 的定量刻画。将 significance 提升到 "memorization vs. reasoning decomposition" 层面后，论文的 potential impact 显著增大，因为它不仅解决 contamination 问题，还为 reasoning evaluation 提供了一个可操作的 measurement-theoretic lens。
- 价值: 直接提升 Significance 维度。将论文的 problem scope 从 "benchmark hygiene" 提升到 "fundamental question in LLM evaluation"，使审稿人觉得 "这个问题值得解决且解决后对领域有重大推动"。
- 调研依据: Wang et al. (ICLR 2026) 证明 likelihood-based detection 在 reasoning models 上失败，说明领域急需 response-pattern-based 方案来分离 memorization 和 genuine reasoning。"Illusion of Reasoning" (arXiv April 2026) 提供了定性分类法（genuine/scaffolding/decorative），CRADE 可定位为提供**定量**分离。

【发掘点 3】
- 维度: related work 差异化
- 内容: Proposal 未引用 Gorney & Wollack (2022) 的两篇论文："Two New Models for Item Preknowledge" (APM 2022) 和 "Generating Models for Item Preknowledge" (JEM 2022)。这两篇是 DGM 之后 test security IRT 文献的最重要后续工作。第一篇提出了允许 preknowledge impact 在 person 和 item 维度上变化的模型——这与 R-G-2PL (person-level ξ_j) 和 full G-2PL (ξ_j·η_i) 在结构上有相似之处。如果审稿人熟悉这条文献线（AAAI 评审池中可能有 psychometrics 背景的人），遗漏这两篇会被视为 related work 的重大盲区。**必须引用并明确差异化**：(a) G&W 2022 仍假设 known exposure status，CRADE 不需要；(b) G&W 的 person-varying impact 是通过不同的 functional form 实现的（low-ability examinees benefit more），而 CRADE 的 ξ_j 是 global contamination probability，语义不同；(c) G&W 未使用 two-stage calibration 或 paired items。第二篇的 data-generating models 可直接支撑 simulation study 的设计选择，增强方法论严谨性。
- 价值: 直接提升 Related Work 差异化维度。消除一个潜在的 reviewer red flag，同时通过与 G&W 的对比进一步凸显 paired adversarial identification 的创新性。
- 调研依据: Gorney & Wollack (APM 2022) "Two New Models for Item Preknowledge"; Gorney & Wollack (JEM 2022) "Generating Models for Item Preknowledge"。

【发掘点 4】
- 维度: trivial alternative 威胁
- 内容: RankLLM (ICLR 2026) 在不进行任何 contamination modeling 的情况下达到 90% human alignment 和极强的排名稳定性（50% model removal 后 ρ=0.94）。一个理性的审稿人会问：**如果不做 contamination decomposition，仅用 difficulty-weighted ranking 就已经足够好了，CRADE 的增量价值在哪？** Proposal 在 validation 中将 RankLLM 列为 baseline，但这不够——需要在 framing 层面预先回应这个 trivial alternative。建议的策略：(a) 明确 articulate RankLLM 的局限：它产生的是 ranking 而非 interpretable parameter（不能说某个模型 "contamination 比例约 40%，corrected ability 为 x"）；(b) 论证 ranking 和 decomposition 解决的是不同问题——ranking 回答 "谁更好"，decomposition 回答 "为什么好/为什么差"；(c) 预设一个 empirical scenario：如果某模型在 RankLLM 排名中表现中等但 CRADE 揭示其 θ 很低且 ξ 很高，这才是 decomposition 的核心价值——它提供的是 diagnostic information 而非仅仅是 leaderboard position。不处理这个问题，审稿人可能直接以 "marginal improvement over simpler baselines" 拒稿。
- 价值: 直接防御 Novelty 维度的潜在威胁，同时强化 Significance（CRADE 提供的是 diagnostic decomposition 而非 ranking improvement，二者目标不同）。
- 调研依据: RankLLM (ICLR 2026) 的 90% human alignment 和 ρ=0.94 stability 数据；参考 PSN-IRT 在 AAAI 2026 Oral 的接收情况——PSN-IRT 提供的也是 interpretable parameters 而非仅排名，表明 AAAI 评审对 "解释性 > 排名" 的贡献是认可的。

【发掘点 5】
- 维度: 核心 claim 强化
- 内容: 当前 claim 结构是 "paired adversarial items as contamination-free anchors → θ identified from variants → ξ identified from original-variant gaps"。这个逻辑链条中，δ_i（variant difficulty shift）是一个关键但可能被低估的节点。如果 δ_i 不仅仅反映难度变化，还反映了 **construct shift**（变体考察的认知技能与原题不完全相同），那么从变体估计的 θ 和从原题估计的 θ 可能不是同一个 construct。例如，将 GSM8K 的数值替换可能不改变推理结构，但结构性重写（改变问题的解题路径）可能引入新的认知维度。当前 δ_i ~ N(0, σ²_δ) 的设定假设变体只引入 difficulty shift，不引入 dimensionality change。建议在 claim 中明确 **将 variant generation strategy 与 identifiability guarantee 绑定**：SymPy-verified value perturbation（保持问题结构不变，只改数值）是 construct-preserving 的最强形式，因为推理路径完全相同；而 structural perturbation 则需要额外的 dimensionality assessment（例如 eigenvalue ratio check）。这不仅强化了 claim 的逻辑严密性，还为 SymPy-verified pipeline 的选择提供了理论 justification（而非仅仅是 "比 LLM-based verification 更准确"）。
- 价值: 强化 Novelty 和核心 claim 的逻辑链条。将 variant generation 从 "engineering choice" 提升为 "measurement-theoretically motivated design decision"，使整个 framework 在方法论层面更加 self-consistent。
- 调研依据: 基于领域整体趋势判断——IRT 文献中 construct validity 是 item quality 的核心标准（dimensionality assessment 是标准实践）；MATH-Perturb (ICML 2025) 的 expert-crafted perturbations 之所以被视为 gold standard，正是因为人工审核确保了 construct preservation。

Sources:
- [PSN-IRT: Lost in Benchmarks? (AAAI 2026 Oral)](https://arxiv.org/abs/2505.15055)
- [Growing Pains: Extensible LLM Benchmarking (arXiv April 2026)](https://arxiv.org/abs/2604.12843)
- [Wang et al.: Fragility of Benchmark Contamination Detection (ICLR 2026)](https://arxiv.org/abs/2510.02386)
- [JECS: Provable Joint Decontamination (arXiv May 2026)](https://arxiv.org/abs/2605.21543)
- [RankLLM: Weighted Ranking of LLMs (ICLR 2026)](https://arxiv.org/abs/2602.12424)
- [DCR: Quantifying Data Contamination (EMNLP 2025)](https://aclanthology.org/2025.emnlp-main.1173/)
- [When Benchmarks Leak: Inference-Time Decontamination (arXiv 2026)](https://arxiv.org/abs/2601.19334)
- [DGM: Shu, Henson, Luecht (Psychometrika 2013)](https://link.springer.com/article/10.1007/s11336-012-9311-3)
- [Gorney & Wollack: Two New Models for Item Preknowledge (APM 2022)](https://journals.sagepub.com/doi/10.1177/01466216221108130)
- [Gorney & Wollack: Generating Models for Item Preknowledge (JEM 2022)](https://onlinelibrary.wiley.com/doi/10.1111/jedm.12309)
- [RIDE: Difficulty Evolving Perturbation with IRT (arXiv 2025)](https://arxiv.org/abs/2511.04120)
- [MaSTer: Automated Robustness Evaluation of Mathematical Reasoning (arXiv 2026)](https://arxiv.org/abs/2506.05038)
- [Quantifying Data Contamination in Psychometric Evaluations of LLMs (arXiv 2025)](https://arxiv.org/abs/2510.07175)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "965639bd-127c-4f0d-b6c9-82821e398c41",
  "isSidechain": false,
  "requestId": "req_011CbV7N7nRGKs97bG91E3Mk",
  "type": "assistant",
  "uuid": "938d1408-2bd5-4cfe-b9b3-b549f2f6ecc6",
  "userType": "external",
  "entrypoint": "sdk-py",
  "cwd": "/home/ubuntu",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5",
  "version": "2.1.142",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019j82RUzCzmmiWoTw7dMcen",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 786,
      "cache_read_input_tokens": 39134,
      "output_tokens": 6446,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 786,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 6446,
          "cache_read_input_tokens": 39134,
          "cache_creation_input_tokens": 786,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 786
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

_source line 53_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  ## Core Problem  No existing framework can determine whether a model fails adversarial…",
  "leafUuid": "938d1408-2bd5-4cfe-b9b3-b549f2f6ecc6",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Runtime record

_source line 54_

```json
{
  "type": "ai-title",
  "aiTitle": "Develop CRADE contamination-ability IRT framework",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Runtime record

_source line 55_

```json
{
  "type": "last-prompt",
  "lastPrompt": "# CRADE: Joint Contamination-Ability Decomposition via Gated Item Response Theory with Paired Adversarial Items  ## Core Problem  No existing framework can determine whether a model fails adversarial…",
  "leafUuid": "938d1408-2bd5-4cfe-b9b3-b549f2f6ecc6",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---

### Runtime record

_source line 56_

```json
{
  "type": "ai-title",
  "aiTitle": "Develop CRADE contamination-ability IRT framework",
  "sessionId": "3e15f2de-7019-46a4-8086-85a482d5a8a5"
}
```

---
