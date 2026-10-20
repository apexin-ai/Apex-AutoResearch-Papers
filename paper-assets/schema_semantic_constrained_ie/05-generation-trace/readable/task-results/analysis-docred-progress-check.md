# analysis docred progress check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_docred_progress_check_20260513T210751_result.json`
- **Structured JSON:** [`dac503d7ac4fe9f5ebdb.json`](../../sessions/da/dac503d7ac4fe9f5ebdb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

DocRED dev set 共 998 篇文档。

## 结果汇总

| 实验 | PID | 状态 | 已完成 | 总计 | 进度 | 运行时间 |
|------|-----|------|--------|------|------|----------|
| **DocRED minimal** | 113153 | 运行中 | 801 | 998 | **80.3%** | 1h37m |
| **DocRED schema-informed** | 116360 | 运行中 | 228 | 998 | **22.8%** | 55m |

**GPU 状态：**
- GPU 0: 88% utilization, 22789/97887 MiB
- GPU 1: 82% utilization, 19545/97887 MiB

两个实验都在正常运行。DocRED minimal 预计还需 ~25-30 分钟完成，schema-informed 预计还需 ~2.5-3 小时。

DocRED minimal 完成后需要跑 violation analysis，目前还未到时机。

---
