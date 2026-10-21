# code fix classify h7

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-classify-h7_20260514T102843_result.json`
- **Structured JSON:** [`2a3fcc2499f7290e58f7.json`](../../sessions/2a/2a3fcc2499f7290e58f7.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成，结果已保存。汇总：

| Run | H7 (single prem=concl) | H1 (multi-prem, concl in prem) | H7+H1 | Proved |
|-----|------------------------|-------------------------------|-------|--------|
| **s42** | 13/81 = 16.1% | 42/81 = 51.8% | 55/81 = 67.9% | 81 |
| **s43** | 59/61 = 96.7% | 0/61 = 0.0% | 59/61 = 96.7% | 61 |
| **s44** | 77/89 = 86.5% | 0/89 = 0.0% | 77/89 = 86.5% | 89 |
| **random** | 0/79 = 0.0% | 56/79 = 70.9% | 56/79 = 70.9% | 79 |

**s42 验证**：H7(13) + H1(42) = 55/81 = 67.9% conclusion-in-premise 总量，与之前 `any(premise==conclusion)` 检测的 55 一致。

注意 s42 的 H7 是 13/81=16.1%（略低于预期的 ~15/81=18.5%），差异来自有 2 个 single-premise 样本的 premise 与 conclusion 不完全相等（single_premise=15 但 H7=13）。s43/s44/random 均符合预期。

---
