# deploy s44 w27 l2norm random

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_s44_w27_l2norm_random_20260528T004236_result.json`
- **Structured JSON:** [`8c1e4e3a7fc51fd520c3.json`](../../sessions/8c/8c1e4e3a7fc51fd520c3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

GPU 0 和 GPU 1 均被占用：

| GPU | PID | 实验 | 已运行 |
|-----|-----|------|--------|
| 0 | 346959 | l2norm k=0.75 s45 | 33 min |
| 1 | 347032 | random k=0.85 s45 | 33 min |

两个 GPU 都在跑 s45 实验，还需约 2.5h 完成。π0.5 Long suite 约 3h，当前实验预计约 3h 后结束。

s44 实验需要等当前 s45 跑完后再部署。是否需要我设置一个定时检查，等 GPU 空闲后自动部署？

---
