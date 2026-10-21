# data topic anchored benign v2

**DisPeD: A Controlled Study of Encoder Adaptation for Multi-Turn Jailbreak Detection** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_data_topic-anchored-benign-v2_20260517T184004_result.json`
- **Structured JSON:** [`e88c756f68dcc52d95c0.json`](../../sessions/e8/e88c756f68dcc52d95c0.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

全部完成。结果总结：

**Generation**: 250/250 成功，0 失败，avg 16.02 turns，source=`qwen3-8b-topic-anchored-v2`

**TF-IDF HARD GATE: FAIL** (F1=1.0000)
- A-type escalation markers: 0
- B-type style confounds: 1
- V2 修复了 V1 的 request-marker 不对称问题（benign 现在有 "could you"、"how to"、"want to"）
- 但新的分离来源是 **formality gap**：benign user simulator 生成过于正式/结构化的请求语言，jailbreak user simulator 使用 casual/informal 风格（"just"、"hey"、"what if"、"really"、"like"）
- V3 需要匹配 register/formality，让 benign conversations 也使用 casual 口语风格

结果已保存至：
- `results/topic_anchored_v2_tfidf.json`（TF-IDF 详细数据）
- `results/topic_anchored_v2_results.json`（完整结果 + 分析）

---
