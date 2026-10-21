# deploy mag perdof object bjb2

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_mag-perdof-object-bjb2_20260515T165718_result.json`
- **Structured JSON:** [`2dedbd7ac450db2b6e37.json`](../../sessions/2d/2dedbd7ac450db2b6e37.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

实验 1 已注册为 RUNNING。

**部署状态：**

| 实验 | GPU | 状态 |
|------|-----|------|
| eval-mag-perdof-norm005-object (norm=0.05) | GPU 1 | RUNNING, PID 109650 |
| eval-mag-perdof-norm03-object (norm=0.3) | — | QUEUED，等待 GPU 释放 |

6 块 GPU 全满，无法立即部署实验 2。当前其他 GPU 任务：
- GPU 0: perdof object norm003 (~10min)
- GPU 2: acr_vla spatial (~13h)
- GPU 3: perdof object default_norm (~6min)
- GPU 4/5: obs_only object norm005/norm03 (~28min)

GPU 0 或 GPU 3 上的实验最先完成，届时可部署 norm=0.3。需要我等 GPU 释放后自动部署，还是稍后手动部署？

---
