# monitor training progress check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_monitor_training_progress_check_20260521T190045_result.json`
- **Structured JSON:** [`fd4477c8b29e0a5377a1.json`](../../sessions/fd/fd4477c8b29e0a5377a1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

```
实验1 (bs16_adaptive_tau07_seed123_r2): step 115/6103 (2%), loss=2.749, ETA ≈ 4h06m
  weighted_loss=2.455~3.173, ess≈8-13, tau=0.7, 速度 2.46s/step

实验2 (bs16_uniform_seed123):          step 793/6103 (13%), loss=1.946, ETA ≈ 3h36m
  b=0 (uniform weighting confirmed), ess=16, tau=0.8, 速度 2.44s/step

实验3 (detect_remove_q05_v2_seed42):   step 4394/6103 (72%), loss=11.19 ⚠️, ETA ≈ 59min
  ess=4, mean_q≈0.1-0.26, 速度 2.09s/step
  ⚠️ loss 异常高 (11.19), grad_norm=16.75, 可能出现训练不稳定

GPU utilization: cuda:0 100% (90G/96G), cuda:1 100% (90G/96G), cuda:2 0% (空闲), cuda:3 99% (45G/96G)
磁盘: /root/autodl-tmp 使用率 59%, 可用 103GB
```

**注意事项**:
- 实验3 的 loss=11.19 明显偏高（实验1/2 在 ~2.0 左右），grad_norm=16.75 也远高于实验2 的 4.4。建议关注后续 step 是否回落，如果持续高位可能需要检查是否有数据异常。
- 实验1 的实际 total steps 是 6103（不是预期的 3052），batch 可能不是 16 而是更小。
- cuda:2 完全空闲，无进程占用。

---
