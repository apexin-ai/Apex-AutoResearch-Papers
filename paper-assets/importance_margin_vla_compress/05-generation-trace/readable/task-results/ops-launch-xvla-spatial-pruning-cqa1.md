# ops launch xvla spatial pruning cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_launch-xvla-spatial-pruning-cqa1_20260520T231855_result.json`
- **Structured JSON:** [`e27a83c5fd728ac51841.json`](../../sessions/e2/e27a83c5fd728ac51841.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验已启动并注册为 RUNNING。

**汇总：**

| 实验 | tmux session | GPU | 显存占用 | 状态 |
|------|-------------|-----|---------|------|
| X-VLA k=0.9 Spatial | `eval_xvla_spatial_k09` | GPU 1 | ~4601 MiB | RUNNING, Ep 1 SUCCESS |
| X-VLA k=0.5 Spatial | `eval_xvla_spatial_k05` | GPU 2 | ~4597 MiB | RUNNING, Ep 1 SUCCESS |

**日志确认：**
- k=0.9: `Suite: libero_spatial | keep_ratio=0.90 | Vision tokens: 50 total, keeping 45 (90%)`
- k=0.5: `Suite: libero_spatial | keep_ratio=0.50 | Vision tokens: 50 total, keeping 25 (50%)`
- 两个实验 Task 0 Ep 1 均已 SUCCESS（steps=78-79）

日志路径：
- `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_spatial_k09_seed42.log`
- `/root/autodl-tmp/importance_margin_vla_compress/logs/eval_xvla_spatial_k05_seed42.log`

---
