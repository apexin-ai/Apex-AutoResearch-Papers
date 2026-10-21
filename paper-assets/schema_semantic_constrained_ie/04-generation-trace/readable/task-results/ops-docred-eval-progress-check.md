# ops docred eval progress check

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_docred_eval_progress_check_20260515T230301_result.json`
- **Structured JSON:** [`62537781966b50429057.json`](../../sessions/62/62537781966b50429057.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## DocRED Unconstrained Eval 进度

### 1. Llama (PID 303525) — cuda:0
| 指标 | 值 |
|------|-----|
| 状态 | **运行中** |
| 运行时间 | 3h05m |
| 进度 | **734 / 998** (73.5%) — 基于输出文件行数 |
| 速率 | ~15.1 sec/sample |
| 预估剩余 | **~66 min (~1h06m)** |
| 异常 | 无（日志中 1 个 grep 命中是误报，"Terror" 包含子串 "error"） |

### 2. Qwen (PID 304006) — cuda:1
| 指标 | 值 |
|------|-----|
| 状态 | **运行中** |
| 运行时间 | 2h59m |
| 进度（日志）| **[487/998]** (48.8%) — 日志最新条目 |
| 进度（输出）| 522 行 — 可能包含之前运行的残留数据 |
| 速率 | ~17-22 sec/sample（近期样本 7-32 秒不等） |
| 预估剩余 | **~3h00m** (按 ~22 sec/sample × 511 remaining) |
| 异常 | 无（同样误报） |

### 注意
- Qwen 输出文件行数 (522) > 日志进度 (487)，可能是之前运行的文件未清理、当前 append 导致。以日志 [487/998] 为准。
- Llama 日志全是 `pad_token_id` warning，进度行被淹没，只能依赖输出文件计数。
- 两个日志中的 tokenizer regex warning 是已知问题，不影响推理。

---
