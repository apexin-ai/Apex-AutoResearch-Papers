# fix cqa1 cleanup deploy random k075 s45

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_fix_cqa1_cleanup_deploy_random_k075_s45_20260528T005855_result.json`
- **Structured JSON:** [`a3e8b86dbcdce0185efa.json`](../../sessions/a3/a3e8b86dbcdce0185efa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

进程正在加载模型（config 确认 `prune=random, keep=0.75, eps=50`），GPU 显存分配即将完成。

**完成总结：**

| 操作 | 结果 |
|------|------|
| 杀 GPU 2 attn_k095_s42_v2 (PID 901265) | done |
| 杀 GPU 3 random_k095_v2 (PID 894077) | done |
| Registry 更新 (conclusion=killed, failure_reason) | done |
| 部署 random_k075_s45 → cuda:2 (PID 911227) | 启动中，模型加载中 |

cqa1-33015 当前布局：
- GPU 0: random k=0.5 s44 (运行中)
- GPU 1: l2norm k=0.95 s44 (运行中)
- GPU 2: **random k=0.75 s45** (新部署)
- GPU 3: 空闲

---
