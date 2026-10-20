# analysis ty batch rerun 19828

**Characterizing the Detectability Landscape of Iterative Model Collapse** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ty_batch_rerun_19828_20260520T194748_result.json`
- **Structured JSON:** [`b1b5e6c73c398055bd40.json`](../../sessions/b1/b1b5e6c73c398055bd40.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。汇总：

- **代码修复**：`run_5method_analysis_d102.py` line 223，`causing=1,caused=0` → `causing=0,caused=1`
- **批量重跑**：34/34 实验全部成功，0 失败
- **验证**：PermG 和 DiffXcorr 在所有 spot check 中完全不变；TY forward sig 随方向修正变化（符合预期）
- **汇总文件**：`results/ty_batch_rerun_19828_summary.json`

---
