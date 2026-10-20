# code case study postprocess

**Beyond Self-Consistency: Self-Extracted Constraints Reduce to Majority Voting under Zero-Shot Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_case-study-postprocess_20260518T113020_result.json`
- **Structured JSON:** [`e093dfa66b8946f32887.json`](../../sessions/e0/e093dfa66b8946f32887.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出已完成。以下是报告。

---

## 后处理报告

### 产出文件
- 脚本: `/root/symb_invariant_consensus/scripts/postprocess_case_study.py`
- 归一化结果: `/root/symb_invariant_consensus/results/case_study_normalized.json`

### 任务 1：归一化后 SC/SICA 结果

| 问题 | Gold | 归一化 SC | SC 分布 | 归一化 SICA | SICA scores |
|------|------|-----------|---------|-------------|-------------|
| folio_134 | Unknown | **True** | True:11, Unknown:1 | **True** | True:55.0, Unknown:0.0 |
| PW-1066_Q6 | False | **False** ✓ | Unknown:4, True:3, False:5 | **False** ✓ | Unknown:115, True:105.5, False:121 |
| PW-903_Q6 | False | **True** | True:5, Unknown:4, False:3 | **True** | True:103.5, Unknown:98, False:58.5 |

### 与 exp-001 对比

| 问题 | exp-001 SC | re-extract SC | 匹配 | exp-001 SICA | re-extract SICA | 匹配 |
|------|-----------|---------------|------|-------------|-----------------|------|
| folio_134 | True | True | ✓ | Unknown | True | ✗ |
| PW-1066_Q6 | False | False | ✓ | True | False | ✗ |
| PW-903_Q6 | False | True | ✗ | False | True | ✗ |

**不一致原因**: re-extraction 是独立的推理采样，12 条 trace 的答案分布与 exp-001 不同。exp-001 三题均为 6:6 平票 (vote_entropy=1.0)，而 re-extraction 的 trace 分布偏向不同方向（folio_134 甚至 11:1）。SICA 的差异是 trace 分布差异的自然结果，不是归一化问题。

归一化本身是正确的：修复前 folio_134 的 SC 票被分裂为 True:5 / `\text{True}`:5 / `\text{true}`:1 / `\text{uncertain}`:1，修复后合并为 True:11 / Unknown:1。

### 任务 2：Constraint count 差异分析

| 问题 | exp-001 | re-extract (Z3 dedup) | weight≥2 | unique expressions |
|------|---------|----------------------|----------|-------------------|
| folio_134 | 7 | 22 | 8 | 17 |
| PW-1066_Q6 | 17 | 31 | 16 | 32 |
| PW-903_Q6 | 44 | 72 | 32 | 51 |

**根本原因：Z3 变量命名不一致导致去重失败。**

以 folio_134 为例，同一逻辑事实 "Some mammals have teeth" 在不同 trace 中被编码为 4 种不同的 Z3 变量：
- `mammals_have_teeth == True` (traces 1,2,3,6)
- `some_mammals_have_teeth == True` (traces 4,5,8,9)
- `some_mammal_has_teeth == True` (trace 11)
- `Exists(x, And(mammal_x, have_teeth_x))` (trace 0)

Z3 equivalence checker 无法判定不同变量名的布尔表达式等价，因此每个变体都作为独立约束保留。

**weight≥2 过滤**（仅保留出现在 2+ trace 中的约束）后得到 8/16/32，与 exp-001 的 7/17 非常接近，说明 exp-001 的模型命名更一致，大部分约束都能被正确去重合并，而 re-extraction 中大量 weight=1 的约束是命名变体碎片。

---
