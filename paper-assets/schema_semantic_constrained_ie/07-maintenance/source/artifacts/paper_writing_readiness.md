# OntoCoDec Paper Writing Readiness Report

> Generated: 2026-05-14 | Target: EMNLP 2026 ARR (May 25 deadline) | Days remaining: 11

---

## 1. Core Claims + Experimental Evidence

### Claim 1: Violation Landscape (Section 3)
**Status: FULLY SUPPORTED**

| Evidence | Exp ID | Key Metric |
|----------|--------|------------|
| SciERC unconstrained DR=15.4% (3x above 5%) | `mvp_phase0_violation_rate` | DR=15.37% |
| DocRED unconstrained DR=18.7% (14x larger ontology, comparable DR) | `mvp_phase0_violation_rate_docred` | DR=18.70% |
| Violation driven by constraint tightness, not ontology size | Both above | SciERC avg 26.1 valid pairs vs DocRED 5.68 |
| Per-relation: Compare 42.4%, Feature-of 33.5% vs Used-for 0.76% | `mvp_phase0_violation_rate` | per_relation_dr |

### Claim 2: Prompt Insufficiency (Section 3)
**Status: FULLY SUPPORTED**

| Evidence | Exp ID | Key Metric |
|----------|--------|------------|
| SciERC schema-informed: DR 15.4%→5.78% (-62.4%), still >5% | `mvp_phase0_scierc_schema` | DR=5.78% |
| DocRED schema-informed: DR 18.7%→12.8% (-31.3%), scales poorly | `mvp_phase0_docred_schema` | DR=12.84% |
| Evaluate-for regression +5.8pp (prior-constraint conflict) | `mvp_phase0_scierc_schema` | per_relation delta |
| Cross-dataset: 62% reduction (7 rels) → 31% (96 rels) | Both schema exps | Prompt scales poorly with complexity |

### Claim 3: Composable Constraint Framework (Section 4-5)
**Status: FULLY SUPPORTED (SciERC), PARTIALLY SUPPORTED (DocRED pending)**

| Evidence | Exp ID | Key Metric |
|----------|--------|------------|
| Grammar-only: RV→0%, ET→0%, DR unchanged, F1 neutral | `phase2_scierc_grammar_only` | RV=0%, ET=0%, R-F1=0.0823 |
| Semantic-only: DR↓24%, but RV/ET persist | `phase2_scierc_semantic_only` | DR=11.65% |
| Full S1: DR↓94%, RV→0%, ET→0%, F1 +0.13pp (neutral) | `phase2_scierc_full_s1` | DR=0.93%, R-F1=0.0836 |
| Enabling dependency: grammar prerequisite for semantic | Ablation comparison | semantic_only DR↓24% vs full_s1 DR↓94% |
| **DocRED grammar_only** | `phase2_docred_grammar_only` | **RUNNING (29/998)** |
| **DocRED full_s1** | `phase2_docred_full_s1` | **RUNNING (89/998)** |

### Claim 4: S1 vs S2 Architectural Ablation (Section 5 / Appendix)
**Status: FULLY SUPPORTED (ablation-level, not core contribution)**

| Evidence | Exp ID | Key Metric |
|----------|--------|------------|
| S2: DR=0.97%, CF=8.03%, R-F1=0.0803 | `phase2_scierc_full_s2` | All metrics ≈ S1 |
| S1 recommended: simpler, marginally better | Comparison | S1 wins DR, R-F1; S2 marginal CF |

---

## 2. Available Materials

### Tables (Data Ready)
| Table | Content | Source | Status |
|-------|---------|--------|--------|
| Table 1 | SciERC Phase 2 main results (5 modes) | `paper_results_summary.md` Section A | READY |
| Table 2 | DocRED Phase 0 prompt comparison | `paper_results_summary.md` Section B | READY |
| Table 3 | Cross-dataset prompt effectiveness | `paper_results_summary.md` Section B | READY |
| Table 4 | Per-relation DR breakdown (SciERC, 7 rels × 5 modes) | `paper_results_summary.md` Section C | READY |
| Table 5 | CF root cause analysis (EVR/WR subtypes) | `paper_results_summary.md` Section D2 | READY |
| Table 6 | S1 vs S2 trade-off | `paper_results_summary.md` Section D3 | READY |
| Table 7 | DocRED Phase 2 constrained results | — | BLOCKED (exps running) |

### Figures
| Figure | Content | Status |
|--------|---------|--------|
| Fig 1 | Architecture overview (Ontology→Compile→Decode) | DONE (`fig1_overview.pdf`) |
| Fig 2 | Per-relation DR violation heatmap (unconstrained→full_s1) | NOT CREATED (data ready) |
| Fig 3 | Ablation bar chart (DR% across 4 modes) | NOT CREATED (data ready) |
| Fig 4 | Cross-dataset prompt scaling (SciERC vs DocRED) | NOT CREATED (data ready) |
| Fig 5 | CF conflict pattern distribution | NOT CREATED (data ready) |

### Reports & Surveys
| Document | Status |
|----------|--------|
| `paper_framing.md` | Comprehensive (title, claims, reviewer Q&A, risk ranking, calibration) |
| `paper_results_summary.md` | Complete for SciERC; DocRED Phase 2 pending |
| `related_work_survey.md` | Detailed (20+ papers, 5 paradigms, differentiation analysis) |
| `literature_map.yaml` | Gap taxonomy + must-cite list (16 must-cite papers) |

### Code Artifacts
| Script | Purpose |
|--------|---------|
| `run_constrained_extraction.py` | Main experiment script (5 modes) |
| `violation_checker.py` / `_docred.py` | Violation analysis |
| `compare_prompts.py` | Prompt comparison + McNemar test |
| `analyze_ontology_docred.py` | DocRED ontology analysis |
| `run_extraction_docred.py` | DocRED extraction |

---

## 3. Missing Materials (Action Items)

### Critical (Must Have for Submission)

| # | Item | Blocker | ETA |
|---|------|---------|-----|
| M1 | DocRED Phase 2 grammar_only results | Running (29/998) | ~May 15-16 |
| M2 | DocRED Phase 2 full_s1 results | Running (89/998) | ~May 16-17 |
| M3 | Table 7: DocRED Phase 2 constrained results | M1+M2 | After M1/M2 |
| M4 | Fig 2: Per-relation DR heatmap | Data ready, need plotting | 1 hr |
| M5 | Fig 3: Ablation bar chart | Data ready, need plotting | 1 hr |
| M6 | Fig 4: Cross-dataset prompt scaling | Data ready, need plotting | 1 hr |

### Important (Strengthens Paper)

| # | Item | Blocker | ETA |
|---|------|---------|-----|
| M7 | Fig 5: CF conflict pattern visualization | Data ready | 1 hr |
| M8 | Bootstrap CI for F1 neutrality claim | Need script + compute | 2 hr |
| M9 | Evaluate-for error case analysis (prior-constraint conflict examples) | Need manual inspection | 2 hr |
| M10 | DocRED Phase 2 semantic_only (completes ablation on complex schema) | GPU time | ~6-8 hr |

### Stretch Goals (Nice to Have)

| # | Item | Blocker | ETA |
|---|------|---------|-----|
| M11 | Cross-model validation (Llama-3.1-8B) | GPU time + setup | ~12 hr |
| M12 | DocRED Phase 2 full_s2 | GPU time | ~8 hr |
| M13 | Decidability taxonomy formal treatment | Writing effort | 2 hr |

---

## 4. Writing Order Recommendation

### Phase A: Can Write NOW (no blockers)

| Section | Content | Dependencies | Est. Time |
|---------|---------|--------------|-----------|
| **Abstract** | Draft with SciERC results, placeholder for DocRED | None | 1 hr |
| **Section 1: Introduction** | Violation motivation + framework overview | `paper_framing.md` | 3 hr |
| **Section 2: Background** | Grammar-constrained decoding + IE ontology | `related_work_survey.md` | 2 hr |
| **Section 3: Violation Landscape** | Phase 0 empirics (SciERC + DocRED) | All Phase 0 data ready | 3 hr |
| **Section 4: Method** | OntoCoDec compiler + TypeConstraintProcessor + S1/S2 | Code + `paper_framing.md` | 4 hr |
| **Section 6: Related Work** | 5 paradigms + differentiation | `related_work_survey.md` + `literature_map.yaml` | 3 hr |
| **Section 7: Conclusion** | Draft with known results | None | 1 hr |

### Phase B: Needs DocRED Results (write after May 16-17)

| Section | Content | Dependencies | Est. Time |
|---------|---------|--------------|-----------|
| **Section 5: Experiments** | Full results tables + ablation + analysis | DocRED Phase 2 (M1-M3) | 4 hr |
| **Section 5.x: CF Analysis** | Limitation disclosure + root cause | CF data ready but DocRED needed for completeness | 2 hr |
| **Abstract/Intro revision** | Update with DocRED results | M1-M3 | 1 hr |

### Phase C: Polish (May 22-24)

| Task | Est. Time |
|------|-----------|
| All figures finalized (M4-M7) | 4 hr |
| Appendix (S2 details, per-relation tables, error examples) | 3 hr |
| Camera-ready formatting (EMNLP template, references, page limit) | 3 hr |
| Final proofread + claim calibration check | 2 hr |

---

## 5. Related Work Coverage Assessment

### Gap Taxonomy Coverage: GOOD

| Constraint Level | Covered? | Key Papers |
|------------------|----------|------------|
| Syntactic (JSON/CFG) | Yes | GCD (EMNLP'23), XGrammar, Outlines, LMQL |
| Vocabulary (entity/relation names) | Yes | GENRE (ICLR'21), AdaKGC (EMNLP'23), iNERD |
| Structural (generation order) | Yes | ATG (AAAI'24), EnriCo |
| Semantic (type checking, code gen) | Yes | PLDI'25, MGD (NeurIPS'23), Synchromesh (NeurIPS'22) |
| Ontology compliance (post-hoc) | Yes | ODKE+ (Apple'25), OntoLogX, SPIRES |
| Constrained decoding quality | Yes | CRANE (ICML'25), Grammar-Aligned (NeurIPS'24), Hidden Cost (RANLP'25) |
| OntoCoDec position (decode-time semantic for IE) | Clearly articulated | THE GAP |

### Must-Cite Papers: 16 identified
All listed in `literature_map.yaml` → `suggested_related_work_citations.must_cite`

### Potential Gaps in Coverage
| Area | Risk | Action |
|------|------|--------|
| ILP-based type constraints (pre-neural) | Covered (Roth & Yih 2004) | OK |
| Code-as-schema approaches | Covered (GoLLIE, CodeIE, KnowCoder) | OK |
| Biomedical IE with ontology | Partially covered (SPIRES, RELATE) | Consider adding 1-2 more bio-specific refs |
| LLM-based IE general surveys | Not explicitly listed | Add 1 recent survey (e.g., Li et al. 2024) |
| Zero-shot IE baselines | GoLLIE covered | OK |

---

## 6. Risk Assessment for Submission

| Risk | Severity | Mitigation Status |
|------|----------|-------------------|
| DocRED Phase 2 not done by May 19 | HIGH | Exps running; worst case: report Phase 0 only for DocRED |
| CF violation as attack surface | MEDIUM-HIGH | Root cause analysis done, proactive disclosure planned |
| Single model (Qwen3-8B only) | MEDIUM-HIGH | Cross-model is stretch goal; position as future work |
| Novelty perception ("PLDI'25 for IE") | MEDIUM | Differentiation clear in literature_map.yaml |
| F1 too low (~8%) for reviewers | MEDIUM | Zero-shot framing ready (C8 in paper_framing.md) |

---

## 7. Summary

**Overall Readiness: ~75%**

- Core claims supported by SciERC evidence
- DocRED cross-dataset validation is the critical blocker (2 exps running)
- 7 sections can be written NOW (Phase A), only Section 5 needs DocRED results
- 5 figures need creation (all data ready)
- Related work coverage is comprehensive (16 must-cite papers identified)
- Paper framing, reviewer Q&A preparation, and claim calibration are mature

**Recommended Next Actions (priority order):**
1. Monitor DocRED experiments → ensure completion by May 16-17
2. Start writing Phase A sections immediately (Intro, Method, Violation Landscape, Related Work)
3. Create figures M4-M6 in parallel (data ready)
4. Run bootstrap CI for F1 (M8) while writing
5. Complete Section 5 once DocRED results arrive
