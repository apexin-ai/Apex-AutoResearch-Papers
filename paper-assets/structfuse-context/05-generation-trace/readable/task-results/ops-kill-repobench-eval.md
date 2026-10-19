# ops kill repobench eval

**StructFuse: Structure-Grounded Hard Negative Mining for Contrastive Code Context Retrieval** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_kill_repobench_eval_20260516T081309_result.json`
- **Structured JSON:** [`671981a743dccceb333e.json`](../../sessions/67/671981a743dccceb333e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成，汇总如下：

| 项目 | 状态 |
|------|------|
| **RepoBench 进程** | 全部已 kill（PID 159855/158952/158947/159860 均 DEAD） |
| **cuda:1 内存** | 从 ~94 GiB 降至 **69,936 MiB (~68 GiB)**，释放约 **24 GiB** |
| **D062 eval** | 正常运行中（PID 158647/158653，已运行 ~21 分钟，在 cuda:0 上跑 selection set） |
| **RepoBench 已完成结果** | **无**（`repobench_*.json` 不存在，说明 repobench eval 在输出结果前被 kill，后续重启需从头跑） |

cuda:1 已释放约 24 GiB，D062 eval 不受影响。RepoBench 没有产出任何 checkpoint，后续重启需要全部重跑。

---
