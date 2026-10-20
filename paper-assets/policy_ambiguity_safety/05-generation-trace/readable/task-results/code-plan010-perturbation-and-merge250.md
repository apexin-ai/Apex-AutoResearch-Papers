# code plan010 perturbation and merge250

**Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_plan010_perturbation_and_merge250_20260520T125715_result.json`
- **Structured JSON:** [`7c5138518418bc7e5367.json`](../../sessions/7c/7c5138518418bc7e5367.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

产出完成：

### 子任务 A：`clauses_perturbation_control.json`（30 条）
- 15 synonym substitution + 15 clause reordering
- 每种 perturbation 覆盖 6 个 ambiguity type

**Surface-level 变化量对比表：**

| Metric | Ambiguity Pairs | Perturbation Pairs | Ratio |
|---|---|---|---|
| Token diff (mean) | 23.3 | 10.0 | **2.33x** |
| Edit distance (mean) | 163.8 | 155.8 | **1.05x** |
| Token diff (max) | 50 | 23 | — |
| Edit distance (max) | 320 | 372 | — |
| Token diff (min) | 3 | 2 | — |
| Edit distance (min) | 29 | 36 | — |

两项 ratio 均在 5x 以内。

### 子任务 B：`clause_templates_full.json`（250 条）
- authorization_scope: 50, conditional_precedence: 50, incompleteness: 50, lexical: 50, scopal: 50
- 按 ambiguity_type (alphabetical) → clause_id 排序
- 11 个必填字段全部填充，无 null

---
