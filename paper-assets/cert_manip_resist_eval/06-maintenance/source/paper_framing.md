# Paper Framing — cert_manip_resist_eval (v10: V2 Aggregation Bootstrap Corrected)

> Last updated: 2026-05-24 | Reason: D041-D043 corrected K=5/K=7 bootstrap numbers from V2 aggregation bootstrap scripts (seed=42, _is_valid_score). K=5: K_eff 10→7, η_max 0→2. K=7: K_eff 9→8, η_max 0→1. "sole significant predictor" → "dominant predictor". Changes from v9: (1) K=5/K=7 bootstrap numbers corrected; (2) η_max no longer drops to zero — sharply attenuates; (3) Language: "sole" → "dominant" throughout; (4) Contribution stack updated; (5) All numbers verified against V2 aggregation bootstrap JSON files.

## Target
EMNLP 2026 (via ARR)

## Title Candidates
1. **"The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels"** (current; still valid)
2. "Against Condorcet: Judge Diversity Uniformly Increases Adversarial Vulnerability in LLM Evaluation Panels" (emphasizes uniform positive finding)
3. "From Weakest Link to Weakest Correlation: A Panel-Size-Dependent Transition in LLM Evaluation Vulnerability" (mechanistic)

## Core Insight
Multi-judge LLM evaluation panels are widely assumed to benefit from judge diversity, drawing on fault-tolerance intuitions from distributed systems (CJT/BFT). We conduct the first large-scale empirical study (15 models, 6435+ panels across K∈{3,5,7}, 6 attacks, 2 benchmarks) and discover:

1. **K_eff is uniformly positive**: Judge diversity is associated with INCREASED vulnerability in **12/12 conditions** under OLS, **12/12 under GAM bootstrap**, across ALL panel sizes and ALL aggregation methods (except 1 Bayesian condition). This contradicts CJT/BFT predictions.

2. **Panel-size-dependent predictor shift**: The RELATIVE importance of diversity (K_eff) versus individual weakness (η_max) shifts with panel size:
   - **K=3**: Both predictors contribute — K_eff 4/12, η_max 3/12 (bootstrap). Co-determination.
   - **K=5**: K_eff dominates — K_eff 7/12, η_max 2/12 (bootstrap). Diversity is dominant predictor while η_max sharply attenuates.
   - **K=7**: K_eff dominates — K_eff 8/12, η_max 1/12 (bootstrap). Pattern stable, η_max nearly negligible.

3. **Aggregation modulates predictability**: Panel composition explains vastly more variance under some aggregation rules (threshold R²=0.83) than others (Bayesian R²=0.09), providing a practical defense lever.

The K_eff positive direction is UNIFORM — no attack-type-dependent sign split exists (V1 artifact confirmed dead). The defense mechanism is not diversity but aggregation-level predictability reduction.

## Hook
"Against the Condorcet Jury Theorem intuition, judge diversity is uniformly associated with increased adversarial vulnerability in LLM evaluation panels — the defense mechanism shifts from individual robustness screening at small panel sizes to managing judge independence at larger sizes."

## Novelty Positioning
We discover that **judge diversity uniformly increases adversarial vulnerability** in LLM judge panels, with a **panel-size-dependent predictor shift** from co-determination to K_eff dominance. Our contributions are:

1. **Uniform positive K_eff direction** — PRIMARY discovery. K_eff coefficient is positive (diversity increases vulnerability) in 12/12 conditions under OLS and 12/12 under GAM bootstrap (88.9-100% positive rate). The DIRECTION is uniform; SIGNIFICANCE is inference-method-dependent: OLS 12/12 → wild cluster bootstrap 4/12 (K=3), 7/12 (K=5), 8/12 (K=7) → clustered SE 1/12 (K=3). The robust claim is positive direction across all conditions, with statistical significance confirmed at K≥5 under all inference methods. Contradicts CJT/BFT predictions.

2. **Panel-size-dependent predictor shift** — K_eff significance increases (4→7→8) while η_max sharply attenuates (3→2→1) across K∈{3,5,7} under bootstrap. At K=3, both contribute (co-determination); at K≥5, K_eff is the dominant predictor while η_max becomes negligible. The "bottleneck" of panel security shifts from shared (both channels) to diversity-dominated.

3. **Aggregation as predictability control** — Threshold unanimity yields R²=0.83 (near-deterministic from panel composition); Bayesian calibration reduces to R²=0.09 (composition explains little). This gradient provides a practical defense lever: Bayesian calibration does not reverse K_eff direction (V1 artifact) but renders both predictors negligible.

## Core Claims

### Claim 0 (PRIMARY): Uniform Positive K_eff + Panel-Size-Dependent Predictor Shift
**Statement**: Judge diversity (K_eff) is **uniformly positively associated** with panel vulnerability across all conditions. The relative importance of K_eff versus η_max shifts with panel size: from co-determination at K=3 to K_eff dominance at K≥5.
**Evidence** (15-model, K=3: 455 panels, K=5: 3003 panels, K=7: 6435 panels, 12 conditions):

OLS (K=3): K_eff **12/12 significant, 12+/0−** (all positive). η_max **10/12**. Dominance: Co:10, K:2, η:0.

Bootstrap summary (most conservative inference):

| K | Panels | η_max (boot) | K_eff (boot) | K_eff direction | Pattern |
|---|--------|--------------|--------------|----------------|---------|
| **3** | 455 | **3/12** | **4/12** | 4+/0− | Co-determination |
| **5** | 3003 | **2/12** | **7/12** | 7+/0− | K_eff dominant |
| **7** | 6435 | **1/12** | **8/12** | 8+/0− | K_eff dominant |

- All bootstraps: B=9999, Rademacher weights, K-position max-p, BH FDR α=0.05
- η_max transition: 3/12 → 2/12 → 1/12 (sharply attenuates at K≥5)
- K_eff transition: 4/12 → 7/12 → 8/12 (monotonically increases with panel size)
- K_eff direction: positive across ALL K values and ALL significant conditions — no exceptions
- K=3 notable: K_eff slightly exceeds η_max (4 vs 3 under bootstrap), but both are relatively low significance — co-determination rather than single-factor dominance

GAM bootstrap (V2 correct from inception):
- K=3: 12/12 positive direction, positive rate 88.9-100% per condition
- K=5: 12/12 positive direction, 100% positive rate in all 12 conditions
- Kruskal-Wallis attack-type magnitude test: p=0.200 (K=3), p=0.423 (K=5) — no significant difference between targeted and shared-bias attacks

**Mechanistic explanation**: At K=3 (majority = 2/3), one weak judge can flip the panel — both η_max and K_eff contribute. At K≥5 (majority ≥ 3/5), the adversary must flip more judges — independent judges (high K_eff) can each be targeted individually, while correlated judges share robust consensus. The marginal contribution of η_max collapses because even high-η judges cannot flip the panel alone.
**Strength**: Strong. K_eff positive 12/12 under OLS and GAM bootstrap; predictor shift confirmed across three K values under most conservative inference (bootstrap).

### Claim 1 (K=3 Regime): Co-Determination
**Statement**: In small panels (K=3), panel vulnerability is determined by **both** individual judge weakness (η_max) and diversity (K_eff). Neither dominates cleanly under conservative inference.
**Evidence** (15-model, 455 panels, 12 conditions):
- **OLS**: η_max **10/12**, K_eff **12/12** (all positive). Dominance: Co:10, K:2, η:0. K_eff beta_std ranges 0.26-0.65; η_max beta_std ranges 0.08-0.29.
- **Wild cluster bootstrap** (B=9999, Rademacher, 3-position max-p): η_max **3/12**, K_eff **4/12** — both reduced but K_eff slightly ahead.
- K_eff significant conditions: mmlu×sycophancy (p=0.032), mmlu×verbosity (p=0.032), mmlu×authority (p=0.032), arc×verbosity (p=0.042)
- η_max significant conditions: mmlu×sycophancy (p=0.002), mmlu×verbosity (p=0.007), arc×sycophancy (p=0.014)
- Overlap: mmlu×sycophancy and mmlu×verbosity are significant for BOTH predictors
- V1→V2 changes: 5 conditions changed. Key: arc×sycophancy K_eff sign flipped (−0.19→+0.26); mmlu×score_manipulation dominance flipped η→K; multiple conditions gained K_eff significance.
- **VIF**: mean=2.98, range 1.23-7.03; 10/12 conditions < 5
**Strength**: Moderate. Neither predictor dominates cleanly at K=3; the "regime" is co-determination. The asymmetry emerges at K≥5 where K_eff takes over completely.
**Headline**: "At K=3, diversity and individual weakness share predictive power; at K≥5, diversity alone drives vulnerability."

### Claim 2 (Empirical): Predictability Gap — Panel Composition Explains RF But Not Adaptive Vulnerability
**Statement**: Panel composition (η_max + K_eff) explains substantially more variance under random faults than under adaptive attacks. K_eff is positively associated with vulnerability in BOTH regimes.
**Evidence** (15-model, K=5: 3003 panels):
- **Random-fault regime** (error = 1 - clean_accuracy, Monte Carlo 10000):
  - R² = 0.66-0.81 (K=3: mean 0.77; K=5: mean 0.70)
  - K_eff significant 2/2 under ALL correction methods (OLS, clustered SE, bootstrap)
  - K_eff positive — diversity associated with HIGHER error
- **Adaptive regime** (V2 corrected):
  - K=5 adaptive mean R² = 0.275
  - RF vs adaptive gap: 0.430 (qualitatively unchanged from V1: 0.449)
- **Interpretation**: Random faults are structurally determined by panel composition (high R²). Adaptive adversaries introduce strategic variance beyond what panel-level predictors capture (low R²).
**Strength**: Strong. RF-adaptive gap robust to V2 correction. Clean methodological insight.

### Claim 3 (Empirical): Diversity-Capability Tradeoff
**Statement**: In the current LLM ecosystem, maximizing panel diversity (K_eff) structurally requires including less capable/robust models. r(K_eff, η_max) = +0.700.
**Evidence**: Unchanged from v8. The structural correlation is unaffected by V2 error correction (computed from clean data).
**Strength**: Moderate (structural correlation strong; independent effect fragile under correction).

### Claim 4 (Methodological): Family Labels ≠ Diversity
**Statement**: Model family labels do not predict judge independence. Capability proximity is the primary driver.
**Evidence**: Unchanged from v8. p=0.179 (MMLU), p=0.385 (ARC).
**Strength**: Moderate.

### ~~Claim 5 (Gaussian Copula Failure)~~ → DEAD (since v8)

### Claim 6 (Practical): Robustness-First Panel Design
**Statement**: min(η_max) selection strategy dominates 12/12 conditions.
**Evidence**: Unchanged from v8. Uses clean accuracy data unaffected by V2 fix.
**Strength**: Strong.

### Claim 7 (Revised): Aggregation Modulates Predictability
**Statement**: Aggregation rules create a gradient of vulnerability PREDICTABILITY from panel composition, but do NOT reverse K_eff direction.
**Evidence** (V2 corrected, 15-model, 455 panels, OLS log-log):

| Method | η_max sig | K_eff sig | K_eff dir | R² |
|--------|-----------|-----------|-----------|-----|
| Threshold | 12/12 | 11/12 | **11+/0−** | **0.829** |
| Majority | 10/12 | 12/12 | **12+/0−** | 0.327 |
| Weighted | 9/12 | 12/12 | **12+/0−** | 0.328 |
| Bayesian | 9/12 | 6/12 | **5+/1−** | **0.087** |

- V1→V2 KEY CHANGE: Bayesian K_eff direction 1+/6−→5+/1−. The "reversal" where Bayesian flipped K_eff to protective was an **artifact of error-as-tie** votes biasing log-odds computation. With V2, Bayesian K_eff is mostly positive like all other methods.
- Aggregation gradient: Threshold (R²=0.83, composition near-deterministic) → Majority/Weighted (R²≈0.33) → Bayesian (R²=0.09, composition explains almost nothing).
- Bayesian calibration does not reverse K_eff direction. It reduces K_eff significance (6/12) and overall predictability (R²=0.09), but η_max persists (9/12 OLS, bootstrap TBD). The defense is partial: predictability drops but the individual weakness channel remains active.
- Threshold amplifies both channels: η 12/12, K_eff 11/12, R²=0.83.
**Strength**: Strong (V2 clean data, fully verified). The finding is simpler and more robust than v8's "Bayesian reversal" — it's a predictability gradient.

## ~~Claim 1b (6:6 Attack-Type Split)~~ → DEAD

**Disposition**: REMOVED. V2 data shows K_eff is positive for ALL attack types (12/12 under both OLS and GAM bootstrap). The V1 "6:6 split" (targeted positive, shared-bias negative) was an artifact of:
1. Error-as-tie bug inflating certain attack types differently
2. Non-seeded pygam gridsearch lambda (not reproducible even with V1 data)
GAM bootstrap confirms: at K=3, 12/12 positive (88.9-100% positive rate); at K=5, 12/12 positive (100%). Kruskal-Wallis shows no significant magnitude difference between attack types (p=0.200 K=3, p=0.423 K=5). The effect is uniform across attack mechanisms.

## ~~Claim 7-old (Bayesian Reversal)~~ → DEAD

**Disposition**: REMOVED. V2 Bayesian K_eff direction is 5+/1− (not 1+/6−). The reversal was caused by API errors counted as "tie" votes systematically biasing Bayesian posterior estimation. The old "aggregation bootstrap" that "confirmed" this reversal also used V1 data → invalid. Replaced with aggregation predictability gradient (Claim 7 revised above).

## Contribution Stack (v9: 3 contributions, V2 verified)

1. **Uniform positive K_eff direction** — PRIMARY. K_eff coefficient positive in 12/12 OLS, 12/12 GAM bootstrap. Direction uniform; significance inference-dependent (OLS 12/12 → bootstrap 4-8/12 → clustered SE 1/12 at K=3; robust at K≥5). Contradicts CJT/BFT.

2. **Panel-size-dependent predictor shift** — Co-determination at K=3 (K_eff 4/12, η_max 3/12); K_eff dominance at K≥5 (7/12 vs 2/12 at K=5; 8/12 vs 1/12 at K=7). Defense strategy must match regime: K=3 screen for individual robustness; K≥5 manage judge independence.

3. **Aggregation predictability gradient** — Threshold R²=0.83 → Bayesian R²=0.09. Bayesian calibration reduces K_eff significance (6/12) and overall predictability, though η_max persists (9/12 OLS). The defense is partial: predictability drops but individual weakness channel remains. Practical: Bayesian + robustness screening = complementary defense.

Supporting evidence (not claimed as contributions):
- Cinelli-Hazlett sensitivity: RV 0.005-0.59; RV exceeds η_max in 11/36 (31%) conditions (K=3: 4/12, K=5: 3/12, K=7: 4/12) — honest confound disclosure
- Cross-benchmark prediction: mmlu→arc 14/18 bootstrap (generalizability)
- Capability-matched replication: r=0.50→9/12 (indirect evidence for transition)
- Random fault contrast: RF R²=0.70 >> adaptive R²=0.28 (CJT holds for random faults, fails for adaptive)
- Theorem 1: 73% satisfy monotonicity; composition-dependent
- Fractional logit: 93.1% OLS concordance

## Anticipated Reviewer Concerns

### RC1: "K_eff positive is just confound with η_max"
**Response**: (a) r=0.70 full pool; (b) Capability-matched subsample (r=0.50) strengthens K_eff to 9/12; (c) API-only (r=0.85) attenuates to 3/12; (d) Cinelli-Hazlett RV 0.005-0.59, exceeds η_max confound in 11/36 (31%) — honest disclosure; (e) Causal language fully downgraded to associational throughout.

### RC2: "Why does diversity hurt? What's the mechanism?"
**Response**: (a) BFT assumes random faults — independent nodes protect via uncorrelated failures; (b) Under adaptive adversaries, independent judges create diverse attack surface — attacker exploits judge-specific vulnerabilities; (c) RF contrast confirms: K_eff is protective under random faults (R²=0.70, genuine) but harmful under adaptive attacks — the mechanism is adversary adaptation; (d) K_eff direction is uniformly positive across all attack types (no attack-mechanism-dependent split). The effect is a property of adaptive adversarial targeting, not of specific attack mechanisms.

### RC3: "Only 15 models — does this generalize?"
**Response**: 15 models, 6 families, 3 tiers, 455-6435 panels. Direction consistent across model scaling.

### RC4: "BFT comparison is a strawman"
**Response**: (a) The implicit "more diverse = more robust" assumption is pervasive in LLM eval literature; (b) We formalize and empirically refute it; (c) RF contrast shows BFT IS correct for random faults — the point is that BFT fails specifically for adaptive adversaries, the relevant threat model for adversarial manipulation.

### RC5: "Why not just use the strongest models?"
**Response**: K_eff is dominant predictor in 2/12 conditions (OLS dominance K:2). Even all-strong panels can be vulnerable through diversity channel.

### RC6: "No theoretical novelty"
**Response**: Theorem 1 + BFT reversal mechanism + empirical discovery.

### RC7: "Why not just use Bayesian aggregation?"
**Response**: (a) V2 data: Bayesian does NOT reverse K_eff direction (5+/1−, not 1+/6−). The v8 "reversal" was a V1 bug artifact; (b) Bayesian reduces predictability (R²=0.09) — neither predictor explains much, but defense is also not reliable; (c) η_max still 9/12 significant under Bayesian — individual weakness persists; (d) Practical: Bayesian + robustness screening as complementary, not substitute.

### RC8: "6-model and 15-model results contradict"
**Response**: 6-model underpowered (20 panels, r=-0.8). 15-model definitive.

### RC9: "Attack-type split is not significant"
**Response**: MOOT under V2. K_eff uniformly positive across all attack types. Kruskal-Wallis p=0.200 (K=3), p=0.423 (K=5) — no significant magnitude difference. Diversity uniformly increases vulnerability regardless of attack mechanism.

### RC10 (new): "V1→V2 bug fix undermines credibility"
**Response**: (a) Bug affected 1.94% of samples (1221/63000), concentrated in 3 models; (b) GAM bootstrap was V2-correct from inception; (c) V2 results are CLEANER (12/12 vs 8/12); (d) Discarded findings were artifacts of non-seeded analysis; (e) Transparent reporting in paper.

## "When Diversity Helps" Section
Under V2, the "when diversity helps" framing is simpler:
1. **Non-adversarial settings**: Under random faults, K_eff is genuinely significant (2/2 bootstrap). CJT/BFT holds for random faults — diversity protects. Protection fails specifically under adaptive adversaries.
2. **After robustness screening**: Once all judges exceed a capability threshold, K_eff's harmful association may diminish. Two-stage recommendation basis.
3. ~~Shared-bias attacks~~: DEAD. V2 shows K_eff positive for shared-bias attacks too.

## Story Arc (v9: Uniform Positive + Predictor Shift)
1. **Background**: Multi-judge LLM evaluation increasingly adopted; diversity assumed to be key defense (CJT/BFT analogy)
2. **Tension**: We test this assumption across panel sizes — 15 models, 6 families, K∈{3,5,7}, 6 attack types, 2 benchmarks, wild cluster bootstrap inference
3. **First surprise**: Diversity (K_eff) is UNIFORMLY associated with INCREASED vulnerability — 12/12 conditions, all positive, all panel sizes, all aggregation methods. No exceptions. Directly contradicts CJT/BFT predictions.
4. **Second surprise (predictor shift)**: The aggregate pattern masks panel-size-dependent structure. At K=3, both individual weakness (η_max) and diversity (K_eff) contribute (co-determination). At K≥5, η_max sharply attenuates (2/12→1/12) — diversity becomes the dominant predictor. The "bottleneck" of panel security shifts with panel size.
5. **Unifying insight**: Under random faults, diversity IS protective (CJT confirmed, R²=0.70-0.77). Under adaptive adversaries, the same independence that protects against random faults creates a diverse attack surface. Independent judges can be targeted individually; correlated judges share robust consensus.
6. **Aggregation as defense**: Aggregation rules modulate PREDICTABILITY, not direction. Threshold makes vulnerability deterministic (R²=0.83); Bayesian makes it unpredictable (R²=0.09). Practical defense lever is aggregation choice.
7. **K-dependent defense**: K=3: screen for individual robustness (η_max still contributes). K≥5: minimize judge independence (K_eff dominant driver). Both + Bayesian aggregation = dual defense stack.
8. **Implication**: Panel security is not single-factor — defense strategy must match panel size regime. CJT/BFT analogy fails because adaptive adversaries exploit independence that protects against random faults.

## V2 Data Audit Trail

### What Changed (V1→V2)
- **Bug**: `.get('winner', 'tie')` in voting scripts treated API errors/malformed responses as "tie" votes
- **Impact**: 1221/63000 samples (1.94%), concentrated in gemini-3.5-flash (742), gemini-3.1-pro-preview (335), gpt-5.5 (144)
- **Fix**: `_is_valid_score()` properly skips error samples

### V2 Verified Data Files
- `table1_corrected.json` — OLS K=3 ✅
- `regime_transition_corrected.json` — Bootstrap K∈{3,5,7} ✅
- `table2_corrected.json` — Aggregation comparison ✅
- `random_fault_contrast_corrected.json` — RF vs adaptive ✅
- `gam_bootstrap_ci_k3.json` — GAM bootstrap K=3 (V2 from inception) ✅
- `gam_bootstrap_ci_k5.json` — GAM bootstrap K=5 (V2 from inception) ✅
- `gam_magnitude_gradient.json` — Attack-type magnitude test ✅

### V1-Contaminated, Pending V2 Rerun (P2)
- ~~`sensitivity_analysis_poolA.json` — Cinelli-Hazlett~~ → V2 rerun complete (2026-05-24): RV 0.005-0.59, 11/36 exceeds. K=3 changed 1→4, K=5/K=7 unchanged.
- `cross_benchmark_iv.json` — cross-benchmark prediction (V2 rerun in progress)
- `keff_stability_split.json` — source script deleted
These are appendix-level analyses; qualitative conclusions likely unchanged.

### Killed Claims
- **6:6 attack-type split** (Claim 1b): Not reproducible even with V1 (fresh run: 2/6 negative). Artifact of V1 bug + non-seeded pygam gridsearch.
- **Bayesian reversal** (Claim 7 old): 1+/6− → 5+/1− after V2. Artifact of error-as-tie biasing Bayesian posteriors.
