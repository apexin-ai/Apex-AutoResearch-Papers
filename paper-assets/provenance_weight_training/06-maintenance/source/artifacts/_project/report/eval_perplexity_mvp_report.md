## Held-out Eval Perplexity Results (MVP)

Evaluated on 5000 docs from data/human/eval_holdout.jsonl (pure FineWeb human text, ~4.08M tokens).
Standard unweighted sliding-window cross-entropy, exp(avg_loss) = perplexity.

| Model | Seed | Eval Loss | Eval PPL | Train Loss |
|-------|------|-----------|----------|------------|
| uniform | 42 | 2.8732 | 17.69 | 7.310 |
| uniform | 123 | 2.8728 | 17.69 | 7.312 |
| uniform | 456 | 2.8736 | 17.70 | 7.289 |
| adaptive | 42 | 2.8704 | 17.64 | 9.267 |
| adaptive | 123 | 2.8696 | 17.63 | 9.267 |
| adaptive | 456 | 2.8703 | 17.64 | 9.235 |

### Summary
- Uniform mean PPL: 17.694 (std=0.008)
- Adaptive mean PPL: 17.639 (std=0.006)
- Delta: -0.055 PPL (adaptive is better)
- All 3 adaptive seeds beat all 3 uniform seeds (no overlap)

### Key Finding
Train loss is NOT comparable (adaptive uses weighted loss = ~9.2 vs uniform = ~7.3).
On held-out unweighted eval, adaptive consistently achieves lower perplexity.

Script: /root/provenance_weight_training/eval_perplexity.py
Results JSON: /root/autodl-tmp/provenance_weight_training/output/eval_perplexity_results.json