# paper writing method

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_writing_method_20260515T045157_result.json`
- **Structured JSON:** [`956f77784d361d9a5ea7.json`](../../sessions/95/956f77784d361d9a5ea7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Verification complete. All 5 checks pass:

1. **Section hierarchy**: `\section` → 4 `\subsection`s (Preliminaries, Stage 1, Stage 2, Stage 3)
2. **Equation labels**: `eq:importance`, `eq:cka`, `eq:overlap`, `eq:score` — all present
3. **Algorithm syntax**: Uses `\State`, `\For`, `\If`, `\Require`, `\Ensure` (algpseudocode) — no algorithm2e commands
4. **Citation keys**: All 8 keys (`rlsqueezes2026`, `ainslie2023gqa`, `shao2024grpo`, `selfhealing2025`, `resp2025`, `kornblith2019cka`, `mpruner2024`, `lachance2024cka`) verified in `references.bib`
5. **No 35% sparsity**: Only "20\% sparsity" appears (line 86, capacity floor context)

Three key changes from the existing draft:
- **Per-layer capacity floor** (lines 81–86): ≥40% MLP groups retained per layer (≥12/28), prevents representational collapse from unconstrained global ranking
- **Two-stage recovery** (lines 91–111): SFT warmup (restore EOS & format) → GRPO (restore reasoning), motivated by EOS collapse in direct GRPO on pruned models
- **Algorithm 1** (lines 113–151): Converted from broken algorithm2e syntax to proper algpseudocode; added capacity floor constraint loop and two-stage recovery steps with `$\mathcal{D}_\text{sft}$`/`$\mathcal{D}_\text{rlvr}$` inputs

---
