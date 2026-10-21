# paper round3 abstract refs

**Depth Profiling: Classifying Recursive Generation Depth in Base-Model LLM Text** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_round3-abstract-refs_20260516T044746_result.json`
- **Structured JSON:** [`cabb625fe7157470362a.json`](../../sessions/ca/cabb625fe7157470362a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits applied to both `artifacts/_project/paper/` and `docs/paper/`. Summary of changes:

### M7: Abstract 精简
- Shortened ordinal depth description: removed verbose gen-0/gen-1/gen-2+ parenthetical, replaced with "by generation depth rather than a binary real-vs-synthetic label"
- Removed `$p < 0.001$ vs.\ all baselines` → "significantly outperforming all individual detection baselines"
- Simplified "consistent with recursive generation inducing a location shift...without altering" → "consistent with a location shift...that preserves"
- Intro: `0.6B--8.2B parameters` → `spanning multiple scales`

### W4: Hypothesis framing
- Intro line 20: removed assertive "reflects" — changed from "We hypothesize that this pattern reflects recursive generation inducing..." to "We hypothesize that recursive generation induces...; under this account, the sampling mechanism governs..."
- Abstract was already hedged with "consistent with"

### MR: 补引用 (5 references)
- **energy_ood** (Liu et al., NeurIPS 2020) + **mahalanobis_ood** (Lee et al., NeurIPS 2018): added to bib; cited in intro line 12 alongside existing detectors, drawing OOD parallel
- **fineweb** (Penedo et al., NeurIPS 2024) + **dolma** (Soldaini et al., ACL 2024): added to bib; cited in intro line 24 (negative finding context) and related_work.tex data quality section
- **Gerstgrasser et al. 2024**: already in bib as `model_collapse_avoidable`, already cited in `related_work.tex` line 21 — no additional citation needed

All `\cite{}` keys match bib entries. All bib entries have matched braces. All references verified via WebSearch.

---
