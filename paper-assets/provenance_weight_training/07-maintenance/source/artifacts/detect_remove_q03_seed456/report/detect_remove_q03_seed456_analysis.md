# detect_remove_q03_seed456 Analysis

## Final Metrics

| Metric | Value |
|--------|-------|
| eval_ppl_holdout | **17.2509** |
| eval_loss_holdout | **2.8479** |
| eval_holdout_tokens | 4,077,068 |
| train_loss | 11.255 |
| total_steps | 6,103 |
| epoch | 0.84 |
| train_runtime | 12,838.9s (~3.57h) |

## Cross-Seed Comparison (q03 threshold)

| Seed | eval_ppl_holdout | eval_loss_holdout | Status |
|------|-----------------|-------------------|--------|
| seed42 | 17.2500 | 2.8480 | DONE (success) |
| seed456 | 17.2509 | 2.8479 | DONE (success) |
| seed123 | — | — | RUNNING |

## 2-Seed Statistics (seed42 + seed456)

| Statistic | PPL | Loss |
|-----------|-----|------|
| Mean | 17.2505 | 2.8480 |
| Std | 0.0006 | 0.0001 |
| Delta | +0.0009 | -0.0001 |

## Conclusion: **SUCCESS**

seed456 reproduces seed42 almost exactly (PPL delta = +0.0009, well within the +/-0.5 threshold). The near-zero variance across seeds confirms that the D&R q03 result (PPL ~17.25) is highly stable and not a seed artifact.

Pending seed123 completion for full 3-seed statistics.

## Configuration

- Model: Qwen3-0.6B
- Data: scored_data_filtered_q03.jsonl (116,935 samples)
- Weighting: uniform (D&R = detect and remove q>0.3)
- Training tokens: ~200M (multi-epoch, ~3.2x)
- Server: westd-30476, cuda:1
- Checkpoint: `/root/autodl-tmp/output/models/detect_remove_q03_seed456/final`
