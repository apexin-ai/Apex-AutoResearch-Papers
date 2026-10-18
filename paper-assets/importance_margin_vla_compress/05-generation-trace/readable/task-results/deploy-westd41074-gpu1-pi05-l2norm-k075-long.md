# deploy westd41074 gpu1 pi05 l2norm k075 long

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_westd41074_gpu1_pi05_l2norm_k075_long_20260526T022909_result.json`
- **Structured JSON:** [`af314be4872721cf73f4.json`](../../sessions/af/af314be4872721cf73f4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 完成

### l2norm_k05_object 结果（OpenVLA）
- **Overall SR: 39.2% (196/500)**
- 逐任务：alphabet soup 56%, ketchup 70%, milk 50%, cream cheese 14%, butter 12%
- 保存于：`eval_results/openvla_l2norm_prune_k05_object_seed42.json`

### π0.5 L2norm k=0.75 Long 部署状态
| 项 | 值 |
|---|---|
| 服务器 | westd-41074 GPU1 |
| PID | 319659 |
| tmux session | `eval_pi05_l2norm_k075_long_v3` |
| Registry | `eval_pi05_l2norm_k075_long_seed42_v3` — DEPLOYED |
| 日志 | `~/runs/importance_margin_vla_compress/eval_pi05_l2norm_k075_long_seed42_v3.log` |
| 当前状态 | 模型加载中（π0.5 加载 ~10 min），GPU1 尚未占用显存 |

### nvidia-smi
```
GPU0: 16188 MiB (占用)
GPU1:     3 MiB (模型加载中，即将占用)
GPU2: 15980 MiB (占用)
GPU3: 10576 MiB (占用)
```

进程健康运行，模型加载完成后 GPU1 显存会跳到 ~15GB 并开始 eval。

---
