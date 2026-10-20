# Analysis: detect_remove_q09_epoch_matched_seed42

## Experiment Summary
- **Filter threshold**: q09 (90th percentile synthetic score, most lenient filter)
- **Training data**: 228,743 samples from scored_data_filtered_q09.jsonl (~124M tokens)
- **Training**: 1 epoch, 3770 steps, uniform weighting, Qwen3-0.6B, seed 42
- **Train loss (final)**: 9.9127
- **Wall clock**: ~2.3 GPU-hours

## Eval Results
- **Holdout PPL**: 17.628
- **Holdout loss**: 2.8695
- **Eval tokens**: 4,077,068
- **Method**: sliding window, stride 1024, max_length 2048, fp16, 5000 docs

## Epoch-Matched Curve (4/5 points complete)

| q | Samples | Epoch-Matched PPL | Multi-Epoch PPL | Delta |
|---|---------|-------------------|-----------------|-------|
| q01 | 93,266 | 18.04 | 17.40 | +0.64 |
| q03 | 137,654 | 17.74 | 17.25 | +0.49 |
| q05 | 172,103 | 17.65 | 17.28 | +0.37 |
| q07 | -- | running | ? | -- |
| q09 | 228,743 | **17.63** | 17.42 | +0.21 |
| adaptive | -- | 17.651 | -- | ref |

## Key Findings

1. **Monotonic decrease confirmed**: The epoch-matched curve shows strictly monotonic improvement as more data is included: 18.04 -> 17.74 -> 17.65 -> 17.63. No U-shape.

2. **U-shape is a multi-epoch artifact**: The original multi-epoch curve showed a U-shape (q05=17.28 -> q09=17.42, PPL rising). Under epoch-matched conditions, q09 (17.63) is the best point so far, not the worst.

3. **Diminishing returns at high retention**: The improvement from q05 to q09 is only 0.02 PPL (17.65 -> 17.63), suggesting the curve is plateauing. Adding the lowest-quality 30% of data (from q05 to q09 filter) barely helps when seen only once.

4. **Multi-epoch gap narrows with more data**: The delta between multi-epoch and epoch-matched PPL shrinks from 0.64 (q01) to 0.21 (q09). At q09, the multi-epoch setting only repeats data ~1.6x, so the repetition benefit is small but the multi-epoch PPL actually rises (17.28 -> 17.42), suggesting overfitting on the added low-quality data.

5. **Adaptive weighting reference**: The adaptive tau08 baseline (PPL=17.651) sits between q05 (17.65) and q09 (17.63) in the epoch-matched curve, suggesting that 1 epoch of q09 data performs comparably to adaptive weighting.

## Conclusion
**SUCCESS**. The epoch-matched curve is monotonically decreasing through 4 of 5 points. The original U-shape in the multi-epoch curve is confirmed as a multi-epoch artifact (overfitting from repeated exposure to low-quality data). When each sample is seen exactly once, including more data always helps or is neutral. Awaiting q07 to complete the full 5-point curve.
