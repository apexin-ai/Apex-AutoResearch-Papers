# eval cls8b ckpt3600 mutation breakdown

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_cls8b-ckpt3600-mutation-breakdown_20260516T011419_result.json`
- **Structured JSON:** [`e6046432859a67828bcb.json`](../../sessions/e6/e6046432859a67828bcb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE。结果已完整，无需重新跑 eval。

## CLS 8B s42 resume ckpt-3600 Mutation Breakdown

| Mutation Type | Correct | Total | Accuracy |
|---|---:|---:|---:|
| gold (pass → pass) | 4,459 | 4,633 | **96.24%** |
| mutation_off_by_one | 159 | 183 | **86.89%** |
| mutation_operator_swap | 2,732 | 3,357 | **81.38%** |
| mutation_return_value | 424 | 562 | **75.44%** |
| mutation_boundary_removal | 492 | 1,049 | **46.90%** |
| **OVERALL** | **8,266** | **9,784** | **84.48%** |

关键发现：
- **gold 样本（正样本）** 识别率极高 96.24%，说明模型 recall_pass 强
- **boundary_removal 最难**，仅 46.90% — 这类 mutation 删除边界条件检查，语义变化微妙
- **off_by_one 最易检测** (86.89%)，但样本量最小 (183)
- operator_swap 是最大的 mutation 类别 (3,357)，准确率 81.38%

Registry `cls8b-s42-resume-ckpt3600-mutation` 已标记 DONE，metrics 已录入。

---
