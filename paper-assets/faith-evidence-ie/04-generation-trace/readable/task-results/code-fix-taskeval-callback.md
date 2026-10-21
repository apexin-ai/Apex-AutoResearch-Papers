# code fix taskeval callback

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_fix-taskeval-callback_20260515T094121_result.json`
- **Structured JSON:** [`cb6998b3216eec2d6ae6.json`](../../sessions/cb/cb6998b3216eec2d6ae6.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复完成。

**修改位置**: `prepare_eval_data` 函数，第 117-120 行

**修改前**:
```python
gold = gold_from_docred(dev_data)
```

**修改后**:
```python
all_gold = gold_from_docred(dev_data)
# Filter gold to match eval_max_docs subset; using full dev gold inflates the denominator
eval_doc_ids = {item["doc_id"] for item in eval_items}
gold = [g for g in all_gold if g["doc_id"] in eval_doc_ids]
```

**逻辑差异**: 之前 `gold` 包含全量 dev set 的 12275 条 triples，但推理只在前 N 个 doc 上执行，F1 分母被严重膨胀。修复后 `gold` 只保留被评估的 N 个 doc 对应的 triples，分子分母对齐。

---
