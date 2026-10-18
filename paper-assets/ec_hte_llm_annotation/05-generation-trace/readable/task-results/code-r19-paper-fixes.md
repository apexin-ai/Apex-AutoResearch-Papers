# code r19 paper fixes

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_r19-paper-fixes_20260524T013802_result.json`
- **Structured JSON:** [`9bf311745143876f741e.json`](../../sessions/9b/9bf311745143876f741e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All checks pass. Summary:

| Check | Result |
|-------|--------|
| Undefined refs | 0 |
| Main text pages | 8 (Conclusion on p8) |
| Limitations | p9 (not counted) |
| Abstract words | 200 |

### Modifications applied

| # | Item | File | Lines |
|---|------|------|-------|
| 1 | SF2: A1 γ\_T=0.10 quantitative | theory.tex:98 | Replaced last sentence with coverage degradation figure |
| 2 | SF3: AUC=0.63 explanation | experiments.tex:73 | Added explanation sentence; trimmed K=2 meta-criterion detail |
| 3 | SF5: 7.4× stratified MLE comparison | experiments.tex:27 | Added 1.5× comparison to stratified MLE with partial pooling note |
| 4 | SF6: Finite-sample remainder | appendix.tex:100-105 | Added paragraph with CLT bound and κ-guard motivation; `stewart1990matrix` bib added |
| 5 | M7: Hyperprior robustness | method.tex:12 | Added "robust to 2× perturbation" parenthetical |
| 6 | M3: CausalForest bootstrap | experiments.tex:65 | Already present in footnote — confirmed, no change needed |
| 7 | Missing reference | related_work.tex:35, references.bib | Added Blette et al. sentence and bib entry |

Page compression: trimmed contribution 1 bullet (introduction.tex) and operating conditions paragraph (experiments.tex) to keep Conclusion on page 8. Abstract trimmed from 201→200 words.

---
