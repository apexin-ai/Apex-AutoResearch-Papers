# paper prep crossarch table

**Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_prep_crossarch_table_20260518T002805_result.json`
- **Structured JSON:** [`cb9dd3f3d738cb460d2f.json`](../../sessions/cb/cb9dd3f3d738cb460d2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Memo 已写入 `artifacts/crossarch_table_prep.md`。

关键发现:
- 14B 表格在 `experiments.tex` lines 231–248 (`tab:14b`), uniform row 在 line 245 以注释形式预留
- KL 的 PPL-MMLU 解耦是核心问题: PPL 最优 (7.62) 但 MMLU 最差 (63.72 vs TEAL 71.83)
- Uniform 数据到位后需改: table row (L245), 叙事段 (L226–229), caption (L233), 以及 sec:scaling 的 cross-arch reference (L192)
- 两种情景方案已写好: A (allocation 根因, 强化 phase transition narrative) vs B (结构性问题, 弱化 claim 聚焦 PPL generalization + limitation)

---
