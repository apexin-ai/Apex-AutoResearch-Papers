# ssh maven preprocess

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_maven-preprocess_20260515T033306_result.json`
- **Structured JSON:** [`b2c1e242b0d9c8b9407e.json`](../../sessions/b2/b2c1e242b0d9c8b9407e.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

完成。结果：

- **valid split**: 710 docs → 8042 sentences, 18904 event mentions
- **168 种事件类型**
- 输出: `/root/schema-dag-extraction/data/maven_parquet/valid.parquet`
- 列: `doc_id`, `sent_id`, `text`, `tokens`, `entities`, `negative_triggers`
- 脚本: `/root/schema-dag-extraction/src/preprocess_maven.py`

每行一个句子，`entities` 是 `[{"text", "type", "start", "end"}]` 格式，`negative_triggers` 也一并保留了。

---
