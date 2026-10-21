# paper compute budget and fixes

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_compute-budget-and-fixes_20260517T125016_result.json`
- **Structured JSON:** [`767c06ad0fb34a9b17b0.json`](../../sessions/76/767c06ad0fb34a9b17b0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

No dashes found. All four modifications complete:

**Modified files:**

1. **`ethics.tex`** (lines 10-18):
   - **Line 10-12**: Licenses paragraph (Modification 2)
   - **Line 14-15**: Compute budget paragraph (Modification 1)
   - **Line 17-18**: Software/package versions paragraph (Modification 3)
     - Python 3.12.3, PyTorch 2.10.0 (CUDA 12.8), Transformers 4.57.6, XGBoost 3.2.0, scikit-learn 1.8.0, NumPy 2.2.6, pandas 3.0.2, SciPy 1.17.1

2. **`appendix_error_analysis.tex`** (line 20):
   - Removed `\resizebox{\linewidth}{!}{...}` wrapper from the table (Modification 4). The 5-column table fits at `\small` size without forced resizing, which was causing the 23.8pt overfull hbox.

---
