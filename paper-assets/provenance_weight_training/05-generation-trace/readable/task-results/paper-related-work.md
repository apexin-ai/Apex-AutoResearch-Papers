# paper related work

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_related_work_20260515T233455_result.json`
- **Structured JSON:** [`9a667b784e959d386e04.json`](../../sessions/9a/9a667b784e959d386e04.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

`register_artifact` tool not available in current tool set. Draft written to:

`artifacts/_project/paper/related_work_draft.md`

**Changes vs existing `related_work.tex`:**
- Added "larger models can *amplify* rather than mitigate" detail from Dohmatob (stronger motivation)
- Tightened Drayson (ii): clarified SIR "discretizes into a resampled subset" vs our "preserving the full batch"
- Removed `yang_2026_data_mixing_agent` and `kuo_2024_data_weighting` from data mixing paragraph (not in task spec, streamlines word count)
- Added closing gap statement: *"no existing method provides principled, per-batch exponent selection… without validation set or known contamination proportions"*
- ~670 words, 4 paragraphs, all citations use `\citet{}`/`\citep{}` format

---
