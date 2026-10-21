# Uniform OOD Baseline Training — Analysis Report

**Date**: 2026-05-19
**Server**: westd-41312 (GPU 2 & 3)
**Model**: Qwen/Qwen3-0.6B
**Data**: mixed_data.jsonl (371,499 examples, 80% human + 20% contaminated)
**Training**: 200M tokens, 6103 steps, bs=4, lr=5e-5, uniform weighting

## Final Metrics

| Metric | seed123 | seed456 |
|---|---|---|
| **Eval PPL (holdout)** | **17.686** | **17.702** |
| Target PPL | 17.686 (±0.01) | 17.702 (±0.01) |
| Delta from target | +0.0001 | -0.0005 |
| Eval loss (holdout) | 2.8728 | 2.8737 |
| Train loss | 7.986 | 7.965 |
| Train runtime | 12,710s (~3.5h) | 12,720s (~3.5h) |
| Eval tokens | 4,077,068 | 4,077,068 |
| Eval time | 163s | 124s |

## PPL Verification

Both experiments are **within ±0.01 tolerance** of their target PPL values:
- seed123: |17.6861 − 17.686| = 0.0001 ✓
- seed456: |17.7015 − 17.702| = 0.0005 ✓

Seed-to-seed PPL variance: 17.702 − 17.686 = **0.016** (0.09%), indicating high reproducibility.

## Checkpoint Paths

| Experiment | Checkpoint |
|---|---|
| uniform_ood_seed123 | `/root/autodl-tmp/provenance_weight_training/output/models/uniform_ood_seed123/final` |
| uniform_ood_seed456 | `/root/autodl-tmp/provenance_weight_training/output/models/uniform_ood_seed456/final` |

Both checkpoints: ~1.1GB model.safetensors + tokenizer + config.

## Eval Method

`eval_perplexity.py` — sliding window (stride=1024, max_length=2048), 5000 docs from `data/human/eval_holdout.jsonl`, autocast fp16.

## Conclusion

**SUCCESS** — Both uniform baselines validated. Checkpoints are ready for OOD evaluation on `eval_openwebtext.jsonl` and `eval_wikipedia.jsonl`.
