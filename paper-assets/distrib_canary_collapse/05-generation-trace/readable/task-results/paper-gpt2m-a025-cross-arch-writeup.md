# paper gpt2m a025 cross arch writeup

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_gpt2m_a025_cross_arch_writeup_20260516T123318_result.json`
- **Structured JSON:** [`e7e23f998cc38c0fbe38.json`](../../sessions/e7/e7e23f998cc38c0fbe38.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits complete. Summary of changes:

**`docs/paper/experiments.tex`** (3 locations):
1. **Lines 130-149** — Added `Table~\ref{tab:cross_arch_regime}`: cross-architecture regime map comparing Pythia-410M and GPT-2-medium at α=0.25 and α=1.0 (drift, Perm. Granger sig rate, Tier-3 count)
2. **Line 131** — Added text noting GPT-2m yields 1/8 Tier 3, 7/8 Tier 2 at α=0.25
3. **Lines 186-188** — Expanded "Failed canary candidates" paragraph with effective rank model-dependence: GPT-2m ER increases from 2.37→8.48 (+258%) vs Pythia decreasing

**`docs/paper/discussion.tex`** (2 locations):
1. **Lines 20-24** — Replaced old 3-line GPT-2m α=0.25 summary with expanded version: full drift profile (entropy -32.8%, ECE +422%, ppl -44.5%, d1 -23.5%, d2 -31.6%, d3 -30.2%, MAUVE -10.5%), Tier breakdown (1/8 T3, 7/8 T2), TY 1/8 sig
2. **Lines 42-48** — New paragraph "Effective rank direction is model-dependent": describes opposite ER directions, starting-point dependence explanation, caveat on representational metrics as universal canaries

All numbers sourced from `gen_wiki_gpt2m_a025_s42`. Claim language capped at "consistent across two transformer decoder-only model families of similar scale".

---
