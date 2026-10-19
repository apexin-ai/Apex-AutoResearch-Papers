# deploy k20 object bjb2 40593

**Knowing When Not to Correct: Adaptive Test-Time Refinement for Vision-Language-Action Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_k20-object-bjb2-40593_20260519T142810_result.json`
- **Structured JSON:** [`05c9367b0644af318b4c.json`](../../sessions/05/05c9367b0644af318b4c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**问题：bjb2-40593 只有 1 块 GPU（RTX 4090 D），不存在 cuda:1/2/3。**

当前状态：
- GPU 0：99% 利用率，6296/24564 MiB 已用（应该是 Spatial K=10 seed43 在跑）
- GPU 1/2/3：**不存在**

无法在此服务器上部署这 3 个实验。需要：
1. 换一台多卡服务器，或
2. 等 GPU 0 的实验跑完后串行执行，或
3. 在其他服务器上并行跑

---
