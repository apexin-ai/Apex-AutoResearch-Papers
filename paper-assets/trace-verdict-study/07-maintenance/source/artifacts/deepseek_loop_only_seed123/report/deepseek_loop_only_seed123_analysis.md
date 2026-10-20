# Experiment Analysis: deepseek_loop_only_seed123

## Overview
- **Experiment**: deepseek_loop_only_seed123
- **Model**: DeepSeek-6.7B (LoRA)
- **Condition**: loop_only
- **Hypothesis**: Accuracy should fall in 78–84% range (cross-seed stability with seed42=81.26%)
- **Status**: ✅ Training completed normally (EXIT_CODE=0)

## Eval Results

| Metric | seed123 | seed42 | Δ |
|--------|---------|--------|---|
| **Accuracy** | **81.26%** | **81.26%** | **0.00pp** |
| Accuracy 95% CI | [79.2%, 83.4%] | — | — |
| Majority baseline | 71.5% | — | — |
| Lift over majority | +9.7pp | — | — |
| pass_precision | 0.8792 | — | — |
| pass_recall | 0.8555 | 0.8825 | −2.70pp |
| pass_f1 | 0.8672 | — | — |
| fail_precision | 0.6602 | — | — |
| fail_recall | 0.7050 | 0.6372 | **+6.78pp** |
| fail_f1 | 0.6819 | — | — |

**n = 1190** samples, 1000 bootstrap resamples.

## Cross-Seed Comparison

- **Accuracy**: Identical at 81.26% — perfect cross-seed reproducibility on the headline metric.
- **Recall tradeoff shifted**: seed123 has notably better fail_recall (+6.78pp) at the cost of slightly lower pass_recall (−2.70pp). This is a calibration-level shift, not a performance divergence.
- **Overall**: Both seeds land squarely at the same accuracy, confirming Tier 2 loop_only is seed-robust for DeepSeek-6.7B.

## Conclusion

**✅ SUCCESS — Seed robust.** Accuracy 81.26% is exactly equal to seed42 (81.26%), well within the pre-specified 78–84% acceptance range. The per-class recall shows a minor precision–recall tradeoff shift between seeds, but aggregate performance is identical. No further seed sweep needed for this condition.

## Paths
- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed123/final`
- **Predictions**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed123/final/predictions.jsonl`
- **Eval results**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_loop_only_seed123/final/eval_results.json`
- **Training log**: `~/runs/trace-verdict-study/deepseek_loop_only_seed123.log`
