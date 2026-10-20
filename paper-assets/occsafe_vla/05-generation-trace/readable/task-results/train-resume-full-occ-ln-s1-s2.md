# train resume full occ ln s1 s2

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_train_resume_full_occ_ln_s1_s2_20260524T175923_result.json`
- **Structured JSON:** [`159c6cbc1cab14089095.json`](../../sessions/15/159c6cbc1cab14089095.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。两个实验已从 20000 步 checkpoint 恢复训练，registry 已更新为 RUNNING。

| 实验 | GPU | seed | PID | log |
|------|-----|------|-----|-----|
| full_occ_ln_s1 | cuda:2 | 43 | 777222 | /root/runs/occsafe_vla/full_occ_ln_s1_resume.log |
| full_occ_ln_s2 | cuda:3 | 44 | 777428 | /root/runs/occsafe_vla/full_occ_ln_s2_resume.log |

- Checkpoint 加载已验证：proprio_projector, action_head, occ_head 均从 20000 步恢复
- 训练速度 ~1.05 it/s，剩余 30005 步，预计 ~8 小时完成
- 将在 log_step 30000/40000/50000 保存 checkpoint，50005 停止

---
