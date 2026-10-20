# check paper status

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_check_paper_status_20260520T101358_result.json`
- **Structured JSON:** [`301b71016f057abbe6b4.json`](../../sessions/30/301b71016f057abbe6b4.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

汇总结果：

---

## 1. Table 2 (tab:composability) — D069 修正未入稿

`section5_scierc_draft.tex:140` Llama DocRED Full S1 行仍为旧值：

| 字段 | 当前值 | D069 应改为 |
|------|--------|-------------|
| **Llama Con E-F1** | **85.23** | **83.94** |
| Qwen Unc CF | 0.12 | 0.09 |
| Qwen Con CF | 0.41 | 0.27 |

根因：beam-4 (d064) 的 E-F1=85.23 被误放入 greedy 行，正确的 greedy 值为 83.94。

## 2. 编译状态

- **main.pdf** 最后生成：`2026-05-20 08:43 UTC`
- **无编译错误**（0 个 `!` error）
- **无 undefined references/citations**
- 13 个 `h→ht` float 警告（正常）
- 1 个 `Label(s) may have changed` 警告（需再跑一次 LaTeX 消除）

## 3. review_issues 状态

| 类别 | 数量 |
|------|------|
| **Resolved** | **24** |
| **Open** | **1** (R11-DIV1: 技术新颖性评估分歧，reviewer 间分歧，无 action item) |

唯一 open issue `R11-DIV1` 是 reviewer 间对新颖性的意见分歧（R1: 3/5, R2: 2.5/5），属于主观评价，无具体修改项。

---

**待办**：D069 的三处数值修正需要写入 `section5_scierc_draft.tex` 的 tab:composability 表。需要我执行修正吗？

---
