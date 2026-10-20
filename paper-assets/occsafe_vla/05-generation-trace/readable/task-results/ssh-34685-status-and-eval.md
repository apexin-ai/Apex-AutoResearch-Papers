# ssh 34685 status and eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_34685_status_and_eval_20260526T033800_result.json`
- **Structured JSON:** [`fcc530b9588a09fb56c6.json`](../../sessions/fc/fcc530b9588a09fb56c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验仍在训练中，没有完成的。

## 34685 状态

| 实验 | 训练状态 | 当前 step | 进度 | 剩余时间 | GPU |
|------|---------|----------|------|---------|-----|
| detach_bn_v2_s0 | 训练中 | ~36035/50005 | 72% | ~3h35m | cuda:0 (99%) |
| detach_bn_v2_s1 | 训练中 | ~36105/50005 | 72% | ~3h35m | cuda:1 (99%) |
| detach_bn_v2_s2 | 训练中 | ~35977/50005 | 72% | ~3h37m | cuda:2 (41%) |
| full_occ_bn_v2_s1 | 训练中 | ~34552/50005 | 69% | ~4h00m | cuda:3 (99%) |

- **预计完成时间**：detach_bn_v2 三个 seed 约 3.5h 后完成，full_occ_bn_v2_s1 约 4h 后完成
- **空闲 GPU**：无
- **50K checkpoint**：均未到达，无法启动 eval
- 所有实验速度正常 ~1.07-1.08 it/s，loss 正常下降

D051 预估 14:30 完成的判断偏早，实际还需约 3.5-4 小时。

---
