# train reverse cutoff s2 fresh

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_reverse_cutoff_s2_fresh_20260525T043824_result.json`
- **Structured JSON:** [`ce6e39fbdc96cbb95468.json`](../../sessions/ce/ce6e39fbdc96cbb95468.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

训练已正常运行。

**结果汇总：**
- 已 kill 旧的 resume 进程 (PID 5764)
- `reverse_cutoff_s2_v3` 从 pretrained 权重 (`/root/autodl-tmp/models/openvla-7b`) 从头训练，**无 --resume**
- 服务器: westd-34685, GPU: cuda:1
- **PID: 8347**
- step 0 开始，`occ_loss_cutoff_step=35000, mode=before`（前 35K 步无 OCC loss）
- tmux session: `reverse_cutoff_s2_v3`
- 日志: `~/runs/occsafe_vla/reverse_cutoff_s2_v3.log`
- Registry 状态: RUNNING

---
