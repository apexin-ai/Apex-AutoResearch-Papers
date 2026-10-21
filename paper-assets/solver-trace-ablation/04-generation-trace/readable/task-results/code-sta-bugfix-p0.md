# code sta bugfix p0

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_sta-bugfix-p0_20260513T174744_result.json`
- **Structured JSON:** [`05950aee86abb0c0544b.json`](../../sessions/05/05950aee86abb0c0544b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部验证通过。

**修复结果：**

| Bug | 文件 | 改动 |
|-----|------|------|
| #1 | `src/sta/ablation.py` | `"True"` → `"$T"`，`"False"` → `"$F"`（3 处） |
| #2 | `src/solvers/prover9.py` | 新增 `_normalize_fol()` 方法，`prove()` 和 `check_consistency()` 入口调用 |
| #2.5 | `src/sta/isr.py` | 过滤条件 `results[0].solver_result.success` → `results[0].original_proved` |

---
