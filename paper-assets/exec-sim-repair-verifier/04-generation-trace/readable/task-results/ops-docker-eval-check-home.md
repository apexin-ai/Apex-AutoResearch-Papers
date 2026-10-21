# ops docker eval check home

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_docker-eval-check-home_20260517T083055_result.json`
- **Structured JSON:** [`7adf3445fa89ed23e4f3.json`](../../sessions/7a/7adf3445fa89ed23e4f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Docker eval **已完成**，进程已退出。

## 结果汇总

| Condition | Instances | Samples | pass@1(any) | Per-sample resolve |
|-----------|-----------|---------|-------------|--------------------|
| A1 | 44 | 295 | **52.3%** | 44.7% |
| A2 | 44 | 295 | 43.2% | 35.9% |
| B | 44 | 295 | 36.4% | 31.2% |
| C | 44 | 295 | 38.6% | 33.6% |
| D | 44 | 295 | 40.9% | 34.2% |
| **Total** | **220** | **1475** | **42.3%** | **35.9%** |

每个 instance 有 ~7 个 samples（对应 K 值），5 conditions × 44 instances = 220 组。

## 问题

- **569/1475 (38.6%) 有 errors**，主要是 "Report not found"，即 swebench harness 报告文件缺失。其中一个反复出现的是 `matplotlib__matplotlib-25287` 的 "Patch Apply Failed: Only garbage was found in the patch input"（日志末尾可见）。
- A1 (最多信息的条件) pass@1 最高 (52.3%)，符合预期；B/C/D 之间差异不大 (36-41%)。

---
