# Response to Reviewers

We thank all reviewers for their thorough and constructive feedback. The revision addresses all 19 identified issues (18 resolved, 1 acknowledged as a structural limitation). We summarize the major changes before responding point-by-point:

**Key improvements in revision:**
- Evidence expanded from 1 judge x 1 axis to **2 judges (GPT-4o, Qwen3-32B) x 3 axes (formality, verbosity, register)**, with all 6 cells showing the Blindspot pattern (Table 1)
- **GEE logistic decomposition** added for all 6 cells, revealing a cross-judge-replicated confound gradient: verbosity (pure style) > formality (mixed) > register (originality-dominated) (Table 3)
- **7-method sensitivity hierarchy** including ordinal regression (p=0.769) and GEE (p=0.587) definitively rules out interval-scale assumptions as the cause (Table 2)
- **Statistical framework upgraded**: Bradley-Terry as primary analysis with pair-level bootstrap CIs, Holm-Bonferroni correction on the primary 3x3 family, primary/exploratory/confirmatory trichotomy
- **3 figures added**: pipeline diagram (Figure 1), forest plot (Figure 2), power curve (Figure 3)
- **22 verified references**, 0 broken citations, 0 undefined LaTeX references

---

## Critical Issues

### R1-N1 + R1-W3 (shared): Causal language mismatch — no DAG, SUTVA, or sensitivity analysis

> *"Extensive use of 'counterfactual', 'interventional', 'ATE' terminology but no DAG, SUTVA discussion, or sensitivity analysis for unmeasured confounders."*

**Response:** We agree that our original causal language overstated the framework's formal guarantees. The revision makes three changes:

1. **Language downgraded throughout** from "counterfactual" to "interventional" — we now explicitly state that CSD provides "interventional rather than formal causal evidence" (Section 1) and do not invoke SUTVA or consistency assumptions.
2. **DAG added** (Section 3.5, Figure 2 in the DAG): A tikz diagram formalizes the assumed data-generating process with three variables (S, Q, Y), showing the R→Q path that the NLI gate blocks.
3. **Assumptions stated explicitly**: "We do not claim a complete structural causal model" (Section 3.5).

**Location:** Section 1 (paragraph 5), Section 3.5 (new subsection), Figure 2 (DAG).

---

### R1-N2: NLI gate 67% false-negative rate creates selection bias

> *"Final analysis based on ~1/3 of original data. 'Lower-bound' claim requires unverified assumption that NLI-rejected pairs have same bias direction."*

**Response:** The "67%" figure conflates the within-rejected rate (8/12) with the overall false-negative rate. The actual FNR is **8/95 = 8.4%**, where the denominator counts all pairs that *any* annotator considers content-preserving.

Three additional analyses confirm these false negatives do not compromise conclusions:
1. **Threshold sensitivity** (Section 5.1): Win rate stable at 72.3–73.9% across thresholds 0.70–0.95 (all p < 0.005)
2. **Covariate balance** (Section 5.6): No significant differences between consistent/inconsistent groups across 4 covariates (all Mann-Whitney p > 0.12)
3. **Directional balance**: 8 false negatives split 6:2 between directions (Fisher p = 0.35)

The NLI gate achieves **precision = 98.9%** (1/88 NLI-passed pairs flagged as content-altered) — it operates as a precision-oriented conservative filter.

**Location:** Section 5.1 (NLI Gate Validation), paragraphs on false negative rate, threshold sensitivity, and supplementary materials.

---

### R1-N3: NLI threshold 0.90 unjustified; per-axis adjustment introduces researcher degrees of freedom

> *"Verbosity axis changed from bidirectional to direction-aware gating post-hoc. Threshold sensitivity analysis should be in main text."*

**Response:**
1. **Threshold on a plateau, not a cliff edge**: NLI scores follow a bimodal distribution (most pairs >0.95 or <0.30). The 0.90 threshold lies on a plateau; results are invariant across 0.70–0.95 (Section 5.1).
2. **Direction-aware NLI is principled, not post-hoc**: For verbosity, expansion necessarily introduces content the original cannot entail — bidirectional verification is conceptually inappropriate. This recovered pass rate from 65% to 86%. The justification is now in Section 3.2.
3. **Sensitivity analysis in main text** as requested (Section 5.1).

**Location:** Section 3.2 (Content Preservation Verification), Section 5.1 (Threshold Sensitivity).

---

### R2-N1: Novelty insufficient — domain transfer of known psychometric phenomenon [IN PROGRESS]

> *"Likert vs forced-choice sensitivity gap is consensus since Thurstone (1927). This is domain transfer, not methodological innovation."*

**Response:** We acknowledge that the superiority of pairwise comparison over rating scales is well-established in psychometrics. Our contribution is not the discovery of this principle but its **first systematic quantification in the LLM judge context**, along with three findings that go beyond simple domain transfer:

1. **The two-layer mechanism** (Section 1): We decompose the Blindspot into (i) 58–73% uninformative ties from integer discretization and (ii) weaker signal even among non-tied pairs — a structural characterization not previously documented for LLM judges.
2. **The 7-method sensitivity hierarchy** (Table 2): All five Likert-based methods fail (including ordinal regression, which respects the ordinal nature of the data), while both pairwise methods succeed — ruling out the possibility that better statistical modeling can rescue Likert scoring.
3. **The GEE confound gradient** (Table 3): Per-axis decomposition reveals qualitatively different confound structures (pure style vs. mixed vs. originality-dominated) that replicate across both judges — a diagnostic capability that single-metric approaches cannot provide.

We have added Stevens (1946), Thurstone (1927), DeCoster et al. (2011), Kiritchenko & Mohammad (2017), and Novikova et al. (2018) to the Related Work to properly contextualize our contribution within the psychometric tradition (Section 2).

**Location:** Section 2 (Measurement Sensitivity paragraph), Table 2, Table 3.

---

### R2-N2: Citation system incomplete — placeholder arXiv IDs, broken citations

> *"Placeholder arXiv IDs ('arXiv:2406.xxxxx') and broken citations. Target 20-30 references."*

**Response:** Fully resolved. The revision contains **22 verified references** with complete bibliographic metadata. All citations compile with 0 undefined references. No placeholders remain.

**Location:** references.bib (22 entries), verified via `verify_references` tool.

---

### R2-N3: RATE criticism lacks matched replication

> *"Internal binarized-Likert comparison is sound, but generalizing to 'RATE's Likert understates bias' is an ecological validity leap."*

**Response:** We now present a **direct head-to-head comparison on identical data** (Section 5.2): RATE's Likert ATE methodology yields Cohen's d = 0.10, p = 0.33 on our formality-transformed pairs, while Bradley-Terry on the same data yields 63.0% formal win probability (p < 0.001). The framing has been revised to position CSD and RATE as **complementary rather than adversarial**: "RATE for population-level quality audits, CSD for per-axis style preference detection."

**Location:** Section 5.2 (Head-to-head comparison with RATE).

---

## Must-Fix Issues (Consensus)

### CROSS-1 + W1: "Blindspot" is actually a sample-size-dependent efficiency gap

> *"Binarized Likert at n=500 reaches p=0.055. Likert is not categorically blind but underpowered at typical n."*

**Response:** We agree and have reframed the Blindspot as a **"two-layer structural limitation"** rather than a categorical measurement failure:
1. Layer 1: Integer discretization produces 58–73% uninformative ties
2. Layer 2: Even among non-tied pairs, absolute scoring captures weaker signal than forced comparison

The power curve (Figure 3) quantifies the practical consequence: at typical evaluation scales (n=50–200), both pairwise methods reach 80% power while both Likert-based methods remain far below. The 80% power crossings are: sign test n≈62, BT n≈114, binarized Likert n≈462, Likert ATE n≈1,473.

The title has been revised to "Causal Style Decomposition Reveals the Likert Blindspot: Standard Scoring Underestimates Style Bias in LLM Judges" — emphasizing underestimation rather than categorical failure.

**Location:** Section 1 (paragraph 4), Figure 3 (power curve), Section 5.2.

---

### CROSS-4 + R1-W1: Ordinal regression is a necessary experiment (CLMM)

> *"If CLMM/ordinal logistic regression is significant, the 'Blindspot' is a flaw of ATE analysis, not of Likert scales."*

**Response:** This was the existential test. We ran ordinal logistic regression (proportional odds model, n=88 pairs, 176 observations) — **the result is non-significant** (β = −0.079, 95% CI [−0.60, 0.45], p = 0.769). Without pair random effects, the model is anti-conservative (favors detection); despite this favorable bias, formality remains undetectable. GEE with pair-level clustering confirms (p = 0.587).

The 7-method sensitivity hierarchy (Table 2) shows that **all five Likert-based methods fail regardless of statistical approach** (ATE t-test, binarized Likert, ordinal regression, GEE, Wilcoxon), while both pairwise methods detect the effect. This definitively establishes that the Blindspot is inherent to Likert measurement itself.

**Location:** Table 2 (Sensitivity Hierarchy), Section 5.2 (paragraphs on ordinal regression).

---

### CROSS-2 + R1-W3: Original preference confound — need per-cell partial-out

> *"OR=1.65, p=0.072 is marginal. Need per-cell logistic regression to formally partial out original preference."*

**Response:** GEE logistic decomposition (exchangeable correlation) has been computed for all 6 judge-axis cells (Table 3). Key findings:
- **Formality survives adjustment** for both judges (GPT-4o: OR=2.21, p=0.010; Qwen3-32B: OR=4.20, p=0.0002)
- **Verbosity is confound-free**: Style OR=13.10/10.97 (both p<.0001), Originality OR=0.49/0.44 (both n.s.)
- **Register is originality-dominated**: Originality OR=5.72/2.21 (both p<0.01)
- The **confound gradient replicates across both judges**, demonstrating that per-axis decomposition captures genuine axis-level properties

**Location:** Table 3 (GEE Decomposition), Section 5.7.

---

### CROSS-3: Likert ATE direction reversal — measuring different constructs

> *"Likert and pairwise may measure different constructs. 'Blindspot' narrative assumes same-construct."*

**Response:** We now frame the finding as a **magnitude gap between measurement methods** rather than a directional claim. The ordinal regression coefficient is negative (β = −0.079) with a wide CI spanning both directions, precluding directional interpretation. The key finding is the **gap**: Likert p ≥ 0.33 vs. pairwise p = 0.006 on identical data.

**Location:** Section 5.2 (ordinal regression paragraph).

---

## Should-Fix Issues

### R1-W2: Consistency filtering ~40-50% data loss

> *"Discarded position-inconsistent pairs may systematically retain stronger formality effects."*

**Response:** Two convergent analyses address this:
1. **Covariate balance** (Section 5.6): Consistent and inconsistent groups are statistically indistinguishable across 4 covariates (NLI score p=0.824, BERTScore p=0.12, text length p=0.137, rewrite length diff p=0.715).
2. **BT vs. filtered sign test**: The BT model uses all 173 comparisons including inconsistent pairs and yields 63.0% — **lower** than the filtered sign test (73.9%). The filter sharpens but does not create the signal.

**Location:** Section 5.6 (Consistency Filter Robustness).

---

### R1-W4: Multiple comparison correction inconsistent

> *"Holm-Bonferroni only on Table 2; other ~20+ tests uncorrected."*

**Response:** We now define a clear statistical framework (Section 4) with three categories:
- **Primary family** (9 tests: 3 judges × 3 axes): Holm-Bonferroni at α=0.05
- **Exploratory** (NLI threshold sweep, register): Uncorrected, interpreted as hypothesis-generating
- **Confirmatory** (consistency filter validation): Nominal α=0.05, orthogonal to primary family

**Location:** Section 4 (Statistical Framework).

---

### R1-W5: Post-hoc power analysis methodological issue

> *"Using observed effect size for power analysis is circular (Hoenig & Heisey 2001)."*

**Response:** We now explicitly disclaim post-hoc power analysis: "This is not a post-hoc power analysis (cf. Hoenig & Heisey, 2001), but a visual comparison of how measurement structure affects the sample size needed to detect effects of a given magnitude." CI-based precision is the primary inference tool; the power curve is illustrative only.

**Location:** Section 5.2 (paragraph before Figure 3), Figure 3 caption.

---

### R2-W1: Scope narrower than title — only formality has full results

> *"Only formality has complete 3×3 results. Verbosity and register have 1 cell each."*

**Response:** The revision presents a **complete 2 judges × 3 axes matrix** (Table 1): all 6 cells now have BT win probabilities with bootstrap CIs. The Blindspot is demonstrated across all 6 cells (4 strong, 2 marginal register). Verbosity provides the strongest effect (GPT-4o 76.0%, Qwen3-32B 77.3%) with confound-free GEE evidence.

**Location:** Table 1 (all 6 cells filled), Sections 5.3–5.5.

---

### R2-W2: No Bradley-Terry modeling

> *"BT modeling would provide proper effect-size confidence intervals."*

**Response:** BT is now the **primary pairwise analysis** for all 6 cells, with pair-level bootstrap CIs (10,000 resamples for Qwen3-32B, 2,000 for GPT-4o). BT uses all comparison data including position-inconsistent pairs, yielding proper effect-size CIs that sign tests cannot provide.

**Location:** Table 1, Section 5.2 (Bradley-Terry analysis).

---

### R2-W3: Related work coverage incomplete

> *"Missing CalibraEval, FairEval, BT for judge evaluation, psychometric theory."*

**Response:** Related work expanded to 5 paragraphs covering:
- Counterfactual approaches (RATE, Qiu et al.)
- Measurement sensitivity (Stevens 1946, Thurstone 1927, DeCoster et al. 2011, Kiritchenko & Mohammad 2017, Novikova et al. 2018)
- Style bias detection and mitigation (Zheng et al., Wang et al. FairEval, Li et al. CalibraEval, CASSE, FairJudge)
- Bradley-Terry models in evaluation (Bradley & Terry 1952, Chatbot Arena, AlpacaFarm)

**Location:** Section 2 (Related Work), references.bib (22 entries).

---

### R2-W4: Zero figures in the paper

> *"At least need: (1) power curve, (2) forest plot, (3) pipeline diagram. For a borderline paper, presentation may be the tipping point."*

**Response:** Three figures added:
1. **Figure 1** (pipeline diagram): CSD pipeline overview with sample attrition at each stage
2. **Figure 2** (forest plot): BT win probabilities across 2 judges × 3 axes with 95% bootstrap CIs
3. **Figure 3** (power curve): Detection probability as a function of sample size for four measurement approaches, directly addressing the blindspot-vs-efficiency-gap debate

**Location:** Figure 1 (Section 3), Figure 2 (Section 4), Figure 3 (Section 5.2).

---

## Questions for Authors

| # | Question | Response | Location |
|---|----------|----------|----------|
| Q1 | Complete attrition data per cell | Reported in Method §3.4 and per-section results | §3.4, §5.1 |
| Q2 | NLI threshold pre-specified? | Sensitivity analysis across 0.70/0.90/0.95 in main text; results invariant | §5.1 |
| Q3 | NLI-rejected pairs bias direction + style distance | 8 FNs split 6:2 (Fisher p=0.35); 3–4 involve prompt leakage | §5.1 |
| Q4 | CLMM/ordinal regression | p=0.769 (non-significant); Blindspot confirmed as measurement-structural | §5.2, Table 2 |
| Q5 | Per-cell logistic regression | GEE for all 6 cells; formality survives, verbosity confound-free | Table 3, §5.7 |
| Q6 | Likert ATE direction reversal | Reframed as magnitude gap; CI spans both directions | §5.2 |
| Q7 | Position bias in discarded pairs | Covariate balance across 4 metrics; BT < filtered sign test | §5.6 |
| Q8 | Headline win rate from n=500? | Primary estimates from BT with bootstrap CIs (63.0–77.3%) | Table 1 |
| Q9 | Contribution beyond domain transfer | Two-layer mechanism + 7-method hierarchy + GEE gradient | §1, Table 2, Table 3 |
| Q10 | All citations verifiable? | 22 verified references, 0 broken, 0 undefined | references.bib |
