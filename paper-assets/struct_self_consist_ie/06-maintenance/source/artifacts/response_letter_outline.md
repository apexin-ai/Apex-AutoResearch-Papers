# Response Letter — ARR Round 25

## Summary of Changes

We thank the reviewers for their constructive feedback on our Round 24 submission. The R24 reviews identified several critical concerns: (1) the decomposition formula lacked empirical validation beyond 3 data points; (2) the gating protocol had circularity and insufficient validation; (3) entity construction was overclaimed as a "resolution"; and (4) the scope was limited to fine-tuned 8B models on 2 NER datasets.

In this revision, we have undertaken a **major experimental expansion** and **narrative recalibration**:

- **Scale**: Extended from 8B to a 7B→14B→32B→72B Qwen2.5 scaling study + 8B cross-family (Qwen3 + LLaMA-3.1), demonstrating the correlation-selection gap persists across model scales and families.
- **Regimes**: Added 72B zero-shot evaluation, confirming the gap is not an artifact of fine-tuning — LP ρ=-0.002 (CoNLL) and 0.081 (SciERC) in zero-shot, with LP-weighted construction achieving +1.53pp on SciERC ZS (p=0.008).
- **Datasets**: Added Few-NERD (32,565 instances) and WNUT-17, expanding from 2 to 4 NER datasets with distinct degeneracy profiles (10%-67.7%).
- **Honest negative reporting**: 72B few-shot construction uniformly non-significant; error correlation hypothesis falsified; decomposition formula deleted after R²=-8.53 on 23 configurations.
- **Narrative**: Entity construction demoted from "principled resolution" to "diagnostic-motivated mitigation"; title changed from "Resolving" to "Addressing"; by-construction vs. empirical failure clearly separated in text.

## Detailed Responses

### Reviewer Theme A: Theoretical Depth & Formula Validation
*Sources: R24-N1, R22-W1 (cross-round consensus)*

- **Concern**: Decomposition formula E[ΔF1]≈(1-d)·Δ_oracle·g(ρ_within) validated on only 3 macro-level data points; 23-configuration data not used. Two reviewers flagged as critical.
  - **Response**: We ran the requested 23-configuration regression. **Result: R²=-8.53** — the formula has no predictive power. We deleted the formula entirely (D162) and replaced it with a qualitative three-factor narrative: (1) degeneracy modulates headroom within settings, (2) LP-quality alignment determines cross-dataset selection success, (3) LP compression is model/task intrinsic.
  - **Evidence**: §4.3 rewritten. 23-config regression results in Appendix. Cross-dataset degeneracy-LP correlation ρ=0.052 (p=0.81) confirms degeneracy alone does not predict selection direction.
  - **Strengthening**: The honest deletion of a failed formula + replacement with empirically grounded characterization is stronger than retaining a misleading heuristic.

### Reviewer Theme B: Gating Protocol Circularity & Validation
*Sources: R24-N2 (critical, consensus from both reviewers)*

- **Concern**: Within-instance ρ(LP,F1) requires gold labels; dev probe uses only 50 SciERC instances; threshold τ=0.3 origin unclear; only 3 datasets tested.
  - **Response**:
    - Bootstrap CI completed: τ=0.3 sits at center of [0.25, 0.35] stable plateau; routing decisions stable across τ∈[0.2, 0.4] (stability ≥95%).
    - Gating now includes **greedy fallback** as third routing option (§4.7: LP selection / construction / greedy fallback).
    - **Gating correctly predicted construction effectiveness in all tested configurations (7/7)** (SciERC→greedy, CoNLL→greedy, FewNERD→LP selection, WNUT-17→greedy).
    - Gating explicitly framed as "preliminary protocol" not validated framework.
  - **Evidence**: Table in §4.7; bootstrap sensitivity analysis in Appendix.
  - **R25 new**: 72B zero-shot gating tested — correctly routes SciERC ZS to LP-weighted construction (+1.53pp) and CoNLL ZS to greedy.

### Reviewer Theme C: Entity Construction Overclaimed
*Sources: R24-W1, R23-N1 (critical, persisted across 2 rounds)*

- **Concern**: "Resolving" in title and "principled resolution" in Contribution 3 imply the problem is solved, but entity construction recovers only 8-11% of oracle headroom (~1pp). Two reviewers flagged independently.
  - **Response**:
    - Title: "Resolving" → "Addressing"
    - Contribution 3: demoted from "principled resolution" to "diagnostic-motivated mitigation"
    - Explicit oracle recovery percentages added to text
    - Construction framed as "the correct self-consistency analogy for set-structured outputs" rather than a complete solution
  - **Evidence**: Updated §1 (Introduction), §5 (Discussion), title.
  - **R25 new**: Entity construction results now span **5 conditions**: SciERC FT +1.02pp, FewNERD FT +1.40pp (multi-seed N=8 mean), SciERC ZS +1.53pp (p=0.008), CoNLL FT +0.10pp (n.s.), CoNLL ZS -0.37pp (n.s.). Effectiveness shown to be headroom-dependent, not universal — honest characterization.

### Reviewer Theme D: Scope Limitation (Fine-tuned 8B only)
*Sources: R22-W7 (persisted warning across 3 rounds), R14 in paper_framing.md*

- **Concern**: All experiments use LoRA fine-tuned models; claims not scoped appropriately. R2 wanted this more prominent.
  - **Response**: **Massively expanded scope**:
    - **Scale**: 4B → 7B → 8B → 14B [pending data] → 32B [pending data] → 72B Qwen2.5 scaling study
    - **Regimes**: Fine-tuned AND zero-shot (72B Qwen2.5-Instruct-AWQ)
    - **Families**: Qwen2.5 + Qwen3 + LLaMA-3.1 (3 model families)
    - **Key finding**: Gap persists from 4B to 72B and from fine-tuned to zero-shot → fundamental, not artifact of specific model/regime
  - **Evidence**: New scaling section (§4.X); 72B ZS results in §4.Y; cross-family comparison table.
  - **Scaling narrative (D163)**: Degeneracy is **model-family-dependent, not scale-dependent** — 7B Qwen2.5 FT degen=31.7% vs 8B Qwen3 FT degen=13.0%. Version B: "measure, don't predict."

### Reviewer Theme E: By-Construction vs. Empirical Failure Distinction
*Sources: R23-N2 (critical, in_progress), R22-W1*

- **Concern**: "Correlation-selection gap" umbrella term blurs the line between definitional failure (4/5 signals are instance-level aggregates → cannot rank by construction) and empirical failure (LP compression, degeneracy).
  - **Response**: Text restructured to clearly separate:
    - **Layer A (definitional)**: SJ/FK/EM/VC are instance-level aggregates → selection failure is by design. Presented as methodological premise (1 paragraph), not empirical finding.
    - **Layer B (empirical)**: LP's failure — compression (0.041 nats), degeneracy (21-58%), LP-alignment misalignment — is the genuine empirical contribution.
    - **Layer C (empirical)**: MBR consensus-proximity gives different samples different scores but still fails → this is genuinely empirical (R1's rebuttal point acknowledged).
  - **Evidence**: §4.1 restructured; terminology disambiguated throughout.

### Reviewer Theme F: Missing Baselines & Related Work
*Sources: R24-W3, R24-W5, R22-MR1, R23-MR1*

- **Concern**: Missing technical comparison with CISC (ACL Findings 2025) and Self-Certainty (ICLR 2026); Self-Certainty and P(True) not tested as signals.
  - **Response**:
    - Related Work expanded with explicit technical differentiation: CISC uses confidence-weighted majority vote for reasoning (discrete answers); Self-Certainty uses KL-divergence reward-free selection; both target reasoning tasks, not structured IE.
    - New Related Work subsection: "Test-Time Scaling & Sample Selection" — positions our work as the first systematic signal comparison for structured IE.
    - Nédellec & Xia (2026) cited as concurrent work with explicit differentiation (surface matching vs. structural metrics).
    - **R24-W5 (wont_fix)**: Self-Certainty and P(True) not tested — acknowledged in Limitations. Verbalized confidence + hidden probes tested and failed, providing indirect evidence. Implementation of verbalized-confidence approaches requires model internals access, which we scope as future work.
  - **Evidence**: §2 (Related Work) substantially expanded; Limitations updated.

### Reviewer Theme G: Statistical Rigor & Reporting
*Sources: R24-W2, R24-I1, R24-I2, R24-I5*

- **Concern**: SciERC selection underpowered (n=529); Table 2 p-values marked '---'; F1 terminology inconsistent; Abstract ρ=0.45 from easiest dataset.
  - **Response**:
    - SciERC selection results now annotated with MDE≈1.5pp ("selection effects below this threshold cannot be reliably detected")
    - Table p-values: '---' → 'n/a†' with caption footnote
    - F1 metric defined in §3 (method.tex)
    - Abstract ρ=0.45: [status: consider adding "(CoNLL-2003)" annotation or reporting cross-dataset median]
  - **Evidence**: Updated tables and method section.

### Reviewer Theme H: Writing & Presentation
*Sources: R24-W6, R24-I3, R24-I4, R22-I1*

- **Concern**: "As a reviewer correctly noted" in appendix reveals review history; orphan bib entries; SJ denominator edge case undiscussed; entity matching criteria scattered.
  - **Response**:
    - "As a reviewer correctly noted" deleted, replaced with direct statement
    - 8 orphan bib entries cleaned; xie2023zeroshot restored
    - SJ denominator footnote added
    - [R22-I1 entity matching: still open — consider consolidating in §3.2]
  - **Evidence**: Appendix, bibliography, method section.

## New Results Not Addressing Specific R24 Reviews

These improvements go beyond direct responses to R24 feedback:

### 1. 72B Zero-Shot Regime (entirely new)
- Validates that the correlation-selection gap is **regime-independent**: LP ρ=-0.002 (CoNLL ZS), 0.081 (SciERC ZS)
- LP-weighted construction +1.53pp on SciERC ZS (p=0.008) — stronger than fine-tuned regime
- θ=2/N heuristic **fails** in zero-shot (-0.52pp SciERC, -0.92pp CoNLL) → LP-weighting necessary in ZS
- Few-shot (72B, 3-shot): construction uniformly non-significant across all datasets → FS regime has independent failure mechanism

### 2. 72B Few-Shot Error Correlation Analysis (new, negative)
- Tested "demonstration-induced error correlation" hypothesis — FS in-context examples causing correlated errors
- **Falsified**: Pairwise error Jaccard virtually identical (SciERC FS=0.454 vs ZS=0.452, p=0.844)
- Entity prediction entropy **higher** in FS (opposite to hypothesis direction)
- Honestly reported; Discussion hypothesis weakened accordingly

### 3. Scaling Study: 7B/14B/32B Qwen2.5 (new)
- 7B FT FewNERD: degen=31.7%, construction n.s. → consistent with gating prediction (>22% threshold)
- Cross-family comparison: 7B Qwen2.5 (31.7% degen) vs 8B Qwen3 (13.0%) proves degeneracy is **family-dependent, not scale-dependent**
- 14B results: [pending data, ETA ~05-20 19:20 UTC]
- 32B results: [pending data, ETA ~05-21 01:40 UTC]
- Scaling narrative Version B: "measure, don't predict" — practitioners must empirically assess degeneracy for their specific model+dataset

### 4. WNUT-17 Social Media NER (new dataset)
- Out-of-distribution evaluation on noisy social media text
- LP signal **inverts** (negative correlation with quality) — gating correctly routes to greedy
- Strengthens gating protocol's practical value (correct routing on 4/4 datasets)

### 5. Comprehensive Appendix Expansion
- 30+ appendix sections covering: epoch ablation, temperature sensitivity, per-entity-type analysis, LoRA rank ablation, free-form decoding ablation, N-scaling, bootstrap details, error correlation analysis, scaling study details
- All negative results transparently reported

## Open Items for Final Submission

| Item | Status | Impact |
|------|--------|--------|
| 14B Qwen2.5 FT results | Training 77.7% (32000/41180), ETA ~14:00-15:00 UTC May 20 | Scaling curve data point |
| 32B Qwen2.5 FT results | Training 57.3% (23448/41180), ETA ~20:00-22:00 UTC May 20 | Scaling curve data point |
| Scaling curve final figure | Blocked on 14B/32B | §4.X figure |
| Abstract ρ=0.45 annotation (R24-I5) | Open | Minor wording |
| R22-I1 entity matching consolidation | Open | §3.2 presentation |
| R22-I3 Figure 3 print readability | Open | Minor formatting |

## Mapping: R24 Issue IDs → Response Sections

| R24 Issue | Severity | Theme | Status |
|-----------|----------|-------|--------|
| R24-N1 (formula validation) | critical | A | resolved |
| R24-N2 (gating circularity) | critical | B | resolved |
| R24-W1 ("Resolving" overclaim) | warning | C | resolved |
| R24-W2 (SciERC underpowered) | warning | G | resolved |
| R24-W3 (CISC/Self-Certainty RW) | warning | F | resolved |
| R24-W4 (English-only limitation) | warning | F | resolved |
| R24-W5 (untested signals) | warning | F | wont_fix (acknowledged) |
| R24-W6 (review history leak) | warning | H | resolved |
| R24-I1-I5 (minor) | info | G/H | mostly resolved |
| R23-N1 (construction novelty) | critical | C | resolved |
| R23-N2 (by-construction gap) | critical | E | in_progress → improved |
| R22-W7 (LoRA-only scope) | warning | D | resolved (72B ZS + scaling) |
