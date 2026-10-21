# CLS@400 Downsample Function-Level Results

## Setup
- Model: Qwen3-4B (LoRA fine-tuned)
- Training samples: ~447 per-test instances (matching TRAJ variant count)
- Unique variants: ~105
- Task: CLS function-level (pass/fail classification)
- Test set: 1,890 instances (978 pass, 912 fail)
- Max sequence length: 2,048
- Epochs: 10

## Results

| Seed | Accuracy | F1 (macro) |
|------|----------|------------|
| 42   | 79.47%   | 79.47%     |
| 123  | 78.20%   | 78.12%     |
| 456  | 78.04%   | 78.00%     |
| **Mean** | **78.57 ± 0.78** | **78.53 ± 0.82** |

## Comparison with TRAJ (Function-Level, 4B)

| Method | Accuracy | F1 (macro) | Training Data |
|--------|----------|------------|---------------|
| TRAJ 4B | 86.30 ± 0.97% | — | 8,052 variant-level samples |
| CLS@400 | 78.57 ± 0.78% | 78.53 ± 0.82% | 447 per-test samples (~105 unique variants) |
| **Gap** | **−7.73 pp** | — | 18× fewer samples |

## Per-Seed Confusion Matrices

### Seed 42
|              | Pred fail | Pred pass |
|--------------|-----------|-----------|
| Actual fail  | 750       | 162       |
| Actual pass  | 226       | 752       |

### Seed 123
|              | Pred fail | Pred pass |
|--------------|-----------|-----------|
| Actual fail  | 683       | 229       |
| Actual pass  | 183       | 795       |

### Seed 456
|              | Pred fail | Pred pass |
|--------------|-----------|-----------|
| Actual fail  | 697       | 215       |
| Actual pass  | 200       | 778       |

## Key Takeaway
CLS with data volume matched to TRAJ (~447 samples) achieves 78.57% accuracy, lagging TRAJ's 86.30% by 7.73 pp. This confirms that TRAJ's advantage is not solely due to having more training data — the trajectory-based formulation itself provides a meaningful signal boost even when controlling for data volume.
