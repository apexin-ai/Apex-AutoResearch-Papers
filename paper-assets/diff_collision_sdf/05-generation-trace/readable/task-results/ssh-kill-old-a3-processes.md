# ssh kill old a3 processes

**How Action Collapse Creates Illusory Safety in Diffusion-Based VLA Collision Avoidance Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_kill_old_a3_processes_20260520T072830_result.json`
- **Structured JSON:** [`7620636e49201a6be2f1.json`](../../sessions/76/7620636e49201a6be2f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

清理完成。总结：

- **已 kill**: 旧 python 进程 38485 (GPU 0) 和 38564 (GPU 1)
- **保留运行中**: 新进程 50328 (GPU 0, spatial_bowl) 和 50407 (GPU 1, object_pudding)，均为 `--save_interval 2000 --resume`
- **GPU 显存**: 每卡从 ~34GB 降到 ~17GB
- **Checkpoint 状态**:
  - `spatial_bowl`: step 2500 (14:54) 和 3000 (15:23)
  - `object_pudding`: step 2500 (15:04)
  
  这些 checkpoint 数据有效，无需删除。

另外旧任务的 shell wrapper 进程（PID 33877/33881/33882/33956/33960/33961/38479/38480 等）仍残留，不占 GPU 但占少量内存，需要的话可以一并清理。

---
