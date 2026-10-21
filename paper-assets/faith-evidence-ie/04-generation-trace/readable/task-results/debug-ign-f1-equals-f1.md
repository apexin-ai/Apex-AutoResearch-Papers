# debug ign f1 equals f1

**Evidence at What Cost? Decoupling and Scaling in LLM-Based Document Relation Extraction** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_ign_f1_equals_f1_20260515T234533_result.json`
- **Structured JSON:** [`55146aebfbd7b42d3964.json`](../../sessions/55/55146aebfbd7b42d3964.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

**All 18 eval results have F1 = Ign-F1.** Bug confirmed across every experiment.

## 根因

`evaluator.py` 的 `_triple_key` 函数将 `doc_id`（即文档 title）作为 key 的一部分：

```python
def _triple_key(doc_id, head, tail, relation):
    return (doc_id, head.lower().strip(), tail.lower().strip(), relation.lower().strip())
```

而 DocRED 的 train 和 dev 文档集**完全不重叠**（verified: 0 overlapping titles among 3053 train + 998 dev docs）。因此 `pred_set - self.train_triples` 永远等于 `pred_set`（没有任何 dev triple 的 doc_id 出现在 train triples 中），导致 Ign-F1 ≡ F1。

DocRED 的 Ign-F1 语义是排除**知识级别**重复的关系事实（即 `(head_entity, relation, tail_entity)` 同时出现在 train 和 dev 中，不论文档），不应包含 doc_id。

## 修复方案

`_triple_key` 和 `from_train_file` 中的 train_triples 构建需要区分两种 key：

1. **F1 计算**（含 doc_id，当前逻辑正确）：用于 pred vs gold 匹配，因为同一实体对在不同文档中的关系标注独立计算
2. **Ign 过滤**（不含 doc_id）：用于判断一个 `(head, tail, relation)` 事实是否在训练集出现过

具体改动：
- `from_train_file` 额外构建一个 `train_facts: set[tuple]`，key 为 `(head, tail, relation)` 不含 doc_id
- `compute_f1` 中 Ign 过滤改为：对 `pred_set` / `gold_set` 中每个 triple，检查其 `(head, tail, relation)` 部分是否在 `train_facts` 中，是则排除

## 影响范围

所有 18 个已完成 eval 的 `ign_f1` 值全部错误（等于 `f1`）。修复后需要**重新计算所有 Ign-F1**——好消息是不需要重跑推理，只需从已有的 `predictions.json` 重新调用修复后的 evaluator 即可。

---
