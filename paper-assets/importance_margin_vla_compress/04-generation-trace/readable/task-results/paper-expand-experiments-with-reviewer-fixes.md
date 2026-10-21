# paper expand experiments with reviewer fixes

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_expand_experiments_with_reviewer_fixes_20260528T180603_result.json`
- **Structured JSON:** [`19ff79c08143b185b3bc.json`](../../sessions/19/19ff79c08143b185b3bc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied successfully. Summary of changes:

**Part A — 5 Reviewer fixes:**
1. **"≥98.0% through k=0.85"** (line 25): scoped to "On Object" + added `(Appendix Table~\ref{tab:full_results})`
2. **Δ symbol** (line 93): changed from `Δ(R−L2) = +36.0pp` to `Δ = −36.0pp`, consistent with method.tex definition (Δ = L2 − Random, positive = L2 better)
3. **VTR reframing** (lines 113): "exceeding the unpruned LoRA baseline by 15.3pp" + extended training control reference + "beneficial inductive bias" framing
4. **k=0.85 appendix refs** (lines 25, 108): both now cite `Appendix Table~\ref{tab:full_results}`
5. **SmolVLA baseline** (line 118): Table caption now explains "Baseline (44.8%) is our LoRA reproduction with smaller batch size; the official SmolVLA checkpoint achieves 59.2%"

**Part B — Content expansion:**
- **Setup** (lines 7-11): expanded from 2 sentences to 3 structured paragraphs (Benchmark with 4 suite descriptions, Models, Protocol with seed/eval details)
- **Cliff vs graded** (line 97): new paragraph explaining why random produces binary collapse while L2 maintains plateau
- **Inverted-U margin** (line 99): new paragraph with full profile analysis (peak at k=0.9, crossover at k≈0.7 with data, convergence at k=0.5)
- **Margin gradient** (line 108): expanded with mechanistic explanation

**Bonus:** all 3 em-dashes (`---`) removed per paper-writing-norms.

---
