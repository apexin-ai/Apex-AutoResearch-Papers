# Batch Failure Diagnosis — westd-34685, 2026-05-28 ~01:53 UTC

## Summary

**Root Cause**: `save_training_checkpoint` calls `AutoModelForVision2Seq.from_pretrained(cfg.vla_path)` to merge LoRA weights into the base model (finetune.py:727). The failed experiments were launched with `--vla_path` pointing to a previous checkpoint that no longer exists on disk — the cleanup mechanism deleted it while training was still running.

**NOT** OOM, disk full, or CUDA error. Disk is fine (autodl-tmp 32% used, 240GB free). GPUs 0/1 are now idle; GPUs 2/3 still running.

## Per-Experiment Errors

### detach_ln_v2_s2 (cuda:0)
- **vla_path**: `/root/autodl-tmp/checkpoints/detach_ln_v2_s2/...--detach_ln_v2_s2--15000_chkpt`
- **Error**: `OSError: Incorrect path_or_model_id` — 15000_chkpt path does not exist
- **Crash time**: 2026-05-28 09:52:02 CST = ~01:52 UTC
- **Progress at crash**: 11753/35005 (~34%)
- **Existing checkpoints**: `--20000_chkpt`, `--25000_chkpt`, `--30000_chkpt` (15000 was deleted)

### vanilla_object_s0 (cuda:1)
- **vla_path**: `/root/autodl-tmp/checkpoints/vanilla_object_s0/...--vanilla_object_s0--10000_chkpt`
- **Error**: Same `OSError` — 10000_chkpt does not exist
- **Crash time**: 2026-05-28 09:51:23 CST = ~01:51 UTC
- **Progress at crash**: ~15k steps (estimated from 4h12m runtime at ~1 it/s)
- **Existing checkpoints**: `--15000_chkpt`, `--20000_chkpt`, `--25000_chkpt` (10000 was deleted)

### detach_bn_object_s0 / full_occ_bn_object_s0
- **Log files not found** on westd-34685. These experiments may be on a different server or have different log paths.

## Common Error Pattern

All confirmed failures share the exact same call chain:
```
finetune.py:1265 → save_training_checkpoint()
finetune.py:727  → AutoModelForVision2Seq.from_pretrained(cfg.vla_path)
                 → cached_file() → OSError (path not found)
```

The failed experiments were **resumed from a previous checkpoint** (`--vla_path=<checkpoint_path>`). The cleanup mechanism deleted that checkpoint, making the LoRA merge during save impossible.

The still-running experiments (full_occ_ln_v2_s3 cuda:2, detach_ln_v2_s3 cuda:3) use `--vla_path=/root/autodl-tmp/models/openvla-7b` (original pretrained) and are **not affected**.

## System State (diagnosis time 09:55 CST)

| Resource | Status |
|----------|--------|
| GPU 0 | idle, 0MiB |
| GPU 1 | idle, 0MiB |
| GPU 2 | full_occ_ln_v2_s3, 62209MiB, 99% util |
| GPU 3 | detach_ln_v2_s3, 62203MiB, 77% util |
| Disk (root) | 39% used |
| Disk (autodl-tmp) | 32% used, 240GB free |
| Cleanup scripts | DISABLED (last ran May 21) |

## Restart Options

### Option A: Disable LoRA merge during training (recommended)
Restart with `--merge_lora_during_training=false`. LoRA adapter is still saved at each checkpoint; merge offline after training. Avoids needing `cfg.vla_path` during saves.

### Option B: Use latest checkpoint as new base
- detach_ln_v2_s2: `--vla_path=...--30000_chkpt`, fresh LoRA from step 0
- vanilla_object_s0: `--vla_path=...--25000_chkpt`, fresh LoRA from step 0
- Downside: retrains from scratch on new base, doubles wall time

### Option C: Use existing checkpoints as-is (no restart)
- detach_ln_v2_s2: 30000-step merged checkpoint exists
- vanilla_object_s0: 25000-step merged checkpoint exists
- If eval target was ~35k steps, these may be close enough
