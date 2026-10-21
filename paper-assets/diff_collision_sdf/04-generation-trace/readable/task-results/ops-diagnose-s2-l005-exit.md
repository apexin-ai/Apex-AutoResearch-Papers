# ops diagnose s2 l005 exit

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_diagnose_s2_l005_exit_20260523T055424_result.json`
- **Structured JSON:** [`e5831bd428052128d510.json`](../../sessions/e5/e5831bd428052128d510.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

诊断完成。总结：

- **根因**：磁盘满（`ENOSPC`），在 step 8000 保存 checkpoint 时触发 `OSError: No space left on device`
- **最终 step**：7999/30000（27%），运行约 5h33m
- **最后 checkpoint**：step 6000（best_loss=0.02684），step 4000 也保存了
- **最终 loss**（step 7999）：action≈0.024, sdf≈0.040, ee≈0.014
- **s2_l01 (cuda:3, PID 292370)**：也已死，确认是服务器级磁盘满事件，4 个实验全部阵亡
- **Registry**：已更新为 DONE/killed，notes 已写入诊断详情
- **Cron**：不存在，无需清除

---
