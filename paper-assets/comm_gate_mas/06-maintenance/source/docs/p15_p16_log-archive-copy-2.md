# P1.5 + P1.6 Discussion Precision Edits

**Date:** 2026-04-26
**File:** `artifacts/paper/sections/discussion.tex`

## Changes Applied

### P1.5 #1: Cascade dissolution testable hypothesis (line 4)
- Added formal conjecture with two jointly-sufficient conditions: cascade rate > 50% and bigram novelty < 10%
- Includes empirical anchors: Qwen-7B (90.7%, 5.7%), Llama-7B (61.9%, verified), MATH boundary (16.6 tokens, 33% novelty)
- All numbers verified against appendix sources

### P1.6 #1: Falsifiability discussion (line 5)
- Added immediately after conjecture: two falsification criteria (low-cascade-safe, high-cascade-informative)
- References Gemma-2-9B intermediate profile via `app:statistical` (no Gemma-specific label exists)

### P1.5 #2: Two-agent limitation bridge (line 27, limitations)
- Replaced generic "Multi-agent pilots suggest cascades are topology-emergent" with mechanistic prediction linking cascade dissolution to multi-agent topologies
- Uses correct label `app:multiagent` (verified; `app:three_agent` does not exist)

### P1.6 #2: Temperature mechanism (line 27, limitations)
- Added oracle suppression drop 36.6% → 28.0% under t=0.7, with mechanistic explanation
- Numbers verified: both from results.tex Table 2 (Llama/GSM8K rows)

## Compressions (to maintain page budget)

| Location | Compression |
|----------|------------|
| Paragraph 1 | "neutralize double dissociation ... argues against a noise hypothesis. Zero error correction with divergent" → "double dissociation ... rules out noise. Divergent" |
| Paragraph 2 | Removed "Oracle validation isolates true ack pruning from heuristic artifacts:" wrapper; shortened suppression sentence |
| Scale invariance | "The ack-pruning safety margin is consistently stable across model scale" → "Ack-pruning safety is stable across scale"; trimmed closing sentence |
| Limitations (heuristic) | "relies on a character-length threshold that requires" → "character-length threshold requires"; "threshold re-tuning" → "re-tuning" |
| Limitations (kappa) | Removed "two annotators independently classifying ... under the same 5-class protocol used for LLM annotation"; compressed FG/efficiency sentence |

## Verified References
- `\ref{app:cascade}` — exists
- `\ref{app:statistical}` — exists (used for Gemma cascade profile)
- `\ref{app:multiagent}` — exists (three-agent pilot)
- `\ref{app:temp-robustness}` — exists
- 90.7%, 61.9%, 5.7%, 16.6, 0.333, 36.6%, 28.0% — all sourced from appendix/results
