# Experiment Status Check — Loop 19
**Time**: 2026-05-16 09:38 UTC

## GPU Usage (seetacloud-westd-4x5090)
| GPU | Model | VRAM Used | Utilization |
|-----|-------|-----------|-------------|
| 0 | RTX 5090 | 17611/32607 MiB (54%) | 75% |
| 1 | RTX 5090 | 21133/32607 MiB (65%) | 88% |
| 2 | RTX 5090 | 17609/32607 MiB (54%) | 99% |
| 3 | RTX 5090 | 21133/32607 MiB (65%) | 90% |

All 4 GPUs actively utilized.

## Experiment Status

### 1. cwm8b-ckpt400-test-eval-v3 (cuda:3, PID 443221)
- **PID**: ALIVE (elapsed 51 min)
- **Progress**: 5712/9784 (58.4%)
- **Accuracy**: 62.8% (on new=425 samples since resume from 5287)
- **Rate**: ~8.4 samples/min (8 per ~57s batch)
- **ETA**: ~8.1 hours (~17:45 UTC)
- **Registry**: RUNNING ✓

### 2. cwm8b-ckpt400-test-eval-shard2 (cuda:1)
- **PID**: ALIVE (process confirmed via ps)
- **Progress**: 7784/9784 (started from idx 7680, 104 new samples done)
- **Accuracy**: 69.2% (on 104 new samples)
- **Rate**: ~8.7 samples/min
- **ETA**: ~3.8 hours (~13:25 UTC)
- **Registry**: RUNNING ✓

### 3. cls8b-seed123-ckpt3000-mutation (cuda:0, PID 447483)
- **PID**: ALIVE (elapsed 16 min)
- **Progress**: 7330/9784 (74.9%)
- **Accuracy**: 85.4%
- **Rate**: ~470 samples/min (CLS is much faster than CWM)
- **ETA**: ~5 minutes (~09:43 UTC) — FINISHING SOON
- **Registry**: RUNNING ✓

### 4. cls8b-s42-resume-ckpt3600-test-v2 (cuda:2, PID 446868)
- **PID**: ALIVE (elapsed 19 min)
- **Progress**: 8630/9784 (88.2%)
- **Accuracy**: 84.3%
- **Rate**: ~459 samples/min
- **ETA**: ~2.5 minutes (~09:41 UTC) — FINISHING SOON
- **Registry**: Was ALLOCATED → updated to RUNNING ✓

## Registry Actions Taken
- `cls8b-s42-resume-ckpt3600-test-v2`: ALLOCATED → RUNNING (PID 446868 confirmed alive)

## Anomalies
- None. All 4 experiments running normally.

## Key Observations
- CLS s42-resume ckpt-3600: 84.3% acc — consistent with prior validation
- CLS seed123 ckpt-3000: 85.4% acc — slightly higher, cross-seed consistency good
- CWM ckpt-400 (v3, full test): 62.8% on new samples — still stabilizing
- CWM ckpt-400 (shard2, idx 7680+): 69.2% on 104 samples — early
- Two CLS evals should complete within minutes; two CWM evals have hours remaining
