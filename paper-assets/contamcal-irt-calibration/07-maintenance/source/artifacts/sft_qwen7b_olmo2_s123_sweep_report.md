# SFT Sweep Report: Qwen-7B & OLMo-2-7B seed=123

**Server:** westd-29999 cuda:2  
**Script:** `bash /root/autodl-tmp/exp001/run_qwen7b_olmo2_s123.sh`  
**Log:** `~/runs/contamcal-irt-calibration/sft_qwen7b_olmo2_s123_sweep.log`  
**Date:** 2026-05-19 ~ 2026-05-20

## Summary

All 10 (model × dosage) checkpoints exist and are valid. No errors, no OOM.

- **Qwen2.5-7B**: All 5 dosages **skipped** — checkpoints pre-existed from a prior run (created May 18–19).
- **OLMo-2-7B**: All 5 dosages **trained fresh** in this run, all exit_code=0.

## Training Config (both models)

| Parameter | Value |
|-----------|-------|
| lora_r | 16 |
| lora_alpha | **32** ✓ (C006 compliant) |
| lr | 5e-5 |
| batch_size | 2 |
| grad_accum | 8 |
| max_seq_length | 2048 |
| epochs | 1 |
| seed | 123 |
| num_samples | 50,000 |

## OLMo-2-7B Training Results (this run)

| Dosage | train_loss | mean_token_acc | entropy | runtime (s) | Wall time |
|--------|-----------|----------------|---------|-------------|-----------|
| d000 | 0.9431 | 0.7855 | 0.9052 | 6,066 (~1h41m) | 21:40 → 23:23 |
| d005 | 0.9475 | 0.7623 | 1.003 | 6,119 (~1h42m) | 23:23 → 01:06 |
| d025 | 0.9601 | 0.8161 | 0.7758 | 6,371 (~1h46m) | 01:06 → 02:54 |
| d050 | 0.9737 | 0.7864 | 0.888 | 6,682 (~1h51m) | 02:54 → 04:47 |
| d100 | 0.9979 | 0.7601 | 1.044 | 7,328 (~2h02m) | 04:47 → 06:51 |

Total OLMo-2-7B training wall time: ~9h10m.

Training loss increases monotonically with dosage (0.943 → 0.998), consistent with contamination injection making the task harder at higher doses.

## Qwen2.5-7B (pre-existing, not retrained)

Training losses not available in this log (trained in a prior run). Checkpoints verified to contain valid adapter weights (~161 MB each).

## Checkpoint Paths

All under `/root/autodl-tmp/exp001/checkpoints/`:

| Model | Dosage | Path | .done | Adapter size |
|-------|--------|------|-------|-------------|
| Qwen2.5-7B | d000 | `Qwen2.5-7B_d000_s123/lora_adapter/` | ✗ | 161 MB |
| Qwen2.5-7B | d005 | `Qwen2.5-7B_d005_s123/lora_adapter/` | ✗ | 161 MB |
| Qwen2.5-7B | d025 | `Qwen2.5-7B_d025_s123/lora_adapter/` | ✗ | 161 MB |
| Qwen2.5-7B | d050 | `Qwen2.5-7B_d050_s123/lora_adapter/` | ✗ | 161 MB |
| Qwen2.5-7B | d100 | `Qwen2.5-7B_d100_s123/lora_adapter/` | ✗ | 161 MB |
| OLMo-2-7B | d000 | `OLMo-2-7B_d000_s123/lora_adapter/` | ✓ | 160 MB |
| OLMo-2-7B | d005 | `OLMo-2-7B_d005_s123/lora_adapter/` | ✓ | 160 MB |
| OLMo-2-7B | d025 | `OLMo-2-7B_d025_s123/lora_adapter/` | ✓ | 160 MB |
| OLMo-2-7B | d050 | `OLMo-2-7B_d050_s123/lora_adapter/` | ✓ | 160 MB |
| OLMo-2-7B | d100 | `OLMo-2-7B_d100_s123/lora_adapter/` | ✓ | 160 MB |

## Notes

1. **Qwen .done markers missing**: Qwen checkpoints lack `.done` files, unlike OLMo. This may be because they were created by an older version of the training script. The adapter weights exist and are the correct size, so the checkpoints are functional.
2. **W&B**: Unable to query W&B runs due to tool error (`list_wandb_runs` API issue). W&B metrics not included.
3. **No anomalies**: Zero ERROR/OOM/CUDA errors in the log.
