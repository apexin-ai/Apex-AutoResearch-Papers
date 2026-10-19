# analysis perlayer kl k2 s42 train

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_perlayer_kl_k2_s42_train_20260523T055644_result.json`
- **Structured JSON:** [`4b5445df9ad0b489ed8b.json`](../../sessions/4b/4b5445df9ad0b489ed8b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry updated. Here's the summary:

## K=2 Per-Layer KL Training Results

**Training** (completed, EXIT_CODE=0):
| Metric | Value |
|--------|-------|
| Final avg_kl | 0.0358 |
| Final avg_sparsity | 0.268 |
| Wall time | 3843s (~64 min) |
| Steps | 1000 |

**Two log files** (`perlayer_kl_k2_s42_train.log` and `perlayer_kl_k2_s42.log`) are the **same training run** — identical layer selections, near-identical KL values, just different wall times (~2s difference) from stdout vs nohup capture.

**Checkpoint**: `/root/distill_sparse_swiglu/checkpoints/perlayer_kl_k2_s42/`
- `predictor_perlayer_kl_k4.pt` (152MB, final predictor-only)
- `predictor_perlayer_kl_k4_step_1000.pt` (456MB, full w/ optimizer)
- `predictor_perlayer_kl_k4_step_500.pt` (456MB, mid-training)
- Note: filenames say "k4" — naming bug in the training script, but contents are K=2 trained.

**PPL Eval** (WikiText-2, 30% sparsity, TEAL global uniform — same mode as K=8):

| K | WikiText-2 PPL |
|---|---------------|
| 1 | 9.0568 |
| **2** | **10.7958** |
| 4 | 8.8932 |
| 8 | 8.9704 |
| 32 | ~8.81 |

K=2 is an anomalous outlier — **1.74 PPL worse than K=1** and **1.9 worse than K=4**. This suggests K=2 hits a pathological regime: too few layers to learn cross-layer interactions, but enough coupling to interfere with single-layer optimization. Worth investigating whether this is a training artifact (insufficient per-layer sample count: ~62 samples/layer vs K=8's ~250) or a genuine signal about the coupling landscape.

---
