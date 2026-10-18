# paper writing efficiency subsection

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_efficiency_subsection_20260525T192453_result.json`
- **Structured JSON:** [`98990c38c4150c6d2426.json`](../../sessions/98/98990c38c4150c6d2426.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Inserted. Two changes made:

1. **`main.tex`**: Added `\newcommand{\placeholder}[1]{\textcolor{red}{[#1]}}` in the preamble (uses the `color` package already loaded by `corl_2026.sty`).

2. **`experiments.tex`** (lines 157-167): New `\subsection{Computational Efficiency}` with:
   - **Paragraph 1** (~150 words): Quadratic attention FLOPs formula (Eq. \ref{eq:flops_ratio}), concrete numbers for π₀.₅ (16% attention savings at k=0.9, 67% at k=0.5), notes that X-VLA's 50 tokens limit gains, and SmolVLA VTR at M=16 gives the largest practical compression (87.5%).
   - **Paragraph 2** (~30 words): Three `\placeholder{}` markers for wall-clock latency measurements (baseline, k=0.9, speedup %).

---
