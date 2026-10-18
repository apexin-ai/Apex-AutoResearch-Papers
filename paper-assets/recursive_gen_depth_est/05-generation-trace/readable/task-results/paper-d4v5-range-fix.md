# paper d4v5 range fix

**How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d4v5_range_fix_20260517T190239_result.json`
- **Structured JSON:** [`c49a356452f64e92a1d5.json`](../../sessions/c4/c49a356452f64e92a1d5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

The tex file uses a different representation (single averaged value 0.653, likely from a different context). The `[0.681, 0.694]` range only appeared in the markdown file.

**Results:**

| Model | d4v5 binary pairwise AUC |
|-------|--------------------------|
| GPT-2 XL | 0.681 |
| Pythia | 0.683 |
| OLMo | 0.684 |

Corrected range: **[0.681, 0.684]** (was [0.681, 0.694])

Fixed in `paper/theory_section_draft.md`. The tex file (`theory_draft.tex`) does not contain this range — it uses a single-point value (0.653) in a different context (geometric decay fitting across all depth pairs, not the 3-model range).

---
