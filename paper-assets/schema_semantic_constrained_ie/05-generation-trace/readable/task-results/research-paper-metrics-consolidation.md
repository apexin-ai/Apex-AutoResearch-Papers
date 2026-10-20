# research paper metrics consolidation

**OntoCoDec: Type-Constrained Information Extraction via Compiled Schema Constraints** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_paper_metrics_consolidation_20260515T230405_result.json`
- **Structured JSON:** [`1f8eeb521f43081327f1.json`](../../sessions/1f/1f8eeb521f43081327f1.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

已保存至 `artifacts/_project/report/paper_tables_consolidated.md` (art_20260515_4687fa)。

关键数字摘要：

**Table 3 (Zero-shot)** — 12/12 格子已填：
- DR reduction: 44.7%–99.4%，SciERC 两个模型均 >93%，DocRED Llama 90.2% 但 Qwen 仅 44.7%（最弱格子）
- 所有 ΔR-F1 在 ±0.5pp 内，ΔE-F1 在 ±1.22pp 内

**Table 5 (Fine-tuned)** — 4/8 格子已填，4 个 DocRED 待完成：
- SciERC: DR reduction 91.9%–100%，ΔF1 几乎为零（最大 ±0.09pp）
- DocRED: 4 个实验仍在 RUNNING/PREPARING

**需要关注的点：**
1. Qwen-DocRED zero-shot DR reduction 仅 44.7%，论文需要解释（schema 复杂度论点）
2. CF% trade-off：constrained 引入 CF 违规（zero-shot 平均 ~7-8%），但 fine-tuning 大幅缓解至 <1%
3. 4 个 DocRED fine-tuned 实验需在 May 19 前完成以支撑 cross-dataset 一致性 claim

---
