# analysis cosine number discrepancy

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_cosine_number_discrepancy_20260522T184356_result.json`
- **Structured JSON:** [`8f87ed449e1e20f6f975.json`](../../sessions/8f/8f87ed449e1e20f6f975.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the full picture:

## Findings

### 1. Worker results: 520 traces, no filtering
- JSON: `n_traces: 520`, `n_step_pairs: 403776`
- The script processes all 520 .pt files, only skipping traces with `n_steps < 2` (none were skipped — all 520 passed)
- L2 = 0.306824, L14 = 0.471799, ratio = 0.472/0.307 = **1.54×**

### 2. Paper already uses the corrected numbers
The appendix.tex has **already been updated** to match the Worker results:
- Line 180: "deep-layer mean cosine distance (0.472) is $1.54\times$ the shallow-layer mean (0.307)"
- Line 204: "volatility ratio $1.54\times$"
- Line 253 (cross-arch table): R1-8B = $1.54\times$

**0.265 does not appear anywhere** in the current paper source. The old numbers (0.265/0.442/1.67×) are not in appendix.tex anymore.

### 3. Stale 1.67× remains only in draft/rebuttal files
- `rebuttal_letter_draft.md` — 4 occurrences of 1.67×
- `_drafts/author_response_template.md` — 3 occurrences of 1.67×

These are not part of the compiled paper but should be updated for consistency.

### 4. Root cause
The original 0.265/0.442/1.67× numbers likely came from an earlier cosine analysis with a different methodology (possibly different layer range definitions or different step-pair selection). The Worker recomputed on the full 520-trace set with explicit probe-selected layers (L2 vs L14) and got 0.307/0.472/1.54×. The paper has already been corrected.

### Recommendation
- **Paper (appendix.tex)**: Already correct — no action needed.
- **Rebuttal drafts**: Update 7 stale references from 1.67× to 1.54× if these drafts will be used.

---
