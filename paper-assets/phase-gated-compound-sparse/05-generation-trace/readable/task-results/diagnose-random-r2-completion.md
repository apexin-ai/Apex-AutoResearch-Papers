# diagnose random r2 completion

**Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_diagnose_random-r2-completion_20260514T010049_result.json`
- **Structured JSON:** [`c2f10f6beb86ad2fb414.json`](../../sessions/c2/c2f10f6beb86ad2fb414.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。

## 进程状态
已退出（PID 32187、32192 均不存在）

## 输出文件
`profiling_results.json` 存在，2.7MB，包含 50 个 problem，JSON 完整（正常闭合）

## 关键指标（Information Impact, random masking baseline）

| Phase | s=0.1 | s=0.15 | s=0.2 | s=0.25 | s=0.3 |
|-------|-------|--------|-------|--------|-------|
| high_sparsity (25862 tok, 511 seg) | +0.061 | +2.361 | +0.818 | +1.655 | +9.548 |
| low_sparsity (32349 tok, 454 seg) | +0.072 | +1.147 | +0.792 | +2.452 | +17.371 |
| mid_sparsity (27996 tok, 391 seg) | +0.097 | +1.969 | +0.643 | +19.244 | +5.858 |

## 结论
**成功完成**，50/50 problems 处理完毕。Verdict: **FAIL**（random masking 在多个 sparsity level 下 II 值显著 >0，说明 random masking 对输出分布有实质性影响，符合预期——random baseline 应表现差）。Registry 已标记 DONE/success。

---
