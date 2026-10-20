# infra deberta wiki cron resolve

**Generational Depth Estimation of Recursive Synthetic Text: Measuring the Discrimination Boundary** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_infra_deberta-wiki-cron-resolve_20260519T215745_result.json`
- **Structured JSON:** [`f797293c4d93aa927970.json`](../../sessions/f7/f797293c4d93aa927970.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

## 结果报告

**结论：success** — 5/5 wiki config 全部完成，无报错，日志末行 "All done."

### K* 结果（θ=0.6）

| Config | K*(DeBERTa) | K*(OBD) | 1v2 AUC(DeBERTa) | 1v2 AUC(OBD) | delta |
|--------|-------------|---------|-------------------|---------------|-------|
| wiki_pythia | 2 | — | 0.7250 | 0.6193 | +0.1057 |
| wiki_olmo | **0** | — | 0.5183 | 0.6193 | **-0.1010** |
| wiki_qwen7b | 2 | — | 0.7619 | 0.6108 | +0.1511 |
| wiki_llama8b | 2 | — | 0.7452 | 0.5954 | +0.1498 |
| wiki_mistral7b | 2 | — | 0.7483 | 0.5552 | +0.1931 |

### 关键发现

- 4/5 config DeBERTa K\*=2，与 OBD-LightGBM 一致，支持假设：**饱和边界 K\*=2 是生成过程的内在属性**，而非特征天花板。
- **wiki_olmo 异常**：DeBERTa K\*=0（1v2 AUC 仅 0.518，近随机），反而**低于** OBD baseline。OLMo 的 depth-1 vs depth-2 对 DeBERTa 几乎不可区分，值得进一步分析。
- DeBERTa 在其他 4 个 config 的 1v2 AUC 比 OBD 高 0.10-0.19，确认了神经表征的优势，但未改变 K\* 边界。

---
