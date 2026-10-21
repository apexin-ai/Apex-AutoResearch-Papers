# check gpu status all4

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_gpu_status_all4_20260521T121339_result.json`
- **Structured JSON:** [`9843228c64aa4ea6e13b.json`](../../sessions/98/9843228c64aa4ea6e13b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

| GPU | 实验 | weighting | lr_scheduler | Step/Total | ETA | GPU Mem |
|-----|------|-----------|-------------|------------|-----|---------|
| cuda:0 | detect_remove_q05_seed42 | uniform | linear (default) | 1291/6103 | ~2h47m | 45634 MiB / 97887 MiB |
| cuda:1 | dr_epoch_matched_indep_lr_seed42 | uniform | linear (default) | 493/2533 | ~1h11m | 45634 MiB / 97887 MiB |
| cuda:2 | uniform_epoch_matched_indep_lr_seed42 | uniform | **见下方⚠️** | 478/2533 | ~2h33m | **91282 MiB** / 97887 MiB |
| cuda:3 | random_reweight_baseline_seed42 | adaptive | linear (default) | 687/6103 | ~3h21m | 45634 MiB / 97887 MiB |

**⚠️ cuda:2 有两个进程冲突：**
- PID 604879：`--lr_scheduler_type cosine`（显式传入）
- PID 606296：无 `--lr_scheduler_type`（默认 linear）
- 两个进程写同一个 output_dir `uniform_epoch_matched_indep_lr_seed42`，共享 GPU 2，导致显存占用翻倍（91GB），训练速度也减半（4.47s/it vs 正常 2.08s/it）

**补充：**
- cuda:2 uniform_epoch_matched 的日志头显示 `lr_scheduler_type: linear`（应该是后启动的 PID 606296 覆盖了日志）
- cuda:1 dr_epoch_matched 的 cmdline 和日志均无 `--lr_scheduler_type`，使用默认 linear
- 所有 4 个实验的 `training_args.json` 尚未生成（仅在训练完成后生成）

---
