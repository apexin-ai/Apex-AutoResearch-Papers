# perlayer_kl_50_s42 — Analysis

## Training Status: COMPLETED

- **Steps**: 10000/10000, EXIT_CODE=0
- **Duration**: ~18216s (~5.06 hours)
- **Server**: westd-41718, cuda:0

## Training Metrics

| Metric | Value |
|--------|-------|
| Final avg_kl | 0.0282 |
| Model-level sparsity (eval) | 0.496 |
| Per-layer sparsity range | 0.480–0.523 (all layers ≈ 0.50 target) |
| tau (final) | 0.100 |

### Per-Layer KL Distribution (U-shaped)
- Early layers (0–4): avg_kl 0.041–0.055 (highest — hardest to compress)
- Middle layers (7–14): avg_kl 0.018–0.024 (lowest — easiest)
- Late layers (15–21): avg_kl 0.028–0.035 (moderate)
- Final layer (31): avg_kl 0.034 (elevated, typical for output-adjacent layer)

Lambda convergence varies widely: layers 0–1 converged to near-zero lambda (≤0.04), while most middle/late layers needed lambda 1024–5000 to maintain 50% sparsity.

## Eval Results

### WikiText-2 PPL
**PPL = 34.85** (seq_len=2048, 141 sequences, teal_global + uniform allocation)

### Downstream Tasks
**Still running** — arc_challenge completed, currently evaluating MMLU. Results pending in `perlayer_kl_50_s42_downstream`.

## Baseline Comparison

| Method | Sparsity | PPL | Δ vs E2E KL |
|--------|----------|-----|-------------|
| E2E KL 50% | 50% | 11.84 | — |
| MSE 50% | 50% | 18.52 | +56.4% |
| **Per-layer KL 50%** | **50%** | **34.85** | **+194.3%** |

## Hypothesis Evaluation

**Hypothesis**: PPL should fall between E2E KL 50% (11.84) and MSE 50% (18.52). If gap to E2E KL is small (<5%), signal type dominates PPL even at 50%.

**Result: FALSIFIED.** Per-layer KL PPL (34.85) is dramatically worse — nearly 3x E2E KL and ~1.9x MSE. The coupling scope penalty at 50% sparsity is catastrophic. Unlike at 30% sparsity where per-layer might track closer to E2E, at 50% the inter-layer signal coordination becomes critical and cannot be compensated by using KL loss alone.

## Conclusion: NEGATIVE

The 2D decomposition (signal type × coupling scope) does **not** hold cleanly at 50% sparsity. At this sparsity level, coupling scope dominates: per-layer training catastrophically degrades PPL regardless of whether KL or MSE loss is used. This suggests:
1. Inter-layer mask coordination becomes essential at higher sparsity
2. The "signal type dominates" conclusion from 30% experiments does not generalize to 50%
3. E2E training's advantage over per-layer grows superlinearly with sparsity

## Checkpoints

- Final: `checkpoints/perlayer_kl_50_s42/predictor_perlayer_kl.pt` (145 MB)
- Step checkpoints: 2000, 4000, 6000, 8000, 10000 (456 MB each)
- Log: `~/runs/distill_sparse_swiglu/perlayer_kl_50_s42.log`
