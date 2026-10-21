# ssh exp3a analysis pipeline

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_exp3a-analysis-pipeline_20260515T050851_result.json`
- **Structured JSON:** [`08058c49a32ca8941778.json`](../../sessions/08/08058c49a32ca8941778.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。产出已注册为 `art_20260515_799e91`。

**GO。** v2 prompt 去掉 offset 要求并加入 "Only extract entities that clearly match" 后：

- **Over-prediction 大幅下降**：P/G ratio 全线降 50-70%（count_1: 6.85→2.97）
- **BCS-quality 相关性增强**：partial r(F1,BCS|count) 0.303→0.400 (p=0.003)；partial r(recall,BCS|count) 从不显著变显著 (p=0.043)；count_12 recall-BCS 从 FAIL 翻转为 PASS (0.222→0.524)
- **低 count F1 提升**：count_1 +59%, count_2 +100%, count_6 +77%
- **代价**：recall 全线降 20-45%，高 count (22-64) F1 降 16-21%
- **Error taxonomy**：低 count 以 spurious 为主 (98%)，高 count wrong_type 升至 55%，支持 "confusability 驱动 type substitution" 的叙事

---
