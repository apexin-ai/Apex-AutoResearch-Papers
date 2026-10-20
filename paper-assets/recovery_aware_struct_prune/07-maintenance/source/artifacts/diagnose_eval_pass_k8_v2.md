# Diagnosis: eval_pass_k8_standard_20_grpo_qwen_math_v2

## Verdict: FALSE POSITIVE — Experiment Completed Successfully

The monitoring system reported "process dead 5x with no sentinel/W&B" and auto-resolved as failed, but the experiment actually ran to completion.

## Evidence

- **Log file**: `/root/runs/recovery_aware_struct_prune/eval_pass_k8_standard_20_v2.log` (17,519 bytes)
- **Start**: 2026-05-17 05:54:56 — model loaded from `/root/autodl-tmp/recovery_aware_struct_prune/grpo_standard_qwen_math`
- **End**: 2026-05-17 07:05:33 — all 200 samples evaluated (runtime ~1h11m)
- **Results JSON**: `/root/autodl-tmp/recovery_aware_struct_prune/results/eval_pass_k8_standard_20_grpo_qwen_math_v2.json` (exists, complete)

## Results

| Metric | Value |
|--------|-------|
| GSM8K pass@8 | **0.9100 ± 0.0202** |
| Coverage (any correct) | 0.9100 |
| EOS rate | 0.999375 (1599/1600 natural EOS, 1 truncated) |
| Avg response length | 130.0 tokens |
| N problems | 200 |
| k | 8 |
| Temperature | 0.7 |

## Why the Monitor Reported Failure

The eval script completed and exited normally, but:
1. **No sentinel file** was written (eval script likely doesn't produce one)
2. **No W&B logging** was configured for this eval run

The monitor polled the process 5 times, found it dead each time (because it had already finished), and classified it as failed. This is a monitoring gap: short-lived eval jobs that finish between polling intervals get misclassified.

## Root Cause

**Not a real failure.** Monitor false positive due to missing sentinel/W&B integration in the eval script.

## Recommended Fix

To prevent future false positives, consider one of:
- Add a sentinel file write at the end of the eval script (e.g., `touch /root/runs/.../eval_pass_k8_v2.sentinel`)
- Or teach the monitor to check for the results JSON as a completion signal
