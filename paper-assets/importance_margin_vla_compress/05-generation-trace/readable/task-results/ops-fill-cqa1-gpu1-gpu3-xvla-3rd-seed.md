# ops fill cqa1 gpu1 gpu3 xvla 3rd seed

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fill-cqa1-gpu1-gpu3-xvla-3rd-seed_20260521T113305_result.json`
- **Structured JSON:** [`41719c324ab2b8b79d6e.json`](../../sessions/41/41719c324ab2b8b79d6e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

4 个 GPU 都有进程在跑，GPU1 (PID 267697, 4521 MiB) 和 GPU3 (PID 269294, 4521 MiB) 已成功占用显存。

部署完成。

| 实验 | GPU | PID | 状态 |
|------|-----|-----|------|
| `eval_xvla_random_k03_object_seed44` (random k=0.3 seed44) | GPU1 | 267697 | RUNNING，已开始 episode 评估 |
| `eval_xvla_l2norm_k07_object_seed44` (l2_norm k=0.7 seed44) | GPU3 | 269294 | RUNNING，已开始 episode 评估 |

注：脚本实际路径在 `/root/autodl-tmp/importance_margin_vla_compress/eval_xvla_pruning_libero.py`（非任务描述中的 X-VLA-Libero 目录）；服务器用 conda 环境，`python` 在 `/root/miniconda3/bin/python`。

---
