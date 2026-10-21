# deploy bjb2 28827 fill gpus

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_bjb2-28827-fill-gpus_20260515T191423_result.json`
- **Structured JSON:** [`7cc9872171366cbc8dfd.json`](../../sessions/7c/7cc9872171366cbc8dfd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

6 个 GPU 全部有进程占用：

| GPU | 显存占用 | 状态 |
|-----|---------|------|
| 0 | 5200 MiB | 已有实验 (perdof norm003 object) |
| 1 | 5200 MiB | 已有实验 (perdof norm005 object) |
| **2** | **23698 MiB** | **eval-mag-perdof-norm03-object-r2 ✓** |
| **3** | **6239 MiB** | **eval-mag-perdof-norm02-seed43-object ✓** |
| 4 | 5200 MiB | 已有实验 (obsonly norm005 object) |
| 5 | 5200 MiB | 已有实验 (obsonly norm03 object) |

两个实验已成功部署，注册表已更新为 RUNNING。

---
