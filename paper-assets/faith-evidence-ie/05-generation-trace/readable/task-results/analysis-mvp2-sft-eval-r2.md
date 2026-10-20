# analysis mvp2 sft eval r2

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_analysis_mvp2_sft_eval_r2_20260514T145314_result.json`
- **Structured JSON:** [`86d52a0839fe9e4c28fa.json`](../../sessions/86/86d52a0839fe9e4c28fa.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

Registry 已更新为 DONE/success。以下是 mvp2_sft_eval_r2 的完整结果：

## SFT Baseline Eval 结果 (DocRED dev, 985 samples)

| 指标 | 数值 |
|------|------|
| **Rel-F1** | **0.4057** |
| **Ign-F1** | 0.4057 |
| **Precision** | 0.4043 |
| **Recall** | 0.4070 |
| **Evi-F1** | **0.7979** |
| Evi-Precision | 0.8035 |
| Evi-Recall | 0.7924 |
| **EDCR** | **0.7118** |
| Format OK | 983/985 (99.8%) |
| **Parse 成功率** | **617/985 (62.6%)** |
| 截断数 | 367/985 (37.3%) |
| 总预测数 | 18,815 |
| 推理耗时 | 6,484.7s (~108min) |

## 分析

**关键问题：截断率过高。** 367/985 (37.3%) 的输出在 max_new_tokens=1024 处被截断，导致 JSON 不完整、无法解析。这是 format_ok_rate (99.8%) 与实际 parse 成功率 (62.6%) 之间巨大差距的原因——模型生成了合法 JSON 格式，但被长度截断后变成不完整的输出。

**对 GRPO 实验的 baseline 参考意义：**
- Rel-F1=0.4057 是 GRPO 需要超越的关系抽取基线
- Evi-F1=0.7979 说明 SFT 模型已经学到了较好的证据定位能力
- EDCR=0.7118 表示约 71% 的引用是针对性的（非 distractor），GRPO 的 CED reward 目标是提升这个值
- 实际可用的只有 62.6% 的样本，**mvp2_sft_eval_r3（统一 eval 代码 + truncated JSON 修复）应能显著提升 parse 率，从而给出更准确的 baseline 数值**

---
