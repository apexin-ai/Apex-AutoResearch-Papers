# analysis qwen3 8b traj func s42

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_qwen3-8b-traj-func-s42_20260517T141256_result.json`
- **Structured JSON:** [`7c6d6b6a87d245af12f3.json`](../../sessions/7c/7c6d6b6a87d245af12f3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。总结：

**qwen3-8b-traj-func-s42 → SUCCESS**

| 指标 | 值 |
|------|------|
| test_accuracy | **87.98%** |
| eval_loss | 0.0975 |
| train_loss (final step) | 0.0312 |
| unparseable | 0 |

**对比分析：**
- 4B TRAJ → 8B TRAJ: 86.30% → 87.98% (+1.68pp)，符合预期的 +1-2pp scaling pattern
- 8B formulation 排序: CLS (89.40%) > **TRAJ (87.98%)** > CWM (86.96%)，与 4B 排序一致
- Hypothesis confirmed：TRAJ 在更大模型上展现了与 CLS/CWM 一致的 scaling 行为

Registry 已更新为 DONE/success，memory.md 已追加分析记录。

---
