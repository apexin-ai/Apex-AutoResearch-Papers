# ops cqa1 check and deploy

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-check-and-deploy_20260527T135138_result.json`
- **Structured JSON:** [`93980125b7c2ab2151a2.json`](../../sessions/93/93980125b7c2ab2151a2.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All 4 GPUs occupied, no deployment possible.

**GPU 状态：**

| GPU | 显存 | 利用率 | 实验 |
|-----|------|--------|------|
| 0 | 10326/24564 MiB | 11% | eval_pi05_attn_k075_long_seed42_strict_cqa1 (PID 300488, alive) |
| 1 | 21141/24564 MiB | 98% | eval_pi05_random_k09_long_seed43_strict_cqa1 (PID 330510, alive) |
| 2 | 10633/24564 MiB | 59% | eval_pi05_l2norm_k07_long_seed42_strict |
| 3 | 10261/24564 MiB | 20% | eval_pi05_l2norm_k09_long_seed42_strict_cqa1 |

**Random k=0.9 seed43 (PID 330510)：**
- 进程活着，正在 GPU1 上跑，98% 利用率
- 当前进度：刚完成 Task 0 (SR=10.0%, 5/50)，耗时 35.7min
- 启动时间 ~21:10 UTC，Long suite 10 tasks 预计还需 ~5-6h
- Registry 标记为 failed 但进程实际在跑，westd-41074 上还有备份实验

**结论：GPU1 被占用，无法部署 `eval_pi05_random_k075_long_seed43_strict_cqa1`。** 需要等 Random k=0.9 seed43 跑完（预计 ~03:00 UTC 5/28）或找其他服务器部署。

---
