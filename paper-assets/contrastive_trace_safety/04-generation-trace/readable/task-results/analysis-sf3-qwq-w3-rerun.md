# analysis sf3 qwq w3 rerun

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_sf3_qwq_w3_rerun_20260519T145600_result.json`
- **Structured JSON:** [`03296d6c33018a6481bd.json`](../../sessions/03/03296d6c33018a6481bd.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

QwQ-32B W=3 重跑完成。结果：

| Method | HS BA | Txt BA | Gap | p |
|---|---|---|---|---|
| linear | 0.6148 | 0.6006 | **1.4pp** | 0.3107 |
| quadratic | 0.6272 | 0.5901 | **3.7pp** | 0.0680 |

注意：3.7pp 出现在 **quadratic** 而非 linear。Linear gap 仅 1.4pp（与之前 W=5 的 0.9pp 方向一致但略大）。如果论文 tab:position_residual 预期 linear gap ≈ 3.7pp，可能需要核实表中对应的是哪行/哪种 residualization。

产出文件：
- `artifacts/sf3_quadratic_residual/qwq_w3_results.json`
- `artifacts/sf3_quadratic_residual/report.txt`（已追加 W=3 section）

---
