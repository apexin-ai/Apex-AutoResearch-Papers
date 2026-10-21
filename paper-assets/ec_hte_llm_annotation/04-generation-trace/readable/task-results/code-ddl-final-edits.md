# code ddl final edits

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_ddl-final-edits_20260524T031039_result.json`
- **Structured JSON:** [`8b29e2df98cd5c27ea0e.json`](../../sessions/8b/8b29e2df98cd5c27ea0e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All three changes are in place. Summary:

### Change 1 (L10): Ashwin 5× → Δπ translation
- Removed: `defined by refugee status, gender, and education level`
- Added: `, implying $\Delta\pi > 0.20$---well above the $0.15$ threshold at which EC-HTE becomes effective`

### Change 2 (L38): Contribution standalone value
- Replaced: `The bias identity applies beyond LLM annotation to any proxy classifier with subgroup-varying error rates; survey coding, medical diagnosis, and satellite imagery classification share this structure.`
- With: `The identity and diagnostic (contributions 1--2) are the primary results, useful without adopting any correction method; EC-HTE is one instantiation showing the identity prescribes effective correction.`

### Change 3 (experiments.tex L38 caption): MC SE bound
- Replaced: `MC SEs in Appendix~\ref{app:mcse}`
- With: `MC SEs $\leq 0.005$ for all entries (Appendix~\ref{app:mcse})`

### Space balancing
Compressed two sentences to maintain page budget:
- **L15**: removed redundant clause about naive estimator being unbiased (−14 words)
- **L17**: removed `empirically` and `semi-synthetic evaluations using ... spanning open-source and proprietary model families` (−8 words)

### Verification
- Conclusion on p8, Limitations on p9
- 0 undefined references/citations
- 31 pages total (unchanged)

---
