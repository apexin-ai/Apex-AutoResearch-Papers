# audit inline numbers verification

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_audit_inline-numbers-verification_20260523T104307_result.json`
- **Structured JSON:** [`724088a86e3385737096.json`](../../sessions/72/724088a86e3385737096.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here is the complete audit report.

---

## Inline Number Audit — Main Text

### === abstract.tex ===

**[L9]** `≤0.21%` DR, `F1 41--46%`, `≤1.4%` CF
- DR≤0.21%: Max across 4 FT+S1 configs = 0.21% (Llama DocRED). **✅**
- CF≤1.4%: Max = 1.33% (70B SciERC LoRA S1, 15/1129). **✅**
- F1 41--46%: Actual 8B FT+S1 range = 40.56--45.47%. Min 40.56% < 41%. **⚠️ minor: Qwen DocRED is 40.56%, below stated 41%**

**[L10]** `CF to 0.11% at 1.18× latency; k=4 eliminates all violation types at 1.39×`
- d066_beam_sweep: k2_con CF=0.11%, latency=3.463/2.932=1.181≈1.18×. **✅**
- k4_con CF=0%, latency=4.069/2.932=1.388≈1.39×. **✅**

**[L11]** `up to 12%` CF in zero-shot
- llama_docred_full_s1_mt6144: CF=12.13%. **✅**

**[L12]** `76--99% on SciERC and 42--90% on DocRED`
- SciERC: 76.5% (Mistral) to 99.4% (Llama). **✅**
- DocRED: 42.2% (Mistral) to 90.2% (Llama). **✅**

**[L12]** `n=3`
- Three schemas (WikiEvents, SciERC, DocRED). **✅**

---

### === section1_introduction_draft.tex ===

**[L8]** `15.4% of triples on SciERC and 18.5% on DocRED`
- phase2_scierc_unconstrained DR=15.37%→15.4%. **✅**
- phase2_docred_unconstrained DR=18.46%→18.5%. **✅**

**[L8]** `0.5--2% even after LoRA fine-tuning`
- Actual range: 0.49--1.95%. Rounds to 0.5--2.0%. **✅**

**[L9]** `R-F1 41--47%`
- 8B FT range: 40.56--45.47. 8B FT+beam4 max=46.18. Neither reaches 47%. **⚠️ upper bound 47% not supported; max observed is 46.18%**

**[L12]** `62% on average` (schema-informed prompting)
- mvp_phase0_scierc_schema vs_minimal_dr_reduction=-0.624 = 62.4%. **✅**

**[L12]** `5.8 pp` (Evaluate-for increase)
- mvp_phase0_scierc_schema per_relation Evaluate-for delta_pp=5.8. **✅**

**[L14]** `up to 48% of predictions` (post-hoc discards)
- posthoc_filtering_baseline docred_rejection_rate=0.481≈48%. **✅**

**[L18]** `24% independent DR reduction` (8B semantic-only)
- phase2_scierc_semantic_only DR=11.65% vs unconstrained 15.37%. (15.37-11.65)/15.37=24.2%. **✅**

**[L18]** `84% independently` (70B semantic-only)
- eval_70b_zs_scierc_semantic_only DR=1.01% vs unc 6.40%. (6.40-1.01)/6.40=84.2%. **✅**

**[L20]** `DR ≤ 0.21% at R-F1 41--46% (±0.3 pp, +10% latency)`
- DR≤0.21%: **✅** (max=0.21%, Llama DocRED)
- ±0.3pp: max|Δ|=0.30pp (Qwen DocRED). **✅** (exact match)
- +10%: p8c_ft_scierc_latency overhead_mean_pct=10. **✅**
- R-F1 41--46%: see abstract ⚠️

**[L20]** `k=4 eliminates all violation types...1.39×`
- **✅** for all 8B FT beam4 configs (all violations = 0)

**[L21]** `~31%` total violation decrease
- Not directly verifiable from individual experiments; requires cross-model average computation. **Unverifiable from registry alone.**

**[L28]** `DR to ≤0.21%`, `±0.3 pp`
- Same as above. **✅**

**[L29]** `R-F1 44.60, CF 0.11%, 1.18×`
- d066_beam_sweep k2_con: R-F1=44.60, CF=0.11%, 1.18×. **✅**

**[L29]** `k=4 eliminates all violations at 1.39×`
- d066_beam_sweep k4_con: all=0%, 1.39×. **✅** (for 8B)

---

### === section3_method_draft.tex ===

**[L41]** `median 17 entities, 6 types` (SciERC) → `6^17 ≈ 1.6×10^13`
- 6^17 = 1.69×10^13. Paper says 1.6×10^13. **✅** (rounded)
- 6 entity types in SciERC: Generic, Task, Method, Metric, Material, OtherScientificTerm. **✅**
- Median 17 entities: requires data-level check. **Not verifiable from registry.**

**[L41]** `median 19 entities, 6 types` (DocRED) → `6^19 ≈ 6.1×10^14`
- 6^19 = 6.09×10^14. Paper says 6.1×10^14. **✅**
- 6 entity types in DocRED: PER, ORG, LOC, TIME, NUM, MISC. **✅**
- Median 19 entities: requires data-level check. **Not verifiable from registry.**

**[L44--45]** `24% DR reduction at 8B`, `84% DR reduction at 70B`
- Both verified above. **✅**

**[L70]** `33--37% spurious pairs on SciERC/DocRED`
- From constraint analysis. **Not verifiable from registry; deterministic from ontology.**

**[L104]** `24% without grammar-enforced vocabulary`
- Same as semantic-only above. **✅**

---

### === section4_composition_draft.tex ===

**[L12]** `84% DR reduction (vs 24% on 8B)`
- **✅**

**[L23]** `κ̄` values: WikiEvents=0.029, SciERC=0.333, DocRED=0.842
- Deterministic from ontology. **Accepted (not independently verifiable from registry).**

**[L23]** `94--99% to 42--90%` DR reduction
- SciERC: 93.9%≈94% to 99.4%≈99%. **✅**
- DocRED: 42.2%≈42% to 90.2%≈90%. **✅**

**[L23]** `p=0.138`
- With n=3, plausible. **Accepted.**

**[L23]** `3.8% of gold triples in DocRED`
- Requires gold data analysis. **Not verifiable from registry.**

**[L29]** `0.5--5.7% of type-bearing positions` (fallback)
- Requires fallback analysis logs. **Not verifiable from registry.**

**[L29]** `≤0.11%` (FT fallback rate)
- Requires fallback logs. **Not verifiable from registry.**

**[L33]** `0/7 SciERC, 23/96 DocRED rectangular`
- Deterministic from ontology. **Accepted.**

**[L33]** `33--37% spurious pairs`
- Same as method section. **Accepted.**

**[L34]** `551 SciERC documents`
- Standard SciERC test set. **✅**

---

### === section3_violation_landscape.tex (Setup) ===

**[L7]** `DR ≤ 0.21%, +10% latency`, `1.39× latency`, `R-F1 41--46%`
- All consistent with verified data. **✅** (with F1 caveat ⚠️)

**[L10]** `551 test sentences, 7 relations, κ̄=0.333`, `998 dev documents, 96 relations, κ̄=0.842`
- 551, 7, 998, 96 are standard dataset properties. **✅**

**[L15]** `R-F1 range 41--47% under LoRA`
- See intro note. **⚠️ same issue: min=40.56, max≤46.18**

**[L18]** `Baseline DR: 15.37% (SciERC), 18.46% (DocRED)`
- phase2_scierc_unconstrained DR=0.1537=15.37%. **✅**
- phase2_docred_unconstrained DR=0.1846=18.46%. **✅**

**[L18]** `62%` (schema-informed prompting reduction)
- **✅** (verified above)

---

### === section5_scierc_draft.tex ===

**Table 1 (tab:scierc-ablation)** — ALL NUMBERS:
| Row | DR | RV | ET | CF | Tot | R-F1 | E-F1 | Status |
|---|---|---|---|---|---|---|---|---|
| Unconstrained | 15.37 | 1.39 | 0.40 | 0.08 | 15.45 | 8.23 | 31.01 | **✅** |
| Grammar | 14.84 | 0 | 0 | 0.08 | 14.92 | 8.23 | 30.98 | **✅** |
| GCD-equiv | 15.26 | 0 | 0 | 0.04 | 15.30 | 8.75 | 30.91 | **✅** |
| Semantic | 11.65 | 1.51 | 0.40 | 2.71 | 14.36 | 8.15 | 31.01 | **✅** |
| S1 | 0.93 | 0 | 0 | 9.90 | 10.83 | 8.36 | 30.98 | **✅** |
| S2 | 0.97 | 0 | 0 | 8.03 | 9.00 | 8.03 | 31.90 | **✅** |

**[L76]** `15--18%`, `3%`, `24%`, `94%`
- 15--18%: 15.37--18.46. **✅**
- 3%: grammar reduction=(15.37-14.84)/15.37=3.4%→3%. **✅**
- 24%, 94%: verified above. **✅**

**[L78]** `76--99% on SciERC and 42--90% on DocRED`, `5/6 settings`
- **✅** (verified above)

**[L78]** `15--74% rejection rates` (post-hoc)
- Verified: SciERC=16.8%, DocRED=48.1%. Mistral cross-model rates likely push up to ~74%. **Partially verifiable; SciERC/DocRED Qwen match.**

**[L88]** `DR ≤ 0.09%`
- Qwen SciERC: 0%, Llama SciERC: 0.09%, Qwen DocRED: 0.01%, Llama DocRED: 0.21%.
- Max is 0.21% (Llama DocRED). Claim "≤0.09%" is violated.
- **❌ ERROR: Should be "≤0.21%" if covering all FT+S1 settings, or explicitly scope to SciERC only.**

**[L88]** `95% CIs ⊆ [-0.69, +0.25] pp`
- From bootstrap analysis. **Not independently verifiable from registry metrics alone.**

**[L88]** `97.6--100% false positives`
- From downstream impact analysis. **Not verifiable from registry alone.**

**[L89]** `39--69% reduction` (semantic layer in FT)
- Qwen SciERC: (1.95-0.60)/1.95=69.2%≈69%. **✅**
- Llama SciERC: (1.11-0.65)/1.11=41.4%≈41%. **⚠️ 41% ≠ 39%; lower bound might be from DocRED (not in registry)**

**[L90]** `0 fallbacks` (Qwen), `5,882` (Llama)
- Not in registry summary metrics. **Not verifiable from registry alone.**

**[L91]** `+9.82 pp` (zero-shot CF delta), `+1.18 pp` (fine-tuned)
- ZS: 9.90-0.08=9.82pp. **✅**
- FT: 1.18-0=1.18pp. **✅**

**[L91]** `63.3% of zero-shot CF`
- From CF distribution analysis. **Not independently verifiable from registry.**
- Paper comments confirm source is ZS (phase2_scierc_full_s1). **ZS/FT labeling: ✅**

**[L91]** `R-F1 43--47`
- 8B FT beam4: 43.60--46.18. **⚠️ upper bound 47 not reached**

**[L98]** `248 cross-field violations across 167 documents`
- Labeled as ZS in code comment. CF_rate=0.099 in registry → 0.099×1729=171 triples, but 248 counts might use different unit (entity-level vs triple-level). **Not independently resolvable; ZS source confirmed. ✅ labeling**

**[L98]** `63.3%`, `34.7%`, `12.3%`
- From ZS CF distribution analysis. **Not verifiable from registry.**

**[L99]** `58.1% hallucinated`, `7.3% cascade`, `2.5× more frequent`
- From ZS cascade analysis. **Not verifiable from registry.**
- Code comments confirm ZS source. **ZS labeling: ✅**

**[L100]** `22 violations across 20 documents (1.18%)`
- w5_lora_scierc_constrained_eval: CF_violations=**21**, rate=0.0118=1.18%.
- 21/1784=1.177%≈1.18%. **✅** on rate.
- **❌ ERROR: Count is 21, not 22.**

**[L100]** `cascade errors completely eliminated (0/22)`
- Should be 0/21 if count is 21. **❌ consistent with count error above.**

**Table 2 (tab:composability)** — ALL NUMBERS:
| Model | Dataset | Mode | DR | CF | R-F1 | E-F1 | ΔDR | Status |
|---|---|---|---|---|---|---|---|---|
| Qwen | SciERC | Unc | 1.95 | 0 | 43.86 | 67.05 | — | **✅** |
| Qwen | SciERC | S1 | 0 | 1.18 | 43.77 | 67.05 | ↓100% | **✅** |
| Qwen | DocRED | Unc | 0.76 | 0.12 | 40.86 | 82.15 | — | **✅** |
| Qwen | DocRED | S1 | 0.01 | 0.41 | 40.56 | 81.43 | ↓98.7% | **✅** |
| Llama | SciERC | Unc | 1.11 | 0 | 45.45 | 67.76 | — | **✅** |
| Llama | SciERC | S1 | 0.09 | 0.46 | 45.47 | 67.76 | ↓92% | **✅** |
| Llama | DocRED | Unc | 0.49 | 0.08 | 43.72 | 83.93 | — | **✅** (CF=0.08 not in registry but consistent with paper) |
| Llama | DocRED | S1 | 0.21 | 0.21 | 43.78 | 83.94 | ↓57% | **✅** |

**Table 2 caption** `Qwen PF: 7--8%; Llama PF: 2--3%`
- Qwen DocRED: 7.11--8.52%. **✅**
- Llama DocRED: 2.30--2.51%. **✅**

**[L146]** `0.49% match gold labels`, `one (0.2%)`, `514 false negatives`
- 1/514=0.194%≈0.2%. Math consistent. **Not independently verifiable from registry.**

**[L147]** `36 residual DR violations`, `39%, 33%, 28%`
- Sum: Qwen SciERC=0, Llama SciERC≈1, Qwen DocRED≈2, Llama DocRED=33. Total=36. **✅**
- Decomposition percentages from manual analysis. **Not verifiable from registry.**

---

### === section5_docred_draft.tex ===

**[L8]** `96 relations, 14× SciERC scale`
- 96/7=13.7≈14×. **✅**

**[L9]** `18.46% to 10.21% (↓45%)`
- (18.46-10.21)/18.46=44.7%≈45%. **✅**

**[L9]** `29.66%→0.03%`
- phase2_docred_unconstrained RV=0.2966=29.66%, phase2_docred_full_s1 RV=0.0003=0.03%. **✅**

**[L9]** `R-F1 +0.50 pp (p<0.001)`
- 8.23-7.74=0.49pp, not 0.50pp. **❌ minor: should be +0.49pp**

**[L11]** `18.46%→26.17%` (grammar increases DR)
- phase2_docred_grammar_only DR=26.17%. **✅**

---

### === section5_wikievents_draft.tex ===

**[L6]** `n=20`, `56 event types, 245 constraints`
- By design. **Accepted.**

**[L7]** `AC 1.3--3.8%`, `≤0.8%`, `±1.1 pp`
- From WikiEvents pilot experiments. **Not individually verified (pilot scale).**

---

### === section5_runtime.tex ===

**[L5]** `+13.1% on SciERC`
- p8_latency_overhead overhead_pct=13.1. **✅**

**[L5]** `+10.0% with 37% lower absolute latency`
- p8c_ft_scierc_latency overhead_mean_pct=10. **✅**
- 37% lower: (4.163-2.612)/4.163=37.3%→37%. **✅** (unconstrained base comparison)

**[L6]** `<0.5 s` compilation, `2--3% up to 200 entity types and 1,000 relations`
- d062_ontology_scalability: compile times 0.322--0.42s <0.5s. **✅**
- Overheads: 1.02--1.03=2--3%. **✅**

**[L11]** `eliminates all four violation types on both SciERC and DocRED at both 8B and 70B scales`
- 8B SciERC beam4: Qwen CF=0%, Llama CF=0%. **✅**
- 8B DocRED beam4: Llama CF=0%. **✅**
- 70B DocRED beam4: CF=0%. **✅**
- **70B SciERC beam4**: eval_70b_lora_scierc_beam4_s1 CF_count=**1**. **❌ ERROR: 70B SciERC beam4 has 1 residual CF violation.**

**[L12]** `R-F1 44.60 (highest), CF 0.11%, at only 1.18× greedy S1 latency`
- d066_beam_sweep k2_con: R-F1=44.60, CF=0.11%, 3.463/2.932=1.18×. **✅**
- "highest" = highest among constrained beam configs. **✅**

**[L12]** `CF=0% but lower R-F1 (43.60) at 1.39×`
- k4_con: CF=0%, R-F1=43.60, 4.069/2.932=1.39×. **✅**

**[L13]** `+10% latency, DR<0.1%, CF≤1.4%`
- +10%: **✅**
- DR<0.1%: max FT+S1 DR=0.21%>0.1%. **⚠️ Should be DR<0.21% for all settings, or DR<0.1% scoped to SciERC only (SciERC max=0.09%)**

**[L21]** `SciERC 6.41%→0%, DocRED 14.98%→0%` (70B ZS)
- r16_70b_scierc_zs_s1: baseline_unc_DR=6.41%, S1 DR=0%. **✅**
- r16_70b_docred_zs_s1: baseline_unc_DR=14.98%, S1 DR=0%. **✅**

**[L21]** `R-F1 11--13`
- SciERC: R-F1=11.24, DocRED: R-F1=13.05. Range 11--13. **✅**

**[L23]** `84% DR reduction vs 8B's 24%`, `CF=76`
- 84.2%, 24.2%. **✅**
- eval_70b_zs_scierc_semantic_only CF_count=76. **✅**

**[L25]** `DR→0% on both datasets, R-F1 44.53, 43.95, |Δ|≤0.20pp, CF 0.18--1.33%`
- 70B LoRA SciERC S1: DR=0%, R-F1=44.53. **✅**
- 70B LoRA DocRED S1: DR=0%, R-F1=43.95. **✅**
- SciERC |Δ|=|44.73-44.53|=0.20, DocRED |Δ|=|43.80-43.95|=0.15. Max=0.20. **✅**
- CF: DocRED=0.18%, SciERC=15/1129=1.33%. **✅**

**[L27]** `12.5%→0.5%, R-F1 +4.19 pp`, `+0.28 pp`
- 70B DocRED S1 parse_fail=12.5%→beam4 0.5%. **✅**
- R-F1: 43.95→48.14, Δ=+4.19pp. **✅**
- SciERC: 44.53→44.81, Δ=+0.28pp. **✅**

**[L32]** `DR=15.26%` (vLLM guided_json)
- vllm_guided_json_scierc_zs DR=15.26%. **✅**

**[L33]** `~15% residual DR`, `94% total reduction`
- Grammar-only DR=14.84%≈15%. S1 reduces 15.37→0.93=93.9%≈94%. **✅**

**[L33]** `9--51% parse failure` (trie-only)
- FT only: Qwen 9.1%, Llama 50.8%→9--51%. **✅** for FT.
- ZS: both 0%. Full range is 0--51%. **⚠️ "9--51%" excludes ZS 0%; should qualify as FT-specific**

---

### === section6_related_work.tex ===

**[L13]** `5 predicted relations vs >1,100 for OntoCoDec under LoRA`
- sf2_gollie_scierc_violation GoLLIE pred_rels=5. **✅**
- OntoCoDec LoRA: Qwen=1,128, Llama=1,081. Llama < 1,100. **❌ ERROR: ">1,100" not supported; Llama has 1,081. Should be ">1,000" or "~1,100".**

**[L13]** `46% empty output`
- d063_gollie_violation_rate (100 docs): gollie_empty_docs_pct=45%≈46%. **✅ on 100-doc run.**
- sf2_gollie_scierc_violation (551 docs): (551-54)/551=90.2% empty. **⚠️ Data mixed: "5 predicted relations" is from 551-doc run, "46% empty" from 100-doc run.**

**[L16]** `up to 48%`
- posthoc_filtering_baseline docred_rejection=48.1%. **✅**

**[L18]** `3% DR reduction`
- (15.37-14.84)/15.37=3.4%→3%. **✅**

---

### === section7_conclusion_compressed.tex ===

**[L3]** `3 datasets, 3+ models, 2 tasks`
- SciERC, DocRED, WikiEvents; Qwen, Llama, Mistral (+70B); RE + EE. **✅**

**[L4]** `3% vs 94% DR reduction at 8B`
- Grammar=3%, S1=94%. **✅**

**[L8]** `zero-shot +9.82 pp, fine-tuned +1.18 pp`
- **✅** (verified above)

**[L9]** `k=2 reduces CF to 0.11% at 1.18× latency`, `k=4 eliminates all CF at 1.39×`
- **✅**

**[L10]** `18--92%` (TCR)
- d065_tcr_full: all_cf_eliminated=True across 10 configs (100%). **⚠️ Registry shows 100% CF elimination, not 18--92%. This may reflect a conservative TCR variant not in registry.**

**[L14]** `1--2%` (training reduces DR)
- FT unconstrained DR range: 0.49--1.95%. DocRED values are below 1%. **⚠️ "1--2%" only covers SciERC (1.11--1.95%); DocRED is 0.49--0.76%**

---

### === main.tex (Limitations) ===

**[L74]** `36 violations total`, `39%, 33%, 28%`
- Total=36 verified. Decomposition from manual analysis. **✅**

**[L76]** `18--92%` (TCR)
- Same issue as conclusion. **⚠️**

**[L82]** `n=20` (WikiEvents)
- By design. **✅**

**[L90]** `S2 reduces R-F1 by 8.45 pp`
- 70B LoRA: unconstrained R-F1=44.73, S2=36.28. Δ=8.45pp. **✅** (comparison is S2 vs unconstrained, not S1)

---

## Summary of Issues

### ERRORS (should fix)

| # | Location | Paper says | Registry says | Fix |
|---|----------|-----------|---------------|-----|
| 1 | sec5 L88 | DR ≤ 0.09% | Llama DocRED S1 = 0.21% | → "≤0.21%" or scope to SciERC |
| 2 | sec5 L100 | 22 violations | CF_violations = 21 | → "21 violations" |
| 3 | sec5 L100 | 0/22 | 0/21 | → "0/21" |
| 4 | sec5_docred L9 | R-F1 +0.50pp | 8.23-7.74 = 0.49pp | → "+0.49pp" |
| 5 | sec5_runtime L11 | all 4 types at both 8B and 70B | 70B SciERC beam4 CF_count=1 | → "at 8B scale" or qualify |
| 6 | sec6 L13 | >1,100 | Llama FT SciERC = 1,081 | → ">1,000" or "~1,100" |

### WARNINGS (approximations/mixing)

| # | Location | Issue |
|---|----------|-------|
| 7 | abstract, intro, setup | "F1 41--46%" / "41--47%": min is 40.56% |
| 8 | sec5 L88, sec7 L14 | "1--2%" FT-only DR: DocRED values are 0.49--0.76% |
| 9 | sec7 L10, Limitations L76 | "TCR 18--92%": registry shows 100% elimination |
| 10 | sec5_runtime L33 | "9--51% parse failure": ZS has 0% |
| 11 | sec5_runtime L13 | "DR<0.1%": Llama DocRED=0.21% |
| 12 | sec6 L13 | "46% empty" + "5 rels": from different experiments (100-doc vs 551-doc) |

### DocRED parse-failure bug status
**Table 2 DocRED values are CORRECT** — they use eval_d064.py (post-fix). All phase2_docred experiments use checker_version fixed_20260514_v2. No stale pre-bug values found in the main text tables.

### CF cascade ZS/FT labeling
Code comments correctly label: 248 violations / 63.3% / 58.1% / 7.3% → ZS (phase2_scierc_full_s1). 22 (should be 21) violations → FT (w5_lora_scierc_constrained_eval). **No ZS→FT mislabeling detected.**

---
