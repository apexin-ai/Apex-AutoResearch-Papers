# DocRED Fine-Tuning Paper Update Mapping

Generated: 2026-05-16

## Required Experimental Data

All four runs must produce: DR, RV, ET, CF, R-F1, E-F1, triple count, parse failure count.

| Run | Status |
|-----|--------|
| Qwen DocRED FT unconstrained | Running |
| Qwen DocRED FT constrained (S1) | Pending |
| Llama DocRED FT unconstrained | Just completed, metrics extraction in progress |
| Llama DocRED FT constrained (S1) | Pending |

---

## Update Locations (Priority Order)

### U1. `section5_composability.tex` — Table `tab:composability` [NEW ROWS]

**Lines**: ~13–42 (the entire table environment)
**Current**: 8 data rows — Qwen (ZS U, ZS S1, LoRA U, LoRA S1) + Llama (same), all on **SciERC only**.
**Action**: Add 8 new DocRED FT rows (4 per model). The table needs a new `\multirow` block or a dataset column. Suggested restructure:

```
Model × Dataset | Train | Decode | DR | CF | R-F1 | E-F1
Qwen SciERC      ZS/LoRA  U/S1    ...
Qwen DocRED      ZS/LoRA  U/S1    ...
Llama SciERC     ZS/LoRA  U/S1    ...
Llama DocRED     ZS/LoRA  U/S1    ...
```

**Data needed**: All 4 DocRED FT runs × {DR, CF, R-F1, E-F1}
**Update type**: Major table restructure + new rows

---

### U2. `section5_composability.tex` — Table caption [MODIFY]

**Line**: ~45
**Current**: "Composability with fine-tuning on SciERC (551 documents)."
**Action**: Change to "Composability with fine-tuning on SciERC (551 documents) and DocRED (998 documents)."
**Data needed**: None (just text)
**Update type**: Caption text modification

---

### U3. `section5_composability.tex` — ¶ "Fine-tuning does not eliminate ontology violations" [MODIFY + EXTEND]

**Lines**: ~52–63
**Current**: Reports SciERC-only FT numbers:
- "R-F1 from 8.23 to 43.86 (Qwen) and from 2.68 to 45.45 (Llama)"
- "residual DR persist at 1.95% (Qwen) and 1.11% (Llama)"
- "Evaluate-for retains 13.1% DR for the fine-tuned Qwen model"

**Action**: Add DocRED FT DR numbers. Key question: does DocRED FT reduce the ZS DR (18.46% Qwen / 26.07% Llama) substantially, and is there a residual?
**Data needed**: Qwen DocRED FT unconstrained DR, Llama DocRED FT unconstrained DR, R-F1 for both
**Update type**: Extend paragraph with DocRED FT evidence

---

### U4. `section5_composability.tex` — ¶ "Constraints compose with fine-tuning at no F1 cost" [MODIFY + EXTEND]

**Lines**: ~64–77
**Current**: SciERC-only: "Qwen 1.95%→0.00%, Llama 1.11%→0.09%", F1 delta <0.1pp
**Action**: Add DocRED FT constrained results. Does the same pattern hold (near-zero F1 cost)?
**Data needed**: All 4 DocRED FT runs × {DR, R-F1, E-F1, CF}. Delta comparisons: constrained vs unconstrained.
**Update type**: Extend paragraph

---

### U5. `section5_composability.tex` — ¶ "Implication" [POSSIBLE MODIFY]

**Lines**: ~79–87
**Current**: General argument backed only by SciERC evidence.
**Action**: If DocRED FT confirms the same pattern, strengthen from "SciERC shows" to "both datasets show". If DocRED FT shows different behavior (e.g., FT on 96-relation ontology eliminates more violations than on 7-relation), add nuance.
**Data needed**: Same as U3/U4
**Update type**: Conditional text modification

---

### U6. `main.tex` — Limitations section, line 69 [DELETE/REWRITE]

**Line**: 69
**Current**: "Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings on SciERC; DocRED fine-tuning is not reported (the Qwen LoRA run is still in progress at submission time)."
**Action**: Remove the DocRED caveat. Rewrite to: "Results cover two 8B-class models on two datasets, in both zero-shot and LoRA fine-tuned settings."
**Data needed**: None (just confirming experiments are done)
**Update type**: Delete caveat

---

### U7. `main.tex` — Limitations section, line 65 [MODIFY]

**Line**: 65
**Current**: "this rate falls to ≤1.18% once the base model is LoRA fine-tuned (Table~\ref{tab:composability})."
**Action**: Update the CF upper bound if DocRED FT produces a higher CF than 1.18%. The current "≤1.18%" is from SciERC Qwen FT S1. DocRED FT S1 may have different CF.
**Data needed**: CF rate for all 4 DocRED FT constrained (S1) runs
**Update type**: Possible number update

---

### U8. `main.tex` — Limitations section, line 68 [MODIFY]

**Line**: 68
**Current**: "under fine-tuning, entity F1 is unchanged for both models on SciERC."
**Action**: Extend to include DocRED FT entity F1 behavior.
**Data needed**: E-F1 delta (constrained vs unconstrained) for both models on DocRED FT
**Update type**: Extend sentence

---

### U9. `section7_conclusion_compressed.tex` — ¶ "Contributions" [MODIFY]

**Lines**: last paragraph (~24–28)
**Current**: "achieves 45--99% DR reduction across two models and two datasets"
**Action**: 
1. The DR reduction range may change if DocRED FT constrained results shift the bounds.
2. Should explicitly mention FT composability as a validated result, not just ZS.
**Data needed**: DR reduction % for DocRED FT constrained (both models)
**Update type**: Update range numbers + add FT mention

---

### U10. `section1_introduction_draft.tex` — Contribution #3 [POSSIBLE MODIFY]

**Line**: 27
**Current**: "Empirical validation on 2 models × 2 datasets: DR ↓94% on SciERC and ↓45--90% on DocRED, with significant R-F1 gains on DocRED (p ≤ 0.013) and model-agnostic structural guarantees."
**Action**: Consider adding "in both zero-shot and fine-tuned regimes" to strengthen the claim. The DR range "45–90%" is ZS DocRED only; FT results may warrant a separate claim.
**Data needed**: DocRED FT DR reduction percentages
**Update type**: Conditional text extension

---

### U11. `abstract.tex` [POSSIBLE MODIFY]

**Lines**: entire abstract (~12 lines)
**Current**: Only ZS numbers. No mention of fine-tuning or composability.
**Action**: If space permits, add one sentence about composability: "The constraints compose with LoRA fine-tuning: residual DR falls to 0% (SciERC) and X% (DocRED) at <0.1pp F1 cost." This would strengthen the abstract significantly.
**Data needed**: Best DocRED FT constrained DR numbers
**Update type**: Optional — add 1 sentence

---

### U12. `appendix_discussion.tex` — ¶ "Practical Significance of Zero-Shot F1" [MODIFY]

**Lines**: 12–17
**Current**: "When applied to fine-tuned models that reach competitive F1 levels, the same constraints remain necessary" — forward-looking claim without direct evidence.
**Action**: Now that FT results exist on both datasets, replace forward-looking language with direct evidence: "We validate this directly: LoRA fine-tuned models on SciERC achieve R-F1 of 43.86/45.45 (Qwen/Llama) yet retain 1.95%/1.11% DR; on DocRED, FT models achieve X/Y R-F1 yet retain A%/B% DR."
**Data needed**: DocRED FT unconstrained R-F1 and DR for both models
**Update type**: Strengthen existing claim with evidence

---

### U13. `paper_tables_draft.tex` — Table 4 `tab:cross-dataset` [LOW PRIORITY — NOT IN main.tex]

**Lines**: Table 4
**Current**: DocRED S1 = "TBD"
**Note**: This file is NOT `\input`'d by main.tex. It's a standalone draft. The real cross-dataset comparison is in `section5_crossmodel_draft.tex` (tab:cross-model). Update only for consistency if this file is maintained as a reference.
**Update type**: Low priority, reference file only

---

## Cross-Cutting Concerns

### C1. 2×2 Matrix Completeness
The composability story currently demonstrates on SciERC only:
```
         SciERC    DocRED
Qwen      ✅        ❌ (pending)
Llama     ✅        ❌ (pending)
```
Completing DocRED fills all four cells and makes the composability claim fully general across the paper's experimental scope.

### C2. Bootstrap Significance Tests
The SciERC FT results report F1 deltas but no bootstrap p-values (because the delta is <0.1pp and clearly non-significant). DocRED FT results should also have bootstrap CIs computed for completeness, especially if the R-F1 delta is larger.

### C3. Per-Relation Analysis
`appendix_llama_per_relation.tex` covers ZS DocRED Llama per-relation DR. If DocRED FT shows interesting per-relation patterns (e.g., tight relations remain problematic even after FT, paralleling SciERC Evaluate-for), consider adding a per-relation FT appendix table.

### C4. CF Behavior Under DocRED FT
The current narrative (section5_composability.tex ¶3) claims CF drops substantially under FT (9.90%→1.18% Qwen, 6.56%→0.46% Llama on SciERC). If DocRED FT shows a different CF pattern (DocRED has τ̄=0.842 vs SciERC's 0.333), this would be an important finding to discuss.

### C5. Tightness × FT Interaction
Section4 and section5_docred establish that tightness governs ZS enforcement ceiling. DocRED FT tests whether FT changes this relationship. If FT reduces DocRED DR to near-zero (like SciERC), the tightness mechanism is less of a fundamental limit and more of a ZS-specific challenge.

---

## Execution Checklist

When all 4 DocRED FT experiments are complete:

1. [ ] Extract metrics from all 4 runs (DR, RV, ET, CF, R-F1, E-F1, triples, parse failures)
2. [ ] Compute deltas: FT constrained vs FT unconstrained (per metric, per model)
3. [ ] Run bootstrap significance tests on R-F1 and E-F1 deltas
4. [ ] Update U1 (table) — most complex, do first
5. [ ] Update U2–U5 (composability section text)
6. [ ] Update U6–U8 (Limitations)
7. [ ] Update U9 (Conclusion numbers)
8. [ ] Update U10–U11 (Introduction/Abstract) — lightest touch
9. [ ] Update U12 (Appendix discussion)
10. [ ] Verify all exp_id comments in source match actual experiment IDs
11. [ ] Recompile and check no broken references
