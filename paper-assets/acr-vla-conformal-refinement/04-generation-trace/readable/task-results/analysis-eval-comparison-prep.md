# analysis eval comparison prep

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_eval-comparison-prep_20260513T231549_result.json`
- **Structured JSON:** [`8d7484ad22288b5c9be9.json`](../../sessions/8d/8d7484ad22288b5c9be9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Here's the status report:

## 3 Spatial Eval Experiments

All 3 eval processes are **running** (confirmed via `ps` and GPU utilization), started at ~07:04 UTC:

| Experiment | GPU | GPU Util | VRAM | Status |
|---|---|---|---|---|
| eval-spatial-v6-full (VLA-only) | cuda:0 | 22% | 12.0 GB | Running, no rollout output yet |
| eval-acr-spatial-v2 (ACR-VLA) | cuda:1 | 23% | 1.5 GB | Running, no rollout output yet |
| eval-reconvla-spatial-v3 (SampleConsensus) | cuda:2 | 21% | 6.7 GB | Running, no rollout output yet |

All 3 logs show model loaded + "10 tasks loaded" but **no rollout results printed yet** (~12 min elapsed). The evaluate.py uses `flush=True` on all prints, but shell-level pipe buffering through tmux may delay log output. The print happens after each rollout completes (line 306), so first output should appear soon.

**Time estimate**: 10 tasks × 10 rollouts × ~45s/rollout ≈ 75 min per eval. Expected completion: ~08:15–08:30 UTC.

Note: eval-acr-spatial-v2 is the only one with `--output_file` set (to `/root/autodl-tmp/eval_results/eval-acr-spatial-v2.json`). The other two (vla_only, reconvla) will only print results to stdout/log — no JSON output file. You may want to re-run them with `--output_file` later if structured results are needed, or parse from logs.

## CRM Ablation: crm-train-a3-obs-only (cuda:3)

- **PID 104611**: Running, GPU 3 at 10% util, 565 MB VRAM
- **Progress**: Epoch 6/50 (~20 min elapsed, ~3.3 min/epoch)
- **Best val_loss so far**: 0.018312 (epoch 4) — notably higher than full CRM's 0.009046, as expected for obs_only (no residual input)
- **ETA**: ~145 min remaining → completion around **09:40 UTC**

| Epoch | train_loss | val_loss | Best? |
|---|---|---|---|
| 1 | 0.059092 | 0.018489 | yes |
| 2 | 0.036756 | 0.018324 | yes |
| 3 | 0.028907 | 0.018316 | yes |
| 4 | 0.029013 | 0.018312 | yes |
| 5 | 0.029115 | 0.018319 | |
| 6 | 0.028937 | 0.018342 | |

Val loss is already plateauing at ~0.0183 (2x worse than full CRM's 0.009). This validates the importance of residual input in CRM — good ablation signal.

---
