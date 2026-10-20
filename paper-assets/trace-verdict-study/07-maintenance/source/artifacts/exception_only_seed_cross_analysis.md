# Exception-Only Seed Cross-Analysis

## Setup
- 3 seeds: 42, 123, 456
- Test set: 1190 samples (exception_only condition)
- Model: Qwen2.5-Coder-7B-Instruct + LoRA

## Results

| Seed | Accuracy | Error Count | Error IDs |
|------|----------|-------------|-----------|
| 42   | 99.83%   | 2           | 901, 905  |
| 123  | 99.83%   | 2           | 901, 905  |
| 456  | 99.83%   | 2           | 901, 905  |

## Cross-Seed Overlap

- **All 3 seeds wrong**: {901, 905} (2 samples)
- **Any 2 seeds wrong**: {901, 905} (2 samples)
- **Union**: {901, 905} (2 samples)

**100% overlap** — all 3 seeds misclassify the exact same 2 samples.

## Error Pattern

| ID  | Label | Pred (all seeds) | raw_pred |
|-----|-------|-------------------|----------|
| 901 | pass  | fail              | fail     |
| 905 | pass  | fail              | fail     |

- Direction: both are **false negatives** (label=pass → pred=fail)
- Both samples involve the same function: `check_dict_case`
- Both traces contain multiple `[ERROR] GeneratorExit` entries from Python generator cleanup
- `GeneratorExit` is a benign signal (not a real error), but logged as `[ERROR]` in the trace
- The model consistently interprets `[ERROR]` tags as failure indicators

## Conclusion

These 2 errors are **irreducible** — they are data-level artifacts, not training variance. The exception_only condition's 99.83% accuracy ceiling is determined by these 2 misleading samples where benign `GeneratorExit` cleanup is logged as `[ERROR]`.
