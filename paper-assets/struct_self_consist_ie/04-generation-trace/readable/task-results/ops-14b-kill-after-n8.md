# ops 14b kill after n8

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_14b_kill_after_n8_20260520T183707_result.json`
- **Structured JSON:** [`71e81bfaf6f959e1f664.json`](../../sessions/71/71e81bfaf6f959e1f664.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

监控脚本已部署并运行。

**汇总：**

| 项目 | 状态 |
|------|------|
| 当前进度 | N=2 推理中，84% (63352/75296) |
| 调度脚本 PID | 200995 (`bash run_14b_fewnerd.sh`) |
| 监控脚本 PID | 224789 (`kill_after_n8.sh`) |
| 触发条件 | 日志出现 `=== FewNERD N=8 finished` 后 kill 整个进程树 |
| 每 15 秒检查一次 | 日志写到 `/tmp/kill_after_n8.log` |

**时间估算：**
- N=1 耗时 ~2.5h，N=2 已跑 ~1.6h 剩 ~16%（约 20min）
- N=4 约 5h，N=8 约 10h
- 预计 N=8 完成时间：约 5/21 18:00-20:00 CST

---
