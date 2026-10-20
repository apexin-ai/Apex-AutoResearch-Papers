# ops fetch tost v2 artifact

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_fetch-tost-v2-artifact_20260519T094902_result.json`
- **Structured JSON:** [`fd984ad5e5133b1ea888.json`](../../sessions/fd/fd984ad5e5133b1ea888.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

最终状态：

| 文件 | 状态 |
|---|---|
| `tost_margin_sweep_v2_results.json` | **新增** — v2 正确数据，mean_diff = -0.4505pp，5 seeds，clustered bootstrap |
| `tost_sensitivity.json` | **保留** — CLS-CWM 数据（Qwen 1.24pp + DeepSeek 0.025pp），标注正确 |
| `tost_sensitivity_full.json` | **已删除** — mean_diff=1.24pp，CLS-CWM 错标为 CLS-TRAJ |
| `tost_sensitivity_cls_traj.json` | **已删除** — +1.89pp 无效 3-seed 数据 |
| `tost_multi_margin.csv` | **已删除** — 旧版 4-pair 数据，被 v2 取代 |

---
