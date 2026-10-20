# analysis experiment progress check

**When Does Detect-and-Reweight Work for Synthetic Contamination?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_experiment-progress-check_20260518T221612_result.json`
- **Structured JSON:** [`b9af82bcad5df31b8cba.json`](../../sessions/b9/b9af82bcad5df31b8cba.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总写入 `artifacts/experiment_progress_snapshot.md`。

关键发现：
- **即将完成 (~43-70 min)**：gpt2_uniform_seed42 (80%)、detect_remove_q02_seed42 (69%)、gpt2_adaptive_seed42 (72%)、detect_remove_q08_seed42 (67%)
- **刚启动 (~3.5h 剩余)**：detect_remove_q03_seed123 和 q03_seed456 (均 6%)
- **中途 (~2.7h 剩余)**：adaptive_1_7b_seed123 (46%)
- **注意**：adaptive_1_7b_seed123 的 progress bar 显示总步数 6103（而非预期的 3125），需确认配置是否正确
- **westd-30476 cuda:2 空闲**，可用于新实验

---
