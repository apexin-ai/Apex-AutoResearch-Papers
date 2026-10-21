# paper experiments

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiments_20260515T233732_result.json`
- **Structured JSON:** [`243d312e57ffb95eee6a.json`](../../sessions/24/243d312e57ffb95eee6a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Section saved to `experiments.tex` with 8 provenance-tracked claims (coverage 21/22).

**Summary**: Experiments section (4 subsections) written in ~750 words covering:
- **Setup**: Qwen3-0.6B continued pretraining, 247K samples/132M+ tokens with 40% self-generated synthetic, balanced holdout eval
- **Detector**: TF-IDF+LR (AUC=0.939), calibration prioritized over accuracy (ECE 0.24→0.048), 46.3% mid-range scores
- **Baselines**: Uniform, Grid-b (6 values, 6× cost), ESS-only (max intervention), Golden Ratio (oracle)
- **Protocol**: 4 experiment groups — main comparison (3 seeds), τ sweep (6 points), n_min sensitivity (4 points), batch size

All numbers traced to registry experiment IDs. Citation placeholders included.

---
