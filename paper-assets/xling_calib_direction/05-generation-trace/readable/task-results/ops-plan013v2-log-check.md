# ops plan013v2 log check

**Shifting the Cross-Lingual Calibration Pareto Frontier: Probe-Based Calibration Transfer via CaCLR** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_plan013v2-log-check_20260521T081658_result.json`
- **Structured JSON:** [`b37fb6e6d8ef3ecec50a.json`](../../sessions/b3/b37fb6e6d8ef3ecec50a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 状态报告

### 1. 进程状态：存活
- **PID 47972** 运行中，已运行 **7 小时 21 分钟**
- CPU 103%（单核满载），内存 0.1%
- 命令：`python -u -W ignore code/probing_controls_v2.py`

### 2. 进度：8 层中完成 2 层，正在处理第 3 层（layer 16）

| Layer | CV AUROC | Perm AUROC | Selectivity | 耗时 |
|-------|----------|------------|-------------|------|
| 0 | 0.6304 | 0.5007 | +0.1297 | 12719s (~3.5h) |
| 12 | 0.6389 | 0.4977 | +0.1411 | 9291s (~2.6h) |
| 16 | *进行中* | — | — | — |

日志最后更新时间：`15:03`（约 1.3 小时前），之后无新输出 → layer 16 正在跑，还没结束。

### 3. 报错：无
日志无任何错误信息。

### 4. 预估剩余时间
- 平均每层 ~11005s（~3h），已完成 2/8 层
- 剩余 6 层 × ~3h ≈ **18 小时**
- 预计完成时间：约明天上午 10:00

### 5. 是否卡住：未卡住
进程 CPU 103% 持续运行中，只是每层耗时很长（permutation test 10 次 × 5-fold CV），属于正常计算密集型任务。Layer 16 已跑了约 1.3 小时，预计还需 ~1.7 小时完成该层。

---
