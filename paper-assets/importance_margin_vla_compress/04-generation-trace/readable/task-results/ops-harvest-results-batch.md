# ops harvest results batch

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_harvest-results-batch_20260521T234728_result.json`
- **Structured JSON:** [`ae9329969f55975fe733.json`](../../sessions/ae/ae9329969f55975fe733.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。汇报：

```
1. k=0.85v2 (Object): SR=5.0% (25/500) [DONE, negative] — cliff 在 0.7-0.85 之间（k=0.7→75.5%, k=0.85→5.0%）
2. L2norm k=0.7 Spatial: SR=67.0% (335/500) [DONE, success] — V-shape recovery 跨 suite 确认（k=0.5→55.6%, k=0.7→67.0%）
3. random k=0.9 Spatial 部署: 成功, PID=9135, GPU1, tmux=eval_pi05_random_k09_spatial_seed42
4. westd-38929 GPU 状态: GPU0 空闲, GPU1 running (random k=0.9 spatial), GPU2 running (l2norm k=0.925 object), GPU3 空闲 — 2 GPU 可用
```

注：两个已完成实验此前被监控系统误判为 failed（sentinel 缺失），实际正常完成。conclusion 已从 "failed" 更正为 negative/success。

---
