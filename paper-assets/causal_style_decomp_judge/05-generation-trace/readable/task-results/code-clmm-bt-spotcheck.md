# code clmm bt spotcheck

**The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_clmm_bt_spotcheck_20260521T022659_result.json`
- **Structured JSON:** [`b8a3fcaadb6cc5c3a87a.json`](../../sessions/b8/b8a3fcaadb6cc5c3a87a.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。汇总：

---

## Task 1: CLMM 分析 — Blindspot 确认

| 方法 | is_formal coef | p-value | 95% CI |
|------|---------------|---------|--------|
| Ordinal Regression | -0.079 | **0.769** | [-0.60, 0.45] |
| GEE (paired) | -0.084 | **0.587** | [-0.39, 0.22] |
| Wilcoxon | — | **0.905** | — |

88 对中 55 对 (62.5%) Likert 分数完全相同。**三个检验一致：Likert 评分无法检测 style effect。**

## Task 2: Bradley-Terry 建模

| 指标 | 值 |
|------|-----|
| BT strength (formal-casual) | **+0.4436** |
| P(formal wins) | **60.9%** |
| Bootstrap 95% CI | **[53.8%, 68.0%]** |
| CI 排除 50% | **Yes** |
| N comparisons | 197 (全量) |

对比 sign test (filtered): 69.1%, p=0.006。BT 更保守但仍显著。

## Task 3: Spot Check 脚本

`csd_pipeline/exp013_spotcheck.py` 已写入服务器。运行需设置 `SPOTCHECK_API_KEY` 环境变量。

---
