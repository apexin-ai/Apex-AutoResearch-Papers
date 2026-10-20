# experiment folio 2x2 master script

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_experiment_folio-2x2-master-script_20260521T234052_result.json`
- **Structured JSON:** [`bf52746d2590e9fcfdfc.json`](../../sessions/bf/bf52746d2590e9fcfdfc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Master 脚本运行正常。

**产出汇总：**
- **Master PID**: 495418（外层 bash），实际 master.sh 是其子进程
- **Log 路径**: `/root/symb_invariant_consensus/results/exp_folio_2x2/master.log`
- **Nohup log**: `/tmp/folio_2x2_master_nohup.log`

**Pipeline 阶段：**
1. **Phase 1**（当前）：等待 Cell A (113/204) + Qwen3 traces (79/204)，每 2 分钟报告进度
2. **Phase 2**：Cell B+C 并行 → Cell D 串行
3. **Phase 3**：调用现有 `compute_folio_2x2_metrics.py`（含 SC/answer-κ/BR/McNemar）

完成时 log 末尾输出 `SENTINEL_FOLIO_2X2_DONE`。

---
