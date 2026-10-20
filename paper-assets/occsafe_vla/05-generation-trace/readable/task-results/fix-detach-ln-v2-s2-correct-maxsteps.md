# fix detach ln v2 s2 correct maxsteps

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_detach_ln_v2_s2_correct_maxsteps_20260528T020958_result.json`
- **Structured JSON:** [`7fd9a563998aa83ac81d.json`](../../sessions/7f/7fd9a563998aa83ac81d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常运行。

**汇总：**
- 旧进程 PID 45380：已 kill（force_killed）
- 25000_chkpt：完整（4 shards + index.json + action_head/occ_head/proprio_projector checkpoints）
- 新进程 PID：47162，westd-34685:cuda:0
- max_steps：50005（已修正），从 resume_step=25000 恢复
- 训练已在出 step，~1.35s/it，日志正常（step=0 时 action_loss=0.0825）

---
