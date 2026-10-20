# data exp 018 integration

**Spectral Early Warning Signals for Model Collapse and Their Prevention–Detectability Tradeoff** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_exp_018_integration_20260523T094602_result.json`
- **Structured JSON:** [`f75b9a91e332e3be868e.json`](../../sessions/f7/f75b9a91e332e3be868e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All old values cleaned up. Here's the summary:

## Part A — Data Extraction & Registry

**exp_018 (r=0.5, seed43) complete metrics extracted** from `phase1_fixed_mix_seed43_results.json`. Per-gen data (Gen 0→10):
- SLV: 2366.68 → 2570.09
- eff_rank: 417.55 → 552.40
- PPL: 9.55 → 15.03
- D-4: 0.741 → 0.209
- sigma1: 1942.82 → 622.69
- train_loss: — → 1.051

**Registry**: exp_018 → DONE(success), all 11 generations of metrics already populated.

## Part B — Paper Integration (2-seed mean)

**9 text edits** across 3 files:
- `experiments.tex`: Table 3 r=0.5 row (2571.7/553.5/15.12/.152), Table 3 caption, Fig 1 caption (2572, 104pts, 2-seed mean), Fig 2 caption, §3.1 SLV value (2572/104), §3.1 PPL/D-4 (58%/79%), §3.5 SLV (2572)
- `conclusion.tex`: 58%/79%
- `limitations.tex`: r=0.2 single seed, r=0.5 2-seed mean

**Figure 1** (`gen_fig1.py`): Rewritten to generate single-panel SLV trajectory with r=0 (3-seed mean, solid) and r=0.5 (2-seed mean, dashed). Outputs to `paper/figures/spectral_trajectory.pdf`.

**Figure 2** (`gen_fig2.py`): r=0.5 array updated from single seed to 2-seed mean (exp_004 + exp_018). Outputs to `paper/figures/phase_diagram.pdf`.

---
