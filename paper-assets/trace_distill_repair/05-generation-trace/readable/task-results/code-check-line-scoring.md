# code check line scoring

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_check_line_scoring_20260514T190503_result.json`
- **Structured JSON:** [`866d47f62100b7121f9b.json`](../../sessions/86/866d47f62100b7121f9b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Line Scoring 进度汇报

**状态：运行中**（2 个进程 PID 60414/60524）

### 进度
- **总实例数**：36 个（排除了 fastapi_2/3/5/1）
- **已完成**：12/36（截至 03:01，完成到 luigi_1）
- **当前正在处理**：13/36 — `luigi_2`（200 segments，截断自 664）
- **进度**：33%

### 时间
- 启动时间：02:28
- 已运行：~36 分钟
- 前 12 个实例耗时 32 分钟，平均 ~2.7 分钟/实例
- 但大实例（luigi 系列，200 segments）需 ~7-8 分钟/个
- **预估剩余**：剩余 23 个实例，预计还需 ~50-70 分钟

### 错误情况
- **502 Bad Gateway**：7 次（自动重试，不影响结果）
- **WARNING**（API 解析失败）：3 次，`'NoneType' object has no attribute 'strip'`（segment 385-389, 390-394, 730-734）
- 成功 API 调用：1129 次
- **错误率很低**（<1%），502 均已自动重试成功

### 输出
- `phase2_line_scores.json` 尚未生成（应在全部完成后写入）
- `pipeline_output/line_scores/` 目录不存在（结果可能汇总写入单文件）

### 备注
- 有多个大实例被截断到 max-segments=200（luigi_10/14/1/2 原始均 300-666 segments）
- 3 个 WARNING 是 API 返回空内容导致解析失败，不影响整体流程

---
