# train grid b0 1 seed42 30476

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_grid_b0_1_seed42_30476_20260517T171837_result.json`
- **Structured JSON:** [`0939be359f2d21d496c3.json`](../../sessions/09/0939be359f2d21d496c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常启动。

**训练状态：**
- **PID**: 34704
- **tmux session**: `grid_b0_1_seed42`
- **GPU**: westd-30476 cuda:0
- **速度**: ~2.18 s/it，预计总时长 ~3h41m
- **参数**: `--weighting_method grid --grid_b_value 0.1`，save_steps=500（与 b0.2/b0.3 一致）
- **输出**: `/root/autodl-tmp/output/models/grid_b0_1_seed42`
- **日志**: `~/runs/provenance_weight_training/grid_b0_1_seed42.log`

b=0.1 的 weighting 指标看起来正常，`alpha_eff` 分布合理（0.03~0.77），ESS 在 3.5~4.0 范围，符合低 b 值的预期行为。

---
