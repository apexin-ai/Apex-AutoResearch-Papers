# research comprehensive results table

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_comprehensive_results_table_20260519T075754_result.json`
- **Structured JSON:** [`fa4de8b91ab03b994307.json`](../../sessions/fa/fa4de8b91ab03b994307.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已完成。产出文件: `artifacts/comprehensive_results.md` (art_20260519_a97536)

包含 10 张表:

| 表 | 内容 |
|---|------|
| Table 1 | Scale x Method ign_f1 主表 (1.7B/4B/8B/14B x SFT/RSFT/GRPO/No-evidence) |
| Table 2 | Evidence metrics 全量明细 (evi_f1, EDCR, rel_f1) |
| Table 3 | Seed variance analysis + per-seed RSFT gain |
| Table 4 | Evidence tax (with vs without evidence) |
| Table 5 | RSFT scoring ablation (CED vs flat-NLI vs Random) |
| Table 6 | GRPO checkpoint analysis (G=4, G=8, RSFT->GRPO) |
| Table 7 | CED reranker (inference-time, no fine-tuning) |
| Table 8 | Cross-architecture (Llama-3.1-8B) |
| Table 9 | Re-DocRED transfer |
| Table 10 | DREEAM baseline |

每个数值标注 source exp_id，pending 实验已标出（14B eval、8B RSFT k=1 s42/s43 eval、D112 pipeline）。

核心发现: 4B RSFT variance reduction 7.1x (3.80pp->0.53pp)、evidence tax 非单调 (1.7B 负税 -8pp / 4B 正税 +7.5pp / 8B 近零)、CED vs Random +3.52pp 但 CED vs flat-NLI 无显著差异。

---
