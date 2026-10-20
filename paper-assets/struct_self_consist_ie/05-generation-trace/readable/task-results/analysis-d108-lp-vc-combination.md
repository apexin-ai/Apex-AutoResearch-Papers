# analysis d108 lp vc combination

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d108_lp_vc_combination_20260516T074431_result.json`
- **Structured JSON:** [`7a75af8533f04aed1f59.json`](../../sessions/7a/7a75af8533f04aed1f59.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Artifacts registered. Here's the summary:

## D108 LP×VC Combination Selection Results

### Baselines

| | SciERC NER (N=8) | CoNLL NER (N=16) |
|---|---|---|
| Random | 0.6261 | 0.8674 |
| LP-only | 0.6602 | 0.8904 |
| Greedy | 0.6633 | 0.9067 |
| Oracle | 0.7775 | 0.9544 |

### Strategy 1: VC-gated LP — **hurts consistently**
Replacing LP with random selection on low-VC instances always degrades F1. Even at the most generous gate (q=0.25), SciERC drops to 0.6455 and CoNLL to 0.8752.

### Strategy 2: Per-sample VC-weighted LP — **best combination**
- **SciERC**: α=2.0 → **0.6669** (+0.0067 vs LP, +0.0036 vs greedy)
- **CoNLL**: α=2.0 → **0.9063** (+0.0159 vs LP, essentially matching greedy at -0.0004)

This is the strongest finding — weighting LP by per-sample voting frequency closes ~half the LP-to-greedy gap on CoNLL.

### Strategy 3: Tied handling — **confirms LP discrimination weakness**
- 60% of SciERC instances are LP-tied at ε=0.05; using VC for tied instances gives 0.6673 (+0.0071 vs LP)
- Oracle for tied instances shows massive headroom (0.7394 on SciERC), confirming the tied instances are where most quality variance lives

### Key takeaway
VC as a per-sample signal (frequency of the exact surface-key set) meaningfully complements LP. The best combination (LP + 2×VC) nearly recovers greedy-level F1 on CoNLL and exceeds greedy on SciERC, but the remaining gap to oracle (0.11 on SciERC, 0.05 on CoNLL) suggests neither signal captures structural correctness well.

---
