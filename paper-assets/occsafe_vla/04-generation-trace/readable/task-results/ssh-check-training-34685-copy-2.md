# ssh check training 34685

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-training-34685_20260528T223237_result.json`
- **Structured JSON:** [`c35f11e8e38616deecb6.json`](../../sessions/c3/c35f11e8e38616deecb6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## full_occ_bn_v2_s2_r2 状态汇总

| 项目 | 状态 |
|------|------|
| **进程** | ALIVE, PID 19218, 已运行 3h01m |
| **当前 step** | 11006 / 50005 (**22%**) |
| **速度** | ~1.02 it/s |
| **已用时间** | 3h00m |
| **预计剩余** | ~10.7h |
| **预计完成时间** | ~2026-05-29 17:15 UTC |
| **启动时间** | 2026-05-29 03:31 UTC |

### Loss 趋势
| Step | action_loss | occ_loss | depth_loss |
|------|------------|----------|------------|
| 0 | 0.6016 | 0.0000 | 0.0000 |
| 11000 | 0.1094 | 0.0000 | 0.0000 |

### Checkpoint
- `10000_chkpt/` — ~15GB（含 model safetensors + lora_adapter 463MB + action_head 289MB + occ_head 2.4MB + proprio_projector 65MB）
- 下一个 checkpoint 在 step 20000

### 异常

1. **进程仅运行 3h，不是 16-18h。** 启动时间为 2026-05-29 03:31 UTC，说明这是一次较新的启动（可能之前的运行失败/被中断后重新启动了）。

2. **occ_loss 和 depth_loss 始终为 0.0000。** 虽然 `--use_occ_head True --occ_detach False`，但 occ head 没有产生 loss。需要确认这是否符合预期（可能是 v2 版本 occ head 的 loss 权重被设为 0，或者数据中没有 occupancy 标签）。

3. **DDL 风险：** 约束 C003 要求 2026-05-28 12:00 UTC 前完成，但该实验预计 2026-05-29 17:15 UTC 才能完成，已超出 DDL 约 29 小时。

---
