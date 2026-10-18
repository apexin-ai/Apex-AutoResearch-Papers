# ops cqa1 fill 3 gpus director plan

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-fill-3-gpus-director-plan_20260521T095213_result.json`
- **Structured JSON:** [`511993ed5a6e9790657e.json`](../../sessions/51/511993ed5a6e9790657e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。cqa1-33015 四卡满载：

| GPU | 实验 | PID | 显存 | 日志 | 状态 |
|-----|------|-----|------|------|------|
| cuda:0 | X-VLA L2norm k=0.3 seed43 | 944993 | 4521 MiB | `logs/eval_xvla_l2norm_k03_object_seed43.log` | Ep 7/50 运行中 |
| cuda:1 | X-VLA random k=0.3 seed43 | 946702 | 4521 MiB | `logs/eval_xvla_random_k03_object_seed43.log` | Ep 3/50 运行中 |
| cuda:2 | X-VLA L2norm k=0.3 seed42 | 707317 | 4519 MiB | `logs/eval_xvla_l2norm_k03_object_seed42.log` | 已有实验 |
| cuda:3 | X-VLA L2norm k=0.7 seed43 | 947883 | 4046 MiB | `logs/eval_xvla_l2norm_k07_object_seed43.log` | Ep 3/50 运行中 |

3 个实验全部注册为 RUNNING，日志无报错。

---
