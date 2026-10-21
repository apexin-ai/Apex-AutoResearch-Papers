# Diagnosis: eval_pi05_random_k085_long_seed42_strict_w27

## Status: COMPLETED SUCCESSFULLY (false alarm)

## Root Cause
Cron monitor looked for log at `~/runs/importance_margin_vla_compress/eval_pi05_random_k085_long_seed42_strict_w27.log` — file doesn't exist there.

Actual log location: `~/autodl-tmp/importance_margin_vla_compress/eval_pi05_random_k085_long_seed42_strict_w27.log` (project root, not ~/runs/).

The cron reported "failed to read log or log empty" because it checked the wrong path.

## Experiment Result
- **Model**: pi0.5
- **Pruning**: random, keep_ratio=0.85 (217/256 tokens)
- **Suite**: libero_10 (LIBERO Long)
- **Seed**: 42
- **Overall SR**: **44.0%** (220/500)
- **Runtime**: 169.8 min (~2.8h)
- **Started**: 2026-05-27 18:41:55
- **Finished**: 2026-05-27 21:33:19

### Per-task breakdown
| Task | Description | SR |
|------|------------|-----|
| T0 | alphabet soup + tomato -> basket | 42% |
| T1 | cream cheese + butter -> basket | 56% |
| T2 | stove on + moka pot | 54% |
| T3 | black bowl -> bottom drawer | 68% |
| T4 | white mug left + yellow mug right | 10% |
| T5 | book -> caddy back | 38% |
| T6 | white mug plate + chocolate pudding | 42% |
| T7 | alphabet soup + cream cheese -> basket | 44% |
| T8 | both moka pots -> stove | 14% |
| T9 | yellow white mug -> microwave | 72% |

## Result JSON
Saved at: `/root/autodl-tmp/importance_margin_vla_compress/eval_results/pi05_random_k0.85_libero_10_seed42.json`

## Server State
- **GPU**: 2x RTX PRO 6000 Black (96GB each), both idle (0MiB used)
- **Disk**: root 69% (9.4G free), /root/autodl-tmp 81% (48G free)
- **Active tmux sessions** (other experiments):
  - `pi05_attn_k075_long` — log 637 bytes only (may have stalled)
  - `pi05_attn_k07_long_rerun` — log 637 bytes only (may have stalled)
  - `pi05_l2norm_k07_long_rerun` — actively running (T1 in progress, T0=72%)

## No restart needed
Experiment already completed. Data is available in the JSON result file.
