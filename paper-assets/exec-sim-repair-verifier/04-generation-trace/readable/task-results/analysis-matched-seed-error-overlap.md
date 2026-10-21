# analysis matched seed error overlap

**A Systematic Comparison of Execution-Free Verification Formulations for Code Repair** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_matched-seed-error-overlap_20260512T165936_result.json`
- **Structured JSON:** [`ff52c6b1691aff6055eb.json`](../../sessions/ff/ff52c6b1691aff6055eb.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。关键结果如下：

---

### 1. Agreement/Disagreement

| 类别 | 数量 | 百分比 |
|------|------|--------|
| Both correct | 1601 | 84.71% |
| Both wrong | 177 | 9.37% |
| CLS-only correct | 59 | 3.12% |
| CWM-only correct | 53 | 2.80% |

- CLS accuracy: **87.83%**, CWM accuracy: **87.51%**
- Cohen's Kappa (prediction): **0.8815** (几乎完全一致)
- Cohen's Kappa (correctness): **0.7259** (实质一致)

### 2. Oracle Combination

- Oracle accuracy: **90.63%** (1713/1890)
- Complementarity: **+2.80%** (在 CLS 87.83% 基础上)

### 3. 按 Mutation Type

| Type | N | CLS% | CWM% | Diff | Sig? |
|------|---|------|------|------|------|
| original | 398 | 89.45 | 85.18 | **+4.27** | No (p=0.09) |
| off_by_one | 671 | 80.33 | 81.82 | -1.49 | No |
| operator_swap | 298 | 85.91 | 88.59 | -2.68 | No |
| return_value | 402 | 98.01 | 97.01 | +1.00 | No |
| variable_swap | 85 | 96.47 | 94.12 | +2.35 | No |
| boundary_removal | 36 | 91.67 | 88.89 | +2.78 | No |

**无一达到统计显著**。CLS 在 original 上优势最大 (+4.27%)，CWM 在 operator_swap (-2.68%) 和 off_by_one (-1.49%) 上略优。

### 4. 按 Problem ID

- 114 个 problems 中，CLS 强势 (>10% diff) 有 9 个，CWM 强势有 8 个
- 最极端：MBPP/397 CLS=100% vs CWM=40%；MBPP/487 CLS=66.7% vs CWM=93.3%

### 5. Error Patterns

**CLS-only errors (53 样本)**：主要是 off_by_one (32) 和 operator_swap (17)，**true label 偏向 FAIL** (40/53=75.5%) — CLS 倾向于把 FAIL 误判为 PASS。

**CWM-only errors (59 样本)**：分布更均匀，original 占 18 个，**true label 偏向 PASS** (49/59=83.1%) — CWM 倾向于把 PASS 误判为 FAIL。

**两模型错误模式互补**：CLS 漏 FAIL，CWM 漏 PASS。

**CWM-only correct 的 exact_match 率**：50/53 = **94.34%** — CWM 在它独占正确的样本上几乎都做了精确输出预测。

**CLS-only correct 时 CWM 的 error_type**：49/59 预测为 PASS（即 CWM 预测程序通过但实际有错误/预测错了 label），7 个 AssertionError。

### 6. 与 Cross-seed 对比

| 指标 | Cross-seed | Matched-seed | 差异 |
|------|-----------|-------------|------|
| Oracle | 90.63% | **90.63%** | 0.00% |
| Complementarity | 5.90% | **2.80%** | **-3.10%** |

**Oracle accuracy 完全一致**（90.63%），但 matched-seed 的 complementarity 从 5.9% 降到 2.8%。原因：matched-seed 时两个模型共享训练数据划分，各自 accuracy 更高（CLS 87.83% vs cross-seed 的 ~84.7%），但互补性下降 — 相同 seed 导致模型在相似样本上犯类似错误。Oracle 上限未变说明两种方法学到的互补空间是稳定的。

---
