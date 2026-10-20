# ops oracle label expansion

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ops_oracle-label-expansion_20260517T043408_result.json`
- **Structured JSON:** [`fa07402ac42e27f9a97e.json`](../../sessions/fa/fa07402ac42e27f9a97e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。所有 mutation patches 的 per-test evaluation 已经在之前的 `pilot_mutation_*` runs 中跑完，报告都在 `logs/run_evaluation/` 中。

**产出总结：**

| 文件 | 说明 |
|------|------|
| `expand_oracle_labels.py` | 解析脚本 |
| `data/swebench_full/swebench_test_expanded.jsonl` | 新增 58 instances 的 per-test labels (34,529 entries) |
| `data/swebench_full/swebench_test_merged.jsonl` | 合并后完整数据：83 instances, 44,313 entries |
| `data/swebench_full/oracle_per_instance_summary.jsonl` | 按 instance×mutation 汇总的 96 条记录 |
| `data/swebench_full/oracle_expansion_summary.json` | 统计 metadata |

**关键数字：**
- 原始：25 instances, 9,784 per-test entries
- 新增：58 instances (F2P≥2), 34,529 per-test entries
- 合计：**83 instances**, 44,313 entries
- 不需要重跑 harness（报告已存在），解析耗时 ~3s

---
