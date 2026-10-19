# deploy magnitude bjb2 28827 batch

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_magnitude-bjb2-28827-batch_20260517T184737_result.json`
- **Structured JSON:** [`e837220de5f8ddc082cf.json`](../../sessions/e8/e837220de5f8ddc082cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

这 3 个实验**已经在跑了**，全部 6 个 GPU 都被占用：

| exp_id | 目标 GPU | 实际运行 GPU | 状态 |
|--------|---------|-------------|------|
| eval-obs-only-object-norm01-seed46 | cuda:1 | cuda:3 (PID 449068) | 运行中 |
| eval-obs-only-object-norm01-seed47 | cuda:3 | cuda:1 (PID 448782) | 运行中 |
| eval-perdof-object-norm02-seed43-r3 | cuda:5 | cuda:5 (PID 449339) | 运行中 |

GPU 分配和任务表中 seed46/seed47 的 GPU 编号对调了（1↔3），但实验本身完全一致（mode、norm_threshold、seed 都对）。其余 GPU 跑着其他实验：
- GPU 0: crm_k1_accg seed42
- GPU 2: crm_perdof seed47 norm0.2
- GPU 4: crm_perdof seed46 norm0.2

无需重新部署，3 个目标实验都已在运行中。

---
