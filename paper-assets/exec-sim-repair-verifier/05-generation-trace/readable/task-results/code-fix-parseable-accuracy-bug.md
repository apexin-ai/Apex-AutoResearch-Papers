# code fix parseable accuracy bug

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-parseable-accuracy-bug_20260521T210558_result.json`
- **Structured JSON:** [`14293be27302deaf1329.json`](../../sessions/14/14293be27302deaf1329.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Bug confirmed and fix validated.

**Bug 原因**：`run_inference` 中 unparseable 的预测（`pred == -1`）被回退为 `majority_class`，然后 `correct = int(pred == label)` 用回退后的 pred 计算。所以部分 unparseable 条目的 `correct = 1`（majority class 恰好匹配 label）。但 shell 脚本里分子 `correct` 包含了这些 unparseable-but-lucky 的条目，分母却只数 parseable 条目，导致比值 > 100%。

**修复**：分子排除 unparseable 条目：
```python
# 旧
correct = sum(1 for r in results if r.get('correct', False))
# 新
correct = sum(1 for r in results if r.get('correct', False) and not r.get('unparseable', False))
```

**验证**（deepseek_cwm_repo_s123_test）：
- 修复前：179.54%（6056 correct / 3373 parseable）
- 修复后：41.27%（1392 correct / 3373 parseable）
- seq4096 数据无 unparseable，不受影响（86.05% 不变）

已修复 5 个 shell 脚本：`eval_deepseek_cwm_s123_v2.sh`、`eval_deepseek_cwm_s456_v2.sh`、`eval_qwen_cwm_s123.sh`、`eval_qwen_cwm_s456.sh`、`eval_14b_cwm_pilot.sh`。

---
