# Training Status Report — 2026-05-15

## GPU Overview (seetacloud-westd-4x5090)

| GPU | Utilization | VRAM Used | Temperature | Status |
|-----|------------|-----------|-------------|--------|
| 0 (RTX 5090) | 0% | 0 MiB / 32607 MiB | 29°C | Idle (eval finished) |
| 1 (RTX 5090) | 98% | 27311 MiB / 32607 MiB | 68°C | Training |
| 2 (RTX 5090) | 94% | 30733 MiB / 32607 MiB | 67°C | Eval in progress |
| 3 (RTX 5090) | 75% | 30913 MiB / 32607 MiB | 68°C | Training |

## Training Experiments

| Experiment | GPU | Current Step | Total Steps | Progress | Speed | ETA (hours) | Last Loss | Last Eval Loss |
|---|---|---|---|---|---|---|---|---|
| repo-level-cls-8b-s42-resume | 1 | 1542 | 6633 | 23% | ~8.0s/step + eval 14min/200steps | ~17h | 0.8855 (step 1500) | 0.3226 (step 1400) |
| repo-level-cwm-8b-conda-v4 | 2 | ~2800 (eval) | 6633 | 42% | ~12s/step + eval 19min/100steps | ~25h | 0.0628 (step 2700) | 0.4260 (step 2700) |
| repo-level-cls-8b-seed123-conda-v3 | 3 | 5102 | 6633 | 77% | ~8.2s/step + eval 14min/200steps | ~5.4h | 0.0899 (step 5100) | 0.3649 (step 5000) |

### ETA Details

- **cls-8b-s42-resume**: Resumed from ckpt-600, running 3h. Effective speed ~11.7s/step (incl eval). ~17h remaining → finish ~May 16 01:00.
- **cwm-8b-conda-v4**: Resumed from ckpt-1600, running 7.2h. Evals every 100 steps (~19min each) dominate runtime. ~25h remaining → finish ~May 16 09:00.
- **cls-8b-seed123-conda-v3**: Resumed from ckpt-3000, running 7.2h. 77% complete. ~5.4h remaining → finish ~May 15 16:30.

### Notes

1. **CWM evals every 100 steps** is a major bottleneck — each eval takes ~19 minutes on 9335 validation samples, adding ~12h of eval-only time over the remaining 3800 steps. Consider increasing eval interval to 200 or 400 steps.
2. **cls-8b-s42-resume loss is high (0.89)** compared to seed123 (0.09) at the same training volume — it's still in early training (step 1542 vs seed123 at 5102), loss should decrease.
3. **cwm training loss (0.063) looks healthy** but eval_loss (0.426) is noticeably higher than CLS eval_loss (~0.32-0.36), suggesting CWM task is harder.

## Completed Evaluation

| Experiment | GPU | Status | Result |
|---|---|---|---|
| cls8b-s42-ckpt800-val8192-eval | 0 | **DONE** | Acc=84.53%, F1-macro=79.24% |

### Eval Results Detail (ckpt-800, val set 9335 samples)
- **Accuracy**: 84.53% (vs majority baseline 75.9%, +8.7pp gap)
- **F1 macro**: 79.24%
  - fail: P=67.0%, R=70.6%, F1=68.8%
  - pass: P=90.5%, R=89.0%, F1=89.7%
- Unparseable predictions: 9
- GPU 0 is now idle and available for new work.
