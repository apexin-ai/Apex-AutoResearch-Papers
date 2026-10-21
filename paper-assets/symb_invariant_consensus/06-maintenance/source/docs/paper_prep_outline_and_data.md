# Paper Preparation: Outline + Data Tables + Figure Inventory
# Updated: 2026-05-20
# Status: Waiting for R (DeBERTa) and S (CoVe) results before writing prose
# Framing: D085 (pending Director's final decision after R/S)

---

## Part 1: Refined Section Outline

### §1 Introduction (1.35pp)

**¶1 — Hook: SC plateau**
- Test-time compute via SC improves reasoning but plateaus (Loo 2025)
- Adding more traces yields diminishing returns → structural mismatch
- Key number: gains plateau and even decline for strong models

**¶2 — Gap: Can self-extraction break the plateau?**
- Neuro-symbolic methods (Logic-LM, DyLoS, FoVer, Aristotle) use external/trained components
- Simpler question: can the SAME model extract useful FOL constraints from its own traces?
- Self-extraction = zero-cost upgrade, no external tools needed

**¶3 — Insight: CJT + Confirmation Bias** [MAJOR UPDATE]
- CJT requires voter independence; same-model traces violate this
- Eff-K = 1.20–3.62 for nominal K=12 → traces beyond 12 add negligible info
- [NEW] Self-extracted constraints don't just inherit correlation — they exhibit Symbolic Confirmation Bias (4.97× bias ratio on incorrect problems)
- [NEW] Process-level analysis: CoT cosine similarity 0.69 >> answer-κ 0.41 → reasoning paths more homogeneous than answers suggest

**¶4 — Evaluation scope**
- SICA pipeline + Condorcet analysis + oracle control
- 6 models (7B–32B), 3 domains, N>3,000, 4-seed replication
- [UPDATE] 25+ remediation strategies (up from 12)

**¶5 — Key results**
- No significant positive; oracle +14.22pp proves mechanism sound
- Independence-accuracy trade-off: Debate κ→0.15 but -18.6pp
- Bottleneck universal across 3 model families (Mistral, LLaMA, Qwen)

**Contributions (4):**
1. **C1 (PRIMARY): Independence-Accuracy Trade-off** — Pareto frontier across 4 methods + 3 families; 25+ interventions all fail
2. **C2 (CORE): Symbolic Confirmation Bias** — 4.97× bias ratio; 94% error overlap with SC; oracle gap 24%; causal chain identified
3. **C3 (NEW): Process-κ + Independence Quantification** — cosine 0.69 >> answer-κ 0.41; κ=0.21–0.82; universal across 3 families
4. **C4: Regime-Dependent Pattern + Diagnostics** — 3 failure modes; C0+SC diagnostic; entropy decomposition

### §2 Related Work (0.70pp)
- SC and extensions (5-6 refs): Wang 2023, USC, Loo 2025, Taubenfeld 2025, DiVeRSe
- Neuro-symbolic (6 refs): Logic-LM, LINC, DyLoS, Aristotle, FoVer, LogicAgent → all use external; we test self-extraction
- CJT/voting (4 refs): Condorcet, Ladha 1992, Lefort 2024 → we extend to symbolic extraction
- Verification (3 refs): ORM, PRM, Math-Shepherd → trained verifier paradigm
- Self-correction parallels (2 refs): Huang 2024, Stechly 2025 → parallel to our confirmation bias
- Debate (2 refs): Liang 2023, Du 2023 → different regime
- [MINOR PATCH: add confirmation bias parallel to self-correction literature]

### §3 Method (1.20pp)

**§3.1 SC and Condorcet (300w)** — KEEP
- SC as majority voting; CJT guarantee; Eff-K formula (Eq. 1)

**§3.2 SICA Pipeline (400w)** — KEEP
- Trace gen → extraction → dedup → MAX-SAT → scoring
- Degeneration under confirmation bias (Eq. 4)
- C0 diagnostic (Eq. 5)
- Figure 1: Pipeline diagram

**§3.3 Oracle Control (200w)** — KEEP
- Gold FOL replaces self-extracted; causal isolation

**§3.4 Process-Level Independence (150w)** — NEW
- Define process-κ: pairwise CoT cosine similarity (TF-IDF)
- Motivation: answer-κ may underestimate true bottleneck
- If traces reason similarly but reach different answers → answer-κ overestimates independence
- Applicable to all LLM trace aggregation

**§3.5 Scope (100w)** — PATCH
- Same-model self-extraction
- 25+ remediation strategies tested (9 prompt + 3 method + 13 additional)

### §4 Experiments (1.50pp)

**§4.1 Setup (250w)** — MINOR PATCH
- 6 models, 3 domains + diagnostics, K=12, T=0.7
- [ADD] mention confirmation bias and process-κ experiments

**§4.2 Main Results (500w)** — KEEP
- Table 1 (table*): ~18 conditions + 2 oracle rows
- Regime pattern: intermediate-SC, Type A, Type C, degenerate
- Figure 2: SC vs Δ scatter

**§4.3 Oracle Control (200w)** — KEEP
- +14.22pp FOLIO, +11.50pp PW; 24% utilization

**§4.4 Four-Seed Replication (150w)** — COMPRESS (was 250w)
- 4 seeds: +3.43 to -0.49pp; mean +1.47pp; 0/4 significant

### §5 Analysis (1.70pp) — MAJOR RESTRUCTURE

**§5.1 Condorcet Effective-K (300w)** — KEEP
- Table 3: κ and Eff-K across 15 conditions
- Cross-model: 3 families κ≥0.41; architecture-independent ceiling
- Dual requirement: sufficient Eff-K AND sufficient SC

**§5.2 Symbolic Confirmation Bias (250w)** — NEW
- Key metrics from exp-confirmation-bias:
  - SICA-correct: gold constraint rate 78.1%, bias ratio 0.28
  - SICA-incorrect: wrong constraint rate 83.3%, bias ratio 4.97×
  - 94% SICA errors overlap SC errors
  - 12 correct flips from minority trace diversity (43% gold support)
- Causal chain: model→answer→FOL confirms answer→aggregation≈SC
- CEGIS validation: refinement doesn't help (oscillates)
- Quality Ladder: cross-model extraction ≈ self-extraction << oracle

**§5.3 Process-Level Independence (200w)** — NEW
- Mistral-7B FOLIO-204 results:
  - CoT cosine similarity: 0.69
  - Answer-κ: 0.41
  - Correlation: r=-0.06, p=0.36 (uncorrelated)
  - Convergent reasoning pairs: 9.3%
- Answer-κ is lower bound on true independence bottleneck
- Even methods targeting answer diversity may not break process-level correlation

**§5.4 Supporting Diagnostics (200w)** — COMPRESS
- Extraction taxonomy: 91.8% discriminative, direction mirrors majority → Appendix
- 42.9% redundant constraints → Appendix
- MAX-SAT ablation: 94.4% agreement with count-only → Appendix
- K/T sensitivity: isolated peaks, SC-confounded → Appendix
- Entropy: all effects in high-entropy, direction regime-dependent → Appendix

**§5.5 Remediation Analysis (600w)** — MAJOR REWRITE
- **Prompt-level (9 strategies, 6 dimensions)**: all fail (compressed, Table in Appendix)
- **Method-level (Table 4)**: ICG neutral, Contrastive harmful, Debate catastrophic
- **13 Additional Directions**: all negative (compressed 1-2 sentences each, full table in Appendix)
  - Categories: paradigm shift (PROVE), multi-round (CEGIS), filtering (DeepConf), cross-model, input diversity, solver objective, voting rule, trace filtering, iterative
- **Independence-Accuracy Trade-off (Table 5)**: SC/DP/ICG cluster κ≈0.40–0.47; Debate κ=0.15 but -18.6pp
- **Cross-model κ**: 3 families all κ≥0.41 → architecture-independent ceiling
- **Pareto frontier**: only external signal breaks through (consistent with oracle)

### §6 Discussion (0.40pp) — MODERATE REWRITE
- Oracle causally isolates extraction as binding bottleneck
- [NEW] Symbolic Confirmation Bias as unifying root cause:
  - Direct channel (voting diversity) + indirect channel (constraint homogenization) unified
  - 25+ failures explained by single mechanism: self-extraction inherits model bias
- [NEW] Process-κ implication: bottleneck deeper than answer-level metrics suggest
- Statistical evidence: 0 significant positives vs multiple significant negatives
- Published methods (DyLoS, Aristotle, FoVer) bypass self-extraction → consistent with diagnosis
- Scale: κ increases with scale (Qwen 7B→14B); 70B+ open
- Three paths: trained extractors, external provers, multi-model pipelines

### §7 Conclusion (0.25pp) — MODERATE REWRITE
- SICA across 6 models, 3 families, 3 domains, N>3,000
- [NEW] Root cause: Symbolic Confirmation Bias (4.97×)
- [NEW] Process-κ: cosine 0.69 >> answer-κ 0.41
- Independence-accuracy trade-off; 25+ interventions all fail
- Universal across 3 architectures
- Diagnostics: C0+SC + Eff-K
- Limitations + future work

---

## Part 2: Comprehensive Data Tables

### Table A: Main SICA Results (Table 1 in paper — EXISTING, no change)

| Model | Domain | n | SC (%) | SICA (%) | Δ (pp) | p | Regime |
|-------|--------|---|--------|----------|--------|---|--------|
| Mistral-7B | PW-D5 | 600 | 39.33 | 36.50 | **-2.83** | 0.014* | Type C |
| Mistral-7B | LogiQA | 200 | 51.00 | 51.50 | +0.50 | 1.000 | Intermediate |
| Mistral-7B | FOLIO (s123) | 204 | 54.41 | 57.35 | +2.94 | 0.070 | Intermediate |
| Mistral-7B | FOLIO (s42) | 204 | 55.88 | 59.31 | +3.43 | 0.092 | Intermediate |
| Mistral-7B | FOLIO (s456) | 204 | 55.88 | 55.88 | 0.00 | 1.000 | Intermediate |
| Mistral-7B | FOLIO (s789) | 204 | 54.41 | 53.92 | -0.49 | 1.000 | Intermediate |
| LLaMA-3.1-8B | FOLIO | 204 | 66.18 | 61.76 | -4.41 | 0.093 | Type A |
| LLaMA-3.1-8B | StrategyQA | 200 | 72.00 | 74.00 | +2.00 | 0.424 | Type A |
| Qwen2.5-14B | FOLIO (ICL) | 199 | 74.37 | 74.87 | +0.50 | 1.000 | Type A |
| Qwen2.5-14B | PW-D5 | 600 | 75.17 | 72.67 | **-2.50** | 0.011* | Type A |
| Qwen2.5-14B | FOLIO | 204 | 75.49 | 74.51 | -0.98 | 1.000 | Type A |
| Qwen2.5-7B | FOLIO | 204 | 75.98 | 76.47 | +0.49 | 1.000 | Type A |
| Qwen2.5-14B | LogiQA | 200 | 78.50 | 78.00 | -0.50 | 1.000 | Type A |
| Qwen3-14B | FOLIO | 204 | 84.80 | 84.31 | -0.49 | 1.000 | Type A |
| Qwen3-14B | PW-D5 | 600 | 85.00 | 85.67 | +0.67 | 1.000 | Type A |
| QwQ-32B | AIME 2024 | 22 | 72.70 | 72.70 | 0.00 | — | Degenerate |
| Qwen2.5-14B | GSM8K | 30 | 96.67 | 96.67 | 0.00 | — | Degenerate |
| **Oracle** | **FOLIO** | **204** | **75.49** | **89.71** | **+14.22** | **<0.001*** | **Oracle** |
| **Oracle** | **PW-D5** | **600** | **75.17** | **86.67** | **+11.50** | **<0.001*** | **Oracle** |

### Table B: Independence Metrics (Table 3 in paper — EXISTING, no change)

| Model | Condition | κ | Eff-K | SC (%) | Δ (pp) |
|-------|-----------|-----|-------|--------|--------|
| Qwen3 (think) | FOLIO | 0.91 | 1.09 | ~84 | ~0 |
| Qwen2.5-14B | LogiQA | 0.82 | 1.20 | 78.50 | -0.50 |
| Qwen3 | FOLIO | 0.77 | 1.26 | 84.80 | -0.49 |
| Qwen2.5-14B | FOLIO | 0.74 | 1.30 | 75.49 | -0.98 |
| Qwen2.5-7B | FOLIO | 0.66 | 1.46 | 75.98 | +0.49 |
| Mistral-7B (T=0.3) | FOLIO | 0.53 | 1.77 | 58.33 | -1.47 |
| Mistral-7B | LogiQA | 0.51 | 1.81 | 51.00 | +0.50 |
| Mistral-7B (s456) | FOLIO | 0.51 | 1.82 | 55.88 | 0.00 |
| Mistral-7B (s42) | FOLIO | 0.50 | 1.84 | 55.88 | +3.43 |
| Mistral-7B (s123) | FOLIO | 0.49 | 1.88 | 54.41 | +2.94 |
| Mistral-7B (s789) | FOLIO | 0.41 | 2.17 | 54.41 | -0.49 |
| Mistral-7B (T=0.5) | FOLIO | 0.52 | 1.80 | 58.33 | -0.98 |
| Mistral-7B (multi-T) | FOLIO | 0.48 | 1.91 | 57.84 | 0.00 |
| Mistral-7B (T=1.0) | FOLIO | 0.48 | 1.91 | 55.39 | 0.00 |
| Mistral-7B | PW-D5 | 0.21 | 3.62 | 39.33 | **-2.83*** |

### Table C: Method Interventions (Table 4 in paper — EXISTING, no change)

| Method | Target | FOLIO Δ (pp) | p | LogiQA Δ (pp) | p |
|--------|--------|-------------|---|--------------|---|
| SC baseline | — | 0.00 | — | 0.00 | — |
| ICG | Trace coupling | -1.96/+1.47 | .206 | -0.50 | .706 |
| Contrastive | Scoring bias | **-9.31** | .007** | -4.50 | .160 |
| Debate | Role diversity | **-18.63** | <.001*** | **-23.00** | <.001*** |

### Table D: κ Generalization / Independence-Accuracy Trade-off (Table 5 — EXISTING, no change)

| Model | Aggregation | κ | Eff-K | K | Acc (%) |
|-------|-------------|-----|-------|---|---------|
| Mistral-7B | Debate | 0.15 | 4.44 | 12 | 38.24 |
| | Diverse-Prompt | 0.40 | 2.21 | 12 | 54.41 |
| | Self-Consistency | 0.44 | 2.02 | 10 | 56.86 |
| | ICG | 0.47 | 1.93 | 10 | 51.96 |
| LLaMA-3.1-8B | Self-Consistency | 0.41 | 2.17 | 12 | 66.18 |
| Qwen2.5-7B | Self-Consistency | 0.66 | 1.46 | 12 | 75.98 |
| Qwen2.5-14B | Self-Consistency | 0.74 | 1.32 | 12 | 75.49 |

### Table E: Confirmation Bias Metrics (NEW — §5.2 inline, appendix detail)

| Metric | Value | Source |
|--------|-------|--------|
| Bias ratio (SICA-incorrect) | 4.97× | exp-confirmation-bias |
| Wrong constraint rate (SICA-incorrect) | 83.3% | exp-confirmation-bias |
| SICA errors overlapping SC errors | 94% | exp-confirmation-bias |
| SICA-correct gold constraint rate | 78.1% | exp-confirmation-bias |
| Correct flips (SICA right, SC wrong) | 12 | exp-confirmation-bias |
| Correct flips with minority gold support | 43% | exp-confirmation-bias |
| CEGIS R1 accuracy | 57.84% (+3.43pp) | exp-direction-d-cegis |
| CEGIS R2→R5 | oscillating, no convergence | exp-direction-d-cegis |
| Cross-model extraction Δ vs self | +0.98pp / -0.98pp | exp-059 / exp-060 |

**⚠️ DATA CONFLICT**: framing says 97.6% error overlap; registry says 94%. Must trace to experiment output.

### Table F: Process-κ Metrics (NEW — §5.3 inline, appendix detail)

| Metric | Value | Source |
|--------|-------|--------|
| Answer-level Fleiss' κ | 0.4093 | exp-wild4-process-kappa |
| CoT cosine similarity (mean) | 0.6902 | exp-wild4-process-kappa |
| Pearson r (cosine vs κ) | -0.064 | exp-wild4-process-kappa |
| Pearson p | 0.36 | exp-wild4-process-kappa |
| Convergent reasoning pairs | 9.3% | exp-wild4-process-kappa |
| Model | Mistral-7B | — |
| Dataset | FOLIO-204 | — |

**⚠️ GAP**: Single model only. Need cross-model validation (at least 1 more model).

### Table G: Selective Abstention (diagnostic, appendix)

| Metric | Value | Source |
|--------|-------|--------|
| AUROC | 0.673 | exp-direction-e-abstention |
| Δpp @ 80% coverage | +4.4 | exp-direction-e-abstention |
| Δpp @ 60% coverage | +8.8 | exp-direction-e-abstention |

### Table H: Entropy Decomposition (appendix, verified from framing)

| Exp | Model | Dataset | High-E n | High-E Δpp | Low-E n | Low-E Δpp |
|-----|-------|---------|----------|-----------|---------|----------|
| s42 | Mistral-7B | FOLIO | 78 | **+12.8** | 126 | 0.0 |
| s123 | Mistral-7B | FOLIO | 77 | **+9.1** | 127 | 0.0 |
| s456 | Mistral-7B | FOLIO | 75 | -1.3 | 129 | 0.0 |
| exp-046 | Mistral-7B | PW-600 | 267 | -4.9 | 333 | -1.2 |
| exp-036 | Qwen2.5-14B | FOLIO | 37 | -8.2 | 167 | -0.6 |
| exp-038 | Qwen2.5-14B | LogiQA | 23 | -4.3 | 177 | 0.0 |
| exp-035 | Qwen2.5-7B | FOLIO | 47 | -2.1 | 157 | 0.0 |
| exp-048 | LLaMA-8B | PW-600 | 76 | -3.9 | 104 | -1.9 |

Key finding: Low-E → Δ≈0 universally (8/8). High-E direction is regime-dependent.

### Table I: 25+ Comprehensive Intervention Results (NEW appendix table)

#### Prompt-Level (9 strategies, 6 dimensions)

| # | Strategy | Dimension | Key Result | exp_id |
|---|----------|-----------|------------|--------|
| 1 | Contrastive prompting | Prompting | disc 8.2%→6.0%, Δ=-1.1pp | exp-029 |
| 2 | Cross-model weak→strong | Architecture | 0% discriminative | exp-030 |
| 3 | Cross-model Qwen3→Mistral | Architecture | Δ=+0.98pp vs self (noise) | exp-059 |
| 4 | Cross-model Qwen14B→Mistral | Architecture | Δ=-0.98pp vs self (noise) | exp-060 |
| 5 | Generational (Qwen3-14B) | Capability | Δ=+0.49pp n.s. | exp-027 |
| 6 | Z3 feedback | Verification | 0.9% UNSAT rate, 0 real impact | exp-036 |
| 7 | Cross-trace UNSAT | Verification | 56.4% zero shared vars | exp-036b |
| 8 | Multi-temperature | Diversity | Δ=0.00pp (b=5,c=5) | exp-055 |
| 9 | Discriminative filtering | Filtering | ~8% non-disc removed, 0 gain | exp-023 |

Also tested but classified as hyperparameter analysis:
- T=0.3: Δ=-1.47pp (exp-057)
- T=0.5: Δ=-0.49pp (exp-058)  
- T=1.0: Δ=+0.49pp (exp-054)
- ICL gold FOL examples: Δ=+0.50pp n.s. (exp-044b)
- Consistency filtering: reverts to SC (exp-043)

#### Method-Level (3 methods × 2 datasets)

| # | Method | FOLIO Δ (pp) | LogiQA Δ (pp) | Failure Mode | exp_ids |
|---|--------|-------------|--------------|-------------|---------|
| 10 | ICG | -1.96/+1.47/-0.98 | -0.50 | Neutral | exp-074/074c/074d, exp-079 |
| 11 | Contrastive | -9.31 / -5.39 | -4.50 / -2.50 | Harmful | exp-075b/082, exp-080/085 |
| 12 | Debate | -18.63 / -15.20 | -23.00 / -21.50 | Catastrophic | exp-076/081, exp-078/084 |

#### Additional Directions — Wave 1-3 (13 experiments)

| # | Direction | Type | Target | Key Metric | Δ (pp) | exp_id |
|---|-----------|------|--------|------------|--------|--------|
| 13 | PROVE (code verification) | Paradigm shift | Formal proof | Code gen 15.2%, conclusive acc 50% | -1.9 | exp-direction-a-prove |
| 14 | CEGIS (iterative refinement) | Multi-round | Consistency | R1 +3.43pp, R2-R5 oscillate | no conv. | exp-direction-d-cegis |
| 15 | DeepConf (logprob filter) | Filtering | Confidence | logprob correct=-0.135 vs incorrect=-0.141 | 0 | exp-direction-b-deepconf |
| 16 | Cross-model SICA (3 families) | Cross-model | Independence | κ_cross=0.422 vs κ_within=0.532 | -0.49 | exp-cross-model-phase2 |
| 17 | Problem perturbation | Input diversity | Trace diversity | κ increased to 0.696 (anti-effect) | negative | exp-wild3-perturbation |
| 18 | MIN-UNSAT | Solver objective | Constraint selection | Mean excluded=1.3 | -6.5 | exp-wild1-max-unsat |
| 19 | κ-aware SC | Voting rule | Weighted voting | 11/11 conditions Δ=0 | 0 | exp-wild6-kappa-aware-sc |
| 20 | Z3 trace filter | Trace filtering | Quality | Precision 49.1%, 7 questions affected | -0.49 | exp-wave3-dir-i-z3-filter |
| 21 | Bootstrapped gold | Iterative | Self-improvement | R1 +2.45pp then oscillates to 52.45% | no conv. | exp-wave3-dir-j-bootstrap |
| 22 | Selective abstention | Diagnostic | Confidence | AUROC=0.673 | +4.4@80%cov | exp-direction-e-abstention |
| 23 | ASCII perturbation | Input diversity | Format diversity | κ_standard=0.39, κ_variable=0.36 | 0 | exp-wild2-ascii |
| 24 | Cross-model κ analysis | Independence | Architecture | Cross-family Δκ=0.22 >> within Δκ=0.08 | (analysis) | exp-cross-model-phase1 |

**TOTAL: 9 prompt + 3 method + 12 additional = 24 distinct interventions + variants = 25+**
**ALL negative or neutral** (selective abstention is diagnostic-only positive)

### Table J: Cross-Model κ Analysis (appendix — EXISTING)

| Model | κ (within) | Eff-K | SC (%) | Source |
|-------|-----------|-------|--------|--------|
| Mistral-7B | 0.44 | 2.02 | 56.86 | exp-077 |
| LLaMA-3.1-8B | 0.41 | 2.17 | 66.18 | exp-063 |
| Qwen2.5-7B | 0.66 | 1.46 | 75.98 | exp-061 |
| Qwen2.5-14B | 0.74 | 1.32 | 75.49 | exp-026 |

Cross-model (Mistral+LLaMA+Qwen mixed K=12):
- κ_cross = 0.422, Eff-K_cross = 2.11
- κ_within = 0.532, Eff-K_within = 1.52
- Accuracy gain: 0 (Δ=-0.49pp, p=1.0)

Key: Cross-family Δκ = 0.22 (Mistral vs Qwen-14B) >> within-family Δκ = 0.08 (Qwen-7B vs Qwen-14B)

### Table K: K and T Sensitivity (appendix)

**K Sensitivity (Mistral-7B FOLIO s42)**
| K | SC (%) | SICA (%) | Δ (pp) | p |
|---|--------|----------|--------|---|
| 4 | 54.41 | 52.94 | -1.47 | 0.629 |
| 8 | 57.35 | 56.37 | -0.98 | 0.754 |
| 12 | 54.41 | 59.31 | +4.90 | 0.013* |
| 16 | 55.88 | 57.35 | +1.47 | 0.629 |
| 20 | 57.35 | 59.31 | +1.96 | 0.219 |

Note: K=12 uses exp-033 SC (pre-tiebreaking=54.41). Paper reports post-tiebreaking SC=55.88, Δ=+3.43pp.

**T Sensitivity (Mistral-7B FOLIO)**
| T | SC (%) | SICA (%) | Δ (pp) | κ | exp_id |
|---|--------|----------|--------|-----|--------|
| 0.3 | 58.33 | 56.86 | -1.47 | 0.53 | exp-057 |
| 0.5 | 58.33 | 57.35 | -0.98 | 0.52 | exp-058 |
| 0.7 | 55.88 | 59.31 | +3.43 | 0.50 | exp-033 |
| 1.0 | 55.39 | 55.88 | +0.49 | 0.48 | exp-054 |

### Table L: Constraint Quality Comparison (appendix — EXISTING)

| Source | Z3 Compile (%) | Redundancy (%) | Disc. Rate (%) |
|--------|---------------|---------------|---------------|
| Standard SICA | 96.1% sat | 42.9% | 91.8% |
| ICG | 99.4% compile | 32.3% | — |
| Contrastive | — | — | 62.7% trivially sat |

---

## Part 3: Figure Inventory

### Main Text Figures (2)

**Figure 1: SICA Pipeline Diagram** (method.tex)
- Type: Conceptual (TikZ)
- Story: Pipeline looks like it introduces independent signal → but self-extraction inherits trace correlation (red dashed box)
- Status: EXISTS, keep as-is
- Data: Manual diagram

**Figure 2: Regime Scatter** (experiments.tex)
- Type: Statistical scatter plot
- Story: SICA Δ vs SC baseline shows narrow intermediate-SC region (~50-55%) with directional positive; outside → neutral or harmful
- Status: EXISTS, keep as-is
- Data: All Table 1 conditions (~15 points)

### Appendix Figures (1 existing + potential new)

**Figure A1: Independence-Accuracy Pareto Frontier** (appendix)
- Type: Statistical scatter
- Story: κ (x) vs Accuracy (y). SC/DP/ICG cluster at κ≈0.40-0.47; Debate at κ=0.15 but 38.24% accuracy. Pareto frontier visible. Cross-model points (LLaMA, Qwen) show architecture-independent ceiling.
- Status: EXISTS in appendix (moved from main text in Plan C)
- Data: Table D + Table J
- **CONSIDERATION**: If space allows, this could return to main text — it's the HERO finding. But 8pp is tight.

### Potential New Figures (for Director decision)

**[CANDIDATE] Figure N1: Confirmation Bias Diagram**
- Type: Conceptual or bar chart
- Story: On correct vs incorrect problems, constraint alignment with gold → 4.97× asymmetry
- Placement: §5.2 or appendix
- Assessment: Numbers are compelling inline; figure may not be necessary

**[CANDIDATE] Figure N2: Process-κ Scatter**
- Type: Statistical scatter
- Story: Per-problem cosine similarity vs answer agreement. Shows most points cluster at high cosine regardless of answer agreement.
- Placement: §5.3 or appendix
- Assessment: Would strengthen the process-κ contribution; depends on space

**[CANDIDATE] Figure N3: 25+ Interventions Summary**
- Type: Grouped bar or dot plot
- Story: All 25+ interventions with Δpp, organized by category. Visually overwhelming negative result.
- Placement: Appendix
- Assessment: Compelling visual for the "exhaustive failure" narrative

---

## Part 4: Open Issues for Director Decision

1. **Framing**: D085 vs "Selective Symbolic Verification" — evaluation submitted, awaiting R/S results
2. **94% vs 97.6%**: Confirmation bias error overlap number conflict
3. **Process-κ cross-model**: Need validation on at least 1 more model
4. **Direction R (DeBERTa)**: If positive → reframe; if negative → strengthen D085
5. **Direction F (Blind FOL)**: Tests causal chain; either outcome is informative
6. **F_A1 placement**: Pareto frontier figure in main text vs appendix
7. **New figures**: Confirmation bias diagram? Process-κ scatter? 25+ summary?
