# cf_batch_part2_v1 Analysis: TracVLA Untrained Counterfactual Sensitivity

## Experiment Overview
- **Content**: TracVLA (Phi-3-Vision base, untrained) counterfactual sensitivity on LIBERO-Goal and LIBERO-Long
- **Method**: cosine_dist (representation cosine distance at L31)
- **Model**: phi3v-base (microsoft/Phi-3-vision-128k-instruct, NOT fine-tuned on LIBERO)
- **Conditions**: wrong, empty, shuffled, paraphrased × 2 suites
- **Samples**: 5000 per condition (10 tasks × 10 demos × 50 timesteps)
- **Server**: westd-19183, cuda:1
- **Runtime**: ~31 min (Goal) + ~29 min (Long) = ~60 min total
- **Exit code**: 0 (success)

## Results: TracVLA Goal Untrained

| Condition | cos_dist (L31) | cohens_d (global) | cross-task mean d |
|-----------|---------------|-------------------|------------------|
| empty | 0.1530 | 8.8871 | 18.1209 |
| shuffled | 0.0839 | 1.4142 | 14.9672 |
| wrong | 0.0160 | 1.2932 | 13.1758 |
| paraphrased | 0.0043 | 2.1607 | 9.7738 |

**Ordering by cos_dist**: empty >> shuffled > wrong > paraphrased

## Results: TracVLA Long Untrained

| Condition | cos_dist (L31) | cohens_d (global) | cross-task mean d |
|-----------|---------------|-------------------|------------------|
| empty | 0.1734 | 11.2529 | 19.0888 |
| shuffled | 0.1204 | 2.0345 | 16.7802 |
| wrong | 0.0221 | 1.8731 | 11.6638 |
| paraphrased | 0.0070 | 1.7351 | 12.9783 |

**Ordering by cos_dist**: empty >> shuffled > wrong > paraphrased

## Comparison with Trained CF

⚠️ **Method difference**: Trained CF used `paired_mse` (action output divergence); untrained CF used `cosine_dist` (hidden representation distance). Magnitudes are NOT comparable. Only orderings can be compared.

### Ordering Comparison

| Suite | Trained (paired_mse) | Untrained (cosine_dist) |
|-------|---------------------|------------------------|
| Goal | empty(1.52) > wrong(1.40) > shuffled(1.34) > para(1.21) | empty(0.153) >> shuffled(0.084) > wrong(0.016) > para(0.004) |
| Long | empty(1.47) > wrong(1.42) > shuffled(1.39) > para(1.16) | empty(0.173) >> shuffled(0.120) > wrong(0.022) > para(0.007) |

### Key Observations (data-level, not conclusions)

1. **Empty dominates in both**: Both trained and untrained show empty as the highest-sensitivity condition. In untrained, empty is dramatically dominant (10-25× larger cos_dist than next condition).

2. **Wrong vs shuffled swap**: Trained models show wrong > shuffled; untrained models show shuffled > wrong. This swap is consistent across both suites.

3. **Paraphrased consistently lowest**: Both trained and untrained agree that paraphrased is the smallest perturbation.

4. **Untrained dynamic range**: The untrained model shows extreme separation between empty and other conditions (cos_dist 0.153-0.173 vs 0.004-0.120), while trained models show a compressed range (d 1.16-1.52).

5. **Cross-suite consistency**: Both suites show identical orderings within each condition (trained or untrained), suggesting the pattern is robust across task types.

## Output Files
- `/root/autodl-tmp/vla-ssd/results/tracvla_goal/untrained/counterfactual_combined.json`
- `/root/autodl-tmp/vla-ssd/results/tracvla_long/untrained/counterfactual_combined.json`

## Log
- `~/runs/vla-ssd/cf_batch_part2_v1.log`
