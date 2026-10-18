# ops xvla batch2 results

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-batch2-results_20260520T110723_result.json`
- **Structured JSON:** [`073db19e660537a9947c.json`](../../sessions/07/073db19e660537a9947c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Batch 1 (k=1.0/0.95/0.9/0.7) 完成，Batch 2 **全部崩溃**。

## 汇总

```
k=1.0:  SR=99.2% [完成] tokens=50→50  per_task: [98, 100, 98, 100, 100, 96, 100, 100, 100, 100]
k=0.95: SR=99.0% [完成] tokens=50→47  per_task: [98, 100, 100, 96, 100, 96, 100, 100, 100, 100]
k=0.9:  SR=97.6% [完成] tokens=50→45  per_task: [96, 98, 100, 92, 100, 96, 100, 98, 96, 100]
k=0.7:  SR=56.2% [完成] tokens=50→35  per_task: [94, 2, 100, 80, 28, 92, 12, 66, 0, 88]
k=0.5:  [崩溃] tokens=50→25
k=0.3:  [崩溃] tokens=50→15
k=0.2:  [崩溃] tokens=50→10
k=0.1:  [崩溃] tokens=50→5
```

**Batch 2 全部失败原因相同**：libero 环境初始化时 MSH 文件为空：
```
ValueError: MSH file '.../alphabet_soup/visual/textured_vis.msh' is empty
```

4 个 k 值都在 Task 0 创建环境时就崩了，没有产生任何 eval 结果。sentinel 文件显示 `SWEEP_DONE`（sweep 脚本认为已结束，但实际是异常退出）。

GPU 上仍有 4 个进程（每个 ~4.8GB），可能是其他任务或残留进程。`textured_vis.msh` 文件损坏需要修复后重跑 Batch 2。

---
