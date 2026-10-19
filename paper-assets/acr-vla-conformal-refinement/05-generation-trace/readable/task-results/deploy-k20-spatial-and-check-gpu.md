# deploy k20 spatial and check gpu

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_k20-spatial-and-check-gpu_20260521T050417_result.json`
- **Structured JSON:** [`17c787a69e9cb04b8f2e.json`](../../sessions/17/17c787a69e9cb04b8f2e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个任务全部启动成功，正在加载模型/环境。

## 部署结果

| 任务 | 服务器 | GPU | 状态 |
|------|--------|-----|------|
| K=20 Spatial seed42 | bjb1-32546 | cuda:2 | 运行中，加载 SmolVLA |
| K=20 Spatial seed43 | bjb1-18228 | cuda:1 | 运行中，加载 LIBERO spatial 环境 |
| K=20 Spatial seed44 | bjb1-18228 | cuda:2 | 运行中，加载 LIBERO spatial 环境 |
| K=20 Object seed45 | bjb2-28827 | cuda:5 | 运行中，加载 LIBERO object 环境 |

**未部署**（GPU 不足）：
- K=20 Object seed46, seed47 — bjb2-28827 仅 1 个空闲 GPU，需等当前 5 个 eval 任务完成后部署

---
