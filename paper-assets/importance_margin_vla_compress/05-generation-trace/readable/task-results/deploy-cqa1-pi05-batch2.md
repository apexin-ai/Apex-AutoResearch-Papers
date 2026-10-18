# deploy cqa1 pi05 batch2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-pi05-batch2_20260521T220116_result.json`
- **Structured JSON:** [`ff5a1f75d27c0e731abe.json`](../../sessions/ff/ff5a1f75d27c0e731abe.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 全部在工作：

| GPU | 显存 | 实验 |
|-----|------|------|
| 0 | 10262 MiB | **实验 A**: random k=0.85 seed43 — 已在跑 episodes |
| 1 | 9507 MiB | **实验 B**: l2norm k=0.5 seed43 — 模型已加载，开始 eval |
| 2 | 10262 MiB | L2norm k=0.85 seed42（既有） |
| 3 | 10134 MiB | random k=0.3 seed43（既有） |

实验 A 已注册为 RUNNING (`eval_pi05_random_k085_object_seed43`)。

**注意**: `eval_pi05_l2norm_k05_object_seed43` 在 registry 中已有完成记录（westd-41074 跑的，SR=33.6%）。当前在 cqa1 重新跑了一份——如果不需要可以 kill PID 720036 释放 GPU1。

---
