# code fix hs exploratory prediction

**Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix_hs_exploratory_prediction_20260520T015119_result.json`
- **Structured JSON:** [`a8752ce2f3bf61a154a3.json`](../../sessions/a8/a8752ce2f3bf61a154a3.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成：

- **`scripts/advbench_hs_exploratory.py`**：`prediction` 字段已替换为 `shallow_deep_ratio` + `note`（行 174），print 语句已同步更新（行 190）
- **`artifacts/advbench_preliminary/hs_exploratory_results.json`**：`prediction` 字段已删除（grep 无匹配），`shallow_deep_ratio: 0.5995` 已写入，JSON 验证通过

---
