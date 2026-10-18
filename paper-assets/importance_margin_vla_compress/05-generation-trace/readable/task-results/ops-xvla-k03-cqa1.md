# ops xvla k03 cqa1

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_xvla-k03-cqa1_20260520T143308_result.json`
- **Structured JSON:** [`98f4f662e042d14d740b.json`](../../sessions/98/98f4f662e042d14d740b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

两个实验均已成功启动并在正常运行。

**启动汇总：**

| GPU | 实验 | PID | 状态 |
|-----|------|-----|------|
| GPU 3 | seed43 k=0.3 | 344865 (wrapper) | 运行中，已到 Ep 4/50 Task 0 |
| GPU 1 | seed44 k=0.3 | 346215 (wrapper) | 运行中，已到 Ep 1/50 Task 0 |

日志路径：
- `/tmp/eval_xvla_k03_seed43.log`
- `/tmp/eval_xvla_k03_seed44.log`

参考现有实验（k=0.7 seed44 已运行约 70 分钟在 Ep 进行中），每个实验预估 **1.5-2 小时** 完成（10 tasks × 50 episodes）。GPU 0 和 GPU 2 上的进程未受影响。

---
