# paper wiki narrative d060

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_wiki-narrative-d060_20260517T234003_result.json`
- **Structured JSON:** [`23c95f07d2b86d54fff3.json`](../../sessions/23/23c95f07d2b86d54fff3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All updates done. Here's the summary:

---

## Completed changes

**experiments_c1.tex (Section 5.5 Cross-Domain Variation)**:
- Restructured into three clear paragraphs: arXiv K*=3 (5-model cross-validation), Wikipedia K*=1 (single-generation saturation), Domain as sole dominant factor
- arXiv evidence now cites boundary-pair 2v3 AUC range (0.6215--0.6544) instead of irrelevant 1v2 range
- Wikipedia framed as "simplest domain tested, encyclopedic regularity, single generation suffices"
- Scorer confound as explicit methodological disclosure: "+1 depth bias under same-family scoring, specific to Qwen on Wikipedia"
- Updated table caption: "(scorer-controlled)", "Raw same-family scoring yields K*=2; controlled value shown"

**discussion.tex (Domain dependence paragraph)**:
- "two independent model families" → "five models spanning four architecture families"
- Added explicit "+1 inflation" mechanism
- Added closing sentence: "Source-domain structural complexity is the sole factor that systematically shifts K*"

**appendix_extended.tex**: Already correct, no changes needed.

---

## introduction.tex: lines needing sync (do not modify, flagging only)

**Line 21** (contribution b):
```
\item \textbf{Domain dependence of $\Kempirical$}: C4 web text yields $\Kempirical{=}2$ (7/8 model configurations), while structured academic text (arXiv) yields $\Kempirical{=}3$, consistent across model families (Section~\ref{sec:cross_domain}).
```
Suggested update:
- "consistent across model families" → "consistent across five models and four architecture families"
- Consider adding Wikipedia to complete the hierarchy: "...yields K*=3 (five models, four architecture families); Wikipedia yields K*=1 (six models, scorer-controlled), producing a three-level hierarchy governed by domain structural complexity"

This is the only introduction line with a direct factual gap relative to the updated experiments section.

---
