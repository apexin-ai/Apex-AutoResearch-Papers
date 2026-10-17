# ARR Submission Pre-Check: Supplementary Material + Checklist

Updated: 2026-05-22

---

## 2. Supplementary Material

### a) Appendix Sections (in main.pdf)

All appendices are embedded in `main.tex` after `\appendix` (starting ~line 57). 25 sections total:

| # | Section Title | Label | Content Summary |
|---|--------------|-------|-----------------|
| A | Additional Figures | `sec:appendix_figures` | Cross-model count-curve tables (8B, 32B), cross-model BCS tables, error taxonomy (IntraSub/Missed by BCS bin), cross-model error taxonomy replication |
| B | SDGD Full Protocol and Results | `sec:appendix_sdgd` | Graph-coloring decomposition protocol, 4-mode comparison table, v2 confidence-gated merge |
| B.1 | Practical Routing Strategies on RE | `sec:appendix_routing` | 5 non-oracle routing strategies on FewRel 80-rel RE |
| C | Factorial Analysis and Separability Test | `sec:appendix_factorial` | Count×BCS regression, TOST equivalence, logit-scale sensitivity, DocRED factorial, range-matched robustness |
| D | Within-Pool CI Details | `sec:appendix_within_pool` | 80-pool 16-sub quartile Δ CI interpretation |
| E | Controlling for Centrality Confounds in MAVEN | `sec:appendix_residualized_bcs` | MiniLM/Qwen3 partial correlations, centrality artifact analysis |
| E.1 | Partial Correlation: Controlling for Degree Centrality | `sec:appendix_partial_corr` | FewRel/DocRED partial correlations, ridge regression under multicollinearity |
| E.2 | NER BCS-Null Power Analysis | `sec:appendix_ner_power` | BCS variance restriction analysis, minimum detectable |r| |
| E.3 | Bootstrap CI Robustness | `sec:appendix_bootstrap_ci` | Cluster-robust inference for shared-instance batches |
| E.4 | Domain Distribution in Extreme-BCS Batches | `sec:appendix_domain_distribution` | χ² domain composition analysis, mediator argument |
| F | Batch Composition Results | `sec:appendix_batch_composition` | Oracle routing accuracy table |
| G | Prompt Templates | `sec:appendix_prompts` | Full prompt templates (v1, v2, etc.) |
| H | Prompt Version Sensitivity Analysis | `sec:appendix_prompt_sensitivity` | RE/NER replication under v2 prompt |
| H.1 | Cross-Prompt-Variant BCS Correlation | `sec:appendix_prompt_variants` | 4 prompt variants × 2 count levels |
| I | BCS Aggregation Sensitivity | `sec:appendix_bcs_sensitivity` | Mean vs. max SCS aggregation comparison |
| J | BCS-Controlled Detailed Results | `app:bcs-controlled-table` | Full BCS-controlled accuracy table, adjusted R² |
| K | Format Independence | `app:format-independence` | Paired constrained vs. unconstrained decoding, per-batch table |
| L | Within-Pool Analysis Methodology | `app:within-pool-method` | 3-way BCS–accuracy table, permutation tests |
| M | SCS Embedding Ablation | `app:scs-ablation` | Name-only vs. name+definition, held-out validation |
| N | Pair-to-Batch Aggregation Simulation | `app:aggregation-sim` | Monte Carlo simulation, unconditional baseline, ecological inference |
| O | BCS Independence from Type Composition | `app:bcs-composition` | Variance decomposition (BCS unique vs. composition unique) |
| P | SCS vs. Simple Baselines | `app:scs-baselines` | SCS vs. WordNet/Levenshtein/same-parent |
| Q | Split-Origin Covariate Analysis | `app:split-origin` | Train/val origin confound control |
| R | Cross-Seed Variance Decomposition | `app:variance-decomposition` | Batch SD vs. seed SD table |
| S | Cross-Domain Connections | `app:cross-domain` | SGD/SGD-X analogy, practical implications |
| T | Cross-Model: LLaMA-3.1-70B-Instruct | `sec:appendix_cross_model_70b` | Full 70B replication (count curves + BCS) |
| U | Cross-Model: Gemini 2.5 Flash | `sec:appendix_cross_model_gemini` | Gemini count curves + BCS, leverage-point analysis |
| V | Few-Shot Prompting and Confusability | `sec:appendix_fewshot_bcs` | 0/1/5-shot BCS gap analysis |
| W | Qualitative Error Analysis | `app:error-analysis` | Top-10 confused pairs (RE + NER), illustrative examples |
| X | Schema Label Renaming Experiment | `app:renaming` | SCS-reduction intervention, label unfamiliarity effect |
| Y | Relaxed Matching Evaluation (NER) | `app:relaxed-matching` | 4 matching modes, per-error-mode analysis |

**Status**: ✅ All appendices are in main.pdf (confirmed by `\appendix` in main.tex). No separate appendix file needed.

### b) Independent Supplementary

- **Code availability mention**: "Code and data will be released upon acceptance" appears in:
  - Introduction footnote 2 (line 4 of introduction.tex)
  - Checklist C4 (checklist.tex line 75)
- **No anonymous GitHub URL** is present in the paper PDF. The anonymous repo is prepared at `artifacts/anonymous_github/` (contains `src/`, `scripts/`, `data/`, `requirements.txt`, `LICENSE`, `README.md`) but has **not been uploaded** to anonymous.4open.science yet.
- **ARR supplementary policy**: ARR accepts a single supplementary PDF or ZIP via the OpenReview form. Since all appendices are in-paper, the supplementary field can be used for the anonymous GitHub link or a ZIP of the code.

**Action needed**:
1. Upload `artifacts/anonymous_github/` to https://anonymous.4open.science/
2. Before upload, verify no path leaks: `grep -r '/root/' artifacts/anonymous_github/`
3. Paste the anonymous GitHub URL in the OpenReview supplementary field

### c) Data/Code Citations

| Artifact | Citation | Location | Status |
|----------|----------|----------|--------|
| Few-NERD | `\citep{fewnerd-2021}` | §3.1, checklist B1 | ✅ PASS |
| FewRel | `\citep{fewrel-2018}` | §3.1, checklist B1 | ✅ PASS |
| DocRED | `\citep{docred-2019}` | §3.1, checklist B1 | ✅ PASS |
| MAVEN | `\citep{maven-2020}` | §3.1, checklist B1 | ✅ PASS |
| Qwen3-32B | `\citep{qwen3-2025}` | §3.5, checklist B1 | ✅ PASS |
| LLaMA-3.1 (8B/70B) | `\citep{llama3-2024}` | §3.5, checklist B1 | ✅ PASS |
| Gemini 2.5 Flash | `\citep{gemini-2025}` | §3.5, checklist B1 | ✅ PASS |
| vLLM | `\citep{vllm-2023}` | §3.5, checklist B1/C4 | ✅ PASS |
| all-MiniLM-L6-v2 | `\citep{minilm-2020}` | §3.2, checklist B1 | ✅ PASS |
| transformers/scikit-learn | Not cited individually | — | ℹ️ N/A (standard libraries; not required by ARR) |

**Status**: ✅ PASS — All datasets, models, and key tools have proper citations.

---

## 3. ARR Responsible NLP Checklist

> Note: EMNLP 2026 checklist is filled in OpenReview submission form, not in PDF. The paper includes a `checklist.tex` but it is commented out in main.tex (`% \input{checklist}`). This is correct per EMNLP 2026 policy.

### A. For Every Submission

| # | Question | Answer | Location / Justification |
|---|----------|--------|--------------------------|
| A1 | Limitations described? | **YES** | Limitations section (after §6, p.8–9). 6 items: (1) model coverage, (2) effect size/statistical design, (3) task scope, (4) causal mechanism/contamination, (5) domain/language scope, (6) multiple comparisons. Plus paragraphs on across-batch correlation and multiple comparisons. |
| A2 | Potential risks discussed? | **YES** | Limitations section. SCS/BCS misuse as deployment criterion noted. |
| A3 | Abstract/intro summarize claims? | **YES** | Abstract (3 findings), §1 (4 findings + 3 contributions). |
| A4 | AI assistant use reported? | **YES** | checklist.tex A4: Claude for writing assistance and code development. |

### B. Scientific Artifacts

| # | Question | Answer | Location / Justification |
|---|----------|--------|--------------------------|
| B1 | Creators cited? | **YES** | §3.1 (datasets), §3.5 (models). All 9 artifacts cited (see §2c above). |
| B2 | License/terms discussed? | **YES** | checklist.tex B2: CC-BY-SA 4.0 (Few-NERD), research-use (FewRel/DocRED/MAVEN), model licenses, API ToS. |
| B3 | Consistent with intended use? | **YES** | checklist.tex B3: All datasets used for IE evaluation. |
| B4 | PII/offensive content? | **N/A** | No new data collection. Established benchmarks. |
| B5 | Artifact documentation? | **YES** | Table 1 (dataset stats), §3.1 (provenance, sampling). |
| B6 | Relevant statistics? | **YES** | §3.1, Table 1, §3.3. |

### C. Computational Experiments

| # | Question | Answer | Location / Justification |
|---|----------|--------|--------------------------|
| C1 | Parameters/compute/infrastructure? | **YES** | §3.5: model sizes (8B/32B/70B), FP8, NVIDIA RTX PRO 6000 (96GB), ~72 GPU-hours inference, no training. Gemini via API. |
| C2 | Experimental setup/hyperparameters? | **YES** | §3.3 (count curves, BCS-controlled design), §3.5 (greedy, temp=0, seed=42). No hyperparameter search. |
| C3 | Descriptive statistics? | **YES** | 95% bootstrap CIs (B=10,000), Spearman with p-values (§4), permutation tests, semipartial R². |
| C4 | Implementation details? | **YES** | §3.5: vLLM v0.20.2, embedding model versions. Code release upon acceptance. |

### D. Human Annotators

| # | Question | Answer | Location / Justification |
|---|----------|--------|--------------------------|
| D1–D5 | All human annotation questions | **N/A** | No human annotation or crowdsourcing. |

### E. AI-Assisted Research

| # | Question | Answer | Location / Justification |
|---|----------|--------|--------------------------|
| E1 | AI assistant use reported? | **YES** | A4: Claude for code development and document formatting. Research design/execution/interpretation by authors. |

---

## Items Requiring Action

| Priority | Item | Details | Suggested Fix |
|----------|------|---------|---------------|
| 🔴 HIGH | Anonymous GitHub not uploaded | Code repo prepared at `artifacts/anonymous_github/` but no URL in paper or OpenReview | Upload to anonymous.4open.science, add URL to OpenReview supplementary field |
| 🟡 MED | Path leak check before upload | anonymous_github may contain `/root/` paths | Run `grep -r '/root/' artifacts/anonymous_github/` and sanitize |
| 🟢 LOW | checklist.tex vs OpenReview consistency | Paper has `checklist.tex` (commented out correctly); ensure OpenReview form answers match | Copy answers from this document when filling the OpenReview form |
| 🟢 LOW | Compute budget for Gemini | C1 mentions ~72 GPU-hours for open-weight models; Gemini API cost not quantified | Consider adding "Gemini API cost: $X" or noting "API cost not reported" in OpenReview form C1 |

No checklist items need to be changed from YES→NO or vice versa. The checklist is complete and accurate.
