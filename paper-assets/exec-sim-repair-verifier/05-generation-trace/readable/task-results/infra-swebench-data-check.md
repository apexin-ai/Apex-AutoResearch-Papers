# infra swebench data check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_swebench-data-check_20260512T093516_result.json`
- **Structured JSON:** [`e2c79ffbc8fd25118278.json`](../../sessions/e2/e2c79ffbc8fd25118278.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**进程已正常完成。**

## 状态报告

| 项目 | 状态 |
|------|------|
| 进程 PID 2312582 | **已退出（正常完成）** |
| 日志最后写入时间 | 2026-05-12 01:37:58 (约 1 小时前) |
| 报错 | 0 个 ERROR |

## 数据产出

**主文件**: `data/swebench_full/swebench_pilot_data.jsonl`
- **89,867 条记录**，541 MB
- 250 个 SWE-bench Verified instance，5 种 patch 类型（gold + 4 种 mutation）

## 数据分布

| 维度 | 分布 |
|------|------|
| 标签 | label=0: 15,479 / label=1: 74,388 |
| 测试类型 | P2P: 71,894 / F2P: 17,973 (20%, 经过 upsampling) |
| Mutation | gold: 39,076 / operator_swap: 23,114 / off_by_one: 11,112 / boundary_removal: 8,732 / return_value: 7,833 |
| 顶级 Repo | django: 32,121 / xarray: 25,573 / matplotlib: 16,139 |

## 注意事项

- 773 个 SKIP（"not completed"），主要是部分 mutation 的 evaluation 未完成，但这些已被跳过并不影响最终数据集
- 日志末尾有 "Warning: Missing predictions for 189 instance IDs"——部分 instance 的某些 mutation 类型没有产出 prediction，被跳过
- 数据已 ready，可以开始 repo-level 训练

---
