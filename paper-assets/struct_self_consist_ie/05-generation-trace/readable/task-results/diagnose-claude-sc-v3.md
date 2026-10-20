# diagnose claude sc v3

**When Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_claude_sc_v3_20260521T085545_result.json`
- **Structured JSON:** [`43f666cff29c3074bd18.json`](../../sessions/43/43f666cff29c3074bd18.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 诊断结论

**进程没有死亡，实验已正常完成。** 无需重启，无需 10min 验证。

| 项目 | 结果 |
|------|------|
| Unique instances | **200/200** (全部完成) |
| 进程状态 | 无运行中进程（正常退出） |
| 磁盘 | 98G 可用，正常 |
| OOM/Crash | 无（日志正常结束） |

### 最终指标（已保存到 `output/frontier_sc_claude_sonnet4/`）

| 指标 | 值 |
|------|-----|
| greedy_f1 | 0.6068 |
| mv_f1 | **0.6226** (+0.0158) |
| oracle_f1 | 0.6544 |
| degeneracy_rate | 0.7400 (148/200) |
| selection_gap | 0.0318 |
| API calls | 1600 |
| Parse failures | 103 |
| 耗时 | 6118s (~102min) |

输出文件：`checkpoint.jsonl` (128KB), `results.jsonl` (67KB), `summary.json` (1KB)，均在 May 21 16:09 写入。

---
