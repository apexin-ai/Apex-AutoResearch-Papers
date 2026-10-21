# ssh check training 10894

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_check-training-10894_20260528T223243_result.json`
- **Structured JSON:** [`8e84e96d947de38cffbb.json`](../../sessions/8e/8e84e96d947de38cffbb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## random_occ_v2_s0 训练状态报告

| 项目 | 状态 |
|------|------|
| **进程** | **存活** (PID 33308, 已运行 3h01m) |
| **启动时间** | 2026-05-29 03:31:55 UTC |
| **当前 step** | 11,132 / 50,005 (22%) |
| **训练速度** | ~1.04 it/s |
| **已用时间** | ~3h00m |
| **预计剩余** | ~10h24m |
| **预计完成时间** | ~2026-05-29 17:00 UTC (北京时间 5月30日 01:00) |

### Loss 趋势
| Step | action_loss | occ_loss | depth_loss |
|------|------------|----------|------------|
| 0 | 0.6836 | 0.0000 | 0.0000 |
| 11,100 | 0.1338 | 0.0000 | 0.0000 |

### Checkpoint
- `10000_chkpt/` — ~15GB，包含 model safetensors + LoRA adapter (463M) + action_head (289M) + occ_head (2.4M) + proprio_projector (65M)

### 注意事项
1. **运行时间与预期不符**：你说 16-18h 前启动，但进程实际只跑了 3h。这说明原始进程可能崩溃后被重新启动了，或者是重新提交的任务。
2. **occ_loss 始终为 0.0000**：`--use_occ_head True --random_occ True` 配置下 occ_loss 全程为零，需确认这是否符合预期。
3. **DDL 风险**：C003 要求 2026-05-28 12:00 UTC 前完成，该 deadline 已过。当前实验预计还需 ~10h。

---
