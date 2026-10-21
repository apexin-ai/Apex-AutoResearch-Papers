# ops cqa1 fill cuda0 cuda1 v2

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-fill-cuda0-cuda1-v2_20260521T072639_result.json`
- **Structured JSON:** [`848663b06701db52e07d.json`](../../sessions/84/848663b06701db52e07d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已启动并注册完毕。

| GPU | exp_id | 配置 | 状态 |
|-----|--------|------|------|
| cuda:0 | `eval_xvla_random_k07_object_seed43_v2` | random k=0.7 seed43 | RUNNING ✓ |
| cuda:1 | `eval_xvla_l2norm_k05_object_seed42` | l2_norm k=0.5 seed42 | RUNNING ✓ |
| cuda:2 | (existing) L2norm k=0.7 seed42 | — |
| cuda:3 | (existing) random k=0.5 seed43 | — |

--mode 参数已从日志确认：实验 1 `mode=random`，实验 2 `mode=l2_norm`。4 卡全部在跑。

---
