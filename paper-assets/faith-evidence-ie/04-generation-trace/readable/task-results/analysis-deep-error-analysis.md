# analysis deep error analysis

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_deep_error_analysis_20260519T101901_result.json`
- **Structured JSON:** [`6ee194ba056111209d2f.json`](../../sessions/6e/6ee194ba056111209d2f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

分析完成。结果文件在 `/root/autodl-tmp/freige/scripts/analysis/results/` 下，summary 已保存到项目 memory。

核心发现：

**Per-Relation**: RSFT gain 高度 relation-dependent。4B 最大增益在 entertainment/media 关系（original network +32pt, cast member +14pt, performer +13pt），损失集中在低频关系（chairperson -16pt, screenwriter -9pt）。8B 增益分布更分散。

**Per-Length (ign_f1)**: 4B gain 跨长度较均匀（+4.8~5.8pt）。8B 有趣的模式：**长文档 gain 最大**（+4.6pt vs 短文档 +2.9pt），说明 RSFT 在 8B 上更多帮助了复杂多句推理。

**Per-Entity-Count (ign_f1)**: 4B 中等实体数文档 gain 最大（+6.4pt）；8B 低/高实体数 gain 相近（~4pt），中等实体数 gain 最小（+2.0pt）。

注意：4B RSFT s42 无 predictions 文件，使用了训练 seed 43 的模型替代（`rsft_s43_dev_eval_preds`, ign_f1=0.451）。

---
