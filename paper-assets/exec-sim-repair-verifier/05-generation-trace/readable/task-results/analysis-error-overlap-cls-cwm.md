# analysis error overlap cls cwm

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_error-overlap-cls-cwm_20260512T160639_result.json`
- **Structured JSON:** [`3a8d15ac0cd0e2f8cf44.json`](../../sessions/3a/3a8d15ac0cd0e2f8cf44.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总关键发现：

---

## 结果汇报

### 任务 1: CLS vs CWM Error Overlap (seed42, n=1890)

| 类别 | 数量 | 比例 |
|------|------|------|
| Both correct | 1601 | 84.71% |
| CLS-only correct | 59 | 3.12% |
| CWM-only correct | 53 | 2.80% |
| Both wrong | 177 | 9.37% |

**互补性**：Oracle 组合 (任一正确即正确) 准确率 = **90.63%**，比 CLS 单独 (+2.80pp)、CWM 单独 (+3.12pp) 都高。两种方法有约 **5.9%** 的互补空间。

**Cohen's Kappa**：
- 预测一致性 κ = 0.88 (almost perfect agreement)  
- 正确性一致性 κ = 0.73 (substantial agreement)

**按 mutation type**：互补性最强的是 **off_by_one** (CWM-only 4.8%, 两者都错 14.9%) 和 **operator_swap** (CWM-only 5.7%)。**return_value** 几乎完全重叠 (96.8% both correct)。

### 任务 2: CWM Per-class F1 Breakdown

CWM 最弱 mutation types:
1. **off_by_one**: acc 81.82%, exact_match 75.71%, fail_f1 79.87%
2. **original** (pass samples): acc 85.18%, exact_match 85.18%  
3. **operator_swap**: acc 88.59%, exact_match 85.91%

最强：**return_value** (97.01% acc, 94.78% exact_match), **variable_swap** (94.12% acc)

### 任务 3: cwm-seed789 Metrics 补录

已更新 registry：
- overall_accuracy: 86.67%
- pass_f1: 86.74, fail_f1: 86.60
- exact_match_rate: 83.97%
- baseline_gap: +34.92pp

---
