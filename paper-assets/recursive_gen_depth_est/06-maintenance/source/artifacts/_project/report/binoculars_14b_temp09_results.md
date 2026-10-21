# Binoculars Baseline + Merged Ablation: Qwen2.5-14B temp0.9

**Cell**: qwen25_14b_temp09 (pythia_nucleus decoding)
**Data**: 20,000 samples (5,000 per depth d0–d3)
**Observer**: EleutherAI/pythia-1.4b | **Performer**: EleutherAI/pythia-410m
**Date**: 2026-05-20

## 1. Binoculars Baseline (5 calibration methods)

| Method | #Features | 4-class Acc | d1–d3 Bal Acc |
|--------|-----------|-------------|---------------|
| equal_width | 1 (score) | 0.2943 ± 0.0029 | 0.3211 ± 0.0210 |
| coral | 1 (score) | 0.2883 ± 0.0038 | 0.3844 ± 0.0051 |
| threshold | 1 (score) | 0.3644 ± 0.0060 | 0.2595 ± 0.0078 |
| RF_single | 1 (score) | 0.2917 ± 0.0063 | 0.2779 ± 0.0087 |
| **RF_multi** | **11** | **0.4252 ± 0.0060** | **0.3717 ± 0.0076** |

Best Binoculars method: RF_multi (11 token-level features), 4-class acc = **0.4252**.

## 2. Merged Feature Ablation (RF 200 trees, 5-fold stratified CV)

| Feature Set | #Features | 4-class Acc | d1–d3 Bal Acc |
|-------------|-----------|-------------|---------------|
| bino_single (bino_score only) | 1 | 0.2917 ± 0.0063 | 0.2779 ± 0.0087 |
| bino_only | 11 | 0.4258 ± 0.0049 | 0.3724 ± 0.0071 |
| stat_only (self-ref) | 19 | 0.5183 ± 0.0069 | 0.4559 ± 0.0083 |
| **merged (stat + bino)** | **30** | **0.5419 ± 0.0093** | **0.4770 ± 0.0120** |

## 3. Key Takeaways

- **Stat features (19) dominate**: 0.5183 acc vs Binoculars RF_multi 0.4258 (+9.25pp).
- **Merging helps**: 30-feat merged achieves 0.5419, a +2.36pp lift over stat-only and +11.61pp over bino-only.
- **Binoculars single score is weak**: 0.2917 acc ≈ random (0.25), consistent with Binoculars not being designed for ordinal depth estimation.
- **d1–d3 balanced accuracy** follows the same ranking: merged (0.477) > stat (0.456) > bino (0.372) > single (0.278).

## 4. Files on Server

- `results/binoculars_14b_temp09.json` — per-calibration Binoculars results
- `results/pythia_nucleus_bino_features.npz` — 11 Binoculars features (20k samples)
- `results/merged_ablation_14b_temp09.json` — merged ablation results
- `data/qwen25_14b_temp09/features_self_ref.jsonl` — 19 stat features (20k samples)
- `scripts/merged_ablation_14b_temp09.py` — ablation script
