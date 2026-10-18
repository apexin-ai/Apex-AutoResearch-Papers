# writing warning review fixes

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_warning-review-fixes_20260515T200308_result.json`
- **Structured JSON:** [`9d595445dc78326b90a7.json`](../../sessions/9d/9d595445dc78326b90a7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 7 modifications complete. Summary:

| # | Item | File | Change |
|---|------|------|--------|
| 1 | R1-N1 EDD formula | `method.tex:94` | Added empty-set convention (`EDD_T=0` when no pair meets threshold) and non-monotonic caveat in footnote |
| 2 | R2-N2 Literature | `related_work.tex:21,31-33` | Added watermarking \cite{kirchenbauer2023_watermark} to detection paragraph; added new "Ordinal Classification" paragraph citing CORAL and CLOC |
| 3 | W3 LoRA | `method.tex:33` | Added parenthetical definition: "low-rank adaptation that freezes pretrained weights and injects trainable rank-decomposition matrices" |
| 4 | W5 Unconditional gen | `method.tex:34` | Clarified "not continuation of a given prompt or prefix" |
| 5 | W6 Per-class recall | `generalization.tex:96-98` | Expanded cross-strategy paragraph to explicitly report d0 (≥89.5%) and d2 (3.7-19%) per-class recall breakdown |
| 6 | R2-W2 Terminology | — | **No changes needed**: audit confirmed consistent usage of EDD formatting (`\mathrm{EDD}`), "decoding strategy", "feature-based methods", "statistical features", and "model family" |
| 7 | R2-W6 Orphan bib | `references.bib` | Removed 3 orphan entries: `dsir2023`, `qurating2024`, `sugiyama2007_importance_weighting`. 0 missing entries found. |

---
