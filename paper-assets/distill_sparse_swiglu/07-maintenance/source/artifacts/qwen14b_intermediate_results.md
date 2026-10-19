# Qwen-2.5-14B Eval Intermediate Results

## Status: GSM8K still running on all 3 experiments

**Important**: The eval script uses lm-eval-harness which batches all tasks (arc_challenge, winogrande, mmlu, gsm8k) together. Results for ALL tasks are only printed/saved after the entire batch completes. Since GSM8K (generate_until, 1319 samples) is still running, ARC/WinoGrande/MMLU scores are NOT yet available in the logs despite their computation being done internally.

## Available: WikiText-2 PPL

| Experiment | Server | PPL | ARC-c (acc_norm) | WinoGrande (acc) | MMLU (acc) | GSM8K |
|------------|--------|-----|------------------|------------------|------------|-------|
| qwen14b_dense_baseline | westd-41718 | 5.1854 | pending | pending | pending | running (81%, ~1065/1319) |
| qwen14b_teal30_eval | westd-41718 | 8.7332 | pending | pending | pending | running (87%, ~1153/1319) |
| qwen14b_bce30_s42_eval | westd-34887 | 8.7634 | pending | pending | pending | running (86%, ~1129/1319) |

## Reference: Completed qwen14b_kl30_s42 (same model, KL-trained predictor)

| Metric | Value |
|--------|-------|
| WikiText-2 PPL | 7.6232 |
| ARC-c (acc_norm) | 0.5717 |
| WinoGrande (acc) | 0.7206 |
| MMLU (acc) | 0.6372 |
| GSM8K (exact_match) | 0.4882 |

Source: `/root/distill_sparse_swiglu/results/benchmark/qwen14b_kl30_s42/results.json` on westd-34887

## GSM8K ETA Estimate

- teal30: 87% done, ~16.7s/iter, ~174 remaining → ~49 min
- dense_baseline: 81% done, variable speed (2-12s/iter), ~254 remaining → ~30-50 min
- bce30_s42: 86% done, ~14.6s/iter, ~190 remaining → ~46 min

## Log File Locations

- `/root/distill_sparse_swiglu/logs/qwen14b_teal30_eval.log` (westd-41718)
- `/root/runs/distill_sparse_swiglu/qwen14b_dense_baseline.log` (westd-41718)
- `/root/runs/distill_sparse_swiglu/qwen14b_bce30_s42_eval.log` (westd-34887)

## Data Source
- PPL values: exact copy from log `PPL = X.XXXX` lines
- GSM8K progress: from last progress bar in each log tail
- 提取时间: 2026-05-17T~13:40 UTC
