# paper d219 final framing fix

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_d219_final_framing_fix_20260524T080020_result.json`
- **Structured JSON:** [`32cee1f6df5bac64881c.json`](../../sessions/32/32cee1f6df5bac64881c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All remaining matches are expected:
- **appendix.tex L731, L758, L780**: Shapley TODO areas — preserved per task instructions (等 Shapley 重算)
- **method.tex L7**: "forward significance rates spanning 0\% to 92\%" — treatment detection rates, not null FPR; correct to keep

Summary of changes across 8 files:

| File | Changes |
|------|---------|
| **abstract.tex** | "0% to 92%" → "3% to 92%" |
| **introduction.tex** | "0% to 92%" → "3% to 92%" |
| **method.tex** | DiffXCorr 16.7%→2.8%; reframed as bidirectional/unsuitable standalone; PermG "lowest" → "lowest among directional methods" (3 locations) |
| **method_reframe.tex** | Added directional qualifier + DiffXCorr 2.8% note (2 locations) |
| **conclusion.tex** | "lowest among all five" → "lowest among directionally-specific" + DiffXCorr note |
| **discussion_reframe.tex** | Same reframing; DiffXCorr 16.7%→2.8% |
| **limitations.tex** | "lowest among all five" → "lowest among directionally-specific" |
| **experiments_reframe.tex** | Same reframing (caught by verification grep) |
| **appendix.tex** | DiffXCorr table data 6/16.7→1/2.8, reordered table, updated caption, updated L804 text, updated L843-846 sensitivity paragraph with correct DiffXCorr weight (35.7), 4 directional qualifier fixes. Shapley TODOs preserved. |

---
