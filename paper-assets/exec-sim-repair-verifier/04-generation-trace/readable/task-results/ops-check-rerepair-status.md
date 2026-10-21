# ops check rerepair status

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_check-rerepair-status_20260517T072253_result.json`
- **Structured JSON:** [`6e7ca8d1d7a2cbc898c8.json`](../../sessions/6e/6e7ca8d1d7a2cbc898c8.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Docker eval 已成功启动并在运行中。

## 状态报告

**Generation (已完成)**：1475/1475 records，5 conditions 全部完成
- 完成时间：2026-05-17 00:04:48
- A1: sim=0.937, B-o-K=0.946, valid=100%
- A2: sim=0.803, B-o-K=0.817, valid=87%
- B: sim=0.723, B-o-K=0.758, valid=81%
- C: sim=0.731, B-o-K=0.776, valid=82%
- D: sim=0.730, B-o-K=0.804, valid=81%

**Docker Eval (运行中)**：PID 3610714
- 388 unique (instance_id, diff) pairs → 42 batches
- 当前：Batch 1/42 开始运行
- 修复：`extracted_diff` → `model_patch` 字段映射
- 环境：`verl_new` (Python 3.10, datasets + swebench + docker)

**注意**：第一个 instance 出现 error，需要后续检查是否为普遍问题。建议 10-15 分钟后复查 log 确认进展正常。

---
