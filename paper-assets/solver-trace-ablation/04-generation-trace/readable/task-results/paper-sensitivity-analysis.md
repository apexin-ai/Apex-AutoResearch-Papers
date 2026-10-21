# paper sensitivity analysis

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_sensitivity-analysis_20260521T181245_result.json`
- **Structured JSON:** [`61b326b426ae72c513b1.json`](../../sessions/61/61b326b426ae72c513b1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Both edits are in place.

**Summary of changes:**

1. **appendix.tex** — Added new subsection "Sensitivity to Seed 43 Exclusion" (`\label{app:sensitivity-s43}`) with:
   - Paragraph explaining why s43 is problematic across all 3 conditions
   - Table `tab:sensitivity-no-s43` with 2-seed (s42+s44) pooled stats for Exec-only, ISR β=0.1, and Random β=0.1
   - Note on 3-seed exec-only being dominated by s43's greedy collapse variance

2. **experiments.tex** — Updated the footnote reference from `Appendix~\ref{app:detailed-results}` to `Appendix~\ref{app:sensitivity-s43}, Table~\ref{tab:sensitivity-no-s43}`

Key numbers in the sensitivity table:
- **ISR TS amplification preserved**: 60.0% (ISR) vs 0% (Random) — consistent with 3-seed 71% vs 14%
- **N-H rates low everywhere**: 3.7% (Exec) / 8.2% (ISR) / 14.3% (Random)
- **CE→TS shift under ISR**: ISR TS=60%/CE=25% vs Random TS=0%/CE=78%
- **3-seed exec-only pooled**: not separately tabled since s43 T=0.7 makes it unreliable; noted in text that 2-seed mean (PR=95.5%) better characterizes the non-degenerate regime

---
