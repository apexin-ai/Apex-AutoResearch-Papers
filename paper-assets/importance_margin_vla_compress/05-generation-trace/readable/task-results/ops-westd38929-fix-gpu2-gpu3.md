# ops westd38929 fix gpu2 gpu3

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_westd38929-fix-gpu2-gpu3_20260521T072942_result.json`
- **Structured JSON:** [`e9bfb5e7dea21b67a47e.json`](../../sessions/e9/e9bfb5e7dea21b67a47e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。4 GPU 全部在运行：

| GPU | Exp ID | Mode | PID |
|-----|--------|------|-----|
| 0 | (existing) L2norm k=0.7 | l2norm_prune | 1945 |
| 1 | (existing) random k=0.3 | random_prune | 2478 |
| 2 | `eval_openvla_random_k07_object_seed42_v2` | random_prune k=0.7 | 3110 |
| 3 | `eval_openvla_l2norm_k05_object_seed42_v3` | l2norm_prune k=0.5 | 3825 |

GPU2/GPU3 实验已经有人启动并正常运行（Task 1/10），无需重新提交。Registry 已注册为 RUNNING。注意 GPU3 因原 v2 exp_id 已 DONE，用了 v3 后缀。

---
