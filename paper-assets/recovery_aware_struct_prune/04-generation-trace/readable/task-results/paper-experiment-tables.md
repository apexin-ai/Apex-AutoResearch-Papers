# paper experiment tables

**How Pruning Criteria Shape Post-RLVR Recovery: A Controlled Study of Structured MLP Pruning in a Reasoning LLM** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_paper_experiment-tables_20260515T043938_result.json`
- **Structured JSON:** [`377ad4d20498c4d301b5.json`](../../sessions/37/377ad4d20498c4d301b5.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

三个表格已创建：

- `artifacts/tables/table1_postprune.tex` — Post-prune 对比，已填入 Baseline/Standard/RASP 20% 数据
- `artifacts/tables/table2_recovery.tex` — Recovery pipeline 对比，已填入 Post-Prune 和 +SFT 数据
- `artifacts/tables/table3_alpha.tex` — α 消融，已填入 α=1.0 数据

所有表格使用 booktabs + siunitx S 列类型，TBD 以 `\textcolor{gray}{TBD}` 标记。主论文引用方式：`\input{tables/table1_postprune}`。需要在 preamble 中加载 `booktabs`、`siunitx`、`xcolor`。

---
