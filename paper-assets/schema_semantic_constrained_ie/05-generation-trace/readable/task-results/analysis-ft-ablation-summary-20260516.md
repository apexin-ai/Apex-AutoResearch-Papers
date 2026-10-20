# analysis ft ablation summary 20260516

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_ft_ablation_summary_20260516_20260516T105606_result.json`
- **Structured JSON:** [`41554039704094146812.json`](../../sessions/41/41554039704094146812.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件写入 `artifacts/ft_ablation_analysis.md` 并注册为 `art_20260516_8464b5`。

核心发现：
- **Grammar 层在 FT 后完全冗余**（ET/RV 已被模型内化为零）
- **Semantic 层提供唯一边际价值**，单独将 DR 降低 41-68%
- **两层协作才能归零 DR**（semantic-only 仍有 0.6% 残余）
- **F1 代价可忽略**（最大变动 -0.17pp R_F1）
- DocRED 的 grammar_only / semantic_only 实验仍在跑，表格中标 TBD

---
