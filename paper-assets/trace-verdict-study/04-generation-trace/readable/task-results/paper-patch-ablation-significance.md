# paper patch ablation significance

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_patch_ablation_significance_20260516T043905_result.json`
- **Structured JSON:** [`ce2f6ce1a11db9cd082c.json`](../../sessions/ce/ce2f6ce1a11db9cd082c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`multirow` is already loaded. Both edits are complete:

**experiments.tex §4.4** (line 129-130): Replaced the vague "broadly overlapping CIs" description with specific bootstrap results — the 512→1024 significant drop (p=0.002), the 1024 vs no_trace non-significance (p=0.078), and the no_limit vs 1024 significance (p<0.001). Added Figure cross-reference.

**appendix.tex trace_length_full** (lines 261-310): 
- Updated the per-condition table caption to reference bootstrap CIs and the new pairwise table
- Added a 12-row pairwise bootstrap comparison table (Table `trace_length_pairwise`) organized in three groups: adjacent budgets, vs no_trace, vs exception_only
- Replaced the old discussion with three structured paragraphs: non-monotonic pattern analysis (with the "worst-of-both-worlds" interpretation for the 1024 dip), baseline comparisons, and interpretation — all backed by specific p-values and CIs from the bootstrap results

---
