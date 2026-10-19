# deploy restart v4 default and perdof norm03 object

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_restart-v4-default-and-perdof-norm03-object_20260515T172554_result.json`
- **Structured JSON:** [`fa2881cb230c5f95b2d2.json`](../../sessions/fa/fa2881cb230c5f95b2d2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。总结：

**两个实验都已在运行**，无需额外部署：
- `eval-acr-object-v4-default` → PID 107658, GPU 3, 从头跑（max_correction_norm=None）
- `eval-mag-perdof-norm03-object` → PID 113552, GPU 3, norm=0.3

**风险点：两个 eval 共享 GPU 3**。GPU 2 有一个已完成实验的僵尸进程 (PID 13737, eval-mag-perdof-norm02 spatial)，杀掉后可以把其中一个迁移过去。要处理吗？

---
