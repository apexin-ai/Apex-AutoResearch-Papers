# infra swebench progress check

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_swebench-progress-check_20260512T050730_result.json`
- **Structured JSON:** [`cc82242009cb235f80cc.json`](../../sessions/cc/cc82242009cb235f80cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## SWE-bench 全量数据构建进度

| 项目 | 状态 |
|------|------|
| **进程** | Running (PID 2312582, 已运行 44 分钟) |
| **当前阶段** | `pilot_gold` 评估 |
| **评估进度** | 96/240 (40%), ✓94 ✖2 error=0 |
| **速度** | ~24.3s/it |
| **本阶段剩余** | ~58 分钟 |

### 已生成的 predictions 文件

| 文件 | 行数 |
|------|------|
| predictions_gold.jsonl | 250 |
| predictions_mutation_operator_swap.jsonl | 138 |
| predictions_mutation_boundary_removal.jsonl | 127 |
| predictions_mutation_return_value.jsonl | 89 |
| predictions_mutation_off_by_one.jsonl | 61 |
| **总计** | **665** |

### 要点

- Predictions 生成已完成（5 个文件共 665 条），当前在执行评估阶段
- `pilot_gold` 评估完成后还需评估 4 个 mutation 类型（共 415 条），预计还需 **2-3 小时**
- 有大量 "WARNING: No Docker image found" 但不影响运行（fallback 到其他执行方式）
- 2 个实例评估失败（✖=2），0 个 error，整体健康

---
