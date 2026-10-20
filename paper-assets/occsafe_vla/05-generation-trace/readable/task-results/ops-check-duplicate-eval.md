# ops check duplicate eval

**Does Auxiliary Spatial Supervision Make Vision-Language-Action Models Safer? A Factorial Analysis** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check_duplicate_eval_20260523T204022_result.json`
- **Structured JSON:** [`4b60041fa2ad2bf5ad51.json`](../../sessions/4b/4b60041fa2ad2bf5ad51.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

无重复进程。当前 evaluate_safelibero 进程列表：

| PID | 任务 | GPU |
|-----|------|-----|
| 464454 | reverse_cutoff_s0_eval | GPU 2 |
| 463150 | cutoff_25k_s0_eval | GPU 3 |

另有两个对应的 bash wrapper 进程（463144、464449），属于正常的 nohup 启动壳，无需处理。

---
