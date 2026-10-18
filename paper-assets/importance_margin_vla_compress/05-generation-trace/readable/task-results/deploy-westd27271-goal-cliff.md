# deploy westd27271 goal cliff

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_goal_cliff_20260526T091847_result.json`
- **Structured JSON:** [`0bdb27c8f65177a4d199.json`](../../sessions/0b/0bdb27c8f65177a4d199.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

服务器 westd-27271 只有 **2 张 GPU**（RTX PRO 6000 Blackwell），不是 4 张：

- **GPU 0**: 空闲（1 MiB, 0%）
- **GPU 1**: 占用中（15964 MiB, 86%）— eval_openvla_attn_k09_goal_seed43_v4

不存在 cuda:2 和 cuda:3。只能用 GPU 0 跑 1 个实验。

**方案选择**：
1. GPU 0 上串行跑 3 个实验（一个跑完再启动下一个）
2. 先在 GPU 0 上跑 1 个优先级最高的，其余等 GPU 1 释放后再跑
3. 找其他服务器部署

怎么处理？

---
