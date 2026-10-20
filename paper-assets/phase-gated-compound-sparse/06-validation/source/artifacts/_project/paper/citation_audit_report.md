# Citation Audit Report

Updated: 2026-05-16 (post-R10 revision)
Paper: Phase-Gated Compound Sparse (EMNLP 2026 ARR submission)

## Summary

- **Total unique citation keys**: 42
- **Verified**: 39
- **Minor issues**: 3 (cosmetic only, no action needed)
- **Fake / removed**: 1 (`mustafar-neurips2025` — LLM-hallucinated, deleted in R10)
- **Dangling references**: 0 (all tex \cite keys match bib keys exactly)
- **Unused bib entries**: 0 (all 42 bib entries are cited)

## MUSTAFAR Removal (R10-C1)

`mustafar-neurips2025` was an LLM-hallucinated citation ("Mustafar: Promoting Unstructured Sparsity for KV Cache Pruning", Joo et al.). It has been:
- ✅ Deleted from `references.bib`
- ✅ Deleted from all `.tex` files (no residual `\cite{mustafar...}`)
- ✅ Confirmed via full-text grep: zero matches in any `.tex` or `.bib` file

The real paper this was confused with: "Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference" (Joo et al., NeurIPS 2025, OpenReview C69741fMFX). Not cited in our manuscript.

## Full Audit

See `artifacts/_project/report/bib_audit_r10.md` for the per-entry verification table (42 entries, WebSearch-verified).

### Minor Issues (cosmetic, no action required)

1. **`snapkv-neurips2024`** — Title casing: "You Are Looking" vs official "You are Looking". Bib style overrides.
2. **`hold-onto-thought-neurips2025`** — Actual venue is NeurIPS 2025 ER Workshop (not main). Bib lists as arXiv preprint (acceptable). Citation key is slightly misleading.
3. **`deepseek-r1-2025`** — Author field uses "DeepSeek-AI" (arXiv convention). Nature version lists individual authors. Acceptable as-is.

## Cross-Check (2026-05-16)

Independent extraction of all `\cite{}` keys from 15 `.tex` files vs all `@entry{}` keys from `references.bib`:
- **42 keys in bib, 42 keys cited in tex** — perfect 1:1 match
- No orphaned bib entries, no undefined citations
