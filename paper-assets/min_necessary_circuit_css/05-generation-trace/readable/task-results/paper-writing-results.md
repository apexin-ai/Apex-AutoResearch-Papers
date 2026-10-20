# paper writing results

**Transformer Model EAP-IG** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_results_20260518T130550_result.json`
- **Structured JSON:** [`ff27c5e8304cfd681e44.json`](../../sessions/ff/ff27c5e8304cfd681e44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Results section written to `docs/paper/sections/results.tex` and registered.

**Summary of what's in the file:**

- **Opening paragraph**: States the universal failure of CSS=1.0 across all 6 configurations, with a roadmap of the five distinct failure modes.
- **Table 1** (`table*`, booktabs): All 6 rows with CPR, Δ, bootstrap CI, p-values, and descriptive outcomes. Size-controlled (†) and bootstrap (‡) footnotes included.
- **GPT-2 IOI** (2 paragraphs): Uncontrolled CPR advantage (0.1095 vs 0.0286) shown to be a size artifact. Size-controlled at N=16: CSS=0.177 vs EP=0.183, p=0.279. Zero ablation: CSS ≡ ACDC at 0.0295.
- **Figure 2** placement with self-contained caption.
- **GPT-2 Arithmetic**: CSS=1.0 ≡ ACDC (17 edges). Collapse caused by isinf binarization asymmetry.
- **GPT-2 SVA**: Best case for CSS (+0.013 CPR), but p=0.099, not significant at α=0.05.
- **GPT-2 Factual Recall**: CSS significantly worse (p=0.000). Caused by EAP-IG×EP Jaccard=0.82 correlation.
- **Qwen-2.5 IOI**: Both configs yield 0 CSS=1.0 edges (empty consensus). IFR Jaccard with gradient methods = 0.00.
- **CIRCUS ablation**: Within-method threshold diversity also fails. IOI CPR=−0.108, SVA CPR=0.994, neither beats single-method baselines.

Style checks: zero em-dashes, zero AI-typical words, zero -ing phrase endings, all numbers verified against registry.

---
