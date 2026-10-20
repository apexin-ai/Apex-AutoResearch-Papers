# Experiment Analysis: deepseek_exception_only_seed123_v2

## Summary

| Metric | Value |
|--------|-------|
| **Accuracy** | **99.50%** (95% CI: [99.08%, 99.83%]) |
| Eval Loss (epoch 2) | 0.4365 |
| Eval Loss (epoch 3) | 0.4780 |
| Train Loss (final avg) | 0.1234 |
| Epochs | 3 |
| Total Steps | 444 |
| Train Runtime | 6288s (~1h 45min) |
| Train Samples | 4720 |
| Eval Samples | 1190 |

## Per-class Metrics

| Class | Precision | Recall | F1 |
|-------|-----------|--------|----|
| pass | 1.000 | 0.993 | 0.996 |
| fail | 0.983 | 1.000 | 0.991 |

Majority baseline: 71.5% (always predict 'pass'). Lift: +28.0pp.

## Comparison

| Experiment | Accuracy | Seed | Code Version |
|------------|----------|------|-------------|
| deepseek_exception_only_seed42 | 99.33% | 42 | current |
| **deepseek_exception_only_seed123_v2** | **99.50%** | 123 | current |
| deepseek_exception_only_seed123 (old, 5/15) | 91.09% | 123 | old |

- vs seed42 (99.33%): +0.17pp, within noise range. Seeds are consistent.
- vs old seed123 (91.09%): +8.41pp. Confirms the old result was caused by a code bug, not seed sensitivity.

## Training Process

- Loss curve: steady descent from ~0.22 (epoch 0.2) to ~0.12 (epoch 0.95). No anomalies.
- Eval loss increased slightly from epoch 2 (0.437) to epoch 3 (0.478), suggesting mild overfitting on NLL but no impact on classification accuracy.
- No errors or warnings in the log beyond expected `pad_token_id` deprecation notices.

## Conclusion

**SUCCESS** — accuracy 99.50% exceeds the 98% threshold. The hypothesis is confirmed: seed123 under the current codebase achieves comparable accuracy to seed42 (99.33%), and the old 91.09% result was definitively caused by a code issue in the earlier version.

## Paths

- **Checkpoint**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123_v2/final/`
- **Log**: `/root/runs/trace-verdict-study/deepseek_exception_only_seed123_v2.log`
- **Predictions**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123_v2/final/predictions.jsonl`
- **Eval Results JSON**: `/root/autodl-tmp/trace-verdict-study-checkpoints/deepseek_exception_only_seed123_v2/final/eval_results.json`
