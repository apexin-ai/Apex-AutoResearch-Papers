# ops cqa1 xvla random k05 object

**Why Token Pruning Crashes Some Robot Policies but Not Others: Vision Connectors and VLA Token Compressibility** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_cqa1-xvla-random-k05-object_20260521T030750_result.json`
- **Structured JSON:** [`be1e033a111a6b63a5cd.json`](../../sessions/be/be1e033a111a6b63a5cd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总如下：

### cqa1 X-VLA Random Pruning Object Eval 状态

| GPU | 实验 | 进度 | 已完成 Task SR |
|-----|------|------|----------------|
| cuda:0 | random k=0.9 (PID 522763) | Task 8/10 进行中 | T0:96%, T1:100%, T2:100%, T3:94%, T4:100%, T5:94%, T6:100%, T7:98% |
| cuda:1 | random k=0.8 (PID 522984) | Task 6/10 进行中 | T0:96%, T1:88%, T2:100%, T3:92%, T4:94%, T5:96% |
| cuda:2 | **random k=0.5 (PID 715930)** | **Task 0/10 刚启动** | Ep 1 SUCCESS |
| cuda:3 | random k=0.85 (PID 522841) | Task 5/10 进行中 | T0:100%, T1:10%, T2:100%, T3:94%, T4:24% |

- **k=0.5 已成功启动**，GPU 2 占用 4540 MiB，正常运行
- k=0.9 和 k=0.8 表现很强（多数 task >90%），预计 1-2 小时完成
- k=0.85 有几个 task SR 偏低（T1:10%, T4:24%），random pruning 方差较大
- 日志路径注意：其他 3 个在 `/root/runs/importance_margin_vla_compress/`，k=0.5 在 `/root/autodl-tmp/importance_margin_vla_compress/logs/`

---
