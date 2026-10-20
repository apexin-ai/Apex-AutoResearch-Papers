# plan017_14b_rsft_s43_no_evi_eval — Analysis

## Experiment Info

| Field | Value |
|-------|-------|
| exp_id | plan017_14b_rsft_s43_no_evi_eval |
| Model | Qwen3-14B + SFT s43 + RSFT s43 (no-evidence) |
| Base model | /root/autodl-tmp/models/Qwen/Qwen3-14B |
| SFT adapter | /root/autodl-tmp/sft_output_14b_s43 |
| RSFT adapter | /root/autodl-tmp/rsft_output_14b_s43 |
| Data | DocRED dev, 985 docs, matched@2048 |
| Server | rtx5090-4x |
| log_path | ~/runs/faith-evidence-ie/plan017_14b_rsft_s43_no_evi_eval.log |
| output_dir | /root/autodl-tmp/eval_results/plan017_14b_rsft_s43_no_evi_eval |
| Inference time | 17799s (~4h57m), 18.07 s/doc |

## Core Metrics

| Metric | Value |
|--------|-------|
| **Ign-F1** | **0.5713** |
| F1 | 0.5850 |
| Precision | 0.5491 |
| Recall | 0.6260 |
| Ign-Precision | 0.5265 |
| Ign-Recall | 0.6244 |
| TP | 7606 |
| Predictions | 20571 |
| Gold count | 12151 |
| Format OK | 983/985 (99.80%) |
| Truncated | 92/985 |
| Evi-F1 | 0.0000 (expected, no-evidence mode) |

## Comparison with s42

| Metric | s42 no-evi (dev) | s43 no-evi (dev) | Δ |
|--------|-----------------|-----------------|---|
| Ign-F1 | 0.5432 | 0.5713 | **+2.81pp** |

| Metric | s42 with-evi (dev) | s42 no-evi (dev) | s42 evidence tax |
|--------|-------------------|-----------------|-----------------|
| Ign-F1 | 0.5886 | 0.5432 | +4.54pp |

s43 with-evidence eval still running — evidence tax TBD.

## Key Observations

1. **s43 no-evidence ign_f1=0.5713 vs s42 no-evidence ign_f1=0.5432**: s43 seed improves no-evidence performance by +2.81pp, a substantial gain.
2. **Format compliance**: 99.80% (983/985), excellent.
3. **Truncation**: 92/985 (9.3%), comparable to prior evals.
4. **Recall-dominant**: recall (0.6260) > precision (0.5491), model predicts aggressively (20571 predictions vs 12151 gold).
