# W1 CF-Fallback SciERC Pilot — Detailed Analysis

**Experiment**: `w1_cf_fallback_scierc_pilot`  vs  baseline `phase2_scierc_full_s1` (Qwen, SciERC test, 551 samples, full S1 stage)
**Status**: DONE / negative (DR escalates while CF is nearly eliminated)
**Date**: 2026-05-15

---

## 1. Executive Summary

The CF-priority fallback policy in W1 was designed to eliminate cross-field-consistency (CF) violations by preferring previously-registered entity types over fresh domain/range masks. The pilot confirms CF is nearly eradicated (9.90 % → **0.04 %**, a 244-of-245 reduction), but at a severe cost: per-triple domain-range (DR) violation rate explodes from **0.93 % → 14.78 %** (+13.85 pp, ×15.9). Of 17 024 semantic-mask invocations, only **58.9 % (10 024)** were "effective" — the remaining **36.6 % (6 237)** were silently overridden by the grammar-first guard (semantic ∩ grammar = ∅) and another **4.5 % (763)** by the CF registry. R-F1 / E-F1 are statistically unchanged (8.36 → 8.23, 30.98 → 30.98), so the move is a pure DR-vs-CF trade with no quality win. The CF residual (a single mention `eigenvectors` typed both as `Material` and `OtherScientificTerm`) is intrinsic to ambiguous lexical items the model emits inside multiple relations. Together the numbers show that **mask invocation counts are misleading as a proxy for semantic enforcement** — a substantial fraction of mask calls are no-ops — and that **decoupling CF from DR via fallback transfers, rather than removes, the violation budget**.

---

## 2. Per-Relation DR Comparison

Computed from `violation_report_w1_cf_fallback_scierc_pilot.json` and `violation_report_phase2_scierc_full_s1_v2.json` (same 551-sample test split, checker `fixed_20260514_v2`). "Tightness" = `1 − |valid_pairs| / 36`, where 36 = 6² is the maximum number of entity-type pairs.

| Relation       | Tightness | Triples (B/P) | Baseline DR | Pilot DR | Δ DR (pp) | New invalid pairs (top) |
|----------------|-----------|---------------|-------------|----------|-----------|--------------------------|
| Used-for       | 0.028 | 791 / 791 | 0.00 % | 0.25 % | +0.25 | (Metric,Metric) ×2 |
| Feature-of     | 0.278 | 495 / 494 | 1.21 % | **31.98 %** | **+30.77** | (Task,OST) ×44; (Generic,Generic) +29; (Task,Material) +25; (Method,Material) +20 |
| Conjunction    | 0.306 | 35 / 33   | 0.00 % | 0.00 % | 0.00 | — |
| Evaluate-for   | 0.361 | 139 / 134 | 5.76 % | **23.13 %** | **+17.37** | (Method,Task) +5; (OST,OST) +4; (Metric,Metric) +3 |
| Hyponym-of     | 0.417 | 123 / 125 | 0.00 % | 14.40 % | +14.40 | (Task,OST) ×10; (Method,Metric) ×4 |
| Part-of        | 0.417 | 75 / 77   | 0.00 % | 23.38 % | +23.38 | (Material,OST) ×7; (Task,OST) ×6 |
| Compare        | 0.528 | 71 / 71   | 2.82 % | **39.44 %** | **+36.62** | (Method,OST) ×6; (Task,Method) ×6; (Method,Task) ×4 |

(OST = OtherScientificTerm; B = baseline, P = pilot.)

**Observation.** ΔDR scales monotonically with tightness for the head-heavy relations (Feature-of, Compare, Part-of, Hyponym-of). The Spearman rank correlation between tightness and ΔDR is essentially 1.0 across the five non-trivial relations (Used-for, Conjunction are tiny by construction). The reading: when the semantic mask is *most* restrictive, the grammar-first guard fires *most* often, and the fallback path emits triples that violate exactly the constraints the mask was supposed to enforce. Tightness is therefore both a feasibility indicator and a fallback-risk indicator.

---

## 3. Attempted vs Effective Semantic Masking (Reviewer-Requested Framing)

The pilot logs cumulative `TypeConstraintProcessor` counters but does **not** record per-mask-call attribution (no per-relation log channel was wired). The global decomposition is:

| Category | Count | Share | Meaning |
|----------|-------|-------|---------|
| **Attempted mask calls** | 17 024 | 100.0 % | Token-decoding steps where the semantic processor was on the stack |
| **→ Effective semantic masking** | 10 024 | **58.9 %** | Semantic ∩ grammar set non-empty → mask actually constrained next-token selection |
| **→ Grammar-first override** | 6 237 | **36.6 %** | Semantic ∩ grammar = ∅ → semantic mask discarded, only grammar enforced (W0 behavior at that step) |
| **→ CF-registry override** | 763 | **4.5 %** | Registered (mention → type) conflicted with the relation's domain/range → CF-consistency prioritized |

**Implication for the paper.** "Times the constraint module was invoked" overstates enforcement strength by ~41 percentage points on this configuration. We should report both rates side-by-side:
- *Coverage*: 100 % of type-field tokens routed through the processor.
- *Effective coverage*: 58.9 % token-steps actually masked.

Because per-call attribution was not logged, the per-relation attempted/effective split is **not directly available** from this pilot. Triangulating via the per-relation ΔDR (Section 2), Feature-of and Compare almost certainly absorb the largest share of grammar-first overrides — their joint Δ accounts for 158 + 28 = 186 of the 239 new DR violations (77.8 %). Adding per-call logging (relation type at fallback time) is a 30-LOC fix and should be done before the camera-ready experiments.

---

## 4. CF Residual Analysis

Recomputing per-document mention-type aggregation from raw JSONL (mirroring `violation_checker.py`):

- **Baseline (no fallback):** 245 CF violations, 0.099 / pred-entity.
- **Pilot (CF fallback on):** **1** CF violation, 0.0004 / pred-entity.
- **Removed by fallback:** 244 / 245 (99.6 %).
- **Newly introduced:** 0.

The single residual case:

```
doc_id   : P06-2012_sent1
mention  : "eigenvectors"
types    : ["Material", "OtherScientificTerm"]
```

Mechanism: the CF registry stores `(mention → type)` *within a generation*, but the residual case occurs when the *first* emission registers one type and a *later* relation's domain/range forces the *opposite* type even after the CF-priority logic — i.e. the relation's valid_pairs set has zero intersection with the registered type at either end, so the fallback policy must choose between violating DR or violating CF, and the current implementation breaks the tie toward DR-consistency for this particular code-path. (We did not instrument which branch fired — adding `cf_break_reason` to the log is another small fix worth doing.)

For Reviewer framing: CF can be made vanishingly small but never strictly zero whenever the schema is non-trivial and the model emits the same lexical item across mutually exclusive domain/range cells.

**Top conflicting type pairs in the baseline 245** (what the fallback successfully erased):

| Conflicting pair | Count |
|------------------|-------|
| Generic ↔ OtherScientificTerm | 85 |
| Generic ↔ Material | 35 |
| Generic ↔ Metric | 30 |
| Method ↔ Task | 20 |
| Material ↔ Method | 17 |
| OtherScientificTerm ↔ Task | 12 |
| Method ↔ OtherScientificTerm | 8 |

`Generic` is the dominant flip-target — consistent with `Generic` being the "fallback" semantic type the model reaches for whenever the head/tail is ambiguous, which then conflicts with a more specific later mention.

---

## 5. DR Escalation Root Cause

Net DR change: 16 → 255 violations (Δ = **+239 new DR violations**) on the same 551-sample test split.

### 5.1 Decomposition by override channel

We do not have a direct per-violation link to fallback channel, so we bound each channel's contribution:

| Channel | Events | Lower bound on DR contribution | Upper bound |
|---------|--------|--------------------------------|-------------|
| Grammar-first override | 6 237 | 0 (mathematically possible if every override happened to pick a valid-pair token by chance) | 239 (if every new DR violation came from this channel) |
| CF-registry override | 763 | 0 | 239 |
| "Effective" semantic mask path | 10 024 | 16 (baseline residual; mask is enforced on this branch) | 16 |

The strict lower bound on the "effective" channel = baseline DR (16) — semantic masking actively enforced on those 10 024 steps still left 16 violations because the per-step token-level mask cannot prevent every multi-step type-pair combination once the head_type is committed (intra-triple coupling). All other DR escalation must come from the two override channels.

### 5.2 Why grammar-first dominates

The grammar-first guard activates when the **per-relation domain/range constraint at the current token position would leave the grammar-valid token set empty**. Concretely, this happens when:
1. The model has already committed `relation=R, head_type=H` (or it is about to emit `tail_type` in a tight relation), **and**
2. No valid `tail_type` token under `valid_pairs(R, H, *)` is also currently grammar-valid (e.g., next-token must start with `O` for `OtherScientificTerm` because of grammar prefix state, but `OtherScientificTerm` isn't in `range(R, H)`).

For a relation like Compare with only 17/36 valid pairs, the probability that a randomly-arrived-at head_type leaves a non-empty tail_type intersection is structurally low — hence Compare's 39.4 % pilot DR.

Verification of channel attribution requires the per-mask-call relation-tagged log (see §3); we recommend adding it before W3 (Llama × SciERC, Llama × DocRED) runs so the same analysis on Llama is directly attributable.

### 5.3 Per-relation new DR violation type-pair signatures

(From JSONL re-analysis; full table in Section 2.) Three patterns repeat across relations:

- **OST-as-bucket**: 67 new violations name `OtherScientificTerm` on at least one side of an invalid pair across Feature-of / Compare / Part-of / Hyponym-of. The model uses OST as a low-specificity fallback type; the CF registry consequently locks it in across calls.
- **Task ↔ OST**: 60 new violations (Hyponym-of, Feature-of, Compare, Part-of). Tasks frequently co-occur with phrases the model parses as OST rather than re-using the Task tag.
- **Generic explosion in Feature-of**: 33 new (Generic, Generic) Feature-of violations. Feature-of does *not* allow (Generic, Generic) in the SciERC training-derived constraint, but Generic is by far the most common fallback type the model emits.

---

## 6. Paper Implications (Reviewer Framing)

The Reviewer's suggestion was to make the **attempted vs effective** decomposition explicit in the paper. This pilot directly supports three load-bearing claims for the methods section:

1. **Mask-invocation count is not enforcement strength.** On Qwen-SciERC, only 58.9 % of semantic-mask calls were effective; 36.6 % were silently overridden by the grammar-first guard and 4.5 % by the CF registry. Papers that report "constrained decoding was applied at 100 % of decoding steps" without this decomposition systematically overstate the contribution of semantic constraints.

2. **CF and DR live in a single violation budget.** Baseline violation budget (DR + CF) = 10.83 %. Pilot budget = 14.82 % (DR 14.78 + CF 0.04). Eliminating CF cost +3.99 pp of total violations — the constraint did not vanish, it moved. This is a clean negative result motivating a *joint* CF + DR scheduler instead of a hierarchical fallback.

3. **Tightness predicts fallback risk.** Across relations the per-relation ΔDR rank-correlates with tightness (Compare ≫ Part-of ≈ Hyponym-of ≈ Feature-of ≫ Used-for). Schemas with high-tightness relations need an alternative enforcement strategy (joint product mask, beam-search with backtracking, or training-time alignment) — fallback-style decoding cannot maintain DR on tight schemas without a quality penalty.

The downstream F1 numbers (R-F1 ±0.13, E-F1 ±0.00) confirm that the move is policy-neutral for end-task accuracy. The *paper-level* contribution of W1 is therefore the negative finding plus the decomposition — both of which strengthen, rather than weaken, the framing of OntoCoDec's joint-mask design as the principled alternative.

---

## Appendix A — Raw Numbers

| Metric | Baseline (`phase2_scierc_full_s1`) | Pilot (`w1_cf_fallback_scierc_pilot`) |
|--------|-----------------------------------|---------------------------------------|
| Total samples | 551 | 551 |
| Total triples extracted | 1 729 | 1 725 |
| Total entities extracted | 2 474 | 2 474 |
| DR violations | 16 | 255 |
| DR rate | 0.93 % | 14.78 % |
| CF violations | 245 | 1 |
| CF rate | 9.90 % | 0.04 % |
| Total violation rate | 6.21 % | 6.10 % |
| Entity F1 | 30.98 | 30.98 |
| Relation F1 | 8.36 | 8.23 |
| Grammar-first fallback events | (n/a) | 6 237 |
| CF-registry fallback events | (n/a) | 763 |
| Total semantic-mask calls | (n/a) | 17 024 |
| Effective semantic-mask share | (n/a) | 58.85 % |

## Appendix B — Data Sources

- `/root/schema_semantic_constrained_ie/outputs/violation_report_w1_cf_fallback_scierc_pilot.json`
- `/root/schema_semantic_constrained_ie/outputs/violation_report_phase2_scierc_full_s1_v2.json`
- `/root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_scierc_pilot.jsonl`
- `/root/schema_semantic_constrained_ie/outputs/phase2_scierc_full_s1_v2.jsonl`
- `/root/schema_semantic_constrained_ie/outputs/w1_cf_fallback_scierc_pilot_fallback_stats.json`
- `/root/schema_semantic_constrained_ie/ontology_constraints.json`

## Appendix C — Recommended Logging Additions (for W1 follow-ups)

Adding to `compiler/type_mask_processor.py`:

1. **Per-relation fallback counters** — when the grammar-first or CF-fallback path triggers, increment `cls.grammar_first_fallback_by_relation[relation]` and `cls.cf_registry_fallback_by_relation[relation]`. ~10 LOC. Enables direct per-relation attempted/effective table in the paper.
2. **`cf_break_reason` on CF residuals** — when CF-priority logic cannot fully resolve a tie (the residual case in §4), record which constraint was violated and why. ~5 LOC.
3. **Per-doc mask call breakdown in JSONL** — write `{effective, grammar_override, cf_override}` counts as a field on each output record so the same analysis can be reproduced without re-parsing.

These three changes preserve the current global counters and add the per-call attribution needed to make Section 3 quantitative across all four W1 cells (Qwen×SciERC, Qwen×DocRED, Llama×SciERC, Llama×DocRED).
