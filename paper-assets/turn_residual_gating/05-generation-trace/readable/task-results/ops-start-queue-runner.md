# ops start queue runner

**Exposure Bias Collapses Auxiliary Attention Losses in Multi-Turn Dialogue** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_start_queue_runner_20260522T231640_result.json`
- **Structured JSON:** [`b9e4e85f0561a5c02c20.json`](../../sessions/b9/b9e4e85f0561a5c02c20.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三项验证全 PASS：

| 检查项 | 状态 |
|--------|------|
| GPU 占用 | PID 50737, 30 MiB（模型加载中） |
| tmux 存活 | `queue_runner` session 运行中 |
| 日志 | [2/8] AR N=50 TG s42 已启动，正在加载模型权重 |

**当前执行项**：[2/8] AR N=50 existing s42 checkpoints（TG/UG/PCGrad/LO 四个 checkpoint 的 AR eval）

**剩余队列**：
- [2/8] AR N=50 existing s42 — eval only，~1-2h
- [3/8] SS s123 train+eval — ~6-7h
- [4/8] SS s456 train+eval — ~6-7h
- [5/8] Base s123 train+eval — ~5-6h
- [6/8] Base s456 train+eval — ~5-6h
- [7/8] TG s123 train+eval — ~6-7h
- [8/8] TG s456 train+eval — ~6-7h

**预估总耗时**：~36-42h，在 53h DDL 内可完成。

---
