# eval westd41074 gpu0 fill

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_westd41074-gpu0-fill_20260520T181831_result.json`
- **Structured JSON:** [`8b408a3ad6e868197457.json`](../../sessions/8b/8b408a3ad6e868197457.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已确认启动成功。

**GPU 0** — OpenVLA random prune **k=0.95 seed43**, PID=564806
- 256 → 243 vision tokens（仅剪 5%）
- 已开始 Task 1/10，正常运行中
- GPU 0 占用 15980 MiB, 73% util

**GPU 1** — OpenVLA random prune **k=0.5 seed43**（进行中）
- Task 1/10, Ep 30/50, 目前 0% SR
- 预估总时长 ~4.5h（参考 k=0.7 跑了 269 min）

**已有结果**:
- k=0.7 seed43: **SR=52.6%**（263/500）

---
