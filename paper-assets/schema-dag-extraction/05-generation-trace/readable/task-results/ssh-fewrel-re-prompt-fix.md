# ssh fewrel re prompt fix

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_ssh_fewrel-re-prompt-fix_20260515T065836_result.json`
- **Structured JSON:** [`2c9ce6c646370484a362.json`](../../sessions/2c/2c9ce6c646370484a362.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

验证通过。

**修改摘要:**

在 `src/run_extraction.py` 第 135-168 行插入两个函数：

- **`build_json_schema_re(relation_types)`** (line 138) — 返回 RE 任务的 JSON schema，输出格式 `{"relation": "&lt;type>"}`，enum 约束为 `sorted(relation_types) + ["none"]`
- **`build_prompt_v2_re(sentence, head, tail, relation_defs, relation_types)`** (line 151) — RE 分类 prompt，匹配 `run_fewrel_pilot.py` 和 `run_extraction.py` 中的 5 参数调用签名

**Import 测试结果:**
```
Schema: {'type': 'object', 'properties': {'relation': {'type': 'string', 'enum': ['nationality', 'place_of_birth', 'none']}}, 'required': ['relation']}
Prompt: Given the following sentence and two entities, classify the relation between them.

Sentence: "Obama was born in Honolulu."
Head entity: "Obama"
Tail entity: "Honolulu"

Candidate relations: nationality, place_of_birth

Output a single JSON object: {"relation": "&lt;relation_type>"}
If none of the candidate relations apply, output: {"relation": "none"}
OK
```

---
