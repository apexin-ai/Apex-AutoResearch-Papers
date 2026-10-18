# debug ner recall denominator

**How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?** · Task result records

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 1
- **Recorded user turns:** 0
- **Tool calls:** 0
- **Original source:** `logs/workers/worker_debug_ner-recall-denominator_20260516T223223_result.json`
- **Structured JSON:** [`7411bd42f7791f4c5348.json`](../../sessions/74/7411bd42f7791f4c5348.json)

## Before a recorded user message

1 recorded events

### Task result

_source line 1_

## 调试结论

### 分母 Bug 假设：**排除**

关键代码 `src/evaluate.py:79`：
```python
gold_entities = [e for e in samples[sid]["entities"] if e["type"] in batch_types]
total_gold += len(gold_entities)
```

分母**已正确过滤到当前 batch schema 内的类型**，不存在分母 bug。

---

### U 型曲线是真实现象，不是 Bug

**数据汇总（text_match recall）：**

| count | mean_recall | gold/batch | std |
|-------|-------------|------------|-----|
| 2 | 0.527 | 92.6 | — |
| 6 | 0.390 | 239.6 | — |
| 12 | 0.306 | 428.8 | — |
| **22** | **0.268** | 876.4 | **0.103** |
| 44 | 0.301 | 1771.2 | — |
| **66** | **0.407** | 2652.0 | **0.002** |

**关键证据：**
1. count_66 = 全部 66 个 Few-NERD 类型（完整 schema），25 个 batch 完全相同，recall 方差接近 0（0.0017）
2. count_22 的 25 个 batch 各不相同，recall 范围 [0.113, 0.444]，方差极大
3. FewRel（classification accuracy）无 U 型，严格单调递减（0.870 → 0.504）

**解释：**
- **低 count（2-6）**：聚焦任务，少量类型 → 高 recall
- **中 count（12-22）**：schema 变长、需区分多类型 → recall 下降
- **高 count（44-66）**：接近 / 等于全集。count_66 时模型无需做类型筛选判断（文本中所有实体都在 schema 内）→ 更激进地提取 → recall 回升

这本质上是 **extraction vs. classification 的行为差异**：partial schema 要求模型同时做两件事（识别实体 + 判断是否属于 schema 内类型），full schema 只需做识别。

---

### FewRel 无此问题

FewRel 是 closed-set classification（从 N 选 1），accuracy 单调递减，符合预期。

---

### 是否需要重跑？

**不需要。** 评估逻辑正确。如果论文中需要展示 "count 增加 → 性能下降" 的叙事：
- FewRel 数据直接支持
- Few-NERD 需解释 U 型：在 partial schema 下 recall 确实下降（count_2→22），但 full schema 是特殊点（无需类型过滤），应在图中标注或从 count curve 分析中排除 count_66 点，或将其单独讨论为 "full-schema baseline"

---
