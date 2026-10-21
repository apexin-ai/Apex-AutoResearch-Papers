# eval westd34685 check and eval v2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd34685_check_and_eval_v2_20260522T234802_result.json`
- **Structured JSON:** [`2c3f49886c580d29d36a.json`](../../sessions/2c/2c3f49886c580d29d36a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个实验全部**仍在训练中**，无 50000_chkpt 目录，均只有 40000_chkpt。

| 实验 | 当前 step | 进度 | 速度 | 预计剩余 |
|------|-----------|------|------|----------|
| cutoff_s0 | 46529/50005 | 93% | ~1.05 it/s | ~55 min |
| cutoff_s1 | 48600/50005 | 97% | ~1.06 it/s | ~22 min |
| depth_s0 | 48569/50005 | 97% | ~1.03 it/s | ~23 min |
| depth_s1 | 48434/50005 | 97% | ~1.04 it/s | ~25 min |

cutoff_s1 / depth_s0 / depth_s1 约 22-25 分钟后完成，cutoff_s0 约 55 分钟后完成。目前无法启动 eval，需要等训练结束产出 50000_chkpt。

---
