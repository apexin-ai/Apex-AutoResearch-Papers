# writing paper assembly v3

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_writing_paper-assembly-v3_20260515T032531_result.json`
- **Structured JSON:** [`d0cfecf140e5c9fc4e48.json`](../../sessions/d0/d0cfecf140e5c9fc4e48.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis written to `artifacts/_project/paper/page_budget_analysis.md`.

**Headline numbers:**
- Current total body: **6,674 words** (Abstract 307 / Intro 874 / Related 900 / Method 1,140 / Experiments 2,600 / Discussion 613 / Conclusion 547)
- Floats: 4 figures + 4 tables → ~2.4 pages of float real estate
- 8-page prose budget: **~3,380 words** → need to cut **~3,200 words (~49%)**

**Biggest cut targets (priority order):**
1. **Experiments −1,500** — main body has too much per-seed narrative that duplicates the tables; §4.3 (Goodhart) and §4.4 (cross-logic) carry the bulk.
2. **Method −490** — move H1–H7 enumeration and reward-formulation variants to appendix (already redundant with Tab 1 + Tab 4).
3. **Related Work −450** — drop tangential cites (LoRP/FoVer, PROF, ProGRS, Kwa, Just, LLMorpheus).
4. **Discussion −365** — kill "Practical Implications" 5-item list and "Classifier Limitations" paragraph (duplicates Exp §4.4).
5. **Conclusion −365** — compress 3 findings to one sentence each; spin Limitations into a separate unpaginated section after References.
6. **Intro −225**, **Abstract −80** — light tightening.

**Must keep:** ISR 0.642→0.003 collapse trajectory, H7 64.5%/0% contrast, premise-count-matched 1.06× number, all 4 figures, Tabs 1–4 (or merge Tab 1+Tab 2), C006 "two semantics of low/high ISR" sentence in Discussion.

**Floats to revisit:** consider merging Tab 1 and Tab 2 (Tab 2 is a per-seed expansion of one Tab 1 row) for ~0.25 page; switch any `\textwidth` figure to `\columnwidth`.

**Open items flagged:** s43 random β=0.3 placeholder and fig:sta-overview asset existence — both unrelated to page budget.

---
