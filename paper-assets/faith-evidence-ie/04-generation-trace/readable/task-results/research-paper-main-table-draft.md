# research paper main table draft

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_main_table_draft_20260516T033151_result.json`
- **Structured JSON:** [`fad27b55f17477712613.json`](../../sessions/fa/fad27b55f17477712613.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件: `artifacts/paper_main_tables_draft.md` (art_20260516_bc261a)

编译了 4 张表:

- **Table 1 (Main Results)**: 8 行，含 SFT no-evidence (Ign-F1=47.36), SFT baseline (40.36), RSFT flat-NLI best/mean, RSFT CED best/mean, CED reranker (F1=48.64), DREEAM。Evidence tax = −7.00pp，CED reranker 恢复 97%。
- **Table 2 (Decoupling Spectrum)**: 9 行，从 catastrophic (GRPO QLoRA F1=1.38) 到 none (RSFT CED F1=46.83)。附带 GRPO bf16 6-step 和 QLoRA 5-step 轨迹补充表。
- **Table 3 (Seed Comparison)**: CED 3 seed + flat-NLI 4 seed，Head-to-head 对比 (Δ=+0.39pp, not significant)，top_k ablation (k=1 > k=3)，D076 unified reeval status。
- **Cross-Table EDCR**: 17 个方法排序，含 plan_003 相关性统计。

5 项 critical PENDING: CED reranker Ign-F1、D076 reevals (×4)、CED s45 eval、多项 Ign-F1 修正、test set evaluation。

---
