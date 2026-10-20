# ssh fix traj eval predictions

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fix-traj-eval-predictions_20260523T093947_result.json`
- **Structured JSON:** [`ce0db0db990c6775c9cc.json`](../../sessions/ce/ce0db0db990c6775c9cc.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。`results["predictions"] = pred_details` 已插入在 line 282（`json.dump` 之前）。语法验证通过。`pred_details` 每条记录包含 `problem_id`、`mutation_type`、`true_label`、`pred_label`、`gen_text`，TOST 分析所需字段齐全。

---
