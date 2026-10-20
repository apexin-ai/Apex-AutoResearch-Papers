# eval home ckpt600 wait then submit ckpt800

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_eval_home-ckpt600-wait-then-submit-ckpt800_20260514T210915_result.json`
- **Structured JSON:** [`2125a50bcb2f87e14b12.json`](../../sessions/21/2125a50bcb2f87e14b12.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

### 1. ckpt-600 val@5120 完整 metrics

| 指标 | 值 |
|---|---|
| **accuracy** | 81.89 |
| **F1_macro** | 77.01 |
| **F1_pass** | 87.60 |
| **F1_fail** | 66.43 |
| precision_pass | 91.16 |
| precision_fail | 60.07 |
| recall_pass | 84.30 |
| recall_fail | 74.29 |
| unparseable | 0 |
| truncated | 234 |
| total | 9335 |
| majority_baseline | 75.88 |
| gap_vs_majority | +6.01pp |

### 2. ckpt-800 eval 提交确认

- **PID**: 3172988（已在运行，GPU 占用 31718 MiB）
- **exp_id**: `cls4b-seed123-ckpt800-val5120-eval`
- **parent**: `repo-level-cls-seed123-home`
- **status**: RUNNING（registry 已注册）

注：ckpt-800 eval 在 ckpt-600 完成后被自动启动（可能由 val_sweep 脚本触发），参数完全匹配，无需重复提交。

### 3. eval_repo_cls.py max_seq_length 默认值

**`--max_seq_length` 默认值 = 2048**

---
