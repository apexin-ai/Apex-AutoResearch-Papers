# diag westd25068 integrity check

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diag_westd25068-integrity-check_20260518T234707_result.json`
- **Structured JSON:** [`8a3ec5877db1077489eb.json`](../../sessions/8a/8a3ec5877db1077489eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**westd-25068 所有实验完好无损。** 汇总：

| 实验 | GPU | 状态 | 详情 |
|------|-----|------|------|
| **exp-028b** | cuda:3 (97%, 88GB) | **运行中** | folio 82/204，ETA ~288 min |
| **exp-051** | cuda:0 (96%, 88GB) | **运行中** | folio 14/204 (K sensitivity)，ETA ~65 min |
| **exp-034** | cuda:1 (98%, 88GB) | **运行中** | HTTP 200 请求持续活跃 |
| **exp-046** | cuda:2 (96%, 88GB) | **运行中** | Mistral PW600，HTTP 200 请求持续活跃（tmux pane 为空但日志正常写入） |
| exp-033 | — | **已完成** | SICA=59.3%, SC=54.4% |
| exp-035 | — | **已完成** | SICA=76.5%, SC=77.0% |

4 张 GPU 全部满载运行，4 个活跃实验进程正常，无任何受损迹象。exp-028b 安全。

---
