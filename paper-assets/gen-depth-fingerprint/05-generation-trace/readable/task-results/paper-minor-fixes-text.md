# paper minor fixes text

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_minor-fixes-text_20260517T174958_result.json`
- **Structured JSON:** [`b23e9aecd2455c3d9aa4.json`](../../sessions/b2/b23e9aecd2455c3d9aa4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied and verified. Here's the summary:

| Fix | File | Change |
|-----|------|--------|
| **1 (R11-M2)** | method.tex:48 | Moved entropy=NLL footnote to inline text after first sentence of `\paragraph{Reference-model features.}`; deleted footnote from `entropy_mean` item (line 52) |
| **2 (R11-M3)** | method.tex:60 | Added rank range justification after tail_decay definition: high-frequency tokens (< 100) lack discriminative variance, ranks > 1000 are sparse/noisy |
| **3 (R11-M4)** | appendix_confusion_matrix.tex:1-2 | Expanded opening sentence to list all 6 generators by name; added sentence pointing to Table 1 (`tab:logo-results`) for the 8-gen evaluation |
| **4 (R11-M5)** | results.tex:66 | Replaced semicolon-joined threshold mention with separate sentence: "The six-fold magnitude gap between drifting ($\|\rho\| > 0.60$) and shape features ($\|\rho\| < 0.10$) serves as the operative criterion for the DDR split" |
| **5 (R11-M6)** | — | No change needed. `appendix_domain.tex:24` already explicitly states cross-domain used $t{=}1.0$ vs main $t{=}0.7$, with detailed comparability discussion |
| **7 (R11-M8)** | method.tex:56 | Rewrote entropy_min justification: leads with "Retained because removing it does not improve performance (LOFO ΔF1 = +0.01 pp, within bootstrap noise)" + four-number summary + marginal distribution shape rationale |
| **8 (R12-M1)** | method.tex:90 | Replaced vague "where multiple comparisons arise" with explicit scope: 21 distributional comparisons (7 features × 3 depth-group pairs) and 4 pairwise baseline comparisons, with section refs |
| **9 (R12-M2)** | results.tex:11 | Added crossover explanation after per-generator results: "reflects differences in gen-0 classification accuracy rather than in depth discrimination per se" |

---
