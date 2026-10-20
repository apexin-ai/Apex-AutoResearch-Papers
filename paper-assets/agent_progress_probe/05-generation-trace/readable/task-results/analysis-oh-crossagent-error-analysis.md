# analysis oh crossagent error analysis

**Are Stagnation Signals Structural? A Systematic Empirical Study of Progress Detection in LLM Agents via Weak Supervision LLM-based agents deployed on software001** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_oh-crossagent-error-analysis_20260515T010007_result.json`
- **Structured JSON:** [`76abf09cff721c02c671.json`](../../sessions/76/76abf09cff721c02c671.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Key findings:

**Probe zero-shot on OH conf>=2 (43,366 windows):**
- macro_f1=0.581, error_rate=19.9% (8,643 errors)
- **80.5% of errors are FP** (stag→prog): probe has massive progress bias on OH embeddings
- **62% of errors are high-confidence** (prob>0.9 or <0.1) — not fixable by threshold tuning
- conf=3 windows: **70.6% error rate** — probe fails hardest where LFs are most unanimous
- Error rate uniform across trajectory positions (~20%), confirming global distribution shift

**Structural GB comparison:**
- Structural GB: macro_f1=0.998, only 57 errors
- **Error overlap: 2 out of 12,328 common windows** (0.08%) — completely disjoint error patterns
- Probe-only errors (2,458) are pure embedding-distribution-shift failures that structural features avoid entirely

**Root cause:** The SWE-trained probe learned embedding patterns for stagnation that don't transfer to OpenHands. OH stagnation windows "look like" SWE progress windows in embedding space. cmd_rep is the biggest confusion source — 88% of FN errors have cmd_rep=prog but the probe still predicts stag.

All outputs saved:
- Script: `oh_crossagent_error_analysis.py` on server
- Results: `results/oh_crossagent_error_analysis.json` on server
- Report: `artifacts/oh-error-analysis/report.md` locally
- Registry: `oh-crossagent-error-analysis` (DONE)

---
