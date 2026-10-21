# analysis error analysis plan018 fix

**Trace Verbosity Degrades SFT Verdict Prediction: A Case Study in Information Density Effects** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error_analysis_plan018_fix_20260521T052911_result.json`
- **Structured JSON:** [`7c46888c7e84c386ddc9.json`](../../sessions/7c/7c46888c7e84c386ddc9.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

All corrections applied. Here's the summary:

---

**W1 — SyntaxError claim 修正**

原文 (line 281): `"Across ALL conditions and ALL models, SyntaxError samples have 0% error rate"`

修正为: `"Across all trace-informed conditions (exception_only, ae_only, loop_only, vota, full_trace) and all models, SyntaxError samples have 0% error rate. The no_trace condition is the exception (19.83% average SyntaxError error rate)"`

**W2 — DeepSeek 错误数根因**

**根因**: 两个完全损坏的训练 run（acc < 16%）被混入分析：
- `deepseek_vota`（无 seed 后缀）: accuracy=15.97%, 1000/1190 errors
- `deepseek_full_trace`（无 seed 后缀）: accuracy=10.59%, 1064/1190 errors

这些 run 没有 seed 后缀，脚本 `parse_experiment_name` 默认将其标记为 seed="42"，Section 5 代码优先选 seed42 run 作为代表，导致选中了这两个坏 run。**不是重复计数问题，是坏 run 被当作有效实验纳入分析。**

**修正**: 在脚本中加入 acc<50% 过滤器，排除 6 个坏 run。修正后数字：

| 指标 | 原值 | 修正值 |
|------|------|--------|
| deepseek VOTA errors | 1000 | 10 (seed123, acc=99.16%) |
| deepseek full_trace errors | 1064 | 248 (seed42_v3, acc=79.16%) |
| vota total unique errors | 1000 | 31 |
| full_trace total unique errors | 1108 | 434 |
| 有效实验数 | 110 | 104 |

---
