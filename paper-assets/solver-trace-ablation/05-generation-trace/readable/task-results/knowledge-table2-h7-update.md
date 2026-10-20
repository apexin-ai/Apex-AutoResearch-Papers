# knowledge table2 h7 update

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_table2-h7-update_20260514T101302_result.json`
- **Structured JSON:** [`7fd93d4f766a9e2f9708.json`](../../sessions/7f/7fd93d4f766a9e2f9708.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。更新汇总：

**新建文件：**
- `artifacts/table2_hacking_taxonomy.csv` — 含 H1/H3/H4/H7 + Genuine/Total，H7 含 3-seed 数据
- `artifacts/table2_hacking_taxonomy.tex` — LaTeX 表格，脚注含 H7 multi-seed 明细和定义

**更新文件：**
- `artifacts/paper_tables_draft.md` — Table 2 加入 H7 行，H1 从 72.8%→60.5%（10 samples reclassified to H7），新增 H7 interpretation
- `artifacts/hacking_taxonomy_comparison.md` — 分布表 H7 从 † 改为校准值 10/12.3%，H1 从 59→49，Key Findings 新增 H7 条目，Mode 6 section 更名为 H7 并补充校准数据

**关键数值变化：** H7 的 10 samples 从 H1 (Conclusion Embedding) 中拆出，H1 Δ 从 -5.7pp 变为 -18.0pp，总 hacking rate 不变（74.1% vs 82.3%）。

---
