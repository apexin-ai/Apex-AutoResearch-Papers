# Rebuttal Draft v1 — Response to Reviewer (Group C)

---

## Q1: CF and DR Weight / Interaction

**Concern**: The reviewer asks how CF (Cross-Field consistency violations) and DR (Domain-Range violations) are weighted and whether they trade off against each other.

**Response**:
CF and DR measure fundamentally different properties and should not be combined into a single weighted metric. DR measures ontological constraint violations (whether entity-type pairs are valid for a given relation), while CF measures cross-field consistency (whether head/tail entities referenced in a relation triple match previously declared entities). They operate on orthogonal axes of schema compliance.

Table 5 (ablation) reports CF and DR separately precisely to expose the trade-off landscape. The key finding: CF rises when the semantic layer is active (full_s1: CF=9.90% on SciERC) because CF is a *byproduct* of the constraint fallback mechanism, not an independent optimization target. When the semantic layer's bitwise AND of grammar mask and domain-range mask produces an empty set (no token simultaneously satisfies both constraints), the system falls back to grammar-only decoding for that token position. This fallback may produce an entity name that is grammatically valid but inconsistent with previously generated fields — hence CF. The fallback design prioritizes generating *some* valid output over blocking generation entirely.

Crucially, DR reduction (15.37% → 0.93% on SciERC, a 93.9% relative reduction) vastly outweighs the CF increase (+9.82pp), and CF violations are inherently less severe: they represent internal naming inconsistencies that downstream systems can resolve via string matching, whereas DR violations represent fundamentally invalid semantic assertions.

**Action**: Add a clarifying footnote in Section 5 explaining that CF is a constraint-fallback artifact, not an independent error mode to be minimized jointly with DR.

---

## Q2: Quality of Grammar-Layer Replacements for OOV Relations

**Concern**: The reviewer questions whether the grammar layer's replacement of out-of-vocabulary (OOV) relation names produces semantically meaningful outputs.

**Response**:
This is precisely the limitation that motivates the semantic constraint layer. In the DocRED zero-shot unconstrained setting, we observe **5,261 triples with OOV relation names** (out of 2,038 unique OOV strings). The grammar layer replaces 4,357 of these with in-vocabulary names, but **36.6% (1,594) of replacements introduce new DR violations**. This occurs because XGrammar performs token-level CFG steering — it selects the nearest *syntactically* valid continuation based on token-prefix matching, with no semantic awareness.

We identify three failure modes:

1. **Token-prefix collisions**: "opponent" → "operator" (both share prefix "op"); "peaked at" → "performer" (share "pe"). These produce semantically absurd triples (e.g., a cricketer "operates" a country).

2. **Ontology gaps**: "population", "instrument" have no valid DocRED equivalent. Any grammar-forced replacement is necessarily wrong (e.g., "population" → "has part", asserting a numeric value is a constituent part of a county).

3. **Silent semantic errors**: "available on" → "operator" passes type-checking (ORG→ORG is valid for P137) but reverses the semantic direction, producing undetectable errors at the type level.

These findings directly justify the two-layer architecture: the grammar layer guarantees *syntactic* schema validity (eliminating ET and RV violations entirely), while the semantic layer is needed to enforce *relational* validity that token-level matching cannot achieve.

**Action**: Add a brief discussion in Section 4.3 with 2-3 representative replacement examples and aggregate statistics (36.6% DR-inducing rate).

---

## Q3: Is Grammar Redundant Under Fine-Tuning?

**Concern**: The reviewer suggests that fine-tuned models may not need the grammar constraint layer at all.

**Response**:
The FT ablation confirms that grammar constraints are indeed *operationally redundant* for ET and RV in fine-tuned models — both Qwen3-8B and Llama-3.1-8B produce zero ET violations and near-zero RV violations without constraints after fine-tuning. However, the grammar layer serves two essential roles even in the FT regime:

**Role 1: Eliminating residual RV.** On DocRED, FT-Qwen unconstrained still shows RV=0.27% and FT-Llama shows RV=0.15%. Grammar-only mode reduces both to RV=0% (Tables 1-2 of the FT ablation). While small in absolute terms, this guarantees zero vocabulary violations — a hard requirement for downstream knowledge graph construction.

**Role 2: Enabling the semantic layer.** The semantic layer's domain-range enforcement operates by looking up the generated relation name in the ontology to retrieve valid (head_type, tail_type) pairs. If the relation name is OOV (not in vocabulary), the lookup fails and no constraint can be applied. Grammar ensures every generated relation name is in-vocabulary, thereby enabling the semantic layer to function. Without grammar, the semantic-only mode on DocRED FT still shows RV=0.23% (Qwen) / 0.15% (Llama) — these represent cases where the semantic layer cannot enforce DR constraints because it cannot resolve the relation name.

The ablation data confirms the complementarity: Semantic-only reduces DR by 41–72% across all four model×dataset settings, but the full system (grammar + semantic) achieves the lowest DR in all cases (0–0.20%), because the grammar layer's guarantee of valid relation names enables complete semantic enforcement.

**Action**: Add a sentence in Section 6.2 explicitly noting that grammar's FT-regime role is as an enabling dependency for the semantic layer rather than as an independent violation reducer.

---

## Q4: R² Generalizability and Mistral as Outlier

**Concern**: The reviewer questions whether the dual-factor regression (R²=0.886) generalizes beyond the four calibrated data points, particularly given Mistral's deviation.

**Response**:
We acknowledge that the n=4 dual-factor model (τ̄ × RV_baseline, R²=0.886) is descriptive rather than predictive — it characterizes the relationship between schema tightness, vocabulary confusion, and residual DR for models that have been properly calibrated to the target schema (via zero-shot prompting with schema-informed instructions).

Mistral's extreme deviation is informative rather than problematic. When included, the single-factor linear fit collapses (R² drops from 0.54 to 0.21 for τ̄-only), confirming that schema tightness alone is insufficient. Mistral's residual DR (13.4% on SciERC, 33.2% on DocRED) originates from a qualitatively different mechanism: **entity type misclassification**, not vocabulary confusion. Mistral generates syntactically valid relation names but systematically assigns wrong entity types (e.g., labeling organizations as persons), producing type-pair violations that no amount of relation-vocabulary calibration can address.

This is a finding about *model architecture limitations* in constrained decoding, not a limitation of our method. In fact, Mistral's case demonstrates that OntoCoDec provides the *greatest absolute benefit* precisely when models are least calibrated — the constrained-vs-unconstrained DR gap is largest for Mistral, validating the system's value proposition for weaker or out-of-distribution models.

**Action**: Reframe the R² discussion in Section 5.4 as a "calibrated-model characterization" rather than a universal predictive model, and explicitly position Mistral as a boundary condition that reveals when grammar+semantic constraints are most impactful.

---

## Q5: Fuzzy Matching Threshold Sensitivity

**Concern**: The reviewer asks whether the fuzzy matching thresholds (Jaccard > 0.8, Levenshtein ≤ 2) were tuned on the evaluation data, potentially inflating reported metrics.

**Response**:
The thresholds are **a priori constants**, not tuned parameters. Both values (Token Jaccard > 0.8, Levenshtein distance ≤ 2) are hardcoded identically across 6 evaluation files (`violation_checker.py`, `unified_f1_eval.py`, `compute_bootstrap_ci.py`, `posthoc_filter.py`, etc.) with no parameterized interface — no CLI argument, no config file, no sweep code exists. They represent standard NLP soft-matching defaults (0.8 Jaccard ≈ allow 1/5 token difference; ≤2 Levenshtein ≈ tolerate minor typos).

More importantly, **fuzzy matching has negligible impact on reported results**:

| Scope | Fuzzy match triggers | Total triples | Impact |
|-------|---------------------|---------------|--------|
| DocRED ZS unconstrained | 129 | 17,497 | 0.74% |
| All constrained modes (grammar/semantic/full) | **0** | — | **0%** |
| All FT experiments | **0** | — | **0%** |
| All SciERC experiments | **0** | — | **0%** |

Fuzzy matching triggers *only* in DocRED zero-shot unconstrained mode (where the model occasionally generates near-miss relation names like "country" for P17). In all constrained decoding modes — which constitute the primary experimental claims — and in all fine-tuned models, the fuzzy match count is exactly zero. The strict-vs-fuzzy R_F1 difference is <0.1pp even in the one setting where it triggers.

All main conclusions (DR reduction, layer complementarity, FT ablation findings) rest entirely on strict matching.

**Action**: Add a footnote in Section 4.1 (Evaluation Protocol) stating that thresholds are fixed a priori constants and that fuzzy matching triggers in <1% of triples, exclusively in unconstrained baselines.

---

## Additional Points (for Author Response if space permits)

### Beam Search / Sampling Compatibility

The current implementation uses greedy decoding. We note that:
- **Sampling** (temperature, top-p, top-k) is immediately compatible with our architecture — it requires only ~10 lines of parameter-passing code, as the semantic constraint processor operates on individual sequences (batch_size=1 per generation call).
- **Beam search**: Beam compatibility is achieved via per-step token replay from XGrammar's stateless API (64 lines for grammar layer, 61 lines for semantic layer). We will add sampling experiments in the camera-ready version.

### RV=0.03% Residual in Grammar Mode

The 5 residual RV violations (0.03%, all in one document "Souvlaki") stem from an XGrammar v0.1.33 enum compilation bug where the grammar bitmask leaks token continuations across enum entries (e.g., after "member", token "icipant" is incorrectly allowed, producing the nonexistent relation "membericipant of"). This is a third-party library bug, not a limitation of our constraint formulation. The FT models do not trigger this bug. We will note this in the camera-ready as a known XGrammar issue.

### Parse Failure Denominator

Our violation rates use parsed-only denominators (excluding documents where JSON parsing fails entirely). The maximum adjustment under an all-set denominator assumption is <0.23pp (Llama DocRED ZS constrained: 2.55% → 2.32%), which does not affect any comparative conclusion. We will report both denominators in the supplementary material.
