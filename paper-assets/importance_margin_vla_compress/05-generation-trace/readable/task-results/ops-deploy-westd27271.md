# ops deploy westd27271

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_deploy_westd27271_20260522T041520_result.json`
- **Structured JSON:** [`8a1fd7f623d2469192ac.json`](../../sessions/8a/8a1fd7f623d2469192ac.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验都已进入评估阶段，运行正常：

| 实验 | GPU | PID | 状态 | 当前进度 |
|------|-----|-----|------|---------|
| eval_pi05_random_k095_spatial_seed43 | cuda:0 | 9465 | 运行中 | T0 ep=20, 100% |
| eval_pi05_l2norm_k085_spatial_seed43 | cuda:1 | 9608 | 运行中 | T0 ep=20, 100% |

- Random k=0.95: keep 243/256 tokens/image (729 total)
- L2norm k=0.85: keep 217/256 tokens/image (651 total)

部署成功，无错误。预计 3-4 小时完成全部 10 tasks × 50 episodes。

---
