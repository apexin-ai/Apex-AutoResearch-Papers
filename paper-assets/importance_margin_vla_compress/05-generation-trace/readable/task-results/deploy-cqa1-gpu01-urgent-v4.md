# deploy cqa1 gpu01 urgent v4

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_deploy_cqa1-gpu01-urgent-v4_20260526T183229_result.json`
- **Structured JSON:** [`cb0d1188e149b9f8e65b.json`](../../sessions/cb/cb0d1188e149b9f8e65b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

部署成功，4 块 GPU 全部在跑。

## 汇报

```
GPU 0 (L2norm k=0.7): PID=617566, GPU Memory=10456MiB, Status=RUNNING
GPU 1 (Attn k=0.7):   PID=617728, GPU Memory=10628MiB, Status=RUNNING
```

nvidia-smi 完整输出（02:36:04 UTC）：
- **GPU 0**: 10475MiB/24564MiB, 8% util, 38°C, P2, PID 617566
- **GPU 1**: 10647MiB/24564MiB, 13% util, 35°C, P2, PID 617728
- GPU 2: 10225MiB (attn k=0.5, PID 582964) — 已有任务继续运行
- GPU 3: 10679MiB (attn k=0.95, PID 546287) — 已有任务继续运行

tmux session: `pi05_l2norm_k07_long` 和 `pi05_attn_k07_long` 均存活。日志写入正常。

---
