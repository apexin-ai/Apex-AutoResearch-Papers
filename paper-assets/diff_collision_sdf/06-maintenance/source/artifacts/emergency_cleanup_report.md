# Emergency Cleanup & Training Health Check Report
**Date**: 2026-05-23 ~14:20 UTC

## Step 1: Disk Cleanup

| Item | Size |
|------|------|
| baseline_object_pudding | 76 GB |
| baseline_spatial_bowl | 76 GB |
| **Total freed** | **152 GB** |

| Metric | Before | After |
|--------|--------|-------|
| Used | 297 GB (85%) | 147 GB (42%) |
| Available | 54 GB | **204 GB** |

## Step 2: Training Health Check

### GPU Memory
| GPU | Memory Used | Utilization |
|-----|-------------|-------------|
| 0 | 19,179 MiB / 97,887 MiB | 100% |
| 1 | 19,179 MiB / 97,887 MiB | 100% |
| 2 | 19,179 MiB / 97,887 MiB | 100% |
| 3 | 19,179 MiB / 97,887 MiB | 100% |

### Training Progress
| Run | Current Step | Loss | SDF Loss | EE Loss | Speed |
|-----|-------------|------|----------|---------|-------|
| s1_l005 | ~6868 | 0.032 | 0.032 | 0.048 | 1.20 s/it |
| s1_l01 | ~6862 | 0.036 | 0.032 | 0.050 | 1.20 s/it |
| s2_l005 | ~6859 | 0.035 | 0.035 | 0.047 | 1.21 s/it |
| s2_l01 | ~6865 | 0.027 | 0.032 | 0.034 | 1.20 s/it |

All 4 processes alive (PIDs: 341795, 341870, 342010, 342695).

### Phase 2 Transition FAILED on Resume

**Expected**: Phase 2 activates at step 5000, unfreezing 33.47M LoRA params → ~27GB GPU memory.

**Actual**: All 4 runs at 19GB GPU memory (Phase 1 level). Only SDF decoder (396K) + EE extractor (263K) trainable. LoRA remains frozen.

**Root cause**: Resume from step 6000 skipped the Phase 2 transition check at step 5000. The transition logic likely only fires at exactly `step == phase1_warmup_steps` and does not check `step >= phase1_warmup_steps` on resume.

**Impact**: Steps 6000-6868+ are training only auxiliary heads without LoRA backbone fine-tuning. SDF/EE losses are decreasing (good for heads), but the main action policy is NOT being fine-tuned.

## Action Required

**P0**: Fix Phase 2 activation logic to handle resume case (`step >= phase1_warmup_steps`), then restart all 4 runs from step 6000 checkpoint.
