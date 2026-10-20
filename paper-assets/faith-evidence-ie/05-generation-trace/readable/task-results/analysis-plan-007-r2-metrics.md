# analysis plan 007 r2 metrics

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_plan_007_r2_metrics_20260516T133725_result.json`
- **Structured JSON:** [`38e3575ef8f3914e384f.json`](../../sessions/38/38e3575ef8f3914e384f.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。

**Re-DocRED cross-dataset 4B SFT eval 结果摘要：**

- **Ign-F1: 36.59%** — 相比 DocRED in-domain eval（D080 提到的基线）确实有明显下降，符合 cross-dataset 泛化预期
- **Evi-F1: 81.70%** — evidence 质量保持很高，说明模型学到了可泛化的 evidence 定位能力
- **EDCR: 66.74%** — 2/3 的 citation 指向非 distractor 句子
- **Format compliance: 99.6%** — 几乎无格式错误
- **Truncated: 139/493 (28.2%)** — 较高的截断率，Re-DocRED 文档较长，max_new_tokens=1024 可能不够

关键观察：Evi-F1 在 cross-dataset 上仍达 81.7%，说明 evidence-grounded 训练的泛化性良好。Ign-F1 下降主要因为 relation recall 低（32.8%），可能与 Re-DocRED 的 relation schema 差异有关。

---
