# deploy cqa1 gpu2 pi05 next

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1_gpu2_pi05_next_20260526T150044_result.json`
- **Structured JSON:** [`d762862a399ab8d17473.json`](../../sessions/d7/d762862a399ab8d17473.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

所有 4 个实验都在活跃运行中，进度如下：

| GPU | 实验 | 进度 | 预计完成 |
|-----|------|------|---------|
| 0 | random k=0.85 | Task 4/10 | ~60% |
| 1 | l2norm k=0.85 | Task 2/10 | ~30% |
| 2 | attention k=0.5 | Task 0/10 | ~4% (刚开始) |
| 3 | attention k=0.85 | Task 6/10 | ~70% |

**无法在 cuda:2 部署新实验 — GPU 2 正在运行 `eval_pi05_attention_k05_long_seed42_v3`，进度约 4%（Task 0, ep 20/50），预计还需数小时。**

选项：
1. **等 GPU 3 跑完**（进度最快，约 70%，可能 1-2 小时后释放），然后在 cuda:3 部署
2. **杀掉 cuda:2 上的实验**（仅 4% 进度，损失不大），立即部署新实验
3. **等待不操作**，稍后再部署

需要你决定怎么处理。

---
