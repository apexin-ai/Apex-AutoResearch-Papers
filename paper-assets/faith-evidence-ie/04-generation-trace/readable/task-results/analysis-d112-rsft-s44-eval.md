# analysis d112 rsft s44 eval

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_d112_rsft_s44_eval_20260519T105916_result.json`
- **Structured JSON:** [`b8aa63c4466c2286853b.json`](../../sessions/b8/b8aa63c4466c2286853b.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新。结果摘要：

## D112 RSFT s44 Eval — 结论：**negative**

| 指标 | D112 RSFT s44 | SFT s44 baseline | RSFT s42 (4B) |
|---|---|---|---|
| **ign_f1** | **0.2181** | 0.4734 | 0.4482 |
| ign_precision | 0.3523 | — | — |
| ign_recall | 0.1579 | — | — |
| EDCR | 0.7762 | — | — |
| evi_f1 (TP) | 0.7654 | — | — |
| evi_f1 (joint) | 0.1785 | — | — |

**ign_f1 = 0.2181，相比 SFT s44 baseline (0.4734) 下降 53.9%，远低于所有基准。** Hypothesis 被否定。

**根因分析：**
- **截断率 85.2%**（839/985 文档被截断）— 模型生成过长输出，在 max_new_tokens=1024 处被截断，导致大量预测不完整
- **evidence_format_rate 仅 13.1%**（129/985）— 绝大多数文档的 evidence 字段格式无效
- **ign_recall 极低 (0.1579)** — 仅预测 5340 个关系中 2108 个 TP（gold 有 12151 个），模型严重欠召回
- 对比之下，evi_f1(TP)=0.7654 和 EDCR=0.7762 说明少数正确预测的 evidence 质量尚可，但整体被截断和格式问题压垮

RSFT 在 4B scale + s44 seed 上未能泛化，产出严重退化。

---
