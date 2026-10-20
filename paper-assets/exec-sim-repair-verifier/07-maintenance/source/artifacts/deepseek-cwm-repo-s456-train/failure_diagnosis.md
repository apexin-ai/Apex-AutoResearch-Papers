# Diagnosis: deepseek-cwm-repo-s456-train

**Date**: 2026-05-20 13:14 UTC
**Verdict**: FALSE POSITIVE — training is alive and running normally

## Root Cause

**Monitoring PID mismatch.** The monitoring system tracked PID 917644, which was a short-lived intermediate shell in the launch chain. The actual training process is PID 917649, running on GPU 2.

Process chain:
- PID 917648: `timeout 21600 env bash -c ...` (wrapper)
- PID 917649: `/root/miniconda3/bin/python train_unified.py ...` (actual training)
- PIDs 918097-918102: DataLoader workers

PID 917644 (monitored) != PID 917649 (actual). The monitoring system checked 917644 five times, found it dead, and auto-resolved as failed.

## Evidence: Training Is Running

- **GPU 2**: 16413MiB / 32607MiB used, 97% utilization
- **Progress**: step 468/2865 (16.3%), ~1.75s/it, ETA ~1h10m
- **Log**: clean startup, no errors, no warnings beyond expected deprecation notice
- **No exit sentinel**: `/tmp/agent-ml-exit/deepseek-cwm-repo-s456-train.exit` does not exist

## Log Excerpt (startup)

```
2026-05-20 13:00:00 INFO Model: deepseek-coder-6.7b-instruct -> family=deepseek
2026-05-20 13:00:00 INFO Loaded train=15290, val=1896
2026-05-20 13:00:18 INFO LoRA target modules: ['q_proj', 'k_proj', 'v_proj', 'o_proj']
2026-05-20 13:00:24 INFO Starting training...
trainable params: 16,777,216 || all params: 6,757,289,984 || trainable%: 0.2483
```

## GPU Status (all 4 GPUs)

| GPU | Process | VRAM | Util | Status |
|-----|---------|------|------|--------|
| 0 | Qwen3-8B CWM repo s123 (PID 886278) | 21246MiB/32607MiB | 99% | Running |
| 1 | (idle) | 0MiB | 100%* | No process |
| 2 | DeepSeek CWM repo s456 (PID 917649) | 16404MiB/32607MiB | 97% | Running |
| 3 | Qwen3-8B CWM repo s456 (PID 886352) | 31252MiB/32607MiB | 99% | Running |

*GPU 1 shows 100% util with 0MiB -- likely residual state or monitoring artifact.

## Disk Status

| Mount | Size | Used | Avail | Use% |
|-------|------|------|-------|------|
| / (root) | 30G | 22G | 8.6G | 72% |
| /root/autodl-tmp | 250G | 199G | 52G | 80% |

No disk pressure.

## Checkpoint Directory

`/root/autodl-tmp/checkpoints_deepseek_cwm_repo_s456/` is empty -- expected at 16% progress (checkpoints likely saved at epoch boundaries or specific step intervals).

## Action Required

1. **No retry needed** -- training is running fine with current config
2. **Fix monitoring**: the agent-ml monitoring should track the actual Python PID (917649), not the intermediate shell PID (917644). The launch wrapper chain creates multiple PIDs; the innermost Python process is the one to track.
3. **ETA**: at ~1.75s/step, remaining 2397 steps ~ 70 min. Expected completion ~14:25 UTC.
