# eval epoch matched seed42

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_epoch_matched_seed42_20260518T094830_result.json`
- **Structured JSON:** [`86987933cbc735752bdd.json`](../../sessions/86/86987933cbc735752bdd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Results: `detect_remove_q05_epoch_matched_seed42`

| Metric | Value |
|---|---|
| **Eval PPL** | **17.650** |
| **Eval Loss** | **2.8707** |
| **Train Loss** (final step) | 3.184 |
| **Total Steps** | 2533/2533 (complete) |
| **Eval Tokens** | 4,077,068 |

### Interpretation

The epoch-matched D&R control (1 content epoch, 2533 steps) achieves PPL **17.650**, vs the full D&R's **17.290** — a gap of **0.36 PPL**.

This is a meaningful but moderate difference. It suggests:

- **The majority of D&R's advantage comes from data quality filtering**, not from multi-epoch training on clean data. The epoch-matched control, despite seeing 60% fewer steps (2533 vs 6103), still captures most of the benefit.
- **Multi-epoch training contributes an additional ~0.36 PPL improvement** on top of the filtering effect. The full D&R's 3.78 content-level epochs vs this control's 1 epoch accounts for this residual gap.
- The result is **neither PPL >> 17.290 nor PPL ≈ 17.290** — it's somewhere in between, leaning toward "data quality is the primary driver, with a secondary epoch effect."

To fully quantify the decomposition, the key comparison chain would be:
`baseline (no filtering) → epoch-matched D&R (17.650) → full D&R (17.290)`

---
