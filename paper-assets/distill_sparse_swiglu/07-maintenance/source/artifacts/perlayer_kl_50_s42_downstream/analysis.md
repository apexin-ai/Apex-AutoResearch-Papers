# Per-Layer KL 50% Downstream Evaluation (perlayer_kl_50_s42)

**Date**: 2026-05-22
**Server**: westd-41718
**Checkpoint**: `checkpoints/perlayer_kl_50_s42/predictor_perlayer_kl.pt`
**Allocation**: uniform, model-level sparsity 0.496
**PPL** (training): 34.85

## Downstream Results

| Task | Metric | Per-Layer KL 50% | E2E KL 50% (s42) | TEAL 50% uniform | Dense |
|------|--------|------------------|-------------------|------------------|-------|
| ARC-c | acc_norm | 0.2705 | 0.3276 | 0.2747 | 0.5828 |
| WinoGrande | acc | 0.5154 | 0.6290 | 0.5438 | 0.7806 |
| MMLU | acc | 0.2658 | 0.2777 | 0.2926 | 0.6527 |
| GSM8K | exact_match | 0.0174 | 0.0212 | 0.0174 | 0.4875 |
| HellaSwag | acc_norm | 0.3818 | 0.5666 | 0.3935 | 0.8233 |
| PIQA | acc_norm | 0.6279 | 0.6910 | 0.6366 | 0.8090 |

## Delta vs E2E KL 50%

| Task | Delta (pp) |
|------|-----------|
| ARC-c | -5.71 |
| WinoGrande | -11.36 |
| MMLU | -1.19 |
| GSM8K | -0.38 |
| HellaSwag | -18.48 |
| PIQA | -6.31 |

Average delta: **-7.24 pp** across 6 tasks.

## Delta vs TEAL 50% (training-free baseline)

| Task | Delta (pp) |
|------|-----------|
| ARC-c | -0.42 |
| WinoGrande | -2.84 |
| MMLU | -2.68 |
| GSM8K | 0.00 |
| HellaSwag | -1.17 |
| PIQA | -0.87 |

Average delta: **-1.33 pp** — per-layer KL is *worse* than even the training-free TEAL baseline.

## Conclusion: NEGATIVE

Per-layer KL distillation at 50% sparsity is a clear failure:
1. **PPL 34.85** vs E2E KL's 11.96 (2.9x worse)
2. All 6 downstream tasks are near-random (ARC-c 27%, MMLU 26.6%, WinoGrande 51.5%)
3. Performs worse than training-free TEAL 50% on 5/6 tasks (avg -1.33pp)
4. Loses 7.24pp on average vs E2E KL 50%
5. HellaSwag shows the largest collapse: 38.2% vs E2E KL's 56.7% (-18.5pp)

The per-layer KL objective fails catastrophically at high sparsity because independent per-layer optimization cannot capture cross-layer error propagation. This confirms the parent experiment's negative status.
