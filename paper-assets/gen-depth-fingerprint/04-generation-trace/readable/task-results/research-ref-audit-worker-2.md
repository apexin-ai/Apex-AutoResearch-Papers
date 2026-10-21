# research ref audit worker 2

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_ref-audit-worker-2_20260526T103724_result.json`
- **Structured JSON:** [`0eaa70597d21c0e08412.json`](../../sessions/0e/0eaa70597d21c0e08412.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Report written to `ref_audit_worker2.md`.

**Summary of findings across all 74 entries:**

- **0 hallucinated papers** — every entry corresponds to a real publication
- **4 issues found:**
  1. **`human_texts_outliers`** (CRITICAL) — wrong authors (Li, Yafu → Zeng, Cong), wrong subtitle, wrong venue (arXiv → NeurIPS 2025) for arXiv:2510.08602
  2. **`xu_spectrum_detection`** — venue outdated: bib says arXiv, paper published at EMNLP 2024
  3. **`two_birds`** — possibly accepted at SecureComm 2025 (verify)
  4. **`wu_survey_2025`** — missing volume/number/pages for published journal article
- **25 orphaned entries** in bib but not cited in any tex file
- **48 actively cited entries** all have accurate cite-context usage

---
