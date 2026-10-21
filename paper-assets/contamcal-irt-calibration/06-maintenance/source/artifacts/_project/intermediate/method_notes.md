# Method Section Notes — ContamCal

Word budget: 1100 words (per writing_plan.yaml §method)

---

## 3.1 Problem Formulation

**Core idea**: Given model $j$, benchmark $k$ with items $i$, observed binary response $y_{ijk}$. The latent ability $\theta_j$ is confounded by contamination exposure. Goal: estimate $\theta_j^{\text{clean}}$ (ability absent contamination).

**Three structural adaptations from educational measurement IRT**:
1. Independent examinees → single model with joint item distribution (all items share one θ per model)
2. Binary leakage indicator → continuous exposure score $e_{ij} \in [0,1]$
3. Stable ability → regime-conditional ability (θ may shift with contamination dosage)

**Prior work to cite**:
- Eckerly (2017): item compromise IRT — closest precedent (binary leak + 3PL)
- Sinharay (2017): compromised item detection via IRT residuals
- De Boeck & Wilson (2004): explanatory IRT framework (covariates on item/person parameters)
- Adams et al. (1997): multifaceted Rasch as structural template
- Mislevy (1986): fixed-effects IRT when N_examinees is small

**Key notation**:
- $y_{ijk} \in \{0,1\}$: response of model $j$ to item $i$ on benchmark $k$
- $\theta_j$: latent ability of model $j$
- $e_{ij}$: exposure score (from Stage 1 RRF)
- $\gamma_k$: per-benchmark contamination effect parameter
- $a_i, b_i, c_i, d_i$: item discrimination, difficulty, guessing, slip

**Corresponding experiments**: exp-006 (all IRT fits)

---

## 3.2 Stage 1: Multi-Signal Exposure Mapping

**Core idea**: Map each (model, item) pair to a continuous exposure score $e_{ij}$ via training-free Reciprocal Rank Fusion of multiple contamination signals. Training-free fusion avoids meta-circularity (a learned aggregator's training data may itself be contaminated).

**Signals**:
| ID | Signal | Method | Source |
|----|--------|--------|--------|
| S1 | Embedding similarity | cosine(item embedding, nearest training chunk) | Provenance-based |
| S2 | Min-K++ | token-level surprise (low perplexity on memorized items) | MIA-based |
| S3 | [Reserved/deprecated] | — | — |
| S4 | Self-Critique | model-generated paraphrase similarity | Behavioral |

**RRF formula**:
$$e_{ij} = \sum_{s \in \text{signals}} \frac{1}{k + r_s(i,j)}$$
where $r_s(i,j)$ is the rank of item $i$ for model $j$ under signal $s$, and $k=60$ (standard RRF constant).

**Critical empirical finding** (feeds into Results §5.2, but contextualize in Method):
- S1 is the only reliable signal (AUC > 0.95 at d005)
- S2 Min-K++ exhibits directional reversal at 0.5B (Cohen's d = -1.98) — actively misleading
- RRF degrades to S1-only in practice; presented honestly as limitation but RRF remains principled design (extensible when better signals emerge)

**Meta-circularity argument**: Learned aggregation (e.g., logistic regression over signals) requires labeled contamination data → circular dependency. RRF is rank-based, parameter-free, training-free.

**Prior work to cite**:
- Cormack et al. (2009): RRF original paper
- Zhang et al. (2024): Min-K++ [CITE: zhang2024minkpp]
- Shokri et al. (2017): MIA foundations for S2 contextualization
- Carlini et al. (2022): training data extraction (broader MIA context)
- Dong et al. (2024): KDS [CITE NEEDED exact ref]
- Shi et al. (2024): CDD [CITE NEEDED exact ref]

**Corresponding experiments**: exp-002 (signal pipeline), exp-003 (RRF ablation), exp-008 (signal evaluation)

---

## 3.3 Stage 2: Contamination-Augmented IRT

**Core idea**: Extend standard IRT with a contamination covariate $\gamma_k \cdot e_{ij}$ in the logit. Per-benchmark $\gamma_k$ captures heterogeneous contamination effects (inflation on GSM8K, forgetting on ARC).

**Model definitions**:

### 2PL + γ (default, robust)
$$P(y_{ijk} = 1) = \sigma\big(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\big)$$

Use when: N < 16, or benchmark is not strictly MCQ format.

### 4PL + γ (full model, MCQ benchmarks)
$$P(y_{ijk} = 1) = c_i + (d_i - c_i) \cdot \sigma\big(a_i(\theta_j - b_i) + \gamma_k \cdot e_{ij}\big)$$

Use when: N ≥ 16, MCQ format benchmark.

- $c_i$: guessing parameter (lower asymptote, ~0.25 for 4-choice MC)
- $d_i$: slip parameter (upper asymptote, <1.0 for careless errors)

**Model selection rule** (C008 constraint):
- 2PL+γ is default — robust even at small N
- 4PL+γ only when N≥16 AND MCQ format (c/d parameters identifiable only with sufficient data)
- ARC N=5 with 4PL+γ → PPP=0.000, MAE worsens 17× (overparameterization collapse)

**Per-benchmark $\gamma_k$ identification strategy**:
- Fit IRT independently per benchmark (not jointly across benchmarks)
- $\gamma_k$ inherits sign and magnitude from exposure-response relationship on that specific benchmark
- Positive $\gamma_k$: contamination inflates scores (memorization helps)
- Negative $\gamma_k$: contamination degrades scores (forgetting/capacity displacement)
- Non-significant $\gamma_k$: benchmark naturally resistant or signal uninformative

**Inference**: Stan NUTS (No-U-Turn Sampler), 4 chains, 1000 warmup + 1000 sampling. Convergence: R̂ < 1.05, ESS > 400. Model fit: PPP ∈ [0.1, 0.9].

**Calibration procedure**:
1. Fit IRT with exposure scores → posterior $p(\theta_j, \gamma_k | \mathbf{y}, \mathbf{e})$
2. Predict clean score: set $e_{ij} = 0$ for all items → $\hat{y}_{ijk}^{\text{clean}}$
3. Calibrated accuracy = mean of predicted clean item responses
4. CI from posterior draws

**Gating criterion** (when NOT to calibrate):
- $\gamma_k$ must be significant (CI excludes 0)
- PPP ∈ [0.1, 0.9] (model not misspecified)
- Calibrated MAE < raw MAE (calibration must help)
- If any condition fails → report raw scores

**Prior work to cite**:
- De Boeck & Wilson (2004): explanatory IRT (covariate on logit)
- San Martín et al. (2009): IRT identifiability conditions
- Maris & Bechger (2009): IRT parameter identifiability
- Lalor et al. (AAAI 2024): IRT for LLM evaluation
- Holland & Wainer (1993): DIF — γ_k is essentially DIF between exposed/unexposed groups
- Talts et al. (2018): SBC for posterior calibration validation
- Brown & Thomson (2024): PPP distribution interpretation

**Corresponding experiments**: exp-006 (all IRT configurations)

---

## 3.4 Fisher Information and Identifiability

**Core idea**: Derive the Fisher Information $I(\gamma)$ for the 4PL+γ model to establish theoretical recovery boundaries. Show that signal AUC and N_models jointly determine γ recoverability. Reveal structural domain-method mismatch: LLM evaluation typically has N=8-30 models, but reliable recovery needs N≥50.

**Key results from simulation sweep** (exp-004, 24 conditions × 240 runs):
- Recovery succeeds at AUC=0.55 (lowest tested) when J≥50 items, N≥20 models
- CI width ∝ $N^{-0.48}$ (empirically estimated decay rate)
- Coverage collapse at N<30 (confirmed D036)
- Lower bound of AUC for recovery remains open (not tested below 0.55)

**Fisher Information sketch** (full derivation in Appendix A):
$$I(\gamma) = \sum_{i,j} e_{ij}^2 \cdot P_{ij}(1-P_{ij}) \cdot \left(\frac{d_i - c_i}{P_{ij} - c_i}\right)^2 \cdot \frac{(P_{ij}-c_i)^2}{(d_i-c_i)^2}$$

Simplified for 2PL+γ (c=0, d=1):
$$I(\gamma) = \sum_{i,j} e_{ij}^2 \cdot P_{ij}(1-P_{ij})$$

Key insight: $I(\gamma)$ scales with (a) variance of exposure scores (higher AUC → more discriminative $e_{ij}$), (b) number of models N, (c) item information (items near difficulty boundary contribute most).

**Domain-method mismatch framing**:
- Educational testing: hundreds of examinees, clear binary leak indicator → recovery trivial
- LLM evaluation: 8-30 models, noisy continuous exposure signal → structural challenge
- This is not merely "IRT needs more data" — it's a fundamental mismatch between the measurement framework's assumptions and the LLM evaluation domain's constraints

**Measurement error extension** (exp-005, negative result — mention briefly):
- Model exposure as noisy observation: $e_{ij} = \tau_{ij} + \epsilon$, $\epsilon \sim N(0, \sigma_e^2)$
- Result: CI width insensitive to $\sigma_e$ across tested range → noise propagation is NOT the binding constraint
- Binding constraint is N (number of models), not signal noise

**Prior work to cite**:
- San Martín et al. (2009): IRT identifiability
- Talts et al. (2018): SBC diagnostic
- Reckase (2009): multidimensional IRT (limitation: our θ is unidimensional)
- Angelopoulos & Bates (2023): conformal prediction as alternative UQ (discuss why Bayesian IRT preferred: interpretable parameters, contamination covariate integration)

**Corresponding experiments**: exp-004 (simulation sweep), exp-005 (noise propagation)

---

## Domain-Level Heterogeneity Analysis (supplements §5.1, methodology described in §3.3)

**Core idea**: Within MMLU, stratify 57 subjects into 8 cognitive domains. Fit 2PL+γ per domain. Reveals Simpson's paradox: aggregate γ≈0 masks domain-level heterogeneity.

**Domain taxonomy**: 57 MMLU subjects → 8 cognitive domains:
- STEM_Math, STEM_Science, STEM_CS_Eng
- Medical (excluded, D112: PPP=1.0 systematic misfit)
- Humanities, Social_Sciences, Business_Law, Other

**Formalization of Simpson's paradox**:
- Aggregate fit: $\gamma_{\text{MMLU}} \approx 0$ (CI includes 0)
- Domain-level: $\gamma_{\text{Math}} = +0.97$, $\gamma_{\text{Science}} = +0.84$, $\gamma_{\text{CS\_Eng}} = +0.20$ (NS)
- Non-STEM: PPP≈1.0 → model misspecification (2PL+γ inadequate for these domains)
- Interpretation: contamination susceptibility maps to factual knowledge density

**Claim scope limitations**:
- Only claim pattern/ranking from domains with PPP ∈ [0.1, 0.9] (Math, Science have acceptable PPP)
- Non-STEM PPP=1.0 is a boundary finding, not failure — reported as model scope limitation
- Cannot claim absolute γ values from domains with PPP=0

**Prior work to cite**:
- Kievit et al. (2013): Simpson's paradox formal framework
- Ercikan et al. (2008): DIF cancellation as empirical precedent
- Thissen et al. (1993): DIF detection in IRT
- Zumbo (1999): DIF overview

**Corresponding experiments**: exp-006 (mmlu_domain_gamma_n24_v4), D108/D115/D116

---

## Cross-Family Validation Protocol (Llama-3.2-3B)

**Core idea**: Test whether contamination susceptibility (per-benchmark γ_k, domain heterogeneity pattern) is a benchmark × domain property rather than a Qwen2.5 family artifact.

**Design**:
- Model: Llama-3.2-3B (different architecture, tokenizer, pretraining data)
- Same injection protocol: LoRA alpha=32, same dosages (d000/d005/d025/d100)
- Same evaluation: aligned + paraphrased format
- Same signal pipeline: S1 embedding similarity (corpus-agnostic)

**Validation criteria**:
- γ_k sign agreement across families (ARC negative, GSM8K non-significant)
- Domain heterogeneity gradient reproduces (STEM > non-STEM)
- If patterns replicate → contamination effects are benchmark properties
- If patterns diverge → model architecture/capacity matters more

**Status**: Llama SFTs running (D106), results expected Day 2-3. If complete before deadline, included in main paper. Otherwise, prepared as rebuttal material (exp-014).

**Corresponding experiments**: exp-014 (cross-family), D106

---

## RRF Aggregation Method Detail

**Formula**:
$$\text{RRF}(i,j) = \sum_{s=1}^{S} \frac{w_s}{k + r_s(i,j)}$$

- $S$: number of active signals (up to 4)
- $w_s = 1$ for all signals (uniform weight — training-free)
- $k = 60$ (standard constant from Cormack et al. 2009)
- $r_s(i,j)$: rank of item $i$ among all items for model $j$ under signal $s$ (1 = most exposed)

**Normalization**: Min-max scale final RRF scores to [0, 1] per model-benchmark.

**Practical reality at current scale**:
- Only S1 provides discriminative signal (AUC > 0.9)
- S2, S4 ≈ random at 0.5B; may improve at 1.5B/3B (pending verification)
- RRF value is principled aggregation architecture; current instantiation ≈ S1-only
- Honest framing: "training-free multi-signal architecture with graceful degradation"

---

## Evaluation Protocol (6 Metrics)

1. **MAE**: $\frac{1}{J}\sum_j |{\hat{acc}_j^{\text{cal}}} - acc_j^{\text{clean}}|$ (point estimate quality)
2. **Coverage@95%**: fraction of true values within 95% credible interval
3. **Sharpness**: mean CI width (narrower = better at fixed coverage)
4. **Kendall's τ**: rank correlation between calibrated and true model rankings
5. **Dose-response monotonicity**: $\gamma$ effect increases with dosage level
6. **SBC** (Talts et al. 2018): simulation-based calibration diagnostic at actual N and J

**Ground truth**: $acc_j^{\text{clean}}$ = accuracy of the d000 (clean) model on same benchmark. For RL observational track (future work): held-out clean benchmark, NOT calibrated scores (avoids circularity).
