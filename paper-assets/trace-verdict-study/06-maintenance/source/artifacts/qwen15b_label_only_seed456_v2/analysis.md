# qwen15b_label_only_seed456_v2 — Analysis

## Seed 456 Results

| Metric | Value | 95% CI |
|--------|-------|--------|
| Accuracy | 82.52% | [80.3%, 84.7%] |
| Majority baseline | 71.5% | — |
| Lift over majority | +11.0pp | [+8.7pp, +13.5pp] |
| Pass Precision | 0.837 | [0.816, 0.860] |
| Pass Recall | 0.938 | [0.923, 0.954] |
| Pass F1 | 0.885 | [0.868, 0.900] |
| Fail Precision | 0.776 | [0.728, 0.833] |
| Fail Recall | 0.543 | [0.485, 0.597] |
| Fail F1 | 0.639 | [0.590, 0.684] |
| Train Loss | 0.2394 | — |
| Eval Loss | 0.3064 | — |

## Qwen-1.5B label_only 3-Seed Summary

| Seed | Accuracy | Pass F1 | Fail F1 |
|------|----------|---------|---------|
| 42 | 78.90% | 0.860 | 0.570 |
| 123 | 81.34% | 0.878 | 0.602 |
| 456 | 82.52% | 0.885 | 0.639 |
| **Mean ± Std** | **80.92% ± 1.85%** | **0.874 ± 0.013** | **0.604 ± 0.035** |

## Qwen-1.5B vs Qwen-7B (label_only, 3-seed)

| Model | Accuracy (mean ± std) | Delta |
|-------|----------------------|-------|
| Qwen-1.5B | 80.92% ± 1.85% | — |
| Qwen-7B | 85.94% ± 1.12% | +5.02pp |

Scale gap of ~5pp is consistent and statistically meaningful (non-overlapping 1-std ranges: 1.5B upper = 82.77%, 7B lower = 84.82%).

## Checkpoint

Path: `/root/trace-verdict-study/outputs/qwen15b_label_only_seed456_v2/final`
Files: adapter_model.safetensors (70MB), eval_results.json, predictions.jsonl

## Conclusion

**Success.** Seed 456 is the strongest of the 3 seeds (82.52%), confirming an upward trend across seeds but within expected variance. The 3-seed mean (80.92%) establishes a reliable Qwen-1.5B label_only baseline, ~5pp below Qwen-7B, consistent with the scaling hypothesis.
