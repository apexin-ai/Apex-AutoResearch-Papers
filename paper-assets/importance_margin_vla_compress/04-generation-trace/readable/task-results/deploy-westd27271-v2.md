# deploy westd27271 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd27271_v2_20260526T050118_result.json`
- **Structured JSON:** [`c12b4bcb5fbd8c0bee4b.json`](../../sessions/c1/c12b4bcb5fbd8c0bee4b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个 GPU 上已有运行中的实验：

| GPU | PID | 命令 | 状态 |
|-----|-----|------|------|
| GPU0 | 11195 | `l2norm_prune k=0.9 goal seed43` | **与你要部署的实验1完全相同** |
| GPU1 | 11378 | `random_prune k=0.9 goal seed43` | **与实验2不同**（你要的是 k=0.5 seed42） |

模型路径确认：`/root/autodl-tmp/openvla-7b-finetuned-libero-goal`

**GPU0 的实验已经在跑你要的 L2norm k=0.9 Goal seed43，无需重复提交。**

GPU1 当前跑的是 Random k=0.9 seed43，需要 kill 才能部署 Random k=0.5 seed42。要 kill PID 11378 并部署新实验吗？还是等它跑完？

---
