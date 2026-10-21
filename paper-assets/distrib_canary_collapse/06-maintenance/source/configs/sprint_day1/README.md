# Day 1 Sprint Experiments

Generated: 2026-05-18

Target server: **westd-17855** (6x RTX PRO 6000 98GB)
Fallback server: westd-19828

## Parameter Compatibility Notes

| Requested param | Actual support |
|----------------|---------------|
| `--bf16` | NOT supported (script uses fp32/auto) |
| `--optimizer` | Use `--optim` instead |
| `--data_strategy accumulate` | Use `--accumulate` flag |
| `--gradient_checkpointing` | Supported (added for 1.3B+ models) |

## Experiment List

| # | File | Plan | Model | Data | Alpha | Seed | Category | Est Hours |
|---|------|------|-------|------|-------|------|----------|-----------|
| 1 | `plan_034_gpt2m_s43.sh` | plan_034 | gpt2-medium | wikitext103_5k | 1.0 | 43 | generalize | ~4h |
| 2 | `plan_030_opt_s43.sh` | plan_030 | opt-1.3b | wikitext103_5k | 1.0 | 43 | generalize | ~8h |
| 3 | `plan_031_interv_pred_s43.sh` | plan_031 | pythia-410m | wikitext103_5k | 1.0 | 43 | intervention | ~5h |
| 4 | `plan_032_interv_react_s43.sh` | plan_032 | pythia-410m | wikitext103_5k | 1.0 | 43 | intervention | ~5h |
| 5 | `plan_033a_interv_a075_pred.sh` | plan_033 | pythia-410m | wikitext103_5k | 0.75 | 42 | intervention | ~5h |
| 6 | `plan_033b_interv_a075_react.sh` | plan_033 | pythia-410m | wikitext103_5k | 0.75 | 42 | intervention | ~5h |
| 7 | `plan_026_a060_s42.sh` | plan_026 | pythia-410m | wikitext103_5k | 0.60 | 42 | alpha_sweep | ~4h |
| 8 | `plan_035_c4_a075.sh` | plan_035 | pythia-410m | c4_5k | 0.75 | 42 | alpha_sweep_c4 | ~4h |
| 9 | `plan_036_14b_c4.sh` | plan_036 | pythia-1.4b | c4_5k | 1.0 | 42 | generalize | ~8h |
| 10 | `plan_008_ablation_accum.sh` | plan_008 | pythia-410m | wikitext103_5k | 0.50 | 42 | ablation | ~4h |
| 11 | `plan_039_a010_s43.sh` | plan_039 | pythia-410m | wikitext103_5k | 0.10 | 43 | alpha_sweep | ~4h |
| 12 | `plan_040_a060_s43.sh` | plan_040 | pythia-410m | wikitext103_5k | 0.60 | 43 | alpha_sweep | ~4h |
| 13 | `plan_004a_c4_a050_s42.sh` | plan_004 | pythia-410m | c4_5k | 0.50 | 42 | alpha_sweep_c4 | ~4h |
| 14 | `plan_004b_c4_a050_s43.sh` | plan_004 | pythia-410m | c4_5k | 0.50 | 43 | alpha_sweep_c4 | ~4h |
| 15 | `plan_004c_c4_a050_s44.sh` | plan_004 | pythia-410m | c4_5k | 0.50 | 44 | alpha_sweep_c4 | ~4h |
| 16 | `plan_037a_interv_14b_pred.sh` | plan_037 | pythia-1.4b | wikitext103_5k | 1.0 | 42 | intervention | ~8h |
| 17 | `plan_037b_interv_14b_react.sh` | plan_037 | pythia-1.4b | wikitext103_5k | 1.0 | 42 | intervention | ~8h |

**Total: 17 experiments**

## Suggested GPU Assignment (6 GPUs)

Strategy: large models (OPT-1.3b, Pythia-1.4b) take 1 GPU each; Pythia-410m experiments queue on remaining GPUs.

### Wave 1 (start immediately, ~4-8h)

| GPU | Experiment | Est Time |
|-----|-----------|----------|
| GPU 0 | plan_030 (OPT-1.3b) | ~8h |
| GPU 1 | plan_036 (Pythia-1.4b C4) | ~8h |
| GPU 2 | plan_034 (GPT2-medium) | ~4h |
| GPU 3 | plan_031 (interv pred s43) | ~5h |
| GPU 4 | plan_032 (interv react s43) | ~5h |
| GPU 5 | plan_026 (a060 s42) | ~4h |

### Wave 2 (after Wave 1 GPUs free up, ~4-5h)

| GPU | Experiment | Est Time |
|-----|-----------|----------|
| GPU 2 | plan_033a (interv a075 pred) | ~5h |
| GPU 3 | plan_033b (interv a075 react) | ~5h |
| GPU 4 | plan_035 (C4 a075) | ~4h |
| GPU 5 | plan_008 (ablation accum) | ~4h |

### Wave 3 (backfill)

| GPU | Experiment | Est Time |
|-----|-----------|----------|
| GPU 2 | plan_039 (a010 s43) | ~4h |
| GPU 3 | plan_040 (a060 s43) | ~4h |
| GPU 4 | plan_004a (C4 a050 s42) | ~4h |
| GPU 5 | plan_004b (C4 a050 s43) | ~4h |

### Wave 4 (final)

| GPU | Experiment | Est Time |
|-----|-----------|----------|
| GPU 0 | plan_037a (interv 1.4b pred) | ~8h |
| GPU 1 | plan_037b (interv 1.4b react) | ~8h |
| GPU 2 | plan_004c (C4 a050 s44) | ~4h |

## Dependencies

- plan_037a/b (1.4b intervention) depends on plan_036 (1.4b baseline) completing to validate model works
- plan_033a/b (a075 intervention) independent of plan_031/032 (a100 intervention)
- All C4 experiments (plan_004a/b/c, plan_035, plan_036) require `data/c4_5k` to be synced to westd-17855
- All wikitext experiments require `data/wikitext103_5k` to be synced to westd-17855
- HF model cache: if westd-17855 has no cache, first run per model will download (~1-3GB each)

## Quick Launch Commands

Each .sh file contains the full `bash -c "..."` command ready for `submit_training_job`.

To run directly on the server:
```bash
# Single experiment
CUDA_VISIBLE_DEVICES=0 bash configs/sprint_day1/plan_034_gpt2m_s43.sh &

# Or use nohup for persistence
CUDA_VISIBLE_DEVICES=0 nohup bash configs/sprint_day1/plan_034_gpt2m_s43.sh > logs/plan_034.log 2>&1 &
```

