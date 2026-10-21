# paper final consistency check

**Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_final-consistency-check_20260521T171519_result.json`
- **Structured JSON:** [`6ee4189fca3ea49451e4.json`](../../sessions/6e/6ee4189fca3ea49451e4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 检查 1: 数据一致性
**结果: PASS — 0 inconsistencies**

| # | 数字 | 出现次数 | 分布文件 | 状态 |
|---|------|---------|---------|------|
| 1 | 78.9% (75/95) | 12 | abstract, intro, related_work, method, experiments, main, conclusion | ✅ |
| 2 | DAF 90.4% [81.1, 99.0] | 12 | intro, method, experiments, main | ✅ |
| 3 | Llama DAF 88.2% [80.2, 95.1] | 3 | intro, experiments, main | ✅ |
| 4 | Gemma DAF 89.7% [79.5, 98.4] | 4 | intro, experiments, main | ✅ |
| 5 | 97.4% step tie rate | 5 | method, intro, main | ✅ |
| 6 | 245 episodes, 11 task types | 20+ | all files | ✅ |
| 7 | MATH 73.5% vs 73.0%, p=0.81 | 2 | experiments, intro | ✅ |
| 8 | 42.9% internal DR | 8 | experiments, main | ✅ |
| 9 | 105 vs 40 deaths | 5 | main, discussion | ✅ |
| 10 | Keyword 62.9%, LOTO 49.2% | 4 | main, experiments, discussion | ✅ |
| 11 | 0.5B death rate 13.3% | 2 | main, discussion | ✅ |
| 12 | Δ_nd = +2.84 | 6 | intro, experiments, main | ✅ |

---

## 检查 2: 交叉引用
**结果: PASS**
- Undefined references: 0
- Undefined citations: 0
- `??` markers: 0

---

## 检查 3: Figure/Table 引用
**结果: 9 issues — 均为有 label 无 ref（定义但未在正文引用）**

| Label | 类型 | 问题 |
|-------|------|------|
| `tab:baselines` | table | 未被引用 |
| `tab:death-taxonomy` | table | 未被引用 |
| `tab:decision-framework` | table | 未被引用 |
| `tab:loo` | table | 未被引用 |
| `tab:loto-daf` | table | 未被引用 |
| `tab:threshold-routing` | table | 未被引用 |
| `tab:wild-cluster` | table | 未被引用 |
| `app:prompt-templates` | appendix | 未被引用 |
| `sec:experiments` | section | 未被引用 |

反向检查（ref 无对应 label）: 0 问题。所有 `\ref{}` 都有对应 `\label{}`。

> **7 个 table 和 1 个 appendix 从未在正文中被 `\ref` 引用。** Reviewer 可能会标记这些为 orphan floats。建议在正文或 appendix 叙述中加入引用。`sec:experiments` 作为顶层章节可以接受。

---

## 检查 4: Orphan bib
**结果: PASS**
- 总 bib entries: 51
- Orphan entries: 0

---

## 检查 5: 编译
**结果: PASS**
- Errors: 0
- Undefined references: 0
- Undefined citations: 0
- Total pages: 25（正文 ~8 页，第 9 页起为 bibliography，第 12-25 页为 appendix/checklist）
- 正文在 8 页限制内 ✅

---

## 总结

| 检查项 | 结果 |
|--------|------|
| 1. 数据一致性 | ✅ PASS |
| 2. 交叉引用 | ✅ PASS |
| 3. Fig/Tab 引用对称性 | ⚠️ 7 tables + 1 appendix 未被正文引用 |
| 4. Orphan bib | ✅ PASS |
| 5. 编译状态 | ✅ PASS |

唯一需要关注的是检查 3 中 7 个未被引用的 table（均在 appendix 中）和 `app:prompt-templates`。如果这些 table 在 appendix 正文中有 "Table X shows..." 这样的自然语言引用但没用 `\ref{}`，则实际问题可能更小。是否需要逐个修复？

---
