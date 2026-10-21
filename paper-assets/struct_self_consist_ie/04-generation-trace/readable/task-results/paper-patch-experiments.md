# paper patch experiments

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_patch-experiments_20260516T024604_result.json`
- **Structured JSON:** [`ff7ec64d9adccba1a570.json`](../../sessions/ff/ff7ec64d9adccba1a570.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 7 tasks complete:

1. **4B Scale Ablation** (lines 221-247) — new `\paragraph` with `tab:scale-ablation` table and discussion
2. **Free-form Ablation** (lines 249-256) — new `\paragraph` discussing score compression intrinsicness, referencing `tab:freeform-ablation`
3. **ε=0.05 Justification** (line 268) — tied definition with robustness across ε∈{0.01, 0.05, 0.10}
4. **Fisher's z-test fix** (line 167) — now specifies NER vs RE ρ values being compared
5. **RE (preliminary)** — added to all 3 table captions (lines 44, 106, 188)
6. **3 Figure environments** — `fig:signal_heatmap` (line 91), `fig:selection_gap` (line 147), `fig:reliability` (line 283)
7. **n=81 RE subset** (line 176) — high-complexity RE instances defined with Voting/SJ correlations

---
