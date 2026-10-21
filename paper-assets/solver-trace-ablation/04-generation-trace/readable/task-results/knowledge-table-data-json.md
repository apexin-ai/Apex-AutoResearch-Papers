# knowledge table data json

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_knowledge_table-data-json_20260514T172336_result.json`
- **Structured JSON:** [`15331c4c4c5bb766938c.json`](../../sessions/15/15331c4c4c5bb766938c.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已生成 `artifacts/table_data.json` 并注册 (`art_20260514_0d350a`)。

内容覆盖：
- **table1_goodhart_landscape**: 9 个条件（base_model, sft, exec-only 500/1000, ISR/Random β=0.1/0.3, convex），含 exp_id、per-seed 精确指标、3-seed mean±std（重新计算）
- **table2_hacking_taxonomy**: 5 个条件的 H7/H1/Genuine 分布 + key findings
- **claim2_isr_vs_random**: premise-count-matched ISR (1.06×)，3-seed 汇总
- **prolog_exec_only_3seed**: 3 seed + mean±std
- **prolog_sta**: s42 done (H7=100%), s43/s44 RUNNING
- **isr_collapse_trajectory**: 100→500→1000 步 ISR 下降轨迹

数据来源注记：random_b01_s43 的 ISR 值来自 eval_sta.py（registry 仅有 hacking taxonomy），ISR_b03 eval 指标来自 evidence_tables_d051（registry 仅有训练指标）。

---
