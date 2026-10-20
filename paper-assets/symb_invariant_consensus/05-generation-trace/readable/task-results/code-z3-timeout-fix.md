# code z3 timeout fix

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_z3_timeout_fix_20260515T220336_result.json`
- **Structured JSON:** [`8021a069d5fe72e8fdd9.json`](../../sessions/80/8021a069d5fe72e8fdd9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

正常求解和超时机制都验证通过。

**修改总结：**

| 项目 | 内容 |
|------|------|
| **文件** | `/root/symb_invariant_consensus/sica/z3_maxsat.py` |
| **函数** | `MaxSATSolver.solve()` |
| **实现** | `threading.Timer` + `z3.main_ctx().interrupt()` — Z3 原生中断机制，能打断 C 层计算（`signal.SIGALRM` 不行） |
| **参数** | 新增 `hard_timeout_s: int = 60`，默认 60 秒 |
| **超时行为** | 返回 `satisfied=[], excluded=all`，记 warning log，实验继续下一题 |
| **验证** | 非线性问题 435 约束，3s 超时精确触发；正常问题 1ms 正确求解 |

---
