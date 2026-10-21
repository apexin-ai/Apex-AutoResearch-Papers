# Qwen-7B s0 Eval Results Summary

Collected: 2026-05-21
Server: cqa1-21977
Results dir: `/root/autodl-tmp/exp001/eval_results_v2/qwen7b_d{dose}_s0/`

## MMLU Results

| Dosage | Accuracy | Correct / Total |
|--------|----------|-----------------|
| d000   | 0.6632   | — / 14042       |
| d005   | 0.6468   | — / 14042       |
| d025   | 0.6567   | — / 14042       |
| d050   | 0.6578   | 9237 / 14042    |
| d100   | 0.6529   | 9168 / 14042    |

## ARC-Challenge Results

| Dosage | Accuracy | Correct / Total |
|--------|----------|-----------------|
| d000   | 0.8720   | 1022 / 1172     |
| d005   | 0.8532   | 1000 / 1172     |
| d025   | 0.8447   | 990 / 1172      |
| d050   | 0.8558   | 1003 / 1172     |
| d100   | PENDING  | running          |

## Notes

- MMLU eval completed for all 5 dosages.
- ARC eval completed for d000-d050; d100 in progress (~3.5 min remaining as of 08:10 CST).
- `eval_results.json` gets overwritten by the last benchmark run. Dedicated files: `mmlu_results.json`, `arc_challenge_results.json`.
- Experiment was not submitted via `submit_training_job`; cron misjudged as failed due to missing W&B tracking.
