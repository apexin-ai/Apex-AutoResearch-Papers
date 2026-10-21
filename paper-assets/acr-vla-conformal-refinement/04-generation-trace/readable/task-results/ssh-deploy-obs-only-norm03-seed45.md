# ssh deploy obs only norm03 seed45

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_deploy-obs-only-norm03-seed45_20260516T153635_result.json`
- **Structured JSON:** [`323909b67273f95b3784.json`](../../sessions/32/323909b67273f95b3784.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

cuda:2 上正在运行 `eval-object-perdof-norm03-seed44`（12分钟前启动）。

**停下来报告：cuda:2 被占用，不执行部署。**

当前 cuda:2 进程详情：
- **PID**: 505419
- **实验**: `eval_object_perdof_norm03_seed44` (CRM perdof mode, object benchmark, norm=0.3, seed=44)
- **启动时间**: 23:24:10（约12分钟前）
- **显存占用**: 5645MiB / 24564MiB

需要等该实验完成后再部署，或者指定其他空闲 GPU。

---
