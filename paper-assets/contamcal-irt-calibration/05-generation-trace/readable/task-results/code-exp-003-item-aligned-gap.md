# code exp 003 item aligned gap

**Not All Models Are Inflated: Profiling Contamination Dose-Response Across Model Families** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_exp_003_item_aligned_gap_20260516T045017_result.json`
- **Structured JSON:** [`bf8584385dbc09825583.json`](../../sessions/bf/bf8584385dbc09825583.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Analysis complete. Results:

**The "item correction < 0.3pp" claim is technically correct but misleading.** It refers specifically to the difference between naive (misaligned) and properly item-ID-matched comparison — that methodological correction is indeed < 0.3pp.

However, the **actual gap between original and paraphrased MMLU items is -2.24pp** (para consistently easier) across all 20 model pairs tested. Key numbers:

| Finding | Value |
|---------|-------|
| Mean gap (aligned − para) | **-2.24 pp** |
| Per-item neutral (|gap| ≤ 0.3) | 84.8% |
| Items flagged (>50% disagreement) | 426 / 6,596 (6.5%) |
| Gap stable across contamination | ~0.8pp variation (d000→d100) |

**For RRF contamination detection**: the systematic bias approximately cancels in differential analysis since it affects all contamination levels similarly. The 426 flagged high-disagreement items should be reviewed for potential IRT exclusion.

Registry updated, artifact registered as `art_20260516_717a60`.

---
