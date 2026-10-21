# code verify taskeval fix

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_code_verify-taskeval-fix_20260515T102826_result.json`
- **Structured JSON:** [`eee1cdaf7ecdbc6c8294.json`](../../sessions/ee/eee1cdaf7ecdbc6c8294.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

修复已应用。关键变更在第 118-120 行：

```python
# 第117行: all_gold = gold_from_docred(dev_data)
# 第118行: # Filter gold to match eval_max_docs subset
# 第120行: gold = [g for g in all_gold if g["doc_id"] in eval_doc_ids]
```

原来直接用 `all_gold`（全部 12275 个 gold triples）作为 F1 分母，现在过滤为 `eval_doc_ids` 子集对应的 gold triples。第 193 行 `self.evaluator.evaluate(all_predictions, self.gold)` 使用的是过滤后的 `gold`，分母正确。

**结论：bug fix 已部署，代码位置 `rsft_trainer.py:118-120`。**

---
