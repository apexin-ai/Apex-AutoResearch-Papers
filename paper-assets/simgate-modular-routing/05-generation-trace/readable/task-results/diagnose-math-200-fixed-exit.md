# diagnose math 200 fixed exit

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_math-200-fixed-exit_20260514T144004_result.json`
- **Structured JSON:** [`12edbd5a9829bd16d12d.json`](../../sessions/12/12edbd5a9829bd16d12d.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果汇总：

**math-200-fixed: FAILED — 在第 56/200 题崩溃**

**崩溃原因**: vLLM 返回 HTTP 400 Bad Request (`localhost:8000/v1/chat/completions`)，发生在 problem 56 的 code interpreter 调用阶段。可能是该题的 prompt 触发了 vLLM 的输入校验错误（如 token 超长或格式异常）。

**部分结果 (55 题)**:
| 指标 | 值 |
|---|---|
| Internal accuracy | 44/55 = **80.0%** |
| CodeInterp accuracy | 41/55 = **74.5%** |
| Code execution rate | 44/55 = 80.0% (11 题 0 code rounds) |
| no-preference | 45 (81.8%) |
| internal-preferred | 7 (12.7%) |
| det-preferred | 3 (5.5%) |
| FILTERED | 11 |
| Sandbox empty output | **0** (auto_print_last_expr 修复生效) |

**后续建议**:
1. 排查 problem 56 触发 400 的具体原因（可能是 context 过长），给 `_generate_api` 加异常重试或跳过逻辑
2. 加 `--resume` 支持，从 offset=105 (50+55) 继续跑剩余 145 题

---
