# cpu paperbanana method fig

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_cpu_paperbanana_method_fig_20260525T062336_result.json`
- **Structured JSON:** [`9fe45f0faa287b56acaf.json`](../../sessions/9f/9fe45f0faa287b56acaf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both PNG (403KB, 300 DPI) and PDF (57KB, vector) are generated. The `save_fig` in `palette.py` already produces a proper vector PDF directly from matplotlib, which is higher quality than the PNG→PDF rasterization path in Step 5 — so the PDF is already optimal.

**Summary**: PaperBanana couldn't be used (TUM proxy key incompatible with direct Google API). Fell back to hand-drawn matplotlib with FancyBboxPatch/FancyArrowPatch. Three-panel figure:
- **(a)** ThreadGate Architecture — residual stream with gating circuit, Gate MLP, skip connection
- **(b)** Training & Evaluation — loss components + TF/AR exposure bias gap (8–17×)
- **(c)** Diagnosis & Fix — causal exclusion chain → β-Steering + Scheduled Sampling

Output: `figures/paper/fig_method_framework.{png,pdf}`, script: `figures/paper/gen_fig_method_framework.py`.

---
