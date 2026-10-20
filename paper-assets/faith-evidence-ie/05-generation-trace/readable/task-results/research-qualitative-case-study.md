# research qualitative case study

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_research_qualitative_case_study_20260518T034656_result.json`
- **Structured JSON:** [`0bbd753195722dae5373.json`](../../sessions/0b/0bbd753195722dae5373.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

3 组定性样例全部提取完成，保存在 `/root/autodl-tmp/eval_results/qualitative_case_study.json`。

**汇总：**

**Group 1 — RSFT vs SFT evidence 质量对比（3 例）：**
- Oleg Tinkov: SFT 引用错误句子 [4]（precision=0.00），RSFT 精准命中 [5]（precision=1.00）
- America's Sweetheart: SFT 堆砌 6 句 [0,1,2,3,4,7]（precision=0.17），RSFT 只引 [0]（precision=1.00）
- Jade (Mortal Kombat): SFT 引了 5 句 [0-4]（precision=0.20），RSFT 精准 [0]（precision=1.00）

**Group 2 — GRPO catastrophic forgetting（2 例）：**
- Something to Believe In: 35 个预测，0 个正确。模型输出 "is a" 等非 DocRED 标准关系
- Józef Piłsudski Monument: 28 个预测，0 个正确。模型输出 "honor"、"location" 等自由格式关系

**Group 3 — EDCR 对比（2 例）：**
- Low EDCR（faithful）: "date of birth"（EDCR=0.12），Dieter Eppler 文档，预测 evidence=[0,1] 与 gold 完全匹配
- High EDCR（distractor-heavy）: "notable work"（EDCR=0.94），Across the Black Waters 文档，预测引 [0] 但 gold 是 [3]，100% distractor

---
