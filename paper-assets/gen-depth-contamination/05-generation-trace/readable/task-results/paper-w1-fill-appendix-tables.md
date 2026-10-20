# paper w1 fill appendix tables

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_w1_fill_appendix_tables_20260522T055736_result.json`
- **Structured JSON:** [`bb2aff7801dca6559a23.json`](../../sessions/bb/bb2aff7801dca6559a23.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 5 tables verified. Here's the final status:

**Table S10 (Pythia decoding ablation)** — FILLED. All 4 configs yield K\*=2. T=0.7 has marginal CI crossing at 2v3 (footnoted). Data from 10K bootstrap on exp-020 features.

**Table S11 (Length ablation)** — FILLED (previous session). K\*=2 for all 3 segment lengths.

**Table S12 (Domain ablation)** — FILLED (previous session). C4/Wiki K\*=2, arXiv K\*=3.

**Table S13 (Scorer sensitivity)** — PARTIALLY FILLED.
- Pythia-1.4B row now filled: Self=2, Pythia=2, OLMo=2 (from exp022 cross-scorer data)
- OLMo-1B, Qwen-7B, Mistral-7B: remain `---` — **NO DATA** for Pythia/OLMo cross-scorer experiments on these generators. exp019b\_mistral\_cross\_scorer exists but scorer identity is unspecified.

**Table 24 (Three-way ANOVA)** — FILLED. Key findings:
- Depth-Pair dominates (F=22738, η²\_p=.997)
- Generator is large (F=852, η²\_p=.866)
- Scorer is significant (F=17.5, p<.001) but small effect (η²\_p=.166)
- Caption updated: original claimed "non-significant Scorer" which contradicts data; now accurately describes modest Scorer variance
- df/N corrected: 3→2 generators, N=300 (not 400), residual df=264

---
