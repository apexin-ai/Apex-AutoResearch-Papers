# ARR May 2026 Submission Metadata

## Venue
- **Submission system**: ARR (ACL Rolling Review) May 2026 cycle
- **Target conference**: EMNLP 2026
- **Track**: Long Paper
- **Deadline**: 2026-05-25

## Paper Information

### Title
How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?

### Abstract
Training-free LLM information extraction degrades as schema complexity grows, yet prior work conflates two factors: type count and type confusability. We present what is, to our knowledge, the first controlled study isolating these factors across NER, RE, and event detection on four datasets. We quantify confusability via the Schema Confusability Score (SCS) and its batch-level aggregation, the Batch Confusability Score (BCS). Degradation operates along two dimensions with task-dependent effect structures: count-related recall decline (up to −49 pp on DocRED 96-relation RE) and confusability-related type substitution. In RE, BCS explains 22–58% of cross-batch accuracy variance (FewRel/DocRED), independent of output format (paired constrained/unconstrained comparison yields virtually identical correlations); NER shows no batch-level BCS signal, as errors scatter across missed entities and boundary failures. Schema decomposition fails due to merge amplification (NER, ED) and routing failure (RE). Both dimensions replicate across four models spanning three architecture families (Qwen, LLaMA, Gemini; 8B–70B), two decoding formats, and five prompt designs.

### Keywords
- information extraction
- schema complexity
- type confusability
- zero-shot / training-free
- large language models
- named entity recognition
- relation extraction
- event detection
- prompt engineering
- schema decomposition

### Authors
Anonymous (ARR double-blind review)

## Submission Checklist Status

| Item | Status | Notes |
|------|--------|-------|
| Main text ≤ 8 pages | ✅ | Verified: Conclusion ends on page 8, Limitations starts page 9 |
| Limitations section | ✅ | 6 items: model coverage, effect size, task scope, causal mechanism, data contamination, domain/language scope |
| Responsible NLP Research Checklist | ✅ | All A/B/C/D/E sections completed |
| Ethics considerations | ✅ | Covered in A2 (SCS/BCS misuse risk) |
| References | ✅ | All citations verified, Llama 3 "et al." rendering fixed |
| Anonymous submission | ✅ | \usepackage[review]{acl}, author = "Anonymous", no identifying URLs |
| Code/data release statement | ✅ | Footnote: "Code and data will be released upon acceptance." |
| AI assistant disclosure | ✅ | A4 and E1: Claude (Anthropic) for writing assistance and code development |
| Compilation | ✅ | 0 errors, 0 undefined references |

## Supplementary Material

### Already in paper (Appendix)
The appendix is included within the main PDF (pages 10–27) and covers:
- Additional figures and tables (cross-model, error taxonomy)
- Prompt templates (v1, v2, RE)
- BCS sensitivity analysis (cross-embedding)
- Factorial interaction tests (TOST equivalence)
- Format independence analysis
- Cross-model validation (Llama-8B, Llama-70B, Gemini 2.5 Flash)
- Prompt variant analysis
- Renaming experiment
- Relaxed matching evaluation
- SCS ablation (name-only vs. name+definition)
- MAVEN centrality analysis
- Variance decomposition
- Aggregation simulation

### Additional supplementary needed?
- **Code**: Not submitted now; will be released upon acceptance (per footnote)
- **Data**: Not submitted now; will be released upon acceptance
- **No separate supplementary PDF needed** — all appendix material is within the main document

## Pre-submission Final Checks
- [ ] Upload PDF to ARR OpenReview
- [ ] Copy-paste title and abstract into submission form
- [ ] Select keywords/topics in submission form
- [ ] Confirm paper type: Long Paper
- [ ] Verify PDF renders correctly on OpenReview preview
- [ ] Check all figures are visible and not cut off
- [ ] Verify no author-identifying information in PDF metadata (`pdfinfo main.pdf`)
