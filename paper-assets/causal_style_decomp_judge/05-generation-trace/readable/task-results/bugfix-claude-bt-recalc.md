# bugfix claude bt recalc

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_bugfix_claude-bt-recalc_20260523T013304_result.json`
- **Structured JSON:** [`5acff9c9213443fd531d.json`](../../sessions/5a/5acff9c9213443fd531d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All done. Here's the old vs new BT comparison:

| Config | Old BT% | Old n | New BT% | New n | New obs | Inflation |
|---|---|---|---|---|---|---|
| LLMBar×formality | 61.7% | 47 | **56.2%** | 88 | 176 | +5.4pp |
| LLMBar×verbosity | 57.1% | 49 | **54.1%** | 86 | 172 | +3.1pp |
| AlpacaEval×formality | 84.0% | 50 | **69.8%** | 86 | 172 | **+14.2pp** |
| AlpacaEval×verbosity | 75.0% | 60 | **68.3%** | 82 | 164 | +6.7pp |
| MT-Bench×formality | 85.4% | 48 | **73.3%** | 73 | 146 | **+12.1pp** |

**Blindspot status** (BT p<0.05 AND Likert p>0.05):
- AlpacaEval×formality: still **YES** (BT p<0.0001, Likert p=0.09)
- All others: NO (unchanged)

**What changed:**
- `bt_pair_bootstrap()` in `claude_crossbench_analysis.py` now uses `trial1_prefers_{axis}` + `trial2_prefers_{axis}` (2 observations per pair) instead of the aggregate `prefers_{axis}`/`formal_wins` field that dropped inconsistent pairs
- Pair-level bootstrap (10000 iterations, seed=42) with `np.random.default_rng`
- Inflation ranged from +3.1pp to +14.2pp, confirming the 5-15pp estimate

---
