# check line scoring v3 progress

**trace distill repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_line_scoring_v3_progress_20260515T083117_result.json`
- **Structured JSON:** [`8db3f36fdae77c84e9cf.json`](../../sessions/8d/8db3f36fdae77c84e9cf.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## Line Scoring v3 状态报告

**PID 100942: ALIVE** — 已运行 2h53m，RSS 92MB，CPU 0.2%

**进度：已完成全部 38 个实例（原始数据集 33 个 + 5 个 annotated 实例，排除 fastapi_3/fastapi_5）**

| 指标 | 数值 |
|------|------|
| 实例数 | 38/38 |
| 总 segments | 3,922 |
| 已评分 | 3,838 (97.9%) |
| 失败 | 84 (2.1%) |
| keep | 257 (6.6%) |
| drop | 3,581 (91.3%) |
| error | 84 (PARSE_FAILURE: 83, API_FAILURE: 1) |

**日志状态**：最新 API 调用持续到 16:31:41，仍在发请求（约每 5-10s 一次）。偶发 "API returned None content" 警告，大多数 1 次重试后成功。进程可能在对 84 个失败 segment 做重试，或在执行后续处理步骤。

**Keep rate 偏低（6.6%）**，绝大多数 trace segment 被判为 drop，这在 line-level scoring 中可能是合理的——大量 trace 是无关的模块加载/import 行。

---
