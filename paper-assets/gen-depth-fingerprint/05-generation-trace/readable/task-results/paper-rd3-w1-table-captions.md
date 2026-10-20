# paper rd3 w1 table captions

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_rd3-w1-table-captions_20260516T051618_result.json`
- **Structured JSON:** [`734320e2bd3fb57960c9.json`](../../sessions/73/734320e2bd3fb57960c9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 14 tables now have consistent `(6-generator LOGO; ...)` or `(6-generator data/dataset)` annotations at the end of their captions.

Summary of changes across 10 files:
- **results.tex**: Tables 1 (logo-results), 2 (ablation), 3 (baselines) — added `(6-generator LOGO; 3-class and binary.)` or `(6-generator LOGO; 3-class.)`
- **table4.tex**: Table 4 (cross-ref) — `(6-generator LOGO; 3-class.)`
- **appendix_classifier.tex**: alt-classifier + sampling-ablation tables
- **appendix_downstream.tex**: `(6-generator data; fine-tuning evaluation.)`
- **appendix_finer_depth.tex**: 5-class tables — `(6-generator LOGO; 5-class: gen-0 through gen-4.)`
- **appendix_lofo.tex, appendix_human_edit.tex, appendix_qlora.tex, appendix_confusion_matrix.tex, appendix_dataset_stats.tex**: each annotated with appropriate scheme

Format is now uniform: parenthetical at end of every caption specifying generator split and class scheme.

---
