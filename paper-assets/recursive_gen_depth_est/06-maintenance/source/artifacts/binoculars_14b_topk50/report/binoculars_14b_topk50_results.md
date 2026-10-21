# Binoculars Baseline + Merged Ablation: Qwen2.5-14B top_k=50

**Cell**: qwen25_14b_topk50 (pythia_nucleus decoding)
**Data**: 20,000 samples (5,000 per depth d0–d3)
**Observer**: EleutherAI/pythia-1.4b | **Performer**: EleutherAI/pythia-410m
**Date**: 2026-05-20

## 1. Binoculars Baseline (5 calibration methods)

| Method | #Features | 4-class Acc | d1–d3 Bal Acc |
|--------|-----------|-------------|---------------|
| equal_width | 1 (score) | 0.2613 ± 0.0048 | 0.3065 ± 0.0152 |
| coral | 1 (score) | 0.2447 ± 0.0035 | 0.3263 ± 0.0046 |
| threshold | 1 (score) | 0.2843 ± 0.0068 | 0.2495 ± 0.0080 |
| RF_single | 1 (score) | 0.2523 ± 0.0048 | 0.2521 ± 0.0095 |
| **RF_multi** | **11** | **0.3768 ± 0.0071** | **0.3386 ± 0.0075** |

Best Binoculars method: RF_multi (11 token-level features), 4-class acc = **0.3768**.

## 2. Merged Feature Ablation (RF 200 trees, 5-fold stratified CV)

| Feature Set | #Features | 4-class Acc | d1–d3 Bal Acc |
|-------------|-----------|-------------|---------------|
| bino_single (bino_score only) | 1 | 0.2523 ± 0.0048 | 0.2521 ± 0.0095 |
| bino_only | 11 | 0.3774 ± 0.0090 | 0.3402 ± 0.0097 |
| stat_only (self-ref) | 19 | 0.4884 ± 0.0082 | 0.4345 ± 0.0091 |
| **merged (stat + bino)** | **30** | **0.5149 ± 0.0053** | **0.4637 ± 0.0042** |

## 3. Baseline Alignment (方案 A)

The stat_only value (48.84%) differs from the main pipeline (47.93%) due to independent CV splits in the ablation script. Following the same convention as other cells (using main pipeline values as the single baseline):

| Feature Set | Acc (ablation) | Acc (aligned) | Δ vs main pipeline (47.93%) |
|-------------|---------------|---------------|---------------------------|
| stat_only | 48.84% | **47.93%** (main pipeline) | baseline |
| merged | 51.49% | 51.49% | **+3.56pp** |

The 0.91pp difference between ablation stat_only (48.84%) and main pipeline (47.93%) is within expected 5-fold CV variance.

## 4. Key Takeaways

- **Stat features (19) dominate**: 47.93% (main pipeline) vs Binoculars RF_multi 37.68% (+10.3pp).
- **Merging helps**: 30-feat merged achieves 51.49%, a **+3.56pp** lift over stat-only main pipeline and +13.8pp over bino-only.
- **Binoculars single score is weak**: 25.23% ≈ random (25%), consistent with Binoculars not being designed for ordinal depth estimation.
- **d1–d3 balanced accuracy** follows the same ranking: merged (0.464) > stat (0.435) > bino (0.340) > single (0.252).
- **Scale confound note**: 19-feat uses self-reference (Qwen2.5-14B, matched scale); Binoculars uses pythia-1.4b observer (10× scale gap). The stat feature advantage partially reflects matched-scale reference, not purely feature design superiority.
- **top_k=50 vs temp=0.9**: RF_multi drops from 42.52% (temp09) to 37.68% (topk50), suggesting top-k truncation reduces the signal Binoculars can detect. Merged lift is comparable (+3.56pp vs +3.7pp).

## 5. Files on Server

- `results/binoculars_14b_topk50/binoculars_14b_topk50.json` — per-calibration Binoculars results
- `results/binoculars_14b_topk50/pythia_nucleus_bino_features.npz` — 11 Binoculars features (20k samples)
- `results/merged_ablation_14b_topk50.json` — merged ablation results
- `data/qwen25_14b_topk50/features_self_ref.jsonl` — 19 stat features (20k samples)
- `scripts/merged_ablation_14b_topk50.py` — ablation script
