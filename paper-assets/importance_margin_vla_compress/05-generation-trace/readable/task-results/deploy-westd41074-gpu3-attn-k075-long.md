# deploy westd41074 gpu3 attn k075 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074-gpu3-attn-k075-long_20260526T183244_result.json`
- **Structured JSON:** [`8fc1554b9689e759e6c6.json`](../../sessions/8f/8fc1554b9689e759e6c6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**GPU 3 被占用，无法立即部署。**

当前 4 块 GPU 全部在跑任务：

| GPU | PID | 启动时间 | 任务 |
|-----|-----|---------|------|
| 0 | 682346 | 22:32 | random_prune k=0.85 libero_object |
| 1 | 652888 | 21:32 | attn_prune k=0.5 libero_object |
| 2 | 755986 | 00:41 | attn_prune k=0.75 libero_object |
| 3 | 824210 | 02:29 | **attn_prune k=0.75 libero_10 unnorm_key=libero_10** |

GPU 3 上 3 分钟前刚启动了一个类似实验，但用的是 `--unnorm_key libero_10`（非 Long 版本），我们需要的是 `--unnorm_key bridge_orig`（Long 版本）。

模型路径确认：`/root/autodl-tmp/openvla-7b-finetuned-libero-10/`

Registry 已创建（PREPARING 状态）。

**需要决策**：等 GPU 3 当前任务跑完后再部署，还是 kill 掉 PID 824210 腾出 GPU 3？

---
