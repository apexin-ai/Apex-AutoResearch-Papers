# analysis r15 taskA paper verification

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_r15_taskA_paper_verification_20260521T014620_result.json`
- **Structured JSON:** [`11fa7038578adc98e626.json`](../../sessions/11/11fa7038578adc98e626.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

结果已保存到 `artifacts/r15_verification/task_a_verification.json`。

**摘要：**

1. **"guarantee" 用词** — 19 处匹配，分布在 9 个 .tex 文件中（含 2 个 DEPRECATED 版本的 abstract）。主要用法：
   - 描述 grammar layer "guarantees" 结构合法性（~7 处）
   - 对比 training-based 方法 "cannot guarantee" / "no guarantee"（~5 处）
   - Contribution 1 中 "formal guarantees at each level"
   - `section6_relwork_additions.tex:25` 是注释行，非正文

2. **Contributions** — 共 2 条 contribution。**κ̄ (kappa bar) 仍在 contribution 1 中**，描述为 "descriptive metric correlating schema restrictiveness with DR reduction"。

3. **BibTeX 验证** — 两个 key 均正常：
   - `chen2024agentre`: bib 中存在（`relwork_new_entries.bib:617`），被 `section5_scierc_draft.tex:108` 引用 ✓
   - `fan2024fsn`: bib 中存在（`relwork_new_entries.bib:626`），被 `section5_scierc_draft.tex:108` 引用 ✓
   - 无 orphan，无 missing

---
