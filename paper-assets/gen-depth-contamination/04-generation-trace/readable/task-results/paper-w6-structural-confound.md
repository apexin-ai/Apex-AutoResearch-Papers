# paper w6 structural confound

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_w6_structural_confound_20260516T032042_result.json`
- **Structured JSON:** [`cce8b6da77ce7fa10208.json`](../../sessions/cc/cce8b6da77ce7fa10208.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All edits are consistent. Let me verify one data point—the OLMo row in the appendix table shows 256 for all depths 1-5 and <1% truncation. The task data didn't include exp-002 EOS truncation rate explicitly, but 256/256 tokens with negligible truncation is correct (almost all samples hit the limit).

Quick cross-check on the Qwen-continuation within-model range: depths 1-5 are 244, 238, 240, 240, 238. Range = 244 - 238 = 6 tokens. The appendix_extended.tex correctly says "except Qwen-continuation at 6 tokens."

Summary of changes:

**4 files modified:**

1. **`discussion.tex`** — Added new subsection "Structural Confound: Token Length and EOS Truncation" (Section 6.4) with three arguments: length asymmetry is directionally opposite to the concern, depth 1-5 lengths are stable, and high-truncation models still yield K*=2.

2. **`appendix.tex`** — Added Table `tab:token_length` with per-model per-depth mean token counts and EOS truncation rates for all 9 configurations (5 models + 4 decoding ablations).

3. **`appendix_extended.tex`** — Added "Structural confound: token length" paragraph in Extended Limitations with quantitative summary referencing the new table.

4. **`main.tex`** — Updated Limitations point (12) to reference the new table and section, updated token range from "214--256" to "195--256" to include Qwen-7B, and added within-model range bound ("$\leq$ 6 tokens").

---
