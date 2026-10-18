# deploy cqa1 4gpu v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_4gpu_v2_20260526T050108_result.json`
- **Structured JSON:** [`639f0286063ff40cf4fd.json`](../../sessions/63/639f0286063ff40cf4fd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

发现 4 GPU 都有实验在跑。对比一下：

| GPU | 在跑的实验 | 用户要求 | 匹配？ |
|-----|-----------|---------|--------|
| 0 | π0.5 random k=0.75 libero_10 seed42 (1h18m) | π0.5 Random k=0.75 Long | **完全一致** |
| 1 | π0.5 attention k=0.75 libero_10 seed42 (1h18m) | π0.5 Attention k=0.75 Long | **完全一致** |
| 2 | OpenVLA attn k=0.9 goal seed43 (36m) | OpenVLA Attn k=0.9 Goal s43 | **完全一致** |
| 3 | OpenVLA random k=0.5 **object** (1h18m) | OpenVLA Random k=0.7 **goal** | **不一致** |

GPU 0/1/2 已经在跑你要的实验了。GPU3 跑的是 random k=0.5 object，你要的是 random k=0.7 goal。

需要 kill GPU3 的进程 (PID 4365) 然后部署新实验吗？还是等它跑完？

---
