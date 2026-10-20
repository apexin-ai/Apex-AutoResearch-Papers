# Literature Scan Report — 2026-05-15

**Scope**: Papers published or posted as arXiv preprints during March–May 2026, relevant to our EMNLP 2026 submission on multi-method consensus for lead-lag analysis in iterative training collapse.

**Baseline**: 30+ papers already tracked in `literature_map.yaml`.

---

## New Papers Found

### 1. [HIGH RELEVANCE] Causal-Audit: A Framework for Risk Assessment of Assumption Violations in Time-Series Causal Discovery

- **Authors**: Marco Ruiz, Miguel Arana-Catania, David R. Ardila, Rodrigo Ventura
- **Date**: April 2, 2026
- **URL**: https://arxiv.org/abs/2604.02488
- **Key Findings**:
  - Proposes pre-screening framework that validates assumptions (stationarity, regularity, persistence, nonlinearity, confounding) before applying causal methods
  - Computes calibrated risk scores (AUROC > 0.95) across five assumption families
  - Abstention-aware decision policy: recommends methods (PCMCI+, VAR-based Granger) only when evidence supports reliable inference
  - **62% false positive reduction** among recommended datasets; 78% abstention on severe violations
- **Relation**: **Complementary (important to cite)**
  - Directly relevant to **Claim 3** (Granger causality pitfalls). They do **pre-screening** of assumptions before method selection; we do **post-hoc consensus** across multiple methods to filter spurious results. Approaches are complementary, not competing.
  - Strengthens our narrative that naive Granger causality is unreliable — their 62% FP reduction validates that standard practice yields high false positive rates.
  - **Action**: Must cite in methodology section. Frame as: "Causal-Audit validates assumptions before method selection; our consensus framework validates conclusions after applying multiple methods. Both address the same fundamental problem — unchecked causal methods produce misleading results."

### 2. [HIGH RELEVANCE] On the Entropy Calibration of Language Models

- **Authors**: Steven Cao, Gregory Valiant, Percy Liang
- **Date**: November 15, 2025 (v1); revised January 13, 2026 (v2)
- **URL**: https://arxiv.org/abs/2511.11966
- **Key Findings**:
  - Entropy miscalibration improves very slowly with scale (exponent ≈ 0)
  - Error accumulation: entropy per step increases as generations grow longer
  - **All current calibration methods reduce entropy at the cost of diversity** — theoretically proves a calibration-diversity tradeoff
  - Proves that reducing entropy while preserving log loss is theoretically possible
- **Relation**: **Complementary (important to cite)**
  - Directly supports **Claim 1** (ECE leads diversity). Their proven calibration-diversity tradeoff provides theoretical backing for why calibration degradation (ECE↑) might precede diversity collapse — if calibration and diversity are fundamentally linked, changes in one should propagate to the other.
  - **Action**: Cite in Discussion. Frame as: "Cao et al. (2026) prove a fundamental calibration-diversity tradeoff in LMs; our empirical lead-lag findings may reflect this theoretical coupling — calibration perturbation propagates to diversity with a temporal lag."

### 3. [MEDIUM RELEVANCE] Calibration Collapse Under Sycophancy Fine-Tuning: How Reward Hacking Breaks Uncertainty Quantification in LLMs

- **Authors**: Subramanyam Sahoo
- **Date**: April 12, 2026
- **URL**: https://arxiv.org/abs/2604.10585
- **Key Findings**:
  - Sycophantic GRPO training increases ECE by +0.006, MCE by +0.010 vs neutral SFT
  - Post-hoc scaling reduces ECE 40–64% but reward-trained model retains worse calibration even after correction
  - Demonstrates calibration is sensitive to training-distribution perturbation
- **Relation**: **Complementary**
  - Different mechanism (RLHF reward hacking vs iterative synthetic data) but same conclusion: ECE is a sensitive indicator of training-induced distributional shift.
  - Provides additional evidence for ECE as a viable canary metric.
  - **Action**: Cite in Related Work (canary metrics section) as independent evidence of ECE's sensitivity.

### 4. [MEDIUM RELEVANCE] CausalCompass: Evaluating the Robustness of Time-Series Causal Discovery in Misspecified Scenarios

- **Authors**: Huiyang Yi, Xiaojian Shen, Yonggang Wu, Duxin Chen, He Wang, Wenwu Yu
- **Date**: February 8, 2026 (v1); revised April 30, 2026 (v2)
- **URL**: https://arxiv.org/abs/2602.07915
- **Key Findings**:
  - Benchmark suite for causal discovery robustness under 8 assumption-violation scenarios
  - No single method consistently dominates; deep learning methods generally best
  - Hyperparameter sensitivity significant across methods
- **Relation**: **Complementary**
  - Supports Claim 3 narrative: causal methods are brittle under misspecification. Our short time series (T=10–20) with non-stationary dynamics is exactly the kind of scenario where methods fail.
  - **Action**: Cite in methodology section alongside Causal-Audit.

### 5. [MEDIUM RELEVANCE] Curated Synthetic Data Doesn't Have to Collapse: A Theoretical Study of Generative Retraining with Pluralistic Preferences

- **Authors**: Ali Falahati, Mohammad Mohammadi Amiri, Kate Larson, Lukasz Golab
- **Date**: May 8, 2026 (ICML 2026)
- **URL**: https://arxiv.org/abs/2605.07724
- **Key Findings**:
  - Multiple reward functions → convergence to stable distribution (weighted Nash bargaining solution)
  - Maintains diversity instead of collapsing
  - Theoretical proof under specific conditions
- **Relation**: **Background**
  - Mitigation strategy (pluralistic curation), not about detection. Different from our focus on early warning.
  - Relevant context: if such mitigation exists, the question "when to trigger it" (which our canary answers) becomes more practical.
  - **Action**: Optional citation in Related Work (mitigation approaches).

### 6. [LOW RELEVANCE] Human-AI Co-Evolution and Epistemic Collapse: A Dynamical Systems Perspective

- **Authors**: Xuening Wu, Yanlan Kang, Qianya Xu, et al.
- **Date**: May 7, 2026
- **URL**: https://arxiv.org/abs/2605.06347
- **Key Findings**:
  - Three dynamical regimes in human-AI feedback loop: co-evolutionary enhancement, fragile equilibrium, degenerative convergence
  - Entropy reduction as indicator of diversity loss
- **Relation**: **Background**
  - Workshop-length paper (5 pages), primarily theoretical, limited empirical validation. Different scope (human-AI system level, not training metrics).
  - **Action**: No citation needed.

### 7. [LOW RELEVANCE] Position: the Stochastic Parrot in the Coal Mine — Model Collapse is a Threat to Low-Resource Communities

- **Authors**: Devon Jarvis, Richard Klein, Benjamin Rosman, Steven James, Stefano Sarao Mannelli
- **Date**: May 5, 2026
- **URL**: https://arxiv.org/abs/2605.04127
- **Key Findings**:
  - Position paper arguing model collapse disproportionately harms low-resource communities
  - No new methods or metrics
- **Relation**: **Background**
  - Position paper, no methodological contribution. Relevant context for motivation only.
  - **Action**: No citation needed.

### 8. [LOW RELEVANCE] Persona-Model Collapse in Emergent Misalignment

- **Authors**: Davi Bastos Costa, Renato Vicente
- **Date**: May 13, 2026
- **URL**: https://arxiv.org/abs/2605.12850
- **Key Findings**:
  - Fine-tuning on harmful data causes persona-model collapse (inability to maintain character personas)
  - Measures moral susceptibility and robustness
- **Relation**: **Background**
  - Different collapse type (persona coherence, not distributional). Not related to iterative synthetic data.
  - **Action**: No citation needed.

### 9. [LOW-MEDIUM RELEVANCE] Synthetic Eggs in Many Baskets: The Impact of Synthetic Data Diversity on LLM Fine-Tuning

- **Authors**: Max Schaffelder, Albert Gatt
- **Date**: November 2025 (v1); revised April 28, 2026 (v3) — ACL 2026 Findings
- **URL**: https://arxiv.org/abs/2511.01490
- **Key Findings**:
  - Diverse synthetic sources preserve output diversity; single-source leads to distribution collapse
  - Fine-tuning on synthetic data maintains higher quality but potentially creates safety concerns
- **Relation**: **Background**
  - Studies source diversity, not iterative training loops. Confirms diversity matters but no lead-lag analysis.
  - **Action**: Optional citation in Related Work.

---

## Novelty Assessment

### Claim 1: ECE as canary for diversity collapse (lead-lag relationship)

**Status: NOVEL — slightly strengthened**

- No new paper performs lead-lag analysis between calibration and diversity metrics.
- chen2025scales (arXiv:2510.05133) remains the closest competitor. It has NOT been updated since October 2025, and remains an unreviewed preprint. They observed ECE degrades before accuracy but did NOT do Granger causality or any formal temporal analysis.
- **New support**: Cao et al. (2026) prove a calibration-diversity tradeoff in LMs, providing theoretical backing for why ECE might lead diversity. Sahoo (2026) independently confirms ECE's sensitivity to training perturbation.
- **Risk**: LOW. No one has moved toward formal lead-lag analysis in this space.

### Claim 2: Non-monotonic regime map (α-dependent detectability)

**Status: NOVEL — no change**

- No new paper studies how canary sensitivity varies with synthetic data ratio.
- Falahati et al. (2026) study pluralistic curation but not α-dependent dynamics.
- The dose-response non-monotonicity remains unreported by others.
- **Risk**: LOW.

### Claim 3: Naive Granger causality pitfalls + multi-method consensus framework

**Status: NOVEL — but landscape has evolved**

- **Causal-Audit** (Ruiz et al., April 2026) is the most relevant new work. They propose assumption pre-screening for causal discovery, achieving 62% FP reduction. This validates our core concern (naive methods fail) but takes a different approach (pre-screening vs post-hoc consensus).
- **CausalCompass** (Yi et al., Feb/April 2026) benchmarks causal method robustness under misspecification, confirming no single method works universally.
- Neither paper applies their framework to ML training metrics or model collapse detection.
- **Risk**: LOW-MEDIUM. The "naive causal methods are unreliable" message is gaining traction. We should clearly differentiate our consensus approach from Causal-Audit's pre-screening approach.

### Overall

**All three claims remain novel.** No direct competitor doing lead-lag analysis of calibration vs diversity in iterative collapse. The methodological landscape around causal inference reliability is maturing (Causal-Audit, CausalCompass), which supports rather than threatens our Claim 3.

---

## Action Items

### Must-cite (add to Related Work)

| Paper | Section | Role |
|-------|---------|------|
| Causal-Audit (Ruiz et al., 2026) | Methodology / Claim 3 discussion | Complementary approach to filtering spurious causal results |
| CausalCompass (Yi et al., 2026) | Methodology | Benchmark evidence that causal methods fail under misspecification |
| Cao et al. (2026) — Entropy Calibration | Discussion / Claim 1 | Theoretical grounding for calibration-diversity coupling |

### Should-cite (strengthen narrative)

| Paper | Section | Role |
|-------|---------|------|
| Sahoo (2026) — Calibration Collapse | Related Work (canary metrics) | Independent evidence of ECE sensitivity to training perturbation |
| Falahati et al. (2026) — Curated Synthetic Data | Related Work (mitigation) | Motivates "when to intervene" question that canaries answer |

### Optional-cite (low priority)

| Paper | Section | Role |
|-------|---------|------|
| Schaffelder & Gatt (2026) — Synthetic Eggs | Related Work (data mixing) | Source diversity preserves output diversity |

### No citation needed

- Wu et al. (2026) — Human-AI Co-Evolution (workshop paper, tangential)
- Jarvis et al. (2026) — Stochastic Parrot (position paper)
- Costa & Vicente (2026) — Persona-Model Collapse (different collapse type)

---

## Update to literature_map.yaml

The following entries should be added:

```yaml
- id: "ruiz2026causalaudit"
  title: "Causal-Audit: A Framework for Risk Assessment of Assumption Violations in Time-Series Causal Discovery"
  authors: "Marco Ruiz, Miguel Arana-Catania, David R. Ardila, Rodrigo Ventura"
  venue: "arXiv (2604.02488)"
  year: 2026
  url: "https://arxiv.org/abs/2604.02488"
  category: "methodology"
  role: "complementary"

- id: "yi2026causalcompass"
  title: "CausalCompass: Evaluating the Robustness of Time-Series Causal Discovery in Misspecified Scenarios"
  authors: "Huiyang Yi, Xiaojian Shen, Yonggang Wu, Duxin Chen, He Wang, Wenwu Yu"
  venue: "arXiv (2602.07915)"
  year: 2026
  url: "https://arxiv.org/abs/2602.07915"
  category: "methodology"
  role: "complementary"

- id: "cao2026entropycal"
  title: "On the Entropy Calibration of Language Models"
  authors: "Steven Cao, Gregory Valiant, Percy Liang"
  venue: "arXiv (2511.11966)"
  year: 2026
  url: "https://arxiv.org/abs/2511.11966"
  category: "canary-metrics"
  role: "theoretical-foundation"

- id: "sahoo2026sycophancy"
  title: "Calibration Collapse Under Sycophancy Fine-Tuning"
  authors: "Subramanyam Sahoo"
  venue: "arXiv (2604.10585)"
  year: 2026
  url: "https://arxiv.org/abs/2604.10585"
  category: "canary-metrics"
  role: "complementary"

- id: "falahati2026curated"
  title: "Curated Synthetic Data Doesn't Have to Collapse"
  authors: "Ali Falahati, Mohammad Mohammadi Amiri, Kate Larson, Lukasz Golab"
  venue: "ICML 2026"
  year: 2026
  url: "https://arxiv.org/abs/2605.07724"
  category: "data-mixing"
  role: "background"
```
