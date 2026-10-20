# paper analysis format rewrite

**Does Reward Curation Kill Diversity? Systematic Evidence of Surprising Resilience in Iterative Self-Training** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_analysis_format_rewrite_20260517T105425_result.json`
- **Structured JSON:** [`a7e32871878f712f3bb4.json`](../../sessions/a7/a7e32871878f712f3bb4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All changes applied and verified:

1. **Table 4**: Replaced C2 vs C5 (different K) with C1 vs C5 (same K=4). All numbers from JSON. The near-identical values across C1/C5 make the point visually obvious.
2. **Removed "curation accelerates"** and the pool-size caveat sentence.
3. **Added K amplification discussion**: C2 (K=8) drops 1.13 bits vs C1/C5 (K=4) at 0.75 bits. K is the scaling factor, not curation.
4. **Rewrote mechanism paragraph**: New causal chain is iterative self-training → pattern overrepresentation → self-reinforcing loop, with K as amplifier. Curation's role is explicitly described as negligible.
5. **Section 5.4 updated**: 0.75 bits for K=4 (with K=8 intensification noted), Vendi Score changed to -0.27%, near-dup rise to 38 pp.
6. **Section 5.4 conclusion paragraph**: "reward curation primarily affects" → "iterative self-training primarily affects... independent of whether reward-curated or randomly selected."
7. **Verified**: zero em-dashes/en-dashes, no -ing phrase endings, all numbers traceable to JSON.

---
